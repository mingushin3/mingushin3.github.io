# 13_Content Lock v1 — 개체 간 변이(IIV/BSV)와 공변량 모델링

**Source lock**: R&T 5e Ch.12–13 (p.361–410); G&W 5e Ch.4 (p.333–352) + PK50 (p.704–710)  
**Output scope**: §1 → §2 → §5 → §7 → §8  
**Length control**: Step 1 Draft v0보다 짧게 압축함.  
**Figure policy**: Audit T6 Figure Inventory는 본 문서에서 판정하지 않고 Phase 4C로 이월.

---

## Updated Curation Map — Content Lock v1

| Tier | Card | 최종 판정 | Source anchor |
|---|---|---|---|
| MUST | **C1. 변이의 구조적 분해 — θ, η, ε / ω², σ²** | **RETAIN + APEX 보강**. 이 세션의 중심축으로 승격. ω²과 σ²의 “분산 보존/경쟁” 직관을 삽입. | R&T p.369–373; G&W p.335–336, p.704–708 |
| MUST | **C2. 잔차 오차 모델 — additive / proportional / exponential** | **RETAIN, shrinkage는 후속 구현 지식으로 격하**. Mixed RUV와 NONMEM `W` coding은 `[교과서 외 구현 번역]` 라벨을 붙임. | R&T p.371–373 |
| MUST | **C3. 공변량 모델링 — CrCl, fu, 식별성** | **RETAIN + 정정**. “fu가 ω²를 28%→9% 줄였다”가 아니라, PK50이 total Cl CV 28%와 unbound Clu CV 9%를 같은 12명 자료의 다른 좌표계로 제시한 것으로 수정. | R&T p.369–371; G&W p.704–710 |
| MUST | **C4. 유전적 다형성 — IIV 안의 불연속 substructure** | **RETAIN + source-lock**. PM 빈도와 예시는 표준 교과서 값만 유지; HLA-B*5701 빈도, 현대 FDA label count, unsupported phenotype frequency table 삭제. | R&T p.393–410 |
| CONTEXT | Spaghetti plot, NAD/NPD, population approach | C1 안에 1문단으로 압축. | G&W p.334–336; R&T p.369 |
| CONTEXT | OFV/LRT/AIC | C1 말미에 2문장으로 유지. | R&T p.373 |
| CONTEXT | EDA “plot before equations” | C1 앞부분에 source-anchored bridge로 삽입. | G&W p.334–335 |
| CONTEXT | Ethnicity caution | C4 limitations에 1문장으로 삽입. | R&T p.395, p.409 |
| EXCLUDED | Lineweaver–Burke, Scatchard, Euler integration | 분산 축이 아니라 모델 적합/수치해석 축이므로 제외. | G&W p.340–352 |

**Curation verdict**: 4개 MUST 카드 유지. C2의 제목과 무게중심은 “shrinkage diagnostic”에서 “residual error model”로 되돌리고, C1을 실질 Apex로 재배치한다.

---

## Adjudication Table Summary

| Source | Item | Verdict | Rationale |
|---|---|---|---|
| Audit T1 | Source range: R&T p.361–410; G&W p.333–352, p.704–710 | ADOPT | 첨부 PDF 범위와 일치. |
| Audit T1 | NLME master equation | PARTIAL_ADOPT | 개념은 R&T mixed-effects 설명과 부합하지만 식 자체는 PDF에 인쇄되지 않아 `[교과서 외 구현/통계 번역]`으로 표시. |
| Audit T1 | θ/η/ε, fixed/random/residual taxonomy | ADOPT | R&T population analysis가 fixed effects, IIV/IOV/residual variability를 직접 설명. |
| Audit T1 | `$THETA/$OMEGA/$SIGMA` control-stream syntax | PARTIAL_ADOPT | 교육적으로 필요하나 교과서 직접 내용이 아니므로 `[교과서 외 구현 번역]` 표시. |
| Audit T1 | Exponential IIV, `CL_i = CL·exp(η)` | ADOPT | R&T p.371에 근거. |
| Audit T1 | `CV(%) ≈ omega × 100` | PARTIAL_ADOPT | 작은 ω에서의 교육용 근사로만 표시. |
| Audit T1 | Additive/proportional/exponential residual error | ADOPT | R&T p.371–373 직접 근거. |
| Audit T1 | Mixed residual model / NONMEM `W` implementation | PARTIAL_ADOPT | PDF 밖 실무 구현이므로 source-derived로 부르지 않음. |
| Audit T1 | Shrinkage formula, thresholds, Savic & Karlsson 2009 | REJECT/PARTIAL_ADOPT | 수식·임계값은 삭제; shrinkage는 후속 GOF/EBE 세션 pointer로만 유지. |
| Audit T1 | FDA deficiency letter, 21 CFR, cost/time/probability claims | REJECT | 첨부 PDF에 없음. |
| Audit T1 | OFV, LRT ΔOFV 3.84, AIC | ADOPT | R&T p.373 직접 근거. |
| Audit T1 | PK50 dose/regimen, total concentration safety threshold | ADOPT | CpD 566 µg/5 h/12명 및 total C >50 µg·L⁻¹ 회피는 G&W p.704–705, p.709 근거. |
| Audit T1 | PK50 Table 50.1 total/unbound parameters | ADOPT | G&W p.708 직접 근거. |
| Audit T1 | `fu = 0.016 ± 0.0049` and `CLu ≈ 720 L/h` | ADOPT | G&W p.708 및 산술 변환과 일치. |
| Audit T1 | Variance propagation equation validating CV reduction | REJECT | PDF에 없고 산술도 성립하지 않음. |
| Audit T1 | “fu covariate reduces ω²(CL) 28%→9%” | REJECT/REPLACE | “total Cl CV 28%, unbound Clu CV 9%”라는 source-exact statement로 교체. |
| Audit T1 | PK50 PD response variability, EC50/Emax/n | ADOPT | G&W p.707–709, Table 50.2 근거. |
| Audit T1 | Warfarin, nortriptyline, midazolam/alfentanil, S-warfarin examples | ADOPT | R&T p.362–364 근거; 필요한 예시만 압축 유지. |
| Audit T1 | CYP2D6/2C9/2C19, TPMT, NAT2, UGT1A1 frequencies | ADOPT | Table 13-1 source-locked 값만 유지. |
| Audit T1 | HLA-B*5701 frequency, FDA biomarker label count | REJECT | 첨부 PDF 밖 현대 규제 정보. |
| Audit T1 | PM/IM/EM/UM detailed frequency table | REJECT/PARTIAL_ADOPT | source-supported PM frequency와 qualitative phenotype만 유지. |
| Audit T2/T3 | “Plot first; do not rush into equations” | ADOPT | G&W Ch.4 author message를 C1 bridge로 삽입. |
| Audit T2/T3 | PK vs PD variability separation | ADOPT | R&T p.363–364와 PK50 p.707–709에 근거하여 C3/C4에 명시. |
| Audit T2/T3 | Ethnicity as imperfect proxy | ADOPT | R&T p.395, p.409 caution을 C4 limitations에 삽입. |
| Audit T4 | MUST_FIX 1–8 | ADOPT | 모두 본문에서 삭제, 라벨링, 또는 source-exact wording으로 치환. |
| Audit T4 | SHOULD_FIX 9–13 | ADOPT/PARTIAL_ADOPT | 정확 수치가 불확실한 항목은 qualitative로 압축. |
| Audit T4 | OPTIONAL 14–16 | PARTIAL_ADOPT | Table 13-4 logic만 C4에서 1문장; 나머지는 제외. |
| Audit T4 | REJECT 17–18 | REJECT | Scope creep 및 source 밖 modernization. |
| Crucible Grade A | A1 ω²/σ² 보존 법칙 | ADOPT | C1 structural necessity에 삽입. |
| Crucible Grade A | A2 ETA 위치 tip for fu | ADOPT | C3 NONMEM 구현 번역 직후 삽입. |
| Crucible Grade A | A3 phenotype level 통합 tip | ADOPT | C4 구현 번역 직후 삽입. |
| Crucible Grade A | A4 Pair 2 Critical Blow 이동 | PARTIAL_ADOPT | “label reissue” 표현은 삭제하고 total/unbound 좌표계 정합 문제로 재작성. |
| Crucible Grade A | A5 sparse + shrinkage tip | PARTIAL_ADOPT | shrinkage는 외부 후속 지식으로 1문장만 유지. |
| Crucible Grade A | A6 deletion list 8개 | ADOPT | STS row, Bayesian row, C2 exponential row 중복, Q8 prepared statement 등 삭제/압축. |
| Crucible Grade B | B1 fu reparameterization | ADOPT | C3 및 §5 Pair 2 핵심 문장으로 반영. |
| Crucible Grade B | B2 PD source intuition | ADOPT | §7 Q5 정답에 반영. |
| Crucible Grade B | B3 GOF signatures | REJECT | §6/Phase 4C 영역이므로 본 산출물 범위 밖. |
| Crucible Grade B | B4 NDA Section consistency | PARTIAL_ADOPT | 특정 section 번호 없이 “regulatory PopPK report consistency”로 일반화. |
| Crucible Grade C | C1–C6 | REJECT | Figure pointer, `$MIX`, Bayesian TDM 수식, individual fu table, phenotype method, Euler/Scatchard는 모두 범위 밖. |

---

## §1 — Session Header & Roadmap

**Session 13 — 개체 간 변이 (IIV / BSV)와 공변량 모델링**  
*Source: R&T 5e Ch.12 (p.361–392) + Ch.13 (p.393–410); G&W 5e Ch.4 일부 (p.333–352) + PK50 (p.704–710)*

<!-- MASTER LENS -->
### Big Idea

NONMEM mixed-effects model의 본질은 관측값을 **θ(인구 평균), η(개체 deviation), ε(잔차 noise)** 로 분해하고, 그 분산인 **ω²와 σ²** 를 따로 추정하는 것이다. 공변량은 ω² 안에 섞여 있던 생리학적 원인을 꺼내는 도구이고, 유전 다형성은 매끄러워 보이는 ω² 안에 숨어 있는 불연속 봉우리다. `[R&T p.369–373; p.393–410]`

G&W는 이론보다 먼저 데이터의 모양을 보라고 한다. 즉, 공변량 모델은 control stream에서 시작하지 않고, spaghetti plot·dose-normalized plot·transformed plot에서 “어떤 개체들이 왜 갈라지는가”를 먼저 보는 데서 시작한다. `[G&W p.334–336]`

### Roadmap

```text
C1. θ / η / ε taxonomy
     ↓
C2. residual error model: ε의 형태를 정한다
     ↓
C3. covariate model: ω² 일부를 설명 가능한 생리학으로 옮긴다
     ↓
C4. genetic polymorphism: ω² 안의 불연속 substructure를 드러낸다
```

### Knowledge Graph Position

| 위치 | 내용 |
|---|---|
| 선행 전제 | 1-·2-compartment model, Cl/V/t½, protein binding, NONMEM 기초 syntax |
| 본 세션 | IIV/IOV/RUV, θ/η/ε, ω²/σ², covariate, genotype/phenotype variability |
| 직후 후속 | FOCE/FOCE-I, GOF/CWRES/η-EBE, shrinkage, stepwise covariate selection |
| 임상 번역 | Bayesian TDM, dose individualization, therapeutic window, PopPK report consistency |

<!-- RECAP -->
**§1 recap**: 이 세션의 질문은 “사람마다 다르다”가 아니다. 질문은 “그 다름 중 무엇이 θ, 무엇이 η, 무엇이 ε, 무엇이 covariate인가”이다.

---

## §2 — Concept Anatomy Cards

---

### C1. 변이의 구조적 분해 — θ, η, ε taxonomy

<!-- MASTER LENS -->
**개념 Big Idea**

θ는 인구의 무게중심, η는 각 개인이 그 중심에서 벗어난 정도, ε는 같은 개인을 같은 조건에서 다시 측정해도 남는 잔차다. 이 세 자리가 분리되지 않으면 `$OMEGA`와 `$SIGMA`는 숫자는 있어도 의미가 없다. `[R&T p.369–373]`

#### A. Formal Definition

`[교과서 외 구현/통계 번역; 개념 근거: R&T p.369–373]`

$$
Y_{ij}=f(\boldsymbol{\theta},\boldsymbol{\eta_i},x_{ij})+g(\boldsymbol{\theta},\boldsymbol{\eta_i},x_{ij})\varepsilon_{ij}
$$

- **θ**: fixed effect, population typical value.
- **ηᵢ**: interindividual deviation; variance-covariance matrix가 **Ω**, diagonal element가 **ω²**.
- **εᵢⱼ**: residual deviation; variance가 **Σ/σ²**.

개인 clearance의 source-anchored exponential IIV:

$$
CL_i = CL\cdot \exp(\eta_i)
$$

R&T는 exponential error model이 CL을 음수로 만들지 않고 approximate constant CV를 제공하기 때문에 population analysis에서 자주 쓰인다고 설명한다. `[R&T p.371]` 작은 ω에서는 `CV(%) ≈ ω × 100`을 교육용 근사로 쓸 수 있다.

#### B. Data Anchor: 평균보다 분포가 먼저다

R&T는 warfarin 200명에서 유사한 anticoagulation을 얻기 위한 daily dose가 넓게 분포하고, nortriptyline 25 mg tid를 복용한 263명에서 plateau concentration이 linear scale에서는 skewed, log scale에서는 거의 symmetric하다고 제시한다. 평균만 보는 순간 dose individualization의 문제는 사라지는 것이 아니라 숨겨진다. `[R&T p.362–363]`

G&W는 다중 피험자 자료에서 먼저 개별 profile과 pooled data를 그려 보라고 한다. Figure 4.2의 spaghetti plot은 같은 dose를 받은 Japanese와 Caucasian group이 서로 다른 exposure profile을 보일 수 있음을 보여 주며, 저자들은 mean curve with error bars보다 spaghetti plot이 variability를 더 잘 드러낸다고 설명한다. `[G&W p.335–336]`

<!-- ANCHOR -->
**NAD/NPD/population bridge**: Naive Averaged Data(NAD)는 각 time point의 평균 농도에 모델을 맞추고, Naive Pooled Data(NPD)는 모든 관측값을 한 개인처럼 적합한다. G&W는 mean data fitting이 편향된 parameter와 variability를 만들 수 있어 피해야 하며, 대안으로 population approach가 필요하다고 설명한다. `[G&W p.335–336]`

#### C. Structural Necessity

1. **θ alone is not enough**: 평균 clearance만 있으면 “일반 환자”의 농도는 예측하지만, narrow therapeutic window에서 독성 또는 무효 노출을 겪을 개인을 설명하지 못한다. `[R&T p.370]`
2. **ω² and σ² compete for the same unexplained variability**: 잔차 모델이 설명하지 못한 분산은 ω²로 새고, 반대로 개인 간 변이를 너무 크게 허용하면 σ²가 작아 보일 수 있다. 이 보존 법칙을 보지 못하면 C2와 C3는 모두 잘못된다.
3. **Population analysis is simultaneous**: R&T는 standard two-stage가 rich sampling을 요구하는 반면, population analysis는 sparse data를 합쳐 structural parameter와 variance parameter를 동시에 최적화한다고 설명한다. `[R&T p.369]`
4. **OFV는 적합의 언어다**: maximum likelihood는 θ, ω, σ를 동시에 조정하여 OFV를 최소화한다. Nested model에서는 ΔOFV 3.84(df=1, α=0.05)가 LRT 기준이고, non-nested model에서는 AIC가 쓰인다. `[R&T p.373]`

#### D. Boundary Conditions

| Boundary | Failure signature |
|---|---|
| η distribution이 unimodal/log-normal이어야 함 | bimodal histogram이면 genotype/phenotype subgroup 가능성. `[R&T p.366, p.393–397]` |
| ε가 mean 0, variance σ²의 random residual이어야 함 | residual trend가 남으면 structural/error model이 variability source를 설명하지 못한 것. `[R&T p.372]` |
| Sparse data도 같은 population에서 왔다고 볼 수 있어야 함 | outlier population이 섞이면 population mean과 ω²이 모두 왜곡. |
| Covariate가 식별 가능해야 함 | G&W의 identifiability/estimability 문제처럼, 데이터가 정보를 주지 않으면 파라미터는 숫자로만 존재한다. `[G&W p.348–351]` |

#### E. Zettelkasten Atom

```yaml
aliases: [IIV, BSV, NLME taxonomy, theta-eta-epsilon]
tags: [pharmacometrics/poppk, nonmem/omega, statistics/nlme]
source: "R&T p.369-373; G&W p.335-336; G&W PK50 p.704-708"
```

<!-- RECAP -->
**C1 recap**: θ는 중심, η는 개인의 위치, ε는 남은 흔들림이다. C2는 ε의 형태를 정하고, C3는 η 안의 설명 가능한 부분을 꺼내며, C4는 η 분포가 매끄럽지 않을 때의 생물학적 이유를 찾는다.

---

### C2. 잔차 오차 모델 — additive / proportional / exponential

<!-- MASTER LENS -->
**개념 Big Idea**

Residual error model은 “assay와 observation process가 어떤 방식으로 틀리는가”에 대한 선언이다. ε를 잘못 선언하면, 실제로는 측정/잔차 구조의 문제인 것이 ω² 또는 covariate 효과처럼 보인다. `[R&T p.371–373]`

#### A. Formal Definition

R&T가 제시하는 residual variability model은 다음 세 가지다. `[R&T p.372]`

| Model | Equation | Interpretation |
|---|---|---|
| Additive | $Y = F + \varepsilon$ | 절대오차가 농도와 무관하게 거의 일정. |
| Proportional | $Y = F(1+\varepsilon)$ | 상대오차/CV가 농도 범위 전반에서 거의 일정. |
| Exponential | $Y = F\exp(\varepsilon)$ | 양수 보장; log-domain에서 additive error가 됨. |

Log transformation 후 exponential error는 다음과 같이 additive form이 된다. `[R&T p.373]`

$$
\ln Y = \ln F + \varepsilon
$$

`[교과서 외 구현 번역]` Combined/mixed residual model은 실무 NONMEM에서 자주 쓰이지만, R&T p.372가 직접 열거한 source model은 additive/proportional/exponential이다. 따라서 combined model은 source-derived가 아니라 구현 번역으로만 둔다.

#### B. Code Structure

```nmtran
; [교과서 외 구현 번역]
$ERROR
IPRED = F
W     = SQRT((THETA(3)*IPRED)**2 + THETA(4)**2)
Y     = IPRED + W*EPS(1)
```

이 코드는 proportional component와 additive component를 하나의 `W`로 합친 구현이다. 그러나 source-locked 본문에서 중요한 점은 코드가 아니라 **잔차가 random, mean zero, variance σ²이어야 한다**는 R&T의 조건이다. `[R&T p.372]`

#### C. Structural Necessity

<!-- ANCHOR -->
잔차 모델은 covariate selection보다 앞선다. 예를 들어 high concentration에서 residual spread가 커지는 자료에 additive error만 쓰면, 모델은 그 확산을 설명하기 위해 ω²를 키우거나 가짜 covariate를 찾는다. 반대로 LLOQ 근처 절대오차가 큰 자료에 proportional error만 쓰면 low concentration residual pattern이 systematic하게 남는다.

R&T는 residual variability가 완전히 random이어야 하며, 그렇지 않으면 structural model 또는 error model이 중요한 variability source를 설명하지 못한 것이라고 명시한다. `[R&T p.372]`

#### D. Boundary Conditions

| Situation | Preferred thinking |
|---|---|
| Concentration range가 좁고 assay SD가 거의 일정 | Additive model 검토. |
| 넓은 concentration range와 constant CV assay | Proportional 또는 exponential model 검토. |
| 여러 order of magnitude의 자료 | ln-transform과 transformed error model을 함께 생각. `[R&T p.373; G&W p.337–339]` |
| Residual trend가 남음 | covariate를 넣기 전 structural/error model부터 재검토. |

#### E. Limitations

- Shrinkage formula, 20–30% threshold, Savic & Karlsson 2009는 이 PDF 범위에 없다. 본 세션에서는 `[교과서 외 후속 구현 지식]`으로만 남긴다.
- Sparse sampling에서 η-EBE와 residual plot을 해석할 때는, low shrinkage/normal-looking η histogram을 좋은 모델의 증거로 단정하지 않는다. 데이터가 EBE를 실제로 식별할 수 있었는지 먼저 묻는다.

<!-- TRENCH -->
**Trench-Level Tip**: C2에서 한 가지를 외운다면 “ε의 실패는 η의 성공처럼 보인다”이다. Residual model을 틀리면 covariate model은 정교해지는 것이 아니라 정교하게 틀린다.

#### F. Zettelkasten Atom

```yaml
aliases: [RUV, residual error, sigma, additive error, proportional error]
tags: [pharmacometrics/nonmem, statistics/residuals]
source: "R&T p.371-373; G&W p.337-339"
```

<!-- RECAP -->
**C2 recap**: ε는 남는 오차가 아니라 observation process의 모델이다. ε가 잘못되면 ω²과 covariate가 모두 오염된다.

---

### C3. 공변량 모델링 — CrCl, fu, and reparameterization

<!-- MASTER LENS -->
**개념 Big Idea**

Covariate modeling은 ω²을 “줄이는 기술”이 아니라, ω² 안에 섞인 생리학을 분리해 이름을 붙이는 작업이다. R&T의 creatinine clearance 예시는 renal clearance의 생리학을 CL_i에 연결하고, G&W PK50은 protein binding `fu`가 total parameter variability의 일부를 설명함을 보여 준다. `[R&T p.369–371; G&W p.706–709]`

#### A. Formal Definition

R&T는 creatinine clearance가 renal clearance의 interindividual difference를 설명하는 covariate가 될 수 있다고 설명한다. 예시 구조는 다음과 같다. `[R&T p.369–371]`

$$
CL_i = \theta_1 + \theta_2\cdot GFR_i + \eta_i
$$

또는 NONMEM 구현에서는 흔히 다음과 같은 centered covariate form을 쓴다.

```nmtran
; [교과서 외 구현 번역]
CL = THETA(1) * (CRCL/90)**THETA(2) * EXP(ETA(1))
```

여기서 covariate가 설명한 부분은 θ 구조로 이동하고, 설명되지 않은 개인 간 차이만 η에 남는다.

#### B. PK50 Anchor: fu는 “ω² reduction”이 아니라 좌표계 변환이다

G&W PK50에서 12명 환자는 CpD 566 µg을 5시간 IV infusion으로 받았고, total concentration과 unbound concentration이 함께 해석되었다. Plasma protein binding data인 `fu`는 total disposition parameter로부터 unbound parameter를 derive하는 데 사용되었다. `[G&W p.704–707]`

| Parameter | Total estimate (CV%) | Unbound estimate (CV%) |
|---|---:|---:|
| Cl | 11.4 L·h⁻¹ (28%) | 720 L·h⁻¹ (9%) |
| Cld | 4.35 L·h⁻¹ (39%) | 265 L·h⁻¹ (33%) |
| Vc | 19.9 L (29%) | 1270 L (18%) |
| Vt | 30.9 L (35%) | 2030 L (51%) |

`[G&W p.708, Table 50.1]`

Source-exact interpretation: **PK50은 total Cl CV 28%와 unbound Clu CV 9%를 보고한다.** 이는 NONMEM covariate model이 ω²(CL)을 28%에서 9%로 “깎았다”는 뜻이 아니라, 같은 12명 자료를 total coordinate와 unbound coordinate로 다시 표현했을 때 variability가 다르게 보인다는 뜻이다. `fu = 0.016 ± 0.0049`였으므로 protein binding variability가 total concentration/parameter variability의 일부를 설명한다. `[G&W p.708–709]`

<!-- TRENCH -->
**Trench-Level Tip — ETA 위치**: `fu`가 deterministic reparameterization이면 `CL = fu * CLu`의 좌표계 변환으로 처리한다. 반대로 population covariate model로 쓸 때는 `CLu`에 남길 η와 `fu` measurement variability를 분리해야 한다. 두 경우를 섞으면 ETA가 physiology가 아니라 accounting error를 흡수한다.

#### C. PK vs PD variability separation

PK50의 결정적 메시지는 protein binding이 모든 variability를 설명하지 않는다는 점이다. CpD는 비슷한 exposure에서도 response가 8배(0.5–4.0 response units)까지 달랐고, unbound concentration을 사용해도 EC50 variability는 오히려 커졌다. 저자들은 Emax < 1인 non-responder가 genetic makeup/receptor density와 관련된다고 해석했다. `[G&W p.707–709]`

R&T도 plasma concentration과 response를 함께 측정해야 PK variability와 PD variability를 구분할 수 있다고 한다. `[R&T p.363–364]` 따라서 covariate가 PK parameter variability를 설명했다고 해서 response variability까지 설명했다고 보면 안 된다.

#### D. Structural Necessity

- Covariate는 **η를 없애는 변수**가 아니라 **η 안의 설명 가능한 구성요소를 θ 구조로 옮기는 변수**다.
- Covariate 도입 전에는 G&W식 EDA가 선행되어야 한다: individual profile, pooled data, dose normalization, transformation으로 subgroup 또는 trend를 먼저 본다. `[G&W p.334–336]`
- Identifiability가 없는 covariate는 이름만 생리학적일 뿐 모델 안에서는 또 다른 noise source가 된다. `[G&W p.348–351]`

#### E. Limitations

- Variance propagation 식 `CV(CL)^2 ≈ CV(fu)^2 + CV(CLu)^2`는 본 문서에서 삭제한다. PDF에 없고, 독립성 가정 및 산술 검증도 성립하지 않는다.
- Total concentration safety threshold와 unbound concentration individualization은 서로 다른 coordinate system이다. G&W는 total C >50 µg·L⁻¹을 피하라고 하면서, variability 있는 protein binding을 고려해 safety margin은 total보다 unbound concentration 기반이 낫다고 결론낸다. `[G&W p.705, p.709]`

#### F. Zettelkasten Atom

```yaml
aliases: [covariate model, creatinine clearance, protein binding, fu, reparameterization]
tags: [pharmacometrics/covariate, pk/protein-binding, nonmem/eta]
source: "R&T p.369-371; G&W PK50 p.704-710"
```

<!-- RECAP -->
**C3 recap**: covariate는 ω²을 마술처럼 줄이지 않는다. 좌표계를 바꾸거나 physiology를 θ 구조로 옮겨서, 남은 η가 진짜 unexplained variability에 가까워지게 한다.

---

### C4. 유전적 다형성 — IIV의 불연속 substructure

<!-- MASTER LENS -->
**개념 Big Idea**

C1–C3은 η를 대개 smooth, log-normal distribution으로 다룬다. 그러나 pharmacogenetics는 η가 실제로는 PM/IM/EM/UM 또는 responder/non-responder 같은 불연속 subpopulation의 합일 수 있음을 보여 준다. `[R&T p.393–410]`

#### A. Formal Definition

R&T는 genetic polymorphism을 population 안에서 inherited phenotype이 polymodal distribution을 만들 수 있는 현상으로 다룬다. Inherited trait는 다른 variability source와 달리 평생 지속되는 개인 특성이라는 점이 핵심이다. `[R&T p.393]`

Hardy-Weinberg logic은 NAT2 acetylator 예시에서 제시된다.

$$
p^2 + 2pq + q^2 = 1
$$

R&T는 slow acetylator가 recessive homozygote일 때, allele frequency로 heterozygous/homozygous fast acetylator frequency를 계산하는 방식을 설명한다. `[R&T p.402]`

#### B. Source-Locked Genetic Examples

| Example | Source-locked point | Modeling implication |
|---|---|---|
| Nortriptyline twins | identical twins의 intrapair variability가 fraternal twins보다 작아 genetics가 PK variability에 크게 기여. `[R&T p.394]` | “unexplained η” 안에 inherited component가 있을 수 있음. |
| CYP2D6 / nortriptyline | functional CYP2D6 gene copy 수가 많을수록 clearance가 커지고 exposure가 낮아짐. `[R&T p.397]` | η(CL)이 smooth가 아니라 gene-copy category로 갈라질 수 있음. |
| CYP2C9 / warfarin | CYP2C9 mutation이 S-warfarin metabolism과 dose variability에 기여. `[R&T p.398, p.406]` | PK genotype + PD genotype(VKORC1)을 동시에 고려해야 함. |
| Codeine | CYP2D6-mediated morphine formation은 minor pathway라도 potent metabolite 때문에 clinically important. `[R&T p.399, p.404]` | Parent drug clearance만 보면 toxic/active metabolite risk를 놓침. |
| TPMT / thiopurines | TPMT polymorphism은 thiopurine dose와 toxicity에 큰 영향. `[R&T p.400]` | Poor metabolizer subgroup은 평균 dose로 다룰 수 없음. |
| NAT2 / isoniazid | 483명에서 6-h isoniazid concentration의 bimodal distribution. `[R&T p.402]` | Bimodal η distribution의 canonical example. |
| VKORC1 / warfarin | CYP2C9, VKORC1, age/body weight 등이 warfarin dose variance를 나누어 설명. `[R&T p.406]` | Single covariate determinism 금지. |

Table 13-1의 poor metabolizer frequency는 source value만 유지한다: CYP2D6 PM은 Caucasians 5–10%, African Americans 3.8%, Asians 0.9%; CYP2C9 PM은 Caucasians 1%; CYP2C19 PM은 Caucasians 3–5%, Asians 16%; TPMT deficient는 Caucasians 0.3%, Asians 0.04%; NAT2 slow acetylator는 Caucasians/African Americans 60%, Asians 10–20%; UGT1A1 poor metabolizer status는 Caucasians 11%, Asians 1–3%. `[R&T p.395]`

#### C. Code Structure

```nmtran
; [교과서 외 구현 번역]
IF (CYP2D6PM.EQ.1) THEN
  CL = THETA(1) * THETA(2) * EXP(ETA(1))
ELSE
  CL = THETA(1) * EXP(ETA(1))
ENDIF
```

<!-- TRENCH -->
**Trench-Level Tip — phenotype level 통합**: categorical covariate는 level별 sample size가 충분하지 않으면 THETA factor가 ETA에 흡수된다. PM n=3 같은 빈 셀에서는 “효과 없음”이 아니라 “효과를 식별할 정보가 없음”일 수 있다.

#### D. Structural Necessity

- Mean과 variance뿐 아니라 **distribution shape**가 중요하다. R&T의 hypothetical clearance distribution에서 bimodal distribution은 평균이 치료적으로 거의 무의미할 수 있음을 보여 준다. `[R&T p.366]`
- Genetic polymorphism은 η histogram의 “두 봉우리”를 physiology로 번역한다.
- R&T는 ethnicity가 genetic characteristic의 proxy일 뿐이며, within-group variability도 클 수 있다고 경고한다. 따라서 ethnicity covariate를 genotype처럼 해석하면 안 된다. `[R&T p.395, p.409]`
- CYP3A4처럼 큰 variability가 있어도 명확한 genetic factor가 드러나지 않는 경우가 있다. 모든 큰 ω²이 genotype peak를 뜻하지는 않는다. `[R&T p.399, p.410]`

#### E. Limitations

- HLA-B*5701 frequency, modern FDA pharmacogenomic label count, detailed PM/IM/EM/UM frequency table은 이 PDF 범위 밖이므로 삭제한다.
- Pharmacogenetics는 강력하지만 완결된 설명이 아니다. R&T는 genotype 외에도 demographics, adherence 등 다른 요인이 optimal dosing에 필요하다고 마무리한다. `[R&T p.409]`

#### F. Zettelkasten Atom

```yaml
aliases: [pharmacogenetics, genetic polymorphism, CYP2D6, CYP2C9, NAT2, TPMT, VKORC1]
tags: [pharmacometrics/iiv, pharmacogenomics, nonmem/categorical-covariate]
source: "R&T p.393-410"
```

<!-- RECAP -->
**C4 recap**: 유전 다형성은 covariate 목록이 아니라 η 분포의 모양을 바꾸는 생물학이다. Smooth log-normal assumption이 깨지는 순간, 평균 dose는 subgroup toxicity 또는 inefficacy를 숨긴다.

---

## §5 — Confusion Pair Dissection

<!-- CONFUSION -->
### Pair 1. ω²(IIV) vs σ²(RUV)

| 구분 | ω² / η | σ² / ε |
|---|---|---|
| 질문 | 사람마다 얼마나 다른가? | 같은 사람의 관측값이 예측에서 얼마나 벗어나는가? |
| 위치 | `$OMEGA`, individual parameter | `$SIGMA`, residual model |
| Source anchor | R&T p.369–371 | R&T p.371–373 |
| 흔한 오류 | assay error를 IIV로 해석 | true IIV를 residual noise로 묻음 |

**Critical distinction**: ω²과 σ²은 같은 총 unexplained variability를 두고 경쟁한다. 잔차 모델을 틀리면 covariate가 보이거나 사라지는 것이 아니라, 분산이 잘못된 그릇으로 이동한다.

<!-- CONFUSION -->
### Pair 2. Total Cl vs Unbound Clu — PK50 anchored

| 구분 | Total coordinate | Unbound coordinate |
|---|---|---|
| 무엇을 봄 | total concentration/parameter | free concentration/parameter |
| PK50 value | Cl 11.4 L·h⁻¹, CV 28% | Clu 720 L·h⁻¹, CV 9% |
| Interpretation | protein binding variability가 섞임 | fu로 재표현된 disposition |
| Source | G&W p.708 | G&W p.708 |

**Corrected Critical Blow**: PK50은 “fu covariate가 ω²을 줄였다”가 아니라, same 12 subjects를 total과 unbound coordinate로 비교했을 때 variability 해석이 달라짐을 보여 준다. Dose/safety 판단에서 total C >50 µg·L⁻¹ 회피 기준과 unbound-based safety margin이 혼동되면, exposure-response 해석의 좌표계가 불일치한다. `[G&W p.705, p.709]`

<!-- CONFUSION -->
### Pair 3. PK variability vs PD variability

PK variability는 concentration-time profile이 왜 다른가를 묻고, PD variability는 같은 exposure에서 response가 왜 다른가를 묻는다. R&T는 plasma concentration measurement가 PK와 PD variability를 분리하는 전제라고 한다. `[R&T p.363–364]`

PK50에서 protein binding은 total concentration variability 일부를 설명했지만, response는 비슷한 exposure에서도 8배 차이를 보였다. 이것은 covariate 하나가 모든 variability를 설명한다는 사고가 왜 위험한지 보여 주는 핵심 예다. `[G&W p.707–709]`

<!-- CONFUSION -->
### Pair 4. Mean distribution vs shape distribution

R&T의 nortriptyline 예시는 log-normal distribution을, hypothetical clearance distribution은 bimodal distribution에서 평균이 치료적 대표값이 되기 어렵다는 점을 보여 준다. `[R&T p.363, p.366]` 평균과 CV만 보고 η distribution의 shape를 확인하지 않으면, C4의 genetic subgroup을 놓친다.

<!-- RECAP -->
**§5 recap**: 이 세션의 혼동은 거의 모두 “어느 좌표계의 변이인가”로 귀결된다 — individual vs residual, total vs unbound, PK vs PD, mean vs shape.

---

## §7 — Self-Test: Active Recall Module

<!-- SELF-TEST -->
### Q1. `CL_i = CL·exp(η_i)`를 쓰는 가장 직접적인 이유는 무엇인가?

**Answer**: CL이 음수가 되지 않도록 보장하면서, η를 normal distribution으로 둘 수 있기 때문이다. R&T는 exponential error model이 approximate constant CV를 제공하고 computational difficulty를 줄인다고 설명한다. `[R&T p.371]`

<!-- SELF-TEST -->
### Q2. Residual variability가 random mean zero가 아니면 무엇을 뜻하는가?

**Answer**: structural model 또는 error model이 아직 중요한 variability source를 설명하지 못했다는 뜻이다. 이 상태에서 covariate를 찾으면, covariate가 biology가 아니라 residual misspecification을 설명할 수 있다. `[R&T p.372]`

<!-- SELF-TEST -->
### Q3. PK50에서 “total Cl CV 28%, unbound Clu CV 9%”를 어떻게 해석해야 하는가?

**Answer**: `fu`를 covariate로 넣어 ω²을 28%에서 9%로 줄였다는 뜻이 아니다. 같은 12명 CpD data를 total coordinate와 unbound coordinate로 표현했을 때, protein binding variability가 total parameter variability의 일부를 설명한다는 뜻이다. `[G&W p.706–709]`

<!-- SELF-TEST -->
### Q4. `CV(CL)^2 ≈ CV(fu)^2 + CV(CLu)^2`를 이 문서에서 쓰지 않는 이유는 무엇인가?

**Answer**: 이 variance propagation 식은 첨부 PDF에 없고, 독립성 가정도 제시되지 않았으며, Audit에서 산술적으로도 검증되지 않는다고 판정되었다. 따라서 source-locked Content Lock에서는 삭제한다.

<!-- SELF-TEST -->
### Q5. PK50에서 unbound concentration을 써도 PD variability가 남은 이유는 무엇인가?

**Answer**: protein binding은 PK coordinate의 variability 일부를 설명하지만, response variability는 receptor density/genetic makeup 같은 PD source를 포함한다. G&W는 Emax <1인 non-responder가 full target expression을 결여한 것으로 해석한다. `[G&W p.707–709]`

<!-- SELF-TEST -->
### Q6. η-EBE histogram이 두 봉우리로 보이면 가장 먼저 무엇을 의심해야 하는가?

**Answer**: smooth log-normal IIV 하나가 아니라, genotype/phenotype subgroup 또는 mixture-like population structure가 섞였는지 의심해야 한다. 단, sparse sampling이면 histogram 자체의 정보량을 먼저 점검해야 한다. `[R&T p.366, p.393–397]`

<!-- SELF-TEST -->
### Q7. Ethnicity covariate를 genotype처럼 해석하면 왜 위험한가?

**Answer**: R&T는 ethnicity가 individual genetic characteristics의 불완전한 proxy이며, within-group variability도 크다고 경고한다. Ethnicity term은 exploratory covariate일 수 있지만 mechanistic genotype의 대체물은 아니다. `[R&T p.395, p.409]`

<!-- SELF-TEST -->
### Q8. 다음 중 먼저 고칠 것은 무엇인가: residual model misspecification vs covariate model 추가?

**Answer**: residual model misspecification을 먼저 고친다. ε의 구조가 틀린 상태에서 covariate를 추가하면 ω²과 σ²의 경쟁이 왜곡되어, biology가 아니라 error model의 실패를 covariate가 설명하게 된다. `[R&T p.371–373]`

<!-- RECAP -->
**§7 recap**: 시험 문제의 정답은 대부분 “source of variability를 잘못된 그릇에 넣지 말라”이다.

---

## §8 — Meta-Frame & Big Picture

### A. Positioning — 28-session architecture

이 세션은 PopPK curriculum의 **variance axis**다. 이전 세션들이 Cl, V, ka, t½ 같은 structural parameter의 평균을 세웠다면, 이 세션은 그 평균 주변의 개인차와 잔차를 분해한다. 이후 FOCE/FOCE-I, GOF, covariate selection, Bayesian TDM은 모두 이 분해 위에서만 의미가 있다.

### B. Dependencies — 대충 넘겼을 때 발생하는 실패 모드

| Dependency | 대충 넘기면 생기는 실패 |
|---|---|
| C1 θ/η/ε | `$OMEGA`와 `$SIGMA`를 숫자로만 읽고, physiology vs residual noise를 구분하지 못함. |
| C2 residual error | 잘못된 ε가 ω²로 새어 가짜 IIV 또는 가짜 covariate를 만듦. |
| C3 covariate/reparameterization | `fu`, CrCl, body weight를 모두 같은 방식의 covariate로 취급해 좌표계 변환과 causal predictor를 혼동. |
| C4 genetic polymorphism | bimodal distribution을 single log-normal η로 덮어 subgroup dose risk를 숨김. |
| EDA-first | spaghetti plot과 transformed plot 없이 control stream부터 쓰다가 subgroup signal을 놓침. `[G&W p.334–336]` |
| Regulatory PopPK consistency | θ, ω², σ², residual model, covariate effect가 서로 맞지 않으면 report table은 있어도 dose rationale이 무너짐. `[R&T p.373]` |

### C. Professional Moat — 이 세션이 전문가를 가르는 지점

초급자는 “IIV가 큽니다”라고 말한다. 중급자는 “CL에 covariate를 넣겠습니다”라고 말한다. 전문가의 질문은 다르다.

1. 이 변이는 **PK인가 PD인가**? `[R&T p.363–364; G&W p.707–709]`
2. 이 변이는 **η인가 ε인가**? `[R&T p.369–373]`
3. 이 변이는 **total coordinate에서만 보이는가, unbound coordinate에서도 남는가**? `[G&W p.706–709]`
4. 이 변이는 **smooth distribution인가, subgroup/phenotype structure인가**? `[R&T p.366, p.393–410]`
5. 이 covariate는 **생리학인가, proxy인가, 또는 식별 불가능한 accounting device인가**? `[G&W p.348–351; R&T p.395]`

<!-- RECAP -->
### Final Recap

Session 13의 최종 메시지는 하나다. **ω²은 “남은 변이”가 아니라 아직 이름 붙이지 못한 생리학·유전학·행동·측정 구조의 혼합물이다.** C2는 residual noise를 정리하고, C3는 설명 가능한 physiology를 꺼내며, C4는 smooth IIV 안에 숨어 있는 genetic discontinuity를 드러낸다. 이 순서를 지키지 않으면 NONMEM은 돌아가지만, dose individualization은 성립하지 않는다.

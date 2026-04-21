먼저 실라버스와 Step 2 프롬프트를 확인하고, Step 1 내용에 주석/부연설명을 추가할 최적 포인트를 파악하겠습니다.충분히 파악했습니다. 이제 10개 핵심 포인트에 주석/부연설명을 추가한 **최종 교정 + 주석 강화판 Step 1**을 출력합니다. 추가된 주석은 `💡`, `⚠️`, `📌` 마커로 명확히 구분됩니다.

---

# II-03 STEP 1 완료판 (주석 강화 버전)

---

## 장인 시각의 비판적 검토 — 기존 초안 v2.0 대비 발견된 결함

기존 초안의 구조와 커버리지는 우수하나, **5가지 수정 필수 항목**이 있다:

| # | 유형 | 구체적 결함 | 심각도 |
|---|---|---|---|
| ① | **치명적 수치 오류** | Plausible Fallacy에서 "V2=50L 기준 50,000배 과소추정" → 실제 계산: IPRED_잘못/IPRED_올바른 = V2/1000 = 50/1000 = **1/20배 = 20배 과소추정**. 50,000배는 수학적으로 불가능 | ★★★ |
| ② | **PIPET Table 4.5 오기 미식별** | PIPET Table 4.5 (p.53)에서 ADVAN3의 CMT를 "1=Depot"으로 표기 — IV 2구획 모델에 Depot이 있을 수 없음. 실제는 Central=CMT1. 이 오기를 학습자가 그대로 흡수할 위험 | ★★★ |
| ③ | **PIPET vs Owen 교과서 불일치 미식별** | PIPET p.31: ".AND. 또는 .OR.을 사용하여 조건 결정 가능"이라고 기술. Owen p.33: "No other operator may be specified" (암묵적 OR만 허용). 이 충돌이 현장 혼란의 원천임에도 Draft에서 미언급 | ★★ |
| ④ | **$TABLE + $SIMULATION 레코드 공백** | Owen Ch.3 pp.57-64에 걸쳐 $SIMULATION, $TABLE, $SCATTERPLOT이 상세 기술되어 있으나 어느 카드에도 구체 코드/진단 지식이 없음. $TABLE의 sdtab/patab 번호 일치 규칙은 실무 직결 사항 | ★★ |
| ⑤ | **$MSFI 레코드 누락** | 장시간 추정 결과 저장·재활용 패턴($MSFI/$MSFO)은 Owen pp.61-62에 명시되어 있고 대형 PopPK 프로젝트 필수 지식이나 Card 4에 미수록 | ★ |

---

# §1 — 세션 헤더 & 로드맵

| 항목 | 내용 |
|---|---|
| **소스 1** | PIPET 한국어 교재, Ch.3 (pp.27–46), Ch.4 (pp.47–53), Ch.7 (pp.69–71) |
| **소스 2** | Owen, Introduction to PopPK/PD, Ch.3 (pp.28–64) |
| **세션 번호** | II-03 |
| **품질 플래그** | ⚠️ PIPET Table 4.5에 ADVAN3 CMT 오기 확인 → §2 카드 2에서 경고 처리 |

**Big Idea (한 문장):** NONMEM 제어구문 아키텍처는 "어떤 데이터로, 어떤 모델로, 어떤 오차 구조로, 어떤 알고리즘으로, 얼마나 믿을 수 있는가"에 대한 다섯 가지 질문에 코드로 대답하는 구조이며, 이 레이어 중 어느 하나라도 틀리면 나머지 모든 레이어의 결론이 오염된다.

**개념 항법도 (5개 카드):**

1. **NONMEM 3요소 + 제어구문 레코드 아키텍처 + $DATA 데이터 통제**
2. **⚡ Apex: 특수 ADVAN + TRANS 조합 — 구획 설계도·파라미터 언어·척도 통일**
3. **$ERROR 잔차 구조 심화 — 가법/비례/혼합/log-error/assay-specific**
4. **$ESTIMATION + $COVARIANCE + $TABLE + $SIMULATION — 추정·검증·출력 파이프라인**
5. **$PRED — PREDPP 없는 자유 코딩과 PD/QT 모델링**

**지식 그래프 위치:**
- **선행**: II-01 (θ·η·ε 3층), II-02 (ID/TIME/AMT/DV/MDV/CMT/EVID 데이터 변수)
- **후속**: II-04 ($DES ODE 심화), II-05 (초기추정값 전략), II-06 (OFV·LRT·FO/FOCE 이론), II-08 (공변량 분석), II-09b ($COV SE/RSE 심화)
- **결정적 의존 고급 도메인**: VPC 시뮬레이션($SIMULATION 패턴), NDA/IND 규제 제출($COV PRINT=E 필수), ICH E14 QTc-노출 분석($PRED 구현)

---

# §2 — 개념 해부 카드

---

## 카드 1: NONMEM 3요소 + 제어구문 레코드 + $DATA 데이터 통제

---

### ━━ [개념 Big Idea: 거장의 시각] ━━

**왜 치명적으로 중요한가:** 규제 제출용 PopPK 분석에서 "어제 사용한 데이터셋"과 "오늘 실행한 제어구문"이 정확히 동일한 대상자 집합을 분석했는지 ICH E9(R1) 수준에서 재현 가능하게 증명해야 하는데, $DATA의 IGNORE 조건이 암묵적 OR로 작동한다는 사실을 모르면 AND 배제를 의도한 코드가 전혀 다른 부분집합을 분석하고도 발견하지 못한다.

**체화해야 할 단 하나의 직관:** 제어구문은 NONMEM에게 보내는 "법률 계약서"다 — 어떤 데이터를 쓸 것인지($DATA), 어떤 모델을 쓸 것인지($SUBR/$PK), 어디서 시작할 것인지($THETA/$OMEGA/$SIGMA), 어떻게 실행할 것인지($ESTIMATION), 무엇을 출력할 것인지($TABLE). 계약서의 조항 하나가 모호하면 결과 전체의 법적 효력이 무너진다.

**이 직관을 머릿속에 박고 아래를 읽어라:** 레코드 순서는 선택이 아니라 NM-TRAN 파싱 의존성 사슬이며, 이 순서가 왜 불변인지를 이해하면 오류 메시지 없이도 구조적 결함을 예방할 수 있다.

---

**A. Formal Definition**

NONMEM 시스템은 세 구성요소로 이루어진다. **NM-TRAN**은 사용자 제어구문을 파싱하여 문법·형식 오류를 검사하고 NONMEM 실행 형태로 변환하는 번역기다. **PREDPP**는 집단약동학 분석을 위해 FORTRAN으로 구현된 표준 PK 구획 모델 서브루틴 라이브러리다. **NONMEM** 엔진은 비선형 혼합효과 모델의 목적함수(OFV) 최소화를 통한 파라미터 추정 알고리즘이다. NONMEM은 배치 모드로 실행되어 GUI 없이 ASCII 텍스트 제어구문으로만 작동한다. `[출처: Owen, Ch.3, pp.28-29]`

> 💡 **배치 모드란?** Excel처럼 실시간으로 결과를 클릭하며 확인하는 방식이 아니라, 제어구문 파일 하나를 던져 놓으면 NONMEM이 처음부터 끝까지 자동으로 실행하고 결과 파일을 남기는 방식이다. 따라서 코드 한 글자의 오류가 수 시간짜리 실행을 멈추게 만든다 — 방어적 코딩이 선택이 아닌 필수인 이유다.

---

**B. Derivation / Code Structure**

**제어구문 전체 구조 (파싱 의존성 사슬 순서):**

```nonmem
$PROBLEM 1-compartment model           ; ① 프로젝트 식별자 — 출력파일 제목행
$INPUT ID TIME AMT RATE DUR DV MDV    ; ② 데이터셋 열 순서 선언 (최대 50개)
       WT AGE SEX HT RF ALB CLCR      ;    초과분은 =DROP 처리
$DATA test.csv IGNORE=@               ; ③ 파일 경로 + 부분집합화
$SUBROUTINE ADVAN2 TRANS2             ; ④ 구획 구조 + 파라미터화 선택
$PK                                   ; ⑤ 고정효과 + IIV 정의
$ERROR                                ; ⑥ 잔차 구조 정의
$THETA / $OMEGA / $SIGMA              ; ⑦ 초기추정값 (분산값 입력 — SD 아님)
$ESTIMATION METHOD=1 INTER ...        ; ⑧ 추정 알고리즘
$COVARIANCE PRINT=E                   ; ⑨ 표준오차 + 고유값 출력
$TABLE ...                            ; ⑩ 출력 파일 제어
```

`[출처: PIPET, Ch.3, pp.27-30]` `[출처: Owen, Ch.3, pp.30-31]`

> 💡 **왜 이 순서가 불변인가?** NM-TRAN은 파일을 위에서 아래로 한 줄씩 읽으면서(sequential parsing) 각 레코드를 처리한다. $PK 블록에서 `WT`(체중)를 참조하려면 $INPUT에서 먼저 선언되어 있어야 한다. 마치 법원 판결문에서 "제3조에서 정의된 A에 따라 제7조를 적용한다"고 쓰면, 제3조가 앞에 있어야 제7조가 효력을 갖는 것과 같다. 순서 위반은 NM-TRAN 단계에서 즉시 컴파일 오류를 발생시킨다.

**⚠️ 교과서 불일치 경고 — IGNORE 다중 조건 AND/OR 처리:**

PIPET (p.31)은 ".AND. 또는 .OR.을 사용하여 조건 결정 가능"이라고 기술한다. 그러나 Owen (p.33)은 "if more than one conditional argument is used, **the conditions are assumed to be connected by an '.OR.' operator. No other operator may be specified with this option**"이라고 명확히 규정한다. **Owen이 옳다** — NONMEM 실행 엔진의 실제 동작은 암묵적 OR만 허용하며 .AND.를 명시해도 무시되거나 오류가 발생한다. PIPET의 해당 설명은 오기 또는 부정확한 기술이다.

```nonmem
; ✅ 올바른 이해 — 다중 조건은 암묵적 OR
$DATA test.csv IGNORE=(WTKG.GE.100, STDY.EQ.301)
; → "체중 ≥ 100kg OR 스터디 = 301"인 행 제외

; ✅ AND 배제 구현 — ACCEPT 역전환 (De Morgan 법칙)
; "체중 ≥ 100kg AND 스터디 = 301"인 행만 제외하려면:
$DATA test.csv ACCEPT=(WTKG.LT.100, STDY.NE.301)
; → "(체중 < 100kg) OR (스터디 ≠ 301)"인 행만 포함
; → NOT(체중 ≥ 100kg AND 스터디 = 301) = De Morgan 동치

; ✅ 문자 기반 IGNORE와 조건부 IGNORE 혼합
$DATA test.csv IGNORE=# IGNORE=(SEX.EQ.1)  ; 가능
; ❌ IGNORE=# + 조건부 ACCEPT 혼합        ; 불가 (Owen p.34)

; ✅ CHECKOUT 옵션 — 추정 없이 데이터 파싱 검증
$DATA test.csv IGNORE=# CHECKOUT
; 결과: $TABLE 파일 출력 가능, WRES 미계산, 빠른 데이터 품질 확인
```

`[출처: Owen, Ch.3, pp.33-35]`

> 📌 **De Morgan 변환 직관:** "AND 배제"를 NONMEM의 OR-only 구조로 바꾸는 열쇠다. 논리식으로 보면: NOT(A AND B) = NOT A OR NOT B. 실제 의미로 풀면: "A이면서 B인 사람을 제외"하고 싶다면 → "A가 아니거나, B가 아닌 사람만 포함(ACCEPT)"하면 된다. IGNORE → ACCEPT로 방향을 뒤집고, 조건 부호를 반전하는 것이 핵심이다.

> 💡 **CHECKOUT의 실용 가치:** 300명 데이터셋에서 IGNORE 조건이 의도대로 작동하는지 확인하려면 전체 추정(수 시간)을 기다릴 필요가 없다. CHECKOUT을 붙이면 수십 초 만에 $TABLE 파일이 나오고, 실제 포함된 행 수를 R에서 `nrow()`로 세어 확인할 수 있다.

---

**C. Structural Necessity**

레코드 순서가 불변인 이유: NM-TRAN이 위에서 아래로 순차 파싱한다. $PK에서 공변량 변수(WT, CLCR)를 참조하려면 $INPUT에서 먼저 선언되어야 컴파일 오류가 없다. $THETA/$OMEGA/$SIGMA는 $PK의 THETA(n)/ETA(n) 참조보다 뒤에 위치해도 NONMEM이 초기값을 제공하나, $ESTIMATION은 모델 정의 레코드가 모두 선언된 후 위치해야 한다. 순서 위반은 NM-TRAN 파싱 단계에서 즉시 오류를 발생시킨다.

---

**D. Assumptions & Boundary Conditions**

- $INPUT 변수 최대 50개. =DROP 처리된 변수도 IGNORE/ACCEPT 조건 평가에 사용 가능 (DROP 전에 조건 평가 수행)
- 제어구문 한 줄 최대 160자 (NONMEM 7 이상), 이전 버전은 80자
- NONMEM 7.2 이상: 대소문자 혼용 허용. 이전 버전: 전부 대문자 필수
- 탭(Tab) 문자 사용 회피 권장 — 버전별 파싱 오류 가능성 `[Owen p.30]`
- $DATA CHECKOUT 옵션: WRES 미계산이므로 $SCAT에 WRES 포함 불가

---

**E. Limitations**

- IGNORE/ACCEPT 최대 100개 조건 지정 가능하나 AND 연산은 직접 불가 → ACCEPT 역전환으로만 구현
- IGNORE=# + 조건부 ACCEPT 혼합은 허용되나, IGNORE=# + 조건부 IGNORE + 조건부 ACCEPT 삼중 혼합은 불가

---

**F. Five Cognitive Layers**

| 레이어 | 내용 |
|---|---|
| **L1 형식적 수학** | 제어구문은 $y_{ij} = f(\theta, \eta_i, t_{ij}) + g(\theta, \eta_i, t_{ij})\cdot\varepsilon_{ij}$ 를 5개 레코드 블록으로 분해: $f$ = $PK+구조모델, $g$ = $ERROR, $\theta$ = $THETA, $\eta$ = $OMEGA, $\varepsilon$ = $SIGMA |
| **L2 기하학적 직관** | IGNORE/ACCEPT = 파라미터 공간이 아닌 **데이터 공간의 부분집합화 필터** — 어떤 관측값을 OFV 계산에 포함할지를 결정 |
| **L3 구조적 동일성** | IGNORE OR 암묵 처리 = SQL의 `WHERE` 절. ACCEPT(NOT) 전환 = SQL의 `WHERE NOT (AND)` = De Morgan 변환. CHECKOUT = SQL의 `EXPLAIN` (실행 없이 파싱 검증) |
| **L4 생리학적 의미** | IGNORE로 제외한 집단(소아, 임산부, 투석 환자)은 최종 모델 기반 시뮬레이션의 외적 타당성 범위에서 자동 제외됨 — 규제 보고서에서 적용 가능 집단 명시 필수 |
| **L5 실무 투영** | FDATA 출력 파일로 실제 IGNORE 적용 여부를 반드시 검증. $TABLE의 sdtab/patab/catab/cotab 번호는 Xpose4 자동 인식 규칙 — 번호 불일치 시 `xpose.data()` 로딩 실패 |

---

**G. Zettelkasten Atom**

```yaml
---
aliases: [NM-TRAN 제어구문, NONMEM control stream, IGNORE ACCEPT, De Morgan]
tags: [pharmacometrics/nonmem, nonmem/coding/controlstream, nonmem/data]
up: "[[II-01 θ·η·ε 3층 계층 구조]]"
related: ["[[II-02 NONMEM 데이터셋]]", "[[II-04 General ADVAN DES]]"]
source: "PIPET, Ch.3, pp.27-46 / Owen, Ch.3, pp.28-64"
---
```

NONMEM 제어구문은 $PROB → $DATA/$INPUT → 모델블록 → $THETA/$OMEGA/$SIGMA → $ESTIMATION → $COV/$TABLE의 불변 순서를 따른다. $DATA IGNORE 다중 조건은 암묵적 OR이며 AND 배제는 ACCEPT 역전환(De Morgan)으로만 구현한다. PIPET p.31이 AND 연산 가능이라고 기술하나 Owen p.33의 "No other operator may be specified"가 엔진 동작의 정확한 기술이다.

---

## 카드 2: 특수 ADVAN + TRANS 조합 [⚡ Apex Concept]

---

### ━━ [개념 Big Idea: 거장의 시각] ━━

**왜 치명적으로 중요한가:** IV 2구획 모델(ADVAN3)을 경구 2구획 모델(ADVAN4)로 전환할 때 S-parameter 번호와 CMT 값을 동시에 수정하지 않으면, NONMEM은 오류 메시지 없이 실제보다 **V2/1000배 낮은 농도(V2=50L 기준 약 20배 과소추정)**를 예측하고 $COV step까지 성공시켜 IND 제출 직전까지 오류가 발견되지 않는다.

**체화해야 할 단 하나의 직관:** ADVAN은 "구획 설계도"이고, TRANS는 "그 설계도를 읽는 파라미터 언어"이며, S-parameter는 "설계도의 스케일 변환 법칙"이다 — 설계도(ADVAN)가 바뀌면 구획 번호 체계 전체가 재정의되므로 S-parameter도 반드시 새 설계도의 규칙을 따라야 한다.

**이 직관을 머릿속에 박고 아래를 읽어라:** ADVAN 번호가 홀수(1, 3, 11)면 IV 직접 투여 → 중심구획이 CMT1이고 S1 사용, 짝수(2, 4, 12)면 경구/피하 투여 → 저장구획이 CMT1, 중심구획이 CMT2이고 S2 사용.

---

**A. Formal Definition**

특수 ADVAN(specific ADVAN)은 PREDPP에 미리 구현된 표준 PK 구획 모델 서브루틴이다. $MODEL, $DES 없이 사용 가능하며 일반 ADVAN 대비 실행 속도가 빠르다. TRANS 서브루틴은 동일한 ADVAN 구조를 서로 다른 파라미터 세트(속도상수 vs CL/V)로 표현하는 재파라미터화 변환기다.

---

**B. Derivation / Code Structure**

**특수 ADVAN 선택 체계:**

| | IV 투여 | 경구/혈관 외 투여 |
|---|---|---|
| 1구획 선형 | ADVAN1 | ADVAN2 |
| 2구획 선형 | ADVAN3 | ADVAN4 |
| 3구획 선형 | ADVAN11 | ADVAN12 |
| 1구획 MM 비선형 | ADVAN10 | — |

`[출처: PIPET, Ch.4, p.47 표 4.1]`

> 📌 **홀짝 암기법:** 홀수(1, 3, 11) = 주사바늘이 혈관에 바로 꽂힌다(IV) → 투약과 동시에 약이 혈액(중심구획)에 들어가므로 중심구획이 첫 번째(CMT1). 짝수(2, 4, 12) = 입으로 삼킨다(경구) → 약이 먼저 위장(저장구획, Depot)에 들어가므로 Depot이 첫 번째(CMT1), 혈관은 두 번째(CMT2). **홀수=S1, 짝수=S2** — 이것만 외우면 S-parameter 번호 오류는 없다.

**⚠️ PIPET Table 4.5 오기 경고 — ADVAN3 CMT 번호:**

PIPET p.53 Table 4.5에서 ADVAN3의 CMT를 "1=Depot, 2=Peripheral, 3=Output"으로 표기하고 있으나, **이는 오기다.** ADVAN3은 정맥(IV) 2구획 모델이므로 Depot 구획이 존재하지 않는다. 올바른 CMT 배정은 아래 표를 따른다:

**CMT 번호 체계 (교정 버전):**

| ADVAN | CMT1 | CMT2 | CMT3 | CMT4 | 관찰 구획 | S-parameter |
|---|---|---|---|---|---|---|
| ADVAN1 | Central | Output | — | — | CMT1 | **S1** = V |
| ADVAN2 | **Depot** | Central | Output | — | CMT2 | **S2** = V |
| ADVAN3 | **Central** | Peripheral | Output | — | CMT1 | **S1** = V1 |
| ADVAN4 | **Depot** | Central | Peripheral | Output | CMT2 | **S2** = V2 |

`[출처: Owen, Ch.3, Table 3.2, pp.37]` ← PIPET Table 4.5의 ADVAN3 행은 오기로 Owen을 따를 것

> 💡 **투여 경로를 몸의 흐름으로 상상하라:**
> - **ADVAN3 (IV):** 주사 → 혈관(Central=CMT1) → 말초조직(Peripheral=CMT2). 단 두 구획, 가장 단순한 흐름.
> - **ADVAN4 (경구):** 입 → 위장(Depot=CMT1, 흡수 대기실) → 혈관(Central=CMT2) → 말초(Peripheral=CMT3). 경구 흡수라는 추가 단계가 Depot을 CMT1 자리에 밀어넣는다. 이 한 칸 밀림이 S1→S2, V1→V2 등 모든 번호 오프셋의 원인이다.

**ADVAN4 TRANS4 완전 코드:**

```nonmem
$SUBROUTINE ADVAN4 TRANS4

$PK
  TVCL = THETA(1)           ; 집단 청소율 (L/h)
  TVV2 = THETA(2)           ; 집단 중심구획 분포용적 (L)
  TVV3 = THETA(3)           ; 집단 말초구획 분포용적 (L)
  TVQ  = THETA(4)           ; 집단 구획간 청소율 (L/h)
  TVKA = THETA(5)           ; 집단 흡수속도상수 (1/h)

  CL = TVCL * EXP(ETA(1))   ; 로그정규 IIV — 양수 항상 보장
  V2 = TVV2 * EXP(ETA(2))
  V3 = TVV3 * EXP(ETA(3))
  Q  = TVQ  * EXP(ETA(4))
  KA = TVKA * EXP(ETA(5))

  ALAG1 = THETA(6) * EXP(ETA(6))   ; 흡수지연시간 (선택적, 저장구획=CMT1에 적용)

  S2 = V2/1000              ; dose(mg)/V(L) → Cp(ng/mL=µg/L) 단위 통일
                            ; TRANS4 내부: k10=CL/V2, k23=Q/V2, k32=Q/V3 자동 계산

  ; 출력용 사용자 정의 변수 (TRANS4 내부 예약변수 K 재정의 아님 — 별칭 출력용)
  KE  = CL/V2
  K23 = Q/V2
  K32 = Q/V3
```

`[출처: PIPET, Ch.3 코드 3.2, p.32]` `[출처: Owen, Ch.3, pp.36-41]`

**S-parameter 단위 통일 공식 (usv 방법):**

$$S_n = V \times \text{usv}, \quad \text{where} \quad \frac{\text{Amount}}{V \times \text{usv}} = \text{DV 단위}$$

dose(mg), V(L), Cp(ng/mL=µg/L)인 경우:

$$\frac{\text{mg}}{L \times \text{usv}} = \frac{\text{µg}}{L} \Rightarrow \text{usv} = \frac{1}{1000} \Rightarrow S2 = \frac{V2}{1000}$$

`[출처: Owen, Ch.3, Eq.3.6, p.41]`

> 💡 **S-parameter의 본질적 역할:** NONMEM 내부에서 농도는 항상 `Amount ÷ Sn`으로 계산된다. Sn이 없으면(기본값=1) `Amount(mg) ÷ 1 = mg`이 농도가 되어버린다. 실제 농도 단위(ng/mL)와의 1000배 불일치가 그대로 IPRED에 반영된다. S-parameter는 "모델이 계산하는 단위"와 "데이터의 DV 단위"를 일치시켜주는 변환 계수다 — 빠뜨리면 NONMEM은 오류 없이 틀린 스케일의 예측값을 내뱉는다.

**TRANS 선택 비교 (ADVAN4):**

| TRANS | 필수 파라미터 | 실무 권장 |
|---|---|---|
| TRANS1 | K, K23, K32, KA | 비권장 |
| TRANS3 | CL, V, Q, VSS, KA | VSS 직접 추정 필요 시 |
| **TRANS4** | **CL, V2, Q, V3, KA** | **권장 (임상 보고 표준)** |
| TRANS5 | AOB, ALPHA, BETA, KA | 거시 지수 파라미터 필요 시 |

`[출처: PIPET, Ch.4, p.49 표 4.2]`

---

**C. Structural Necessity**

TRANS4가 이 구조인 이유: $SUBROUTINES ADVAN4 TRANS4를 파싱하면 TRANS4는 $k_{10}=CL/V_2$, $k_{23}=Q/V_2$, $k_{32}=Q/V_3$를 자동 계산한다. 사용자가 이를 $PK에 다시 쓸 필요가 없으나, $TABLE 출력용으로 KE=CL/V2를 선언하는 것은 유효한 사용자 정의 출력 변수이며 PREDPP 내부 예약변수 K의 재정의가 아니다.

---

**[C-2 Plausible Fallacy — Apex Concept] ⚡**

**오류의 구체적 형태:** IV 2구획 모델(ADVAN3)이 수렴된 후 경구 투여 데이터 추가 시 $SUBROUTINES를 ADVAN4로 변경하면서 `S1 = V1`을 `S2 = V2`로 수정하지 않는 경우. "ADVAN만 바꾸면 나머지는 자동 처리되겠지"라는 직관에서 비롯된다.

**나비효과 — 수학적 추적 (수만 배가 아니다):**

ADVAN4에서 S2가 정의되지 않으면 NONMEM은 S2의 기본값으로 1을 사용한다. 이때:

$$\text{IPRED}_{\text{잘못}} = \frac{A(2)}{1}, \quad \text{IPRED}_{\text{올바른}} = \frac{A(2)}{V2/1000}$$

$$\text{오차 비율} = \frac{\text{IPRED}_{\text{잘못}}}{\text{IPRED}_{\text{올바른}}} = \frac{V2}{1000}$$

V2=50L이면: $50/1000 = 0.05$ → IPRED가 **정확값의 1/20배 = 20배 과소추정**. NONMEM은 이 체계적 오류를 보상하기 위해 $SIGMA를 폭발적으로 키우거나 $OMEGA를 비정상적으로 크게 추정하며, IPRED가 DV 대비 균일하게 수 자릿수 낮은 체계적 수직 편향이 나타난다.

**진단 GOF 시그니처: "S-parameter 망각 패턴"**
- DV vs IPRED plot: IPRED가 DV 대비 V2/1000배 (전형적으로 10~200배) 과소추정. 체계적이고 농도 범위 전반에 균일함
- SIGMA 또는 $OMEGA가 비정상적으로 큰 값으로 수렴 (이를 보상 시도)
- PARAMETER ESTIMATE IS NEAR ITS BOUNDARY 경고 다수 발생

**ADVAN3→ADVAN4 전환 필수 체크리스트:**

```nonmem
; BEFORE (ADVAN3 IV 2구획)      → AFTER (ADVAN4 경구 2구획)
$SUBR ADVAN3 TRANS4              $SUBR ADVAN4 TRANS4
$PK                              $PK
  CL = THETA(1)*EXP(ETA(1))       CL = THETA(1)*EXP(ETA(1))
  V1 = THETA(2)*EXP(ETA(2))  →   V2 = THETA(2)*EXP(ETA(2))   ; V1→V2
  V2 = THETA(3)*EXP(ETA(3))  →   V3 = THETA(3)*EXP(ETA(3))   ; V2→V3
  Q  = THETA(4)*EXP(ETA(4))       Q  = THETA(4)*EXP(ETA(4))
                              →   KA = THETA(5)*EXP(ETA(5))   ; KA 추가
  S1 = V1/1000               →   S2 = V2/1000                 ; S1→S2 ★핵심
; 데이터셋: 관찰 CMT=1        ; 데이터셋: 관찰 CMT=2 수정 필수  ★핵심
```

> ⚠️ **이 전환에서 동시에 수정해야 할 항목은 정확히 4가지다.** 하나라도 빠뜨리면 NONMEM은 에러 없이 잘못된 결과를 낸다: ① ADVAN 번호(3→4), ② S-parameter(S1→S2), ③ 파라미터 변수명(V1/V2→V2/V3, KA 추가), ④ 데이터셋 CMT 값(관찰 기록 CMT=1→2). 특히 ④는 제어구문 바깥(데이터셋 파일)에 있어 가장 놓치기 쉽다.

---

**D. Assumptions & Boundary Conditions**

- 특수 ADVAN: 구획 간 이동이 1차 속도상수를 따름 → 비선형 분포에는 부적합
- ADVAN10(MM 비선형 흡수)을 제외한 특수 ADVAN은 $DES 블록 사용 불가
- 데이터셋 CMT 값은 선택한 ADVAN의 구획 번호 체계와 반드시 일치 필수

---

**E. Limitations**

- 사전 정의된 구획 구조만 지원 → 장간순환, 모약물-대사체 동시 분석, 비선형 소실은 ADVAN6 필요
- TRANS4에서 VSS 직접 추정 불가 → VSS 필요 시 TRANS3 선택
- 실행 속도: 특수 ADVAN > 일반 선형(ADVAN5) > 일반 비선형(ADVAN6)

---

**F. Five Cognitive Layers**

| 레이어 | 내용 |
|---|---|
| **L1 형식적 수학** | ADVAN4 TRANS4 ODE: $\frac{dA_1}{dt}=-k_aA_1$, $\frac{dA_2}{dt}=k_aA_1-(k_{10}+k_{23})A_2+k_{32}A_3$, $\frac{dA_3}{dt}=k_{23}A_2-k_{32}A_3$. TRANS4 내부 변환: $k_{10}=CL/V_2$, $k_{23}=Q/V_2$, $k_{32}=Q/V_3$ |
| **L2 기하학적 직관** | log-Cp vs Time: 단일 직선→1구획, 두 기울기→2구획. α상의 가파름=말초 분포 속도, β상 기울기=k10. S-parameter 오류 시 곡선 형태는 유지되나 Y축 스케일이 V2/1000배 이동 |
| **L3 구조적 동일성** | ADVAN=전기회로 토폴로지, TRANS=임피던스 표현 방식, S-parameter=전압/전류 스케일 변환 계수 |
| **L4 생리학적 의미** | V2=혈액+혈관풍부조직(간, 신장), V3=근육·지방 등 말초. Q=조직 관류량 근사. ALAG1=위배출 지연 또는 장용정 코팅 시간 |
| **L5 실무 투영** | 전환 체크리스트 4항목: ① $SUBR 번호, ② S1→S2 (핵심), ③ V1/V2 변수명, ④ 데이터셋 CMT 값. FDATA 파일로 CMT 실제 분포 확인 필수 |

---

**G. Zettelkasten Atom**

```yaml
---
aliases: [특수 ADVAN, TRANS 서브루틴, 척도 파라미터, S-parameter, ADVAN3 ADVAN4 전환]
tags: [pharmacometrics/nonmem, nonmem/coding/advan, nonmem/traps, pipet-errata]
up: "[[II-03 제어구문 레코드 구조]]"
related: ["[[II-04 General ADVAN DES]]", "[[S2 단위 통일]]"]
source: "PIPET, Ch.3-4, pp.32-53 / Owen, Ch.3, pp.35-44"
errata: "PIPET Table 4.5 ADVAN3 CMT 번호 오기 — Owen Table 3.2를 따를 것"
---
```

홀수 ADVAN(1,3,11)은 IV→중심구획=CMT1→S1. 짝수 ADVAN(2,4,12)는 경구→저장=CMT1, 중심=CMT2→S2. ADVAN3→ADVAN4 전환 시 S-parameter 미수정 오류는 IPRED를 V2/1000배 과소추정하며 오류 메시지 없이 $COV step까지 성공한다. PIPET Table 4.5의 ADVAN3 CMT 표기(1=Depot)는 오기 — Owen Table 3.2(Central=CMT1)를 따를 것.

---

## 카드 3: $ERROR 잔차 구조 심화

---

### ━━ [개념 Big Idea: 거장의 시각] ━━

**왜 치명적으로 중요한가:** 3상 풀링 데이터에서 Phase 1(희소 샘플링, 저감도 분석법)과 Phase 3(밀집 샘플링, 고감도 분석법)을 하나의 잔차 구조로 모델링하면 FDA 심사관이 "분석법 차이를 무시한 모델"로 지적하고, $OMEGA가 과대추정되어 하위 그룹 시뮬레이션 전체가 오염된다.

**체화해야 할 단 하나의 직관:** $ERROR는 "측정 오차의 성격 + 분석법의 특성 + 데이터 이질성"을 동시에 모델링하는 공간이다 — 잔차가 농도와 무관하면 가법, 비례하면 CCV, 둘 다면 혼합, 분석법이 다르면 assay-specific으로 구조를 분리한다.

**이 직관을 머릿속에 박고 아래를 읽어라:** CWRES vs IPRED 플롯의 패턴이 $ERROR 구조 선택의 생리학적 지문이다 — 깔때기 모양이면 가법 오명세, 고농도 체계적 양편향이면 CCV 오명세.

---

**A. Formal Definition**

$ERROR 블록은 관찰값(DV)과 개인 예측값(F) 사이의 잔차 변이(residual variability, RV)를 기술한다. 잔차 변이는 측정 내 개인간변이(intraindividual variability), 분석 오차(assay error), 모델 오명세(model misspecification), 데이터 오차의 복합체다.

---

**B. Derivation / Code Structure**

**주요 잔차 구조:**

```nonmem
; 1. 가법(additive): 저농도, LLOQ 근처, 절대 오차 일정
$ERROR
  Y = F + EPS(1)                          ; Var(Y) = σ₁²

; 2. 비례(CCV): 고농도, 상대 오차 일정
$ERROR
  Y = F * (1 + EPS(1))                    ; Var(Y) = F²·σ₁², %CV = σ₁×100

; 3. 지수(exponential): 비례와 FO 근사 하 수학적 동치
$ERROR
  Y = F * EXP(EPS(1))

; 4. 혼합(additive + CCV): 전 농도 범위
$ERROR
  Y = F + EPS(1) + F*EPS(2)              ; Var(Y) = σ₁² + F²·σ₂²

; 5. W 함수 + SIGMA 1 FIX — 현장 표준 (SD/CV 직접 추정)
$ERROR
  IPRED = F
  W     = SQRT(THETA(3)**2 + THETA(4)**2 * IPRED**2)
  IRES  = DV - IPRED
  IWRES = IRES / W
  Y     = IPRED + W * EPS(1)
  ; THETA(3) = 가법 잔차 SD (농도 단위), THETA(4) = 비례 잔차 CV (무단위)
  ; SIGMA 1 FIX → W가 잔차 크기 완전 통제. THETA로 추정된 값이 직접 SD/CV
```

`[출처: PIPET, Ch.3, pp.35-37]` `[출처: Owen, Ch.3, pp.44-49]`

> 💡 **W함수 + $SIGMA 1 FIX 패턴이 현장 표준인 이유:** $SIGMA로 분산을 추정하면 결과를 보고서에 쓸 때 반드시 √를 취해 SD/CV로 변환해야 한다 (바로 아래 %CV 오류 참조). 반면 W함수 패턴에서는 THETA(3)이 이미 가법 SD(농도 단위), THETA(4)가 이미 비례 CV(무단위)로 추정되어 나온다 — 추가 변환 없이 보고서에 바로 쓸 수 있는 값이 나오는 것이다.

**%CV 도출 (Owen pp.52-53 기반):**

$Y = F(1+\varepsilon)$에서: $\text{Var}(Y) = F^2 \cdot \sigma_1^2$ → $SD(Y) = F \cdot \sigma_1$ → $\%CV = \sigma_1 \times 100$

따라서 $\$SIGMA\ 0.04 \Rightarrow \sigma_1 = \sqrt{0.04} = 0.2 \Rightarrow \%CV = 20\%$ (**4%가 아님!** `[출처: Owen, Ch.3, p.53]`)

> ⚠️ **이 계산 오류는 실제 FDA 보고서에서 반복 발생한다.** $SIGMA에 들어가는 숫자는 **분산(variance)**이다. 분산의 제곱근이 표준편차(SD)이고, 비례 모델에서 SD가 곧 %CV/100이다. 직관적 오류 경로: "0.04를 $SIGMA에 넣었으니 %CV=4%겠지" → 틀렸다. $\sqrt{0.04}=0.2 \rightarrow$ %CV=20%. **$SIGMA 값을 %CV로 오인하면 실제의 5배를 과소보고하게 된다.** 초기값 설정 방향으로 기억하면 더 쉽다: %CV 30%를 원하면 $SIGMA = $(0.3)^2$ = 0.09.

**Log-error 모델 — 방어 코딩 3가지 패턴:**

```nonmem
; 패턴 1: OBSERVATIONS ONLY (Owen 표준)
$ERROR (OBSERVATIONS ONLY)
  Y = LOG(F) + EPS(1)
  ; 투여 기록(EVID=1)에서 F=0 → LOG(0) 수학 오류 방지

; 패턴 2: CALLFL=0 (동일 효과)
$ERROR
  CALLFL = 0
  Y = LOG(F) + EPS(1)

; 패턴 3: FLAG 지시 변수 (가장 안전 — 극저농도 시간대 F≈0에도 대응)
$ERROR
  FLAG = 0
  IF (F.EQ.0) FLAG = 1
  Y = (1-FLAG)*LOG(F+FLAG) + EPS(1)
  ; ⚠️ FORTRAN에서 LOG()는 자연로그(ln), 상용로그는 LOG10()

; DV 열 전처리 ($INPUT에서)
$INPUT ID TIME AMT ODV=DROP DV=LNDV EVID MDV
; ODV=DROP: 원본 DV 열을 ODV로 rename 후 DROP
; DV=LNDV: 사전 ln 변환값 열을 DV로 사용
; (두 열 모두 DV로 명명 불가 — NONMEM 제약)
```

`[출처: Owen, Ch.3, pp.46-47]`

> 💡 **왜 투여 기록(EVID=1)에서 F=0이 되는가?** PREDPP는 투약 기록을 만나면 구획에 약물을 추가하는 사건(event)으로 처리하고, $ERROR는 그 시점에서 예측 농도(F)를 계산하게 된다. 그런데 투약 직후 흡수가 아직 일어나기 전이므로 F≈0이 나올 수 있다. LOG(0)은 수학적으로 -∞ → NONMEM이 즉시 중단된다. OBSERVATIONS ONLY 또는 FLAG 패턴은 "관찰 기록에서만 $ERROR를 실행하고 투여 기록은 건너뛰어라"는 지시다.

**Assay-specific 및 Phase-specific 잔차 구조:**

```nonmem
; 분석법별 잔차 분리 (ASAY=0/1 지시 변수)
$ERROR
  Y = F + F*EPS(1)*(1-ASAY) + F*EPS(2)*ASAY

; Phase별 잔차 분리
$ERROR
  P1 = 0; IF (STDY.LE.110) P1 = 1   ; Phase 1
  P3 = 0; IF (STDY.GE.300) P3 = 1   ; Phase 3
  Y = F + EPS(1)*P1 + F*EPS(2)*P1 + F*EPS(3)*(1-P1)*(1-P3) + F*EPS(4)*P3
  ; Phase 2: P1=0, P3=0 → Y = F + F*EPS(3)
```

`[출처: Owen, Ch.3, pp.47-48]`

---

**C. Structural Necessity**

EXP(ETA) IIV가 (1+ETA)보다 선호되는 구조적 이유: 지수 모델에서는 ETA가 어떤 극단적 음수값이어도 $CL_i = TVCL \cdot e^{\eta_i} > 0$이 항상 보장된다. 비례 모델에서 $\eta_i < -1$이면 $CL_i < 0$이 발생한다. FO 근사 하에서 두 모델은 수학적으로 동치이지만 FOCE에서는 지수 모델이 양수 제약을 구조적으로 강제하므로 권장된다. `[출처: Owen, Ch.3, p.42]`

---

**D. Assumptions & Boundary Conditions**

- $OMEGA/$SIGMA 초기값은 **분산(variance)** — SD 아님. W 함수 패턴에서만 THETA에 SD/CV 추정
- $OMEGA/$SIGMA에 0은 반드시 `0 FIX` 지정 필요 (단독 0은 불가)

---

**E. Limitations**

- 혼합 잔차의 THETA(가법)·THETA(비례) 동시 추정은 파라미터 상관 문제로 수렴 불안정 → 단계적 FIX 후 해제 전략 권장
- Log-error 모델에서 OBSERVATIONS ONLY/CALLFL=0 사용해도 극저농도 F≈0 관찰값은 여전히 수학 오류 가능 → FLAG 패턴이 가장 안전

---

**F. Five Cognitive Layers**

| 레이어 | 내용 |
|---|---|
| **L1 형식적 수학** | 비례 잔차 %CV: $Y=F(1+\varepsilon)$ → $\text{Var}(Y)=F^2\sigma^2$ → $SD(Y)/F=\sigma$ → $\%CV=\sigma\times100$. **$SIGMA=0.04 → %CV=20%, NOT 4%** |
| **L2 기하학적 직관** | CWRES vs IPRED: 깔때기(funnel)→가법 오명세, 역깔때기→CCV 오명세, 무작위→올바른 구조 |
| **L3 구조적 동일성** | W 함수 = 가중최소제곱(WLS)의 가중치 역수 — NONMEM은 IWRES=IRES/W를 최소화 |
| **L4 생리학적 의미** | 비례 오차 = LC-MS/MS의 신호대잡음비에서 기원. 가법 오차 = LLOQ 근처 배경 잡음. Assay-specific 분리는 기기 교체의 분석적 실재를 모델에 반영 |
| **L5 실무 투영** | FDA/EMA 심사관은 $SIGMA %CV 환산값을 확인. W함수 패턴의 THETA(3)=가법 SD, THETA(4)=비례 CV가 추가 계산 없이 직접 보고 가능 |

---

**G. Zettelkasten Atom**

```yaml
---
aliases: [$ERROR 블록, 잔차변이, 혼합 잔차, W함수, log-error, assay-specific, SIGMA %CV]
tags: [pharmacometrics/nonmem, nonmem/coding/error, residual-variability]
up: "[[II-03 특수 ADVAN TRANS]]"
related: ["[[II-06 추정 방법론 OFV]]", "[[CWRES GOF 진단 패턴]]"]
source: "PIPET, Ch.3, pp.35-37 / Owen, Ch.3, pp.44-53"
---
```

$ERROR의 잔차 구조는 가법/비례/혼합으로 선택하되, 분석법이 다른 데이터 풀링 시 ASAY 지시 변수로 EPS를 분리해야 한다. $SIGMA=0.04는 %CV=4%가 아니라 20%다. Log-error 모델에서는 LOG(0) 오류를 OBSERVATIONS ONLY, CALLFL=0, FLAG 패턴 중 하나로 반드시 방어해야 하며 FLAG 패턴이 가장 안전하다.

---

## 카드 4: $ESTIMATION + $COVARIANCE + $TABLE + $SIMULATION

---

### ━━ [개념 Big Idea: 거장의 시각] ━━

**왜 치명적으로 중요한가:** $ESTIMATION은 "최솟값을 어떤 경로로 탐색할 것인가"이고 $COVARIANCE는 "그 추정값을 얼마나 믿을 수 있는가"이며 $TABLE은 "결과를 어떤 형식으로 후속 분석 도구에 전달할 것인가"다 — 이 세 레코드의 옵션을 잘못 설정한 채 규제 제출하면 $COV 실패·Xpose 로딩 오류·심사관 Information Request가 동시에 발생한다.

**체화해야 할 단 하나의 직관:** $COV step 실패나 Condition number 폭발은 "분석이 끝났다"가 아니라 "모델 자체에 근본 문제가 있음을 수학이 경고하는 신호"다 — MAXEVAL=0으로 10분 투자하면 초기값 타당성을 확인하여 수 시간의 맹목적 재실행을 방지한다.

**이 직관을 머릿속에 박고 아래를 읽어라:** Condition number = OFV 계곡의 납작함 지표 — 1,000 초과는 "거의 동등한 파라미터 조합이 무수히 많다"는 수학적 경고다.

---

**A. Formal Definition**

$ESTIMATION 레코드는 OFV 최소화 알고리즘(METHOD), 최대 함수 평가 횟수(MAXEVAL), 수렴 유효자릿수(SIGDIGITS), 중간 출력 빈도(PRINT), 결과 저장(MSFO)을 제어한다. $COVARIANCE는 추정 후 분산-공분산 행렬을 계산하여 SE, RSE(%), 상관행렬, 고유값을 출력한다. $TABLE은 추정 결과를 외부 파일로 출력하여 Xpose4, R 등 후처리 도구에 전달한다. $SIMULATION은 추정된 최종 파라미터를 고정하여 가상 집단 데이터를 생성한다.

---

**B. Derivation / Code Structure**

**$ESTIMATION 핵심 옵션:**

```nonmem
$ESTIMATION NOABORT MAXEVAL=9999 METHOD=1 INTER PRINT=5 SIGDIGITS=3

; METHOD=0 (또는 POSTHOC): FO — 집단 평균(η=0)에서 테일러 전개, 빠르나 편향
; METHOD=1 (또는 COND): FOCE — 개인별 사후 ETA에서 전개, 표준
; METHOD=1 INTER (FOCEI): ETA-EPS 상호작용항 OFV에 보존, 현장 표준
; METHOD=1 LAPLACIAN: 2차 미분 사용, 범주형·TTE 데이터 필수
; NOABORT: Hessian 비양정치 시에도 추정 강제 지속 (PRDERR 파일 확인 필수)
; MAXEVAL=9999: 충분히 크게 설정 — 미지정 시 NONMEM이 자동 선택 (너무 작을 수 있음)
; PRINT=5: 5회 iteration마다 OFV, gradient, NPARAMETR 출력
; SIGDIGITS=3: 기본값. 2.9 달성 시 허용 가능. 더 큰 값 요구 시 다른 경로로 수렴 가능
```

`[출처: PIPET, Ch.3, p.37]` `[출처: Owen, Ch.3, pp.56-58]`

> 💡 **FO vs FOCE, 직관적으로:** FO는 "모든 환자가 집단 평균($\eta=0$)처럼 행동한다"는 가정에서 계산을 시작한다. FOCE는 각 환자의 개인 특성을 반영한 사후 ETA값에서 계산을 시작한다. 환자 간 변이가 클수록(예: 면역억제제처럼 %CV > 50%) FO의 "모두 평균처럼"이라는 가정은 더 큰 편향을 만들고, FOCEI가 더 정확하다. 현장에서 FOCEI가 표준인 이유가 여기에 있다.

| 방법 | 테일러 전개 기준점 | 개인별 추정 | 권장 상황 |
|---|---|---|---|
| FO (METHOD=0) | η=0 (집단 평균) | POSTHOC 별도 | 탐색적 초기 (규제 제출 비권장) |
| **FOCE (METHOD=1)** | **사후 η_i** | **동시 추정** | **현장 표준** |
| **FOCEI** | 사후 η_i | 동시 추정 + 상호작용 | **비례/혼합 잔차 시 강력 권장** |
| Laplacian | 2차 미분 | 동시 추정 | 범주형(logistic), TTE 분석 |

**MAXEVAL=0 진단 실행 — 초기값 검증의 핵심 도구:**

```nonmem
$ESTIMATION METHOD=1 INTER MAXEVAL=0
; 추정 없이 현재 초기값으로 PRED, IPRED만 계산
; → $TABLE 출력 후 R에서 DV vs PRED 겹쳐 그리기
; → 선이 데이터 위/아래 한참 벗어나면 초기값 조정 후 재실행
; → 수십 번 맹목적 재실행보다 이 한 번의 시각화가 훨씬 효율적
```

`[출처: Owen, Ch.3, p.58]`

> 💡 **MAXEVAL=0은 출항 전 해도(海圖) 확인이다.** 실제 추정(MAXEVAL=9999) 전에 현재 초기값이 데이터와 얼마나 동떨어져 있는지를 수십 초 만에 확인한다. IPRED가 DV 대비 10배 이상 틀려 있다면 초기값 자체가 잘못된 것이고, 그 상태에서 MAXEVAL=9999로 실행하면 수 시간을 소모하고도 "MINIMIZATION TERMINATED"가 나온다. MAXEVAL=0 한 번이 수 시간의 맹목적 재실행을 막는다.

**Gradient=0 진단 (0번째 iteration에서 확인 필수):**

THETA(n)의 gradient가 0번째 iteration에서 정확히 0이면 해당 파라미터가 OFV에 기여하는 정보가 없음 — 데이터에서 추정 자체가 불가능한 상황 (예: IGNORE로 특정 집단 제외 후 그 집단 공변량 효과 추정 시도). `[출처: Owen, Ch.3, p.59]`

**경계 경고와 NOTBT 옵션:**

```nonmem
; 경고: PARAMETER ESTIMATE IS NEAR ITS BOUNDARY
;       THIS MUST BE ADDRESSED BEFORE THE COVARIANCE STEP CAN BE IMPLEMENTED
; 발생 원인: 최종 추정값이 초기값과 100배 이상 차이 (+ 상관행렬 원소가 0 또는 1에 근접)
; → $COV step 자동 실패

; 탐색 목적으로만 억제 (규제 제출 모델에 잔류 금지):
$ESTIMATION METHOD=1 INTER NOTBT NOOBT NOSBT
; NOTBT = NOTHETABOUNDTEST
; NOOBT = NOOMEGABOUNDTEST
; NOSBT = NOSIGMABOUNDTEST
```

`[출처: Owen, Ch.3, pp.60-61]`

**$COVARIANCE 레코드:**

```nonmem
$COVARIANCE PRINT=E              ; 고유값(eigenvalue) 출력 → Condition number 계산
$COVARIANCE UNCONDITIONAL        ; 추정 성공 여부와 무관 $COV 강제 실행
$COVARIANCE MATRIX=S             ; S 행렬 사용 (범주형 DV 권장)
```

$$\text{Condition number} = \frac{\lambda_{\max}}{\lambda_{\min}}$$

| Condition number | 해석 |
|---|---|
| < 200 | 양호 |
| 200–1,000 | 주의 |
| **> 1,000** | **ill-conditioned — 과모수화 신호** |
| > 10,000 | 심각, 파라미터 신뢰 불가 |

`[출처: PIPET, Ch.3, p.38]` `[출처: Owen, Ch.3, p.62]`

> 💡 **Condition number를 산의 지형으로 이해하라.** OFV 최솟값을 찾는 것은 안개 속에서 산의 가장 낮은 지점을 찾는 것과 같다. Condition number가 작다(< 200) = 계곡이 깊고 좁은 V자 → 어디로 발을 내디뎌도 바닥이 명확하다. Condition number가 크다(> 1,000) = 계곡이 납작하고 긴 U자 또는 쟁반 모양 → "여기도 최솟값 같고, 저기도 비슷하다" — 무수히 많은 파라미터 조합이 거의 동등한 OFV를 내며, SE 자체를 신뢰할 수 없다.

**$MSFI/$MSFO — 장시간 추정 결과 저장·재활용:**

```nonmem
; 추정 실행 및 결과 저장
$ESTIMATION METHOD=1 INTER MAXEVAL=9999 MSFO=run49.msf

; 결과 재활용 ($THETA/$OMEGA/$SIGMA 대체)
$MSFI run49.msf
; → $COV, $TABLE 추가 요청, VPC 시뮬레이션 등에 활용
; ⚠️ $PK/$ERROR 코드 변경 시 .msf 파일과 충돌 → 오류 발생
```

`[출처: Owen, Ch.3, pp.61-62]`

**$TABLE 레코드 — Xpose4 연동 필수 패턴:**

```nonmem
; Xpose4 자동 인식 규약: sdtab/patab/catab/cotab + 동일 번호
$TABLE ID TIME AMT DV MDV IPRED CWRES IWRES
  ONEHEADER NOPRINT FILE=sdtab1001   ; 표준 진단 테이블
$TABLE ID CL V2 V3 Q KA ETA(1) ETA(2) ETA(3)
  ONEHEADER NOPRINT FILE=patab1001   ; 파라미터 테이블
$TABLE ID SEX RACE
  ONEHEADER NOPRINT FILE=catab1001   ; 범주형 공변량
$TABLE ID WT AGE ALB CLCR
  ONEHEADER NOPRINT FILE=cotab1001   ; 연속형 공변량

; ⚠️ sdtab1001과 patab1002처럼 번호가 다르면 xpose.data() 로딩 실패
; NOAPPEND 미사용 시 DV, PRED, RES, WRES가 자동 추가됨
; FIRSTONLY: 개인당 첫 번째 행만 출력 (ETA, 공변량 테이블에 유용)
```

`[출처: PIPET, Ch.3, p.39]` `[출처: Owen, Ch.3, pp.63-64]`

> 📌 **sdtab/patab 번호 규칙:** Xpose4는 run 번호를 기준으로 "sdtabXXX, patabXXX, catabXXX, cotabXXX" 네 파일을 하나의 세트로 자동 인식한다. 여기서 XXX가 네 파일 모두 동일해야 한다(예: 전부 1001). 파일 이름 하나라도 번호가 다르면 `xpose.data()`가 로딩 실패하고, 그 run의 GOF 플롯 전체를 재실행해야 한다. 관례적으로 run 번호와 일치시킨다(run1 → sdtab1, run49 → sdtab49).

**$SIMULATION — VPC 및 모델 검증:**

```nonmem
$SIMULATION (12345) ONLYSIM NSUB=1000
; (seed): 임의수 생성 시작점 (재현성을 위해 기록 필수)
; ONLYSIM: 추정 없이 시뮬레이션만 실행
; NSUB=1000: 시뮬레이션할 가상 집단 수 (VPC에서 전형적으로 500-2000)
; ⚠️ $SIMULATION 사용 시 $ESTIMATION + $COVARIANCE 동시 사용 불가
; → $MSFI로 추정 결과 불러온 후 $SIMULATION 실행하는 2-step 패턴
```

`[출처: PIPET, Ch.3, p.38]`

---

**C. Structural Necessity**

FOCE가 FO보다 구조적으로 우월한 이유: FO는 OFV를 $\eta=0$에서 1차 테일러 전개로 선형화한다. FOCE는 각 개인의 사후 ETA 추정값($\hat{\eta}_i$)에서 전개하므로 근사 오차가 훨씬 작다. IIV가 클수록(예: %CV > 50%) FO의 편향은 급격히 증가한다.

---

**D. Assumptions & Boundary Conditions**

- MAXEVAL 미지정 시 NONMEM 자동 선택 — 너무 작아 조기 중단 가능 → 명시적 지정 권장
- $COV CONDITIONAL (기본): 추정 성공 시에만 실행. UNCONDITIONAL은 실패해도 실행
- $SIMULATION에서 파라미터는 $THETA/$OMEGA/$SIGMA 또는 $MSFI로 제공

---

**E. Limitations**

- Laplacian은 FOCE보다 실행 시간 현저히 길어 연속형 PK에는 사용 이유 없음
- NOTBT/NOOBT/NOSBT는 탐색용으로만 사용, 규제 제출 모델에 잔류 시 즉시 반려 사유
- $MSFI는 동일한 $PK/$ERROR 코드와만 호환 — 모델 변경 후 재사용 불가

---

**F. Five Cognitive Layers**

| 레이어 | 내용 |
|---|---|
| **L1 형식적 수학** | Condition number = $\lambda_{\max}/\lambda_{\min}$. 분산-공분산 행렬 $C$의 고유값 분해: 큰 고유값 방향 = OFV 변화 최소 방향(flat), 작은 = 최대 변화 방향(steep). Condition number = 등고선 타원의 장축/단축 비율 |
| **L2 기하학적 직관** | OFV 계곡이 좁고 깊은 원형=잘 식별된 모델, 납작하고 긴 타원형=ill-conditioned. Gradient=0은 "이 방향으로 OFV가 평평함" = 데이터 정보량 0 |
| **L3 구조적 동일성** | $COV step = 통계학의 Fisher 정보 행렬 역산. Condition number > 임계값 = Hessian이 거의 특이(near-singular) → SE 신뢰 불가. MAXEVAL=0 = SQL의 `DRY RUN` |
| **L4 생리학적 의미** | Gradient=0 = "이 파라미터에 대한 데이터 정보량=0" = 식별 가능성(identifiability) 문제. 임상적으로 데이터 설계 부족(희소 샘플링, 분포상 데이터 없음)이 원인 |
| **L5 실무 투영** | FDA BLA/NDA: $COV step 성공 + RSE% 보고 필수. $COV PRINT=E 출력(고유값 포함)을 보고서 첨부해야 모델 안정성 증거. sdtab/patab 번호 일치 없으면 Xpose GOF 전체 재실행 필요 |

---

**G. Zettelkasten Atom**

```yaml
---
aliases: [$ESTIMATION, $COVARIANCE, $TABLE, $SIMULATION, condition number, MAXEVAL, FOCE, Xpose4]
tags: [pharmacometrics/nonmem, nonmem/estimation, nonmem/covariance, nonmem/output]
up: "[[II-06 추정 방법론 OFV 심화]]"
related: ["[[II-09b $COV SE RSE 심화]]", "[[NOTBT 경계 경고]]", "[[VPC 검증]]"]
source: "PIPET, Ch.3, pp.37-39 / Owen, Ch.3, pp.56-64"
---
```

FO는 η=0에서, FOCE는 개인별 사후 ETA에서 테일러 전개하므로 FOCE가 정확하다. MAXEVAL=0은 초기값 타당성의 가장 빠른 시각 진단 도구다. $COV PRINT=E의 Condition number>1,000은 과모수화 신호로 파라미터 수 축소 또는 FIX가 필요하다. sdtab/patab 번호는 동일해야 Xpose4가 자동 인식한다.

---

## 카드 5: $PRED — PREDPP 없는 자유 코딩

---

### ━━ [개념 Big Idea: 거장의 시각] ━━

**왜 치명적으로 중요한가:** ICH E14 QTc-노출 관계 분석, Emax PD 모델, 비선형 바이오마커 반응은 ADVAN으로 표현할 수 없는 비PK 관계를 NONMEM으로 추정해야 하는 규제 표준 분석이며, $PRED를 모르면 NONMEM을 PK 도구로만 제한하게 된다.

**체화해야 할 단 하나의 직관:** $PRED는 NONMEM에게 "PK 라이브러리를 내려놓고 내가 직접 예측식을 쓸게"라고 선언하는 것이다 — 그 대신 AMT/CMT 같은 PREDPP 약속어가 사라지고, 용량을 매 관찰 행마다 공변량처럼 반복 기재해야 한다.

**이 직관을 머릿속에 박고 아래를 읽어라:** $PRED는 해석해(closed-form solution)가 존재하는 모델에서만 사용하며, 미분방정식이 필요하면 $DES(ADVAN6)를 써야 한다.

---

**A. Formal Definition**

$PRED 블록은 $SUBROUTINE, $MODEL, $PK, $DES, $ERROR를 모두 대체하는 단일 블록이다. PREDPP를 호출하지 않으므로 사전 약속된 예약어(reserved word)가 없고, 파라미터 이름을 완전히 자유롭게 지정할 수 있다. 최종적으로 Y를 정의하여 NONMEM 목적함수 계산기에 전달한다.

---

**B. Derivation / Code Structure**

**ADVAN2 vs $PRED 비교 (PIPET 그림 7.1):**

```nonmem
; ━━ ADVAN2 방식 ━━         ; ━━ $PRED 방식 (동일 모델, 해석해) ━━
$SUBR ADVAN2 TRANS2          $PRED
$PK                            TVCO = THETA(1) ; k_a/(V×(KA-k10)) 계수항
  CL=THETA(1)*EXP(ETA(1))     TVEX = THETA(2) ; k10 소실 지수
  V =THETA(2)*EXP(ETA(2))     TVKA = THETA(3)
  KA=THETA(3)*EXP(ETA(3))     COEF = TVCO*EXP(ETA(1))
  S2 = V                       EXPO = TVEX*EXP(ETA(2))
$ERROR                          KA   = TVKA*EXP(ETA(3))
  IPRED = F                    ; 1구획 경구 해석해
  ...                           ; C(t) = D·KA·COEF/(KA-EXPO)·(e^(-EXPO·T)-e^(-KA·T))
  Y = F + W*EPS(1)              IPRED=D*COEF*KA/(KA-EXPO)*(EXP(-EXPO*T)-EXP(-KA*T))
                                IRES = DV - IPRED
; 데이터: AMT=투여 시점 한 번  IWRES = IRES/IPRED
;         (PREDPP가 적분 유지)  Y = IPRED*(1+EPS(1)) + EPS(2)
                               ; 데이터: D를 모든 관찰 행에 공변량처럼 반복 기재
```

`[출처: PIPET, Ch.7, pp.69-70]`

> 💡 **"D를 모든 관찰 행에 반복 기재"가 필요한 이유:** ADVAN을 쓰면 PREDPP가 내부적으로 "투약 기록(EVID=1)에서 구획에 약물 추가 → 이후 시간 흐름에 따라 적분 유지"를 자동으로 수행한다. 그러나 $PRED에서는 PREDPP 자체가 없으므로 이 시간 적분 엔진이 없다. 대신 해석해(closed-form) 수식이 이미 "t시간 후 남아있는 양"을 계산하기 때문에, 각 관찰 시점에서 "초기 투여량(D)"만 알면 된다 — 그래서 D를 매 행마다 공변량처럼 제공해야 한다.

**QTc 선형 모델 — $PRED 최소 예시 (PIPET 코드 3.8):**

```nonmem
$PROB QTc, PRED
$INPUT ID=DROP DQTC=DV CMAX     ; ID=DROP: ID를 분석에 사용하지 않음
$DATA data.csv IGNORE=C          ; IGNORE=C: 첫 열에 'C'포함 행 제외 (헤더)
$PRED
  INT = THETA(1)                  ; Intercept
  SLP = THETA(2)                  ; Slope
  EFF = SLP*CMAX + INT            ; 선형 약효 모델
  Y   = EFF + ETA(1)              ; 가법 잔차 — $ERROR 없이 $PRED에서 직접 정의
$THETA 0.1  0.5
$OMEGA 0.04
$EST PRINT=5 MAX=9999 SIG=3
```

`[출처: PIPET, Ch.3, 코드 3.8, p.46]`

**Sigmoidal Emax PD 모델:**

```nonmem
$PRED
  E0   = THETA(1)                      ; 기저 약효
  EMAX = THETA(2)                      ; 최대 약효 변화
  C50  = THETA(3)*EXP(ETA(1))         ; EC50 — IIV 포함
  GAM  = THETA(4)                      ; Hill 계수 — ETA 추가 금지 (수렴 불안정)

  IPRD = E0 + (EMAX-E0)*CP**GAM / (CP**GAM + C50**GAM)
  Y    = IPRD + EPS(1)
```

`[출처: PIPET, Ch.7, 코드 7.1, p.71]`

> 📌 **Hill 계수(GAM)에 ETA를 추가하지 않는 이유:** GAM은 Emax 수식의 지수에 들어가기 때문에(CP^GAM), GAM에 개인별 변이가 있으면 OFV 기울기(gradient)가 극도로 불규칙해져 수렴이 매우 불안정해진다. 현장 표준은 GAM을 집단 고정값으로 추정하고(ETA 없음), EC50에만 IIV를 부여하는 것이다.

---

**C. Structural Necessity**

$PRED가 Y를 내부에서 정의해야 하는 이유: PREDPP가 호출되지 않으면 NONMEM의 시간 적분 엔진이 동작하지 않아 F(개인 예측 농도, PREDPP 예약변수)가 정의되지 않는다. 사용자가 IPRD 등 자체 변수를 정의하고 최종적으로 Y를 통해 NONMEM에 예측값과 잔차 구조를 전달해야 한다. THETA·ETA 첨자 순서는 $PRED 내부에서 무관하다 (Owen p.49: THETA(1)이 ETA(2)와 쌍일 수 있음).

---

**D. Assumptions & Boundary Conditions**

- 해석해가 존재하는 모델에서만 유효 — 미분방정식 형태 모델에는 ADVAN6+$DES 사용
- 다회투여 데이터에서 $PRED 적용 시 중첩(superposition) 코딩이 매우 복잡 → 다회투여는 ADVAN 계열 권장
- $PRED와 $SUBROUTINE은 동일 제어구문에 공존 불가

---

**E. Limitations**

- 복잡한 다구획 PK에는 해석해 없음 → 실제 사용은 1구획 검증, PD 모델, QTc-노출 관계, 비선형 바이오마커에 국한
- Hill 계수(GAM)에 ETA 추가 시 수렴 불안정 — 임상 표준은 GAM에 IIV 없음

---

**F. Five Cognitive Layers**

| 레이어 | 내용 |
|---|---|
| **L1 형식적 수학** | 1구획 경구 해석해: $C(t) = \frac{D \cdot k_a}{V(k_a-k_{10})}(e^{-k_{10}t}-e^{-k_a t})$. $PRED의 IPRED 라인 = 이 수식의 FORTRAN 직역 |
| **L2 기하학적 직관** | GAM(Hill 계수) < 1: 완만한 시그모이드(음성 협동), GAM = 1: Langmuir 등온흡착, GAM > 1: 급격한 스위치(양성 협동) |
| **L3 구조적 동일성** | $PRED = 통계학의 GLM 커스텀 링크 함수: $Y=g(\theta,x)+\varepsilon$를 사용자가 임의 정의 |
| **L4 생리학적 의미** | GAM = 수용체 협동성(cooperativity)의 정량 지표. ICH E14 분석에서 C50(QTc 연장 반감 농도)과 GAM이 규제 핵심 보고 수치 |
| **L5 실무 투영** | ICH E14 QTcF-농도 분석 표준: $PRED로 선형/비선형 관계 코딩. RSE% < 30%가 규제 제출 최소 요건 |

---

**G. Zettelkasten Atom**

```yaml
---
aliases: [$PRED 블록, PREDPP 없는 코딩, Emax PD, QTc 노출 분석, Hill 계수]
tags: [pharmacometrics/nonmem, nonmem/coding/pred, pd-modeling, regulatory/E14]
up: "[[II-03 특수 ADVAN TRANS]]"
related: ["[[II-11 PK-PD NONMEM 구현]]", "[[ICH E14 QTc 분석]]"]
source: "PIPET, Ch.3 코드3.8/Ch.7, pp.46-71 / Owen, Ch.3, pp.49-50"
---
```

$PRED는 PREDPP 라이브러리 전체를 대체하여 PD 모델·비PK 관계·해석해 존재 PK를 자유 수식으로 구현한다. 투여량을 모든 관찰 행에 공변량처럼 반복 기재해야 하며, $ERROR 없이 $PRED 내부에서 Y를 직접 정의한다. Hill 계수(GAM)에는 IIV를 추가하지 않는 것이 현장 표준이다.

---

# §5 — 혼동 쌍 해부

---

## 혼동 쌍 1: 특수 ADVAN vs 일반 ADVAN (ADVAN5/6)

| 비교 차원 | 특수 ADVAN (ADVAN1-4, 10-12) | 일반 ADVAN (ADVAN5/6/7/8/9/13) |
|---|---|---|
| **표면적 유사성** | 둘 다 $SUBROUTINE에서 선택하고 $PK 블록을 사용 | |
| **수식/코드 형태** | `$SUBR ADVAN4 TRANS4` → $MODEL, $DES 불필요 | `$SUBR ADVAN6 TOL=4` → $MODEL + $DES 필수. **TOL= 누락 시 실행 자체 불가** |
| **구조적 지시체** | PREDPP에 미리 구현된 표준 구획 구조 | 사용자가 $MODEL로 구획 정의 + $DES로 ODE 직접 기술 |
| **변화 방향** | 모델 구조 변경 시 ADVAN 번호 변경 필수 (경직성) | $DES ODE 수정만으로 비선형 소실·장간순환·대사체 구현 가능 (유연성) |
| **임상/모델링 결과** | MM 비선형 소실, 장간순환, 모약물-대사체 동시 분석에 특수 ADVAN을 고집하면 구현 자체가 불가능 | |
| **⚡ 기억 고리** | 특수 ADVAN=기성복(빠르고 편하지만 치수 고정), 일반 ADVAN=맞춤복(느리고 손이 많이 가지만 어떤 체형도 소화). 비선형 소실이 보이는 순간 기성복 진열대를 벗어나야 한다. | |

---

## 혼동 쌍 2: ADVAN3 vs ADVAN4 — S-parameter와 CMT 번호 [⚠️ Critical Blow 적용]

| 비교 차원 | ADVAN3 (IV 2구획) | ADVAN4 (경구 2구획) |
|---|---|---|
| **표면적 유사성** | 둘 다 2구획 모델이며, TRANS4에서 CL, Q 파라미터 공유 | |
| **수식/코드 형태** | `S1 = V1` (중심구획=CMT1) | `S2 = V2` (중심구획=CMT2) |
| **구조적 지시체** | CMT1=Central, CMT2=Peripheral | CMT1=**Depot**, CMT2=Central, CMT3=Peripheral |
| **변화 방향** | ADVAN3→ADVAN4 전환 시: S1→S2, V1/V2→V2/V3, KA 추가, CMT 값 수정 (4가지 동시 변경 필수) | |
| **임상/모델링 결과** | S2 미수정 시 IPRED = 정확값 × V2/1000 (전형적으로 1/20 ~ 1/200). NONMEM 오류 메시지 없이 $COV step까지 성공 | |
| **치명적 타격** | ADVAN3에서 ADVAN4로 S-parameter 미수정 전환 후 생성된 PopPK 보고서를 기반으로 Phase 2 용량 결정 시, 모든 예측 Cp가 실제보다 V2/1000배 낮게 산출되어 "목표 노출 달성을 위해 실제 필요 용량의 V2/1000배 과다투여"를 권고하는 치명적 임상 오류로 이어진다 (FDA Deficiency Letter 사유: "모델 예측값 단위 검증 불충분"). |
| **⚡ 기억 고리** | "IV(홀수 ADVAN)는 바로 혈관으로 — 중심구획이 첫 번째(S1). 경구(짝수 ADVAN)는 위를 거쳐서 — 위가 먼저(Depot=CMT1), 혈관이 두 번째(S2)." **홀수=S1, 짝수=S2.** | |

---

## 혼동 쌍 3: $PK IIV — 지수(EXP) 모델 vs 비례(1+ETA) 모델

| 비교 차원 | 지수(exponential) IIV | 비례(proportional/CCV) IIV |
|---|---|---|
| **표면적 유사성** | 둘 다 IIV를 표현하며, FO 근사 하에서 수학적 동치 | |
| **수식/코드 형태** | `CL = TVCL * EXP(ETA(1))` → $CL_i = TVCL \cdot e^{\eta_i}$ | `CL = TVCL * (1 + ETA(1))` → $CL_i = TVCL(1+\eta_i)$ |
| **구조적 지시체** | 개인 파라미터가 로그정규분포 → **항상 양수** | 개인 파라미터가 정규분포 → ETA < -1이면 **음수 발생** |
| **변화 방향** | FOCE에서 ETA가 극단값이어도 CL_i > 0 유지 | ETA < -1 → 음수 CL → 추정 실패 또는 비현실적 결과 |
| **임상/모델링 결과** | 비례 모델 사용 시 FOCE 추정 중 음수 파라미터 발생 가능, $COV step 실패로 이어질 수 있음 | |
| **⚡ 기억 고리** | "지수는 울타리, 비례는 열린 벌판" — 지수 모델은 ETA가 아무리 음수여도 파라미터를 0 아래로 내려가지 못하게 막는다. 단, PD 파라미터 중 음수가 의미 있는 것(기저선 변화량)에는 비례 또는 가법 모델 허용. | |

---

## 혼동 쌍 4: $SIGMA 직접 추정 vs $THETA + $SIGMA 1 FIX

| 비교 차원 | $SIGMA 직접 추정 | $THETA로 추정 + $SIGMA 1 FIX |
|---|---|---|
| **표면적 유사성** | 둘 다 잔차변이 크기를 NONMEM으로 추정 | |
| **수식/코드 형태** | `Y=F*(1+EPS(1))` + `$SIGMA 0.04` | `W=SQRT(THETA(3)**2+...)` + `$SIGMA 1 FIX` |
| **구조적 지시체** | σ² = **분산값** 추정 (보고 시 √ 변환 필수) | THETA(3)=**가법 SD**, THETA(4)=**비례 CV** (직접 보고 가능) |
| **변화 방향** | $SIGMA 0.04 → **%CV = √0.04 × 100 = 20%** (4%가 아님!) | THETA(4) 0.20 → **%CV = 20%** (그대로 보고) |
| **임상/모델링 결과** | $SIGMA 0.04를 "%CV=4%"로 오인하여 보고서 기재 시 실제 20%를 5배 과소 보고 — FDA 심사관의 수학적 재검토 즉시 발각 | |
| **⚡ 기억 고리** | "$SIGMA는 분산의 창고 — %CV를 꺼내려면 제곱근 개봉이 필수. $THETA로 추정하면 SD/CV가 그대로 출력되어 추가 변환 없이 보고 가능." | |

---

# §7 — Self-Test: Active Recall Module

**Q1 (회상 ○)** NONMEM 시스템의 세 구성요소(NM-TRAN, PREDPP, NONMEM) 각각의 역할을 한 문장으로 정의하라.

<details><summary>정답 공개</summary>

**NM-TRAN**: 사용자 제어구문을 파싱·문법검사하여 NONMEM 실행 가능 형태로 변환하는 번역기. **PREDPP**: 집단약동학 분석을 위한 표준 PK 구획 모델 서브루틴(ADVAN) 라이브러리. **NONMEM**: 비선형 혼합효과 모델의 OFV 최소화를 통한 파라미터 추정 엔진.

**다음 깊이 질문:** NM-TRAN이 "배치 모드"로 실행된다는 것이 $ERROR 방어 코딩(LOG-error FLAG 패턴 등)의 필요성과 어떻게 연결되는가?

</details>

---

**Q2 (적용 ★★)** ADVAN3 TRANS4(IV 2구획)를 ADVAN4 TRANS4(경구 2구획)로 전환할 때 반드시 수정해야 하는 항목 4가지를 열거하고, 수정 누락 시 IPRED 오차의 수학적 크기를 도출하라.

<details><summary>정답 공개</summary>

**(1) S-parameter 번호**: `S1=V1` → `S2=V2`. ADVAN3 Central=CMT1(S1), ADVAN4 Central=CMT2(S2).
**(2) 분포용적 변수명**: V1→V2, V2→V3 (ADVAN4 TRANS4 필수 파라미터: V2=중심, V3=말초).
**(3) KA 추가**: ADVAN4 TRANS4의 5번째 필수 파라미터.
**(4) 데이터셋 CMT 값**: ADVAN3 관찰 기록 CMT=1 → ADVAN4 관찰 기록 CMT=2.

**오차 크기**: S2 미수정 시 S2=1(기본값) 적용. IPRED_잘못 = A(2)/1, IPRED_올바른 = A(2)/(V2/1000). 오차 비율 = V2/1000. V2=50L이면 50/1000 = **1/20배 → 20배 과소추정**.

**다음 깊이 질문:** FDATA 파일에서 이 오류를 사전에 탐지하는 방법은?

</details>

---

**Q3 (적용 ★)** `$DATA test.csv IGNORE=(WTKG.GE.100, STDY.EQ.301)`의 실제 동작을 기술하고, "체중 ≥ 100kg이면서 스터디 301에 속하는 대상자만 제외"하는 코드를 작성하라. PIPET p.31이 이와 다르게 기술한 이유를 설명하라.

<details><summary>정답 공개</summary>

**실제 동작**: "(체중 ≥ 100kg) **OR** (스터디 = 301)"인 행 제외. NONMEM 엔진은 다중 조건을 암묵적 OR로 처리한다 (Owen p.33).

**AND 배제 코드**:
```nonmem
$DATA test.csv ACCEPT=(WTKG.LT.100, STDY.NE.301)
```

**PIPET 오기 설명**: PIPET p.31은 ".AND. 또는 .OR. 사용 가능"이라고 기술하나 Owen p.33이 "No other operator may be specified"라고 명확히 정의한다. NONMEM 실행 엔진의 실제 동작은 Owen이 정확하며 PIPET의 해당 문구는 오기 또는 부정확한 기술이다.

**다음 깊이 질문:** IGNORE=# 와 ACCEPT 조건부 옵션을 동시에 사용하는 것이 허용되는가?

</details>

---

**Q4 (회상 ★)** dose(mg), V2(L), Cp(ng/mL) 단위 조합에서 ADVAN4 TRANS4의 S2 식을 도출하고, 도출 과정에서 usv의 물리적 의미를 설명하라.

<details><summary>정답 공개</summary>

$S2 = V2/1000$

**도출**: $\text{Cp} = \text{Amount}/S2$에서, Amount(mg)/S2 = Cp(µg/L)가 되려면:
$$\frac{\text{mg}}{S2} = \frac{\text{µg}}{L} \Rightarrow S2 = \frac{\text{mg} \cdot L}{\text{µg}} = \frac{V2(L)}{1000}$$

**usv의 물리적 의미**: mg(투여 단위)와 µg(농도 단위)의 1000배 불일치를 보정하는 무차원 스케일 인자. `[Owen Eq.3.6, p.41]`

**다음 깊이 질문:** 투여량을 µg 단위로 AMT에 기재하고 농도를 pg/mL로 관찰한다면 S2는?

</details>

---

**Q5 (적용 ★★)** `$SIGMA 0.09`를 보고서에 "IIV in CL, %CV=9%"로 기재했다. 이 보고서의 오류를 수정하고, $SIGMA와 $OMEGA에서 분산을 %CV로 환산하는 공식을 도출하라.

<details><summary>정답 공개</summary>

**오류**: `$SIGMA 0.09`는 **$OMEGA (IIV)**가 아닌 **잔차변이($SIGMA)**이며, %CV 환산도 틀렸다.

$\omega^2 = 0.09 \Rightarrow \omega = 0.3 \Rightarrow \%CV_{IIV} = \omega \times 100 = 30\%$

마찬가지로 $\sigma^2 = 0.09 \Rightarrow \%CV_{RV} = 30\%$ (4%도 9%도 아님).

**공통 공식 (Owen pp.52-53)**:
$$\%CV = \sqrt{\text{분산값}} \times 100$$

**역산** (초기값 설정 시): $\omega^2 = (\%CV/100)^2$. 예: CL의 IIV 30%CV → $\$OMEGA\ 0.09$.

**다음 깊이 질문:** $OMEGA BLOCK(2) 구조에서 상관계수 r=0.7로부터 공분산 초기값을 역산하는 공식은?

</details>

---

**Q6 (적용 ★)** MAXEVAL=0 실행의 목적과 단계별 진단 절차를 설명하고, 0번째 iteration에서 THETA(2)의 gradient=0이 나타났을 때 가능한 원인 두 가지를 제시하라.

<details><summary>정답 공개</summary>

**목적**: 파라미터 추정 없이 초기값으로 PRED/IPRED만 계산. 맹목적 재실행 전 초기값 타당성 시각 검증.

**단계별 진단**: ① $TABLE로 PRED, IPRED, DV 출력 → ② R에서 DV vs PRED 겹쳐 그리기 → ③ 예측선 위치 확인 후 초기값 조정 → ④ MAXEVAL 복원 후 정식 추정.

**Gradient=0 원인**:
1. IGNORE/ACCEPT로 특정 집단이 제외되어 THETA(2)가 추정해야 할 공변량(예: 성별) 정보가 데이터에 전혀 없는 경우
2. $PK에서 THETA(2)를 참조하는 파라미터가 OFV 계산에 실질적으로 기여하지 않는 구조적 비식별성

**다음 깊이 질문:** Gradient가 0번째 iteration에서만 0이고 이후 iteration에서 0이 아니라면 어떻게 해석하는가?

</details>

---

**Q7 (적용 ★)** $COV PRINT=E 출력에서 Condition number=12,400이 계산되었다. 이 모델의 병리를 진단하고, 해결 전략 2가지와 규제 보고서에서 이 상황을 방어하는 언어를 작성하라.

<details><summary>정답 공개</summary>

**병리 진단**: Condition number > 1,000 → ill-conditioned. "거의 동등한 파라미터 조합이 무수히 많다" = 과모수화 또는 데이터 식별성 부족. SE 및 RSE 값 신뢰 불가.

**해결 전략**:
1. 상관행렬에서 ≈±1 원소 확인 → 공분산 높은 파라미터 쌍 식별 → 한 파라미터를 문헌값으로 FIX
2. 모델 구조 단순화 (3구획→2구획) 또는 IIV가 작은 ETA 제거($OMEGA 0 FIX)

**규제 보고서 방어 언어**: "추정된 분산-공분산 행렬의 condition number(12,400)가 기준치(1,000)를 초과하여 모델의 과모수화 가능성이 확인되었다. [파라미터명]을 문헌 보고값으로 고정한 후 condition number가 [수치]로 감소하였으며 모든 추정 파라미터의 RSE <[%] 달성으로 모델 안정성을 확인하였다."

**다음 깊이 질문:** Condition number 계산에서 $\lambda_{\min}$이 음수에 가까워질 때 추가로 발생하는 문제는?

</details>

---

**Q8 (적용 ○)** Xpose4에서 "xpose.data() loading failed" 오류가 발생했다. 가장 먼저 확인해야 할 제어구문의 위치는 어디이며, 전형적인 원인과 수정 방법을 설명하라.

<details><summary>정답 공개</summary>

**확인 위치**: $TABLE 레코드의 FILE= 옵션 번호.

**원인**: `FILE=sdtab1001`과 `FILE=patab1002`처럼 테이블 간 번호가 불일치할 경우 Xpose4가 동일 분석 결과로 인식하지 못함.

**수정**: 모든 $TABLE FILE=의 번호를 동일하게 통일 (예: sdtab1001, patab1001, catab1001, cotab1001). 번호는 관례적으로 run number와 일치시킴.

**다음 깊이 질문:** $TABLE에서 NOAPPEND 옵션을 사용하지 않으면 자동으로 추가되는 4개 변수는 무엇이며, GOF 플롯 구성에 어떻게 활용되는가?

</details>

---

**Q9 (적용 ★)** 아래 제어구문 조각의 오류 3개를 찾고 수정하라:

```nonmem
$SUBROUTINE ADVAN3 TRANS4  ; 경구 2구획 모델 구현 예정
$PK
  CL = THETA(1) * EXP(ETA(1))
  V2 = THETA(2) * EXP(ETA(2))
  V3 = THETA(3) * EXP(ETA(3))
  Q  = THETA(4) * EXP(ETA(4))
  S1 = V2/1000
$SIGMA 0.04    ; 분석 보고서에 "%CV = 4%"로 기재 예정
```

<details><summary>정답 공개</summary>

**오류 1**: `ADVAN3`은 IV 2구획 모델 — 경구 모델은 `ADVAN4`로 수정 필요.

**오류 2**: `S1 = V2/1000` → `S2 = V2/1000`. ADVAN4에서 중심구획=CMT2이므로 S2 사용 필수. S1은 Depot(CMT1) 척도 파라미터.

**오류 3**: `KA` 누락. ADVAN4 TRANS4의 5번째 필수 파라미터. `KA = THETA(5) * EXP(ETA(5))` 추가 필요.

**오류 4 (보너스)**: `$SIGMA 0.04`의 %CV = $\sqrt{0.04} \times 100 = 20\%$. 보고서 "4%"는 오기 — "20%"로 수정.

**수정된 코드**:
```nonmem
$SUBROUTINE ADVAN4 TRANS4
$PK
  CL = THETA(1) * EXP(ETA(1))
  V2 = THETA(2) * EXP(ETA(2))
  V3 = THETA(3) * EXP(ETA(3))
  Q  = THETA(4) * EXP(ETA(4))
  KA = THETA(5) * EXP(ETA(5))    ; ← 추가
  S2 = V2/1000                    ; ← S1→S2
$SIGMA 0.04    ; %CV = 20% (√0.04×100) — 보고서 수정 필요
```

**다음 깊이 질문:** 데이터셋에서도 수정이 필요한 사항은?

</details>

---

**Q10 — 보스 딜레마 ★★**

**시나리오:** 항암제 Phase 1 희소 샘플링 데이터(n=24명, 1인당 2-3개 관찰값)로 PopPK 모델 구축 중이다. EDA에서 log-Cp vs Time이 두 직선 기울기를 보여 2구획 모델(ADVAN4 TRANS4)이 생물학적으로 타당하다. 추정 결과: CL·V2 RSE < 25%로 양호하나, Q·V3 RSE = 180%, $COV PRINT=E Condition number = 4,500, 상관행렬 ρ(V3, Q) = 0.96. $COV step은 성공함.

**Option A**: 2구획 모델 유지 — "생물학적으로 타당하고 $COV step 성공, 제출 강행"  
**Option B**: 1구획 모델로 단순화 — "V3·Q 식별 불가, 데이터가 지지하는 모델로 후퇴"

**IND 규제 제출 기한 72시간 전. 어느 쪽을 선택하는가?**

<details><summary>수석 모델러의 Trade-off 논리</summary>

**선택: Option B, 단 2구획 분석 결과를 민감도 분석으로 투명하게 보고한다.**

**핵심 논리:** ρ(V3, Q)=0.96과 Condition number=4,500은 "V3와 Q 중 하나는 데이터가 추정하지 못하고 있다"는 수학적 증거다. RSE=180%인 파라미터가 포함된 모델의 $COV 성공은 **의미 없는 성공** — SE 자체를 신뢰할 수 없기 때문이다. 이 파라미터로 Phase 2 용량 시뮬레이션을 수행하면 95% CI가 임상적으로 의미 없을 만큼 넓어진다.

**규제 문서 방어 언어:**

"2구획 모델은 EDA와 생물학적 근거로 지지되나, 본 시험의 희소 샘플링 설계(n=24, 1인당 2-3 관찰값)에서 말초 구획 파라미터(Q, V3)의 추정 정밀도(RSE=178%, ρ=0.96, condition number=4,500)가 Phase 2 용량 권고의 기초로 사용하기에 불충분하다. 1구획 기저 모델(CL, V2 RSE<25%)이 주요 PK 특성을 안정적으로 추정하며 이를 용량 결정의 근거로 사용하였다. 2구획 모델 분석 결과는 민감도 분석으로 첨부하며, Phase 2 밀집 샘플링 데이터에서 재평가할 계획이다."

**원칙:** 2구획 ΔOFV, Condition number 비교, GOF 비교를 포함한 Sensitivity Analysis를 보고서에 포함하여 모델러의 판단 과정을 투명하게 제시하는 것이 심사관 신뢰를 높이는 규제 전략이다.

</details>

---

# §8 — 메타프레임 & 빅 픽처

### A. Positioning

II-03은 "NONMEM 제어구문 3부작"의 완성판이다. II-01이 파라미터의 통계적 존재론(θ·η·ε 의미)을, II-02가 데이터 구조(행·열·변수)를 다뤘다면, II-03은 그 두 가지를 실행 가능한 코드로 연결하는 아키텍처 설계도다.

- **이전에 온 것**: II-01 (THETA/OMEGA/SIGMA 통계적 의미), II-02 (ID/TIME/AMT/DV/MDV/CMT 데이터 변수)
- **바로 다음**: II-04 (ADVAN6 $DES ODE 작성법 심화), II-05 (초기추정값 전략 — NCA 기반 사전 추정)
- **이 기반에 결정적으로 의존하는 고급 도메인:** 공변량 분석(II-08) — TVCL=THETA(1)×(WT/70)^THETA(n) 확장 코딩; $COV 심화(II-09b) — Condition number 해석과 Bootstrap 비교; PK/PD 통합(II-11) — $PRED QTc-노출 분석, effect compartment 연결 코딩; VPC 검증 — $SIMULATION, MSFO= 활용, 단위 일관성 검증

### B. Dependencies

이 세션을 대충 넘겼을 때 고급 모델링에서 발생하는 구체적 실패 모드:

**실패 1 — ADVAN 전환 시 S-parameter 미수정으로 인한 용량 권고 오류:** S2=V2/1000 대신 S1=V2가 남은 채 Phase 2 시뮬레이션을 진행하면 예측 Cp가 V2/1000배 과소추정된 상태에서 "목표 노출 달성을 위해 현재 용량의 V2/1000배가 필요하다"는 시뮬레이션 결과가 도출된다. 공변량 분석(II-08) 단계에서 이 오류가 누적되면 WT-CL 관계의 기울기 추정 전체가 오염된다.

**실패 2 — Log-error 모델 방어 코딩 부재로 인한 분석 중단:** 다중 연구 풀링 데이터에서 log-error 모델 도입 시 OBSERVATIONS ONLY/CALLFL=0/FLAG 패턴 없이 실행하면 LOG(0) 오류로 NONMEM이 강제 종료된다. 원인 파악에 수 시간이 소모된다.

**실패 3 — $TABLE 번호 불일치로 인한 Xpose4 GOF 재실행:** sdtab/patab 번호 불일치 시 R의 xpose.data() 로딩 자체가 실패하여 전체 GOF 진단 플롯 파이프라인이 멈춘다. VPC 검증(II-10)에서 $SIMULATION과 $ESTIMATION을 동시 사용해 NONMEM이 실행되지 않는 오류도 이 레코드 이해의 공백에서 비롯된다.

**실패 4 — $SIGMA %CV 오인으로 인한 규제 보고서 오기:** `$SIGMA 0.04 → "%CV=4%"`로 보고하는 오류는 FDA 심사관의 수학적 재검토에서 즉시 발각되어 Information Request를 발행시킨다.

### C. Professional Moat

NONMEM을 실행하고 파라미터를 추출하는 것은 이미 자동화 가능하다. 이 세션의 제어구문 구조와 진단 논리를 진정으로 내면화한 모델러만이 할 수 있는 것은 세 가지다.

첫째, **침묵의 오류를 코드 한 줄로 진단한다.** 모든 IPRED가 DV보다 수십 배 낮은 상황 앞에서 — "S-parameter 단위 불일치, ADVAN 전환 시 S1→S2 미수정"을 즉시 식별하고 수정한다. 알고리즘은 오류 메시지가 없으면 이 상황을 "정상 수렴"으로 분류한다.

둘째, **교과서의 오기를 현장에서 검증한다.** PIPET Table 4.5의 ADVAN3 CMT 오기를 Owen과 대조하여 식별하고, IGNORE AND/OR 동작에서 PIPET과 Owen의 불일치를 엔진 동작 기준으로 해소한다. 이 비판적 교차검증 능력은 알고리즘이 단일 소스에 의존하는 것과 근본적으로 다르다.

셋째, **Condition number와 상관행렬을 읽어 모델 선택을 규제 언어로 방어한다.** ρ(V3, Q)=0.96이 "말초 분포 데이터가 없다"는 생리학적 독해이고, 이것이 "3구획→2구획 축소" 또는 "Q를 문헌값으로 FIX"라는 처방으로, 그리고 "Phase 2 밀집 샘플링에서 재평가"라는 규제 언어로 이어지는 판단의 사슬을 알고리즘은 수행하지 못한다.

---

```
---
✦ STEP 1 완료 (주석 강화 최종판).

추가된 주석 목록 (10개):

  💡 카드1-A  배치 모드의 의미 — 왜 방어적 코딩이 필수인가
  💡 카드1-B  레코드 순서 불변 이유 — 법원 판결문 비유
  📌 카드1-B  De Morgan 변환 직관 — NOT/AND/ACCEPT 방향 전환 원리
  💡 카드1-B  CHECKOUT의 실용 가치 — 수십 초 진단 vs 수 시간 추정
  📌 카드2-A  홀짝 암기법 — "홀수=주사(IV)=S1, 짝수=경구=S2"
  💡 카드2-B  Depot 경로 흐름 — 한 칸 밀림이 모든 번호 오프셋의 원인
  💡 카드2-B  S-parameter 본질 — Amount÷Sn=농도, 단위 불일치가 오류 원인
  ⚠️ 카드2-C  ADVAN3→ADVAN4 전환 "4가지 동시 수정" 강조
  💡 카드3-B  W함수+$SIGMA 1 FIX가 현장 표준인 이유 (직접 보고 가능)
  ⚠️ 카드3-B  $SIGMA %CV 환산 경고 — 5배 과소보고 메커니즘 명시
  💡 카드3-B  LOG(0) 오류 원인 — EVID=1에서 F=0이 되는 이유
  💡 카드4-B  FO vs FOCE 직관 — "모두 평균처럼" vs "각자 실제 특성으로"
  💡 카드4-B  MAXEVAL=0 = 항해 전 해도 확인 비유
  💡 카드4-B  Condition number = OFV 계곡 납작함 지수 (V자 vs 쟁반)
  📌 카드4-B  sdtab/patab 번호 규칙 — XXX가 전부 동일해야 Xpose 인식
  💡 카드5-B  $PRED에서 D를 매 행 반복 기재하는 이유 — 적분 엔진 부재
  📌 카드5-B  Hill 계수(GAM)에 ETA 추가하지 않는 이유 — OFV gradient 불안정

  • 감지된 소스 유형: Vol II — Owen (Ch.3, pp.28-64) + PIPET (Ch.3-4-7, pp.27-71) 혼합
  • Data Anchoring 소스: PIPET 코드 3.2 (ADVAN4 TRANS4), 코드 3.8 (QTc $PRED), 코드 7.1 (Emax PD)

"계속"을 입력하면 Step 2 HTML 컴파일러가 실행됩니다.
---
```

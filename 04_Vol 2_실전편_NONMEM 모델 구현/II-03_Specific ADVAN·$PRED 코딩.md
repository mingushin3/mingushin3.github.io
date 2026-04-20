# §1 — 세션 헤더 & 로드맵

---

## 소스 정보

| 항목 | 내용 |
|---|---|
| **소스 1** | PIPET 한국어 교재 |
| **챕터/섹션** | Ch.3 (pp.27–46) + Ch.4 (pp.47–53) + Ch.7 (pp.69–71) |
| **제목** | NONMEM 모델 종류 별 제어구문 소개 / 특수 ADVAN을 이용한 제어구문의 코딩 / $PRED: ADVAN을 쓰지 않는 코딩 |
| **소스 2** | Owen (Introduction to PopPK/PD) |
| **챕터/섹션** | Ch.3 (pp.28–64) |
| **제목** | NONMEM Overview and Writing an NM-TRAN Control Stream |
| **세션 번호** | II-03 |

---

## Big Idea (한 문장)

NONMEM 제어구문은 세 가지 선택지 — 특수 ADVAN, 일반 ADVAN, $PRED — 사이의 의식적 선택이며, 이 선택이 모델의 구조적 유연성, 실행 속도, 그리고 코딩 부담 사이의 모든 Trade-off를 결정한다.

---

## 개념 항법도

이 세션에서 다루는 핵심 개념:

1. **NONMEM 시스템 3요소** — NM-TRAN, PREDPP, NONMEM 엔진의 역할 분리
2. **제어구문 레코드 구조** — $PROB → $DATA/$INPUT → 모델 블록 → $THETA/$OMEGA/$SIGMA → $ESTIMATION → $COVARIANCE/$TABLE 의 순서와 각 레코드의 기능
3. **특수 ADVAN + TRANS 조합** — ADVAN1~4, 11, 12와 TRANS 서브루틴 선택, 필수·부가 파라미터
4. **$PK 블록 코딩** — TVCL/TVV 관용 패턴, EXP(ETA) IIV 모델, 척도 파라미터(Sn) 단위 통일
5. **$ERROR 블록 잔차변이 구조** — 가법, 비례(CCV), 혼합, 로그오차 모델
6. **일반 ADVAN (ADVAN5/6)** — $MODEL + $DES를 이용한 사용자 정의 구획 모델
7. **$PRED 코딩** — PREDPP 없이 수식을 직접 기술하는 방식과 데이터셋 차이
8. **$ESTIMATION 옵션** — METHOD, MAXEVAL, INTERACTION, NOABORT, SIGDIGITS
9. **$COVARIANCE step** — 표준오차, eigenvalue, condition number
10. **$TABLE 출력 제어** — sdtab/patab/catab/cotab Xpose4 관용 패턴

---

## 지식 그래프 위치

**선행 지식 (이 세션이 전제하는 것):**
- II-01: θ·η·ε 3층 계층 구조 (THETA/OMEGA/SIGMA의 통계적 의미)
- II-02: NONMEM 데이터셋 변수 (ID, TIME, AMT, DV, MDV, CMT, EVID)

**이 세션이 열어주는 후속 지식:**
- II-04: General ADVAN (ADVAN6/13) + $DES ODE 작성법
- II-05: 초기추정값 전략 — 수렴의 과학
- II-06: 추정 방법론 심화 (OFV, LRT, FO/FOCE 이론)
- II-07: 기저 모델 구축 프로세스
- II-08: 공변량 분석 (TVCL = THETA(1)*(COV/median)**THETA(n) 확장)
- II-09b: $COVARIANCE step 심화 · SE/RSE · condition number

---

---

# §2 — 개념 해부 카드

---

## 카드 1: NONMEM 시스템 3요소와 제어구문 레코드 구조

---

### ━━ [개념 Big Idea: 거장의 시각] ━━

**왜 치명적으로 중요한가:** NONMEM을 "실행하는" 사람과 NONMEM을 "제어하는" 사람의 차이는 바로 이 레코드 구조를 뼈대처럼 암기하고 있는가에 달려있다. 오류 메시지가 뜰 때 어느 레코드에서 문제가 생겼는지를 즉각 추적하지 못하면, 디버깅에 몇 시간을 낭비하게 된다.

**체화해야 할 단 하나의 직관:** 제어구문은 NONMEM에게 보내는 "작업 지시서"다 — "무엇을 분석할 것인지($PROB/$DATA/$INPUT)", "어떤 모델로 할 것인지($SUBROUTINE/$PK/$ERROR 또는 $PRED)", "어디서 시작할 것인지($THETA/$OMEGA/$SIGMA)", "어떻게 실행할 것인지($EST)", "무엇을 출력할 것인지($COV/$TABLE)"의 다섯 질문에 순서대로 답한다.

**이 직관을 머릿속에 박고 아래를 읽어라:** 제어구문의 각 레코드는 독립적으로 존재하지 않고, 위에서 아래로 흐르는 인과적 순서를 갖는다 — 이 순서를 먼저 장착하고 각 레코드의 세부 옵션을 익히면 암기가 아닌 이해로 체화된다.

---

**A. Formal Definition**

NONMEM 시스템은 세 구성요소로 이루어진다. **NM-TRAN**은 사용자가 작성한 제어구문을 파싱하여 문법·형식 오류를 검사하고 NONMEM이 읽을 수 있는 형태로 변환하는 번역기다. **PREDPP**는 집단약동학 모델링을 위해 미리 구축된 FORTRAN 서브루틴 라이브러리로, 다양한 PK 모델 구조(ADVAN)와 파라미터화(TRANS)를 제공한다. **NONMEM** 엔진 자체는 비선형 혼합효과 모델의 파라미터 추정을 수행하는 최적화 알고리즘의 핵심이다.

제어구문은 `$` 기호로 시작하는 레코드들의 연속이며, 각 레코드는 최소 3글자로 축약 가능하다(`$PROBLEM` → `$PROB`). NONMEM 7.2 이상에서는 대소문자 혼용이 허용되며, 세미콜론(`;`) 이후의 내용은 주석으로 처리된다.

---

**B. Derivation / Code Structure**

제어구문의 전형적 구조를 PIPET 코드 3.1(1구획 모델)을 기반으로 해부한다:

```
$PROB 1-compartment model                    ← 프로젝트 식별자 (자유 텍스트)

$INPUT ID TIME AMT RATE DUR DV MDV           ← 데이터셋 열 순서 선언
       WT AGE SEX HT RF ALB CLCR             (최대 50개 항목)

$DATA test.csv IGNORE=@                      ← 데이터 파일 경로 + 부분집합화
                                             IGNORE=@ : 비숫자 문자 행 제외
                                             IGNORE=# : # 포함 행 제외 (기본값)

$SUBR ADVAN1 TRANS2                          ← 모델 구조 선택
                                             ADVAN1=1구획 IV, TRANS2=CL·V 파라미터화

$PK
  V  = THETA(1)*EXP(ETA(1))                 ← 고정효과 + 개인간변이 정의
  CL = THETA(2)*EXP(ETA(2))
  S1 = V                                    ← 척도 파라미터: 단위 통일

$ERROR
  IPRED = F                                 ← F: NONMEM 내부 예측값
  W = SQRT(THETA(3)**2 + THETA(4)**2*IPRED**2)  ← 혼합 잔차 구조
  IRES  = DV - IPRED
  IWRES = IRES / W
  Y = IPRED + W*EPS(1)                      ← 최종 관찰값 예측 방정식

$THETA
  (0, 400)    ← THETA(1): V 초기값, 하한 0
  (0, 100)    ← THETA(2): CL 초기값
  0.0001 FIX  ← THETA(3): 가법변동 SD (고정)
  0.5         ← THETA(4): 비례변동 CV

$OMEGA  0.02  ← ω²_CL: ETA(1)의 분산
        0.02  ← ω²_V:  ETA(2)의 분산

$SIGMA  1 FIX ← EPS(1)의 분산=1로 고정 (W 통해 잔차 구조를 $THETA로 추정)

$ESTIMATION NOABORT MAXEVAL=9999 METHOD=1 INTER PRINT=5
$TABLE ID TIME AMT DV IPRED IRES CWRES ONEHEADER NOPRINT FILE=sdtab1001
$TABLE ID TIME AMT DV CL V ETA1 ETA2 ONEHEADER NOPRINT FILE=patab1001
```

`[출처: PIPET, Ch.3, p.29–30]`

Owen 교재의 동일한 구조를 대조하면:

```
$PROBLEM Example NM-TRAN Control Stream for a 1-cmt Model
$DATA /home/pathtomydataset/datafilename.dat IGNORE=#
$INPUT ID TIME AMT DV CMT EVID MDV
$SUBROUTINES ADVAN2 TRANS2
$PK
  TVCL = THETA(1)             ← TV(typical value) 관용 패턴: 공변량 확장 준비
  CL   = TVCL * EXP(ETA(1))
  TVV  = THETA(2)
  V    = TVV * EXP(ETA(2))
  TVKA = THETA(3)
  KA   = TVKA                 ← KA에 IIV 없음 (추정 안정성 고려)
  S2   = V/1000               ← 단위: dose(mg) / V(L) → Cp(ng/mL) 변환
$ERROR
  Y = F*(1 + EPS(1))          ← 순수 비례 잔차
$THETA (0,3.9) (0,52.1) (0,0.987)
$OMEGA (0.09) (0.16)
$SIGMA (0.04)
$EST METHOD=1 INTER MAXEVAL=9999 PRINT=5 MSFO=example.msf
$COVAR PRINT=E
```

`[출처: Owen, Ch.3, p.31]`

---

**C. Structural Necessity**

이 레코드 순서가 불가피한 이유: NM-TRAN은 위에서 아래로 순차 파싱한다. $DATA/$INPUT이 $PK보다 앞에 위치해야 하는 것은, $PK 내부에서 참조하는 공변량 변수(WT, AGE 등)가 먼저 선언되어 있어야 NM-TRAN이 undefined variable 오류 없이 컴파일할 수 있기 때문이다. 마찬가지로 $THETA/$OMEGA/$SIGMA는 $PK/$ERROR에서 THETA(n)/ETA(n)/EPS(n)으로 참조된 파라미터의 초기값을 제공하므로, 반드시 추정 레코드 이전에 위치해야 한다.

---

**D. Assumptions & Boundary Conditions**

- 데이터 파일은 순수 ASCII 텍스트여야 한다 (Word 같은 워드프로세서 형식 불가).
- 한 레코드의 최대 길이: 160자 (NONMEM 7 이상). 초과 시 줄 바꿈 후 계속.
- $INPUT 변수 목록: 최대 50개. 초과 변수는 `=DROP`으로 제거.
- `IGNORE=#`와 `IGNORE=(조건식)`은 동시 사용 가능; `ACCEPT`와 조건식 `IGNORE`는 동시 사용 불가.

---

**E. Limitations**

- 배치 실행 방식(batch mode)이므로 GUI가 없다 — 코드 오류가 실행 후에만 발견된다.
- 레코드 순서를 변경하면(예: $THETA를 $PK 앞에 배치) 파싱 오류가 발생한다.
- $TABLE 파일 이름 뒤 숫자(sdtab**1001**, patab**1001**)가 일치하지 않으면 Xpose4에서 결과 연결 실패.

---

**F. Five Cognitive Layers**

| 레이어 | 내용 |
|---|---|
| **L1 형식적 수학** | 제어구문은 비선형 혼합효과 모델 $y_{ij} = f(\theta, \eta_i, t_{ij}) + g(\theta, \eta_i, t_{ij})\cdot\varepsilon_{ij}$ 를 레코드로 분해한 것. $f$=$PK+구조모델, $g$=$ERROR, $\theta$=$THETA, $\eta$=$OMEGA, $\varepsilon$=$SIGMA |
| **L2 기하학적 직관** | 제어구문은 파라미터 공간의 탐색 경계를 설정한다 — THETA 하한(0)이 음수 CL 추정을 원천 봉쇄하고, MAXEVAL이 탐색 반경을 제한한다 |
| **L3 구조적 동일성** | Python 클래스 정의 구조: `$PK` = `__init__` (파라미터 초기화), `$ERROR` = 손실함수 정의, `$ESTIMATION` = `model.fit()` 호출 |
| **L4 생리학적 의미** | $INPUT의 공변량(WT, CLCR, ALB)은 생물학적 개체간변이의 "측정 가능한 원인"이며, $PK에서 TVCL 식에 연결되어 비측정 IIV(ETA)의 크기를 줄인다 |
| **L5 실무 투영** | sdtab/patab/catab/cotab 명명 관용은 Xpose4 자동 인식을 위한 것 — 이 규칙을 어기면 R의 `xpose.data()` 로딩이 실패한다 |

---

**G. Zettelkasten Atom**

```yaml
---
aliases: [NM-TRAN 제어구문, NONMEM control stream, 레코드 구조]
tags: [pharmacometrics/nonmem, nonmem/coding/controlstream]
up: "[[II-01 θ·η·ε 3층 계층 구조]]"
related: ["[[II-02 NONMEM 데이터셋]]", "[[II-04 General ADVAN]]", "[[II-05 초기추정값]]"]
source: "PIPET, Ch.3, pp.27–46 / Owen, Ch.3, pp.28–64"
---
```

NONMEM 제어구문은 $PROB → $DATA/$INPUT → 모델블록 → $THETA/$OMEGA/$SIGMA → $ESTIMATION → $COVARIANCE/$TABLE 의 불변 순서를 따른다. 각 레코드는 "무엇을 / 어떤 모델로 / 어디서 시작해 / 어떻게 실행하고 / 무엇을 출력하는가"라는 5개 질문에 순서대로 답한다. $TABLE 파일 번호는 Xpose4 연동을 위해 반드시 일치시켜야 한다.

---

---

## 카드 2: 특수 ADVAN + TRANS 조합 — 모델 구조와 파라미터화 선택 [⚡ Apex Concept]

---

### ━━ [개념 Big Idea: 거장의 시각] ━━

**왜 치명적으로 중요한가:** 임상 1상 시험의 경구 투여 2구획 데이터에 ADVAN3 대신 ADVAN4를 적용하거나, TRANS4 대신 TRANS1을 선택하면 파라미터 추정값의 생물학적 해석이 완전히 달라진다. IND(신약 개발 신청서) 제출용 모델에서 이 선택의 근거를 방어하지 못하면 FDA Deficiency Letter의 직접적 원인이 된다.

**체화해야 할 단 하나의 직관:** ADVAN은 "구획 구조와 투여 경로"를 선택하는 것이고, TRANS는 "그 구조를 어떤 언어(파라미터)로 표현할 것인가"를 선택하는 것이다 — 같은 생리학적 모델이 TRANS1에서는 속도상수($k_{10}$, $k_{12}$, $k_{21}$)로, TRANS4에서는 CL·V로 말해진다.

**이 직관을 머릿속에 박고 아래를 읽어라:** ADVAN = 구획 설계도, TRANS = 그 설계도를 읽는 언어 — 언어가 달라도 같은 구조를 나타낼 수 있지만, 언어마다 추정값의 해석과 초기값 설정 전략이 달라진다.

---

**A. Formal Definition**

특수 ADVAN(specific ADVAN)은 PREDPP 라이브러리에 미리 구현된 표준 PK 구획 모델 서브루틴이다. 구획 수와 투여 경로에 따라 선택하며, 일반 ADVAN 대비 실행 속도가 빠르다. TRANS 서브루틴은 동일한 ADVAN 구조를 서로 다른 파라미터 세트로 표현하는 재파라미터화 변환기다.

---

**B. Derivation / Code Structure**

**특수 ADVAN 선택 체계:**

| 구획 | IV 투여 | 경구(혈관 외) 투여 |
|---|---|---|
| 1구획 | ADVAN1 | ADVAN2 |
| 2구획 | ADVAN3 | ADVAN4 |
| 3구획 | ADVAN11 | ADVAN12 |
| 1구획 MM 비선형 | ADVAN10 | — |

`[출처: PIPET, Ch.4, p.47]`

**ADVAN4 TRANS4 — 2구획 경구 모델 완전 코드:**

```
$SUBROUTINES ADVAN4 TRANS4

$PK
  TVCL = THETA(1)                    ; 집단 CL (L/h)
  TVV2 = THETA(2)                    ; 집단 중심구획 V (L)
  TVV3 = THETA(3)                    ; 집단 말초구획 V (L)
  TVQ  = THETA(4)                    ; 집단 구획간 CL (L/h)
  TVKA = THETA(5)                    ; 집단 흡수속도상수 (1/h)

  CL = TVCL * EXP(ETA(1))           ; 개인별 CL: 로그정규 IIV
  V2 = TVV2 * EXP(ETA(2))           ; 개인별 중심구획 V
  V3 = TVV3 * EXP(ETA(3))           ; 개인별 말초구획 V
  Q  = TVQ  * EXP(ETA(4))           ; 개인별 구획간 CL
  KA = TVKA * EXP(ETA(5))           ; 개인별 흡수속도상수

  ALAG1 = THETA(6) * EXP(ETA(6))   ; 흡수지연시간 (선택적)
  S2 = V2 / 1000                    ; 척도: dose(mg) → Cp(μg/L=ng/mL) 변환
                                    ; KE, K23, K32는 TRANS4가 내부 자동 계산
```

`[출처: PIPET, Ch.4, pp.49–50]` `[출처: Owen, Ch.3, pp.36–39]`

**척도 파라미터(Sn) 단위 통일 공식:**

$$S_n = V \times \text{usv} \quad \text{단, usv} = \frac{\text{AMT 단위}}{\text{DV 단위} \times V \text{단위}}$$

예시: dose(mg), V(L), Cp(ng/mL = μg/L)인 경우:
$$\frac{\text{mg}}{\text{L} \times \text{usv}} = \frac{\text{ng}}{\text{mL}} \Rightarrow \text{usv} = \frac{1}{1000} \Rightarrow S2 = \frac{V2}{1000}$$

`[출처: Owen, Ch.3, p.41, Eq.3.6]`

**TRANS 선택에 따른 필수 파라미터 비교 (ADVAN4):**

| TRANS | 필수 파라미터 | 특징 |
|---|---|---|
| TRANS1 | K, K23, K32, KA | 속도상수 직접 추정. 생물학적 해석 어려움 |
| TRANS3 | CL, V, Q, VSS, KA | VSS = 정상상태 분포용적 사용 |
| **TRANS4** | **CL, V2, Q, V3, KA** | **CL·V 파라미터화. 임상 보고 표준. 가장 많이 사용** |
| TRANS5 | AOB, ALPHA, BETA, KA | 거시적 지수 파라미터 |
| TRANS6 | ALPHA, BETA, K32, KA | 혼합 파라미터화 |

`[출처: PIPET, Ch.3, pp.32–33 표 3.1]`

**ADVAN5 vs ADVAN6 — 일반 ADVAN 선택:**

```
; ADVAN5: 선형 일반 ADVAN — $DES 불필요, 1차 속도상수만
$SUBROUTINE ADVAN5
$MODEL
  COMP(DEPOT, DEFDOSE)     ; 구획 1: 저장소 (투여구획)
  COMP(CENT, DEFOBS)       ; 구획 2: 중심 (관찰구획)
  COMP(PERI)               ; 구획 3: 말초
$PK
  K12 = KA                 ; ADVAN5에서는 속도상수로 구획간 이동 정의
  K20 = CL/V2
  K23 = Q/V2
  K32 = Q/V3

; ADVAN6: 비선형 일반 ADVAN — $DES 필수, TOL= 반드시 지정
$SUBROUTINE ADVAN6 TOL=4   ; TOL 없으면 실행 자체 불가
$MODEL
  COMP(DEPOT, DEFDOSE)
  COMP(CENTRAL, DEFOBS)
  COMP(PERIPH)
$PK
  KE = CL/V2
  K12 = Q/V2
  K21 = Q/V3
$DES
  DADT(1) = -KA*A(1)
  DADT(2) = KA*A(1) - KE*A(2) - K12*A(2) + K21*A(3)
  DADT(3) = K12*A(2) - K21*A(3)
```

`[출처: PIPET, Ch.3, pp.41–44]`

---

**C. Structural Necessity + C-2 Plausible Fallacy**

ADVAN+TRANS 조합이 이 구조를 가져야 하는 이유: NONMEM이 PREDPP를 호출할 때, ADVAN이 어떤 구획 구조(몇 개의 미분방정식, 어떤 경계조건)를 쓸지를 결정하고, TRANS가 그 구획 구조의 파라미터를 사용자가 지정한 기호(CL, V, Q 등)로부터 내부 속도상수로 변환한다. TRANS4는 $SUBROUTINES 레코드 파싱 시 자동으로 $K = CL/V2$, $K_{23} = Q/V2$, $K_{32} = Q/V3$ 변환식을 컴파일하며, 사용자는 $PK 블록에 이 변환식을 직접 쓸 필요가 없다. 이 변환이 내부에서 일어나기 때문에, 사용자가 $PK에 직접 KE=CL/V2를 작성하지 않아도 NONMEM은 올바르게 동작한다.

**[C-2 Plausible Fallacy — Apex Concept 적용]**

**오류의 형태:** 초보 모델러가 ADVAN4 TRANS4를 사용하면서 $PK 블록 안에 `KE = CL/V2`, `K23 = Q/V2`, `K32 = Q/V3`를 명시적으로 추가로 기술하는 경우. "투명하게 모든 파라미터를 선언해야 안전하다"는 직관적 믿음에서 비롯된다.

**나비효과:** TRANS4는 이미 내부에서 이 변환을 수행하므로, 사용자가 $PK에 동일한 변환을 다시 쓰면 파라미터가 이중 정의(double definition)된다. NONMEM은 오류 메시지를 출력하거나, 더 위험하게는 사용자 정의값이 PREDPP 내부 계산값을 덮어쓰면서 두 정의가 충돌하여 예측값 F가 완전히 틀린 값으로 계산된다. 이때 GOF 플롯에서 CWRES가 체계적으로 음(-)의 방향으로 편향되는 "하강 파형 패턴"이 나타난다.

**진단 GOF 시그니처: "TRANS 이중 선언 편향 파형"** — CWRES vs TIME 플롯에서 투여 직후 구간에 체계적 음의 편향, DV vs IPRED 플롯에서 대각선 위쪽에 점들이 집중(모델이 농도를 과소추정).

---

**D. Assumptions & Boundary Conditions**

- 특수 ADVAN은 구획 간 이동이 1차 속도상수를 따른다고 가정. 비선형 분포 과정(예: receptor-mediated endocytosis)에는 부적합.
- ADVAN10(MM 비선형 흡수)을 제외한 특수 ADVAN은 $DES 블록 사용 불가.
- ADVAN5/7은 선형 모델 전용 → 비선형 소실 모델링 시 ADVAN6/8/9/13으로 전환 필수.

---

**E. Limitations**

- 특수 ADVAN은 사전 정의된 구획 구조만 지원 → 장간순환(enterohepatic circulation), 모약물-대사체 동시 분석 등 복잡 구조에는 일반 ADVAN 필요.
- TRANS4 파라미터화는 CL, V2, Q, V3를 독립적으로 추정하므로, VSS를 직접 추정하려면 TRANS3를 선택해야 한다.
- 실행 속도: 특수 ADVAN > 일반 ADVAN (ADVAN5/7) > 일반 비선형 ADVAN (ADVAN6/8/9/13).

---

**F. Five Cognitive Layers**

| 레이어 | 내용 |
|---|---|
| **L1 형식적 수학** | ADVAN4 TRANS4의 내부 변환: $k_{10} = CL/V_2$, $k_{23} = Q/V_2$, $k_{32} = Q/V_3$. 2구획 경구 모델 미분방정식: $\frac{dA_1}{dt} = -k_a A_1$, $\frac{dA_2}{dt} = k_a A_1 - (k_{10}+k_{23})A_2 + k_{32}A_3$, $\frac{dA_3}{dt} = k_{23}A_2 - k_{32}A_3$ |
| **L2 기하학적 직관** | Log-농도 vs 시간 그래프에서 직선 하나 → 1구획(ADVAN1/2), 꺾이는 두 직선 → 2구획(ADVAN3/4). α상(분포상)의 기울기가 가파를수록 말초로의 분포가 빠름 |
| **L3 구조적 동일성** | ADVAN = 전기회로 토폴로지 선택(직렬/병렬), TRANS = 그 회로를 R·C 값으로 표현하느냐 임피던스 값으로 표현하느냐의 파라미터화 선택 |
| **L4 생리학적 의미** | V2 = 혈액+혈관풍부조직의 겉보기 부피, V3 = 근육·지방 등 말초 조직의 겉보기 부피, Q = 혈액과 말초 사이의 물질교환 속도(=장기 관류량 근사) |
| **L5 실무 투영** | TRANS4 사용 시 S2=V2/1000 (dose:mg, Cp:ng/mL) 또는 S2=V2 (dose:mg, Cp:mg/L) — 단위 불일치는 CWRES 전체 체계적 편향의 주범. 규제 제출 시 파라미터 단위 명시 필수 |

---

**G. Zettelkasten Atom**

```yaml
---
aliases: [특수 ADVAN, specific ADVAN, TRANS 서브루틴, 척도 파라미터]
tags: [pharmacometrics/nonmem, nonmem/coding/advan, nonmem/coding/trans]
up: "[[II-03 제어구문 레코드 구조]]"
related: ["[[II-04 General ADVAN DES]]", "[[S2 단위 통일]]"]
source: "PIPET, Ch.3–4, pp.32–53 / Owen, Ch.3, pp.35–44"
---
```

특수 ADVAN은 구획 수·투여 경로를 선택하고, TRANS는 그 구조를 어떤 파라미터 언어로 표현할지를 결정한다. TRANS4 선택 시 $PK에 KE=CL/V2 등의 변환식을 중복 기술하면 이중 정의 충돌이 발생한다. 척도 파라미터 S2=V2/1000은 dose(mg)과 Cp(ng/mL) 단위 불일치 해소를 위한 필수 코드다.

---

---

## 카드 3: $PRED — ADVAN을 쓰지 않는 코딩

---

### ━━ [개념 Big Idea: 거장의 시각] ━━

**왜 치명적으로 중요한가:** PK/PD 모델링에서 Emax, Sigmoid-Emax, QTc-농도 관계, 생체지표 반응 모델 등 약동학이 아닌 약력학 또는 통계적 관계를 NONMEM으로 추정할 때, ADVAN 체계로는 표현할 수 없는 경우가 빈번하다. 이때 $PRED를 모르면 NONMEM 사용 범위가 PK로만 제한되고, PK/PD 통합 모델링에서 주도권을 잃는다.

**체화해야 할 단 하나의 직관:** $PRED는 NONMEM에게 "PK 패키지를 내려놓고, 내가 직접 수식을 쓸게"라고 선언하는 것이다 — 그 대가로 AMT, CMT 같은 PREDPP 약속어가 사라지고, 데이터셋에서 용량을 매 행마다 공변량처럼 반복 입력해야 한다.

**이 직관을 머릿속에 박고 아래를 읽어라:** $PRED는 자유도가 높지만 그만큼 책임이 무겁다 — 미분방정식 풀이가 없으므로 해석해(closed-form solution)를 직접 라플라스 변환 등으로 도출하여 넣어야 한다.

---

**A. Formal Definition**

`$PRED`는 PREDPP 라이브러리를 사용하지 않고, 연구자가 원하는 임의의 수식을 직접 기술하여 예측값을 계산하는 서브루틴 블록이다. $SUBROUTINE, $MODEL, $PK, $DES, $ERROR 레코드 전체를 대체한다. 약속된 용어(reserved word)가 없으므로 파라미터 이름을 완전히 자유롭게 지정할 수 있다.

---

**B. Derivation / Code Structure**

**ADVAN2 vs $PRED — 1구획 경구 모델 비교 (PIPET 그림 7.1 기반):**

```
; === ADVAN2 방식 ===
$SUBROUTINE ADVAN2 TRANS2
$PK
  CL = THETA(1)*EXP(ETA(1))
  V  = THETA(2)*EXP(ETA(2))
  KA = THETA(3)*EXP(ETA(3))
  S2 = V
$ERROR
  IPRED = F
  IRES  = DV - IPRED
  W = SQRT(THETA(4)**2 + THETA(5)**2*IPRED**2)
  IWRES = IRES/W
  Y = F + W*EPS(1)

; === $PRED 방식 — 동일 모델을 해석해로 직접 기술 ===
$PRED
  TVCO = THETA(1)                    ; 집단 CL/V (소실 지수)
  TVEX = THETA(2)                    ; 집단 V (분포용적)
  TVKA = THETA(3)                    ; 집단 KA

  COEF = TVCO * EXP(ETA(1))         ; 개인별 계수 (= CL/(V*(KA-CL/V)))
  EXPO = TVEX * EXP(ETA(2))         ; 개인별 소실 지수 (= CL/V = k10)
  KA   = TVKA * EXP(ETA(3))        ; 개인별 흡수속도상수

  ; 1구획 경구 해석해:
  ; C(t) = Dose * (KA/(KA-k10)) * (exp(-k10*t) - exp(-KA*t)) / V
  IPRED = D*COEF*KA/(KA-EXPO)*(EXP(-EXPO*T)-EXP(-KA*T))

  IRES  = DV - IPRED
  IWRES = IRES/IPRED
  Y = IPRED*(1 + EPS(1)) + EPS(2)   ; $PRED에서는 $ERROR 없이 Y를 여기서 정의
```

`[출처: PIPET, Ch.7, pp.69–70]`

**$PRED 전용 데이터셋 구조 차이:**

ADVAN2 방식에서 `AMT`는 0시간에 한 번만 입력하면 PREDPP가 이후 시간 내내 그 투여를 "기억"한다. 반면 $PRED에서는 용량(D)이 약속어가 아니므로, 데이터셋의 모든 관찰 행에 용량 값을 공변량처럼 반복 기재해야 한다.

```
; $PRED 데이터셋 (모든 행에 AMT=150000 반복)
#ID  TIME   AMT     DV      MDV
  1   0      150000  0       0
  1   0.25   150000  .       1
  1   0.5    150000  55.51   0
  1   0.75   150000  348.7   0
  ...
```

`[출처: PIPET, Ch.7, p.70 그림 7.2]`

**Sigmoidal-Emax PD 모델 — $PRED 완전 코드:**

```
$PROB Sigmoidal PD Model
$DATA ../sigmoidal_effect.csv IGNORE=@
$INPUT ID CP RESP=DV              ; CP=혈중농도, RESP=약효 반응(DV로 재명명)

$PRED
  E0   = THETA(1)                ; 기저효과
  EMAX = THETA(2)                ; 최대효과
  C50  = THETA(3)*EXP(ETA(1))   ; EC50 (IIV 있음)
  GAM  = THETA(4)                ; Hill 계수 (IIV 추정 어려움 — 수렴 불안정)

  IPRD = E0 + (EMAX-E0)*CP**GAM / (CP**GAM + C50**GAM)
  Y    = IPRD + EPS(1)           ; 가법 잔차

$THETA  ...
$OMEGA  0.04
$EST PRINT=5 MAX=9999 SIG=3
```

`[출처: PIPET, Ch.7, p.71 코드 7.1]`

Owen 교재의 $PRED 예시 — Emax 모델:

```
$PRED
  BSLN  = THETA(3) + ETA(3)         ; THETA와 ETA 첨자가 반드시 일치할 필요 없음
  TVEMX = THETA(1)
  EMAX  = TVEMX*EXP(ETA(2))
  TVD50 = THETA(2)
  ED50  = TVD50*EXP(ETA(1))
  NUM   = EMAX*DOSE
  DEN   = ED50 + DOSE
  RESP  = BSLN*(1 + NUM/DEN)
  Y     = RESP + EPS(1)
```

`[출처: Owen, Ch.3, p.49]`

---

**C. Structural Necessity**

$PRED가 이 구조를 가져야 하는 이유: PREDPP를 호출하지 않으면 NONMEM의 내부 시간 적분 엔진이 동작하지 않는다. 따라서 모든 시점에서의 예측값을 사용자가 해석해로 직접 계산하고, 최종적으로 `Y`를 정의하여 NONMEM의 목적함수 계산기에 전달해야 한다. `Y`는 $ERROR 블록의 역할(잔차 구조 정의)을 $PRED 내부에서 동시에 수행한다.

---

**D. Assumptions & Boundary Conditions**

- 미분방정식 형태의 모델에는 사용 불가 — 해석해가 존재해야 함.
- 용량은 데이터셋의 모든 관찰 행에 상수로 존재해야 함 (PREDPP의 AMT 약속어 메커니즘 없음).
- $PRED와 $SUBROUTINE은 같은 제어구문에 공존 불가.

---

**E. Limitations**

- 복잡한 다구획 PK에는 해석해가 없거나 매우 복잡 → 실제 사용은 PD 모델, 간단한 1구획 검증, 비-PK 관계 모델링에 국한.
- 다회투여(multiple dosing), 추가 투여(ADDL), 항정상태(SS) 처리가 PREDPP 기반보다 훨씬 복잡 → 수동 중첩(superposition) 코딩 필요.

---

**F. Five Cognitive Layers**

| 레이어 | 내용 |
|---|---|
| **L1 형식적 수학** | 1구획 경구 해석해: $C(t) = \frac{D \cdot k_a}{V(k_a - k_{10})}\left(e^{-k_{10}t} - e^{-k_a t}\right)$. $PRED 코드의 IPRED 라인이 이 수식의 직접 FORTRAN 번역 |
| **L2 기하학적 직관** | $PRED 모델은 파라미터 공간의 탐색 경계가 없다 — THETA 하한을 설정하지 않으면 음수 EC50도 탐색 대상이 됨 |
| **L3 구조적 동일성** | $PRED = 통계학의 일반선형모델(GLM) 커스텀 링크 함수 — Y = g(θ, x) + ε 형태를 사용자가 직접 정의 |
| **L4 생리학적 의미** | $PRED의 Sigmoidal-Emax 모델에서 GAM(Hill 계수)은 수용체 협동성(cooperativity)의 정량적 지표 — GAM>1: 양성 협동, GAM<1: 음성 협동, GAM=1: Langmuir 등온흡착 |
| **L5 실무 투영** | IND/NDA PK/PD 섹션에서 $PRED를 이용한 QTc-노출 관계 분석이 규제 표준(ICH E14 guidance follow-up)으로 자리잡음 — Hill 계수와 EC50의 RSE%가 핵심 보고 수치 |

---

**G. Zettelkasten Atom**

```yaml
---
aliases: [$PRED 블록, PRED 모델링, PREDPP 없는 코딩]
tags: [pharmacometrics/nonmem, nonmem/coding/pred, pd-modeling]
up: "[[II-03 특수 ADVAN TRANS]]"
related: ["[[II-11 PK/PD NONMEM 구현]]", "[[I-09 Emax Hill PD 모델 기초]]"]
source: "PIPET, Ch.7, pp.69–71 / Owen, Ch.3, pp.48–49"
---
```

$PRED는 PREDPP 라이브러리 전체를 대체하는 자유 코딩 블록으로, PD 모델·비-PK 관계·해석해가 존재하는 단순 PK에 사용한다. ADVAN과 달리 용량을 데이터셋 모든 행에 공변량으로 반복 기재해야 하며, $ERROR 없이 $PRED 내부에서 Y를 직접 정의한다.

---

---

## 카드 4: $ERROR 잔차변이 구조와 $THETA/$OMEGA/$SIGMA 초기값 전략

---

### ━━ [개념 Big Idea: 거장의 시각] ━━

**왜 치명적으로 중요한가:** 잔차변이 구조를 잘못 선택하면 — 예를 들어 고농도에서 비례오차가 지배적임에도 가법오차 모델을 적용하면 — CWRES가 농도에 비례하여 증가하는 깔때기 패턴이 나타나고, $OMEGA 추정값이 과대추정되어 PopPK 보고서의 모든 하위 분석(시뮬레이션, VPC)이 오염된다.

**체화해야 할 단 하나의 직관:** $ERROR는 "측정 오차의 성격"을 모델링하는 것이다 — 측정값의 절대 오차가 농도와 무관하면 가법(additive), 농도에 비례하면 비례(proportional/CCV), 둘 다라면 혼합(combined) 모델.

**이 직관을 머릿속에 박고 아래를 읽어라:** 실제 분석 데이터에서 저농도 샘플(검출 한계 근처)에는 가법 오차가 지배적이고, 고농도에서는 비례 오차가 지배적인 경우가 많다 — 이것이 혼합 잔차 모델을 권장하는 생물학적 이유다.

---

**A. Formal Definition**

$ERROR 블록은 관찰값(DV)과 개인 예측값(F 또는 IPRED) 사이의 잔차 변이(residual variability, RV)를 기술하는 코드 블록이다. 잔차는 측정 내 개인간변이(intraindividual variability), 분석 오차(assay variability), 모델 오명세(model misspecification), 데이터 오차의 복합체다.

---

**B. Derivation / Code Structure**

**주요 잔차 구조 코드:**

```
; 1. 가법(additive) 잔차 — 저농도 데이터, 절대 측정 오차 일정
$ERROR
  Y = F + EPS(1)
  ; Var(Y) = σ²: 농도와 무관한 등분산

; 2. 비례(CCV/proportional) 잔차 — 고농도 데이터, 상대 오차 일정
$ERROR
  Y = F*(1 + EPS(1))
  ; Var(Y) = F²·σ²: 농도에 비례하는 이분산

; 3. 혼합(combined) 잔차 — 가장 현실적, 권장
$ERROR
  Y = F + EPS(1) + F*EPS(2)
  ; Var(Y) = σ₁² + F²·σ₂²

; 4. W 함수를 이용한 혼합 잔차 (SIGMA 1 FIX 패턴)
$ERROR
  IPRED = F
  W = SQRT(THETA(3)**2 + THETA(4)**2*IPRED**2)
  IRES  = DV - IPRED
  IWRES = IRES/W
  Y = IPRED + W*EPS(1)
; 여기서 THETA(3) = 가법 SD, THETA(4) = 비례 CV
; $SIGMA 1 FIX — W가 이미 잔차 크기 조절, SIGMA=1은 정규화
```

`[출처: PIPET, Ch.3, pp.36–37]` `[출처: Owen, Ch.3, pp.45–47]`

**$OMEGA 초기값 결정 공식:**

$$\omega^2 = \left(\frac{\%CV}{100}\right)^2$$

예: CL의 IIV가 약 30%CV로 예상될 때 → $OMEGA(CL) = (30/100)² = 0.09

```
$OMEGA 0.09   ; CL IIV ~30%CV 추정
       0.2025  ; V  IIV ~45%CV 추정
```

`[출처: Owen, Ch.3, p.53]`

**$OMEGA BLOCK — ETA 간 공분산 추정:**

$$\omega_{2,1} = \rho_{1,2} \times \sqrt{\omega_{1,1}^2} \times \sqrt{\omega_{2,2}^2}$$

```
$OMEGA BLOCK(2)    ; CL과 V 간 공분산 추정
  0.09             ; ω²_CL
  0.03 0.16        ; ω_CL,V (공분산), ω²_V
```

`[출처: Owen, Ch.3, p.53]`

---

**C. Structural Necessity**

EXP(ETA) 형태의 IIV 모델이 `*(1+ETA)` 형태보다 선호되는 수학적 이유: 지수 모델에서 ETA가 아무리 큰 음수여도 CL_i = TVCL·exp(ETA) > 0이 항상 보장된다. 반면 비례 모델 CL = TVCL·(1+ETA)에서 ETA < -1이면 음수 CL이 발생한다. 약동학 파라미터는 물리적으로 양수만 허용되므로, 지수 모델이 구조적으로 필수다.

---

**D. Assumptions & Boundary Conditions**

- $OMEGA와 $SIGMA의 초기값은 분산(variance)으로 입력 — 표준편차(SD)가 아님.
- $OMEGA/$SIGMA에 0을 사용하려면 반드시 FIX가 필요 (추정 0은 경계값 오류 발생).
- $OMEGA BLOCK에서 FIXED가 하나라도 있으면 블록 전체가 FIXED로 처리됨.

---

**E. Limitations**

- 로그오차(log-error) 모델은 F=0(투여 직전, 투여 후 극장시간)에서 수학적 오류 발생 → FLAG=0/1 조건 코딩 또는 CALLFL=0 옵션 필요.
- 혼합 잔차 모델에서 THETA(additive)와 THETA(proportional) 동시 추정은 파라미터 상관이 높아 수렴 불안정 — 시뮬레이션 기반 초기값 탐색 권장.

---

**F. Five Cognitive Layers**

| 레이어 | 내용 |
|---|---|
| **L1 형식적 수학** | 비례 잔차 모델의 %CV 도출: $Y = F(1+\varepsilon)$ → $\text{Var}(Y) = F^2\sigma^2$ → $\text{SD}(Y)/E(Y) = \sigma$ → $\%CV = \sigma \times 100$ |
| **L2 기하학적 직관** | CWRES vs IPRED 플롯에서 깔때기 모양(funnel pattern): 저예측값에서는 오차 작고 고예측값에서는 오차 큰 패턴 → 가법 잔차 모델 오명세의 시각 시그니처 |
| **L3 구조적 동일성** | $ERROR의 W 함수 = 통계학의 가중최소제곱(WLS)에서 가중치 행렬의 대각원소 — NONMEM은 IWRES=IRES/W를 최소화하는 방향으로 파라미터를 조정 |
| **L4 생리학적 의미** | 비례 오차 성분은 분석기기(immunoassay, LC-MS/MS)의 신호-대-잡음비에서, 가법 오차 성분은 LLOQ 근처의 배경 잡음에서 기원한다 |
| **L5 실무 투영** | FDA/EMA PopPK 리뷰어는 $OMEGA과 $SIGMA의 %CV 환산값이 파라미터 추정치와 함께 보고서에 명시되어 있는지 확인한다. RSE% = SE/추정값 × 100도 같이 보고 필수 |

---

**G. Zettelkasten Atom**

```yaml
---
aliases: [$ERROR 블록, 잔차변이 구조, 혼합 잔차, W함수, OMEGA BLOCK]
tags: [pharmacometrics/nonmem, nonmem/coding/error, residual-variability]
up: "[[II-03 특수 ADVAN TRANS]]"
related: ["[[II-06 추정 방법론 OFV]]", "[[II-09b $COVARIANCE SE/RSE]]"]
source: "PIPET, Ch.3, pp.35–37 / Owen, Ch.3, pp.44–55"
---
```

$ERROR 잔차 구조는 측정 오차의 성격(가법/비례/혼합)에 맞게 선택해야 하며, W 함수 + SIGMA 1 FIX 패턴이 현장에서 가장 많이 쓰이는 혼합 잔차 구현이다. $OMEGA 초기값은 예상 IIV(%CV/100)²로 역산하고, ETA 간 공분산이 예상되면 $OMEGA BLOCK으로 추정한다.

---

---

# §5 — 혼동 쌍 해부

---

## 혼동 쌍 1: 특수 ADVAN vs 일반 ADVAN (ADVAN5/6)

| 비교 차원 | 특수 ADVAN (ADVAN1–4, 10–12) | 일반 ADVAN (ADVAN5/6/7/8/9/13) |
|---|---|---|
| **표면적 유사성** | 둘 다 $SUBROUTINE에서 선택하고 $PK를 사용 | |
| **수식/코드 형태** | `$SUBR ADVAN4 TRANS4` → $MODEL, $DES 불필요 | `$SUBR ADVAN6 TOL=4` → $MODEL + $DES 필수 |
| **구조적 지시체** | 미리 구현된 표준 PK 구획 모델 (1/2/3구획, IV/경구) | 사용자가 $MODEL로 구획 정의 + $DES로 ODE 직접 기술 |
| **변화 방향** | 모델 구조 변경 시 ADVAN 번호 바꿔야 함 (경직성) | $DES 내 ODE 수정만으로 모델 구조 유연하게 변경 가능 |
| **임상/모델링 결과** | 모약물-대사체 동시 분석, Michaelis-Menten 비선형 소실, 장간순환 모델에 특수 ADVAN을 고집하면 모델 구현 자체가 불가능 | |
| **⚡ 기억 고리** | 특수 ADVAN은 "기성복" — 빠르고 편하지만 치수(구조)가 고정되어 있다. 일반 ADVAN은 "맞춤복" — 느리고 손이 많이 가지만 어떤 체형(모델)도 소화한다. 비선형 소실이 보이는 순간 기성복 진열대를 벗어나야 한다. | |

---

## 혼동 쌍 2: $PK 블록의 ETA 지수 모델 vs 비례 모델

| 비교 차원 | 지수(exponential) IIV 모델 | 비례(proportional/CCV) IIV 모델 |
|---|---|---|
| **표면적 유사성** | 둘 다 개인간변이를 표현하며, FO 근사 하에서 수학적으로 동치 | |
| **수식/코드 형태** | `CL = TVCL * EXP(ETA(1))` → $CL_i = TVCL \cdot e^{\eta_i}$ | `CL = TVCL * (1 + ETA(1))` → $CL_i = TVCL \cdot (1+\eta_i)$ |
| **구조적 지시체** | 개인 파라미터가 **로그정규분포** 따름 → 항상 양수 보장 | 개인 파라미터가 **정규분포** 따름 → ETA<-1일 때 음수 가능 |
| **변화 방향** | ETA가 극단적 음수여도 CL_i > 0 항상 유지 | ETA < -1이면 CL_i < 0 발생 → 추정 오류 또는 비현실적 결과 |
| **임상/모델링 결과** | 비례 모델을 사용하면 FOCE 추정 시 음수 파라미터 발생 가능, $COV step 실패로 이어질 수 있음 | |
| **⚡ 기억 고리** | "지수는 울타리, 비례는 열린 벌판" — 지수 모델은 ETA가 아무리 작아도 파라미터가 0 아래로 내려가지 못하도록 울타리를 친다. 비례 모델은 ETA가 -1.1이 되는 순간 울타리 밖(음수 CL)으로 나가버린다. |  |

---

## 혼동 쌍 3: $SIGMA vs $THETA를 통한 잔차 추정 [Critical Blow 적용]

| 비교 차원 | $SIGMA 직접 추정 | $THETA로 추정 + $SIGMA 1 FIX |
|---|---|---|
| **표면적 유사성** | 둘 다 잔차변이의 크기를 NONMEM으로 추정 | |
| **수식/코드 형태** | `Y=F*(1+EPS(1))` + `$SIGMA 0.04` → σ²=0.04 추정 | `W=SQRT(THETA(3)**2+THETA(4)**2*IPRED**2)` + `$SIGMA 1 FIX` → THETA(3)=가법 SD, THETA(4)=비례 CV 추정 |
| **구조적 지시체** | σ² = **분산**값이 추정됨 (단위: 농도²) | THETA(3), THETA(4) = **표준편차/CV 값**이 추정됨 (단위: 농도 또는 무단위) |
| **변화 방향** | 잔차 구조 변경 시 $SIGMA 행렬 구조를 바꿔야 함 | W 식만 수정하면 어떤 잔차 구조든 유연하게 표현 가능 |
| **임상/모델링 결과** | **$SIGMA 0.04에서 %CV를 계산할 때: $CV = \sqrt{0.04} \times 100 = 20\%$임을 모르고 "잔차변이가 4%"라고 보고서에 기재하면 FDA 리뷰어의 Deficiency Letter 직접 사유** | |
| **치명적 타격** | $SIGMA 추정값을 "%CV"라고 오인하여 NDA 임상약리 섹션에 "잔차변이 4%(sigma=0.04)"로 보고하면, 실제 20%CV를 4%CV로 5배 과소 보고하는 오류가 발생하며, 이는 모델 적합도의 심각한 허위 진술로서 심사관의 Complete Response Letter(CRL) 발행 사유에 해당한다. |
| **⚡ 기억 고리** | "$SIGMA는 분산의 창고, %CV를 보려면 제곱근을 꺼내야 한다. $THETA로 추정할 때는 이미 SD/CV 값이 나오므로 그대로 보고한다." | |

---

---

# §7 — Self-Test: Active Recall Module

---

**Q1 (회상 ○)** NONMEM 시스템의 세 구성요소인 NM-TRAN, PREDPP, NONMEM 각각의 역할을 한 문장으로 설명하라.

<details><summary>정답 공개</summary>

**NM-TRAN**: 사용자 제어구문을 파싱·문법검사하여 NONMEM이 읽을 수 있는 형태로 변환하는 번역기.
**PREDPP**: 집단약동학 모델링을 위한 표준 PK 구획 모델 서브루틴(ADVAN) 라이브러리.
**NONMEM**: 비선형 혼합효과 모델의 목적함수 최소화를 통한 파라미터 추정 엔진.

**다음 깊이 질문:** NM-TRAN이 $PK 블록을 FORTRAN 서브루틴으로 변환하는 과정에서, 사용자가 정의한 TVCL 같은 사용자 변수와 NONMEM 예약어(F, Y, ETA 등)를 어떻게 구분하는가?

</details>

---

**Q2 (회상 ★) ADVAN4 TRANS4를 선택했을 때 $PK에 반드시 정의해야 하는 필수 파라미터 5가지를 나열하고, 각각의 생리학적 의미를 기술하라.**

<details><summary>정답 공개</summary>

CL(청소율), V2(중심구획 분포용적), Q(구획간 청소율), V3(말초구획 분포용적), KA(흡수속도상수). CL은 단위시간당 약물이 완전히 제거되는 가상 혈액 부피, V2는 중심구획의 겉보기 분포용적, Q는 중심-말초 간 약물 교환 속도, V3는 말초조직의 겉보기 분포용적, KA는 흡수 부위에서 중심구획으로의 1차 흡수속도상수.

**다음 깊이 질문:** ADVAN4 TRANS4에서 Ke(소실속도상수)를 출력 테이블에 포함시키려면 어떻게 $PK 코드를 작성해야 하는가?

</details>

---

**Q3 (적용 ★★) 투여 용량 단위가 mg, 분포용적 V2의 단위가 L, 관찰 혈중농도 단위가 ng/mL일 때, $PK 블록에서 척도 파라미터 S2를 어떻게 정의해야 하는가? 수식적 근거를 포함하여 설명하라.**

<details><summary>정답 공개</summary>

`S2 = V2/1000`

근거: $C = \text{Amount}/V$에서 Amount의 단위가 mg, V의 단위가 L이면 C의 단위는 mg/L. 그러나 DV는 ng/mL = μg/L이므로, 1 mg/L = 1000 ng/mL 관계에서 분모를 1000배 키워 예측 농도 단위를 DV 단위와 일치시킨다. 즉 S2 = V2 × (1/1000) = V2/1000.

**다음 깊이 질문:** 만약 용량을 μg 단위로 AMT 열에 기재하고 농도를 ng/mL로 관찰한다면, S2는 어떻게 달라지는가?

</details>

---

**Q4 (적용 ★) 다음 $ERROR 코드에서 THETA(4)로 추정되는 값의 통계적 의미와 단위를 설명하라:**

```
W = SQRT(THETA(3)**2 + THETA(4)**2 * IPRED**2)
Y = IPRED + W * EPS(1)
$SIGMA 1 FIX
```

<details><summary>정답 공개</summary>

THETA(3)는 가법 잔차의 표준편차(SD, 단위: 농도 단위와 동일), THETA(4)는 비례 잔차의 변동계수(CV, 무단위 또는 소수 형태). $SIGMA를 1로 고정하여 EPS(1)의 분산=1로 표준화했으므로, W 전체가 잔차의 표준편차를 나타낸다. 예를 들어 THETA(4)=0.2이면 비례 잔차 CV=20%를 의미한다.

**다음 깊이 질문:** 이 코드에서 THETA(3)의 추정값이 0에 매우 가깝게 수렴한다면, 데이터와 모델에 대해 어떤 결론을 내릴 수 있는가?

</details>

---

**Q5 (적용 ★) $PRED를 사용하는 모델에서 ADVAN 기반 모델과 가장 큰 데이터셋 차이점은 무엇이며, 그 이유를 PREDPP 메커니즘 관점에서 설명하라.**

<details><summary>정답 공개</summary>

ADVAN 모델에서는 AMT(투여량)가 투여 시점에 한 번만 기재되어도 PREDPP가 이후 모든 시점에서 그 투여 이벤트를 "기억"하며 구획 내 약물량을 적분한다. $PRED에서는 PREDPP 적분 엔진이 동작하지 않으므로, 수식 내 용량 변수(예: D)가 모든 관찰 행에서 참조되어야 한다 — 마치 시간에 따라 변하지 않는 공변량처럼 모든 행에 동일한 투여량을 반복 기재해야 한다.

**다음 깊이 질문:** 다회투여(multiple dosing) 데이터에서 $PRED를 사용하여 각 투여 후 중첩(superposition)을 구현하려면 어떤 코딩이 필요한가?

</details>

---

**Q6 (회상 ○) $OMEGA 0.09의 의미를 %CV로 변환하고, 이것이 어떤 PK 파라미터의 IIV 크기를 반영하는지 임상적으로 해석하라.**

<details><summary>정답 공개</summary>

$OMEGA 0.09 → ω² = 0.09 → ω = 0.3 → %CV = 30%. 이는 집단 전체에서 해당 PK 파라미터(예: CL)의 개인별 값이 집단 대표값을 중심으로 약 ±30%의 변동을 갖는다는 의미다. 임상적으로, 동일 용량 투여 시 환자 간 노출(AUC)의 변동성이 약 30% 수준임을 시사한다.

**다음 깊이 질문:** η-shrinkage가 > 30%인 경우, 이 $OMEGA 추정값의 신뢰성에 대해 어떤 우려가 발생하는가?

</details>

---

**Q7 (적용 ★) ADVAN6을 선택할 때 $SUBROUTINE에 TOL=n 옵션이 필수인 이유를 ODE 수치 적분 관점에서 설명하고, TOL 값이 너무 크면 어떤 문제가 발생하는지 서술하라.**

<details><summary>정답 공개</summary>

ADVAN6은 비선형 ODE를 수치적으로 적분(Runge-Kutta 또는 Adams 방법)하여 각 시점의 약물량 A(n)을 계산한다. TOL은 수치 적분의 허용 오차(tolerance) — 즉, 각 적분 스텝에서 허용하는 최대 상대 오차를 10^(-TOL)으로 설정한다. TOL을 지정하지 않으면 NONMEM이 기본값을 찾지 못해 실행 자체가 중단된다. TOL 값이 너무 크면(예: TOL=2) 적분 정확도가 낮아져 농도 곡선이 부드럽지 않고 계단형이 되며, 목적함수 계산에 수치 노이즈가 추가되어 수렴이 불안정해진다. 일반적으로 TOL=4~6이 권장된다.

**다음 깊이 질문:** TOL 값을 높일수록 실행 시간과 정확도가 어떻게 변하는가? 규제 제출 모델에서 TOL 선택의 근거를 어떻게 문서화해야 하는가?

</details>

---

**Q8 (적용 ★) NONMEM 파라미터 추정 결과에서 CL의 경계 경고(PARAMETER ESTIMATE IS NEAR ITS BOUNDARY) 메시지가 나타났다. 이 경고의 원인과 $COV step에 미치는 영향, 그리고 해결 전략을 구체적으로 설명하라.**

<details><summary>정답 공개</summary>

이 경고는 최종 추정값이 초기값 대비 100배 이상 차이날 때 발생한다. $COV step이 자동으로 실패(COVARIANCE STEP ABORTED)하여 SE/RSE 계산이 불가능해진다. 해결 전략: ① 초기값을 EDA(탐색적 데이터 분석) 또는 단순 NCA로 사전 추정한 값으로 교체, ② $THETA의 하한/상한 범위를 실제 데이터 범위에 맞게 조정, ③ $ESTIMATION에 NOTBT NOOBT NOSBT 옵션 추가로 경계 검사를 억제(단, 이 해결책은 파라미터 식별성 문제를 감출 수 있어 임시방편임).

**다음 깊이 질문:** SE/RSE를 계산할 수 없는 경우, NDA 규제 제출 보고서에서 파라미터 불확실성을 어떻게 정량화할 수 있는가?

</details>

---

**Q9 — 보스 딜레마 ★★**

**시나리오:** 새로운 항암제 PK 데이터를 분석 중이다. EDA에서 log-농도 vs 시간 그래프가 명확한 두 직선 기울기를 보여 2구획 모델이 적절하다. Phase 1 희소 샘플링(sparse sampling) 데이터로 1인당 2–3개 관찰값만 있다.

**두 가지 선택지:**

- **Option A**: ADVAN4 TRANS4를 사용해 2구획 경구 모델을 적합. CL, V2, Q, V3, KA 총 5개 파라미터 + 5개 IIV를 추정. 2구획 모델이 임상적으로 타당하지만, 희소 데이터에서 Q와 V3의 RSE > 100% 예상. $COV step 실패 가능성 높음.

- **Option B**: ADVAN2 TRANS2를 사용해 1구획 경구 모델을 적합. CL, V, KA 3개 파라미터 + 3개 IIV. $COV step 안정적 수렴 예상. GOF는 약간 나쁘지만 규제 제출 일정을 맞출 수 있음.

**당신은 Phase 1 IND 규제 제출을 앞두고 어느 선택을 하는가?**

<details><summary>수석 모델러의 Trade-off 논리</summary>

**수석 모델러의 판단: Option B를 선택하되, Option A의 발견을 투명하게 보고한다.**

**논리:**

Phase 1 IND 제출의 1차 목적은 안전성 확인과 용량 범위 파악이다. 이 단계에서 Q와 V3의 RSE > 100%이면, 2구획 모델을 "선택했다"는 것이 오히려 모델 식별성 부재를 인정하는 것과 같다. 규제 관점에서 "$COV step 실패 = 표준오차 없음 = 파라미터 불확실성 정량화 불가"는 용량 결정의 근거 취약으로 해석된다.

**규제 문서 방어 논리:**

"2구획 모델은 EDA에서 지지되나, Phase 1 희소 샘플링 설계(n=X관찰/대상자)에서 말초 구획 파라미터(Q, V3)의 추정 정밀도($RSE > 100\%$, $\$COV$ step 실패)가 임상적 결론 도출에 충분하지 않았다. 따라서 이 단계에서는 파라미터 추정 안정성이 확인된 1구획 모델을 기저 모델로 채택하였으며, Phase 2의 밀집 샘플링 데이터에서 2구획 모델의 타당성을 재평가할 계획이다."

**중요 단서:** Option A 분석 결과를 숨기지 않고 sensitivity analysis로 보고서에 포함시켜야 한다. 2구획 모델의 OFV 개선 정도(ΔOFV)와 시각적 GOF를 나란히 제시하면, 심사관이 모델러의 판단 과정을 추적할 수 있고 이것이 오히려 신뢰도를 높인다.

</details>

---

---

# §8 — 메타프레임 & 빅 픽처

---

### A. Positioning

**28세션 PK/PD 지식 아키텍처에서의 위치:**

이 세션(II-03)은 Vol II의 "NONMEM 제어구문 기초 3부작"의 완성판이다. II-01(θ·η·ε 3층 구조)이 파라미터의 통계적 의미를, II-02(데이터셋 변수)가 데이터의 구조를 다뤘다면, II-03은 그 두 가지를 제어구문의 구체적 코드로 연결하는 가교다.

- **이전에 온 것**: II-01(THETA/OMEGA/SIGMA의 통계적 의미), II-02(ID/TIME/AMT/DV/MDV/CMT 데이터 변수)
- **바로 다음에 오는 것**: II-04(General ADVAN + $DES ODE 작성법 — 이 세션에서 ADVAN5/6을 소개했지만 심화는 II-04에서)
- **이 기반에 결정적으로 의존하는 고급 도메인**:
  - **II-08 공변량 분석**: TVCL = THETA(1)·(COV/기준값)^THETA(n) 확장 코딩이 이 세션의 $PK TV 패턴 없이는 불가능
  - **II-09b $COVARIANCE 심화**: $COV PRINT=E, eigenvalue, condition number 해석은 이 세션의 $COVARIANCE 기초 위에서만 의미 있음
  - **II-11 PK/PD NONMEM 구현**: $PRED 기반 PD 모델, Effect Compartment 코딩은 이 세션의 $PRED 이해가 선행 필수
  - **PopPK**: VPC, Bootstrap, SAEM 추정법 모두 완전한 제어구문 코딩 능력 전제

---

### B. Dependencies

이 섹션을 대충 넘겼을 때 고급 모델링에서 발생하는 구체적 실패 모드:

**실패 1 — 척도 파라미터(S2) 오류로 인한 공변량 분석 왜곡**: S2=V2/1000을 S2=V2로 잘못 기술하면 모든 예측 농도가 1000배 과소 계산된다. 이 상태에서 공변량 분석(II-08)을 진행하면 TVCL이 실제보다 1000배 큰 값으로 추정되고, WT-CL 관계의 기울기가 완전히 왜곡된다. Phase 2/3 용량 결정이 이 값에 근거한다면 치명적 용량 과다로 이어질 수 있다.

**실패 2 — TRANS 선택 오류로 인한 파라미터 해석 불능**: ADVAN4에서 TRANS1을 선택(K, K23, K32, KA 추정)하고 보고서에 "CL = K × V2"라고 계산해서 보고하는 경우, TRANS1의 K는 $k_{10} = CL_{total}/V_2$이 아니라 $k_{10}$만을 의미하므로, CL_renal과 CL_hepatic이 혼합된 총 CL의 올바른 분리가 불가능해진다. 규제 보고서의 파라미터 해석 섹션 전체가 오염된다.

---

### C. Professional Moat

NONMEM을 실행하고 파라미터를 추출하는 것은 이미 자동화 가능하다. 이 세션의 제어구문 구조와 ADVAN/TRANS/\$PRED의 코딩 원리를 진정으로 내면화한 모델러만이 다음을 할 수 있다:

**수렴은 됐는데 예측 농도가 DV보다 1000배 작은 상황** 앞에서 — 단순히 "모델이 나쁘다"가 아니라 "S2 단위 불일치"를 30초 안에 코드 한 줄로 진단하고 수정한다.

**$COV step이 "PARAMETER NEAR BOUNDARY" 메시지와 함께 실패한 상황** 앞에서 — 이것이 파라미터 식별성 문제인지, 초기값 불량인지, 데이터 희소성 문제인지를 THETA 경계 설정과 gradient 출력을 읽으며 구별한다.

**IND 규제 제출 마감 전날 $PRED로 작성한 QTc-노출 모델에서 음수 Y가 발생했을 때** — FLAG=0/1 조건 코딩과 CALLFL=0 옵션의 차이를 알고, 어떤 상황에서 어느 것을 쓸지를 즉각 판단한다.

이것들은 알고리즘이 재현할 수 없는 판단이다. 알고리즘은 에러 메시지를 읽을 수 있지만, 에러 메시지와 코드 구조와 데이터 맥락을 동시에 연결하여 인과 추적하는 것은 이 세션의 내용을 구조적으로 내면화한 모델러에게만 가능하다.

---

```
---
✦ STEP 1 완료.

다음이 준비되었습니다:
  • §1 세션 헤더 & 로드맵
  • §2 개념 해부 카드 (4개 개념, Apex: 특수 ADVAN + TRANS 조합)
  • §5 혼동 쌍 해부 (3개 쌍, Critical Blow 적용: $SIGMA vs $THETA 잔차 추정)
  • §7 자기 테스트 (9개 질문, 보스 딜레마 포함)
  • §8 메타프레임 & 빅 픽처
  • 감지된 소스 유형: Vol II — Owen (Ch.3, pp.28–64) + PIPET 한국어 (Ch.3–4, Ch.7, pp.27–71) 혼합
  • Data Anchoring 소스: PIPET 코드 3.1 (1구획 모델 실제 제어구문), 코드 3.4–3.6 (2구획 ADVAN4/5/6 비교), 코드 3.7 (모약물-대사체 ADVAN6), 코드 3.8/$PRED (Sigmoidal Emax PD), Owen 예시 제어구문 (CL=3.9 L/h, V=52.1 L, KA=0.987 h⁻¹)

"계속"을 입력하면 Step 2 HTML 컴파일러가 실행됩니다.
Step 2는 위 내용 전체(§1·§2·§5·§7·§8) +
§3(구조적 동형성 지도) + §4(인터랙티브 시뮬레이터 + Assumption Collapse 토글) +
§6(실용 시나리오 & 진단 병리)를 단일 완성 HTML 파일로 통합합니다.
---
```

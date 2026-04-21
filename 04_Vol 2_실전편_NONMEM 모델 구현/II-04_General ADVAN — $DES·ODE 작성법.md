# §1 — 세션 헤더 & 로드맵

---

**소스 정보**

| 문헌 | 챕터/섹션 | 제목 | 페이지 |
|---|---|---|---|
| PIPET 한국어 교재 | Ch.5 | 일반 ADVAN을 이용한 제어구문의 코딩 | pp.55–63 |
| PIPET 한국어 교재 | Ch.6 | 기타 ADVAN (ADVAN9/10/11/12/13) | pp.65–67 |
| Owen & Fiedler-Kelly | Ch.9 | User-Written Models | pp.232–249 |

**감지된 소스 유형:** Vol II — Owen + PIPET 혼합
- Owen = General ADVAN 알고리즘적 배경·복잡 흡수 모델 이론·코드 예시(alpha interferon, parent-metabolite) 담당
- PIPET = 한국어 구현 패턴·`$DES` 문법 해부·`TOL` 설정·DEFDOSE/DEFOBS 디버깅 담당

---

**Big Idea (한 문장)**

특수 ADVAN의 경직된 틀에서 벗어나, `$MODEL`로 구획을 자유롭게 선언하고 `$DES`에 ODE를 직접 서술함으로써 — 선형이든 비선형이든, 흡수가 단순하든 복잡하든 — *임의의 약동학적 현실*을 NONMEM 코드로 정확하게 번역하는 능력이 이 세션의 핵심이다.

---

**개념 항법도** (§2 카드 연결)

1. **일반 ADVAN 분류 체계** — ADVAN 5/6/7/8/9/13의 선택 논리
2. **`$MODEL` 구획 선언** — COMP, DEFDOSE, DEFOBS의 의미와 CMT 데이터 우선성
3. **`$DES` ODE 작성법** ⚡ Apex Concept — `DADT(i)`, `A(i)`, `T` 변수, TOL 설정
4. **선형 vs 비선형 구현 비교** — ADVAN5(K12 마이크로상수) vs ADVAN6($DES) 동일 모델 이중 구현
5. **복잡 흡수 모델 패턴** — 병렬 흡수, 분수 흡수(Fz), MTIME/MPAST 활용
6. **Parent-Metabolite 모델** — 비선형 소실 + 대사체 동시 추정

---

**지식 그래프 위치**

```
선행 지식 (전제)                  현재 세션                    후속 지식 (열림)
─────────────────────           ─────────────────           ──────────────────────
II-02 데이터셋 (CMT, EVID) ──→  General ADVAN + $DES  ──→  II-11 PK/PD 구현
II-03 ADVAN1-4 특수 ADVAN ──→  ODE 자유 서술            ──→  (Emax·Imax NONMEM 코딩)
θ·η·ε 구조 (II-01)       ──→  $MODEL/$PK/$DES/$ERROR  ──→  TMDD (II-08 이론 → 구현)
I-07 Michaelis-Menten 이론──→  ADVAN6 비선형 ODE         ──→  II-12 지연효과 PD 구현
```

---

---

# §2 — 개념 해부 카드

---

## 카드 1: 일반 ADVAN 분류 체계 — 선택의 논리

---

### ━━ [개념 Big Idea: 거장의 시각] ━━

**왜 치명적으로 중요한가:** 잘못된 ADVAN을 선택하면 추정이 수렴하지 않거나, 수렴하더라도 내부적으로 수치적으로 불안정한 해를 반환한다 — ADVAN6로 stiff 단일클론항체를 추정하다 며칠을 날리는 것은 이 체계를 모르는 모델러의 전형적 경험이다.

**체화해야 할 단 하나의 직관:** ADVAN 선택은 "어떤 모델을 쓰느냐"가 아니라 "미분방정식 풀이기(solver)를 어느 것으로 쓰느냐"의 문제다 — 같은 2구획 경구 모델을 ADVAN5로도, ADVAN6로도 쓸 수 있다. 차이는 *수학적 해법의 종류*이지 모델 구조 자체가 아니다.

**이 직관을 머릿속에 박고 아래를 읽어라:** 모델 선택(구획 수, 비선형성)과 ADVAN 선택(수치 풀이 전략)은 독립적인 두 개의 의사결정이다.

---

**A. Formal Definition**

일반 ADVAN(General ADVAN)은 NONMEM의 PREDPP 서브루틴 중 사용자가 `$MODEL`로 구획 구조를, `$PK` 및 `$DES`로 전이 관계를 직접 명시해야 하는 ADVAN군이다. 특수 ADVAN(ADVAN1–4, 10–12)이 미리 정의된 구조만 허용하는 것과 달리, 최대 999개 구획까지 임의의 전이 구조를 표현할 수 있다.

**B. 분류 체계 코드 구조**

```
일반 ADVAN
├── 선형 (Linear) — $DES 불필요, $PK에서 K12 마이크로상수로 정의
│   ├── ADVAN5: 고유값이 복소수(complex eigenvalue) — PBPK 등 복잡 구조
│   └── ADVAN7: 고유값이 실수(real eigenvalue) — 대부분의 PK 시스템, 더 빠름
│
└── 비선형 (Nonlinear) — $DES 필수
    ├── ADVAN6: nonstiff 모델 → Runge-Kutta method (가장 범용)
    ├── ADVAN8: stiff 모델 → Gear method (속도상수 간 큰 차이, mAb 등)
    ├── ADVAN9: ADVAN6 대안, equilibrium compartment 허용
    └── ADVAN13: LSODA 기법 (stiff/nonstiff 자동 감지, BAYESIAN·MCMC 시 유리)
```

`[출처: PIPET Ch.5, 표5.1·5.2, pp.55–56; Owen Ch.9, §9.3, pp.236–238]`

**ADVAN5 vs ADVAN7 선택 기준:**

| 기준 | ADVAN5 | ADVAN7 |
|---|---|---|
| 고유값 종류 | 복소수 | 실수 |
| 대표 사용 사례 | PBPK 모델 | 일반 PK 시스템 |
| 실행 속도 | 느림 | 빠름 |

**ADVAN6 vs ADVAN8 실용적 선택법 (Owen 제안):**
`$ESTIMATION` 구문에 `MAXEVAL=1`을 설정한 후 ADVAN6와 ADVAN8를 각각 실행하여 첫 번째 반복에서 더 빠르게 성공하는 ADVAN을 선택한다.

**C. Structural Necessity**

선형 vs 비선형의 구분이 ADVAN을 분기하는 이유는 수치 해석의 필연이다. 선형 ODE는 행렬 지수(matrix exponential)의 수치적 근사로 풀 수 있으므로 `$DES` 없이 $PK의 K_mn 마이크로상수만으로 충분하다. 반면 비선형 ODE(Michaelis-Menten, TMDD 등)는 해석적 해가 존재하지 않으므로 반드시 수치 적분기(Runge-Kutta, Gear)가 필요하고, 이를 구동하기 위해 `$DES` 블록이 구조적으로 요구된다.

**D. Assumptions & Boundary Conditions**

- ADVAN5/7은 *구획 간 이동이 전적으로 1차 선형*이라는 가정이 기반. 포화 대사, TMDD, 효과 구획 등 비선형 전이가 하나라도 있으면 즉시 비선형 ADVAN으로 전환해야 한다.
- ADVAN8(Gear method)은 stiff 문제에 최적화되어 있으나, nonstiff 문제에 적용하면 불필요하게 느리다.

**E. Limitations**

일반 ADVAN은 유연하지만 코드 오류에 훨씬 취약하다: 특수 ADVAN은 NONMEM이 내부적으로 K12/K21/K10을 자동으로 처리하지만, 일반 ADVAN에서는 모든 전이 관계를 모델러가 직접 정의해야 하므로 파라미터 누락·부호 오류·단위 불일치가 모두 침묵 속에 틀린 추정값을 반환한다.

**F. Five Cognitive Layers**

| 레이어 | 내용 |
|---|---|
| **L1 형식적 수학** | 선형 ODE: $\frac{d\mathbf{A}}{dt} = \mathbf{K}\mathbf{A}$, 해: $\mathbf{A}(t) = e^{\mathbf{K}t}\mathbf{A}(0)$ (행렬 지수) |
| **L2 기하학적 직관** | stiff ODE = 시간 스케일이 매우 다른 두 기울기가 공존하는 상황 → Runge-Kutta step이 작은 스케일에 묶여 무한히 작아짐 → Gear method의 암묵적 적분이 해결 |
| **L3 구조적 동일성** | 같은 2구획 모델 = ADVAN3(특수) = ADVAN5(일반선형) = ADVAN6(일반비선형 $DES) — 수학 구조는 동일하나 풀이 방식만 다름 |
| **L4 생리학적 의미** | stiff 모델의 대표: 단일클론항체(ka ≫ Ke) — 흡수는 빠르나 반감기가 수십 일 → 두 속도상수 간 수천 배 차이 |
| **L5 실무 투영** | ADVAN6 → ADVAN8로 전환 결정 기준: 추정 시간이 비정상적으로 길거나, OFV가 반복마다 진동하며 수렴하지 않을 때 |

**G. Zettelkasten Atom**

```yaml
---
aliases: [General ADVAN, 일반 ADVAN, ADVAN5, ADVAN6, ADVAN7, ADVAN8]
tags: [pharmacometrics/nonmem, nonmem/advan, nonmem/coding]
up: "[[NONMEM Control File Architecture]]"
related: ["[[$DES ODE 작성법]]", "[[특수 ADVAN vs 일반 ADVAN]]", "[[Stiff ODE]]"]
source: "PIPET Ch.5, pp.55-56; Owen Ch.9, §9.3, pp.236-238"
---
```

일반 ADVAN은 NONMEM의 `$MODEL`+`$PK`+(`$DES`)로 구성된 사용자 정의 모델 체계다. 선형 전이만 포함하면 ADVAN5/7을, 비선형 전이가 포함되면 ADVAN6/8/9/13을 선택한다. 선택의 실질적 기준은 *모델의 stiffness*이며, ADVAN6(Runge-Kutta)로 시작하여 수치 불안정 시 ADVAN8(Gear)으로 전환하는 것이 표준 워크플로다. 같은 모델을 다수의 ADVAN으로 구현할 수 있으므로, ADVAN 선택과 모델 구조 선택을 반드시 분리하여 사고해야 한다.

---

## 카드 2: `$MODEL` 구획 선언 — COMP, DEFDOSE, DEFOBS

---

### ━━ [개념 Big Idea: 거장의 시각] ━━

**왜 치명적으로 중요한가:** `DEFDOSE`와 `DEFOBS`를 잘못 설정하면 NONMEM이 투여 기록과 관찰값을 엉뚱한 구획에 배정하며, 이 오류는 NONMEM이 경고 없이 추정을 진행하고 OFV가 수렴하는 척 보이기 때문에 — 잘못된 파라미터가 규제 제출 문서에 올라가는 사고로 이어질 수 있다.

**체화해야 할 단 하나의 직관:** `$MODEL`의 COMP 선언은 NONMEM에게 "이 구획이 무엇을 받고, 무엇을 관찰하는 기본값인지" 알려주는 주소지 등록이다 — 데이터셋에 CMT 컬럼이 있으면 이 주소지는 덮어쓰이므로, *데이터셋의 CMT가 항상 최종 결정권*을 가진다.

**이 직관을 머릿속에 박고 아래를 읽어라:** $MODEL은 CMT 컬럼이 없을 때의 보험이고, CMT 컬럼이 있으면 그것이 진짜 주소다.

---

**A. Formal Definition**

`$MODEL` 블록은 일반 ADVAN 사용 시 모델에서 사용할 구획의 수와 각 구획의 속성을 정의하는 제어구문이다. 각 구획은 `COMP(이름, [속성])` 형식으로 선언하며, 최대 999개까지 허용된다.

**B. 코드 구조 해부**

```nonmem
$MODEL
    COMP(DEPOT,    DEFDOSE)    ; 1번 구획: 투여 기본 구획 (first-order 흡수)
    COMP(CENTRAL,  DEFOBS)     ; 2번 구획: 관찰값 기본 구획 (혈중 농도 측정)
    COMP(PERIPH)               ; 3번 구획: 말초 구획 (임의 명칭)
```

`[출처: PIPET Ch.5, pp.59-60; Owen Ch.9, §9.2, p.235]`

**DEFDOSE vs DEFOBS 우선순위 규칙:**

| 상황 | NONMEM 동작 |
|---|---|
| CMT 컬럼 없음 + DEFDOSE 지정 | DEFDOSE로 지정된 구획에 투여 |
| CMT 컬럼 없음 + DEFDOSE 없음 + `DEPOT` 명칭 구획 있음 | 첫 번째 `DEPOT` 구획에 투여 |
| CMT 컬럼 없음 + 위 조건 모두 없음 | 1번 구획에 투여 |
| **CMT 컬럼 있음** | **CMT가 $MODEL 설정을 완전히 덮어씀 (최우선)** |

**C. Structural Necessity**

`$MODEL`이 일반 ADVAN에서 필수인 이유: 특수 ADVAN은 구획 구조가 코드에 하드코딩되어 있어 NONMEM이 K10, K12, K21을 자동으로 인식한다. 일반 ADVAN은 구획 수 자체를 모르므로, `$MODEL`이 없으면 `$PK`의 K12 정의가 무엇을 가리키는지 NONMEM이 해석 불가능하다.

**D. Assumptions & Boundary Conditions**

- 구획 번호는 `$MODEL` 선언 순서대로 1, 2, 3... 자동 부여된다 — 이 번호가 `$DES`의 `DADT(i)`, `A(i)` 인덱스와 1:1 대응한다.
- `DEFDOSE`와 `DEFOBS`는 한 모델에 각각 하나씩만 지정 가능하다.

**E. Limitations**

흡수 경로가 두 개 이상인 경우(병렬 1차 흡수, 동시 1차+0차 흡수), CMT 컬럼을 반드시 데이터셋에 포함시켜야 한다. DEFDOSE는 단일 투여 기본 구획만 정의하므로, 두 depot에 동시에 투여하는 시나리오는 CMT 컬럼 없이는 불가능하다.

**F. Five Cognitive Layers**

| 레이어 | 내용 |
|---|---|
| **L1 형식적 수학** | 구획 번호 i → `A(i)` = 시간 t에서 구획 i의 질량(mass), 단위: dose 단위(예: mg) |
| **L2 기하학적 직관** | $MODEL = 구획 공간의 지도, CMT 컬럼 = GPS 좌표 — GPS가 있으면 지도의 기본값은 무시됨 |
| **L3 구조적 동일성** | $MODEL의 COMP 선언 ↔ 시스템 생물학의 species 선언 ↔ 화학 반응식의 반응물 목록 |
| **L4 생리학적 의미** | DEPOT = 흡수부위(GI tract, 피하), CENTRAL = 혈장, PERIPH = 조직(근육, 지방) |
| **L5 실무 투영** | 병렬 흡수 모델에서 데이터셋에 CMT를 정확히 지정하지 않으면 두 depot 중 첫 번째에만 투여가 집중되는 침묵의 오류 발생 |

**G. Zettelkasten Atom**

```yaml
---
aliases: [$MODEL, COMP, DEFDOSE, DEFOBS, 구획 선언]
tags: [nonmem/coding, nonmem/advan/general]
up: "[[General ADVAN 분류 체계]]"
related: ["[[$DES ODE 작성법]]", "[[CMT 데이터 항목]]", "[[PREDPP 구획 시스템]]"]
source: "PIPET Ch.5, pp.59-60; Owen Ch.9, §9.2, p.235"
---
```

`$MODEL`은 일반 ADVAN의 구획 구조를 정의하는 블록으로, `COMP(이름, [DEFDOSE|DEFOBS])` 형식으로 구획을 순서대로 선언한다. 선언 순서가 구획 번호를 결정하며, 이 번호는 `$DES`의 `DADT(i)` 및 `A(i)`와 직접 연결된다. DEFDOSE/DEFOBS는 데이터셋에 CMT 컬럼이 없을 때의 기본값이며, CMT 컬럼이 존재하면 모든 $MODEL 설정을 덮어쓴다. 따라서 복수 투여 구획이 필요한 복잡 흡수 모델에서는 CMT 컬럼을 데이터셋에 반드시 명시해야 한다.

---

## 카드 3: `$DES` ODE 작성법 ⚡ [Apex Concept]

---

### ━━ [개념 Big Idea: 거장의 시각] ━━

**왜 치명적으로 중요한가:** `$DES`는 NONMEM의 심장이다 — 여기서 ODE의 부호 하나가 틀리면(유입이 유출로, 또는 반대로) 추정은 수렴하되 생물학적으로 불가능한 파라미터를 반환하며, 이 오류는 GOF 플롯만으로는 잡히지 않는다. 실제 NDA 심사에서 `$DES` 부호 오류가 발각된 사례가 존재한다.

**체화해야 할 단 하나의 직관:** `$DES`의 각 줄은 "이 구획에서 질량이 들어오는 것은 더하고(+), 나가는 것은 빼라(−)"는 *질량 보존 원칙의 직역*이다 — 시스템의 모든 구획에 대해 이 원칙만 충실히 따르면, 어떤 복잡한 ODE도 쓸 수 있다.

**이 직관을 머릿속에 박고 아래를 읽어라:** `DADT(i) = (i로 들어오는 모든 항의 합) − (i에서 나가는 모든 항의 합)`이 `$DES`의 유일한 문법이다.

---

**A. Formal Definition**

`$DES` 블록은 비선형 ADVAN(ADVAN6, 8, 9, 13) 사용 시 각 구획의 질량 변화율을 미분방정식으로 서술하는 제어구문이다. 구획 i의 변화율은 `DADT(i)`로 표현하며, 구획 i의 현재 질량은 `A(i)`로 참조한다. `$DES` 내부의 시간 변수는 연속형 `T`를 사용하며, 데이터셋의 이산형 `TIME`과 구분된다.

**B. Derivation & Code Structure — 핵심 문법 완전 해부**

**기본 문법 원칙:**

$$\text{DADT(i)} = \frac{dA_i}{dt} = \sum(\text{구획 i로의 유입}) - \sum(\text{구획 i로부터의 유출})$$

`[출처: PIPET Ch.5, p.60; Owen Ch.9, §9.3.3, p.239]`

**예시 1 — 2구획 경구 모델 (ADVAN6 구현):**

수식:
$$\frac{dA_1}{dt} = -k_a \cdot A(1)$$
$$\frac{dA_2}{dt} = k_a \cdot A(1) - (k_{23} + k_{20}) \cdot A(2) + k_{32} \cdot A(3)$$
$$\frac{dA_3}{dt} = k_{23} \cdot A(2) - k_{32} \cdot A(3)$$

NONMEM 코드:
```nonmem
$SUBROUTINE ADVAN6 TOL=4

$MODEL
    COMP(DEPOT,   DEFDOSE)   ; 1번: 흡수 구획
    COMP(CENTRAL, DEFOBS)    ; 2번: 중심 구획 (혈중)
    COMP(PERIPH)             ; 3번: 말초 구획

$PK
    CL  = THETA(1)*EXP(ETA(1))  ; 청소율 (L/hr)
    V2  = THETA(2)*EXP(ETA(2))  ; 중심 구획 부피 (L)
    V3  = THETA(3)*EXP(ETA(3))  ; 말초 구획 부피 (L)
    Q   = THETA(4)*EXP(ETA(4))  ; 구획간 청소율 (L/hr)
    KA  = THETA(5)*EXP(ETA(5))  ; 흡수 속도상수 (1/hr)
    K20 = CL/V2                  ; 소실 마이크로상수 (1/hr)
    K23 = Q/V2                   ; 중심→말초 마이크로상수 (1/hr)
    K32 = Q/V3                   ; 말초→중심 마이크로상수 (1/hr)
    S2  = V2                     ; 스케일 파라미터 (농도 변환)

$DES
    ; 1번 구획 (Depot): KA로 중심으로 유출, 유입 없음
    DADT(1) = -A(1)*KA

    ; 2번 구획 (Central): Depot에서 유입(+), 소실 및 말초로 유출(-), 말초에서 환류(+)
    DADT(2) = A(1)*KA - A(2)*(K23+K20) + A(3)*K32

    ; 3번 구획 (Peripheral): 중심에서 유입(+), 중심으로 환류(-)
    DADT(3) = A(2)*K23 - A(3)*K32

$ERROR
    IPRED = F        ; F = NONMEM이 자동 계산한 예측 농도 = A(2)/S2
    W     = SQRT(THETA(6)**2 + THETA(7)**2 * IPRED**2)
    IRES  = DV - IPRED
    IWRES = IRES/W
    Y     = IPRED + W*EPS(1)
```

`[출처: PIPET Ch.5, 그림5.5, p.61; 코드5.2, pp.62-63]`

**TOL 설정 규칙:**

$$\text{TOL} = \text{SIG (in \$ESTIMATION)} + 1 \text{ or } 2$$

TOL은 각 구획 내부값(질량, 농도, 효과) 계산에 필요한 유효 자릿수(NRD, Number of Required Digits)를 의미한다. `$ESTIMATION SIGDIGIT=3` 이라면 `TOL=4` 또는 `TOL=5`가 일반적이다.

`[출처: PIPET Ch.5, pp.59; Owen Ch.9, §9.3, p.236]`

**시간 변수 T vs TIME:**

| 변수 | 위치 | 특성 | 용도 |
|---|---|---|---|
| `TIME` | 데이터셋 | 이산형(discrete) | 관찰 시점 |
| `T` | `$DES` 내부 | 연속형(continuous) | 수치 적분 내부 시간, 시간 의존 파라미터에 사용 |

**예시 2 — Parent-Metabolite 비선형 모델 (Owen Ch.9 실제 코드):**

```nonmem
$SUBROUTINE ADVAN6 TOL=4

$MODEL
    COMP(DEPOT,    DEFDOS)   ; 1번: 흡수 구획
    COMP(CENTPRNT, DEFOBS)   ; 2번: 모약 중심 구획
    COMP(CENTMETB)           ; 3번: 대사체 중심 구획

$PK
    K20  = THETA(1)*EXP(ETA(1))  ; 모약 신장 소실 (1/hr)
    V2   = THETA(2)*EXP(ETA(2))  ; 모약 부피 (L)
    KA   = THETA(3)
    VMAX = THETA(4)              ; 최대 대사 속도 (mg/hr)
    KM   = THETA(5)              ; 반최대 기질 농도 = 질량 A(2) 단위 (mg)
    K30  = THETA(6)              ; 대사체 소실 속도상수 (1/hr)
    V3   = THETA(7)
    S2   = V2/1000               ; 단위 변환: mg/L → ng/mL
    S3   = V3/1000

$DES
    ; 1번 구획 (Depot): 1차 흡수로 유출
    DADT(1) = -KA*A(1)

    ; 2번 구획 (모약 Central): 흡수 유입 - 신장 소실 - MM 대사 소실
    DADT(2) = KA*A(1) - K20*A(2) - (VMAX*A(2))/(KM + A(2))

    ; 3번 구획 (대사체 Central): MM 대사로부터 유입(분자량 비 MPR 적용) - 소실
    DADT(3) = -K30*A(3) + ((VMAX*A(2))/(KM + A(2)))*MPR

$ERROR
    IF (CMT.EQ.2) TYPE=0   ; 모약 농도 관찰
    IF (CMT.EQ.3) TYPE=1   ; 대사체 농도 관찰
    ; 모약/대사체에 각각 다른 잔차 오차 구조 적용
    Y = F*EPS(1)*(1-TYPE) + F*EPS(2)*TYPE
```

`[출처: Owen Ch.9, §9.4.6, pp.247-249]`

**C. Structural Necessity**

`DADT(i)` 구문이 반드시 이 형태여야 하는 이유: NONMEM의 수치 적분기(Runge-Kutta, Gear)는 `dA_i/dt`를 시간 T에서 평가하여 다음 시간 스텝의 `A(i)`를 예측한다. 이 과정에서 NONMEM은 모델러가 제공한 `DADT(i)` 수식을 4차 Runge-Kutta(ADVAN6) 또는 Gear 알고리즘(ADVAN8)에 입력하여 수치 적분을 수행한다. 따라서 `$DES`는 ODE 시스템 그 자체를 서술하는 것이며, NONMEM이 해를 구하는 방식(수치 적분)과 1:1로 연결된다.

**C-2. Plausible Fallacy (그럴싸한 오류)** ← ⚡ Apex Concept

**오류의 구체적 형태:**
2구획 경구 모델의 `$DES`에서 중심 구획 번호가 2번임에도 불구하고, Owen 교재의 표준 매개변수 표기를 그대로 차용하여 중심→말초 전이를 `K12`(실제로는 구획 1→2 이동을 의미함)로 코딩하는 오류:

```nonmem
; ❌ 잘못된 코드 — K12는 NONMEM에서 구획1→구획2 이동 상수
; Depot = 구획1, Central = 구획2임에도 불구하고
; 문헌의 K12 (central→peripheral) 개념을 그대로 K12로 코딩하면
; NONMEM은 이를 Depot→Central 이동으로 해석함

$DES
    DADT(1) = -KA*A(1)
    DADT(2) = KA*A(1) - K12*A(2) - K20*A(2) + K21*A(3)  ; K12 = 구획1→2, 실제로는 Depot→Central!
    DADT(3) = K12*A(2) - K21*A(3)                        ; 이 K12가 중심→말초를 의미하길 원하지만
```

```nonmem
; ✅ 올바른 코드 — NONMEM 구획 번호에 맞게 K23(중심→말초), K32(말초→중심) 사용
$DES
    DADT(1) = -KA*A(1)
    DADT(2) = KA*A(1) - K23*A(2) - K20*A(2) + K32*A(3)  ; K23 = 구획2→구획3
    DADT(3) = K23*A(2) - K32*A(3)                        ; K32 = 구획3→구획2
```

**나비효과 (피팅·임상 예측에 미치는 영향:**

오류 코드에서 NONMEM은 `K12`를 Depot→Central 이동(사실상 두 번째 KA)으로 해석하고 `K12 ≈ KA`로 수렴을 시도한다. 그 결과 Central→Peripheral 전이가 모델에서 사라지며, 2구획 모델이 사실상 1구획 모델로 파괴된다. 피팅은 수렴하지만 `eta_CL`이 비정상적으로 커지고(`IIV` 팽창), CWRES 대 TIME 플롯에서 초기 시점 체계적 양(+) 편향, 말기 시점 음(−) 편향의 패턴이 나타난다 — 2구획 분포상(distribution phase)을 1구획이 설명하지 못하는 전형적 GOF 시그니처다.

**발견하는 GOF 시그니처 패턴 이름: "Half-Life Split Sign" (이중 부호 분리 패턴)**

CWRES vs TIME 플롯에서 초기 시점(0–2 t½)과 말기 시점(>2 t½)이 반대 부호의 체계적 편향을 보이며, 이는 분포상을 무시하고 단일 지수로 적합했을 때의 고전적 징후다.

**D. Assumptions & Boundary Conditions**

- `$DES`의 모든 변수는 각 수치 적분 스텝(연속 시간 T)에서 평가된다 — 데이터셋의 공변량(예: WT)은 `$DES` 내부에서 사용 가능하지만, 이것들은 이산 시점의 값이므로 시간 내삽이 필요한 경우 `T`를 활용한 조건문이 필요하다.
- `F` (예측값)는 `$ERROR`에서 자동으로 `A(DEFOBS 구획)/S(DEFOBS 구획)`으로 계산된다.

**E. Limitations**

`$DES`에서 시간 의존적 파라미터(time-varying covariate)를 처리할 때, 데이터셋의 `TIME`은 이산형이므로 수치 적분 내부의 연속 시간 `T`에서 중간값을 어떻게 처리할지를 모델러가 명시적으로 결정해야 한다. 이를 무시하면 계단함수(step function) 형태의 파라미터 변화를 가정하게 되어 임상적으로 부적절한 결과를 초래할 수 있다.

**F. Five Cognitive Layers**

| 레이어 | 내용 |
|---|---|
| **L1 형식적 수학** | $\frac{dA_i}{dt}\bigg|_{t=T} = f(A_1(T), A_2(T), ..., \theta, \eta)$ — ODE 시스템을 수치 적분기에 넘기는 인터페이스 |
| **L2 기하학적 직관** | `DADT(i)` = 구획 i의 순간 기울기(slope) — 모든 구획의 기울기를 동시에 계산하여 다음 시간 스텝의 농도를 예측 |
| **L3 구조적 동일성** | `DADT(i) = -KA*A(i)` ↔ $\frac{dC}{dt} = -k \cdot C$ ↔ RC회로 $\frac{dV}{dt} = -\frac{V}{RC}$ ↔ 방사성 붕괴 $\frac{dN}{dt} = -\lambda N$ |
| **L4 생리학적 의미** | DADT = 해부학적 구획에서 약물 질량의 순간 변화; 음수 = 제거/분포, 양수 = 투여/환류 |
| **L5 실무 투영** | `$DES` 검증 체크: 모든 구획의 `DADT(i)`를 합산하면 순 유출(소실)만 남아야 한다 — $\sum_i \text{DADT}(i) = -k_{el} \cdot A_{central}$ |

**G. Zettelkasten Atom**

```yaml
---
aliases: [$DES, DADT, ODE 작성법, 미분방정식 NONMEM]
tags: [nonmem/coding, nonmem/advan/general, pharmacometrics/pk]
up: "[[General ADVAN 분류 체계]]"
related: ["[[$MODEL 구획 선언]]", "[[TOL 설정]]", "[[ADVAN6 vs ADVAN8]]", "[[Parent-Metabolite Model]]"]
source: "PIPET Ch.5, pp.59-63; Owen Ch.9, §9.3.3, pp.238-240"
---
```

`$DES`는 비선형 ADVAN에서 각 구획의 순간 질량 변화율을 `DADT(i) = ...` 형식의 ODE로 서술하는 블록이다. 핵심 원칙은 질량 보존 — 유입 항은 더하고(+), 유출 항은 뺀다(−). `A(i)`는 구획 i의 현재 질량, `T`는 수치 적분 내부의 연속 시간이다. 구획 번호는 `$MODEL`의 COMP 선언 순서와 1:1 일치해야 하며, 문헌의 K12(central→peripheral) 개념이 NONMEM에서는 depot(1)→central(2)를 의미하는 K12로 혼동되는 것이 가장 흔한 치명적 부호 오류다.

---

## 카드 4: 선형 vs 비선형 구현 비교 — 동일 모델 이중 구현

---

### ━━ [개념 Big Idea: 거장의 시각] ━━

**왜 치명적으로 중요한가:** 동일한 2구획 경구 모델을 ADVAN5(선형)와 ADVAN6(비선형)으로 구현할 수 있다는 사실은, 추정 결과가 동일해야 한다는 검증 수단을 제공한다 — 두 구현이 다른 파라미터를 반환한다면 어딘가에 코딩 오류가 있다는 증거다.

**체화해야 할 단 하나의 직관:** ADVAN5는 "정답을 먼저 알고 대입하는 방식(행렬 지수)"이고, ADVAN6는 "한 걸음씩 수치 적분하는 방식"이다 — 1차 이동만 있다면 ADVAN5가 더 빠르고 안정적이다.

**이 직관을 머릿속에 박고 아래를 읽어라:** 비선형성이 없다면 ADVAN5/7을 써라 — 동일한 모델을 더 빠르고 안정적으로 추정한다.

---

**A. Formal Definition**

선형 ADVAN(ADVAN5/7)은 구획 간 이동이 모두 1차 선형인 경우, `$PK` 블록의 마이크로상수(K_mn) 정의만으로 모델을 완전히 기술할 수 있다. 비선형 ADVAN(ADVAN6 등)은 선형과 비선형 이동 모두를 `$DES`의 ODE로 서술한다.

**B. 동일 2구획 경구 모델: ADVAN5 vs ADVAN6 완전 비교**

```nonmem
; ════════════════════════════════════════════
; ADVAN5 구현 — $DES 없음, K_mn으로 정의
; ════════════════════════════════════════════
$SUBROUTINE ADVAN5

$MODEL
    COMP(DEPOT,   DEFDOSE)
    COMP(CENTRAL, DEFOBS)
    COMP(PERIPH)

$PK
    CL  = THETA(1)*EXP(ETA(1))
    V2  = THETA(2)*EXP(ETA(2))
    V3  = THETA(3)*EXP(ETA(3))
    Q   = THETA(4)*EXP(ETA(4))
    KA  = THETA(5)*EXP(ETA(5))
    S2  = V2
    K12 = KA          ; Depot(1) → Central(2): 흡수 속도상수
    K20 = CL/V2       ; Central(2) → 체외: 소실
    K23 = Q/V2        ; Central(2) → Periph(3): 분포
    K32 = Q/V3        ; Periph(3) → Central(2): 환류

$ERROR
    Y = F*(1+EPS(1))
```

```nonmem
; ════════════════════════════════════════════
; ADVAN6 구현 — $DES 필수, ODE 직접 서술
; ════════════════════════════════════════════
$SUBROUTINE ADVAN6 TOL=4    ; ← TOL 필수

$MODEL
    COMP(DEPOT,   DEFDOSE)
    COMP(CENTRAL, DEFOBS)
    COMP(PERIPH)

$PK
    CL  = THETA(1)*EXP(ETA(1))
    V2  = THETA(2)*EXP(ETA(2))
    V3  = THETA(3)*EXP(ETA(3))
    Q   = THETA(4)*EXP(ETA(4))
    KA  = THETA(5)*EXP(ETA(5))
    S2  = V2
    K20 = CL/V2
    K23 = Q/V2
    K32 = Q/V3

$DES                         ; ← ADVAN5에는 없는 블록
    DADT(1) = -A(1)*KA
    DADT(2) = A(1)*KA - A(2)*(K23+K20) + A(3)*K32
    DADT(3) = A(2)*K23 - A(3)*K32

$ERROR
    Y = F*(1+EPS(1))
```

`[출처: PIPET Ch.5, 코드5.1 & 코드5.2, pp.60-63]`

**선택 의사결정 트리:**

```
모델에 비선형 전이가 있는가?
├── YES → 비선형 ADVAN (ADVAN6/8/9/13)
│          → $DES 필수 + TOL 설정
└── NO (모두 1차 선형)
    └── 일반 선형 ADVAN (ADVAN5 또는 ADVAN7) → $DES 불필요
        → 속도 우선? ADVAN7 (고유값 실수)
        → 복잡 구조? ADVAN5 (고유값 복소수도 처리)
```

**C. Structural Necessity**

ADVAN5는 `K_mn` 마이크로상수를 이용하여 전이 속도 행렬 **K**를 구성하고, NONMEM이 내부적으로 행렬 지수 $e^{\mathbf{K}t}$를 계산하여 해석적에 가까운 해를 구한다. ADVAN6는 이 해석적 접근 대신 수치 적분(Runge-Kutta)을 사용하므로 TOL 설정이 요구된다. 두 방법이 수학적으로 동일한 모델을 표현하는 이유는 1차 선형 ODE의 해가 행렬 지수와 수치 적분 모두로 도달 가능하기 때문이다.

**D. Assumptions & Boundary Conditions**

ADVAN5/7 사용 시: 단 하나의 비선형 전이(MM 소실, 포화 흡수 등)도 존재하면 선형 ADVAN은 사용 불가능하다. 혼합 1차·비선형 모델에서 선형 ADVAN을 억지로 사용하면 NONMEM은 에러 없이 잘못된 추정을 진행하므로 특히 주의가 필요하다.

**G. Zettelkasten Atom**

```yaml
---
aliases: [ADVAN5 vs ADVAN6, 선형 vs 비선형 ADVAN, K12 마이크로상수]
tags: [nonmem/coding, nonmem/advan/general]
up: "[[General ADVAN 분류 체계]]"
related: ["[[$DES ODE 작성법]]", "[[1차 이동 선형 모델]]"]
source: "PIPET Ch.5, 코드5.1 & 5.2, pp.60-63"
---
```

동일한 2구획 경구 모델을 ADVAN5(K_mn 마이크로상수)와 ADVAN6($DES ODE)로 이중 구현할 수 있다. 모든 전이가 1차 선형이면 ADVAN5가 빠르고 안정적이다. 비선형 전이가 하나라도 있으면 ADVAN6 이상의 비선형 ADVAN이 필수다. 두 구현의 결과가 다르면 코딩 오류의 증거다.

---

## 카드 5: 복잡 흡수 모델 패턴 — 병렬 흡수와 분수 파라미터

---

### ━━ [개념 Big Idea: 거장의 시각] ━━

**왜 치명적으로 중요한가:** 약물의 실제 흡수는 단순 1차가 아닌 경우가 압도적으로 많다 — 경구 서방형, 피하 흡수, 폐 흡수 등에서 병렬·순차 흡수가 나타나며, 이를 단순 ADVAN2로 적합하면 Tmax와 흡수 AUC를 체계적으로 오추정한다.

**체화해야 할 단 하나의 직관:** 두 depot에 전체 용량을 각각 넣되 $F_1 + F_2 = 1$로 제약하면 — 분수(fraction)가 파라미터가 된다. 이것이 "추정된 분수 흡수(estimated fraction)" 패턴의 핵심이다.

**이 직관을 머릿속에 박고 아래를 읽어라:** 두 depot에 동량을 넣고 생체이용률 파라미터로 분배 비율을 추정하는 것이 병렬 흡수 모델의 표준 데이터셋 설계다.

---

**A. Formal Definition**

병렬 흡수 모델(parallel absorption model)은 하나의 투여 용량이 두 개 이상의 흡수 경로를 통해 동시에 중심 구획으로 유입되는 모델이다. 각 경로의 흡수 분율(fraction)을 추정 파라미터로 설정하여 모델링한다.

**B. 핵심 구현 패턴 — Alpha interferon 기반 (Owen Ch.9)**

**데이터셋 구조 (병렬 1차+0차 흡수, 분율 미지인 경우):**

| ID | TIME | DV | AMT | EVID | RATE | MDV | CMT |
|----|------|----|-----|------|------|-----|-----|
| 1 | 0 | . | 300 | 1 | 0 | 1 | 1 |
| 1 | 0 | . | 300 | 1 | −2 | 1 | 2 |

두 dosing record 모두 전체 용량(300mg)을 입력하되, CMT=1에는 1차 흡수(RATE=0), CMT=2에는 0차 흡수(RATE=−2, D2로 기간 추정)를 배정한다.

```nonmem
$PROBLEM Parallel first-order and zero-order absorption
         ; Chatelut et al. (1999) alpha interferon model
$INPUT ID TIME AMT DOSE DV EVID RATE MDV CMT
$DATA study01.csv
$SUBROUTINE ADVAN2

$PK
    F1    = THETA(1)       ; Depot 분율 (1차 흡수 비율, 0<F1<1)
    F2    = 1 - F1         ; Central 분율 (0차 흡수 비율)
    ALAG2 = THETA(2)       ; 0차 흡수 지연 시간 (hr)
    D2    = THETA(3)       ; 0차 흡수 지속 시간 (hr)
    KA    = THETA(4)       ; 1차 흡수 속도상수 (1/hr)
    TVV2  = THETA(5)
    V2    = TVV2*EXP(ETA(1)) ; 중심 구획 부피 (L)
    TVK   = THETA(6)
    K     = TVK*EXP(ETA(2))  ; 1차 소실 속도상수 (1/hr)
    S2    = V2/1000        ; 단위 변환: mg/L → ng/mL
```

`[출처: Owen Ch.9, §9.4.3, pp.243-244]`

**MTIME/MPAST를 이용한 순차적 1차 흡수 (흡수 속도 변화 모델):**

```nonmem
$PK
    KAFAST     = THETA(1)          ; 상부 GI 흡수 속도 (빠름)
    KASLOW     = THETA(2)          ; 하부 GI 흡수 속도 (느림)
    MTIME(1)   = THETA(3)          ; 흡수 속도 전환 시점 (hr)
    ; MPAST(1): TIME≤MTIME(1)이면 0, TIME>MTIME(1)이면 1
    KA = KAFAST*(1-MPAST(1)) + KASLOW*MPAST(1)
```

`[출처: Owen Ch.9, §9.4.2, pp.242-243]`

**C. Structural Necessity**

$F_1 + F_2 = 1$ 제약이 필수인 이유: 제약 없이 두 depot에 전체 용량을 각각 입력하면 시스템에 실제 투여량의 2배가 주입된다. $F_1 \leq 1$과 $F_2 = 1 - F_1$의 보완 관계가 질량 보존을 보장하는 유일한 수학적 메커니즘이다.

**G. Zettelkasten Atom**

```yaml
---
aliases: [병렬 흡수 모델, 분수 흡수, MTIME, MPAST, F1, F2]
tags: [nonmem/coding, pharmacometrics/pk/absorption]
up: "[[$DES ODE 작성법]]"
related: "[[ALAG 지연 흡수 파라미터]]", "[[복잡 흡수 모델 패턴]]"]
source: "Owen Ch.9, §9.4.2-9.4.4, pp.242-246"
---
```

병렬 흡수 모델은 두 dosing record에 동일 전체 용량을 입력하고, $F_1 = \theta_1$, $F_2 = 1 - F_1$의 보완 관계로 질량 보존을 보장한다. 이 분율이 분배하는 것은 절대 생체이용률이 아니라 흡수된 약물 중 각 경로를 통하는 분율임에 주의해야 한다. MTIME/MPAST는 흡수 속도의 시간 의존적 전환(상부→하부 GI 이동)을 단일 depot으로 표현할 때 사용한다.

---

---

# §5 — 혼동쌍 해부

---

## 혼동쌍 1: ADVAN5 `K12` vs 문헌 표준 `K12` (구획 번호 인덱싱 충돌)

| 비교 차원 | NONMEM K12 | 문헌 표준 K12 |
|---|---|---|
| **표면적 유사성** | 동일한 기호 `K12`를 사용함 | 동일한 기호 `K12`를 사용함 |
| **수식/코드 형태** | `K12 = KA` (ADVAN5, Depot→Central이 구획1→2이므로) | $k_{12}$: Central→Peripheral 전이 |
| **지시 대상** | NONMEM 구획 번호 1 → 구획 번호 2 이동 | 문헌의 중심→말초 이동 (흡수 구획 없는 2구획 체계) |
| **변화 방향** | 흡수 경로가 있으면 K12=KA | 2구획 소실 파라미터 (CL_q/V1에 해당) |
| **임상/모델링 결과** | K12를 문헌 개념으로 썼다가 NONMEM이 KA=K12로 해석하면 분포상(α phase) 파라미터가 사라지고 1구획으로 파괴됨 | |
| **⚡ 기억 고리** | NONMEM의 K_mn은 "구획 **m**에서 구획 **n**으로" — Depot이 구획1이면 Depot→Central이 K12이고, 문헌의 Central→Peripheral은 K23이 된다. *구획 번호가 바뀌면 K 인덱스도 바뀐다.* |

### ⚠️ Critical Blow 행

| **치명적 타격** | 2구획 모델을 ADVAN6로 구현할 때 문헌의 K12를 중심→말초 전이로 `$DES`에 코딩하면, NONMEM은 이를 Depot→Central(즉 두 번째 KA)로 처리하여 말초 구획이 사실상 제거된다 — NDA/IND 제출 후 심사관의 GOF 패턴 검토에서 CWRES 이중 부호 분리가 발각되면 Major Deficiency로 처리된다. |

---

## 혼동쌍 2: `$DES`의 `T` vs 데이터셋의 `TIME`

| 비교 차원 | `T` (in $DES) | `TIME` (in Dataset) |
|---|---|---|
| **표면적 유사성** | 둘 다 "시간"을 나타내는 변수명 | |
| **수식/코드 형태** | 연속형 변수, 수치 적분기가 내부적으로 사용 | 이산형 변수, 관찰 레코드의 실제 샘플링 시점 |
| **지시 대상** | Runge-Kutta step 내부의 연속 시간 | 데이터셋 각 행의 시간 열(hr, min 등) |
| **변화 방향** | 적분기 step size에 따라 세밀하게 변함 | 관찰 간격에 따라 점프함 |
| **임상/모델링 결과** | `$DES`에서 `TIME`을 사용하면 수치 적분 중간 step에서 TIME이 고정되어 시간 의존 파라미터가 계단함수로 처리됨 — 비선형 시간 의존 PK에서 추정 편향 발생 | |
| **⚡ 기억 고리** | `T`는 적분기의 내부 시계(analog), `TIME`은 데이터의 스냅샷(digital) — `$DES` 내에서 시간 의존 파라미터를 다룰 때는 반드시 아날로그 시계 `T`를 써라. |

---

## 혼동쌍 3: `DEFDOSE`/`DEFOBS` vs CMT 컬럼 우선순위

| 비교 차원 | `$MODEL`의 DEFDOSE/DEFOBS | 데이터셋의 CMT 컬럼 |
|---|---|---|
| **표면적 유사성** | 둘 다 투여 구획·관찰 구획을 지정함 | |
| **지시 대상** | $MODEL 선언 시의 기본값(fallback) | 각 레코드별 개별 구획 지정 |
| **우선순위** | 낮음 — CMT가 있으면 무시됨 | 높음 — 항상 DEFDOSE/DEFOBS를 덮어씀 |
| **임상/모델링 결과** | CMT 컬럼 없이 병렬 흡수 모델을 구현하려 하면, 두 번째 depot에 투여가 안 되고 모든 용량이 첫 번째 depot으로 집중 → 흡수 분율 추정 불가 | |
| **⚡ 기억 고리** | DEFDOSE/DEFOBS는 "우편번호 기본값" — 데이터셋 CMT는 "직접 주소". 복잡 흡수 모델에서 반드시 직접 주소(CMT)를 써야 두 번째 depot에 편지가 간다. |

---

---

# §7 — Self-Test: Active Recall Module

---

**Q1 [★★ 회상]**
`$SUBROUTINE ADVAN6 TOL=4`에서 `TOL=4`가 의미하는 것은 무엇인가? `$ESTIMATION`의 `SIGDIGIT=3`와 어떤 관계인가?

<details>
<summary>정답 공개</summary>

TOL은 각 구획 내부값(질량, 농도, 효과) 계산에 필요한 유효 자릿수(NRD)를 의미한다. `TOL=4`는 적분 계산에서 4자리 유효숫자를 유지하라는 의미다. 일반 규칙: `TOL = SIGDIGIT + 1 or 2`. SIGDIGIT=3이면 TOL=4 또는 TOL=5로 설정한다. TOL이 너무 낮으면 수치 부정확, 너무 높으면 실행 시간이 과도하게 증가한다.

**다음 깊이 질문:** TOL을 SIGDIGIT보다 낮게 설정하면 NONMEM은 어떤 행동을 보이는가?
</details>

---

**Q2 [○ 회상]**
`$DES` 블록에서 2구획 경구 모델의 중심 구획(구획 2) ODE를 작성하라. KA(흡수), K23(중심→말초), K32(말초→중심), K20(소실)을 사용하라.

<details>
<summary>정답 공개</summary>

```nonmem
DADT(2) = A(1)*KA - A(2)*(K23 + K20) + A(3)*K32
```

- `A(1)*KA`: Depot(구획1)에서 유입 (+)
- `-A(2)*(K23 + K20)`: 말초로 분포 + 체외 소실 (−)
- `+A(3)*K32`: 말초에서 환류 (+)

**다음 깊이 질문:** 모든 구획의 DADT(i)를 합산하면 어떤 항만 남아야 하는가? 그 이유는?
</details>

---

**Q3 [★★ 적용]**
동일한 2구획 경구 모델을 ADVAN5와 ADVAN6로 각각 구현했더니 추정된 CL이 2.1 L/hr vs 2.4 L/hr로 달랐다. 가장 먼저 의심해야 하는 원인은 무엇인가?

<details>
<summary>정답 공개</summary>

ADVAN6의 `$DES`에서 ODE 부호 오류 또는 K 인덱스 혼동을 가장 먼저 의심해야 한다. 두 구현이 동일한 모델을 표현한다면 파라미터가 동일해야 한다. 다른 경우 ADVAN6 `$DES`의 DADT 수식에서 (1) 잘못된 구획 인덱스 (K12를 K23 대신 사용), (2) 부호 오류 (−를 +로), (3) 마이크로상수 정의 불일치(K23≠Q/V2)를 순서대로 점검한다. ADVAN5의 K_mn 표기와 ADVAN6 $DES의 ODE 표기가 동일한 수학 구조를 반영하는지 확인한다.

**다음 깊이 질문:** ADVAN5 추정 결과를 "기준값"으로 삼아 ADVAN6를 검증하는 것이 왜 합리적인가?
</details>

---

**Q4 [★ 적용]**
병렬 1차+0차 흡수 모델에서 두 dosing record에 각각 전체 용량(예: 300mg)을 입력하는 이유는 무엇인가? $F_1 + F_2 = 1$ 제약이 없으면 어떤 오류가 발생하는가?

<details>
<summary>정답 공개</summary>

두 경로의 흡수 분율($F_1$, $F_2$)을 파라미터로 추정하기 때문에 전체 용량을 각 depot에 넣고 생체이용률 파라미터($F_1$, $1-F_1$)로 실제 흡수량을 조절한다. $F_1 + F_2 = 1$ 제약 없이 양 depot에 300mg씩 넣으면 NONMEM은 600mg이 투여된 것으로 처리하여 실제 투여량의 2배를 흡수 모델에 투입한다 → CL과 V가 2배 과소추정된다.

**다음 깊이 질문:** 이 설계에서 추정되는 $F_1$은 절대 생체이용률인가, 아니면 다른 무엇인가?
</details>

---

**Q5 [★★ 적용]**
ADVAN6로 stiff 단일클론항체(mAb) 모델을 추정 중 실행 시간이 72시간이 넘어도 수렴하지 않는다. 어떤 단계를 취하는가?

<details>
<summary>정답 공개</summary>

1. **ADVAN8로 전환 테스트**: `$ESTIMATION MAXEVAL=1`로 ADVAN6와 ADVAN8을 각각 1회 반복 실행하여 더 빠르게 성공하는 ADVAN을 선택한다.
2. **ADVAN13 시도**: stiff/nonstiff 자동 감지 LSODA 기법 — BAYESIAN 추정 방식과 조합 시 특히 유리하다.
3. **TOL 조정**: TOL을 3으로 낮춰 속도를 높이되 정밀도 희생을 감수한다 (최종 모델에서는 원래 TOL로 복구).
4. **ODE 구조 단순화**: 모델 복잡도를 줄이거나 일부 파라미터를 고정(fix)하여 stiffness를 완화한다.

**다음 깊이 질문:** ADVAN8(Gear method)은 왜 stiff ODE에서 Runge-Kutta보다 안정적인가?
</details>

---

**Q6 [★ 적용]**
Parent-Metabolite 모델의 `$ERROR` 블록에서 `TYPE=0`과 `TYPE=1`을 이용해 모약과 대사체에 서로 다른 잔차 오차 구조를 적용하는 코드를 설명하라.

<details>
<summary>정답 공개</summary>

```nonmem
$ERROR
    IF (CMT.EQ.2) TYPE=0   ; 모약 관찰 (CMT=2)
    IF (CMT.EQ.3) TYPE=1   ; 대사체 관찰 (CMT=3)
    Y = F*EPS(1)*(1-TYPE) + F*EPS(2)*TYPE
```

- CMT=2(모약): TYPE=0 → Y = F*EPS(1)*1 + F*EPS(2)*0 = F*EPS(1)
- CMT=3(대사체): TYPE=1 → Y = F*EPS(1)*0 + F*EPS(2)*1 = F*EPS(2)
- EPS(1)과 EPS(2)는 `$SIGMA`에서 각각 다른 분산을 가지므로 모약과 대사체의 잔차 오차 크기를 독립적으로 추정할 수 있다.

**다음 깊이 질문:** CMT를 조건으로 TYPE을 정의하는 대신 FLAG 변수를 데이터셋에 추가하는 방법과 비교할 때 장단점은?
</details>

---

**Q7 [○ 회상]**
ADVAN5와 ADVAN7의 차이를 고유값(eigenvalue) 관점에서 설명하고, 각각의 대표적인 사용 사례를 하나씩 제시하라.

<details>
<summary>정답 공개</summary>

ADVAN5: 속도상수 행렬의 고유값이 복소수(complex)인 경우 사용. 복잡한 구조의 PBPK 모델처럼 구획 간 이동이 복잡하게 얽혀 있을 때 고유값이 복소수가 될 수 있다. 실행 시간이 느리다.

ADVAN7: 고유값이 실수(real)임이 알려진 경우 사용. 대부분의 일반 PK 시스템(1-3구획 선형 모델)에서 해당. ADVAN5보다 빠르게 실행된다.

실무 선택: 확신이 없으면 ADVAN5를 먼저 시도하고, 수렴 후 ADVAN7로 전환하여 속도 개선을 확인한다.

**다음 깊이 질문:** 고유값이 복소수가 된다는 것은 시스템 거동에 어떤 의미를 갖는가?
</details>

---

**Q8 [★★ 보스 딜레마] ← 마지막 질문**

---

당신은 Phase 2 항암제 PopPK 모델링을 진행 중이다. 약물은 2구획 경구 모델이며, 흡수 패턴이 단순 1차가 아닌 것으로 의심된다 — Tmax 예측이 관찰 데이터보다 일관되게 늦다. 두 가지 선택지가 있다:

**선택 A:** 병렬 1차+0차 흡수 모델 (ADVAN6, $DES 필요, F₁ 추정 포함) — 데이터 적합도가 개선되지만 데이터셋에 두 dosing record가 필요하고 추정 파라미터가 2개 늘어난다. Phase 2 소규모 데이터(n=28)에서 수렴이 불안정할 가능성이 있다.

**선택 B:** 흡수 lag time을 추가한 단순 1차 흡수 모델 (ADVAN2 유지) — 간단하고 수렴이 안정적이지만 Tmax 설명의 기계론적 타당성이 떨어지며, NDA에서 흡수 모델 misspecification 지적을 받을 위험이 있다.

**Phase 2 용량 결정 회의에서 당신은 어느 쪽을 택하는가?**

<details>
<summary>수석 모델러의 Trade-off 논리 공개</summary>

**권장 선택: 선택 A를 단계적으로 시도하되, B를 기저모델로 출발점 삼기.**

**수석 모델러의 논리:**

Phase 2 데이터는 n=28로 소규모이므로 수렴 실패 위험이 실질적이다. 그러나 Phase 2 PopPK의 핵심 목적이 Phase 3 용량 예측이라면, 흡수 misspecification은 Cmax와 Tmax 예측 오차로 이어지고 — 항암제에서 Cmax 과소추정은 독성 예측 실패를 의미한다.

**실행 전략:**

1. ALAG1을 추가한 ADVAN2(선택 B+)로 기저 모델 확정 → OFV 확인
2. ADVAN6 병렬 흡수 모델(선택 A)을 시도 → F₁ 초기값 0.3–0.5, D2 초기값 4–8hr로 설정
3. $COV step 성공 여부와 F₁의 RSE < 30% 기준으로 선택 A 채택 결정
4. 수렴 실패 시: F₁을 고정(F₁=0.5)하고 D2만 추정하는 단순화 버전으로 후퇴

**규제 문서 방어 언어 (선택 A 채택 시):**

"A parallel first-order and zero-order absorption model was selected based on a statistically significant improvement in OFV (ΔOFV = −X, p < 0.05) and visual improvement in conditional weighted residuals versus time profiles. The fraction absorbed via first-order process (F₁ = 0.XX, RSE = XX%) was estimated with acceptable precision. Model selection was further supported by visual predictive check demonstrating appropriate coverage of observed Tmax distribution."

**규제 문서 방어 언어 (선택 B 유지 시):**

"Although a parallel absorption model was explored, the limited sample size (n=28) precluded reliable estimation of the additional absorption parameters (RSE > 50%, $COV step failure). A first-order absorption model with lag time was retained as the base model, with the acknowledgment that Cmax predictions carry uncertainty that will be reassessed in the Phase 3 dataset."

두 선택 모두 규제적으로 방어 가능하나 — Phase 2의 진짜 목적(Phase 3 설계 지원)을 고려하면 선택 A 시도가 과학적으로 더 정직하다.

</details>

---

---

# §8 — Meta-Frame & Big Picture

---

### A. Positioning — 28세션 아키텍처에서의 위치

```
II-03 (특수 ADVAN 코딩)
   │ → 특수 ADVAN의 한계 인식
   ↓
II-04 (General ADVAN + $DES) ← 현재 세션
   │ → 임의 ODE 표현 능력 확보
   ↓
II-11 (PK/PD NONMEM 구현: Emax·Imax)
   │ → $DES로 PD ODE 서술
   ↓
II-12 (지연효과 PD: Turnover·Effect compartment)
```

**이 기반에 결정적으로 의존하는 고급 도메인:**

- **TMDD (Target-Mediated Drug Disposition):** 수용체 결합·내재화·재생성 ODE 전체가 `$DES` 기반 — `$DES` 없이는 TMDD 구현 불가능
- **PBPK:** 장기별 혈류·분배계수·대사 효소를 구획으로 표현 → ADVAN5 기반 다수 구획 선형 시스템
- **QSP (Quantitative Systems Pharmacology):** 면역·신호전달 경로의 수십 개 ODE → `$DES` 확장이 유일한 구현 경로
- **Parent-Metabolite 비선형 동시 추정:** ADVAN6 + 복수 `$ERROR` TYPE 분기 패턴의 직접 응용

---

### B. Dependencies — 대충 넘겼을 때 발생하는 실패 모드

**실패 모드 1: K 인덱스 혼동 → 침묵의 모델 붕괴**

`$DES`에서 구획 번호와 K 인덱스의 관계를 체득하지 못한 모델러는 문헌의 K12(central→peripheral)를 NONMEM K12(구획1→구획2 = depot→central)로 혼용한다. NONMEM은 경고 없이 수렴하고, 말초 구획 없이 1구획으로 작동하는 파라미터를 반환한다. 이 오류는 GOF 플롯의 CWRES 이중 부호 분리 패턴으로만 사후 발견된다 — 규제 제출 후 발각되면 전체 모델 재개발이 요구된다.

**실패 모드 2: 복잡 흡수 모델의 데이터셋 설계 오류 → 용량 2배 투입**

병렬 흡수 모델에서 두 dosing record에 전체 용량을 넣는 이유와 F₁+F₂=1 제약의 필연성을 이해하지 못하면, F₁ 제약 없이 두 depot에 각각 전체 용량을 넣어 모든 파라미터가 2배로 오추정되는 사고가 발생한다. CL과 V가 실제값의 50%로 추정되어 용량 과소처방이 발생한다.

---

### C. Professional Moat

NONMEM을 실행하고 파라미터를 추출하는 것은 이미 자동화 가능하다. `$DES` 코드 구조와 ODE 수치 적분의 수학을 진정으로 내면화한 모델러만이 다음을 할 수 있다:

**수렴 실패 앞에서**: NONMEM의 에러 메시지("MINIMIZATION TERMINATED")를 보고 TOL 문제인지, ODE 부호 오류인지, 파라미터 식별성 문제인지를 에러 메시지 한 줄에서 구분하는 진단 논리를 즉시 실행할 수 있다.

**CWRES 편향 앞에서**: 흡수 구획의 Tmax 체계적 과소추정 패턴을 보고 "단순 1차 흡수의 구조적 misspecification"으로 진단하고, 병렬 흡수 모델로의 전환 필요성을 데이터 없이 판단할 수 있다 — 이것은 `$DES` 구조와 흡수 ODE의 형태가 실제 약물 동태에 어떻게 대응하는지를 체득한 사람만의 능력이다.

**신규 생물학적 현상 앞에서**: 기존 특수 ADVAN이 없는 새로운 기전(예: 수용체 매개 내재화 + 리간드 재순환 + 표적 재생성)을 처음 마주쳤을 때, 생물학적 프로세스를 ODE로 번역하고 `$DES` 블록으로 즉시 구현할 수 있다. 이 능력은 특수 ADVAN 사용법 암기로는 절대 도달할 수 없으며, ODE와 `$DES` 구문이 1:1로 대응한다는 구조적 이해에서만 나온다.

---

```
✦ STEP 1 완료.

다음이 준비되었습니다:
  • §1 세션 헤더 & 로드맵
  • §2 개념 해부 카드 (5개 개념, Apex: $DES ODE 작성법)
  • §5 혼동쌍 해부 (3개 쌍, Critical Blow 적용: K12 인덱스 충돌)
  • §7 자기 테스트 (8개 질문, 보스 딜레마 포함)
  • §8 메타프레임 & 빅 픽처
  • 감지된 소스 유형: Vol II — Owen Ch.9 (pp.232-249) + PIPET Ch.5-6 (pp.55-67) 혼합
  • Data Anchoring 소스: Chatelut et al. (1999) alpha interferon 피하주사 병렬흡수 모델 (Owen); PIPET 실제 NONMEM 코드 패턴 및 2구획 경구 모델 실습 예시 (sildenafil, PIPET p.61)

"계속"을 입력하면 Step 2 HTML 컴파일러가 실행됩니다.
Step 2는 위 내용 전체(§1·§2·§5·§7·§8) +
§3(구조적 동형성 지도) + §4(인터랙티브 시뮬레이터 + Assumption Collapse 토글) +
§6(실용 시나리오 & 진단 병리)를 단일 완성 HTML 파일로 통합합니다.
---
```

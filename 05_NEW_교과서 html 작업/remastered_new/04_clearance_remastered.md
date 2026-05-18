# 세션 04 — 청소율(Clearance) 완전정복: 4-좌표 주소 읽기 — Remastered Edition

> **이 문서는 무엇인가**
> 원본 v4.0 final의 콘텐츠를 그대로 보존하되, **학습 동선을 4-좌표 순서로 재구성**한 강의용 본문임. 임상에서 보고서 한 장 받았을 때 "지금 내 손이 자동으로 어디로 가야 하는가?"를 결정하는 본능을 만드는 게 이 챕터의 목표임. 수식 annotation(overbrace/underbrace)·출처(G&W, R&T 페이지 번호)는 원본 그대로 유지함.

---

## 프롤로그 — 60 L/h가 알려주는 진짜 이야기

자, 환자 차트 한 줄로 시작함.

> "Plasma $CL = 60\ \mathrm{L/h}$, 간 혈류 $Q_H = 81\ \mathrm{L/h}$"

옆자리 펠로우가 슬쩍 보더니 그럼. "어, 중등도 이상 hepatic extraction이네요? $60/81 \approx 0.74$니까." 그럴듯함. 책 한 권만 본 사람이면 이렇게 답하는 게 자연스러움.

근데 같은 환자에서 한 줄이 더 있음 — $C/C_b = 0.5$. 약물이 RBC에 절반쯤 가 있다는 뜻임. 이걸 알고 다시 계산하면:

$$
CL_b = 60 \times 0.5 = 30\ \mathrm{L/h}, \qquad E_H = \frac{30}{81} \approx 0.37
$$

**중등도 이상이 아니라 low-to-intermediate임.** 분류가 통째로 바뀜.

이게 왜 큰일이냐면 — 이 한 줄짜리 판단이 DDI 라벨 문구를 바꾸고, 간장애 환자 dose adjustment 결정을 바꾸고, PBPK input의 $f_{ub} \cdot CL_{int}$ 단위를 바꿈. **임상 약리 보고서 전체가 이 하나의 매트릭스 mismatch에서 갈라짐.**

이 챕터에서 우리가 진짜 익히는 건 청소율이라는 숫자가 아님. **"지금 다루는 게 정확히 어떤 청소율인가?"라는 4-좌표 질문을 본능적으로 던지는 습관**임. 그리고 그 4-좌표를 **어느 순서로 점검해야 안전한가**를 몸에 새기는 거임.

---

## §0 운영체계 — 4-좌표를 어느 순서로 읽을 것인가

원본에서 이 네 좌표를 이렇게 나열함:

| # | 좌표 | 묻는 내용 |
|---|---|---|
| 1 | 농도 기준 | 혈장? 전혈? 비결합? |
| 2 | 장기 | 신장? 간? |
| 3 | 투여 경로 | IV? Oral? |
| 4 | 분석 대상 | 모약물? 대사체? |

근데 이 순서가 **임의가 아님**. 1번을 안 풀고 2번으로 가면 hepatic extraction 분류가 통째로 틀어짐(프롤로그 사례). 2번을 안 풀고 3번으로 가면 first-pass가 어느 장기에서 일어나는지 모름. 3번을 안 풀고 4번으로 가면 first-pass 형성과 systemic 형성을 구분 못 함.

**그래서 점검 순서는 1 → 2 → 3 → 4임. 절대 거꾸로 가면 안 됨.**

이 챕터의 구조도 그 순서를 따라감:

```
프롤로그 (60 L/h 미스터리)
   ↓
§1 청소율의 정의 — CL은 비례상수, t½는 결과 (M1)
   ↓
§2 좌표 #1: 매트릭스 — plasma vs blood vs unbound (M8)
   → 여기서 프롤로그 미스터리 풀림
   ↓
§3 좌표 #2A: 신장 분해 — CL_R = f_e·CL (M2, M2.5, M3)
   ↓
§4 좌표 #2B: 간 분해 — Well-stirred + 확장 (M4, M6, M9, M10, M10.5)
   ↓
§5 좌표 #3: 투여 경로 — Route × Extraction × Endpoint (M5)
   ↓
§6 좌표 #4: 대사체 — 율속단계 → 노출비 → 신부전 (M11, M12, M13, M14)
   ↓
§7 구현 다리 — PK5 동시 적합 (M7)
§8 종간 정규화 — Allometric scaling
§9 혼동 쌍 10개 / §10 자기검증 / §11 한 페이지 요약
```

시간이 없을 때 다섯 카드만 골라 읽으라면 — **M1 → M8 → M2 → M4 → M14**임. 4-좌표 전체를 이 다섯 개로 압축할 수 있음.

---

## §1 가장 먼저 — $CL$은 비례상수, $t_{1/2}$는 결과

<!-- SLIDE_START: §1 | title: §1 CL은 비례상수, t½는 결과 -->

### 1.1 왜 반감기로 시작하면 안 되는가

환자 차트에 "반감기가 늘었어요"라고 적혀 있으면 본능적으로 "아, 신부전인가?" 하고 머리가 감. **이거 막아야 함.** 

$t_{1/2}$는 결과값임. 원인이 아님. 식으로 보면 [R&T pp.148–150 Eq 5-24–5-27]:

$$
\underbrace{t_{1/2}}_{\text{반감기}}=\frac{\underbrace{0.693}_{\ln 2}\cdot\underbrace{V}_{\text{분포용적}}}{\underbrace{CL}_{\text{제거능}}}
$$

분자에 $V$, 분모에 $CL$이 있음. 반감기가 늘었다는 말은 **$V$가 늘었거나, $CL$이 줄었거나, 둘 다거나** — 셋 중 어느 건지 아직 모른다는 뜻임.

예를 들어 어떤 환자가 hepatomegaly로 $V$가 커진 경우랑, 신부전으로 $CL$이 떨어진 경우랑, 두 경우 모두 같은 $t_{1/2}$ 증가를 보일 수 있음. 그런데 임상 조치는 완전히 다름 — 전자는 유지용량 안 건드리고 loading만 늘려야 하고, 후자는 유지용량을 줄여야 함. **$t_{1/2}$만 보고 가면 둘을 못 구별함.**

> **본능 한 줄**: $t_{1/2}$ 변화 보고서 받으면 첫 손은 항상 $CL$과 $V$를 분리하는 자리로 감.

### 1.2 청소율의 진짜 정의

$CL$은 "제거 속도" 자체가 아님. **농도로 정규화한 제거능**임 [G&W p.49 Eq 2:83–2:86]:

$$
\underbrace{\frac{dX}{dt}}_{\text{체내 변화속도}}=-\underbrace{CL}_{\text{제거능}}\cdot \underbrace{C}_{\text{농도 신호}}
$$

이 식이 왜 유용하냐면 — first-order 조건에서 **$CL$은 시간마다 새로 바뀌는 게 아니라, 관찰 구간 전체를 설명하는 하나의 비례상수**임. 즉 IV bolus를 주든 IV infusion을 주든, 어느 시점에 측정하든, **$CL$은 같은 숫자가 나와야** 함. 안 그러면 비선형이거나 모델이 틀렸거나 둘 중 하나임.

여기서 magical한 결과 하나가 나옴 [G&W pp.77–79; R&T pp.124–128]:

$$
\underbrace{CL}_{\text{IV CL}}=\frac{\underbrace{Dose_{iv}}_{\text{IV 투여량}}}{\underbrace{AUC_{0-\infty}}_{\text{IV 전신노출}}}, \qquad \underbrace{\frac{CL}{F}}_{\text{경구 CL/F}}=\frac{\underbrace{D_{po}}_{\text{경구 투여량}}}{\underbrace{AUC_{po}}_{\text{경구 노출}}}
$$

**Compartment model 없이도 성립함.** 왜냐하면 총 제거량 = dose이고, $\int Rate\,dt = CL \cdot \int C\,dt = CL \cdot AUC$이니까. 그래서 NCA가 의미를 갖는 거임 — 모델을 안 가정해도 $CL$을 뽑을 수 있음.

### 1.3 파라미터 해부

| 파라미터 | 단위 | 의미 | 변화 원인 |
|---|---:|---|---|
| $CL$ | L/h | 농도 대비 제거능 | 신장·간 기능, 단백결합, 효소 |
| $V$ | L | 농도를 양으로 환산하는 분포용적 | 조직분포, 단백결합, 체액량 |
| $t_{1/2}$ | h | $V/CL$의 **결과** | $V \uparrow$ 또는 $CL \downarrow$ |
| $F$ | fraction | 경구 생체이용률 | 흡수, first-pass |

### 1.4 NONMEM에서 이게 어디 들어가는가

NONMEM control stream의 가장 기본 골격이 정확히 이 분리를 강제함:

```
TVCL = THETA(1) * (covariate effects)
TVV  = THETA(2) * (covariate effects)
K    = CL / V    ; 이건 derived parameter
```

$CL$과 $V$를 따로 추정해야 covariate를 어느 자리에 넣을지 결정할 수 있음. $t_{1/2}$를 직접 추정하는 NONMEM 모델은 거의 없음 — 이유가 바로 이거임.

> **이 절의 한 줄**: 반감기로 시작하지 마라. **항상 $CL$과 $V$를 먼저 분리한 다음** 진단을 시작함.

---

## §2 좌표 #1 — 어느 농도 기준인가 (Matrix)

<!-- SLIDE_START: §2 | title: §2 좌표 #1 매트릭스 plasma vs blood vs unbound -->

### 2.1 왜 이게 4-좌표 중 *맨 앞*에 있어야 하는가

원본 자료에서 이 카드(M8)가 한참 뒤에 나오는데, 그러면 안 됨. 왜냐면 — 

- 신장 분해($CL_R = f_e \cdot CL$)에서 $CL$이 plasma 기준임 → matrix가 무엇인지 알아야 $f_e$ 해석이 안 흔들림
- 간 분해(well-stirred)에서 $f_{ub}$가 **혈액 기준** 비결합 분율임 → plasma 측정값을 그대로 넣으면 분자가 자릿수로 틀어짐
- PBPK input에서 $C/C_b$ 변환은 모든 organ extraction의 *분모를 정해주는 자리*임

**그래서 이 좌표를 먼저 잠그지 않으면 §3 이후가 다 무너짐.** 프롤로그의 60 L/h가 정확히 이 함정의 사례였음.

### 2.2 Plasma vs Blood — 변환 한 줄

$R = C/C_b$로 정의함(plasma 농도 / blood 농도). 핵심 변환식 [R&T pp.124–128 Eq 5-4–5-6]:

$$
\underbrace{CL_b}_{\text{혈액 CL}}=\underbrace{CL}_{\text{혈장 CL}}\cdot\underbrace{\frac{C}{C_b}}_{\text{변환비 }R}
$$

$R < 1$이면 약물이 RBC에 농축되어 있다는 뜻 → blood 농도가 plasma보다 큼 → 같은 dose에서 $CL_b$는 plasma $CL$보다 작아짐.

**Organ extraction은 무조건 blood 기준임:**

$$
\underbrace{E_H}_{\text{간 추출률}}=\frac{\underbrace{CL_{H,b}}_{\text{blood 기준 간 CL}}}{\underbrace{Q_H}_{\text{간 혈류}}}
$$

분자도 분모도 같은 단위(blood-based)여야 함. Plasma $CL$을 $Q_H$로 나누면 단위가 안 맞음 — 이게 프롤로그의 false-high extraction이 만들어진 메커니즘임.

### 2.3 60 L/h 미스터리 해결

다시 환자 차트로 돌아감:

- Plasma $CL = 60\ \mathrm{L/h}$
- $C/C_b = 0.5$ → 약물이 RBC에 절반쯤 가 있음
- $Q_H = 81\ \mathrm{L/h}$

**Step 1**: $CL_b = 60 \times 0.5 = 30\ \mathrm{L/h}$
**Step 2**: $E_H = 30 / 81 \approx 0.37$

처음에 보였던 $60/81 = 0.74$는 **단위가 틀린 비율**이었음. 실제로는 0.37, **low-to-intermediate extraction**. 

자, 이 차이가 임상에서 뭘 바꾸냐면 —

- **DDI 평가**: high extraction(>0.7) 약물은 hepatic blood flow에 더 민감하고 enzyme inhibitor에는 둔감. Low-to-intermediate(0.3–0.7)는 반대로 enzyme inhibitor 영향이 큼 → 강력한 CYP3A4 inhibitor 동반투여 안전성 라벨 문구가 완전히 바뀜.
- **간장애 라벨**: high extraction이면 hepatic blood flow 감소에 따른 dose 감량 권고가 우선. 0.37이면 enzyme capacity 감소가 더 중요한 결정 요인.
- **PBPK input**: $f_{ub} \cdot CL_{int}$ 분자에 plasma 기준 $f_u$를 넣으면 또 한 번 자릿수 틀어짐 → 다음 절에서 다룸.

> **본능 한 줄**: hepatic extraction을 판단하기 전에 손이 자동으로 가는 자리는 **"$CL$이 plasma 기준인가 blood 기준인가?"** 한 줄임. 안 묻고 가면 프롤로그 함정에 빠짐.

### 2.4 $f_u$ vs $f_{ub}$ — 또 하나의 매트릭스 함정

$f_u$와 $f_{ub}$는 이름이 비슷해서 같은 변수의 별명처럼 보이지만 **분모가 다른 두 측정량**임:

$$
\overbrace{\underbrace{f_u}_{\text{plasma 기준}}=\frac{\underbrace{C_u}_{\text{비결합 농도}}}{\underbrace{C}_{\text{plasma 총농도}}}}^{\text{plasma 측정}}\,,\qquad \overbrace{\underbrace{f_{ub}}_{\text{blood 기준}}=\frac{\underbrace{C_u}_{\text{비결합 농도}}}{\underbrace{C_b}_{\text{blood 총농도}}}}^{\text{blood 환산}}
$$

비결합 농도 $C_u$ 자체는 plasma든 blood든 동일함(자유 분자가 평형이라는 전제). 그래서 분자는 같고 분모만 바뀜. 변환식 [R&T App.D pp.775–776 Eq D-4–D-5]:

$$
\overbrace{\underbrace{f_{ub}}_{\text{blood 유리분율}}=\underbrace{f_u}_{\text{plasma 유리분율}}\cdot\underbrace{\frac{C}{C_b}}_{\text{변환비 }R}}^{\text{App.D 변환 — well-stirred 입력 직전 필수}}
$$

| 시나리오 | $R = C/C_b$ | 결과 |
|---|---:|---|
| RBC와 plasma 분배 균등 | 1.0 | $f_u = f_{ub}$ — 변환 불필요 |
| **약물이 RBC에 농축** (tacrolimus, cyclosporine) | ~0.05–0.5 | $f_{ub} \ll f_u$ — plasma $f_u$ 그대로 쓰면 well-stirred 분자 과대평가 |
| 약물이 plasma 우세 | > 1 | $f_{ub} > f_u$ (드뭄) |

Plasma에서 측정한 $f_u = 0.1$인 약물이 $R = 0.5$이면 $f_{ub} = 0.05$. **분자가 2배 차이 남.** 이게 well-stirred 식에 그대로 들어가면 high/low extraction 분류가 흔들리고, IVIVE 예측이 2배 빗나가고, PBPK simulation의 PK profile이 통째로 다른 모양으로 나옴.

### 2.5 측정 매트릭스 — Plasma / Serum / Whole blood

PopPK control stream을 받았을 때 가장 자주 발견되는 *조용한* 오류가 이거임 — **TDM 보고서의 측정 매트릭스를 확인하지 않고 plasma인 척 모델에 넣는 것.**

| 매트릭스 | 정의 | 대표 약물 |
|---|---|---|
| **Plasma** (혈장) | 항응고제 처리 후 원심분리, RBC 제거 | warfarin, phenytoin, valproate, 대부분의 항생제 |
| **Serum** (혈청) | 응고 후 원심분리, RBC + clot factor 제거 | digoxin, 일부 항경련제 |
| **Whole blood** (전혈) | RBC 포함 | **tacrolimus, cyclosporine, sirolimus, everolimus** |

**Tacrolimus가 왜 전혈 표준인가?** RBC 결합/분배가 너무 강해서 $C/C_b$가 **0.05–0.2** 수준임. Plasma 농도는 hematocrit에 따라 자릿수로 흔들림. Whole blood는 안정적임. 그래서 이식센터 TDM은 무조건 whole blood로 측정함.

만약 tacrolimus whole blood 농도를 plasma 농도로 잘못 해석하면 — $V$ 추정이 5–20배 과소평가됨. 모든 후속 PK 파라미터가 어긋남. 이게 흔히 일어남.

> **본능 3단 체크**: PK 결과 받으면 손이 자동으로 가는 자리는 ① 매트릭스(plasma/serum/whole blood) → ② $C/C_b$ → ③ well-stirred 식에서 $f_u$를 $f_{ub}$로 변환 — 이 3단 정합성 점검임. **한 단계만 빠져도 hepatic extraction 분류와 PBPK 입력이 통째로 흔들림.**

### 2.6 NONMEM에서 이게 어디 들어가는가

```
$INPUT ID TIME DV AMT MDV MATRIX CMT ...   ; MATRIX flag로 plasma/blood/wb 구분
$PK
  R = THETA(7)              ; C/C_b 변환비, covariate화 가능
  FUB = FU_PLASMA * R       ; well-stirred 입력 변환
  CL_BLOOD = CL * R         ; organ extraction 계산용
```

- `$INPUT`에 `MATRIX` flag 추가 — TDM 데이터 검토 단계에서 표준화
- $R = C/C_b$를 fixed scalar 또는 covariate(hematocrit 의존성 큰 약물)로 처리
- well-stirred fitting 시 $f_u$ 입력은 *반드시* $f_{ub}$로 변환한 후 넣음

> **이 절의 한 줄**: 4-좌표의 1번 매트릭스를 안 풀고 §3 이후로 가면 안 됨. 신장·간 분해는 매트릭스가 잠긴 뒤에야 작동함.

---

## §3 좌표 #2A — 신장 청소율 분해

<!-- SLIDE_START: §3 | title: §3 좌표 #2A 신장 분해 CL_R = f_e · CL -->

### 3.1 분해의 의미 — 경로 분해 vs 비례 단축

기본 식 [G&W pp.49–50 Eq 2:87–2:89; R&T pp.139–142]:

$$
\underbrace{CL_R}_{\text{신장 CL}}=\underbrace{f_e}_{\text{신장 지분}}\cdot\underbrace{CL}_{\text{전체 CL}}, \qquad \underbrace{CL}_{\text{전체 CL}}=\underbrace{CL_R}_{\text{신장}}+\underbrace{CL_H}_{\text{간}}+\underbrace{CL_{other}}_{\text{기타}}
$$

이 식의 *진짜 의미*는 "신장이 차지하는 지분이 $f_e$"라는 게 아님. **신부전 covariate가 들어갈 자리가 $CL$ 전체가 아니라 $CL_R$ 위치 하나라는** 분해 규칙임.

실수 패턴이 이거임 — neonate나 신부전 환자 PopPK 할 때 본능적으로 `TVCL = THETA(1) * (CRCL/100)**THETA(2)`로 covariate를 *전체 CL*에 곱함. 그러면 nonrenal pathway까지 같이 줄어듦. Drug X의 $f_e$가 0.4면 60%가 nonrenal인데, 이 60%까지 신부전에 비례해 줄어드는 가짜 효과가 생김 → systematic CL underestimation → dose adjustment가 안전성 측으로 너무 보수적으로 빠짐.

올바른 covariate 식은 분해된 자리에 거는 것:

```
TVCL_R   = THETA(1) * (CRCL/100)**1     ; 신장 covariate는 여기만
TVCL_NR  = THETA(2)                      ; nonrenal은 신기능 무관
TVCL     = TVCL_R + TVCL_NR              ; 합쳐서 모델에 넣음
```

### 3.2 신장 생리 — 30초 요약

[G&W p.48; R&T pp.119–120]: 네프론은 보먼주머니 → 근위세뇨관 → 헨레고리 → 원위세뇨관 → 집합관. GFR ≈ **120 mL/min** [R&T]. Urine pH 범위 4.5–8. 평균 신장 혈류 약 **1.1 L/min**(=66 L/h) — 이게 신장 추출의 혈류 상한임.

여기서 한 가지 — 신장 추출률을 따질 일이 별로 없는 이유가 **신장 혈류가 간 혈류보다 작아서**라기보다, 신장 청소율 자체가 일반적으로 GFR(120 mL/min) 수준에서 결정되기 때문임. 분비가 강하게 작동하는 약물(예: penicillin, ranitidine)에서만 $CL_R$이 혈류 한계에 근접함.

### 3.3 여과 + 분비 − 재흡수

핵심 분해 [R&T p.139 Eq 5-17–5-18]:

$$
\overbrace{\underbrace{CL_R}_{\text{순 신장 CL}}=\underbrace{(1-F_R)}_{\text{재흡수 잔여율}}\cdot(\underbrace{CL_f}_{\text{여과}}+\underbrace{CL_S}_{\text{분비}})}^{\text{1차 재흡수 가정 하의 단순 모델}}, \qquad \underbrace{CL_f}_{\text{여과 CL}}=\underbrace{f_u}_{\text{유리분율}}\cdot\underbrace{GFR}_{\text{여과율}}
$$

**진단 패턴 한 줄**:
- $CL_R > f_u \cdot GFR$ → **분비(secretion) 작동 중**. Active transport가 추가로 약물을 세뇨관 내강으로 밀어내고 있음.
- $CL_R < f_u \cdot GFR$ → **재흡수(reabsorption)** 일어나는 중 OR 측정 방식이 잘못됐는지 의심.

### 3.4 1차 재흡수 가정의 함정 — methamphetamine 사례

위 $(1-F_R)$ 항은 "재흡수가 농도 무관한 일정 분율"이라는 1차 가정에 기댄 단순 모델임. **실제 재흡수는 세 변수에 강하게 의존함** — 소변 유속, 소변 pH, 약물의 친유성/이온화도 [R&T pp.142–148]:

$$
\overbrace{F_R}^{\text{재흡수 분율}}=\underbrace{f\bigl(\underbrace{\text{urine pH}}_{\text{이온화 균형}},\ \underbrace{\text{urine flow}}_{\text{체류시간}},\ \underbrace{\text{lipophilicity}}_{\text{막 투과}},\ \underbrace{\text{transporter}}_{\text{활성 수송}}\bigr)}_{\text{다변수 함수 — 단순 분율로 묶을 수 없음}}
$$

임상 anchor [R&T p.145, Fig 5-16]:

| 약물 | 산성 소변 (pH 4.9–5.3) | 알칼리성 소변 (pH 7.8–8.2) |
|---|---|---|
| **Methamphetamine** (pKa 10, 약염기) | 회수율 **70–80%** | 회수율 **1–2%** |
| **Phenobarbital** (pKa 7.2, 약산) | 낮은 $CL_R$ | 알칼리화 시 $CL_R \uparrow$ |

→ **소변 pH 하나로 $CL_R$이 자릿수 단위로 흔들림.** $(1-F_R)$ 단순 분율로 봉합 불가. 강제 이뇨(forced diuresis)와 소변 알칼리화가 phenobarbital 중독 치료에 쓰이는 이유가 정확히 이거임 [R&T p.147].

NONMEM에서 이게 보이는 신호는 — 같은 환자에서 $CL_R$ 추정치가 occasion 간에 자릿수로 흔들리는 경우, 또는 urine pH/flow가 잔차 변이로 흡수돼 들어가는 경우임. Inter-occasion variability(IOV) 항을 $CL_R$에 별도로 걸어야 fitting이 안정화됨.

### 3.5 신장 transporter DDI — OAT/OCT/MATE 지도

신장 근위세뇨관에는 명확한 transporter 배치가 있음 — basolateral 쪽에 **OAT1/OAT3, OCT2**가, apical 쪽에 **MATE1/MATE2-K, MRP2/MRP4, P-gp**가 있어서 약물 유입과 유출이 분리되어 일어남.

| DDI 짝 | 기전 | 결과 |
|---|---|---|
| **Metformin + cimetidine** | OCT2/MATE 억제 | Metformin AUC 약 1.5배 ↑ |
| **Probenecid + penicillin** | OAT 억제 | β-lactam 분비 차단, 농도 유지 (고전 anchor) |
| **Dolutegravir + metformin** | MATE1 억제 | Metformin 노출 상승 |
| **Tenofovir nephrotoxicity** | OAT1/3 매개 uptake | 세뇨관 세포내 농도 상승 → 신독성 |

이거 PopPK에서 자주 놓침. 신장 covariate를 CrCl 단독으로만 잡으면 OCT2/MATE 다형성이나 동반 약물 효과가 잔차 변이로 흡수돼버림. Metformin PopPK에서 cimetidine 동반복용 여부를 covariate로 안 넣으면 IIV가 부풀어 오름.

### 3.6 eGFR 식 선택 — 라벨링과의 정합성

이거 정말 자주 놓침. 신부전 라벨에 "CrCl 30 mL/min에서 50% 감량" 같은 권고가 있을 때, **그 CrCl이 어떤 식으로 계산됐는지 보고서에 안 적힌 경우가 대부분임.**

| 추정식 | 입력 | 단위 | 임상 위치 |
|---|---|---|---|
| **Cockcroft-Gault (CG)** | SCr, 나이, 체중, 성별 | mL/min | 약물 라벨 cutoff 표준 (가장 자주 쓰임) |
| **MDRD** | SCr, 나이, 인종, 성별 | mL/min/1.73 m² | CKD 진단·분류 |
| **CKD-EPI** | SCr (또는 Cystatin C), 나이, 인종, 성별 | mL/min/1.73 m² | 정상~약간 감소 영역에서 가장 정확 |

$$
\underbrace{\text{CrCl}_{\text{CG}}}_{\text{Cockcroft-Gault}}=\frac{\overbrace{(140-\text{Age})}^{\text{연령항}}\cdot\overbrace{\text{Weight}}^{\text{체중항}}}{\underbrace{72\cdot\text{SCr}}_{\text{혈청 Cr 비례}}}\cdot\underbrace{(0.85\text{ if female})}_{\text{성별 보정}}
$$

**점검 본능**:
- 단위 차이 — CG는 mL/min(절대), MDRD/CKD-EPI는 mL/min/1.73 m²(BSA 정규화). 같은 환자가 식에 따라 cutoff를 넘나들 수 있음.
- 비만 환자 — CG는 체중항 때문에 과대평가. Adjusted body weight 적용 필요.
- 약물 라벨 cutoff와의 정합성 — 대부분 신부전 권고가 CG 기반이라, PopPK에서 CKD-EPI로 covariate를 잡았어도 라벨 검증 단계에서는 CG로 재계산하는 게 안전.

### 3.7 담즙 청소율 + 장간순환

신장·간 외 *제3의* 배설 경로 — 담즙임. M2 가산성 식에서 $CL_{other}$로 묶이는 자리.

$$
\underbrace{CL_{\text{biliary}}}_{\text{담즙 CL}}=\frac{\overbrace{(\text{Bile flow})}^{\approx 0.5{-}0.8\ \text{mL/min}}\cdot\overbrace{(C_{\text{bile}})}^{\text{담즙 농도}}}{\underbrace{C_{\text{plasma}}}_{\text{혈장 농도}}}
$$

고담즙 CL의 4가지 조건 [R&T p.138]: ① apical efflux transporter (P-gp, MRP2, BCRP) 기질, ② 극성, ③ MW > 350, ④ 이온화 가능. **글루쿠로니드 대사체**(MW > 350, 극성, pKa ~3)가 전형적임 — 이게 §4.3 Phase II와 직접 연결됨.

**중요 정정**: **장간순환은 소실이 아니라 분포의 일부임** [R&T p.138]. 

```
간 → 담즙 → 소장 → 재흡수 (다시 간) : 분포의 일부
                ↓
                분변 배설 : 진짜 소실
```

장간순환이 일어났다고 약물이 체외로 나간 게 아님. 그래서 청소율 가산성 식에는 장간순환 자체가 아니라 **재흡수되지 않고 분변으로 빠진 분율만** 들어감.

임상 신호는 — **PK 곡선의 secondary peak**(2차 피크), $t_{1/2}$ 연장, 그리고 β-glucuronidase 영향 항생제 동반투여 시 PK 변화. **MMF(MPA-MPAG 순환)**이 대표 anchor임 — 모약물의 글루쿠로니드 대사체가 장내 세균 β-glucuronidase에 의해 가수분해되어 모약물로 되돌아옴.

**NONMEM 신호**: 2차 피크가 잡히는 시점에 dose 입력(MTIME 또는 transit chain)을 안 넣으면, 단순 1구획·2구획 fitting 시 terminal slope가 시간에 따라 변화하는 인상을 줘서 **비선형 PK로 오인**됨. 이거 임상 PK 보고서에서 자주 발견되는 misdiagnosis임.

### 3.8 데이터로 풀기 — ARE plot vs Excretion-rate plot

소변 데이터 받으면 두 가지 plot이 가능함 [G&W pp.50–52 Eq 2:90–2:98]:

**Rate plot** (구간 배설속도):

$$
\underbrace{\ln\left(\frac{dX_u}{dt}\right)}_{\text{로그 배설속도}}=\underbrace{\ln\left(CL_R\cdot\frac{D_{iv}}{V}\right)}_{\text{초기절편}}-\underbrace{K}_{\text{소실기울기}}\cdot\underbrace{t}_{\text{시간}}
$$

**ARE plot** (잔여 누적량):

$$
\underbrace{\ln(X_{u,0-\infty}-X_u)}_{\text{잔여량 로그}}=\underbrace{\ln(X_{u,0-\infty})}_{\text{총량절편}}-\underbrace{K}_{\text{소실기울기}}\cdot\underbrace{t}_{\text{시간}}
$$

| 판단 축 | Rate plot | ARE plot |
|---|---|---|
| 수집 간격이 반감기보다 길 때 | 취약 | 상대적 안정 |
| 불완전 방광 배출 | 취약 | 누적 편향 가능 |
| $X_{u,0-\infty}$ 필요도 | 낮음 | 높음 |
| pH/flow에 따른 $CL_R$ 시간 변동 | **잘 보임** | 평탄해져서 덜 보임 |

**핵심 trap**: 두 plot의 slope가 안 맞을 때, 본능이 "아 다구획 모델이 필요하나?"로 빠지면 안 됨. **먼저 의심할 건 ① collection interval, ② bladder emptying, ③ pH/flow 변동임.** 이 순서로 거른 다음에야 구조 모델로 넘어가는 거임.

### 3.9 NONMEM에서 이게 어디 들어가는가

```
$INPUT ID TIME DV AMT MDV DVID ...    ; DVID로 plasma(1)/urine(2) endpoint 구분
$PK
  TVCL_R   = THETA(1) * (CRCL/100)
  TVCL_NR  = THETA(2)
  TVCL     = TVCL_R + TVCL_NR
  TVV      = THETA(3)
$ERROR
  IF (DVID.EQ.1) Y = IPRED * (1+EPS(1)) + EPS(2)   ; plasma
  IF (DVID.EQ.2) Y = IPRED * (1+EPS(3)) + EPS(4)   ; urine — 잔차가 더 큼
```

핵심은 **plasma와 urine endpoint를 한 모델에서 동시에 fitting**, 잔차오차는 별도로(plasma CV ~2.84%, urine CV ~8.96%, M7 PK5 anchor). 분리하면 $f_e$와 $CL_R$를 따로 추정할 수 없음.

> **이 절의 한 줄**: 신부전 covariate는 *분해된 자리*에 거는 거임 — $CL$ 전체가 아니라 $CL_R$에. 그리고 신장 분해는 단순 비례식이 아니라 **여과·분비·재흡수의 다변수 함수**이고, **장간순환은 분포의 일부**라는 두 정정을 본능에 새김.

---

## §4 좌표 #2B — 간 청소율 분해

<!-- SLIDE_START: §4 | title: §4 좌표 #2B 간 분해 well-stirred + 확장 -->

### 4.1 Well-stirred 식의 본능적 판독

핵심 식 [G&W pp.79–82 Eq 2:188–2:195; R&T pp.130–135]:

$$
\underbrace{CL_{H,b}}_{\text{간 CL_b}}=\underbrace{Q_H}_{\text{간혈류}}\cdot\underbrace{E_H}_{\text{추출률}}=\frac{\underbrace{Q_H}_{\text{혈류한계}}\cdot\underbrace{f_{ub}}_{\text{혈액 유리분율}}\cdot\underbrace{CL_{int}}_{\text{간세포 제거능}}}{\underbrace{Q_H}_{\text{혈류}}+\underbrace{f_{ub}\cdot CL_{int}}_{\text{유리·효소축}}}
$$

이 식 자체가 어려운 게 아님. **분모에 $Q_H + f_{ub}\cdot CL_{int}$가 있다는 거** — 이 두 항 중 어느 게 큰지가 임상 결정 전체를 가름.

비유로 보면 간은 수도관 + 정수기 장치임. 물(혈류 $Q_H$)이 적게 들어오면 혈류가 한계고, 정수기 용량(효소·결합 $f_{ub}\cdot CL_{int}$)이 작으면 그 쪽이 한계임. 둘 중 작은 쪽이 전체 throughput을 결정함.

극한 근사:

$$
\begin{aligned}\underbrace{f_{ub}CL_{int}\gg Q_H}_{\text{제거용량>혈류}}&\Rightarrow \underbrace{CL_{H,b}\approx Q_H}_{\text{혈류제한, high extraction}}\\ \underbrace{f_{ub}CL_{int}\ll Q_H}_{\text{제거용량<혈류}}&\Rightarrow \underbrace{CL_{H,b}\approx f_{ub}CL_{int}}_{\text{용량·결합제한, low extraction}}\end{aligned}
$$

$Q_H \approx$ **1.35 L/min = 81 L/h** [R&T p.125]. 이걸 기준으로 $f_{ub}\cdot CL_{int}$가 81보다 큰지 작은지를 *손이 자동으로 비교하는* 게 본능임.

**임상에서 이게 뭘 바꾸냐면**:

| 분류 | DDI 민감도 | Hepatic blood flow 민감도 | $f_u$ 변화 민감도 |
|---|---|---|---|
| **High extraction** ($E_H > 0.7$) | 효소 inhibitor에 둔감(IV) | **매우 민감** | IV total은 둔감, oral은 민감 |
| **Low extraction** ($E_H < 0.3$) | **매우 민감** | 둔감 | total CL에 민감 |
| **Intermediate** (0.3–0.7) | 둘 다 어느 정도 작동 | 어느 정도 | endpoint에 따라 |

그래서 high vs low가 라벨 문구를 완전히 다르게 만듦. 그런데 **이 분류 자체가 매트릭스 변환(§2)을 거친 뒤에야 의미가 있음** — 프롤로그 60 L/h가 정확히 이 단계에서 분류가 바뀐 사례임.

### 4.2 $CL_{int}$ 자체가 합성이다 — 효소·다형성·염증

위 식에서 $CL_{int}$를 단일 숫자로 보면 안 됨. 실제로는 **효소 분포 + 유전형 다형성 + 시간 의존 변동**의 합성임.

**효소 분포** [R&T pp.121–123]:

| CYP | 간 abundance | 처방약 CL 기여 | 특기 |
|---|---|---|---|
| **CYP3A4/5** | 최대 (간+장벽) | ~40–50% | 가장 광범위 |
| **CYP2D6** | ~2% | ~25% | 다형성 임상 영향 큼 |
| **CYP2C9** | 다수 | 산성 약물 (warfarin, NSAIDs) | |
| **CYP2C19** | 다수 | omeprazole, clopidogrel | 다형성 |
| **CYP1A2** | 다수 | caffeine, theophylline | 흡연 유도 |
| **CYP2E1** | 다수 | 알코올, halothane | acetaminophen 활성화 |

여기서 **CYP2D6가 가장 흥미로운 비대칭**임 — abundance는 2%인데 처방약 CL의 25% 담당. 그래서 CYP2D6 다형성 영향이 임상에서 제일 격렬함.

**CYP2D6 다형성 phenotype** [R&T pp.549–559]:

| Phenotype | 유전형 | 활성 | 임상 |
|---|---|---|---|
| **PM** (Poor) | *4/*4 | ~0 | substrate AUC ↑↑ (4배+) |
| **IM** (Intermediate) | *10/*10 | 0.25–0.5 | 중간 |
| **EM** (Extensive) | wt | 1.0 | 참조 |
| **UM** (Ultra-rapid) | *1×N | 1.5–2+ | substrate AUC ↓ → codeine→morphine의 경우 오히려 morphine 독성 |

**Desipramine + quinidine** 사례 [R&T p.549]: quinidine은 CYP2D6 강력 억제제. EM이 사실상 PM phenotype으로 *전환*되고, desipramine CL이 4배 감소, $t_{1/2}$가 4배 연장됨.

위에 inhibitor가 들어가는 시나리오 — **CYP polymorphism + inhibitor**가 DDI 위험이 가장 크게 증폭되는 자리임 [R&T p.557 Eq 17-18]:

$$
\overbrace{\text{Maximum exposure ratio (PM, inhibitor)}}^{\text{R\&T Eq 17-18}}=\frac{1}{\underbrace{1-f_{m,\text{POLY}}-f_{m,\text{NP}}}_{\text{차단되지 않은 경로 분율}}}
$$

$f_{m,\text{POLY}}$가 0.75에 도달하면 PM에서 nonpolymorphic pathway 강력 억제 시 노출비가 10배 이상까지 갈 수 있음.

**염증성 CYP downregulation** — 패혈증·중증 감염·진행성 종양·자가면역에서 IL-6, TNF-α, IL-1β가 hepatic CYP 발현을 억제함. CYP3A4가 가장 민감, CYP1A2·2C9·2D6·2C19도 영향. PopPK 신호는:

- 정상 자원자 데이터에서 외삽되지 않는 ICU/중증감염/진행암 cohort
- $CL_{int}$가 환자 상태에 따라 시간 의존적으로 변하므로, 베이지안 individual estimate가 한 방향으로 지속 치우치면 의심
- COVID-19 cytokine storm에서 narrow therapeutic window 약물(immunosuppressant, anticoagulant) 노출 변동 임상 보고

→ 이게 단순 IIV가 아니라 **체계적 IOV** 신호임. PopPK에서 IOV 항을 $CL$에 별도로 안 걸면 fitting이 불안정해짐.

### 4.3 Phase I 옆자리에 항상 Phase II — UGT 축

여기서 자주 놓치는 게 있음 — **대사 = CYP**라는 무의식적 등식. CYP가 abundance와 처방약 비중에서 가장 크긴 하지만, **임상에서 가장 격렬한 phenotype 차이를 만드는 자리는 오히려 UGT 쪽**에 자주 있음.

| 분류 | 반응 |
|---|---|
| **Phase I** | 산화·환원·가수분해 (CYP가 대표) |
| **Phase II** | 접합 (UGT·SULT·NAT·GST) |

Phase I과 Phase II는 **흔히 순차적**임 — CYP가 hydroxyl을 만들고, UGT가 거기에 glucuronic acid를 붙임. 그래서 CYP 기질 약물 대부분이 Phase II 후속을 거침.

$$
\underbrace{CL_{int,\text{total}}}_{\text{전체 내재 CL}}=\underbrace{\sum_i CL_{int,\text{CYP}_i}}_{\text{Phase I 합}}+\overbrace{\underbrace{\sum_j CL_{int,\text{UGT}_j}}_{\text{Phase II UGT 합}}+\underbrace{CL_{int,\text{SULT}}+CL_{int,\text{others}}}_{\text{기타 접합}}}^{\text{흔히 누락되는 좌표}}
$$

**임상 anchor 4개**:

**(1) Irinotecan / SN-38 (UGT1A1*28)**: irinotecan → SN-38(활성) → SN-38G(비활성, UGT1A1). UGT1A1*28 동형접합체(Gilbert syndrome, Caucasian ~10%)에서 SN-38 비활성화가 느려져 dose-limiting myelosuppression·diarrhea 위험. **약물 라벨에 *28/*28 환자 시작 용량 감량 권고**가 들어가 있음 — UGT가 라벨을 만든 대표 anchor.

**(2) Lamotrigine + Valproate (UGT2B7 억제)**: lamotrigine 단독 $t_{1/2}$ ~25h. Valproate 동반 시 UGT2B7 억제로 CL 반감 → $t_{1/2}$ ~50h. **시작 용량을 절반 이하로 낮추는 적정** 필수(SJS 위험).

**(3) Mycophenolate (MMF) — UGT + 장간순환**: MMF → MPA → MPAG(UGT) → 담즙 → 장내 β-glucuronidase → MPA로 재가수분해 → 재흡수. **2차 피크 PK 곡선**과 항생제(β-glucuronidase 억제) 동반투여 시 MPA 노출 감소. §3.7 enterohepatic cycling과 직접 연결됨.

**(4) Morphine / M6G (UGT2B7)**: morphine의 활성 대사체 M6G가 UGT2B7로 생성. **신부전에서 M6G 축적 → 진정·호흡억제** — §6.4 active metabolite 신부전 시나리오의 정확한 구조.

**신생아 UGT 미성숙** — chloramphenicol gray baby syndrome이 고전 anchor. UGT 발달이 늦어서 chloramphenicol glucuronide conjugation이 안 됨 → 모약물 축적 → 독성. §8 maturation function이 정확히 이 좌표에 맞아 들어감.

### 4.4 IVIVE가 빗나갈 때 — 입력 정보 손실 진단

자, in vitro에서 microsome 또는 hepatocyte로 $CL_{int}$를 측정한 다음, well-stirred 식을 거쳐 in vivo CL을 예측함. 이게 IVIVE임. Phase 1 임상에서 5–10배 빗나가는 경우가 흔함.

**본능 패턴**: IVIVE mismatch 보고서 받으면 첫 손은 "hepatic model이 안 맞나?"가 *아님*. 첫 손은 **"in vitro 입력 정보가 이미 뭉개졌나?"**임.

세 가지 함정 [G&W pp.85–89]:

**(1) 단일 농도 함정**: 한 농도에서 측정한 rate를 $V_{max}/K_m$처럼 쓰면 비선형성·포화를 통째로 놓침. 농도-속도 관계 곡선 자체가 사라짐.

**(2) MMP 보정 함정**: 간 g당 microsomal protein 보정. 평균값 하나로 끝나지 않음. G&W Table 2.8: 같은 약물에서 MMP를 **20 / 50 / 77 mg/g**로 바꿨을 때, 분류가 **low → intermediate → high**까지 *통째로* 바뀜. 어느 값을 쓸지가 환자마다 다르고, 평균값 사용 시 그 변이가 잔차로 흡수됨.

**(3) 데이터 압축 함정**: 농도-속도 관계를 단일 $CL_{int}$로 압축하면 곡선 형태·이상치 구조가 사라짐. 흐릿하게 압축된 사진을 고해상도로 띄울 수 없는 것과 같음 — 원본 정보가 이미 소실됐기 때문에, 그 위에 어떤 정교한 hepatic model을 얹어도 곡률이 복구되지 않음.

> **본능 한 줄**: IVIVE mismatch → ① single-point rate? → ② MMP/scaling 변이? → ③ data 압축? → ④ transporter/permeability 누락(§4.5)? — 이 순서로 점검함. Hepatic 식을 의심하는 건 마지막 순서임.

### 4.5 효소가 아니라 막이 병목일 때 — $\rho$

기본 well-stirred는 "간세포 안팎의 unbound 농도가 빠르게 평형"이라고 가정함. 근데 hepatic uptake permeability가 느리면 이 가정이 무너짐 — 세포 내부 unbound 농도가 혈액 쪽보다 *낮아짐*. 그러면 $CL_{int}$가 충분해도 약물이 hepatocyte로 들어가질 못해서 hepatic clearance가 낮음.

비유: 공장 정문 회전문이 느리면 안쪽 라인이 아무리 빨라도 전체 생산량이 떨어지는 것과 같음.

이걸 정량화하는 항이 $\rho$임 [R&T App.E pp.778–779 Eq E-9–E-15]:

$$
\underbrace{\rho}_{\text{세포접근성}}=\frac{\underbrace{P_{in}\cdot SA}_{\text{유입투과}}}{\underbrace{P_{out}\cdot SA}_{\text{유출투과}}+\underbrace{CL_{int}}_{\text{대사제거}}}
$$

수정된 hepatic clearance:

$$
\underbrace{CL_{H,b}}_{\text{간 CL_b}}=\frac{\underbrace{Q_H}_{\text{혈류}}\cdot\underbrace{f_{ub}}_{\text{혈액 유리분율}}\cdot\underbrace{\rho}_{\text{세포접근성}}\cdot\underbrace{CL_{int}}_{\text{대사제거}}}{\underbrace{Q_H}_{\text{혈류}}+\underbrace{f_{ub}\cdot \rho\cdot CL_{int}}_{\text{보정 제거축}}}
$$

passive diffusion이 충분히 크면 $\rho \to 1$이 되어 기본 well-stirred로 환원됨. 반대로 uptake permeability가 작으면 $\rho < 1$이고 clearance가 permeability-limited가 됨.

**임상 신호**: PopPK에서 *모든 cohort*에서 $f_u$ covariate가 비유의로 떨어지고 계수가 ~0인데, IVIVE는 $CL_{int}$만 5–10배 underpredict — 이 패턴이 보이면 well-stirred 자체가 아니라 $\rho$ 누락을 의심함. Covariate 자리를 $f_u$에서 SLCO1B1 genotype 같은 transporter 변수로 옮겨야 함.

### 4.6 Extended Clearance — Sirianni-Pang 정량 분해

$\rho$가 정성적 신호라면, 이걸 정량으로 펼친 게 Sirianni-Pang Extended Clearance Model임 [R&T App.E pp.778–779; R&T pp.136–138 box]:

$$
\overbrace{\underbrace{CL_{H,b}}_{\text{Extended 간 CL}_b}=\frac{\underbrace{Q_H}_{\text{혈류}}\cdot\underbrace{f_{ub}}_{\text{혈액 유리분율}}\cdot\underbrace{PS_{inf}}_{\text{유입 투과}}\cdot(\underbrace{CL_{int,met}}_{\text{대사 CL}}+\underbrace{PS_{eff,bile}}_{\text{담즙 efflux}})}{\underbrace{Q_H}_{\text{혈류}}(\underbrace{PS_{eff,sin}+CL_{int,met}+PS_{eff,bile}}_{\text{세포 내 처리 합}})+\underbrace{f_{ub}\cdot PS_{inf}}_{\text{유입 단계}}(\underbrace{CL_{int,met}+PS_{eff,bile}}_{\text{비유입 처리}})}}^{\text{Sirianni-Pang Extended Clearance}}
$$

| 기호 | 의미 | 생리학적 자리 |
|---|---|---|
| $PS_{inf}$ | sinusoidal uptake | basolateral OATP/OCT/OAT |
| $PS_{eff,sin}$ | sinusoidal efflux | basolateral MRP3/4 (혈액 방향) |
| $CL_{int,met}$ | 세포 내 대사 | CYP/UGT |
| $PS_{eff,bile}$ | canalicular efflux | apical P-gp/BCRP/MRP2 (담즙 방향) |

**극한 분기**:

| 조건 | 결과 | 임상 |
|---|---|---|
| $PS_{inf} \gg CL_{int,met} + PS_{eff,bile}$ | well-stirred 환원 (§4.1과 동일) | 수동확산 우세 |
| $PS_{inf} \ll CL_{int,met}$ | **Uptake-limited** ($CL_{H,b} \approx f_{ub} \cdot PS_{inf}$) | **statin 계열 (OATP1B1 기질)** |
| $PS_{eff,bile} \gg CL_{int,met}$ | Biliary efflux-limited | P-gp/BCRP 기질 |

**Statin anchor**: rosuvastatin, pitavastatin은 OATP1B1 uptake-limited임. **SLCO1B1*5 다형성**에서 AUC가 2–3배 상승. **Cyclosporine·gemfibrozil + statin** DDI는 OATP 억제가 효소 억제보다 영향이 큼 — 그래서 statin 라벨에 cyclosporine 동반 시 max dose 제한이 박혀 있음.

**Pravastatin**: 거의 전체가 OATP1B1 uptake에 의존 — well-stirred 단순 적용 시 hepatic CL 예측이 5–10배 underpredict됨. IVIVE 함정의 대표 사례. PopPK에서 *covariate 자리가 $f_{ub}$가 아니라 $PS_{inf}$*인 경우임.

### 4.7 DDI는 inhibition만이 아니다 — Induction 축

본 챕터의 DDI 사례가 inhibition 일색이면, 임상에서 **induction DDI**를 통째로 놓침. 두 기전은 분자생물학적으로 다름:

- **Inhibition**: 효소·수송체 *활성*을 즉시 떨어뜨림 (분 단위)
- **Induction**: mRNA 합성 → 단백 합성 → 활성 발현의 1–2주 timescale, 효소·수송체 *발현*을 높임

**주요 inducer 지도** [R&T pp.121–123, Ch.17]:

| Inducer | 기전 | 영향 받는 것 | 결과 |
|---|---|---|---|
| **Rifampin** | PXR ligand | CYP3A4, 2B6, 2C9, **P-gp, BCRP, OATP1B1/1B3** | midazolam·warfarin·statin·digoxin·피임약 AUC ↓ 30–80% |
| **Carbamazepine** | PXR/CAR | CYP3A4, **P-gp** | **자기유도(autoinduction)** — 자기 CL이 시간 따라 증가 |
| **St. John's Wort** | PXR | CYP3A4, P-gp | cyclosporine 거부반응 (herbal-drug 고전 anchor) |
| **Phenytoin, Phenobarbital** | CAR | CYP3A, 2C, P-gp | 전형적 inducer |
| **Smoking (PAHs)** | AhR | CYP1A2 | caffeine, theophylline CL ↑ |

$$
\overbrace{\underbrace{CL_{H,b,\text{induced}}}_{\text{유도 후 간 CL}}=\underbrace{Q_H}_{\text{혈류}}\cdot\overbrace{E_H(\underbrace{CL_{int}\cdot\alpha_{ind}}_{\text{유도된 }CL_{int}}, \underbrace{PS_{inf}\cdot\beta_{ind}}_{\text{유도된 uptake}})}^{\text{효소·수송체 양쪽 모두 변화}}}^{\text{Induction effect on Extended Clearance}}
$$

$\alpha_{ind}, \beta_{ind}$가 induction fold(rifampin의 경우 CYP3A4 ~5–10, P-gp ~2–3).

**Inhibition과 결정적으로 다른 점**:
- **워시아웃**: rifampin 중단 후 효소 baseline 복귀에 약 2주 — DDI design에서 washout period가 핵심
- **임상 영향 방향**: inhibition은 substrate ↑ → 독성. Induction은 substrate ↓ → **치료 실패**(피임실패, 거부반응, 항응고 효과 상실)

**Carbamazepine autoinduction** — 처음 1–2주 동안 자기 자신의 CL이 점점 증가함. 단순 1구획 fitting 시 terminal slope가 시간에 따라 가팔라지는 것처럼 보임. NONMEM에서 *days since inducer start*를 time-varying covariate로 모델링해야 잡힘. Binary covariate로는 induction의 시간 진행을 놓침.

### 4.8 NONMEM에서 이게 어디 들어가는가

OATP 기질 약물(statin 등):
```
TVCL = THETA(1) * (ALB/40)**THETA(5) * (SLCO_GENO_FACTOR)
       ; SLCO1B1*5 carrier에서 PS_inf 감소 → CL 감소
```

Rifampin 동반 cohort:
```
DAYS_INDUCER = (TIME - RIFAMPIN_START_TIME)
INDUCTION_FACTOR = 1 + (THETA(6)-1) * (1 - EXP(-THETA(7)*DAYS_INDUCER))
TVCL = THETA(1) * INDUCTION_FACTOR
```

CYP polymorphism cohort:
```
IF (CYP2D6_PHENO.EQ.1) PHENO_FACTOR = 0.05   ; PM
IF (CYP2D6_PHENO.EQ.2) PHENO_FACTOR = 0.4    ; IM
IF (CYP2D6_PHENO.EQ.3) PHENO_FACTOR = 1.0    ; EM (참조)
IF (CYP2D6_PHENO.EQ.4) PHENO_FACTOR = 1.8    ; UM
TVCL_2D6 = THETA(2) * PHENO_FACTOR
```

> **이 절의 한 줄**: 간 CL을 만났을 때 본능은 ① $Q_H$ vs $f_{ub}\cdot CL_{int}$ 비교 → ② $CL_{int}$ 자체가 효소·다형성·염증 합성임을 기억 → ③ Phase II 좌표 같이 점검 → ④ IVIVE 빗나가면 입력 정보 손실부터 의심 → ⑤ 막 병목 가능성($\rho$) → ⑥ Sirianni-Pang으로 uptake/met/efflux 분해 → ⑦ Induction 축도 본능에 포함. 7단 동선임.

---

## §5 좌표 #3 — 어느 투여 경로인가

<!-- SLIDE_START: §5 | title: §5 좌표 #3 투여 경로 IV vs Oral -->

### 5.1 같은 약, 다른 답 — Route × Extraction × Endpoint 매트릭스

"High extraction이면 $f_u$ 무관" — 이 한 줄, 약리학 시험에는 정답이지만 **임상에서는 절반의 진실**임. 정확히는 **IV total concentration endpoint에 한정되는 진술**임. Route가 바뀌거나 endpoint가 unbound로 바뀌면 결론이 뒤집힘.

| 시나리오 | Total $C$ / AUC | Unbound $C$ |
|---|---|---|
| **IV + High** | $CL \approx Q_H$, total은 $f_u$에 둔감 | $C_u = f_u C$, $f_u$ ↑ 시 unbound ↑ 가능 |
| **IV + Low** | $CL \approx f_u\cdot CL_{int}$, total $\downarrow$ | $C_u$는 대체로 $CL_{int}$가 보존 |
| **Oral + High** | first-pass 때문에 total AUC가 $f_u\cdot CL_{int}$에 민감 | unbound AUC는 $CL_{int}$ 중심 |
| **Oral + Low** | total AUC가 $f_u\cdot CL_{int}$에 민감 | unbound AUC는 $CL_{int}$ 중심 |

핵심 식 [G&W pp.83–85; R&T pp.150–163]:

$$
\begin{aligned}\text{IV high: }&\underbrace{CL\approx Q_H}_{\text{혈류제한 CL}},\quad \underbrace{C_u=f_uC}_{\text{유리농도 확인}}\\ \text{Low/oral 축: }&\underbrace{CL\approx f_uCL_{int}}_{\text{결합·용량민감}},\quad \underbrace{AUC\propto (f_uCL_{int})^{-1}}_{\text{경구노출 민감}}\end{aligned}
$$

→ **3-축 좌표화**: route × extraction class × total/unbound endpoint. 이 셋 중 하나라도 빠뜨리고 결론 내면 다른 시나리오로 일반화될 때 깨짐.

### 5.2 임상 anchor 5개

원본의 5개 사례를 그대로 가져옴 — 이게 매트릭스 각 칸을 채우는 임상 anchor임.

**(1) Alfentanil (저추출 opioid) + Rifampin** [R&T p.152]: rifampin이 CYP3A를 강력하게 *induce*함. 저추출 약물이라 $CL$ ↑, AUC ↓로 *직접 반응*. → **"저추출 약물은 $CL_{int}$ 변화에 직접 반응"**의 사례.

**(2) Alprenolol (고추출 β차단제) + Pentobarbital(효소 유도)** [R&T p.153]: 같은 효소 유도라도 IV alprenolol은 high extraction의 혈류 제한 때문에 변화가 작음. 근데 **경구 생체이용률은 분명히 감소함**. → **"같은 약이라도 IV와 oral에서 효소 유도에 반응하는 방식이 다름"**의 사례.

**(3) Fentanyl (고추출 opioid) + Itraconazole / Ritonavir** [R&T pp.154–155]: itraconazole(약한 CYP3A 억제)은 IV fentanyl PK에 큰 영향 없음. 근데 **ritonavir(강한 억제)는 CL을 0.94 → 0.32 L/h/kg로 떨어뜨림**. → **"강한 효소 억제가 같은 약을 고추출에서 저추출로 분류를 전환시킴"**의 사례. 분류는 약물 이름이 아니라 *상태*임.

**(4) Phenytoin + 요독증(uremia)** [R&T pp.159–160]: 요독에서 알부민 결합 ↓ → $f_u$ ↑. **Total 농도는 낮게 측정되는데 unbound는 안 변하거나 오히려 ↑**. 임상 효과(약리학적)는 unbound가 결정. → **"total과 unbound가 다른 질문에 답함"**의 사례. 요독 환자 phenytoin은 total로 판단하면 underdose됨.

**(5) Clofibric acid + 신증후군(nephrotic syndrome)** [R&T pp.161–162]: 작은 $V$에서 $f_u$ ↑ → $V$ ↑와 $CL$ ↑가 동시 → $t_{1/2}$ 단축. → **"$f_u$ 변화 하나가 $V$와 $CL$ 양쪽에 작용해 $t_{1/2}$를 흔듦"**의 사례. M1에서 다룬 "$t_{1/2}$로 시작하지 마라"의 직접 이유가 여기 있음.

### 5.3 현장 함정 한 줄

> High extraction 약물의 **IV DDI study가 음성이라고 oral DDI도 안전하다고 결론 내리면 안 됨.** Route가 바뀌면 first-pass와 $f_u\cdot CL_{int}$ 민감도가 같이 바뀜. IV negative DDI는 oral safety의 보장이 아님.

라벨링 검토 단계에서 이거 자주 놓침. 임상 DDI study가 IV로만 수행되고 oral 시판제형 라벨에 그대로 외삽되면, fentanyl-style 시나리오에서 라벨이 통째로 실패함.

### 5.4 NONMEM에서 이게 어디 들어가는가

Route 영향은 $F$ 추정과 $f_u$ covariate 위치로 나타남:

```
$INPUT ID TIME DV AMT MDV CMT ROUTE ...
$PK
  TVF = THETA(8) * (1 - HEP_EXTRACT)   ; high extraction이면 F 작음
  IF (ROUTE.EQ.1) F1 = TVF              ; oral
  IF (ROUTE.EQ.2) F1 = 1                ; IV
```

IV+oral data를 모두 가진 cohort에서 $F$ 추정 가능. 같은 약의 IV·oral 모두 fitting하면 — first-pass와 systemic clearance가 식별 가능해짐.

> **이 절의 한 줄**: 단백결합·DDI 평가 시 본능은 **route × extraction × endpoint** 3축을 동시에 좌표화하는 거임. 하나라도 빼면 IV negative → oral safety 일반화 같은 라벨 방어 실패가 일어남.

---

## §6 좌표 #4 — 모약물인가 대사체인가

<!-- SLIDE_START: §6 | title: §6 좌표 #4 대사체 — 율속단계 노출비 신부전 -->

### 6.1 대사체의 임상적 중요성

대사체가 임상적으로 중요한 이유 [R&T pp.658–659]: **활성, 독성, 효소 억제, 효소 유도, displacement**. 단, "활성 대사체가 있다"와 "임상적으로 의미가 있다"는 *같은 말이 아님*. 충분한 농도에 도달하지 않으면 우려는 작음. 그래서 active metabolite를 다룰 때 본능 한 줄은:

> **활성 대사체 = (활성 자체) × (도달 농도) × (제거 속도)** — 셋 다 봐야 함.

### 6.2 대사체 말단 기울기의 함정 — 율속단계

질량수지 [R&T pp.659–662]:

$$
\underbrace{\frac{dA(m)}{dt}}_{\text{대사체 변화}}=\underbrace{k_fA}_{\text{형성입력}}-\underbrace{k(m)A(m)}_{\text{제거출력}}
$$

대사체 농도-시간 곡선의 *말단 기울기*를 보고 "아, 이게 대사체 반감기네"라고 라벨링하는 게 가장 흔한 함정임. 

| 분류 | 조건 | 관찰 | 해석 |
|---|---|---|---|
| **Formation rate-limited** | $k \ll k(m)$ | 모약물에 *나란히* 감소 | 관찰된 metabolite terminal $t_{1/2}$은 **parent의 half-life** |
| **Elimination rate-limited** | $k(m) \ll k$ | 더 늦게 peak, 더 느리게 감소 | terminal $t_{1/2}$이 **metabolite 자신의 half-life** |

$$
\begin{aligned}\underbrace{k\ll k(m)}_{\text{형성 느림}}&\Rightarrow \underbrace{t_{1/2,\mathrm{obs}}(m)\approx t_{1/2,\mathrm{parent}}}_{\text{parent 잔향}}\\ \underbrace{k(m)\ll k}_{\text{제거 느림}}&\Rightarrow \underbrace{t_{1/2,\mathrm{obs}}(m)\approx t_{1/2,\mathrm{metabolite}}}_{\text{대사체 지배}}\end{aligned}
$$

**핵심**: 순차 연쇄에서 downstream 물질의 말단 감소는 "fastest k"가 아니라 **가장 느린 단계가 지배**함 [R&T p.661]. 대사체는 앞차(모약물)를 따라가는 차량 — 앞차가 느리면 뒤차 속도계가 아니라 교통 흐름이 느린 거임.

**임상 함정**: 모약물과 대사체가 평행 감소를 보이면 "대사체 반감기 = 모약물 반감기"로 보고하기 쉬움. **그러면 안 됨.** 정확히는 "모약물 투여 후 *관찰된* 말단 반감기"가 모약물의 반감기를 그대로 보여주는 거임. 대사체 자체 반감기는 *별도 대사체 IV 시험*으로만 확인됨.

이게 왜 위험하냐면 — 신부전 환자에서 대사체 축적 외삽이 잘못됨. Parent 잔향을 metabolite own half-life로 라벨링했는데 실제 metabolite own half-life가 훨씬 더 길면, 신부전에서 metabolite Css가 예상보다 훨씬 높이 쌓임. §6.4의 본 게임이 정확히 여기서 시작됨.

### 6.3 $AUC(m)/AUC$ 분해 — 형성분율 ≠ 노출비

자주 보는 등식 — "$AUC(m)/AUC = f_m$". **틀림.** 이건 절반만 맞는 식임.

질량수지에서 적분:

$$
\underbrace{\frac{dA(m)}{dt}}_{\text{대사체 변화}}=\underbrace{CL_f\cdot C}_{\text{형성입력}}-\underbrace{CL(m)\cdot C(m)}_{\text{제거출력}}
$$

시간 적분하면:

$$
\underbrace{\frac{AUC(m)}{AUC}}_{\text{노출비}}=\frac{\underbrace{CL_f}_{\text{형성 CL}}}{\underbrace{CL(m)}_{\text{대사체 CL}}}, \qquad \underbrace{CL_f}_{\text{형성 CL}}=\underbrace{f_m}_{\text{형성분율}}\cdot\underbrace{CL}_{\text{parent CL}}
$$

합치면:

$$
\boxed{\underbrace{\frac{AUC(m)}{AUC}}_{\text{노출비}}=\underbrace{f_m}_{\text{형성분율}}\cdot\frac{\underbrace{CL}_{\text{parent CL}}}{\underbrace{CL(m)}_{\text{대사체 CL}}}}
$$

**즉 $AUC(m)/AUC$는 $f_m$과 $CL/CL(m)$이 곱해진 합성량임.** 하나의 식에 두 미지수가 있음. AUC ratio 하나만 보고 형성 쪽 문제인지 제거 쪽 문제인지 *원리적으로 구분 불가*.

비유: 욕조 수위 = 수도꼭지 유입($f_m$) × 배수구 크기($CL(m)$)의 역수. 수위 하나로는 수도꼭지가 작은 건지 배수구가 큰 건지 못 가림.

**부등식 한 줄**: $AUC(m)/AUC < 1$이고 $f_m$ 미상이면, **$CL(m) \geq CL/f_m$이라고 추론할 수 없음**. 원전에 부합하는 부등식은 오직 $CL(m) > f_m \cdot CL$뿐임.

**Eq 20-7** (속도상수 비교) [R&T p.664]:

$$
\underbrace{\frac{k(m)}{k}}_{\text{속도비}}=\frac{\underbrace{CL(m)/CL}_{\text{청소율비}}}{\underbrace{V(m)/V}_{\text{분포비}}}
$$

여기서 $V(m)/V$ 분포비가 필요한 이유는 — 대사체와 모약물이 분포용적이 다를 수 있기 때문임. 그래서 $CL(m)/CL = k(m)/k$로 단순 환원되지 않음.

**임상 anchor**:
- **Methylprednisolone hemisuccinate (prodrug) → methylprednisolone (active)** [R&T pp.662–665]: prodrug→active의 대표 사례. AUC ratio가 형성 단계의 산물임.
- **Tolbutamide → hydroxytolbutamide**: 활성/비활성 비교, 율속단계와 상대적 청소율의 구분.
- **Propranolol → naphthoxylactic acid**: high first-pass 모약물의 대사체 사례(§6.4에서 다시 등장).

### 6.4 First-pass 대사체 + 정상상태 — Morphine/M6G의 진짜 이야기

경구 모약물 투여 후 대사체는 **두 군데**에서 생김 [R&T pp.665–669]:
- ① 흡수·초회통과 중 형성
- ② 흡수 후 전신에서 형성

이 둘이 한 모델에서 동시에 작동하는 게 임상 default임. 그런데 **oral 단독 데이터만으로는 두 경로를 따로 추정 불가** — IV·oral 비교 design이 필수.

**Propranolol** (고추출 β차단제, 경구 20 mg) [R&T p.666]: naphthoxylactic acid 대사체가 propranolol과 *거의 같은 시간*에 최고 농도. 초회통과 대사체 유입 패턴. → **high first-pass면 대사체 입력에서 초회통과 비중이 큼**의 사례.

**Morphine / M6G** [R&T pp.667–668]: 경구 11.7 mg vs 정맥 5 mg morphine. Morphine 경구 F는 낮음. 근데 *초회통과에서 M6G(활성)가 형성*되니까 — **M6G 노출량은 두 경로에서 비슷할 수 있음.** → **모약물 F가 낮아도 활성 대사체 노출은 보존됨**의 사례. 이게 morphine 경구 진통 효과의 진짜 메커니즘 일부임.

**Isoproterenol** [R&T p.669]: 투여 경로에 따라 장벽 대사 vs 간외 대사 작동 위치가 바뀜 → 소변 회수율 달라짐. → **route가 first-pass 위치 자체를 옮김**의 사례.

**정상상태 대사체** [R&T pp.669–673]:

$$
\underbrace{C(m)_{ss}}_{\text{대사체 Css}}=\frac{\underbrace{f_m}_{\text{형성분율}}\cdot\underbrace{R_{inf}}_{\text{입력속도}}}{\underbrace{CL(m)}_{\text{대사체 CL}}}
$$

다회 투여 시 중첩 원리:

$$
\underbrace{C(m)_{av,ss}}_{\text{평균 Css}}=\frac{\underbrace{AUC(m)_{single}}_{\text{단회 노출}}}{\underbrace{\tau}_{\text{투여간격}}}
$$

**정상상태 도달 시간은 율속 패턴에 따라 모약물 또는 대사체 소실 중 *더 느린 쪽***이 결정함. **N-desalkylhalazepam**(diazepam계 활성 대사체)에서 대사체 축적이 모약물보다 느림. **Carbamazepine autoinduction**(§4.7)은 추가로 시간 변동까지 들어가서 정상상태가 *움직임*.

### 6.5 종착역 — 신부전 + 활성 대사체 (Q9 풀이)

자, 이제 이 챕터의 본 게임에 도달함. 4-좌표가 한 환자에서 동시에 충돌하는 시나리오.

**원전 시나리오** [R&T pp.673–675; Fig 20-10; Table 20-4]:

| 파라미터 | Parent | Active metabolite |
|---|---:|---:|
| 전체 CL | 30 L/h | 10 L/h |
| 신장 CL | 15 L/h | 8.5 L/h |
| Parent 경구 F / $f_m$ | $F=0.8$ | $f_m=0.3$ |

경구 10 mg/h 투여 시 정상 신기능에서:
- Parent Css = **0.27 mg/L**
- Metabolite Css = **0.24 mg/L**
- 총 활성 농도 = **0.51 mg/L**

자, 환자가 **무뇨(anuria)**가 됨. parent renal CL과 metabolite renal CL이 모두 0. 손이 자동으로 어디로 가야 하나? **단순히 "parent CL이 반으로 줄었으니 dose도 반으로"로 가면 라벨 실패**임. 이유를 단계별로 풀어보자.

**Step 1. 정상상태 청소율 분해**:
- Parent total CL = 30 L/h = (CL_R = 15) + (CL_nonrenal = 15)
- Parent의 nonrenal CL 15 L/h 중 metabolic formation CL = $f_m \cdot CL = 0.3 \times 30 = 9$ L/h
- 따라서 nonrenal nonmetabolic CL = 15 − 9 = **6 L/h**
- Metabolite total CL = 10 L/h = (CL_R(m) = 8.5) + (CL_nonrenal(m) = 1.5)

**Step 2. 무뇨 상태에서 청소율 재구성**:

$$
\underbrace{CL_{\text{parent, anuria}}}_{\text{무뇨 시 parent}}=\underbrace{0}_{\text{신장 차단}}+\underbrace{9}_{\text{대사 유지}}+\underbrace{6}_{\text{기타 nonrenal 유지}}=15\ \text{L/h}
$$

$$
\underbrace{CL(m)_{\text{anuria}}}_{\text{무뇨 시 metabolite}}=\underbrace{0}_{\text{신장 차단}}+\underbrace{1.5}_{\text{nonrenal 유지}}=1.5\ \text{L/h}
$$

→ Parent CL은 30 → 15, **약 2배** 증가.

**Step 3. $f_m$이 자동으로 증가함** — 이게 13배 폭증의 진짜 출발점:

$$
\overbrace{\underbrace{f_{m,\text{normal}}}_{=0.3}\xrightarrow{\text{무뇨 시}}\underbrace{f_{m,\text{anuria}}}_{=?}}^{\text{핵심 산출 단계}}=\frac{\overbrace{CL_{\text{metabolic}}}^{=9\ \text{L/h, 유지}}}{\underbrace{CL_{\text{parent, anuria}}}_{=15\ \text{L/h}}}=\boxed{0.6}
$$

즉, **무뇨에서 $f_m$이 0.3 → 0.6으로 두 배 증가**함. 왜? metabolic formation CL의 *절대값*은 유지되는데(효소는 정상), 신장 경로가 닫히면서 *전체 parent CL 중 차지하는 비율*이 올라가기 때문. 이게 핵심임.

**Step 4. 대사체 노출 비율** ($AUC(m) \propto F \cdot f_m / CL(m)$):

$$
\overbrace{\frac{AUC(m)_{\text{anuria}}}{AUC(m)_{\text{normal}}}}^{\text{대사체 노출 변화}}=\frac{\underbrace{f_{m,\text{anuria}}/CL(m)_{\text{anuria}}}_{0.6/1.5\,=\,0.4}}{\underbrace{f_{m,\text{normal}}/CL(m)_{\text{normal}}}_{0.3/10\,=\,0.03}}=\boxed{\approx 13.3\text{배}}
$$

**모약물 약 2배, 대사체 약 13배**. 모약물만 보고 50% 감량하면 대사체는 여전히 약 6–7배 과노출.

**Step 5. 통합 용량비**: 정상 총 활성 농도(0.51 mg/L)를 유지하려면 용량을 **정상의 약 0.14배**로 낮춰야 함. Parent-only 50% 감량으로는 도달 불가.

**핵심 교훈**: "소수 대사 경로($f_m$ 작음)"는 "소수 안전성 우려"가 아님. **신장이 닫히는 순간 $f_m$이 자동 상승**하고, 대사체 신장 의존도가 높으면 $CL(m)$이 무너지면서 두 요인이 곱해져 대사체 노출이 *자릿수*로 폭증함. 두 효과가 곱해져 13배를 만드는 거임 — $f_m$ 2배 × $CL(m)$ 약 6.7배 = **약 13.3배**.

**라벨 방어 두 가지 입장** (둘 다 방어 가능, 셋째는 방어 불가):

- **(a) 통합 노출 기반 용량 조정**: 통합 활성을 정상 수준에 맞추는 용량비(~0.14) 적용. *보수적*, underdose 위험. 라벨 문구: "based on combined active exposure"
- **(b) 2단계 모니터링**: 모약물 용량은 모약물 CL에만 맞추고, 활성 대사체 TDM으로 안전 안내선 운영. *정밀하지만 분석법·turnaround 필요*
- **(불가) Parent $f_e$ 비례 일률 감량 단독**: §6.4 Step 4에서 시나리오 (3) 가능성을 닫지 못함 — 시판 라벨링에서 *방어 불가*

**Interconversion 추가 함정** [R&T pp.676–679]: 모약물과 대사체가 서로 재생성 가능한 경우. 대사체 쪽 신장애가 모약물의 *겉보기* 소실까지 늦출 수 있음. **Clofibric acid**가 대표 anchor. Parent profile만 보고 "renal-safe"로 분류하면 메커니즘을 놓침.

### 6.6 NONMEM에서 이게 어디 들어가는가

Parent+metabolite joint model의 구조:

```
$MODEL
  COMP=(PARENT)    ; 모약물
  COMP=(METAB)     ; 대사체
$PK
  CL    = THETA(1) * (CRCL/100)**THETA(11)   ; parent renal+nonrenal 분해됨
  CLm   = THETA(2) * (CRCL/100)**THETA(12)   ; metabolite는 별도 신기능 covariate
  FM    = THETA(3)                            ; 형성분율 (시간 의존 가능)
  V     = THETA(4)
  Vm    = THETA(5)
  K     = CL/V
  Km    = CLm/Vm
$DES
  DADT(1) = -K*A(1)
  DADT(2) = FM*K*A(1) - Km*A(2)
```

**식별가능성 (identifiability) 점검**:
- Oral 단독 data만으로는 $F$와 $f_m$이 product confounding됨 → IV 또는 separate metabolite IV data 필요
- $V(m)$ 추정 어려움 → 문헌값 fixing이 일반적
- $f_m$이 시간 의존이면(autoinduction 등) — $f_m(t)$로 모델링

**Q9 시나리오 라벨 검토 본능**:
1. Active metabolite ESRD PK 데이터가 dossier에 있는가? 없으면 시나리오 (3) 가능성이 닫히지 않음 → label defense 실패
2. Combined exposure ratio 계산이 라벨 권고에 반영됐는가?

> **이 절의 한 줄**: 신부전 + 활성 대사체에서 본능은 **parent + metabolite combined exposure**를 계산하고, **$f_m$이 자동 상승함**을 항상 기억하는 거임. Minor pathway를 minor concern으로 분류하면 작은 $f_m$의 위험이 통째로 가려짐.

---

## §7 구현 다리 — PK5 동시 적합

<!-- SLIDE_START: §7 | title: §7 구현 다리 PK5 plasma+urine 동시 적합 -->

§2~§6이 *생리학적 좌표*를 깔았다면, 이 절은 그걸 *데이터에 어떻게 fitting*하는지를 한 사례로 보여줌. 이게 NONMEM에서 다중 endpoint를 한 모델에 fitting하는 사고방식의 모범 사례임.

### 7.1 PK5 시나리오

**250 mg IV bolus** [G&W p.494]. 데이터는 plasma 농도-시간 곡선 + 누적 소변량. 초기 추정 $V \approx 7$ L, $CL \approx 2$ L/h, $f_e \approx 0.3$.

모델 골격 [G&W pp.497–499]:

$$
\underbrace{C(t)}_{\text{혈장농도}}=\frac{\underbrace{D_{iv}}_{\text{IV 용량}}}{\underbrace{V}_{\text{분포용적}}}\exp\left(-\underbrace{\frac{CL}{V}}_{\text{소실상수 }k}\underbrace{t}_{\text{시간}}\right)
$$

$$
\underbrace{X_u(t)}_{\text{누적 소변량}}=\underbrace{f_e}_{\text{신장 지분}}\cdot\underbrace{D_{iv}}_{\text{IV 용량}}\left[1-\exp\left(-\underbrace{\frac{CL}{V}}_{\text{소실상수}}\underbrace{t}_{\text{시간}}\right)\right]
$$

**최종 추정**: $CL \approx 1.2$ L/h, $f_e \approx 35\%$, $CL_R \approx 0.42$ L/h. Parameter CV < 5%. 잔차 CV는 **plasma 2.84%, urine 8.96%** [G&W pp.497–498].

### 7.2 왜 한 모델에서 동시에 적합해야 하나

**소변 데이터를 별도 계산표로 처리하면 그 순간 $f_e$와 $CL_R$를 plasma model 안에서 따로 추정할 수 없게 됨.** 두 endpoint를 같이 적합해야 — endpoint별 오차 구조와 renal fraction이 *한 모델 안에서* 추정 가능.

**Endpoint별 잔차오차 분리가 핵심**:
- Plasma: 일반적으로 CV ~2–5%, 측정법 정밀
- Urine: 일반적으로 CV ~5–15%, collection completeness·bladder emptying·sample homogeneity 영향

이 차이를 무시하고 단일 잔차오차로 fitting하면 — plasma fit이 urine 잔차에 끌려가서 plasma parameter 추정이 흔들림.

### 7.3 NONMEM 구현 — 이게 진짜 자리

```
$INPUT ID TIME DV AMT MDV DVID CMT
$DATA pk5_data.csv
$SUBROUTINES ADVAN1 TRANS2

$PK
  TVCL = THETA(1)
  TVV  = THETA(2)
  TVFE = THETA(3)
  CL = TVCL * EXP(ETA(1))
  V  = TVV  * EXP(ETA(2))
  FE = TVFE
  S1 = V               ; plasma 농도용
  S2 = 1               ; urine 누적량용

$DES
  DADT(1) = -K*A(1)
  DADT(2) = FE*K*A(1)  ; 누적 소변량

$ERROR
  IPRED = A(1)/V
  IF (DVID.EQ.1) Y = IPRED*(1+EPS(1))      ; plasma, CV ~2.84%
  IF (DVID.EQ.2) Y = A(2)*(1+EPS(2))       ; urine, CV ~8.96%
```

이게 §3.9에서 미리 깐 구조의 실제 control stream임. **DVID로 endpoint 구분, EPS 분리, 같은 ETA로 plasma와 urine을 연결** — 이 패턴이 plasma+urine, IV+oral, parent+metabolite 같은 모든 다중 endpoint 문제의 출발점임.

> **이 절의 한 줄**: 다중 endpoint를 만나면 본능은 **한 모델 + DVID 분리 + 잔차오차 블록 분리**임. 이걸 안 하면 endpoint 간 정보 공유가 끊겨서 식별가능성이 무너짐.

---

## §8 종간/체구 정규화 — Allometric Scaling

<!-- SLIDE_START: §8 | title: §8 종간 정규화 Allometric scaling -->

여기까지 *한 환자 내 생리학*을 다뤘다면, 이 절은 *환자 간(또는 종간) 정규화*를 정함. NONMEM에서 체중·연령·BSA covariate를 PopPK에 도입하는 첫 단계임.

### 8.1 표준 거듭제곱 법칙

[G&W p.87, Table 2.7]:

$$
\overbrace{CL=CL_{70}\cdot\left(\frac{BW}{70\ \text{kg}}\right)^{0.75}}^{\text{청소율: 3/4 power}}\,,\qquad \overbrace{V=V_{70}\cdot\left(\frac{BW}{70\ \text{kg}}\right)^{1.0}}^{\text{분포용적: 선형}}\,,\qquad \overbrace{Q=Q_{70}\cdot\left(\frac{BW}{70\ \text{kg}}\right)^{0.75}}^{\text{intercompartmental CL}}
$$

| 파라미터 | 지수 | 근거 |
|---|---:|---|
| $CL$ (총) | **0.75** | Kleiber's law, 간 효소·신장 GFR의 체구 의존성 |
| $Q$ (구획간) | **0.75** | 혈류 비례 |
| $V$ | **1.0** | 체액 부피와 거의 정비례 |
| $K_a$ | **−0.25** or 0 | 시간 척도 — 큰 동물은 흡수 느림 |

→ **$t_{1/2} \propto BW^{1.0-0.75} = BW^{0.25}$** — 큰 동물일수록 반감기 *느리게* 증가. 종간 비교 핵심.

### 8.2 종간 비교 표

[G&W p.87, Table 2.7]:

| Species | BW (kg) | Liver wt (g) | Liver flow (mL/min) |
|---|---:|---:|---:|
| Human | 70 | 1500 | 1450 |
| Dog | 10 | 320 | 309 |
| Rabbit | 2.5 | 77 | 177 |
| Rat | 0.25 | 10 | 13.8 |
| Mouse | 0.020 | 1.75 | 1.8 |

→ rat → mouse에서 BW 12배 감소 시 liver flow는 7.7배만 감소. **단순 mg/kg 변환이 interspecies CL 예측에서 실패하는 정량 anchor.**

### 8.3 소아·신생아 — Maturation Function

순수 allometric만으론 효소 미성숙·신장 발달 못 잡음. 그래서 PopPK에서는:

$$
\overbrace{CL_{\text{pediatric}}=CL_{70}\cdot\underbrace{\left(\frac{BW}{70}\right)^{0.75}}_{\text{Size}}\cdot\underbrace{\frac{PMA^{H}}{TM_{50}^{H}+PMA^{H}}}_{\text{Maturation (Hill 함수)}}}^{\text{Anderson \& Holford framework}}
$$

| 변수 | 의미 |
|---|---|
| $PMA$ | Postmenstrual age (수태후 주) |
| $TM_{50}$ | 성인 활성 50% 도달 PMA — UGT2B7 ~36주, CYP3A4 ~45주 |
| $H$ | Hill coefficient |

→ §4.3의 **chloramphenicol gray baby (UGT 미성숙)**가 정확히 이 framework에 끼워 들어감.

### 8.4 비만 환자 — ABW vs IBW vs LBW

| 약물 특성 | 적용 체중 | 예시 |
|---|---|---|
| 친수성 (분포 제한) | IBW or LBW | aminoglycosides; vancomycin (load=ABW, maint=IBW) |
| 지용성 (조직 분포 큼) | ABW | 일부 마취제 |
| 중간 | dosing weight = $LBW + 0.4 \times (ABW - LBW)$ | 다수 가이드라인 |

**Aminoglycosides 함정**: lean tissue 분포라서 LBW 기반이 더 정확. ABW로 dose 계산 시 신독성 위험 ↑. 이거 임상에서 정말 자주 놓침.

### 8.5 NONMEM 구현

```
TVCL = THETA(1) * (WT/70)**0.75 * (PMA**HILL / (TM50**HILL + PMA**HILL))
TVV  = THETA(2) * (WT/70)
TVQ  = THETA(3) * (WT/70)**0.75
TVV2 = THETA(4) * (WT/70)
```

**결정 사항**:
- Exponent fix vs estimate — sparse data면 0.75/1.0 fix 안정적
- Centering BW — 보통 70 kg 또는 데이터 median
- Maturation $TM_{50}$과 $H$ — 같이 추정 어려운 경우 많아 prior 문헌값 fixing 일반적
- TMDD 약물 — target-mediated 항은 receptor abundance 반영하니까 BW^0.75에 안 따름

> **이 절의 한 줄**: PopPK covariate 모델의 첫 단추는 **$CL \propto BW^{0.75}$ + $V \propto BW^{1.0}$ + maturation function**임. 없이 mg/kg ad-hoc로 가면 소아 dose·FIH·interspecies 외삽이 통째로 흔들림.

---

## §9 혼동 쌍 10개 — 절대 같이 두지 말 것

<!-- SLIDE_START: §9 | title: §9 혼동 쌍 10개 -->

M1~M14·§3~§8을 다 통과했어도, 임상 보고서 한 장에서 흔들리게 만드는 건 *비슷해 보이는 두 숫자*임. 이 섹션은 그 쌍들을 4축(차원/위치/원인/결과)으로 잘라서 다시는 같은 자리에 두지 않도록 만듦.

### 쌍 1. $CL$ vs $CL_R$ / $f_e$

| 비교 기준 | $CL$ | $CL_R$ / $f_e$ |
|---|---|---|
| 단위 | L/h, 전체 전신 청소율 | $CL_R$: L/h; $f_e$: fraction |
| 식 위치 | $CL = CL_R + CL_H + CL_{other}$ | $f_e = CL_R/CL$; $CL_R = f_e \cdot CL$ |
| 변화 원인 | renal + nonrenal pathway 전체 | 신기능, urine route |
| 혼동 결과 | total CL에 renal covariate 무차별 적용 | nonrenal까지 줄어 systematic underestimation |

> **⚡ 한 줄**: $f_e$는 신장 *지분*임. 곱셈 분해이지 비례 단축이 아님. 신부전 covariate는 $CL_R$ 위치에만 곱함.

### 쌍 2. ARE plot vs Excretion-rate plot

| 비교 기준 | ARE plot | Rate plot |
|---|---|---|
| 단위 | 잔여 누적량 로그 | 구간 배설속도 로그 |
| 식 위치 | $\ln(X_{u,0-\infty}-X_u)$ | $\ln(dX_u/dt)$ |
| 변화 원인 | $X_{u,0-\infty}$ 추정, 누적 편향 | collection interval, pH/flow, bladder |
| 혼동 결과 | 평활된 누적량을 변동 없음으로 오인 | sampling artifact를 구조 모델로 오인 |

> **⚡ 한 줄**: Rate plot은 시간 정보 노출, ARE는 누적량으로 변동 평탄화. Slope 불일치 → 구조 모델 점프 전에 sampling design부터.

### 쌍 3. Plasma $CL$ vs Blood $CL_b$

| 비교 기준 | Plasma $CL$ | Blood $CL_b$ |
|---|---|---|
| 단위 | plasma 기준 L/h | blood 기준 L/h |
| 식 위치 | $CL = Dose/AUC_{plasma}$ | $CL_b = CL \cdot C/C_b$ |
| 변화 원인 | plasma binding, measurement | hematocrit, RBC partition |
| 혼동 결과 | $CL/Q_H$로 false-high extraction | DDI 해석 실패 |

> **⚡ 한 줄**: $E_H = CL_b/Q_H$임. $CL/Q_H$ 아님. App.D bridge 없이 organ extraction을 말하지 마라. **프롤로그 60 L/h가 이 함정의 사례.**

### 쌍 4. $f_u$ vs $f_{ub}$

| 비교 기준 | $f_u$ | $f_{ub}$ |
|---|---|---|
| 단위 | plasma 내 unbound 분율 | blood 내 unbound 분율 |
| 식 위치 | plasma binding 식 | well-stirred의 $f_{ub}\cdot CL_{int}$ |
| 변화 원인 | albumin/AAG, displacement | $f_u$ + $C/C_b$ 변환 |
| 혼동 결과 | plasma 분율을 blood 식에 직접 대입 | hepatic extraction과 PBPK 입력 단위 오류 |

> **⚡ 한 줄**: $f_{ub} = f_u \cdot R$. 분모가 다른 두 측정량이지 별명이 아님. **매트릭스 anchor**: tacrolimus·cyclosporine = whole blood; warfarin·phenytoin = plasma; digoxin = serum.

### 쌍 5. High extraction IV vs High extraction oral

| 비교 기준 | IV | Oral |
|---|---|---|
| 단위 | systemic $CL \approx Q_H$ | first-pass F/AUC |
| 식 위치 | 혈류 제한 항 | $F$, first-pass, $f_{ub}CL_{int}$ 민감 |
| 변화 원인 | hepatic blood flow | enzyme induction/inhibition, first-pass formation |
| 혼동 결과 | IV negative DDI를 oral safety로 오판 | route-dependent DDI 누락 |

> **⚡ 한 줄**: IV에서는 $Q_H$ 상한이 enzyme 변화를 가림. Oral에서는 first-pass가 그 상한을 풂. IV negative ≠ oral safety.

### 쌍 6. Well-stirred vs Extended/permeability-limited

| 비교 기준 | Well-stirred | Extended |
|---|---|---|
| 단위 | rapid equilibration 가정 | membrane/transporter 병목 포함 |
| 식 위치 | $f_{ub}CL_{int}$ | $f_{ub}\rho CL_{int}$ 또는 uptake/efflux 분해 |
| 변화 원인 | blood flow, binding, enzyme | uptake permeability, transporter |
| 혼동 결과 | 낮은 $CL_{int}$처럼 오인 | transporter covariate 누락 |

> **⚡ 한 줄**: $\rho < 1$이면 *효소가 아니라 막*이 병목. Statin/OATP1B1 기질에서 $f_u$ covariate가 비유의로 떨어지면 의심.

### 쌍 7. 단일점 $CL_{int}$ vs Michaelis–Menten 정보

| 비교 기준 | 단일점 | MM 정보 |
|---|---|---|
| 단위 | 한 농도 rate의 압축값 | 농도-속도 곡선 |
| 식 위치 | $CL_{int}$ 하나 입력 | $V_{max}$, $K_m$, free conc |
| 변화 원인 | 측정 농도 선택, scaling | saturation, enzyme capacity |
| 혼동 결과 | 곡선 정보 소실 후 정교 모델 적용 | IVIVE 예측 실패 |

> **⚡ 한 줄**: 한 농도 rate를 $V_{max}/K_m$로 쓰는 건 곡선을 버리고 분수식을 정교화하는 것임. 정보 손실은 어떤 hepatic model로도 복구 안 됨.

### 쌍 8. Formation-rate-limited vs Elimination-rate-limited

| 비교 기준 | Formation-limited | Elimination-limited |
|---|---|---|
| 단위 | parent가 metabolite slope 지배 | metabolite own elimination 지배 |
| 식 위치 | $k \ll k(m)$ | $k(m) \ll k$ |
| 변화 원인 | 느린 parent disappearance | 느린 metabolite clearance |
| 혼동 결과 | parent 잔향을 metabolite half-life로 라벨 | 신부전 축적·다회 투여 예측 실패 |

> **⚡ 한 줄**: 평행 감소 = 모약물의 잔향. 보고된 metabolite terminal $t_{1/2}$이 *그 metabolite의 것이 아닐 수 있음*. Separate IV 또는 model-based formation rate fixing 필요.

**▶ 치명적 타격**: NDA에서 sponsor가 active metabolite IV 단독 시험 없이 "metabolite 반감기는 X시간"을 명시하면, 이는 system-level slope에 metabolite 라벨을 붙인 거임. → (a) 신부전 축적 외삽 빗나감 (b) 다회 투여 축적 예측 빗나감 (c) dose-response timing 평가 동시 빗나감.

### 쌍 9. $AUC(m)/AUC$ vs $f_m$

| 비교 기준 | $AUC(m)/AUC$ | $f_m$ |
|---|---|---|
| 단위 | 노출비 | 형성분율 |
| 식 위치 | $f_m \cdot CL/CL(m)$ | 형성항 단독 |
| 변화 원인 | formation + metabolite clearance | metabolic pathway share |
| 혼동 결과 | 낮은 ratio를 낮은 formation으로 단정 | $CL(m)$ 변화·신장애 위험 누락 |

> **⚡ 한 줄**: $AUC(m)/AUC < 1$은 **한 식에 두 미지수**. $f_m$ 모르면 $CL(m)/CL$ 부등식 쓰지 마라. 원전 부합 부등식은 $CL(m) > f_m \cdot CL$뿐.

### 쌍 10. Sequential metabolism vs Interconversion

| 비교 기준 | Sequential | Interconversion |
|---|---|---|
| 단위 | 한 방향 흐름 | 양방향 parent↔metabolite |
| 식 위치 | downstream chain | reversible transfer |
| 변화 원인 | 대사 경로 순차 | 재생성·재전환 |
| 혼동 결과 | parent profile만으로 renal-safe 오판 | metabolite 신부전이 parent apparent elimination까지 지연 |

> **⚡ 한 줄**: Sequential = 한 방향, interconversion = 양방향. 후자에선 parent $f_e$가 작아도 metabolite 신부전이 parent 겉보기 소실을 늦춤. Clofibric acid가 anchor.

---

## §10 자기 검증 — 소크라테스식 9문제

<!-- SLIDE_START: §10 | title: §10 자기 검증 -->

### Q1. 청소율 정의

$CL = Dose/AUC$가 compartment model 없이도 성립하는 이유는?
**답**: 총 제거량 = dose이고 $\int Rate\,dt = CL \cdot \int C\,dt$이므로 $CL = Dose/AUC$가 모델 독립적으로 성립함.

### Q2. 신장 분해

정상 $CL = 10\ \mathrm{L/h}$, $f_e = 0.6$인 약물. 신기능 25%로 감소, nonrenal 보존. 새 total CL은?
**답**: renal 6 → 1.5, nonrenal 4 유지, total = **5.5 L/h**.

### Q3. 소변 plot

Rate plot과 ARE plot의 slope가 달라요. 무엇부터 의심?
**답**: 수집 간격, 방광 배출, pH/flow 변동, $X_{u,\infty}$ 편향. 이 순서로. 구조 모델은 마지막.

### Q4. Well-stirred 극한

$Q_H = 81\ \mathrm{L/h}$, $f_{ub}\cdot CL_{int} = 20\ \mathrm{L/h}$. High/low/intermediate? $f_{ub}$가 4배 증가하면?
**답**: 초기 $E = 20/(81+20) = 0.20$, 낮은 편. 4배 → $f_{ub}\cdot CL_{int} = 80$, $E \approx 0.50$, intermediate.

### Q5. Plasma CL vs Blood CL

Plasma $CL = 60\ \mathrm{L/h}$, $C/C_b = 0.5$, $Q_H = 81\ \mathrm{L/h}$. $CL_b$와 $E_H$는?
**답**: $CL_b = 30\ \mathrm{L/h}$, $E_H = 0.37$. **Plasma 기준으로 가면 실제보다 높은 추출률로 분류됨.** (이게 프롤로그 미스터리)

### Q6. IVIVE 함정

한 농도에서 얻은 in vitro rate, MMP 평균값 scaling. Phase 1에서 in vivo CL이 예측의 1/5. 어느 세 가지를 우선 점검?
**답**: ① 단일 농도 비선형성, ② $f_u$/free conc 오류, ③ MMP/scaling 변이, ④ transporter/permeability 항 누락.

### Q7. 대사체 율속단계

Parent 투여 후 모약물과 대사체가 평행 말단 감소. Separate metabolite IV에서는 반감기가 더 짧음. 무엇?
**답**: **Formation rate-limited**. Parent 투여 후 관찰되는 metabolite slope는 parent가 지배.

### Q8. AUC 비

$AUC(m)/AUC = 0.5$. $f_m = 0.5$라고 말할 수 있나?
**답**: **불가능.** $CL(m)/CL$이 필요함. 식은 $AUC(m)/AUC = f_m \cdot CL/CL(m)$.

### Q9. Boss 딜레마 — 신부전 + 활성 대사체

(§6.5 참조) Parent: $CL = 30$, $CL_R = 15$, $F = 0.8$. Metabolite: $CL(m) = 10$, $CL_R(m) = 8.5$, $f_m = 0.3$. 무뇨에서 모약물만 50% 감량이 왜 불안전한가?

**답** (5단계):
1. 정상: parent CL 분해 → renal 15 + metabolic 9 + 기타 nonrenal 6 = 30
2. 무뇨: parent CL = 0 + 9 + 6 = 15 (약 2배)
3. **$f_m$ 자동 상승**: $9/15 = 0.6$ (0.3에서 두 배)
4. Metabolite Css 비: $\frac{0.6/1.5}{0.3/10} \approx 13.3$배
5. 통합 활성 유지 용량비 ≈ **0.14** — 50% 감량으로 도달 불가

**핵심**: $f_m$이 무뇨에서 자동 상승하고, $CL(m)$이 무너지면서 두 효과가 곱해져 13배. Minor pathway가 minor concern이 아닌 이유임.

---

## §11 한 페이지 요약 + 실패 모드 카탈로그

<!-- SLIDE_START: §11 | title: §11 한 페이지 요약 -->

### 11.1 요약 11줄

1. $CL$은 농도로 정규화한 제거능임 — 제거 속도 자체 아님 [G&W p.49; R&T pp.124–128]
2. $t_{1/2}$는 $V/CL$의 결과값임. $CL$과 $V$를 먼저 분해하지 않고 해석 ❌ [R&T pp.148–150]
3. $CL_R = f_e \cdot CL$, 그러나 실제 신청소율 = 여과 + 분비 − 재흡수이고 urine pH/flow가 흔듦 [G&W pp.48–56; R&T pp.138–148]
4. Well-stirred는 $Q_H$, $f_{ub}$, $CL_{int}$. High/low extraction은 극한 근사지 영구 라벨 아님 [G&W pp.79–85; R&T pp.130–135]
5. Organ extraction은 blood 기준. Plasma → blood 변환(App.D)이 hepatic 분류의 전제 [R&T App.D pp.775–776]
6. IVIVE는 in vitro 입력 정보 손실 시 실패 — single-point, MMP, permeability 누락 [G&W pp.85–90; R&T App.E]
7. Parent–metabolite는 $f_m$, $CL(m)$, 율속단계 별도 추정. $AUC(m)/AUC$는 $f_m$ 아님 [R&T pp.659–665]
8. 신부전 dose는 parent $f_e$만이 아니라 active metabolite CL 별도 평가 [R&T pp.673–679]
9. 측정 매트릭스(plasma/serum/whole blood)와 $f_u \to f_{ub}$ 변환은 well-stirred·PBPK 입력 직전 필수 [R&T App.D]
10. Extended Clearance(Sirianni-Pang)는 OATP 기질에서 well-stirred IVIVE underprediction을 uptake/met/efflux로 분해 [R&T pp.136–138; App.E]
11. DDI는 inhibition만이 아니라 induction(rifampin, carbamazepine, St. John's Wort)도 양 축 — 치료 실패 위험 [R&T pp.121–123, Ch.17]

### 11.2 실패 모드 카탈로그 — 6패턴

| ID | 패턴 | 신호 | 원인 | Anchor |
|---|---|---|---|---|
| **DS-1** | Phantom Plasma Clearance | 추정 $CL$이 $Q_H$(81 L/h) 초과 — 생리학적 불가능 | Plasma $CL$을 organ flow와 직접 비교한 단위 mismatch | §2 |
| **DS-2** | Phantom Metabolite Half-life | metabolite $k$가 parent $k$와 거의 동일 | Formation rate-limited에서 parent 잔향을 metabolite own slope로 오해 | §6.2 |
| **DS-3** | Renal Covariate Asymmetry | metabolite CrCl power ≈ 1.0인데 parent power 작음 | 활성 대사체가 거의 신배설 ($f_e(m) \approx 1$), parent $f_e$는 작음 — Tozer Scenario (3) 직접 신호 | §6.5 |
| **DS-4** | Permeability Rate-Limited Mismatch | $f_u$ covariate 모든 cohort에서 비유의/계수 ≈ 0, IVIVE만 5–10배 underestimate | 수송체 기질에서 $\rho < 1$ — well-stirred rapid equilibration 가정 붕괴 | §4.5, §4.6 |
| **DS-5** | Induction Time-Course Misfit | rifampin·carbamazepine cohort에서 $CL$이 시간에 따라 점진 증가, terminal slope 가팔라짐 | Self-induction 또는 외인성 induction의 1–2주 timescale, binary covariate로는 누락 | §4.7 |
| **DS-6** | Matrix Mismatch | tacrolimus·cyclosporine cohort에서 추정 $V$ 비정상적으로 작거나 hematocrit이 거대 잔차로 흡수 | TDM whole blood 결과를 plasma로 잘못 해석 | §2.5 |

### 11.3 한 줄 본능 모음

| 상황 | 본능 |
|---|---|
| $t_{1/2}$ 변화 보고서 | 먼저 $CL$과 $V$ 분리 |
| Hepatic extraction 판단 | $CL_b = CL \cdot R$ 변환부터 |
| Well-stirred 입력 | $f_{ub} = f_u \cdot R$ 변환 필수 |
| TDM 결과 받음 | 매트릭스(plasma/serum/whole blood) 확인 → $R$ → $f_{ub}$ 3단 |
| 신부전 covariate | $CL$ 전체가 아니라 $CL_R$ 위치에만 |
| 소변 데이터 받음 | Plasma+urine 한 모델에 동시 적합, DVID로 endpoint 분리, 잔차 블록 분리 |
| Urine plot slope 불일치 | Sampling artifact부터 (collection/bladder/pH-flow), 구조 모델은 마지막 |
| 간 CL 보면 | $Q_H$ vs $f_{ub}\cdot CL_{int}$ 비교, $CL_{int}$ = 효소·다형성·염증 합성 |
| IVIVE 빗나감 | Hepatic model보다 입력 정보 손실(single point, MMP, permeability) 먼저 |
| $f_u$ covariate 비유의 + IVIVE underpredict | $\rho$ 또는 SLCO1B1 같은 transporter genotype 검토 |
| DDI 검토 | Inhibition + induction 양 축, 효소 + 수송체 양 축 |
| 단백결합 변화 | Route × extraction × total/unbound endpoint 3축 |
| Metabolite 평행 감소 | Formation rate-limited 가능성 (parent 잔향) |
| $AUC(m)/AUC$ 받음 | $f_m$과 $CL(m)$ 분해 — 둘 다 모르면 부등식만 |
| 신부전 + active metabolite | Parent + metabolite combined exposure, $f_m$ 자동 상승 기억 |
| 소아 PopPK | Allometric BW^0.75 + maturation function |
| 비만 환자 dose | 약물 친수성/지용성에 따라 ABW/IBW/LBW 선택 |

---

## §12 닫는 말 — 4-좌표를 한 바느질로

이 챕터가 한 일을 다시 정리하면 — **임상 보고서 한 장에서 청소율 숫자 하나를 봤을 때, 손이 자동으로 4-좌표 점검 순서를 밟는 본능**을 만드는 거였음. 

```
청소율 숫자를 봤다
   ↓
좌표 #1 (매트릭스): plasma인가 blood인가 unbound인가?  → §2
   ↓
좌표 #2 (장기): 신장? 간? 분해 식 어디에 들어가야 하나?  → §3, §4
   ↓
좌표 #3 (경로): IV? Oral? Route × Extraction × Endpoint 3축이 정합한가?  → §5
   ↓
좌표 #4 (분석 대상): 모약물? 대사체? 율속단계는? AUC ratio 분해됐나? 신부전에서 $f_m$ 자동 상승은 봤나?  → §6
   ↓
구현: 한 모델 + DVID + 잔차오차 블록 분리 + 체구 정규화  → §7, §8
   ↓
점검: 혼동 쌍 10개에 걸려있지 않은가?  → §9
```

프롤로그의 60 L/h를 다시 보자. 처음에는 그냥 큰 숫자 하나였음. §2를 통과하면 그게 *plasma 기준*이라는 걸 알게 됨. $R = 0.5$ 변환을 거치면 30 L/h. $Q_H = 81$과 비교하면 $E_H = 0.37$. Low-to-intermediate. 이제 DDI 평가에서는 enzyme inhibitor 영향이 더 중요할 거라고 짐작할 수 있음. 간장애에서는 enzyme capacity가 더 중요할 거라고. 

그리고 만약 이 약물이 active metabolite를 가지고, 그 metabolite가 신장으로 빠진다면 — §6.5의 13배 폭증 시나리오가 자동으로 머릿속에 떠야 함. 그게 본능이 자리잡은 상태임.

**한 바느질로 꿰어진다는 게 그런 거임.** 좌표 #1을 풀면 #2가 풀리고, #2가 풀리면 #3이 풀리고, #3이 풀리면 #4가 풀림. 거꾸로 가면 매번 같은 자리에서 무너짐.

> "어떤 청소율입니까?" — 이 한 줄 질문에 4-좌표로 답하는 습관이 평생 가는 본능임.

---

<!-- 변환 노트
- 원본: 세션 04 청소율 v4.0 final
- 재구성 원칙:
  · 14개 카드(M1~M14)를 4-좌표 순서(매트릭스→장기→경로→대사체)로 재배치
  · M8(매트릭스)을 §2로 승격 — 프롤로그 60 L/h 미스터리의 해결책으로 활용
  · M7(PK5)을 §3.9 미리 깔기 + §7 구현 다리로 분리
  · M2.5(eGFR, 담즙, 장간순환)를 §3 신장 분해 안에 흡수
  · M10.5(Phase II)를 §4.3에 흡수 — CYP 옆자리에 즉시 배치
  · 각 절 끝에 "NONMEM에서 이게 어디 들어가는가" 박스 추가 — physiology→implementation 다리
  · "본능 한 줄" 패턴으로 trench-level habit 반복 노출
  · 어미: 음슴체 (~함, ~임, ~음, ~것임) 일관 적용
- 보존:
  · 모든 수식 overbrace/underbrace annotation
  · 모든 G&W / R&T 페이지·식 번호 출처
  · 모든 임상 anchor (methamphetamine, fentanyl/ritonavir, propranolol, morphine/M6G, irinotecan, lamotrigine/valproate, MMF, alfentanil/rifampin, alprenolol/pentobarbital, phenytoin/uremia, clofibric acid, tolbutamide, isoproterenol, carbamazepine, methylprednisolone hemisuccinate, N-desalkylhalazepam, metformin/cimetidine, probenecid/penicillin, dolutegravir/metformin, tenofovir, desipramine/quinidine, statins/OATP1B1)
  · PK5 numerical anchor (250 mg, CL ~1.2, fe ~35%, plasma CV 2.84%, urine CV 8.96%)
  · Q9 5단계 산출 (fm 0.3→0.6, 13.3배, dose 0.14)
  · MMP 20/50/77 anchor
  · Allometric scaling 전체 + species table
  · Maturation function (PMA, TM50, H)
  · 혼동 쌍 10개 모두
  · 자기검증 9문제 모두
- 추가:
  · 프롤로그 60 L/h 미스터리를 §2에서 명시적으로 해결하는 구조
  · 각 절 NONMEM 구현 다리
  · "한 줄 본능 모음" 표 (§11.3) — 임상 상황별 즉각 점검 항목
  · "닫는 말" §12 — 4-좌표 점검 순서를 한 흐름도로 마무리
-->

---

**문서 ID**: C-260518-085347-K4P

# § 1 — Session Header & Roadmap

---

**소스 자동 감지 결과**

| 문헌 | 범위 | 역할 분담 |
|---|---|---|
| Gabrielsson & Weiner 5e | §2.8.1–2.8.7, pp.141–157 + PK41, pp.661–664 | 수식 도출·ODE·실험 데이터 앵커링 |
| Rowland & Tozer 5e | Appendix A, pp.759–762 + Ch.2 §NCA, pp.17–24 | 임상 의미·개념 정의·적용 맥락 |

---

**세션 I-14: NCA — 수학적 기초·파라미터 계산**

**Big Idea**: NCA는 구획 모델 없이 $AUC$(0차 모멘트 면적)와 $AUMC$(1차 모멘트 면적)라는 단 두 개의 적분값으로 청소율·분포 부피·평균 체내 잔류 시간을 계산하는 '모델-독립 적분 기계'이며, 이 단순함이 규제 제출의 표준이 된 이유이자 — Turbojoint® PK41 사례처럼 — 비선형 PK를 처음 탐지해내는 가장 빠른 진단 도구이기도 하다.

**개념 항법도**

1. NCA vs 회귀분석 — 두 접근의 구조적 차이
2. AUC/AUMC — 선형 사다리꼴 규칙과 외삽
3. AUC/AUMC — 로그-선형 사다리꼴 규칙
4. **[⚡ Apex Concept]** λz — 말단 기울기 추정 전략과 외삽 오차의 전파
5. NCA 핵심 파라미터 — CL, MRT, Vss, Vz, t½의 모멘트 기반 도출
6. PK41 Turbojoint® — NCA로 MM 비선형 PK 진단 + 초기 추정값 도출

**지식 그래프 위치**

선행 지식: 1구획 IV bolus PK (I-01), 청소율·반감기 기하학, 단순 지수 소실  
열어주는 후속 지식: 비선형 PK (I-07, Michaelis-Menten), PopPK 공변량 분석 (II-08), 생물학적 동등성 시험 설계, 규제 제출용 PK 보고서 작성

---

# § 2 — Concept Anatomy Cards

---

## Card 1 — NCA vs 회귀분석: 두 언어의 구조적 차이

---

### ━━ [개념 Big Idea: 거장의 시각] ━━

**왜 치명적으로 중요한가**: NDA/IND 제출 시 1차 PK 파라미터 산출에 NCA를 사용할지 모델 기반 회귀를 사용할지를 혼동하면, 규제 심사관이 요청하는 CL과 Vss 계산 근거 자체가 무너져 Deficiency Letter를 받는다.

**체화해야 할 단 하나의 직관**: NCA는 '데이터가 말하는 면적의 언어'이고, 회귀분석은 '모델이 주장하는 함수의 언어'이다. NCA는 $C_i$들의 합에서 CL을 추론하고, 회귀는 $K_a$·$K$·$V$ 같은 파라미터로 CL을 역산한다 — 같은 데이터에서 같은 답을 내지만 경로가 전혀 다르다.

**이 직관을 머릿속에 박고 아래를 읽어라**: 사다리꼴 합산이 왜 CL이 되는지가 자연스럽게 보이기 시작할 것이다.

---

**A. Formal Definition**

NCA(비구획 분석)는 특정 구획 모델을 가정하지 않고 농도-시간 프로파일의 면적 적분값으로부터 PK 파라미터를 직접 계산하는 방법이다. 단, 소실은 샘플링 구획에서만 일어나며 선형(1차) 소실임을 가정한다. 회귀분석은 함수 파라미터($K_a$, $K$, $V$)를 추정하여 데이터에 모델 곡선을 적합시킨다.

**B. Derivation**

Figure 2.113 (Gabrielsson p.141)이 두 접근을 나란히 보여준다:

$$Cl_{NCA} = \frac{Dose}{\sum_{i=1}^{n} A_i}$$

$$Cl_{regression} = \frac{Dose}{\int \frac{K_a F D}{V(K_a - K)}\left[e^{-Kt} - e^{-K_a t}\right] dt}$$

왼쪽은 면적의 합, 오른쪽은 함수의 적분. 모수 추정 없이 면적만으로 CL을 얻는다는 것이 NCA의 핵심 구조다.

**C. Structural Necessity**

이 형태가 불가피한 이유: 선형 PK에서 $CL = Dose/AUC_0^\infty$는 질량 보존 법칙의 직접적 결과다. 체내에 들어온 모든 약물이 결국 CL에 의해 소실되므로, $AUC_0^\infty \cdot CL = Dose$는 항등식이다. 어떤 구획 구조도 이 관계를 변경하지 않는다.

**D. Assumptions & Boundary Conditions**

① 소실은 샘플링 구획(혈장)에서만 일어남 → 말초 구획에서 소실이 있으면 CL 과소추정  
② 선형(1차) 소실 가정 → Turbojoint® PK41처럼 비선형 PK에서 NCA-CL이 용량 의존적으로 변함 (이것 자체가 진단 시그니처)  
③ 외삽 구간이 전체 AUC의 20-25% 이내여야 함 (Gabrielsson p.148)

**E. Limitations**

비선형 PK에서 CL, Vss 값은 용량 의존적으로 변하므로 직접 비교 불가. MM PK에서 NCA-CL은 특정 농도 조건에서의 겉보기 청소율일 뿐이다.

**F. Five Cognitive Layers**

- L1: $CL = D_{iv}/AUC_0^\infty$ — 단위: L/h, 면적에서 직접 도출
- L2: AUC는 C-t 곡선 아래 면적 = 농도의 '시간 가중 누적' — 직사각형의 합이 적분을 근사
- L3: 수문학의 유역 유량(강수량/유출 면적)과 구조적 동형
- L4: CL은 간·신장 생리학과 연결, Vss는 조직 분포를 반영
- L5: Phoenix WinNonlin, R PKNCA 패키지에서 자동 계산

**G. Zettelkasten Atom**

```yaml
---
aliases: [NCA, 비구획 분석, 모델-독립 PK]
tags: [pharmacometrics/pk, nca, regulatory]
up: "[[PK 파라미터 계산 MOC]]"
related: ["[[AUC 면적 계산]]", "[[청소율 CL]]", "[[MRT]]"]
source: "Gabrielsson 5e, §2.8.1, p.141; R&T 5e, App.A, p.759"
---
```

NCA는 구획 모델 가정 없이 $CL = Dose/AUC_0^\infty$로 청소율을 계산하며, 소실이 샘플링 구획에서만 선형으로 일어난다는 최소 가정만 요구한다. 회귀분석과 상보적으로 사용되며, NCA는 탐색·진단 도구, 회귀는 기전 해석 도구로 이해할 수 있다. Turbojoint® PK41에서처럼 용량 의존적 CL 변화를 NCA로 먼저 탐지하고, MM 비선형 모델로 회귀하는 순서가 모범 워크플로다.

---

## Card 2 — [⚡ Apex Concept] λz — 말단 기울기 추정과 외삽 오차의 전파

---

### ━━ [개념 Big Idea: 거장의 시각] ━━

**왜 치명적으로 중요한가**: λz를 잘못 추정하면 외삽 AUC, CL, MRT, Vss가 모두 틀어지는 '연쇄 오류 폭발'이 일어난다 — 하나의 기울기 오류가 NCA 보고서 전체를 오염시킨다.

**체화해야 할 단 하나의 직관**: λz는 '말단 소실 속도의 순수한 측정값'이다 — 흡수 구간이 아닌 진정한 terminal phase에서, 최소 3-4개 관측값이 로그-선형으로 늘어선 구간만을 선택해야 한다. '가장 많은 점을 포함할수록 좋다'는 직관은 치명적 오류다.

**이 직관을 머릿속에 박고 아래를 읽어라**: λz 선택이 왜 알고리즘이 아닌 판단의 문제인지가 보일 것이다.

---

**A. Formal Definition**

λz는 반대수(semi-log) 농도-시간 곡선의 말단 하강 기울기의 절댓값으로, 단위는 time⁻¹이다. 로그-선형 회귀로 추정하며, 이 기울기가 말단 반감기 $t_{1/2z}$와 $AUC_{t_{last}}^\infty$의 외삽 계산에 직접 사용된다.

**B. Derivation**

농도가 지수 소실하면 (Gabrielsson Eq. 2:314):

$$C_{i+1} = C_i \cdot e^{-K \cdot \Delta t}$$

양변에 자연로그를 취하면 기울기 K(= λz for 1-compartment)를 얻는다:

$$K = \lambda_z = \frac{\ln(C_i / C_{i+1})}{\Delta t} \quad \text{[Eq. 2:315]}$$

`[출처: Gabrielsson 5e, §2.8.3, p.144]`

외삽 AUC는 이 λz로:

$$AUC_{t_{last}}^\infty = \frac{C_{last}}{\lambda_z} \quad \text{[Eq. 2:311 / Eq. 2:319]}$$

`[출처: Gabrielsson 5e, §2.8.2, p.143]`

**외삽 비율 품질 기준:**

$$\% \; extrapolated = \frac{AUC_{t_{last}}^\infty}{AUC_0^\infty} \times 100 \quad \text{[Eq. 2:324]}$$

Gabrielsson 권고: 이 비율이 20-25%를 초과하면 샘플링 설계 재검토 필요 (p.148).

**실제 수치 앵커링 — Turbojoint® PK41**: Gabrielsson p.661-664에서, 310 µg/kg 투여군의 말단 데이터(t=6, 8, 10 h; C=15, 5, 0.47 µg·L⁻¹)로부터 λz를 추정하고 외삽. 이로부터 NCA CL = 1.6 L·h⁻¹·kg⁻¹을 얻었으며, 780 µg/kg 군에서는 CL = 0.9 L·h⁻¹·kg⁻¹로 감소 — λz 추정 정확도가 용량 의존성 탐지의 핵심이었다.

**C-2. Plausible Fallacy — "더 많은 점을 포함할수록 λz가 정확해진다"**

**오류의 구체적 형태**: 분포상(α phase)이 끝나지 않은 초기 관측값들을 말단 회귀에 포함시킬 때 발생한다. 2구획 약물에서 α-상 데이터를 λz 추정에 포함하면 기울기가 완만해져 λz가 과소추정된다.

**나비효과**: λz 과소추정 → $AUC_{t_{last}}^\infty = C_{last}/\lambda_z$ 과대추정 → $AUC_0^\infty$ 과대추정 → $CL = Dose/AUC$ 과소추정 → $MRT = AUMC/AUC$ 과대추정 → $V_{ss} = MRT \cdot CL$ 방향 불분명(두 오류가 상쇄 또는 증폭). 단 하나의 기울기 오류가 모든 NCA 파라미터를 오염시키는 '연쇄 오염 시그니처'다.

**GOF 시그니처**: 반대수 플롯에서 선택된 점들이 직선에 잘 맞지 않고 곡선 형태를 보임 — 이를 **"말단 곡률 편향(Terminal Curvature Bias)"** 이라 명명한다.

**D. Assumptions & Boundary Conditions**

- 최소 3-4개 관측값 필요 (Gabrielsson p.146, Figure 2.119)
- 이상적으로 2-3 반감기 이상 경과 후 데이터 포함
- 마지막 관측 농도($C_{obs}$)가 회귀선에서 벗어난 경우 예측값($\hat{C}_{last}$) 사용 권고 (Gabrielsson p.147, Figure 2.120)
- LOQ 미만 값은 결측(missing)으로 처리, 0 또는 LOQ로 대체 금지 (Gabrielsson p.153)

**E. Limitations**

2구획 이상 약물에서 λz는 '진정한 소실 속도'가 아닌 '말단 하강 속도'이며, 실제 소실은 α와 β가 복합된 결과다. 이 경우 $V_z$(= $CL/\lambda_z$)는 진정한 분포 부피가 아닌 '말단 위상 분포 부피'가 된다.

**F. Five Cognitive Layers**

- L1: $\lambda_z = \ln(2)/t_{1/2}$, 단위: h⁻¹; 로그-선형 회귀의 기울기 절댓값
- L2: 반대수 플롯에서 말단 직선 구간의 음의 기울기 — 시각적으로 '어디가 진짜 terminal인가'를 눈으로 먼저 확인
- L3: 방사성 동위원소 붕괴 상수와 수학적으로 동일 구조
- L4: λz ≈ K_el(1구획) = CL/V; 간·신장 기능 저하 시 λz 감소, t½ 연장
- L5: WinNonlin λz interval 지정 필수; R PKNCA `pk.calc.half.life()` 자동 선택 알고리즘은 R² 기반 — 임상 판단 필요

**G. Zettelkasten Atom**

```yaml
---
aliases: [lambda z, 말단 소실 속도 상수, terminal slope]
tags: [pharmacometrics/pk, nca, lambda_z]
up: "[[NCA 파라미터 계산]]"
related: ["[[AUC 외삽]]", "[[t½ 반감기]]", "[[Vz vs Vss]]"]
source: "Gabrielsson 5e, §2.8.3-2.8.4, pp.144-147"
---
```

λz는 반대수 농도-시간 곡선의 말단 직선 구간을 로그-선형 회귀하여 얻는 말단 소실 속도 상수다. 최소 3-4개 관측값이 필요하며 분포상 데이터를 포함해서는 안 된다. λz의 오류는 $AUC_{t_{last}}^\infty$, CL, MRT, Vss 전체로 전파되는 연쇄 오염을 일으키므로, NCA 워크플로에서 λz 선택 구간 결정이 단일 최고 위험 단계다. 마지막 관측 농도가 회귀선에서 벗어난 경우 예측값 사용을 권고한다.

---

## Card 3 — NCA 핵심 파라미터 — CL, MRT, Vss, Vz의 모멘트 도출

---

### ━━ [개념 Big Idea: 거장의 시각] ━━

**왜 치명적으로 중요한가**: Vss와 Vz를 혼동하여 NDA 보고서에 Vz를 '분포 부피'로 보고하면 조직 분포 특성을 오해한 용량 설계로 이어질 수 있으며, 심사관 질의를 받을 수 있다.

**체화해야 할 단 하나의 직관**: MRT는 약물 분자 한 개가 체내에 머무는 '평균 시간'이고, Vss는 그 평균 시간 동안 분포한 '평균 공간'이다 — 두 파라미터 모두 약물 분자의 '시공간 거동'을 기술한다.

**이 직관을 머릿속에 박고 아래를 읽어라**: MRT·Cl·Vss의 삼각 관계가 하나의 필연적 구조로 보일 것이다.

---

**A. Formal Definition**

0차 모멘트(AUC)와 1차 모멘트(AUMC)를 이용한 파라미터 계산:

**B. Derivation**

**청소율 (Clearance)**:
$$Cl = \frac{D_{iv}}{AUC_0^\infty} \quad \text{[Eq. 2:325]}$$

`[출처: Gabrielsson 5e, §2.8.5, p.149]`

**경구 청소율**: $Cl_o = Cl/F = D_{po}/AUC_0^\infty$

**생체이용률**: 
$$F = \frac{AUC_{0,po}^\infty}{AUC_{0,iv}^\infty} \cdot \frac{D_{iv}}{D_{po}} \quad \text{[Eq. 2:327]}$$

**평균 체내 잔류 시간 (MRT)**:
$$MRT = \frac{AUMC_0^\infty}{AUC_0^\infty} \quad \text{(IV bolus)}$$

지속 정주 보정: $MRT = \frac{AUMC_0^\infty}{AUC_0^\infty} - \frac{T_{inf}}{2}$ `[Eq. 2:328]`

1차 흡수 보정: $MRT = \frac{AUMC_0^\infty}{AUC_0^\infty} - \frac{1}{K_a}$ `[Eq. 2:329]`

**정상 상태 분포 부피 (Vss)**:
$$V_{ss} = MRT \cdot Cl = \frac{AUMC_0^\infty}{AUC_0^\infty} \cdot \frac{D_{iv}}{AUC_0^\infty} = \frac{D_{iv} \cdot AUMC_0^\infty}{\left[AUC_0^\infty\right]^2} \quad \text{[Eq. 2:337]}$$

`[출처: Gabrielsson 5e, §2.8.5, p.151]`

**말단 위상 분포 부피 (Vz)**:
$$V_z = \frac{Cl}{\lambda_z} = \frac{D_{iv}}{AUC_0^\infty \cdot \lambda_z} \quad \text{[Eq. 2:338]}$$

**말단 반감기**: $t_{1/2z} = \frac{\ln 2}{\lambda_z}$ `[Eq. 2:340]`

**효과적 반감기**: $t_{eff} = \ln(2) \cdot MRT$

**AUMC 선형 사다리꼴 규칙** (Gabrielsson Eq. 2:312):

$$AUMC_0^{t_{last}} = \sum_{i=1}^{n} \frac{t_i \cdot C_i + t_{i+1} \cdot C_{i+1}}{2} \cdot \Delta t$$

**AUMC 외삽** (Eq. 2:313):

$$AUMC_{t_{last}}^\infty = \frac{t_{last} \cdot C_{last}}{\lambda_z} + \frac{C_{last}}{\lambda_z^2}$$

**실제 수치 앵커링 — Turbojoint® PK41 (Gabrielsson pp.661-664)**:  
체중 70 kg, 310 µg/kg 투여 (= 21,700 µg 총량):
- NCA 결과: $Cl$ = 1.6 L·h⁻¹·kg⁻¹, $V$ = 2.3 L·kg⁻¹, $MRT$ = 1.4 h
- 780 µg/kg: $Cl$ = 0.9 L·h⁻¹·kg⁻¹, $V$ = 1.8 L·kg⁻¹, $MRT$ = 1.9 h
- 용량 증가 → CL 감소 → MM 비선형 소실 진단

**C. Structural Necessity**

$V_{ss} = MRT \cdot Cl$이 불가피한 이유: 약물이 체내를 'CL 속도'로 통과하며 'MRT 시간' 동안 머물 때 차지하는 공간이 Vss다. 이것은 $\text{공간} = \text{속도} \times \text{시간}$의 운동학적 필연이다. 반면 Vz = Cl/λz는 말단 위상에서 분포와 소실이 평형 상태에 있다는 추가 가정이 필요하여, 다구획 약물에서는 Vss ≠ Vz다.

**D. Assumptions & Boundary Conditions**

Vss는 선형 PK와 IV bolus(또는 짧은 주입) 가정 하에서만 Vss = MRT·CL이 성립. 경구 투여 시 AUMC에는 흡수 시간이 포함되어 MRT가 아닌 MRTPO = MRT + MIT가 관측된다.

**E. Limitations**

AUMC는 AUC보다 외삽 오차에 훨씬 민감하다 — 말단 구간이 $t \cdot C$ 가중치로 증폭되기 때문. 따라서 Vss의 정확도는 AUC보다 낮으며, 외삽 비율이 클수록 Vss 불확실성이 급격히 증가한다 (Figure 2.121, Gabrielsson p.148).

**F. Five Cognitive Layers**

| 레이어 | 내용 |
|---|---|
| L1 수식 | $V_{ss} = D_{iv} \cdot AUMC_0^\infty / [AUC_0^\infty]^2$, 단위: L |
| L2 기하학 | AUC는 C-t 곡선 아래 면적; AUMC는 t·C-t 곡선 아래 면적 — 두 곡선의 모양 비교가 직관적 |
| L3 동형성 | 통계학의 분산(Var) = E[X²]–E[X]²와 동일한 모멘트 구조 |
| L4 생리학 | $V_{ss}$ ↑ → 조직 결합 강함; MRT ↑ → 체내 잔류 길어짐 |
| L5 실무 | WinNonlin: AUC_last + AUC_inf; NCA 보고서에 Vss와 Vz 둘 다 기재 필수 |

**G. Zettelkasten Atom**

```yaml
---
aliases: [Vss, MRT, NCA 파라미터, 모멘트 해석]
tags: [pharmacometrics/pk, nca, Vss, MRT]
up: "[[NCA 파라미터 계산]]"
related: ["[[λz 추정]]", "[[Vz vs Vss 혼동쌍]]", "[[AUMC]]"]
source: "Gabrielsson 5e, §2.8.5, pp.148-151"
---
```

NCA에서 Vss = MRT·CL이며, 두 파라미터 모두 $AUMC_0^\infty$와 $AUC_0^\infty$의 비에서 도출된다. AUMC는 외삽 오차에 AUC보다 민감하므로 Vss는 외삽 비율 관리가 특히 중요하다. Vz = CL/λz는 말단 위상 기반 분포 부피로 Vss와 다르며, 다구획 약물에서 Vz > Vss가 전형적이다.

---

## Card 4 — AUC/AUMC 면적 계산: 선형 vs 로그-선형 사다리꼴 규칙

---

### ━━ [개념 Big Idea: 거장의 시각] ━━

**왜 치명적으로 중요한가**: 생물학적 동등성 시험에서 두 제제의 AUC 비교가 핵심인데, 사다리꼴 규칙 선택이 달라지면 AUC 추정값이 체계적으로 편향되어 동등성 판정 결과가 뒤바뀔 수 있다.

**체화해야 할 단 하나의 직관**: 선형 사다리꼴은 '곡선을 직선으로 근사'하고, 로그-선형 사다리꼴은 '곡선을 지수 감소로 근사'한다 — 어느 것이 더 정확한가는 구간에서 농도 프로파일의 실제 모양에 달려 있다.

**이 직관을 머릿속에 박고 아래를 읽어라**: 어떤 구간에 어떤 방법을 써야 하는지가 규칙이 아닌 원리로 이해될 것이다.

---

**A. Formal Definition**

**선형 사다리꼴 규칙** — 인접 두 점 사이를 직선으로 연결하여 면적을 근사 (R&T Appendix A, p.759; Gabrielsson Eq. 2:310):

$$AUC_0^{t_{last}} = \sum_{i=1}^{n} \frac{C_i + C_{i+1}}{2} \cdot \Delta t$$

`[출처: Gabrielsson 5e, §2.8.2, p.143; R&T 5e, App.A, p.759]`

**로그-선형 사다리꼴 규칙** — 농도가 두 점 사이에서 순지수 감소한다고 가정 (Gabrielsson Eq. 2:316):

$$AUC_i^{i+1} = \frac{C_i - C_{i+1}}{\ln(C_i/C_{i+1})} \cdot \Delta t$$

`[출처: Gabrielsson 5e, §2.8.3, p.145]`

**B. 언제 어느 방법을?**

| 상황 | 권고 방법 |
|---|---|
| 상승 구간 (Cmin → Cmax) | 선형 |
| 하강 1차 소실 구간 | 로그-선형 |
| Ci = 0 또는 Ci+1 = Ci | 선형 (로그-선형 불가) |
| 0차 소실 (선형 감소) | 선형 (큰 △t도 무방) |
| 반감기 대비 △t가 큰 경우 | 로그-선형 권고 |
| 교차 비교 생물학적 동등성 | 혼합법(Lin-Log) 표준 |

실제 적용: **혼합법(Lin-Log)** — 상승 구간에 선형, 하강 구간에 로그-선형 (Figure 2.118, Gabrielsson p.146).

**실제 수치 앵커링 — Zileuton (R&T App.A, Table A-2)**: 600 mg 경구 투여 후 zileuton 농도 데이터:

| 시간(h) | 0 | 0.5 | 1 | 1.5 | 2 | 3 | 4 | 6 | 8 | 10 | 12 | 14 | 24 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| C(mg/L) | 0 | 2.14 | 2.95 | 3.25 | 3.27 | 2.68 | 2.15 | 1.12 | 0.611 | 0.321 | 0.180 | 0.101 | 0.011 |

선형 사다리꼴 적용 시 $AUC_{0-24}$를 계산하면 약 13.7 mg·h/L (0-24h 합산). 이후 $C_{24}/\lambda_z$ 를 더하면 $AUC_0^\infty$ 산출 가능.

**C. Structural Necessity**

선형 규칙이 하강 구간에서 과대추정하는 이유: 지수 감소 곡선의 직선 근사는 곡선 위를 덮게 된다. 샘플링 간격이 반감기와 유사할 때 이 오차가 임상적으로 의미 있어진다 (Figure 2.115, Gabrielsson p.142).

**D. Assumptions & Boundary Conditions**

로그-선형 규칙은 두 점 사이가 순지수 감소여야 함. 2구획 약물의 분포상에서는 이 가정이 위반된다.

**E. Limitations**

Gabrielsson p.146 실용적 조언: "두 방법의 차이는 합리적인 샘플링 설계 하에서 임상적으로 거의 무시 가능하다. 교차 연구의 평균 AUC에서 개인별 오차는 상쇄된다."

**G. Zettelkasten Atom**

```yaml
---
aliases: [사다리꼴 규칙, AUC 계산, 선형-로그 선형]
tags: [pharmacometrics/pk, nca, AUC_calculation]
up: "[[NCA 파라미터 계산]]"
related: ["[[λz 추정]]", "[[AUC 외삽]]"]
source: "Gabrielsson 5e, §2.8.2-2.8.3, pp.141-146; R&T 5e, App.A, pp.759-762"
---
```

AUC 계산에는 선형 사다리꼴(직선 근사)과 로그-선형 사다리꼴(지수 감소 근사) 두 방법이 있다. 상승 구간에는 선형, 하강 구간에는 로그-선형이 이론적으로 더 정확하지만, 충분한 샘플링 밀도 하에서 두 방법의 차이는 임상적으로 무시 가능하다. 생물학적 동등성 시험에서는 두 방법을 혼용하는 Lin-Log 방식이 표준이다.

---

# § 5 — Confusion Pair Dissection

---

## 혼동 쌍 1: Vss vs Vz (Vdβ) — 가장 많이 틀리는 분포 부피

| 비교 차원 | **Vss** | **Vz** (= Vdβ) |
|---|---|---|
| **표면적 유사성** | 둘 다 '분포 부피', 단위 L 또는 L/kg | |
| **수식** | $V_{ss} = MRT \cdot Cl = \frac{D \cdot AUMC_0^\infty}{[AUC_0^\infty]^2}$ | $V_z = \frac{Cl}{\lambda_z} = \frac{D}{AUC_0^\infty \cdot \lambda_z}$ |
| **생물학적 지시체** | 약물이 정상 상태에서 모든 구획에 분포된 총 부피 — 조직/혈장 결합의 진정한 평형 | 말단 β 위상에서 분포와 소실이 겉보기 평형인 상태의 부피 — λz에 의존 |
| **다구획 약물에서** | Vss는 $V_1 + V_2$에 가깝게 추정됨 | Vz ≥ Vss (항상); β가 느릴수록 Vz >> Vss |
| **λz 변화 시** | λz 변해도 Vss 불변 (CL과 MRT의 함수) | Vz = CL/λz이므로 λz가 변하면 즉시 변함 |
| **임상/규제 결과** | 약물-약물 상호작용(DDA)로 단백 결합 변화 시 Vss가 임상 예측에 유효 | Vz를 Vss 대신 NDA에 보고하면 조직 분포 과대추정 오류 |
| **⚡ 기억 고리** | **"Vss는 조직의 포부(aspiration), Vz는 β의 그림자(shadow)"** — 분포 평형에서의 진짜 공간이 Vss고, 말단 기울기가 느릴수록 그 그림자(Vz)가 길게 늘어난다 | |
| **치명적 타격** | Vz를 Vss로 보고하고 신부전 환자의 용량을 설계할 경우, 진정한 분포 부피를 과대추정하여 부하 용량(loading dose)을 과다 처방 — 독성 사고 시나리오 직결 | |

---

## 혼동 쌍 2: MRT vs t½ (말단) — 수학적으로 항상 다르다

| 비교 차원 | **MRT** | **t½z** |
|---|---|---|
| **표면적 유사성** | 둘 다 약물이 '체내에 머무는 시간'을 기술하는 것처럼 보임 | |
| **수식** | $MRT = \frac{AUMC_0^\infty}{AUC_0^\infty}$ | $t_{1/2z} = \frac{\ln 2}{\lambda_z}$ |
| **생물학적 지시체** | 약물 분자 한 개의 평균 체내 잔류 시간 — 모든 구획 분포 포함 | 말단 위상에서 농도가 절반으로 감소하는 시간 — λz만의 함수 |
| **1구획 IV bolus** | $MRT = 1/k = 1/\lambda_z = t_{1/2}/\ln 2$ | $t_{1/2} = \ln 2 / k$ |
| **비율** | $MRT = t_{1/2} / \ln 2 = 1.4427 \times t_{1/2}$ (1구획) | 항상 MRT보다 짧음 (1구획에서) |
| **다구획 약물** | MRT가 더 크게 벌어짐 — 분포 구획 체류 시간 포함 | 단지 β 위상 반감기 |
| **임상/규제 결과** | 다중 투여 약물의 축적 예측에 MRT 기반 effective t½ = ln(2)·MRT 사용 필요 | t½z만 보고하면 다구획 약물의 진정한 체내 잔류 기간을 과소평가 |
| **⚡ 기억 고리** | **"MRT는 t½보다 항상 44% 더 길다 — ×1/ln2. 이 비율은 지수함수의 수학적 필연이지, 생리학적 차이가 아니다."** Gabrielsson p.151: "effective half-life = ln(2)·MRT" | |

---

## 혼동 쌍 3: AUC 외삽 — 관측 Clast vs 예측 Ĉlast

| 비교 차원 | **관측값 Clast 사용** | **회귀 예측값 Ĉlast 사용** |
|---|---|---|
| **표면적 유사성** | 둘 다 $C_{last}/\lambda_z$ 형태 | |
| **수식** | $AUC_{t_{last}}^\infty = C_{last,obs}/\lambda_z$ | $AUC_{t_{last}}^\infty = \hat{C}_{last}/\lambda_z$ |
| **권고** | Clast가 회귀선에 잘 맞을 때만 사용 | **일반적으로 Gabrielsson 권고** (p.147) |
| **임상 결과** | Clast가 선 위에 있으면 AUC 과대추정; 선 아래면 과소추정 (Figure 2.120) | 회귀선 기반으로 안정적 |
| **⚡ 기억 고리** | "마지막 점 하나가 노이즈면 외삽 면적 전체가 흔들린다 — 예측값을 쓰는 것이 더 정직한 통계다" | |

---

# § 7 — Self-Test: Active Recall Module

---

**Q1 [회상] ○**  
선형 사다리꼴 규칙으로 $AUC_0^{t_{last}}$를 계산할 때 사용하는 수식을 쓰고, 왜 하강 구간에서 이 방법이 과대추정을 유발하는지 설명하라.

<details><summary>정답 공개</summary>

$$AUC_0^{t_{last}} = \sum_{i=1}^{n} \frac{C_i + C_{i+1}}{2} \cdot \Delta t$$

하강 구간에서 1차 소실은 지수 감소이므로 두 점 사이의 곡선이 직선 아래로 오목하게 꺾인다. 선형 근사는 이 오목한 부분을 메워 실제보다 넓게 잡으므로 과대추정이 발생한다. 샘플링 간격 △t가 t½ 대비 클수록 이 오차가 커진다.

**다음 깊이 질문**: 로그-선형 사다리꼴 규칙이 $C_i = 0$ 또는 $C_{i+1} = C_i$인 경우 실패하는 수학적 이유는?
</details>

---

**Q2 [회상] ★★**  
$V_{ss}$를 $AUC_0^\infty$와 $AUMC_0^\infty$, 그리고 IV 볼루스 용량 $D$만으로 표현하는 수식을 쓰고, 이 수식이 $V_{ss} = MRT \cdot CL$과 동치임을 보여라.

<details><summary>정답 공개</summary>

$$V_{ss} = \frac{D_{iv} \cdot AUMC_0^\infty}{\left[AUC_0^\infty\right]^2}$$

증명:
$$MRT = \frac{AUMC_0^\infty}{AUC_0^\infty}, \quad CL = \frac{D_{iv}}{AUC_0^\infty}$$
$$MRT \cdot CL = \frac{AUMC_0^\infty}{AUC_0^\infty} \cdot \frac{D_{iv}}{AUC_0^\infty} = \frac{D_{iv} \cdot AUMC_0^\infty}{\left[AUC_0^\infty\right]^2} = V_{ss} \quad \blacksquare$$

**다음 깊이 질문**: 동일한 약물에서 Vss와 Vz 중 어느 것이 더 크며, 그 이유는 무엇인가?
</details>

---

**Q3 [적용] ★★**  
Turbojoint® PK41 (Gabrielsson p.661-664)에서 310 µg/kg 투여 시 NCA-CL = 1.6 L·h⁻¹·kg⁻¹이고 780 µg/kg 투여 시 NCA-CL = 0.9 L·h⁻¹·kg⁻¹이었다. 이 NCA 결과가 어떤 PK 모델을 제안하며, 그 모델에서 CL이 용량 의존적으로 변하는 이유를 수식으로 설명하라.

<details><summary>정답 공개</summary>

용량 증가에 따른 NCA-CL 감소는 **Michaelis-Menten 비선형(용량 포화) 소실**을 시사한다.

MM 모델에서 CL은:
$$CL = \frac{V_{max}}{K_m + C}$$

고농도($C$가 $K_m$과 비슷하거나 큼)일수록 $K_m + C$가 커져 CL이 감소한다. 310 µg/kg 투여의 최고 농도(44 µg/L)보다 780 µg/kg 투여의 최고 농도(180 µg/L)가 훨씬 높으므로, 780 µg/kg 군에서 CL이 더 낮게 측정된다. 따라서 NCA는 "$CL$과 $V$가 용량 의존적"이라는 신호를 통해 비선형 모델의 필요성을 진단한다.

**다음 깊이 질문**: Gabrielsson은 이 NCA 결과를 어떻게 MM 초기 추정값($V_{max}$, $K_m$)으로 변환했는가?
</details>

---

**Q4 [회상] ○**  
λz 추정 시 "최소 3-4개 관측값이 필요하다"는 권고의 수학적·통계적 근거는 무엇인가?

<details><summary>정답 공개</summary>

직선을 추정하는 데 이론적으로 2개 점이면 충분하지만, 2개 점은 잔차가 0이므로 회귀 적합도(R², SE)를 계산할 수 없다. 최소 3개 점이 있어야 잔차를 가지며, 4개 이상이면 말단 직선 구간의 선형성(linearity in log scale)을 통계적으로 검정하고 이상치를 탐지할 수 있다. Gabrielsson p.146: 이상적으로 3-4 반감기가 경과한 데이터를 사용하되, 현실적 제약 시 최소 3-4점을 요구한다.

**다음 깊이 질문**: 반대수 플롯에서 말단 구간이 완벽히 직선처럼 보여도 실제로 2구획 약물의 α상이 포함되어 있을 수 있다 — 이를 어떻게 구분하는가?
</details>

---

**Q5 [적용] ★**  
지속 정주(constant-rate infusion)로 투여한 약물의 MRT를 IV bolus와 동일하게 $AUMC/AUC$로만 계산하면 어떤 오류가 발생하는가? 올바른 보정 수식을 제시하라.

<details><summary>정답 공개</summary>

지속 정주 시 약물 분자는 주입 라인(시린지, 카테터 등)에서 평균 $T_{inf}/2$ 만큼의 시간을 보내고 나서야 혈장에 도달한다. 이 '입력 평균 시간(MIT = $T_{inf}/2$)'이 측정된 AUMC/AUC에 포함되어 있으므로, 이를 빼지 않으면 MRT가 과대추정된다.

올바른 보정 (Gabrielsson Eq. 2:328):
$$MRT = \frac{AUMC_0^\infty}{AUC_0^\infty} - \frac{T_{inf}}{2}$$

1차 흡수(경구)의 경우 (Eq. 2:329):
$$MRT = \frac{AUMC_0^\infty}{AUC_0^\infty} - \frac{1}{K_a}$$

**다음 깊이 질문**: 경구 투여 시 MAT(평균 흡수 시간)를 IV와 PO의 MRT 차이로 구할 수 있다 — 이 방법의 가정과 한계는?
</details>

---

**Q6 [적용] ★**  
$AUC_{t_{last}}^\infty$가 $AUC_{total}$의 30%를 차지하는 NCA 분석 결과를 제출받았다. 어떤 조치를 취해야 하며 그 이유는?

<details><summary>정답 공개</summary>

Gabrielsson p.148 권고 기준(20-25% 이내)을 초과하는 수치이므로, 외삽 의존도가 과도하다. 이 경우 CL, Vss, MRT 모두 λz 추정 오차에 크게 의존하게 된다.

조치: (1) λz 추정 구간 재검토 — 점 수, 구간 적절성 확인; (2) 샘플링 설계 문제라면 추가 시점 채혈 또는 연구 재설계 권고; (3) 보고 시 "AUC 외삽 비율 30%로 예비 추정값(preliminary estimate)임"을 명시; (4) 모델 기반 회귀분석(예: NONMEM 1구획 모델)으로 CL을 독립적으로 확인하는 것을 권고.

**다음 깊이 질문**: 비선형 MM 소실 약물(예: Turbojoint®)에서 λz가 용량 의존적으로 변할 때 AUC 외삽 비율은 어떻게 달라지는가?
</details>

---

**Q7 [적용] ★★**  
Zileuton (R&T App.A, Table A-2) 데이터에서 t=12h, C=0.180 mg/L과 t=14h, C=0.101 mg/L의 두 관측값 구간에 대해 (a) 선형 사다리꼴 AUC와 (b) 로그-선형 사다리꼴 AUC를 각각 계산하고 차이를 비교하라.

<details><summary>정답 공개</summary>

**(a) 선형 사다리꼴**:
$$AUC = \frac{0.180 + 0.101}{2} \times 2 = 0.1405 \times 2 = 0.281 \; \text{mg·h/L}$$

**(b) 로그-선형 사다리꼴**:
$$AUC = \frac{(0.180 - 0.101)}{\ln(0.180/0.101)} \times 2 = \frac{0.079}{\ln(1.782)} \times 2 = \frac{0.079}{0.5793} \times 2 = 0.1364 \times 2 = 0.273 \; \text{mg·h/L}$$

**차이**: 선형이 로그-선형보다 약 3% 과대추정. 이 구간에서 농도비(0.180/0.101 ≈ 1.78배)가 크지 않아 차이가 작다. 2배 이상 차이 날 때 로그-선형이 유의미하게 더 정확해진다.

**다음 깊이 질문**: 이 두 관측값 구간에서 실제로 어떤 약물 거동이 선형 사다리꼴을 더 적합하게 만드는 상황이 있는가?
</details>

---

**Q8 [보스 딜레마] ★★ — 소크라테스식 딜레마**

Phase 1 FIH 연구에서 5명의 피험자에게 단회 경구 투여 후 PK 데이터를 수집했다. 샘플링은 72시간까지만 진행되었으며, 1명의 피험자에서 AUC 외삽 비율이 35%에 달했다. 규제 제출 시한이 2주 후이며, 추가 샘플링은 현실적으로 불가능하다.

**딜레마**: NCA로 얻은 CL과 Vss를 그대로 보고서에 사용하는가, 아니면 모델 기반(1구획 NONMEM) 추정값으로 대체하는가? 두 선택 모두 단점이 있다.

<details><summary>수석 모델러의 Trade-off 논리</summary>

**NCA 사용 시**: 외삽 비율 35%는 Gabrielsson 권고 기준 초과이므로, 보고서에 "외삽 의존도 높음, 추정값 불확실"을 명시해야 한다. 규제 심사관이 Deficiency Letter를 보낼 가능성이 있다.

**모델 기반 대체 시**: NONMEM 1구획 모델은 샘플링 부족 상황에서 수렴 실패나 파라미터 식별성 문제가 발생할 수 있다. 또한 모델 선택(1구획 vs 2구획)이 CL 추정값에 영향을 주므로, 모델 의존적이라는 비판을 받을 수 있다.

**수석 모델러의 실무 결정**: 두 방법을 **병행 보고**한다. 기본 NCA 결과를 primary로 제시하되 외삽 비율 명시, 1구획 모델 기반 CL을 sensitivity analysis로 제시하여 두 값의 일치도를 보인다. 불일치(예: 20% 이상 차이)가 크면 데이터 제한 사항을 규제 문서에 명시하고, Phase 2에서 PK 샘플링 설계를 강화한다는 약속을 포함한다. IND 또는 Phase 2 프로토콜에 "말단 반감기 신뢰 추정을 위한 충분한 샘플링 시점 확보" 조항을 삽입한다.

**규제 방어 언어**: "NCA-derived PK parameters were estimated from data with a terminal AUC extrapolation of 35%. A sensitivity analysis using a one-compartment model yielded consistent estimates (CL within X%). These results are considered preliminary and will be refined with improved sampling design in the Phase 2 study."
</details>

---

# § 8 — Meta-Frame & Big Picture

---

## A. Positioning — 28세션 지식 아키텍처에서의 위치

**이전에 온 것**: I-01(CL·V·t½ — 1구획 IV 기하학)에서 $AUC = C_0/k$를 처음 만났고, I-03(F·KA·Tmax)에서 경구 투여 AUC를 다루었다. I-07(Michaelis-Menten)에서 비선형 PK의 AUC 개념이 등장한다.

**I-14의 위치**: Vol I 이론 세션의 '정산(reconciliation)' 지점이다. 모든 이론 세션(I-01~I-13)에서 등장한 PK 파라미터들이 실제 데이터에서 어떻게 측정되는지를 NCA가 통합한다.

**바로 다음에 오는 것**: I-15(TDM·모델 기반 용량관리) — NCA로 얻은 CL, Vd를 Bayesian 개인화 용량 계산의 사전 정보로 사용.

**결정적으로 의존하는 고급 도메인**:
- **PopPK** (II-07~II-08): NCA 파라미터가 공변량 탐색의 출발점 — 개인별 NCA-CL이 나이/신기능과 상관되는지 탐색
- **생물학적 동등성**: AUC와 Cmax의 NCA 추정이 BE 판정의 유일한 근거
- **TMDD** (I-08): NCA-CL이 용량 의존적으로 변할 때 TMDD 또는 MM PK 구분 필요

---

## B. Dependencies — 대충 넘겼을 때의 구체적 실패 모드

**실패 모드 1**: λz 추정 원칙 없이 "소프트웨어가 자동 계산해주는" 것에 의존하면, 2구획 약물의 α상 데이터가 λz 추정에 포함되어도 인지하지 못한다. 이 오류는 Vss 과소추정 → 로딩 용량 계산 오류 → 임상 실패로 연결된다.

**실패 모드 2**: MRT와 t½z를 혼용하면, 다구획 약물의 다중 투여 설계에서 축적 인자(accumulation factor = 1/(1-e^{-λz·τ}) 대신 1/(1-e^{-k_{el}·τ})를 잘못 사용하여 항정 상태 도달 예측을 오류 내게 된다.

---

## C. Professional Moat

NCA를 실행하고 CL, Vss, t½를 보고서에 기입하는 것은 WinNonlin이 0.1초 만에 한다. AI도 사다리꼴 합산을 즉시 수행한다.

이 세션의 원리를 구조적으로 내면화한 연구자만이 다음을 할 수 있다:

**용량-의존적 NCA 파라미터 변화의 기전 해석**: Turbojoint® PK41에서처럼 NCA-CL이 세 용량 수준에서 단조 감소할 때, 이것이 MM 포화 소실인지, 시간 의존적 자가 유도(autoinduction)인지, 아니면 샘플링 오류인지를 NCA 데이터 패턴만으로 가설을 세우고, 이를 검정할 MM ODE 모델의 초기 추정값 — $V_{max} \approx 184$ µg·h⁻¹·kg⁻¹, $K_m \approx 83$ µg·L⁻¹ — 을 두 연립 방정식(Eq. 41:3, 41:4)으로 손 계산하여 회귀분석에 즉시 넘길 수 있다. 이 계산은 알고리즘이 아니라, NCA와 모델 구조가 어떻게 연결되는지를 이해하는 사람만이 수행할 수 있는 판단이다.

---

✦ STEP 1 완료.

다음이 준비되었습니다:
- §1 세션 헤더 & 로드맵
- §2 개념 해부 카드 (4개 개념, Apex: λz — 말단 기울기 추정과 외삽 오차의 전파)
- §5 혼동 쌍 해부 (3개 쌍, Critical Blow 적용: Vss vs Vz)
- §7 자기 테스트 (8개 질문, 보스 딜레마 포함)
- §8 메타프레임 & 빅 픽처
- 감지된 소스 유형: Vol I — Gabrielsson 5e + R&T 5e 혼합
- Data Anchoring 소스: Turbojoint® (Gabrielsson PK41, pp.661-664) — 1명 피험자, 5h 정주, 3 용량(310/520/780 µg·kg⁻¹·70kg), NCA CL 1.6→0.9 L·h⁻¹·kg⁻¹; Zileuton (R&T App.A, Table A-2) — 600mg 경구, 0-24h 농도 데이터

"계속"을 입력하면 Step 2 HTML 컴파일러가 실행됩니다.
Step 2는 위 내용 전체(§1·§2·§5·§7·§8) + §3(구조적 동형성 지도: 적분을 이용한 파라미터 추출의 수학적 동형성) + §4(인터랙티브 NCA 시뮬레이터 — 사다리꼴 면적 실시간 계산, λz 구간 선택, AUC/MRT/Vss 자동 산출) + §6(실용 시나리오 & 진단 병리)를 단일 완성 HTML 파일로 통합합니다.

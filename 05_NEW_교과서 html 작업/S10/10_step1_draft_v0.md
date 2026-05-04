```
=== SCOPE LOCK ===
Source       : Gabrielsson & Weiner 5e (G&W) Ch.3 §3.1–3.6.1 + §3.6.6–3.6.7 + Case Study PD3
               + Rowland & Tozer 5e (R&T) Ch.8 "Response"
Pages        : G&W p.199–224 / p.229–234 / p.732–741  ;  R&T p.233–264
              ※ G&W §3.6.2–3.6.5 (pp.225–228) 첨부 PDF 부재 → 본 세션에서 [확인 필요 — 첨부 PDF 미포함 구간] 처리
Mode         : A-Critical (수식 도출 + 실험 데이터 앵커링 + 규제 파급력)
Image rights : None
Hybrid role  : G&W = 수식 도출 + 실험 데이터 앵커링 / R&T = 임상·생리학적 시간 해석
=================
```

---

# CURATION MAP — Master's Lens First

## MUST (체화 필수, §2 Concept Anatomy Card 부여)

| # | Concept | Source | 구조적 필연성 (Test) |
|---|---|---|---|
| **C1** | Law of Mass Action → Emax 골격 도출 | G&W §3.3 + §3.5.4 | C2 Sigmoid Emax 도출의 사전조건. 이 골격 없이는 Hill `n`의 메커니즘적 의미 해석 불가. |
| **C2** | **Sigmoid Emax / Hill model** [⚡ Apex Concept] | G&W §3.5.5 + PD3 | 이 챕터 전체의 정점. 이후 모든 indirect response·Effect Compartment 모델의 'output 함수'로 재등장. PD3 실측 추정 (E0=171, Imax=34.7, IC50=140, n=2.03) 직접 적용. |
| **C3** | Hysteresis — 시간 지연의 진단 도구 | R&T Ch.8 (digoxin, naproxen) | 농도-반응 관계의 시간 차원이 어떻게 시각화되는지 모르면 C4 Effect Compartment의 도입 동기를 이해할 수 없음. |
| **C4** | Effect Compartment + Direct / Indirect link + 간접반응 모델 골격 | R&T Ch.8 (warfarin, ibuprofen) | C3에서 진단된 hysteresis를 어떤 모델 구조로 흡수하는가의 직접 답. 후속 세션 kin/kout 모델의 진입로. |
| **C5** | AUEC + 효과 지속 시간 + PK / PD rate-limiting 이중성 | G&W §3.6.6–3.6.7 + R&T (succinylcholine, aspirin, omeprazole, paclitaxel) | "효과는 약물 반감기로 결정된다"는 가장 흔한 임상적 오해를 깨뜨리는 축. 아스피린 단회 → 며칠간 항혈소판, omeprazole 2시간 PK → 3일 효과. |

## CONTEXT (이해 보완, 1–2문장으로 MUST 카드 내 통합)

- **Linear / Log-linear effect models** (G&W §3.5.2–3.5.3) → C2 카드 도입부에 "Emax의 부분적 근사로 회귀" 형태로 흡수.
- **Saturation / Displacement binding 실험** (G&W §3.4, Cheng-Prusoff Eq.3:15) → C1 카드 한계(E)에 1문장 언급. Ki vs IC50 변환 의미만.
- **Spare receptor / Cascade effect** (G&W Eq.3:12, Fig.3.5–3.6) → C1 카드 한계(E)에 "EC50 ≪ Kd 발생 메커니즘"으로 흡수.
- **Composite Emax / Mixture dynamics** (G&W §3.5.6, Lundström 1992 데이터: IC50,1=1.8, IC50,2=23 µg·L⁻¹) → C2 카드 한계(E)에 "n이 1 미만일 때의 메커니즘적 단서"로 흡수.
- **Multiple binding site model** (G&W §3.5.7, Eq.3:48) → C2 카드 한계(E)에 "비단조 곡선 발생 조건"으로 1줄 흡수.
- **Competitive antagonism 시작부** (G&W §3.6.1) + **§3.6.2–3.6.5** → 본문에서 [확인 필요 — 첨부 PDF 미포함 구간]으로 명시. 추정·보완 금지.
- **PD3 통계 도구** (F-test, AIC, Δ-function, VIF, partial derivatives) → C2 카드 §F-L5(실무 투영)에 "model discrimination 무기고"로 1문장 압축.
- **Transporter polymorphism (rosuvastatin OATP1B1)** (R&T 후반) → C4 카드에 "site-of-action 농도와 plasma 농도의 분리"의 임상 사례로 1문장 흡수.
- **Methylprednisolone dose linearity 예시** (R&T) → C5 카드 도입부 Big Idea에 "PK 선형성 ≠ PD 선형성"의 핵심 증거로 1줄 흡수.

---

# §1 — Session Header & Roadmap

**Source 통합:** Gabrielsson & Weiner 5e Ch.3 (PD Concepts §3.1–3.6.1, 비평형 §3.6.6, AUEC §3.6.7) + Case Study PD3 + Rowland & Tozer 5e Ch.8 "Response"

**Big Idea (한 문장):**
> PD 모델링의 본질은 농도-효과 관계의 **비선형성(Emax / Hill `n`)**과 **시간 지연(hysteresis)**을 동시에 해부하는 것이며, 이 두 축이 만나는 지점에서 Sigmoid Emax 모델과 Indirect Response 모델이 탄생한다 — 둘을 분리하지 못하면 Phase 1 용량 예측에서 5–100배 오차가 발생한다.

**개념 항법도:**
- C1. Law of Mass Action → Emax 골격 (G&W §3.3, §3.5.4)
- C2. **Sigmoid Emax / Hill model** [⚡ Apex] (G&W §3.5.5, PD3 데이터)
- C3. Hysteresis — 시간 지연의 진단 (R&T Ch.8: digoxin, naproxen)
- C4. Effect Compartment + Indirect Response (R&T Ch.8: warfarin, ibuprofen)
- C5. AUEC + Duration + PK/PD rate-limiting (G&W §3.6.6–3.6.7 + R&T: succinylcholine, aspirin, omeprazole)

**지식 그래프 위치:**
- **선행 (전제):** PK 1구획·다구획 모델 (소실속도 K, t½), 평형/정상상태 개념, ODE 기초 (이전 세션 General ADVAN/$DES).
- **후속 (열어주는):** kin/kout 간접반응 모델 (build/loss-stim/inhib 4종), Effect Compartment 정식 ODE 형태, Tolerance / Receptor downregulation 모델, TMDD with target turnover (이전 I-08 세션 연계), PopPK/PD에서 IIV이 EC50 vs Emax 어디에 들어가야 하는가의 covariate 의사결정.

**이 챕터의 구조적 흐름:**
질량작용법칙(C1) → Emax 쌍곡선 → Hill `n` 도입으로 sigmoid 일반화(C2) → 평형 가정 깨기(C3 hysteresis) → Effect Compartment / Indirect Response로 시간 통합(C4) → 효과의 적분량(AUEC)과 지속 시간의 log-dose 의존성(C5).

---

# §2 — Concept Anatomy Cards

---

## Card C1 — Law of Mass Action → Emax 골격

<!-- MASTER LENS -->
### [개념 Big Idea: 거장의 시각]

**왜 치명적으로 중요한가:**
신약 후보의 in vitro Kd (radioligand binding)에서 in vivo EC50 (functional response)를 추정할 때, 두 값이 같다고 가정하면 FIH 용량이 5–100배 과추정될 수 있다. 그 차이를 만드는 것이 바로 이 카드에서 다루는 cascade effect와 spare receptor 메커니즘이다.

**체화해야 할 단 하나의 직관:**
수용체를 '결합 자리'로 보지 말고 **'신호 증폭기'**로 보라. Kd는 결합 강도의 직접 지표지만, EC50는 결합 → 자극(stimulus) → 효과로 이어지는 cascade 후의 '잔영'이다. 두 숫자가 다른 것은 결함이 아니라 시스템의 표준 동작 방식이다.

**이 직관을 머릿속에 박고 아래를 읽어라.** Emax 식이 왜 쌍곡선 형태일 수밖에 없는가는 평형 조건과 1:1 결합 가정에서 자동으로 따라온다.

<!-- ANCHOR -->
*평형 결합의 미시적 동역학(Eq.3:1)을 Eq.3:11까지 단계별로 외화하면, Emax 모델의 모든 파라미터가 어디서 유래했는지 하나하나 추적할 수 있다.*

### A. Formal Definition

평형 상태의 가역적 약물-수용체 결합 시스템에서, 관찰되는 약리 반응 $E$는 점유된 수용체 농도 $[RC]$에 비례한다(Ariens 1954 가정). 비례 상수 $\alpha$를 intrinsic activity라 하며, 모든 수용체가 점유될 때 $E_{max} = \alpha \cdot [R_T]$.

### B. Derivation (단계별 수식 도출)

**[Step 1] 평형 조건:**

$$
V_c \cdot \frac{d[RC]}{dt} = k_1 \cdot [R][C] - k_{-1} \cdot [RC] = 0
$$

평형에서 $d[RC]/dt = 0$ → $k_1[R][C] = k_{-1}[RC]$.

**[Step 2] 평형 해리상수 정의:**

$$
\frac{[C][R]}{[RC]} = \frac{k_{-1}}{k_1} = K_d
$$
*(작을수록 → 평형이 RC 쪽으로 이동 → 결합 강함)*

**[Step 3] 총 수용체 보존 ($[R_T] = [R] + [RC]$) 대입 후 정리:**

$$
\frac{[RC]}{[R_T]} = \frac{[C]}{[C] + K_d}
$$

이것이 receptor occupancy의 쌍곡선 형태. **단위 차원의 의미:** 분자에 $[C]$, 분모에 $[C] + K_d$ → 무차원 점유율. 분자가 증가해도 분모가 동시에 증가하므로 점유율은 1을 초과할 수 없다.

**[Step 4] Response = α · [RC], Emax = α · [R_T] 대입:**

$$
\boxed{\frac{E}{E_{max}} = \frac{[C]}{[C] + K_d}} \quad \text{또는} \quad E = \frac{E_{max} \cdot [C]}{[C] + K_d}
$$

`[출처: G&W 5e, Ch.3, p.203, Eq.3:8–3:10]`

**[Step 5] Functional response에서는 Kd 대신 EC50 사용:**

$$
E = \frac{E_{max} \cdot C}{EC_{50} + C}
$$

EC50는 in vivo 관찰된 half-max 농도. **EC50 ≠ Kd인 이유**는 cascade effect (Eq.3:12, Fig.3.5): receptor 점유의 작은 비율(예: 10%)이 cascade를 거쳐 거의 완전한 response(예: 90%)를 유발하므로, **EC50는 Kd보다 일반적으로 훨씬 작다**(Fig.3.4).

### C. Structural Necessity

쌍곡선 형태가 다른 형태(예: 선형, 지수)일 수 없는 이유:
1. **분자 $[C]$**: 점유는 자유 약물 농도에 1차 비례.
2. **분모 $[C] + K_d$**: 자유 receptor 보존에서 $[R] = [R_T] - [RC]$가 자동으로 들어감.
3. **포화 거동**: 분자/분모가 같은 차수 → 큰 C에서 1로 점근 → maximum effect 존재.

선형 가정은 $C \ll K_d$ 영역에서만 1차 근사로 성립 (`E ≈ Emax · C / Kd`). 이것이 G&W §3.5.2 linear effect 모델의 적용 범위 한계.

### D. Assumptions & Boundary Conditions

| 가정 | 위반 시 결과 |
|---|---|
| 가역적 1:1 결합 | 비가역 결합(예: omeprazole, aspirin) → 효과가 receptor turnover로 율속 (C5 참고) |
| 단일 receptor 부위 | 다중 부위 → composite Emax 또는 multiple binding site model 필요 (Eq.3:48) |
| 평형 도달 | 비평형 → kinetic-dynamic ODE 모델 필요 (§3.6.6) |
| Active metabolite 없음 | 활성 대사체 존재 → composite 모델 또는 metabolite kinetics 통합 필요 |
| Response ∝ [RC] | Cascade 증폭 → EC50 ≪ Kd, 직접 점유율 ≠ effect (Fig.3.5의 3단계 cascade) |

### E. Limitations

이 골격이 **실패하는** 지점:
1. **Spare receptor 시스템** (Fig.3.6): 점유율 40%에서 이미 max effect → EC50 ≪ Kd. 이 격차는 다음 수준의 모델(operational model of agonism, Eq.3:11 with intrinsic efficacy ε)에서 명시화됨.
2. **U-shaped / bell-shaped relationship** (Fig.3.21–3.22, Eq.3:43–3:44): 한 약물이 같은 시스템에서 agonist + antagonist 양면 작용. Composite Emax 모델 필요.
3. **다중 결합 부위** (Eq.3:48, caffeine brain concentration 예시): high concentration에서 effect 감소.
4. **비가역적 결합**: aspirin (cyclooxygenase 아세틸화), omeprazole (proton pump 공유 결합). 효과 지속이 약물 농도가 아닌 receptor 재합성에 율속 → C5 카드.
5. **Cheng-Prusoff 변환의 한계** (Eq.3:15, 3:16): displacement 실험에서 IC50 → Ki 변환은 radioligand 농도 [L]과 그것의 Kd를 알아야 하며, 이 둘이 부정확하면 Ki 추정이 함께 흔들림.

### F. Five Cognitive Layers

| Layer | 내용 |
|---|---|
| **L1 형식 수학** | Eq.3:1→3:10 단계별 유도, $K_d = k_{-1}/k_1$ 차원 분석 ($M^{-1}s^{-1} \cdot s = M$), 평형 조건의 ODE 영점화. |
| **L2 기하 직관** | $E$ vs $C$ 쌍곡선의 점근선($E \to E_{max}$), 변곡점의 부재(n=1), log-C 좌표에서의 sigmoid 외관(symmetric around log EC50). |
| **L3 구조 동일성** | Michaelis-Menten ($V = V_{max}S/(K_m+S)$)과 1:1 동형. Langmuir 흡착 등온식과도 동형. 모두 "단일 자리 평형 점유"의 보편 형태. |
| **L4 생리학 의미** | Kd는 한 receptor-ligand 쌍의 화학; EC50는 그 receptor가 속한 시스템의 amplification까지 포함한 phenotype. 종간 차이의 일부는 amplification 차이로 흡수. |
| **L5 실무 투영** | NONMEM에서 `EMAX*C/(EC50+C)` 한 줄 코드. PopPK/PD에서 EC50가 covariate sensitive 한 이유는 이것이 system parameter (Emax도 마찬가지)이기 때문. Pure drug parameter는 Kd와 ε. |

### G. Zettelkasten Atom

```yaml
---
aliases: [Mass Action, Receptor Occupancy, Emax Foundation, Hyperbolic Binding]
tags: [pharmacometrics/pd, theory/equilibrium, derivation/emax]
up: "[[PD 모델 계보 MOC]]"
related: ["[[Sigmoid Emax C2]]", "[[Cascade Effect]]", "[[Spare Receptors]]", "[[Cheng-Prusoff Equation]]"]
source: "Gabrielsson & Weiner 5e, Ch.3 §3.3 + §3.5.4, p.202–215"
---
```

> Receptor occupancy는 평형 조건에서 단일 부위 1:1 결합의 보존식을 풀면 자동으로 쌍곡선 $[C]/([C]+K_d)$ 형태로 도출된다. Functional response는 점유율에 cascade amplification이 곱해진 결과이므로 EC50는 일반적으로 Kd보다 훨씬 작고, 두 값을 동일시하는 것은 spare receptor 시스템에서 FIH 용량을 5–100배 과추정하는 직접적 원인이다. 이 골격이 깨지는 지점(비가역 결합, multiple sites, U-shape)은 모두 후속 모델 계보의 출발점이 된다.

---

## Card C2 — **Sigmoid Emax / Hill Model** [⚡ Apex Concept]

<!-- MASTER LENS -->
### [개념 Big Idea: 거장의 시각]

**왜 치명적으로 중요한가:**
Hill coefficient `n`은 단순한 fitting parameter가 아니다. **이 한 숫자가 약물의 therapeutic window 폭을 결정한다.** n=1 (ordinary Emax): 농도가 10배 변하면 effect는 약 9배 → 완만한 dose titration 가능. n=4 (steep sigmoid): 농도가 2배만 변해도 20%→80% effect로 점프 → all-or-nothing 거동, 좁은 안전 마진. PD3 사례에서 ordinary와 sigmoid를 잘못 선택하면 IC50 추정이 175 vs 140 (25% 편향), Imax 추정이 49.8 vs 34.7 (43% 편향)로 갈라진다. 이 편향이 그대로 NDA 권장 용량에 들어간다.

**체화해야 할 단 하나의 직관:**
n을 '곡선의 기울기'가 아니라 **'시스템의 위상 게이트키퍼'**로 보라. n>1: cooperativity 또는 cascade 증폭이 작동 중이라는 메커니즘적 신호. n<1: 다중 결합 부위 또는 활성 대사체의 흔적. n=1: ordinary Emax의 특수해(받아들이지 말 것 — 가설로서만 검증).

**이 직관을 머릿속에 박고 아래를 읽어라.** 도출의 모든 단계에서 n이 어떻게 들어가고 빠지는지 추적하라.

<!-- ANCHOR -->
*Ordinary Emax(C1)의 분자/분모 양쪽에 같은 지수 n을 붙이는 행위는 단순 일반화로 보이지만, 그것이 PD3에서 모델 식별성과 추정 정밀도 전체를 뒤흔든다.*

### A. Formal Definition

Sigmoid Emax 모델 (Hill equation, Hill 1910):

$$
E = \frac{E_{max} \cdot C^n}{EC_{50}^n + C^n}
$$

baseline 포함 형태:

$$
E = E_0 + \frac{E_{max} \cdot C^n}{EC_{50}^n + C^n} \quad (\text{stim}) \qquad
E = E_0 - \frac{I_{max} \cdot C^n}{IC_{50}^n + C^n} \quad (\text{inhib})
$$

`[출처: G&W 5e, Ch.3, p.216, Eq.3:32 / p.218, Eq.3:34–3:35]`

여기서 $n$ = Hill coefficient (sigmoidicity factor). $n=1$일 때 ordinary Emax로 수렴.

### B. Derivation & Initial Estimate Recovery

**[Step 1] 도함수 dE/d(ln C) 계산** — 그래픽 추정의 근거:

$\ln(C)$로 놓고 $E = E_0 + E_{max} \cdot e^{n \ln C} / (EC_{50}^n + e^{n \ln C})$ 미분:

$$
\frac{dE}{d \ln C} = \frac{n \cdot E_{max} \cdot EC_{50}^n \cdot C^n}{(EC_{50}^n + C^n)^2}
$$

**[Step 2] $C = EC_{50}$에서의 slope (변곡점 기울기):**

$$
m = \left.\frac{dE}{d \ln C}\right|_{C=EC_{50}} = \frac{n \cdot E_{max} \cdot EC_{50}^{2n}}{(2 EC_{50}^n)^2} = \frac{n \cdot E_{max}}{4}
$$

따라서:

$$
\boxed{n = \frac{4m}{E_{max}}}
$$

`[출처: G&W 5e, Ch.3, p.219, Eq.3:38–3:40]`

이것이 Levy(1995) 그래픽 초기 추정의 핵심: 20–80% effect 영역에서 $E$ vs $\ln C$ plot의 접선 기울기 $m$을 자로 재고, $E_{max}$ 추정치로 나누면 $n$이 즉시 나온다.

**[Step 3] 외삽으로 $C_0$ (intercept) 회수:**

$$
C_0 = EC_{50} \cdot e^{-2/n}
$$

`[출처: G&W 5e, Ch.3, p.219, Eq.3:42]`

### C. Structural Necessity

**왜 분자와 분모의 C에 같은 지수 n이 붙는가?** Ordinary Emax(C1)의 평형 도출은 단일 부위 1:1 결합을 가정했다. n>1을 정당화하는 메커니즘:
1. **Positive cooperativity** (Hill 1910 hemoglobin–O2): n개 ligand가 함께 결합하지 않으면 효과 없음. → "n번째 결합이 안 되면 점유 무효" 라는 강한 가정.
2. **Cascade amplification** (G&W Fig.3.5): 결합 → stimulus 1 → stimulus 2 → response 3단계 hyperbolic 곱 → 합성 곡선의 sharper steepness. n은 cooperativity가 아닌 amplification depth의 지표가 됨.
3. **Receptor heterogeneity** (n<1): 친화도가 다른 두 결합 부위 → composite 곡선이 평탄해 보임.

**왜 unbound 농도에서 n이 보존되는가?** Eq.3:33 도출:
$$
E = \frac{E_{max} \cdot C^n}{EC_{50}^n + C^n} = \frac{E_{max}(C_u/f_u)^n}{(EC_{50}/f_u)^n + (C_u/f_u)^n} = \frac{E_{max} \cdot C_u^n}{EC_{u50}^n + C_u^n}
$$
$f_u^n$이 분자/분모에서 약분된다. 단, $n$이 total plasma concentration에서 추정된 값이라면 단백 결합 변동에 의해 인공적으로 영향받을 수 있음 — 종간 비교에는 unbound 권장.

<!-- TRENCH -->
**[Trench-Level Tip — 모델 빌더의 자):** Hill `n`을 NONMEM에서 추정할 때, 데이터의 noise level이 5%(CV)를 넘으면 `n`의 정밀도가 50% 이상으로 폭발한다 (PD3 Table 3.3 Simulation 결과). 이런 데이터에서는 `n`을 1로 fix하고 ordinary Emax로 진행하거나, 다른 연구의 prior로 `n`을 외부 고정하는 것이 더 robust하다. Sandwich estimator나 bootstrap으로 `n`의 신뢰구간을 반드시 확인할 것.

### C-2 [⚡ Apex Concept] Plausible Fallacy: "Curvature Suppression"

**그럴싸한 오류:**
> "데이터가 약간 sigmoidal하지만 ordinary Imax 모델로도 fit이 그럭저럭 나온다. 모델은 단순할수록 좋으니 n=1로 진행한다."

**나비효과 추적 (PD3 실측):**
G&W PD3 (혈압 강하, 0–800 µg·L⁻¹ 범위, n=10 데이터 포인트):

| Parameter | Ordinary Imax (n=1 고정) | Sigmoid Imax (n 추정) | 편향 |
|---|---|---|---|
| Imax (mm Hg) | 49.8 ± 8% | **34.7 ± 10%** | +43% 과추정 |
| IC50 (µg·L⁻¹) | 175 ± 31% | **140 ± 11%** | +25% 과추정 |
| n | (1) | 2.03 ± 21% | — |
| E0 (mm Hg) | 177 ± 2% | 171 ± 1% | +3.5% |
| AIC | 50.8 | **45.6** | sigmoid 우위 |

`[출처: G&W 5e, PD3, p.735, Table 3.2]`

**기계론적 추적:**
- Imax 과추정 → "이 약물은 혈압을 50 mm Hg 낮출 수 있다"는 잘못된 efficacy 주장
- IC50 과추정 → "치료역 농도가 175 µg·L⁻¹ 이상 필요"라는 잘못된 dosing 권장 (실제는 140이면 충분)
- 두 오차가 합쳐져 임상 시험에서 2x 더 높은 용량을 시도 → 부작용 빈도 증가

**진단 시그니처 — "Curvature Suppression":**
GOF 플롯에서 ordinary Imax fit의 잔차가 농도 축에 대해 **체계적 패턴(0–100 µg·L⁻¹에서 양수, 100–300에서 음수, 300+ 에서 양수)**을 보임 (PD3 Fig.3.3 빨간 선). 이런 잔차의 amplitude가 sigmoid fit의 거의 4배. 진정한 random 잔차는 평탄해야 한다.

**해결: F-test 적용 (PD3 Eq.3:3):**
$$
F^* = \frac{|WRSS_1 - WRSS_2|/|df_1 - df_2|}{WRSS_2/df_2}
$$
PD3 0–800 µg·L⁻¹ 데이터: $F^* = 6.47 > F_{table}(1,7,0.05) = 5.59$. → sigmoid가 통계적으로 우위. 단, 0–500 µg·L⁻¹만 사용 시 $F^* = 3.53 < 5.99$ → 결정 불가. **즉, 데이터의 농도 범위가 IC50의 4–5배까지 확장되지 않으면 n을 식별할 수 없다.** 이것이 PD3 §"Delta function"이 가르치는 design 통찰 — 70 µg·L⁻¹, 275 µg·L⁻¹, 800 µg·L⁻¹ 부근 sample이 모델 구분에 결정적.

### D. Assumptions & Boundary Conditions

| 가정 | 위반 시 결과 |
|---|---|
| 단일 메커니즘 (cooperativity OR cascade OR multiple sites 중 하나) | 두 메커니즘 혼재 시 n이 시간/조건에 따라 변동 |
| Concentration range가 0–EC50의 5x 이상 커버 | 좁은 범위 → n과 Emax 강한 상관 → 식별 불가 |
| Noise level CV ≤ 3% | 5% 초과 시 n 정밀도 폭발 (PD3 Table 3.3) |
| Baseline E0 시간 불변 | 시간 변동 시 baseline model 결합 필요 (G&W §3.12 [확인 필요 — 첨부 PDF 미포함 구간]) |

### E. Limitations

1. **메커니즘 불명확성:** n이 1.4라고 해서 그것이 cooperativity인지 cascade인지 다중부위 평균인지 식별할 수 없음. 외부 in vitro binding 실험 필요.
2. **단백 결합 영향:** total C 기준 n은 fu 변동에 인공적 sensitivity. unbound 권장.
3. **U-shape / bell-shape는 표현 불가:** Composite Emax 필요 (G&W §3.5.6). Lundström(1992) 데이터: IC50,1=1.8, IC50,2=23 µg·L⁻¹; Imax,1=4, Imax,2=3.2; n1=1.4, n2=3.7 — 두 phase가 분명히 분리될 때만 추정 가능.
4. **시간 차원 부재:** 평형 가정이 깨지면(C3 hysteresis) 즉시 ODE 형태로 확장 필요(C4).

### F. Five Cognitive Layers

| Layer | 내용 |
|---|---|
| **L1 형식 수학** | Eq.3:32 도출, dE/dlnC 계산, n = 4m/Emax 그래픽 회수, target concentration 모델 (Table 3.1: $C_T = EC_{50}\sqrt[n]{(E_T-E_0)/(E_0+E_{max}-E_T)}$) |
| **L2 기하 직관** | Log-C plot에서 inflection symmetric, n→∞ 극한은 step function (all-or-nothing), n→0 극한은 거의 평탄. 20–80% range가 항상 ln(EC50)을 중심으로 (4/n) 폭. |
| **L3 구조 동일성** | Allosteric enzyme kinetics (Monod-Wyman-Changeux), oxygen-hemoglobin Hill 1910, voltage-gated ion channel activation, dose-response curve in epidemiology. 모두 "cooperative threshold passing"의 보편 형태. |
| **L4 생리학 의미** | n=1: 단순 receptor occupancy. n>1: cascade가 작동 중이라는 직접적 증거. n<1: 활성 metabolite 또는 multiple receptor의 신호. 예: 2-3은 효소-기질 cooperativity, 4 이상은 cascade 또는 voltage-gated 채널의 4-subunit cooperativity. |
| **L5 실무 투영** | NONMEM `EMAX*C**HILL/(EC50**HILL+C**HILL)`. PopPK/PD에서 IIV 부여 시 EC50와 Emax 우선, n에 IIV 부여는 데이터가 매우 풍부할 때만. Initial estimate은 Levy(1995) graphical method. Model discrimination: F-test, AIC, residual pattern (PD3 §"Interpretation"). |

### G. Zettelkasten Atom

```yaml
---
aliases: [Hill Equation, Sigmoid Emax, Hill Coefficient, Sigmoidicity Factor]
tags: [pharmacometrics/pd, model/sigmoid, apex-concept]
up: "[[PD 모델 계보 MOC]]"
related: ["[[Mass Action C1]]", "[[Cascade Effect]]", "[[Cooperativity]]", "[[Composite Emax]]", "[[Indirect Response C4]]"]
source: "Gabrielsson & Weiner 5e, Ch.3 §3.5.5, p.216–220 + Case Study PD3, p.732–741"
---
```

> Hill 모델은 ordinary Emax의 분자/분모 양쪽에 같은 지수 n을 붙인 일반화이며, n은 cooperativity·cascade·multiple sites 중 어느 하나의 메커니즘적 흔적이다. PD3 사례에서 ordinary와 sigmoid를 잘못 선택하면 IC50/Imax 추정이 25–43% 편향되어 그대로 NDA 권장 용량에 들어간다. n의 식별을 위해서는 농도 범위가 IC50의 4–5배까지 확장되어야 하며, noise level CV가 5%를 초과하면 n의 정밀도가 50% 이상으로 폭발한다. 데이터가 빈약하면 n을 1로 fix하고 외부 prior를 사용하는 것이 더 robust하다.

<!-- RECAP -->
*C1–C2까지: 평형 가정 하에서 농도-효과 관계의 비선형성을 어떻게 형식화하는가. 이제 평형 가정 자체가 깨지는 영역으로 들어간다 — 시간 차원의 도입.*

---

## Card C3 — Hysteresis: 시간 지연의 진단 도구

<!-- MASTER LENS -->
### [개념 Big Idea: 거장의 시각]

**왜 치명적으로 중요한가:**
Digoxin 1 mg iv 투여 후 처음 4시간 동안 plasma 농도가 떨어지면서 left ventricular ejection-time index가 **상승**한다 (Shapiro 1970, R&T Fig.8-1). 이 데이터를 그대로 plasma C-E curve로 그리면 "농도가 낮을수록 효과가 크다"는 부조리한 결론에 도달한다. 이것은 약리학적 paradox가 아니라 진단 신호 — **분포 평형이 아직 도달되지 않았다**는 것이다. 이 신호를 무시하고 plasma TDM을 기반으로 용량 결정을 내리면, digoxin은 6시간 distribution equilibrium 도달 전에 추가 투여되어 심독성을 일으킨다.

**체화해야 할 단 하나의 직관:**
히스테리시스를 **'잘못된 모델의 잔재'가 아니라 '시간 지연의 직접 가시화'**로 보라. 반시계 방향(counterclockwise) loop는 "효과가 농도보다 늦다"는 명시적 증거이고, 그 원인이 분포 지연인지 시스템 동역학인지를 구별하는 것이 모델 빌더의 첫 임무다.

**이 직관을 머릿속에 박고 아래를 읽어라.**

<!-- ANCHOR -->
*평형 가정(C1, C2)이 깨질 때 가장 먼저 나타나는 데이터의 표현형이 hysteresis loop이며, 그 모양이 다음 카드(C4)의 모델 선택을 결정한다.*

### A. Formal Definition

**Hysteresis (이력현상):** Plasma 농도 $C(t)$와 response $E(t)$를 시간을 매개변수로 하여 $E$ vs $C$ 평면에 plot했을 때, 농도 상승 구간과 하강 구간이 **다른 경로**를 따르는 현상.

- **Counterclockwise hysteresis (반시계방향):** 같은 농도에서 상승 구간 < 하강 구간의 effect. → 효과가 농도보다 **늦다**.
- **Clockwise hysteresis (시계방향):** 같은 농도에서 상승 구간 > 하강 구간의 effect. → tolerance, downregulation, 또는 active metabolite 소실 (이 챕터 범위 외, Vol II).

### B. Derivation: 검출 로직

**iv bolus 후:** $C(t)$는 단조 감소. 시간 진행과 함께 $C$가 단조 감소하므로 hysteresis 자체는 검출 안 됨. 그러나 effect가 즉각이 아니면 $E$ vs $\ln C$ plot에서 변곡점이 늦게 나타남 → 시간 지연 시그니처 (R&T Fig.8-1 digoxin).

**Extravascular dose 후:** $C(t)$가 상승 후 하강 (Cmax 정점). 같은 $C$ 값을 두 번 통과 → 두 시점의 $E$ 비교 가능 → hysteresis loop 직접 가시화 (R&T Fig.8-2 naproxen).

**Naproxen 500 mg PO (R&T Fig.8-2, dental pain 모델):**
- 시점 1 (1h): unbound C ≈ 8 µg/L, pain relief ≈ 0.15
- 시점 4 (3h): unbound C ≈ 43 µg/L, pain relief ≈ 1.0
- 시점 8 (8h): unbound C ≈ 18 µg/L, pain relief ≈ 0.85
- → Counterclockwise loop

### C. Structural Necessity

Hysteresis가 발생하는 **물리적 이유** 3가지:
1. **분포 지연 (tissue distribution lag):** Site of action에 도달하는 데 시간 필요. plasma → effect site 전이 속도 상수 $k_{e0}$로 표현됨 (C4).
2. **System dynamics (turnover lag):** Effect가 endogenous substance의 turnover에 의존 (warfarin → prothrombin complex; ibuprofen → body heat dissipation).
3. **Active metabolite 누적:** Parent drug 농도와 다른 시간 패턴.

**각 원인의 추가 진단 방법:**
- 1번이면 effect compartment ($k_{e0}$) 추정으로 hysteresis 사라짐 (R&T Fig.8-14 naproxen).
- 2번이면 effect compartment로도 사라지지 않고 indirect response 모델 필요 (R&T Fig.8-10 warfarin).
- 3번이면 metabolite kinetics 측정 필요.

### D. Assumptions & Boundary Conditions

| 가정 | 위반 시 결과 |
|---|---|
| Plasma C가 site of action C와 비례 | 비례하지 않으면 hysteresis 외에 추가 비선형성 |
| Effect 측정 시간 해상도 충분 | 분 단위 변화를 시간 단위로 측정하면 hysteresis 시각화 실패 |
| Single dose protocol | 반복투여에서는 tolerance/induction 같은 다른 시간 효과와 혼합 |

### E. Limitations

- **시간 해상도 한계:** Ibuprofen (R&T Fig.8-9) 데이터에서 20분 간격 측정. 더 짧은 시간 구조는 보이지 않음.
- **임상에서 hysteresis 검출 자체가 어려움:** Routine TDM은 한 시점만 측정. PK/PD 연구 프로토콜에서만 dense sampling 가능.
- **Pseudo-hysteresis:** Measurement error나 baseline drift가 hysteresis처럼 보일 수 있음. 통계적 검증 필요.

### F. Five Cognitive Layers

| Layer | 내용 |
|---|---|
| **L1 수학** | $E(t) = f(C(t-\tau))$ 형태의 시간 지연. effect compartment에서 $dC_e/dt = k_{e0}(C_p - C_e)$. |
| **L2 기하** | $E$ vs $C$ 평면의 phase portrait. Loop의 폭이 시간 지연 척도. Loop 사라짐이 모델 적합 검증. |
| **L3 동일성** | 전기회로 RC 지연, 열역학 hysteresis (자기장-자화), 인구 동역학 lag. 모두 "input-output 사이의 integrating capacitor" 메커니즘. |
| **L4 생리학** | Counterclockwise = 시스템이 cause를 따라가지 못함 (저주파 응답). Digoxin: 심근 내 receptor 결합. Warfarin: 응고 인자 turnover. Ibuprofen: 체열 dissipation. |
| **L5 실무** | NONMEM에서 $K_{e0}$ 추정으로 hysteresis 제거 → unified C-E relationship 회복. PopPK/PD model building 워크플로의 진단 단계. |

### G. Zettelkasten Atom

```yaml
---
aliases: [Hysteresis, Counterclockwise Loop, Time Delay Signature]
tags: [pharmacometrics/pd, diagnostic/time-delay]
up: "[[PD 모델 계보 MOC]]"
related: ["[[Effect Compartment C4]]", "[[Indirect Response]]", "[[Direct Link]]"]
source: "Rowland & Tozer 5e, Ch.8, p.234–238"
---
```

> Hysteresis loop는 농도-효과 관계가 시간에 따라 다른 경로를 그리는 현상이며, counterclockwise loop는 효과가 농도보다 시간적으로 늦다는 명시적 증거다. 원인은 (1) 분포 지연, (2) 시스템 동역학, (3) 활성 대사체 셋 중 하나이며, 각각 effect compartment, indirect response, metabolite kinetics 모델로 흡수된다. Plasma TDM만으로 dose 결정을 내리기 전에 반드시 검출해야 하는 패턴이다.

---

## Card C4 — Effect Compartment + Direct/Indirect Link + Indirect Response 골격

<!-- MASTER LENS -->
### [개념 Big Idea: 거장의 시각]

**왜 치명적으로 중요한가:**
Warfarin 1.5 mg/kg PO 후 plasma 농도는 30시간 안에 거의 0으로 떨어지지만, prothrombin complex activity는 5일이 지나야 baseline에 복귀한다 (Nagashima 1969, R&T Fig.8-10). "Plasma 농도가 0이 됐으니 효과도 끝났을 것"이라고 가정하고 추가 warfarin을 투여하면 출혈 위험이 누적된다. 또 다른 사례: Acenocoumarol (t½=15h) vs Phenprocoumon (t½=5d). 두 약 모두 같은 prothrombin 합성 억제로 작동하지만, baseline 복귀 시간이 3일 vs 2주로 6배 차이 (R&T Fig.8-11). **이 차이는 PK가 결정하는가, PD가 결정하는가?** 답은 둘 중 더 느린 쪽이 율속한다(C5에서 일반화).

**체화해야 할 단 하나의 직관:**
Effect compartment ($C_e$)는 가상의 box가 아니라 **'관찰되지 않는 site of action 평형의 그림자'**다. $k_{e0}$는 분포 지연을 흡수하는 단일 파라미터. 한편 Indirect response 모델은 한 단계 더 나아가 **'효과 자체가 turnover 시스템'**인 경우 — 약물은 input/output rate를 modulate하고, 측정되는 effect는 그 시스템의 현재 상태.

**이 직관을 머릿속에 박고 아래를 읽어라.**

<!-- ANCHOR -->
*C3에서 진단된 hysteresis를 어떻게 모델 구조로 흡수하는가의 직접 답이 이 카드. 분포 지연 → effect compartment, 시스템 동역학 → indirect response.*

### A. Formal Definition

**Direct link (즉각 PK-PD link):**
$E(t) = f(C_p(t))$. 농도-시간 곡선의 maximum과 effect-시간 곡선의 maximum이 동시. log-linear 관계 사용 시 effect는 **zero-order로 감소** (R&T Eq.8-1~8-3, midazolam Fig.8-6 예시).

**Indirect link via Effect Compartment:**

$$
\frac{dC_e}{dt} = k_{e0}(C_p - C_e), \qquad E(t) = f(C_e(t))
$$

`[출처: R&T 5e, Ch.8, p.245–246, Fig.8-13]`

$k_{e0}$는 effect compartment의 first-order 평형 상수. 추정 후 $E$ vs $C_e$ plot이 hysteresis-free → C2 sigmoid Emax로 직접 fit 가능. Naproxen 사례 (R&T Fig.8-14): $C_e$ 변환 후 hysteresis 완전 소실.

**Indirect Response Model (4가지 표준형):**

기본 turnover 식 (R&T Eq.8-5, Eq.8-6):
$$
\frac{dA}{dt} = R_{syn} - k_t \cdot A
$$

약물 작용 위치에 따라 4가지:
1. **Inhibition of synthesis (input):** $R_{syn} \to R_{syn}(1 - I_{max} C^n / (IC_{50}^n + C^n))$ — warfarin
2. **Stimulation of synthesis (input):** $R_{syn} \to R_{syn}(1 + E_{max} C^n / (EC_{50}^n + C^n))$
3. **Inhibition of degradation (output):** $k_t \to k_t(1 - I_{max} C^n / (IC_{50}^n + C^n))$
4. **Stimulation of degradation (output):** $k_t \to k_t(1 + E_{max} C^n / (EC_{50}^n + C^n))$

### B. Derivation: Warfarin Indirect Response 사례

R&T Eq.8-6:
$$
\frac{dA}{dt} = R_{syn} - k_t \cdot A
$$

**[Step 1] Blocking dose 실험으로 $k_t$ 분리:**
1.5 mg/kg PO sodium warfarin → 처음 48시간 동안 $R_{syn} \approx 0$ (완전 차단) → $A(t) = A_0 e^{-k_t t}$ → semilog plot의 기울기로 $k_t$ 직접 측정. **Prothrombin complex의 $k_t \approx 0.5$ day⁻¹** ($t_{1/2} \approx 1.5$ day).

`[출처: R&T 5e, Ch.8, p.247, Fig.8-15]`

**[Step 2] 회복 단계의 $R_{syn}(t)$ 회수 (Eq.8-7):**
$A_1, A_2$를 $\Delta t$ 간격으로 측정:
$$
R_{syn}(t) = \frac{A_2 - A_1}{\Delta t} + k_t \cdot \frac{A_1 + A_2}{2}
$$

**[Step 3] 억제율 계산 (Eq.8-8):**
$$
\% \text{ inhibition} = 100 \cdot \frac{R_{syn(n)} - R_{syn}(t)}{R_{syn(n)}}
$$
$R_{syn(n)} = k_t \cdot A_{(n)}$ (정상 baseline 합성률).

**[Step 4] 억제율 vs warfarin plasma C의 관계:**
$\ln C$ vs % inhibition plot이 직선 (R&T Fig.8-16) → log-linear effect 또는 Hill model fit.

### C. Structural Necessity

**왜 effect compartment는 minimal 1-parameter 확장으로 충분한가?**
- 가장 단순한 시간 지연 표현: 1차 distribution kinetics.
- $k_{e0}$ 하나만으로 분포 지연을 흡수.
- 더 복잡한 multi-compartment site-of-action 모델은 over-parametrization 위험.

**왜 indirect response는 turnover 가정이 필수인가?**
- Steady-state 시스템(blood pressure, heart rate, hormone levels)의 본질적 구조: rate of input = rate of output.
- 약물이 어느 한쪽을 modulate해야 시스템이 새로운 steady-state로 이동.
- $k_t$는 system-specific (drug-independent) → 다른 약물도 같은 $k_t$ 공유 (warfarin과 acenocoumarol이 같은 prothrombin turnover 공유).

### D. Assumptions

| 모델 | 핵심 가정 | 위반 시 |
|---|---|---|
| Effect Compartment | Site-of-action concentration이 single 1차 distribution으로 plasma와 평형 | Multi-compartment site → biphasic delay |
| Indirect Response | $R_{syn}$ 또는 $k_t$ 중 하나만 약물 modulation, 다른 하나는 시간 불변 | Drug-induced enzyme induction → 시간 변동 |
| 모두 | $E_0$ baseline 시간 불변 | Disease progression → baseline drift |

### E. Limitations

1. **$k_{e0}$의 식별성 (identifiability):** Plasma kinetics와 effect kinetics의 시간 척도가 비슷하면 $k_{e0}$와 $k$ 강한 상관 → 추정 정밀도 낮음 (Trench-Level Tip 카드 C2 참고).
2. **Indirect response의 4가지 형태 구분 어려움:** 단회 투여 데이터만으로는 input vs output 구분 거의 불가. Multiple dose levels 필요.
3. **$k_t$ 추정의 ethical issue:** Blocking dose 실험은 normal subject에서만 가능 (overdose 위험). Patient에서는 prior에 의존.
4. **Transporter polymorphism (rosuvastatin OATP1B1 사례):** Plasma C와 site-of-action C의 비례 관계 자체가 깨진다 — TT/TC/CC genotype에서 plasma AUC가 +63%, +111% 다르지만 PD response (mevalonic acid 감소)는 거의 동일 (3–6%). Bioequivalence 가정에 직접 충격.

### F. Five Cognitive Layers

| Layer | 내용 |
|---|---|
| **L1 수학** | Effect compartment ODE, indirect response 4종 ODE, blocking dose에서 $k_t$ 분리, 회복 구간에서 $R_{syn}(t)$ 회수. |
| **L2 기하** | Hysteresis loop가 $C_e$ 변환 후 직선으로 collapse (Fig.8-14). Indirect response의 dose-response peak 시간이 dose 무관 (warfarin은 모든 dose에서 36-48h에 peak). |
| **L3 동일성** | RC 회로 (effect compartment ↔ low-pass filter), heated room (body heat ibuprofen 예시 Eq.8-4), 인구 동역학 (birth-death model = synthesis-degradation), bank account (deposit-withdrawal). |
| **L4 생리학** | Effect compartment = brain ↔ blood-brain barrier transit (e.g., midazolam, opioids). Indirect response = endogenous turnover system (clotting factors, hormones, blood cells). |
| **L5 실무** | NONMEM `\$DES` 블록에서 effect compartment 추가 ODE 한 줄, 또는 indirect response의 4가지 표준 코드. PopPK/PD 빌딩의 표준 워크플로. ke0 추정 시 grid search로 식별성 확인. |

### G. Zettelkasten Atom

```yaml
---
aliases: [Effect Compartment, Hypothetical Effect Site, Indirect Response Model, Turnover Model, ke0]
tags: [pharmacometrics/pd, model/time-delay, model/turnover]
up: "[[PD 모델 계보 MOC]]"
related: ["[[Hysteresis C3]]", "[[Sigmoid Emax C2]]", "[[Warfarin Case]]", "[[kin-kout Model]]"]
source: "Rowland & Tozer 5e, Ch.8, p.245–248"
---
```

> Effect compartment ($k_{e0}$)는 분포 지연 hysteresis를 단일 파라미터로 흡수하여 site-of-action 농도와 effect 사이의 직접 관계를 회복시킨다. Indirect response 모델은 effect 자체가 turnover 시스템(synthesis-degradation balance)인 경우 약물이 input 또는 output rate를 modulate한다는 4가지 표준형으로 구분되며, $k_t$는 system parameter (warfarin과 acenocoumarol이 prothrombin turnover를 공유). 이 모델 계보가 Vol II의 kin/kout 표준 코드와 직접 연결된다.

<!-- RECAP -->
*C3–C4까지: 시간 지연을 어떻게 진단하고 모델 구조로 흡수하는가. 이제 효과의 적분량과 지속 시간으로 이동.*

---

## Card C5 — AUEC + Duration + PK/PD Rate-Limiting

<!-- MASTER LENS -->
### [개념 Big Idea: 거장의 시각]

**왜 치명적으로 중요한가:**
Methylprednisolone 16 mg부터 1000 mg까지 7개 dose에서 plasma AUC는 정확히 dose-proportional (R&T Fig.8-26). 그러나 lymphocyte count 감소 response는 250 mg에서 1000 mg까지 거의 동일 (R&T Fig.8-27) — 4배 dose 증가가 거의 같은 effect를 produce. **PK 선형성은 PD 선형성을 보장하지 않는다.** 더 극단적: Aspirin 650 mg PO → t½ = 15분, 2시간 안에 거의 전부 elimination. 그런데 platelet thromboxane B2 inhibition은 며칠 지속 (R&T Fig.8-20). 만약 의사가 "약이 몸에 없으니 효과도 없다"고 판단하면, 수술 전 7일 aspirin 중단 권고를 5일로 줄여 perioperative bleeding이 발생한다.

**체화해야 할 단 하나의 직관:**
효과 지속 시간은 '약이 몸에 얼마나 남아있나'가 아니라 **'시스템이 얼마나 빠르게 회복하나'**에 의해 결정될 수 있다. **PK rate-limited (succinylcholine, propranolol)** vs **PD rate-limited (aspirin, omeprazole, warfarin)** — 둘 중 **더 느린 쪽이 율속**한다. 이 이중성은 covalent binding, receptor turnover, target system turnover 같은 메커니즘에서 출현한다.

**이 직관을 머릿속에 박고 아래를 읽어라.**

<!-- ANCHOR -->
*C2 Sigmoid Emax + C4 indirect response의 시간 통합이 효과의 적분량(AUEC)과 지속 시간 표현으로 이어진다.*

### A. Formal Definition

**Area Under the Effect Curve (AUEC):** Effect-time curve의 적분.

$$
AUC_E = \int_0^\infty E \, dt
$$

1구획 iv bolus에 ordinary Emax를 적용한 단힌 형태 (G&W Eq.3:73):

$$
\boxed{AUC_E = \frac{E_{max}}{K} \cdot \ln\left(1 + \frac{D}{EC_{50} \cdot V}\right) = \frac{E_{max}}{K} \cdot \ln\left(1 + \frac{C_0}{EC_{50}}\right)}
$$

`[출처: G&W 5e, Ch.3, p.233, Eq.3:73]`

**Duration of Effect ($t_D$):** Effect가 minimum effective level $C_{min}$ 이상으로 유지되는 시간. 1구획 iv bolus + plasma C가 PD를 직접 driving하는 경우 (R&T Eq.8-12):

$$
\boxed{t_D = \frac{1}{K} \ln\left(\frac{Dose}{C_{min} \cdot V}\right) = \frac{1}{K} \ln\left(\frac{Dose}{A_{min}}\right)}
$$

`[출처: R&T 5e, Ch.8, p.254, Eq.8-12]`

### B. Derivation

**[AUEC, Eq.3:72→3:73]:**
1구획 bolus: $C(t) = (D/V)e^{-Kt}$. Ordinary Emax: $E = E_{max} C / (EC_{50} + C)$. 두 식 결합 후 적분:

$$
AUC_E = \int_0^\infty \frac{E_{max} \cdot (D/V) e^{-Kt}}{EC_{50} + (D/V)e^{-Kt}} dt
$$

치환 $u = (D/V)e^{-Kt}$, $du = -Ku\,dt$:

$$
AUC_E = \frac{E_{max}}{K} \int_0^{C_0} \frac{du}{EC_{50} + u} = \frac{E_{max}}{K} \ln\left(\frac{EC_{50} + C_0}{EC_{50}}\right) = \frac{E_{max}}{K} \ln\left(1 + \frac{C_0}{EC_{50}}\right)
$$

**핵심 함의:** Dose를 2배 → AUEC는 2배가 **아니라** $\ln(1 + 2C_0/EC_{50})/\ln(1 + C_0/EC_{50})$ 배만 증가. 작은 dose에서 거의 비례, 큰 dose에서 saturating.

**[Duration, Eq.8-11→8-12]:**
$C_{min} = (D/V)e^{-K t_D}$ → $t_D = (1/K)\ln(D/(C_{min} \cdot V))$.

**핵심 정리: "Dose 2배 → Duration 1 t½ 증가":**
$D_0$에서 duration $t_D$. $2 D_0$에서 처음 1 t½ 후 잔량 = $D_0$ → 그 시점에서 처음 dose 시작과 동일 → duration = $t_{1/2} + t_D$.

R&T Fig.8-23: dose 축 log-scale로 plotting하면 $t_D$ vs log(dose)가 직선 (slope = $1/K$, intercept at zero duration = $\ln A_{min}$).

**검증 사례 — Succinylcholine (Walts & Dillon 1967):**
- 0.5 mg/kg → T50 ≈ 6 min
- 1.0 mg/kg → T50 ≈ 10 min
- 2.0 mg/kg → T50 ≈ 14 min
- 4.0 mg/kg → T50 ≈ 18 min
- 각 단계 +4 min = $t_{1/2}$ 추정. $K = 0.2$ min⁻¹, $t_{1/2} \approx 4$ min — 가수분해 elimination 반감기와 일치.

`[출처: R&T 5e, Ch.8, p.255, Fig.8-24]`

### C. Structural Necessity (PK vs PD Rate-Limiting)

**PK rate-limited 조건:**
- Site of action ↔ plasma 빠른 평형
- Effect가 receptor occupancy에 즉각 비례 (no covalent binding, no downstream dynamics)
- 예: 신경근 차단(succinylcholine), β-blockade(propranolol), 마취제(midazolam)

**PD rate-limited 조건:**
- 약물이 비가역적으로 receptor 결합 (Aspirin: cyclooxygenase 아세틸화, Omeprazole: proton pump 공유 결합)
- 또는 약물이 indirect turnover system을 modulate (Warfarin: prothrombin synthesis 억제)
- → effect 회복이 receptor / system turnover에 의존

**선택 규칙:**
$$
\text{Effect } t_{1/2} \approx \max(t_{1/2,PK}, t_{1/2,PD\text{-system}})
$$
*더 느린 쪽이 율속.* Acenocoumarol (PK $t_{1/2}$=15h, PD system $t_{1/2}$≈1.5d) → PD-rate-limited (3일 회복). Phenprocoumon (PK $t_{1/2}$=5d, PD system $t_{1/2}$≈1.5d) → PK-rate-limited (2주 회복). **같은 메커니즘인데 회복 시간 6배 차이.**

`[출처: R&T 5e, Ch.8, p.243, Fig.8-11]`

<!-- TRENCH -->
**[Trench-Level Tip — Aspirin perioperative timing]:** Aspirin 단회 75 mg 후에도 platelet thromboxane B2 inhibition은 7-10일 지속 (full platelet pool turnover). Plasma t½(15min)에 의존해 "1일 wash-out 후 수술 가능"이라고 판단하면 perioperative bleeding 위험. 표준 권고: aspirin discontinuation **7일 전**부터. 이 7일은 PK가 아니라 platelet turnover가 결정한다.

### D. Assumptions

| 가정 | AUEC 공식 | Duration 공식 |
|---|---|---|
| 1구획 1차 elimination | 필수 | 필수 |
| Ordinary Emax (n=1) | 필수 | (해당 없음 — duration은 모델 형태에 무관) |
| Site-of-action ↔ plasma 즉각 평형 | 필수 | 필수 (PK rate-limited 가정) |
| Cmin 일정 | (해당 없음) | 필수 |
| 비가역적 결합 없음 | 필수 (없으면 indirect 형태 필요) | 필수 |

### E. Limitations

1. **Sigmoid Emax (n≠1)에서 AUEC 닫힌 해 부재:** Numerical integration 필요.
2. **Multi-compartment PK에서 공식 깨짐:** 분포 단계 동안 effect dynamics가 다름.
3. **Cmin 가정의 임상 실패:** "Effect가 Cmin 미만에서 0"이라는 가정은 graded effect의 특성을 무시. 실제로는 점진적 감소.
4. **Indirect response에서 Eq.8-12 적용 불가:** Warfarin 같은 indirect 약물의 duration은 dose에 거의 무관하게 prothrombin turnover에 의해 지배.

### F. Five Cognitive Layers

| Layer | 내용 |
|---|---|
| **L1 수학** | $\int E dt$ 적분, 치환 적분, log-dose 비례성, slope-intercept linear regression. |
| **L2 기하** | $E$ vs t plot의 3 region (Region 3: max plateau, Region 2: linear decline, Region 1: PK-tracking decline). Dose 2배 → 곡선이 t½ 만큼 오른쪽 평행이동. |
| **L3 동일성** | Population epidemiology의 SIR model, predator-prey decay, RC capacitor discharge with threshold detection. 모두 "exponential decay above threshold"의 보편 형태. |
| **L4 생리학** | PD rate-limited 사례의 메커니즘적 분류: 비가역 결합 (aspirin, omeprazole) vs slow turnover (warfarin) vs slow target dissociation (Fig.8-4 illustrative). 각각 다른 receptor 재합성 시간 척도. |
| **L5 실무** | NONMEM에서 AUEC 계산은 effect 데이터의 trapezoidal integration. Duration 계산은 simulation 후 threshold crossing detection. PopPK/PD에서 duration은 dose-titration 결정의 핵심 outcome. |

### G. Zettelkasten Atom

```yaml
---
aliases: [AUEC, Duration of Effect, log-dose Duration, PK Rate-Limiting, PD Rate-Limiting]
tags: [pharmacometrics/pd, response/temporal, dosing/duration]
up: "[[PD 모델 계보 MOC]]"
related: ["[[Sigmoid Emax C2]]", "[[Indirect Response C4]]", "[[Aspirin Antiplatelet]]", "[[Warfarin Anticoagulation]]"]
source: "Gabrielsson & Weiner 5e, Ch.3 §3.6.6–3.6.7, p.229–234 + Rowland & Tozer 5e, Ch.8, p.248–256"
---
```

> 1구획 ordinary Emax 시스템에서 AUEC는 dose에 log-비례하며 ($E_{max}/K \cdot \ln(1 + D/(EC_{50}V))$), duration은 dose log에 선형 비례 ($t_D = (1/K)\ln(D/A_{min})$, dose 2배 → duration 1 t½ 증가). 그러나 실제 효과 지속 시간은 PK $t_{1/2}$과 PD system $t_{1/2}$ 중 더 느린 쪽에 의해 율속되며, aspirin·omeprazole·warfarin·paclitaxel 같은 약물은 PD rate-limited여서 plasma 농도가 0이 된 뒤에도 며칠 effect 지속. 이 이중성은 perioperative aspirin 7일 중단 같은 임상 결정의 직접 근거.

<!-- RECAP -->
*C1–C5 통합: 평형 모델(C1–C2) → 시간 차원 도입(C3–C4) → 효과의 적분과 지속 시간(C5). 이 5축이 §3 구조적 동형성과 §4 시뮬레이터의 골격이 된다.*

---

# §5 — Confusion Pair Dissection

<!-- CONFUSION -->
## Pair 1: Kd vs EC50 (결합 친화도 vs 기능적 효능)

| 비교 차원 | Kd (binding affinity) | EC50 (functional potency) |
|---|---|---|
| **표면적 유사성** | 둘 다 'half-max에서의 농도' 형태로 표현되며, Emax 식의 분모에 동등하게 등장 (Eq.3:8 vs Eq.3:10). 단위가 같고 (M 또는 µg/L) 그래프 모양도 같음. | |
| **수식/코드 형태** | $\frac{[RC]}{[R_T]} = \frac{C}{C+K_d}$ (binding) | $\frac{E}{E_{max}} = \frac{C}{C+EC_{50}}$ (functional) |
| **생리학적 지시체** | 단일 receptor-ligand 쌍의 화학적 결합 강도. $K_d = k_{-1}/k_1$. **Drug-specific** parameter. | Receptor occupancy → cascade → downstream → 측정 가능한 functional response의 합성 결과. **Drug + System** parameter. |
| **변화 방향** | Receptor density [R_T]가 변해도 Kd 불변. Cascade amplification이 변해도 Kd 불변. Pure drug-receptor property. | Spare receptor density 증가 → EC50 감소. Cascade gain 증가 → EC50 감소. Receptor downregulation → EC50 증가. **시스템 의존적.** |
| **임상/모델링 결과** | In vitro radioligand binding 실험에서 측정. FIH 용량 추정에서 직접 사용. | In vivo functional assay에서 측정. Phase 1 dose-finding에서 직접 사용. **EC50를 Kd로 대체 사용하면 spare receptor 시스템에서 5–100배 dose 과추정.** |
| **⚡ 기억 고리** | **"Kd는 자물쇠와 열쇠의 fit. EC50는 자물쇠가 풀린 뒤 문 너머에서 일어나는 모든 일의 합산. 따라서 EC50 ≪ Kd가 보통이며, 이 격차는 cascade amplifier의 깊이를 측정한다 — 격차가 클수록 spare receptor가 많다."** | |

---

<!-- CONFUSION -->
## Pair 2: Ordinary Emax (n=1) vs Sigmoid Emax (n>1)

| 비교 차원 | Ordinary Emax | Sigmoid Emax |
|---|---|---|
| **표면적 유사성** | 둘 다 hyperbolic 형태로 보이고, 파라미터 이름 Emax/EC50가 같다. 데이터가 noise 있을 때 두 fit이 시각적으로 유사. | |
| **수식 형태** | $E = \frac{E_{max} C}{EC_{50} + C}$ | $E = \frac{E_{max} C^n}{EC_{50}^n + C^n}$ |
| **메커니즘 의미** | 단일 부위 1:1 결합. No cooperativity, no cascade amplification 강조. | n>1: cooperativity, cascade depth, threshold passing. n<1: multiple sites, active metabolite. |
| **변화 방향** | 농도 10x 변화 → effect ~9x 변화 (Region 1). 완만. | n=4: 농도 2x 변화로 20%→80% effect 점프. All-or-nothing. |
| **임상/모델링 결과 (PD3)** | Imax=49.8 (43% 과추정), IC50=175 (25% 과추정), AIC=50.8. **"이 약은 50 mm Hg 혈압 강하 가능"이라는 잘못된 efficacy.** | Imax=34.7, IC50=140, n=2.03, AIC=45.6. F-test $F^*=6.47 > F_{table}=5.59$로 통계적 우위. |
| **⚡ 기억 고리** | **"n은 곡선의 가파름이 아니라 시스템의 위상 차원이다. n=1을 default로 가정하는 순간 'cascade는 없다'는 강한 메커니즘 가설을 무의식적으로 채택한 것이다. 이 가설이 틀리면 IC50/Imax가 양쪽으로 끌려가서 dose 권장이 갈라진다 — PD3에서 25–43% 편향."** | |

---

<!-- CONFUSION -->
## Pair 3: PK Rate-Limited vs PD Rate-Limited Decline ⚡ (Critical Pair)

| 비교 차원 | PK Rate-Limited | PD Rate-Limited |
|---|---|---|
| **표면적 유사성** | 둘 다 effect-time curve가 단조 감소. 동일 약물에서도 농도 영역에 따라 둘 사이를 오갈 수 있음 (R&T Fig.8-17 Region 1 vs Region 3). | |
| **결정 메커니즘** | Site-of-action ↔ plasma 즉각 평형. 비가역 결합·cascade·turnover 없음. Receptor occupancy에 effect 즉각 비례. | 비가역적 결합 (aspirin, omeprazole), slow target dissociation, 또는 endogenous turnover system (warfarin, paclitaxel-leukocyte). |
| **수식 형태** | $E(t) \propto C(t)$. Effect 반감기 ≈ PK 반감기 (Region 1). | Effect 반감기 = receptor 재합성 또는 system turnover 반감기. PK와 무관. |
| **변화 방향** | PK 변경(예: clearance 증가) → effect duration 즉시 변화. | PK 변경 → effect duration 거의 영향 없음 (아스피린 예: hepatic enzyme inducer로 elimination 빨라져도 platelet effect 같음). |
| **임상 결과** | 표준 dose adjustment 적용 가능 (CrCl 감소 → dose 감소). Succinylcholine, propranolol, midazolam, minoxidil. | "약이 몸에 없으면 효과도 없다"는 직관 실패. Aspirin: t½=15min PK, 7-10일 perioperative discontinuation. Omeprazole: 1h PK, 3일 acid 억제. Warfarin: 1.5d PK, 5일 INR 회복. Paclitaxel: 2d PK, 3주 leukocyte 회복. |
| **🔥 치명적 타격 (Critical Blow)** | **신경외과 환자가 매일 75 mg aspirin 복용 중. 응급 수술 결정이 수요일에 내려졌고, 외과의가 "aspirin 반감기가 짧으니 24시간 wash-out으로 충분"이라고 판단한다. 그러나 aspirin은 PD rate-limited (platelet turnover ≈ 7-10일)이며 cyclooxygenase 비가역적 아세틸화로 작동한다. 24시간 후 수술 → intraoperative hemorrhage → emergency platelet transfusion → mortality risk 증가. NDA 라벨의 "Discontinue aspirin 7-10 days before elective surgery" 권고를 PK 데이터가 아닌 PD 메커니즘 기반으로 작성하지 않으면 FDA Deficiency Letter — 이것이 PK ↔ PD rate-limiting 혼동의 가장 직접적 임상 결과.** | |
| **⚡ 기억 고리** | **"PK는 약물의 시간, PD는 시스템의 시간. 둘 중 더 느린 시계가 환자의 시간을 결정한다. Aspirin의 시계는 platelet pool의 turnover (1주); warfarin의 시계는 clotting factor synthesis (1-2일); succinylcholine의 시계는 hepatic esterase의 가수분해 (4분). 약리학자는 두 시계를 동시에 들고 다닌다."** | |

---

<!-- CONFUSION -->
## Pair 4: Direct Link vs Indirect Response (둘 다 hysteresis 만들지만)

| 비교 차원 | Direct Link with Effect Compartment | Indirect Response Model |
|---|---|---|
| **표면적 유사성** | 둘 다 plasma C-time과 effect-time 사이에 시간 지연을 만들고, counterclockwise hysteresis loop를 produce. | |
| **수식 구조** | $\dot{C_e} = k_{e0}(C_p - C_e)$, $E = f(C_e)$. Single 시간 지연 파라미터. | $\dot{A} = R_{syn}(C_p) - k_t \cdot A$. Effect는 turnover system의 현재 state. |
| **메커니즘** | Plasma → site of action 분포 지연. Tissue perfusion + membrane permeability + tissue affinity. | Effect가 endogenous substance의 turnover (synthesis-degradation balance). Drug는 그 balance를 modulate. |
| **시간 척도 진단** | $k_{e0}$ 추정 후 hysteresis 사라짐 → site-of-action 분포 지연이 원인. | $k_{e0}$ 추정해도 hysteresis 유지 → underlying turnover system ($k_t$) 필요. Blocking dose 실험으로 $k_t$ 별도 측정. |
| **Dose-response peak time** | Dose에 의존 (큰 dose → peak earlier). | **Dose 무관** (warfarin 모든 dose에서 36–48h peak). $k_t$가 결정. |
| **임상 사례** | Naproxen pain relief (R&T Fig.8-2, 8-14): $k_{e0}$ 추정으로 hysteresis 완전 소실. | Warfarin → prothrombin (R&T Fig.8-10), Ranitidine → gastric pH (R&T Fig.8-8), Paclitaxel → leukocyte. |
| **⚡ 기억 고리** | **"Effect compartment는 약물이 site에 도착하는 데 걸리는 시간. Indirect response는 시스템이 새로운 균형에 도달하는 데 걸리는 시간. 첫 번째는 dose 크기가 도착 속도를 바꾸지만, 두 번째는 시스템이 자신의 시계로 작동하므로 dose는 균형의 깊이만 바꿀 뿐 도달 시간은 그대로다."** | |

---

# §7 — Self-Test: Active Recall Module

<!-- SELF-TEST -->
**Q1 (★★ 회상):** Ordinary Emax 모델 $E = E_{max} C / (EC_{50} + C)$를 평형 receptor occupancy로부터 출발하여 4단계 이내로 도출하시오. 각 단계에서 사용된 가정 1개씩 명시.

> **정답:**
> Step 1: 평형 조건 $k_1[R][C] = k_{-1}[RC]$ (가정: 1:1 가역 결합).
> Step 2: $K_d = k_{-1}/k_1 = [C][R]/[RC]$ (가정: 단일 부위).
> Step 3: $[R_T] = [R] + [RC]$ 보존 → $[RC]/[R_T] = C/(C+K_d)$ (가정: receptor 총량 시간 불변).
> Step 4: $E = \alpha[RC]$, $E_{max} = \alpha[R_T]$ → $E/E_{max} = C/(C+K_d)$, EC50를 Kd로 대체 (가정: response가 점유율에 직접 비례, 즉 cascade gain=1).
> **다음 깊이 질문:** Step 4의 마지막 가정이 깨지면 (cascade gain ≠ 1) EC50와 Kd의 관계는?

---

<!-- SELF-TEST -->
**Q2 (★★ 회상):** Hill 모델의 Hill coefficient $n$이 가질 수 있는 메커니즘적 해석 3가지를 나열하고, 각각 어떤 데이터 패턴을 나타내는가?

> **정답:**
> 1. **n>1 with cooperativity:** 같은 receptor에 ligand가 cooperatively 결합 (Hill 1910 hemoglobin-O2). 데이터 패턴: 같은 receptor에서 multiple binding site가 함께 활성화.
> 2. **n>1 with cascade amplification:** 결합 → stimulus 1 → stimulus 2 → response의 다단계 hyperbolic 곱 (G&W Fig.3.5). 데이터 패턴: in vitro binding curve는 n=1이지만 in vivo functional curve는 n>1.
> 3. **n<1 with multiple receptor sites or active metabolite:** 친화도가 다른 두 부위 또는 활성 대사체. 데이터 패턴: 곡선이 EC50 부근에서 평탄화되고 unbound 농도로 변환해도 n이 같음.
> **다음 깊이 질문:** PD3에서 추정된 n=2.03의 95% CI는 약 1.2–2.9 (CV=21%). 이 범위 안에서 cooperativity vs cascade를 구별할 수 있는가?

---

<!-- SELF-TEST -->
**Q3 (★ 회상):** R&T의 Eq.8-3은 $E(t) = E(0) - m \cdot k \cdot t$ 형태로 effect가 zero-order로 감소함을 보인다. 이 식의 도출에서 핵심 가정 2가지는?

> **정답:**
> (1) Plasma C가 1구획 1차 elimination $\ln C(t) = \ln C(0) - kt$.
> (2) Response가 log-linear 형태 $E = m \ln C + b$ (즉, log-concentration 영역에서 선형).
> 두 가정을 결합하면 t의 1차 항만 남아서 effect가 zero-order로 감소. 단, 이 식은 Region 2 (20–80% effect)에서만 유효 — Region 3에서는 plateau, Region 1에서는 PK와 평행.
> **다음 깊이 질문:** Sigmoid Emax 모델 $n>1$에서는 Region 2의 slope가 어떻게 달라지는가? Eq.3:38에서 답이 나옴.

---

<!-- SELF-TEST -->
**Q4 (★★ 적용):** PD3 Phase 2 시뮬레이션. 신약 X의 혈압 강하 데이터에서 Imax=34.7 mm Hg, IC50=140 µg·L⁻¹, n=2.03 추정. baseline E0=171. **목표 혈압 강하 = 25 mm Hg.** 필요한 정상 농도 $C_T$를 계산하시오 (target concentration model, G&W Table 3.1).

> **정답:**
> Sigmoid Imax model의 target concentration model:
> $$C_T = IC_{50} \cdot \sqrt[n]{\frac{E_T - E_0}{E_T - I_{max} - E_0}}$$
> $E_T - E_0 = 25 - 0 = -25$ (혈압 강하이므로 E_T < E_0이지만 부호 정리: 강하량 25). 정확히는 $E_T = E_0 - 25 = 146$, $E_T - E_0 = -25$, $E_T - I_{max} - E_0 = 146 - 34.7 - 171 = -59.7$.
> $$C_T = 140 \cdot \sqrt[2.03]{\frac{-25}{-59.7}} = 140 \cdot \sqrt[2.03]{0.419} = 140 \cdot 0.652 \approx 91 \, \mu g/L$$
> **다음 깊이 질문:** 이 $C_T = 91$의 95% CI는 IC50와 n의 추정 불확실성을 어떻게 propagate하면 얻을 수 있는가? (Delta method 또는 simulation)

---

<!-- SELF-TEST -->
**Q5 (★★ 적용):** Succinylcholine 임상 사례. 0.5 mg/kg iv → T50 (twitch 50% 회복) = 6 min. **2 mg/kg iv 후 T50을 추정하시오.** (R&T Fig.8-24 사용 금지, 원리만 사용.)

> **정답:**
> Dose 2배 → duration 1 $t_{1/2}$ 증가 (R&T 핵심 정리). Succinylcholine $t_{1/2} \approx 4$ min.
> - 0.5 → 1.0 mg/kg: T50 = 6 + 4 = 10 min
> - 1.0 → 2.0 mg/kg: T50 = 10 + 4 = 14 min
> 따라서 2 mg/kg 후 T50 ≈ 14 min. (R&T Fig.8-24 실측치와 일치.)
> **다음 깊이 질문:** Phenytoin 같은 saturable Michaelis-Menten elimination 약물에서는 이 "dose 2배 → 1 t½ 증가" 규칙이 어떻게 깨지는가?

---

<!-- SELF-TEST -->
**Q6 (★★ 적용):** Warfarin 1.5 mg/kg PO 후 prothrombin complex activity가 36–48 시간에 minimum (~20% baseline)에 도달한 뒤 5일에 걸쳐 회복한다 (R&T Fig.8-10). 회복 단계의 특정 시점에서 측정값이 $A_1=30\%$, $A_2=42\%$ ($\Delta t=12$ h). $k_t = 0.5$ day⁻¹ = 0.0208 hr⁻¹. 그 시점에서의 **% inhibition of synthesis**는?

> **정답:**
> R&T Eq.8-7:
> $$R_{syn}(t) = \frac{A_2 - A_1}{\Delta t} + k_t \cdot \frac{A_1 + A_2}{2} = \frac{42 - 30}{12} + 0.0208 \cdot \frac{30 + 42}{2} = 1.0 + 0.749 = 1.75 \text{ \%/h}$$
> 정상 합성률 $R_{syn(n)} = k_t \cdot 100\% = 0.0208 \cdot 100 = 2.08$ %/h.
> $$\% \text{ inhibition} = 100 \cdot \frac{2.08 - 1.75}{2.08} = 16\%$$
> 이 시점에서 warfarin은 prothrombin synthesis를 16% 억제. plasma warfarin 농도와 이 값을 짝지어 plotting하면 R&T Fig.8-16의 log-linear C-inhibition 관계가 나옴.
> **다음 깊이 질문:** $k_t$ 추정 자체가 부정확하면 (실제 $k_t$=0.4 instead of 0.5), inhibition 추정이 어느 방향으로 편향되는가?

---

<!-- SELF-TEST -->
**Q7 (★ 적용):** R&T Fig.8-2의 naproxen 데이터에서 unbound plasma C와 pain relief가 counterclockwise hysteresis loop를 만든다. 이 loop를 effect compartment 모델로 흡수했더니 (R&T Fig.8-14) hysteresis가 사라졌다. 이 결과는 시간 지연의 원인이 (A) 분포 지연인지 (B) indirect response system인지 어느 쪽을 지지하는가? 근거를 1문장으로.

> **정답:** (A) **분포 지연을 지지.** Effect compartment ($k_{e0}$ 단일 파라미터)만으로 hysteresis가 완전히 흡수되었다는 것은 site-of-action 농도가 plasma와 1차 distribution kinetics로 평형을 이룬다는 가설이 데이터와 부합함을 의미. Indirect response가 원인이라면 $k_{e0}$ 변환 후에도 잔여 hysteresis가 보일 것 (예: warfarin에서는 effect compartment만으로 안 됨).
> **다음 깊이 질문:** Naproxen의 추정된 $k_{e0}$ 값은 약 0.5–1 hr⁻¹ 범위인데, 이는 어떤 생리학적 과정과 일치하는가?

---

<!-- SELF-TEST -->
**Q8 — 보스 딜레마 (★★ Socratic):**

당신은 신약 후보 Z (sigmoid Imax 메커니즘으로 혈압 강하)의 Phase 2/3 transition 회의에 참석한 lead 모델러다. Phase 2 데이터에서 명확한 counterclockwise hysteresis가 plasma C-effect 평면에서 관찰되었다 (loop 폭 ≈ 25%, peak effect time이 plasma Cmax보다 2-3시간 늦음). 두 가지 모델 옵션이 있다:

**(A) Effect Compartment 모델 ($C_e$ + sigmoid Imax):**
- 추정 결과: $k_{e0} = 0.32$ hr⁻¹ (CV 48%), Imax=33 (CV 12%), IC50=160 µg/L (CV 18%), n=2.1 (CV 25%).
- Hysteresis 거의 완전 소실.
- 단점: $k_{e0}$의 정밀도가 낮고, Phase 3 외삽 시 hepatic impairment 환자에서 $k_{e0}$ 값이 어떻게 변할지 prior 부재. 실제 mechanism이 indirect response (해당 약물은 baroreceptor reflex 경유 가능)일 수 있다는 외부 약리학적 증거 존재.

**(B) Plasma 직접 sigmoid Imax 모델:**
- 추정 결과: Imax=39 (CV 8%), IC50=185 µg/L (CV 9%), n=1.7 (CV 14%).
- AIC가 (A)보다 12 높음 (모델 적합 나쁨).
- 잔차 plot에서 명확한 시간 의존적 패턴 (initial timepoints에서 음수, late timepoints에서 양수). 그러나 추정 정밀도는 매우 좋음.
- Phase 1 ascending dose 데이터와 IC50가 다름 (Phase 1: 145 µg/L; 이 모델: 185).

**Phase 3 NDA 제출용 모델로 어느 쪽을 선택하는가?** 그 결정을 FDA 심사관에게 어떻게 정당화하는가?

> **수석 모델러의 Trade-off 논리:**
>
> **결론: (A) Effect Compartment를 선택하되, 단순 default가 아니라 *"mechanism-agnostic time-delay absorber"*로 frame한다. 동시에 sensitivity analysis에서 indirect response model을 alternative로 fit하여 외삽의 robustness를 검증한다.**
>
> **정당화 논리 (3축):**
>
> 1. **Hysteresis가 명확한 데이터에서 plasma direct model을 사용하는 것은 모델 misspecification.** AIC 12 차이 + 시간 의존적 잔차 패턴은 "(B)는 systematic bias가 있다"는 직접 증거. FDA Deficiency Letter 사유.
>
> 2. **(A)의 $k_{e0}$ 정밀도가 낮은 것(CV 48%)은 결정적 약점이지만, *외삽 시 boundary condition을 명시*하는 것으로 mitigate 가능.** 즉, label에서 "extrapolation to hepatic impairment beyond the studied range may have additional uncertainty in $k_{e0}$"를 명시. PopPK/PD에서 $k_{e0}$를 IIV로 estimate하지 않고 fixed로 두는 sensitivity analysis도 함께 제출.
>
> 3. **Indirect response 가설이 존재하면 *둘 다 fit하고 비교*.** Effect compartment가 main model로 채택되더라도, indirect response (kin/kout) model을 supplementary analysis로 fit. 만약 indirect 모델이 (A)보다 AIC가 더 낮으면 main model 교체 후보로 검토. 만약 두 모델이 비슷하면 effect compartment의 simplicity 채택.
>
> **FDA 심사관에게 핵심 메시지:** "We selected the effect compartment model based on objective fit criteria (AIC, residual diagnostics). We acknowledge $k_{e0}$ uncertainty (CV 48%) and have characterized its impact on extrapolations through sensitivity analyses. We have additionally evaluated an indirect response model as an alternative mechanism, which yielded comparable predictions within the studied dose range. Should new mechanism-specific data emerge in Phase 4, the model may be updated."
>
> **반대 결정의 정당화도 가능:** 만약 외부 약리학적 증거가 indirect response를 강하게 시사하면 (예: baroreceptor knockout 동물 데이터), main model을 indirect response로 두고 effect compartment를 sensitivity analysis로 두는 것이 더 mechanistically defensible. 핵심은 *"data-driven selection AND mechanism-aware narrative AND uncertainty disclosure"*의 3축이 NDA 모델의 standard.

---

# §8 — Meta-Frame & Big Picture

## A. Positioning (28-세션 PK/PD 아키텍처에서의 위치)

**이전에 온 것 (선행):**
- I-08 TMDD: target-mediated drug disposition. 이 세션의 receptor occupancy 식 (Eq.3:8)이 거기서 quasi-equilibrium approximation으로 다시 나타남.
- II-04 General ADVAN/$DES: ODE 기반 모델 코딩. 이 세션의 effect compartment / indirect response가 모두 ODE 형태로 표현되며, 거기서 배운 $DES 코드 패턴이 직접 적용됨.
- 1구획·다구획 PK 기초: $C_p(t) = C_0 e^{-Kt}$가 모든 직접 link 모델의 input.

**바로 다음에 오는 것 (후속):**
- **kin/kout indirect response 4종 표준 코드 세션**: 이 세션의 Eq.8-6을 4가지 변형 (input/output × stim/inhib)으로 일반화.
- **Tolerance / Receptor downregulation 세션**: clockwise hysteresis가 이 세션 범위 외이므로 거기서 다룸.
- **Effect compartment 정식 ODE + ke0 식별성**: $k_{e0}$ 추정 한계를 해결하는 alternative parameterization.

**이 기반에 결정적으로 의존하는 고급 도메인:**
- **PopPK/PD (ICH E14, M14)**: EC50의 covariate 분석. 이 세션을 모르면 EC50가 system parameter임을 인식 못해서 covariate effect를 잘못 attribute.
- **PBPK/PD coupling**: 각 organ의 indirect response가 systemic exposure에 어떻게 mapping되는지.
- **QSP (Quantitative Systems Pharmacology)**: cascade effect (Fig.3.5)의 다단계 확장이 정확히 QSP의 신호 전달 모델.
- **모델 기반 dose-finding (MBMA)**: AUEC의 log-dose 의존성과 duration의 log-dose linearity가 dose escalation 설계의 직접 근거.

## B. Dependencies (이 섹션을 대충 넘겼을 때의 실패 모드)

**Failure Mode 1: EC50 covariate misclassification.**
EC50가 system parameter임을 모르면, IIV에 들어간 EC50 변동을 drug PK 변동으로 잘못 해석. 예: renal impairment subgroup에서 EC50가 다르게 나오면 "약물 분포가 달라졌다"고 판단 → 실제로는 receptor density나 cascade gain이 다른 것. 이 misattribution은 dose adjustment 권고를 잘못된 방향으로 끌고 가서 Phase 3에서 efficacy gap 발생. 추적 가능한 인과: 이 세션 §C1 spare receptor 부분 → covariate analysis 챕터 → Phase 3 dose protocol → label.

**Failure Mode 2: PD rate-limited 약물의 dose interval 선정 실패.**
Aspirin/omeprazole/warfarin 같은 PD rate-limited 약물에서 dose interval을 PK $t_{1/2}$ 기반으로 결정하면 (예: aspirin BID), unnecessary cumulative covalent binding이 발생하거나 (overdosing) 또는 receptor turnover를 놓쳐서 효과 gap (underdosing). 이 세션 §C5 "둘 중 더 느린 쪽이 율속" 원칙을 놓치면 Phase 3 dosing 문서 전체가 fragile. 추적 가능한 인과: rate-limiting 분석 누락 → dose interval 잘못된 추정 → Phase 3 dosing protocol → safety signal 또는 efficacy failure.

## C. Professional Moat (이 섹션 내용에 직접·구체적으로)

NONMEM을 실행하고 `EMAX*C/(EC50+C)` 한 줄을 코딩할 수 있는 주니어 모델러는 이미 자동화 가능. ChatGPT가 sigmoid Imax fit을 제안할 수도 있다. 이 섹션의 원리를 진정으로 내면화한 연구자만이 다음과 같은 판단을 내릴 수 있다:

- **PD3 데이터를 보고 즉시:** "n=1.94 vs 2.03의 차이는 통계적이 아니라 noise level CV가 5% 이상이라는 신호. 추정 정밀도 (PD3 Table 3.3)에서 5% CV → n CV 50%. 이 데이터로 cooperativity vs cascade를 구별하려는 시도는 over-interpretation."

- **새로운 indirect response 데이터에서 30초 안에:** "Hysteresis가 보이는데 dose에 무관한 peak time이면 indirect response. Dose에 비례하는 peak shift면 effect compartment. 둘 다 fit해보고 AIC 차이가 4 미만이면 mechanism-agnostic 결정 — 그러나 외삽이 필요하면 mechanism 선호."

- **임상에서 "왜 aspirin은 7일 중단 권고인가?"라고 질문받으면:** "PK rate-limited 약물의 7 t½ 규칙(2시간)은 적용 안 됨. Cyclooxygenase 비가역적 acetylation으로 platelet pool 전체 turnover (≈10일)가 율속. Plasma에서 aspirin이 측정 안 되는 것은 효과 없음을 의미하지 않음. 이는 R&T Ch.8의 PD rate-limiting의 정확히 그 사례."

- **EC50가 covariate에 따라 변하는 데이터를 보면:** "EC50 = drug + system. Drug 부분(Kd-equivalent)은 covariate 무관. System 부분(receptor density, cascade gain)이 covariate-sensitive. Renal impairment에서 EC50가 변하면 spare receptor density가 변한 가능성 높음 — 이 가설은 in vitro Bmax 실험으로 검증 가능."

이런 판단은 *"수식을 외우는 것"*이 아니라 *"수식이 어디에서 왜 그 형태로 나왔는지를 추적할 수 있는 것"*에서 나온다. 그것이 이 세션의 §2 "Big Idea" 블록과 §C2 Plausible Fallacy가 박아 넣으려는 이유이며, 그것이 자동화될 수 없는 직업적 해자다.

---

```
---
✦ STEP 1 완료.

다음이 준비되었습니다:
  • §1 세션 헤더 & 로드맵 (Big Idea: 비선형성 × 시간 지연 이중 축)
  • §2 개념 해부 카드 5개
      - C1: Law of Mass Action → Emax 골격
      - C2: Sigmoid Emax / Hill model [⚡ Apex Concept]
      - C3: Hysteresis as Diagnostic
      - C4: Effect Compartment + Indirect Response
      - C5: AUEC + Duration + PK/PD Rate-Limiting
      Apex: C2 (Sigmoid Emax / Hill model — Plausible Fallacy "Curvature Suppression")
  • §5 혼동 쌍 해부 4쌍
      Pair 1: Kd vs EC50
      Pair 2: Ordinary Emax vs Sigmoid Emax
      Pair 3: PK Rate-Limited vs PD Rate-Limited [Critical Blow]
      Pair 4: Direct Link vs Indirect Response
      Critical Blow 적용: Pair 3 (Aspirin perioperative 시나리오)
  • §7 자기 테스트 8개 질문 (회상 3 / 적용 4 / 보스 딜레마 1)
      Boss Dilemma: Phase 3 NDA에서 Effect Compartment vs Plasma Direct vs Indirect Response 모델 선택
  • §8 메타프레임 & 빅 픽처 (Position / Dependencies / Professional Moat)
  • 감지된 소스 유형: Vol I 혼합 (Gabrielsson + Rowland & Tozer)
  • Data Anchoring 소스:
      - PD3 (G&W p.732–741): E0=171, Imax=34.7, IC50=140, n=2.03 (0–800 µg·L⁻¹ design)
      - Lundström 1992 (G&W §3.5.6): IC50,1=1.8, IC50,2=23, Imax,1=4, Imax,2=3.2, n1=1.4, n2=3.7
      - Remoxipride (G&W §3.6.6): 600 mg/day, t½(response)=1–2 wk vs t½(plasma)=5–10 h
      - Digoxin Shapiro 1970 (R&T Fig.8-1): 1 mg iv, 6 normal subjects
      - Naproxen Syntex 1994 (R&T Fig.8-2, 8-14): 500 mg PO, dental pain
      - Warfarin Nagashima 1969 (R&T Fig.8-10, 8-15): 1.5 mg/kg PO, prothrombin t½=1.5 d
      - Acenocoumarol vs Phenprocoumon (R&T Fig.8-11): t½ 15h vs 5d, 회복 3d vs 2주
      - Succinylcholine Walts & Dillon 1967 (R&T Fig.8-18, 8-24): 0.5 mg/kg iv, K=0.2 min⁻¹
      - Aspirin Ali 1980 (R&T Fig.8-20): 650 mg PO, t½=15min, antiplatelet 효과 며칠
      - Omeprazole Lind 1983 (R&T Fig.8-21): 40 mg PO, acid 억제 3일
      - Methylprednisolone Derendorf 1991 (R&T Fig.8-25–8-27): 16–1000 mg, PK 선형 + PD 비선형
      - Paclitaxel Minami 1998 (R&T Fig.8-22): leukocyte 회복 3주

[확인 필요 — 첨부 PDF 미포함 구간]:
  • G&W §3.6.2–3.6.5 (pp.225–228): 비경쟁/non-equilibrium 길항 모델 — 본 세션에서 추정·보완하지 않음. 후속 세션 또는 보충 PDF 확보 후 별도 처리 필요.
  • G&W §3.12 baseline modeling: C2 카드 Limitations에서 1줄 언급만, 깊이 있는 다룸은 보류.

"계속"을 입력하면 Step 2 HTML 컴파일러가 실행됩니다.
Step 2는 위 내용 전체(§1·§2·§5·§7·§8) +
§3(구조적 동형성 지도) + §4(인터랙티브 시뮬레이터 + Assumption Collapse 토글) +
§6(실용 시나리오 & 진단 병리)를 단일 완성 HTML 파일로 통합합니다.
---
```

---

C-260502-014732-K7P

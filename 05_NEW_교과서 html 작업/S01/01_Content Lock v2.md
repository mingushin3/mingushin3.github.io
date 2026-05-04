# 01_Content Lock v2 — One-Compartment IV Kinetics: CL · V · t½ · K

**Source:** Gabrielsson & Weiner 5e Ch.2 §2.2.1–2.2.5 + Case Study PK1 / Rowland & Tozer 5e Ch.3  
**Pages:** G p.14–32, p.469–475 / R&T p.53–76  
**Mode:** A-Critical | **Learner:** PhD pharmacometrics, PopPK entry–intermediate  
**Content status:** Phase 4B text-final deliverable. Figure inventory is carried forward to Phase 4C unchanged; no figure markers are inserted here.

---

## Updated Curation Map

<!-- ANNOTATION -->
이 세션의 핵심은 하나다. **$CL$과 $V$는 독립적 primary parameter(← 먼저 추정·해석하는 기본값)이고, $K$와 $t_{1/2}$는 그 두 값에서 파생되는 secondary parameter(← 기본값에서 계산되는 파생값)다.** 따라서 $K$나 $t_{1/2}$를 원인처럼 해석하면 안 된다. 이 위계를 잘못 잡으면 semi-log plot 해석, 유지용량, 항정상태 시간, NONMEM parameterization이 모두 흔들린다. [G p.17; R&T p.56–58]

### MUST — 전용 §2 카드 유지

| # | 개념 | Lock 판정 | Source tags |
|---|---|---|---|
| C1 | **Clearance ($CL$)** | Apex. AUC, 항정상태 농도, 유지용량의 중심. | [G p.16–19, 22–23; R&T p.55–60] |
| C2 | **Volume of Distribution ($V$)** | $C_0$, loading dose, $K=CL/V$의 분모. Apparent volume로 체화. | [G p.14–21, 470, 473; R&T p.62–64] |
| C3 | **Elimination Rate Constant ($K$)** | 1차 소실의 fractional rate; $CL/V$의 그림자. | [G p.16–18; R&T p.56–58] |
| C4 | **Half-life ($t_{1/2}$)** | $0.693V/CL$의 합성 시간 척도. 단독 해석 금지. | [G p.17–18, 22; R&T p.58–66] |
| C5 | **Mean Residence Time ($MRT$)** | NCA bridge. 1-cmt IV bolus에서 $1/K=1.443t_{1/2}$. | [G p.19, 474; R&T p.60–61] |

### CONTEXT — 전용 카드 없음, 1–2문장 처리

- **Extravascular absorption, $K_a$, $F$, $t_{lag}$:** 별도 흡수 모델 세션. 이 세션에서는 $F$가 개입하면 apparent parameter 해석이 필요하다는 수준으로만 언급한다. [G p.28–32]
- **$f_u$, $V_u$, tissue partition, $K_{Pi}$:** $V$가 free fraction과 tissue distribution의 함수라는 직관까지만 유지한다. [G p.20–21]
- **Constant infusion:** $C_{ss}=R_{in}/CL$과 time-to-steady-state만 유지한다. [G p.22–28]
- **Distribution vs terminal phase:** midazolam, Fig.3-6, gentamicin 예외를 $t_{1/2}$ 해석의 경계조건으로만 사용한다. [R&T p.61–66]
- **Renal clearance, $f_e$:** $CL_R=f_e\cdot CL$ 수준의 context로 유지한다. [R&T p.66–68]

### REJECTED / DEFERRED

- 흡수 동력학 본격 도출, flip-flop/residual method 전개, $K_a$ 추정 카드. [G p.28–32]
- Tissue partition coefficient 표 전체와 PBPK식 전개. [G p.21]
- Renal clearance 단독 카드 및 plasma/urine worked dataset 전개. [R&T p.68–71]
- 출처 없는 정량적 임상 주장, 규제 통계, invented NONMEM/OFV 수치.

---

## Adjudication Table Summary

Audit v1에는 별도 T7 page-tag correction table이 없었다. 따라서 본 Content Lock은 Audit T1–T5와 Crucible Grade A/B/C 판정에 따라 source page tag를 본문에 직접 보존·병합했다. T6 Figure Inventory는 지시대로 4A 판정 대상에서 제외했다.

| Source | Item (brief description) | Verdict | Rationale |
|---|---|---|---|
| Audit T1/T3/T5 | Core hierarchy, IV bolus ODE, integrated equation, semi-log slope, $K=CL/V$, $t_{1/2}=0.693V/CL$, $CL=Dose/AUC$, $C_{ss}=R_{in}/CL$, $V=D/C^0$, AUC/AUMC/MRT, creatinine/inulin, midazolam, gentamicin, renal context | ADOPT | 모두 PDF와 일치하며 이 세션의 골격이므로 보존. |
| Audit T1/T2 #S1/S4 | C1 anchor가 Subject 1과 4의 $CL$이 같다고 해석 | ADOPT | 오류를 정정: S1 $CL=0.1$, S4 $CL=0.2$ L/min; $K$와 $t_{1/2}$만 유사. |
| Audit T1 | Quinacrine $V=40{,}000$ L | ADOPT | Source-bound 직관 anchor로 유지. [G p.20] |
| Audit T1/T4 | Quinacrine “600×”, “0.0017%” | PARTIAL_ADOPT | “인체보다 훨씬 큰 apparent volume”으로만 압축; 세부 계산은 삭제. |
| Audit T1/T4 | “환자를 죽일 수 있는 추론” | PARTIAL_ADOPT | 교육적 과장 삭제; “처방 오판”으로 톤 완화. |
| Audit T1/T4 | “신부전 + 부종 $V$ 30–50% 증가” | REJECT | PDF 범위 내 근거 없는 정량 주장. |
| Audit T1/T4 | “신생아 체수분 1.5배”, gentamicin underdosing | REJECT | PDF 범위 내 근거 없는 정량 소아 주장. |
| Audit T1/T4 | midazolam high-extraction/liver cirrhosis scenario | REJECT | R&T excerpt는 midazolam PK 계산을 제공하나 high-extraction/간경변 추론을 전개하지 않음. |
| Audit T1/T4 | high/low extraction 약물 예시 | PARTIAL_ADOPT | $CL=Q\cdot E$는 유지하되 high/low 분기는 후속 hepatic clearance 세션으로 1문장 처리. |
| Audit T1/T4 | NONMEM code, TRANS1/TRANS2, GOF/CWRES | PARTIAL_ADOPT | PDF source-bound 내용은 아니므로 `<!-- TRENCH -->`와 [실무 확장/교과서 외 해석] 태그로 분리. |
| Audit T1/T4 | “FDA Deficiency Letter 약 30%”, ICH/TQT invented statistics | REJECT | 근거 없는 외부 규제 통계와 수치는 삭제. |
| Audit T2/T5 | G Fig.2.3, Fig.2.7, Case Study PK1 Tables 1.2/1.3 | ADOPT | $V$, $CL$, $MRT/t_{1/2}$의 핵심 source anchor. |
| Audit T2/T5 | G Table 1.1 raw data, sampling design advice | REJECT | 유익하지만 10분 handout 핵심이 아니며 실험설계 세션 성격. |
| Audit T2/T5 | G absorption/flip-flop/residual method | REJECT | 별도 흡수 세션 주제. |
| Audit T2/T5 | R&T Fig.3-1/3-2 A–D opening examples | ADOPT | $C_0$, slope, AUC 차이를 저자가 직접 여는 핵심 bridge. |
| Audit T2/T5 | R&T Fig.3-6 distribution vs elimination competing processes | ADOPT | terminal phase 일반화의 경계조건을 가르치는 핵심 bridge. |
| Audit T2/T5 | R&T renal clearance Table 3-2 / Fig.3-8/3-9 | REJECT | renal clearance 카드 승격 금지; context로 충분. |
| Audit T3 | R&T precision/computer-use comments | REJECT | metacognitive value는 있으나 현재 CL/V/t½ handout에서 우선순위 낮음. |
| Audit T4 #16–18 | Full extravascular, full tissue partition card, full renal clearance card | REJECT | Scope Lock에 따라 모두 후속 세션으로 이월. |
| Crucible Grade A Fix-1 | Subject 1 vs 4 자기모순 정정 | ADOPT | 가장 치명적인 source-fidelity 오류. |
| Crucible Grade A Fix-2 | 강한 임상·규제 어조 완화 | ADOPT | source-bound 학습자료의 문체 안정화. |
| Crucible Grade A Delete-3/4 | unsupported clinical numbers and FDA 30% | ADOPT | 모두 삭제. |
| Crucible Grade A Add-5/6 | R&T Fig.3-1/3-2, Fig.3-6 anchors | ADOPT | 문서 길이를 늘리지 않고 핵심 bridge 강화. |
| Crucible Grade A Tip-7 | TRANS1 vs TRANS2 covariate separation | PARTIAL_ADOPT | [실무 확장/교과서 외 해석]으로 태그한 1문장만 유지. |
| Crucible Grade A Tip-8 | Distribution-phase AUC fraction rule | ADOPT | R&T p.62–66에 직접 근거가 있어 $t_{1/2}$ limitation에 통합. |
| Crucible Grade A Compress-9 | Q9 Boss Dilemma invented 수치 제거 | ADOPT | source-bound mechanism trade-off 문제로 재구성. |
| Crucible Grade B TT-2/TT-3 | V vs $V_{ss}$ loading-dose caution, terminal λz practical checks | PARTIAL_ADOPT | 길이 증가 없이 [실무 확장] 1문장으로만 압축. |
| Crucible Grade B Pair 2 compression | $V$ vs $V_{ss}$ 혼동쌍 1/3 압축 | ADOPT | 본 세션은 1구획이므로 후속 가교 수준이 적절. |
| Crucible Grade B high/low extraction compression | 약물 예시 삭제, 후속 세션 예고 | ADOPT | source scope 유지. |
| Crucible Grade C | 추가 NONMEM streams, hepatic extraction 본격 도입, PBPK full expansion, renal card promotion, Volume Drift source-bound 유지 | REJECT | 모두 source 부재 또는 scope creep. |

---

## §1 — Session Header & Roadmap

<!-- MASTER LENS -->
<!-- ANNOTATION -->
**Big Idea:** $CL$과 $V$는 약물 disposition(← 분포와 소실을 묶은 체내 처리 과정)을 결정하는 두 primary coordinate이고, $K$와 $t_{1/2}$는 그 좌표가 만든 시간 그림자다. 즉 관찰되는 slope와 half-life는 원인이 아니라 결과다. 그림자($K$, $t_{1/2}$)만 보고 원인($CL$인지 $V$인지)을 단정하면 유지용량, 부하용량, 공변량 위치가 모두 틀릴 수 있다. [G p.17; R&T p.58]

```
IV bolus, 1-cmt, first-order
        │
        ├── Primary:  CL  ──┐
        │                   ├── K = CL/V ── t½ = ln(2)/K = 0.693V/CL
        └── Primary:  V   ──┘

Exposure/AUC  ← governed by CL
Initial concentration C0 ← governed by V
Mean residence time MRT ← 1/K only in 1-cmt IV bolus
```

<!-- ANCHOR -->
R&T의 opening figures가 이 구조를 가장 빠르게 보여준다. Drugs A/B는 같은 초기 농도에서 출발하지만 slope와 AUC가 다르다. 반대로 Drugs C/D는 같은 half-life를 보이지만 초기 농도와 AUC가 다르다. 즉 “처음 높이”와 “기울기”는 같은 정보가 아니라, 서로 다른 primary determinant가 표면에 드러난 모습이다. [R&T p.54–55]

이 세션은 다음 다섯 카드만 lock한다: **C1 Clearance → C2 Volume → C3 Elimination Rate Constant → C4 Half-life → C5 MRT**.

**선행:** 1차 ODE, 자연로그, plasma/blood/tissue 구분.  
**후속:** multi-compartment kinetics, absorption models, hepatic/renal clearance, PopPK covariate modeling, NCA moment analysis.

---

## §2 — Concept Anatomy Cards

### 🃏 C1. Clearance ($CL$) [Apex]

<!-- MASTER LENS -->
<!-- ANNOTATION -->
$CL$은 “농도가 얼마나 빨리 내려가는가”가 아니라 **단위 시간당 완전히 비워지는 가상의 혈장/혈액 부피**다. 이 관점에서 $CL=Q\cdot E$는 즉시 직관화된다. 혈류량 $Q$가 약물을 장기에 가져오고, 추출비 $E$(← 장기 통과 중 제거되는 비율)가 청소 효율을 정한다. 따라서 완전 추출자라도 $CL$은 $Q$를 넘을 수 없다. [R&T p.55–56]

#### A. Formal definition

**Clearance ($CL$):** 단위 시간당 혈장 또는 혈액에서 약물이 완전히 제거되는 apparent volume. 단위는 flow unit이다. [G p.16; R&T p.56]

$$
\text{Rate of elimination}=CL\cdot C \qquad [\text{R\&T Eq.3-4, p.56; G Eq.2:2, p.16}]
$$

$$
CL=Q\cdot E \qquad [\text{R\&T Eq.3-5, p.56}]
$$

#### B. Dose, AUC, and steady state

<!-- ANNOTATION -->
AUC는 시간 전체에 걸친 exposure integral(← 농도-시간 곡선 아래 면적)이다. 1차 IV bolus에서는 제거된 총량이 $CL\cdot AUC$로 표현된다. 전체 dose가 결국 제거되므로 다음 관계가 성립한다. [G p.19; R&T p.59–60]

$$
CL=\frac{Dose}{AUC_0^\infty}
$$

Constant infusion에서는

$$
\frac{dC}{dt}=\frac{R_{in}}{V}-\frac{CL}{V}C
$$

항정상태에서 $dC/dt=0$이므로

$$
C_{ss}=\frac{R_{in}}{CL} \qquad [\text{G Eq.2:22, p.23}]
$$

<!-- ANCHOR -->
여기서 $V$가 소거된다. $V$는 항정상태에 도달하는 **속도**를 바꾸지만, 동일 infusion rate에서 최종 $C_{ss}$는 $CL$이 결정한다. [G p.22–23]

#### C. Compound A anchor

Gabrielsson Case Study PK1은 4명에게 Compound A 10 mg IV bolus를 투여한 source-bound 계산 anchor다. [G p.469–475]

| Subject | Sex | $K$ (min⁻¹) | $V$ (L) | $CL$ (L/min) | $AUC$ (µg·min·L⁻¹) |
|---|---:|---:|---:|---:|---:|
| 1 | M | 0.01 | 10 | 0.1 | 98,000 |
| 2 | M | 0.02 | 9.8 | 0.2 | 49,000 |
| 3 | F | 0.02 | 10 | 0.2 | 51,000 |
| 4 | F | 0.01 | 20 | 0.2 | 51,000 |

[Source: G Tables 1.2/1.3, p.473–474]

<!-- ANCHOR -->
**정정된 핵심:** Subject 1과 4는 $K$와 $t_{1/2}$가 비슷하지만 $CL$은 다르다. S1은 $CL=0.1$ L/min, S4는 $CL=0.2$ L/min이다. S4에서는 $V$도 2배 커져 있으므로 $K=CL/V$가 우연히 비슷하게 보존된다. 따라서 같은 $R_{in}$에서는 $C_{ss}$가 같지 않다. [G p.473–474; G Eq.2:22, p.23]

#### D. Boundary and compression

- $CL=Q\cdot E$는 hepatic/renal clearance의 문을 열지만, high/low extraction 약물 예시와 장기별 모델은 후속 clearance 세션으로 넘긴다. [R&T p.56]
- Extravascular dosing에서는 $F$ 때문에 apparent parameter 해석이 필요하지만, $K_a$, $F$, $t_{lag}$는 흡수 세션 주제다. [G p.28–32]
- $CL_R=f_e\cdot CL$은 renal contribution을 분리하는 context로만 유지한다. [R&T p.66–68]

<!-- TRENCH -->
[실무 확장/교과서 외 해석] NONMEM에서 공변량을 $K$에 직접 묶으면 $CL$ 변화와 $V$ 변화가 한 항에 섞인다. `TRANS2`처럼 $CL$과 $V$를 분리해 두는 이유는 통계적 편의가 아니라 인과 위치 보존이다.

<!-- RECAP -->
**C1 Recap:** $CL$은 exposure와 maintenance dose를 결정하는 primary elimination parameter다. $t_{1/2}$이나 $K$가 아니라 $CL$을 먼저 물어야 한다.

---

### 🃏 C2. Volume of Distribution ($V$)

<!-- MASTER LENS -->
<!-- ANNOTATION -->
$V$는 실제 해부학적 부피가 아니라 **체내 총량을 혈장 농도로 환산하는 apparent dilution space(← 농도로 환산한 겉보기 분포공간)**다. 같은 100 units를 넣어도 물에만 녹으면 $V=10$ L, charcoal에 결합해 물에서 거의 안 보이면 $V=100$ L이 된다. 총량은 같지만 측정 가능한 농도가 다르기 때문이다. [G Fig.2.3, p.14–15; R&T p.63–64]

#### A. Formal definition

$$
V=\frac{A_b}{C} \qquad [\text{G Eq.2:14, p.20; R\&T Eq.3-26, p.63}]
$$

IV bolus에서는 back-extrapolated intercept로 다음을 계산한다.

$$
V=\frac{D_{iv}}{C^0} \qquad [\text{G Eq.2:13, p.20}]
$$

R&T는 time-zero extrapolation만으로 $V$를 확신하기 어려운 상황을 지적한다. 분포 평형이 완성되기 전의 intercept는 실제 분포공간을 안정적으로 대표하지 못할 수 있기 때문이다. 그래서 terminal phase에서 $CL$과 $k$로 $V$를 구하는 우회식을 제시한다. [R&T p.63]

$$
V=\frac{CL}{K}=1.44\cdot CL\cdot t_{1/2} \qquad [\text{R\&T Eq.3-27/3-28, p.63}]
$$

#### B. Why apparent volume can be huge

Gabrielsson은 $V$를 unbound volume과 free fraction으로 분해한다. [G p.20]

$$
V=V_u\cdot f_u \qquad [\text{G Eq.2:15, p.20}]
$$

Tissue partition까지 고려하면 $V_{ss}$는 혈액 부피와 조직별 분배계수의 합으로 표현된다. [G Eq.2:16–2:18, p.20–21]

$$
V_{ss}=V_B+\sum V_{Ti}\cdot K_{Pi}\cdot(1-E_{Ti})
$$

Quinacrine의 $V=40{,}000$ L는 apparent volume의 극단값이다. 이 값은 실제 체적이 아니라 tissue binding과 measurement space의 불일치를 흡수한 환산률로 읽어야 한다. [G p.20]

#### C. Compound A anchor

Compound A에서 Subject 1–3의 $V$는 약 10 L이고, Subject 4는 20 L이다. Gabrielsson Fig.1.2는 Subject 4의 낮은 intercept가 더 큰 volume을 의미한다고 설명한다. [G p.470, p.473]

<!-- ANCHOR -->
$V$가 커지면 동일 dose에서 $C^0=D/V$가 낮아진다. 그러나 $V$만으로 AUC가 결정되지는 않는다. AUC는 $CL$이 결정한다. [G Fig.2.6, p.17; G Fig.2.12, p.26–27]

#### D. Boundary and compression

- 1구획 모델에서는 $V$와 $V_{ss}$ 구분이 사실상 사라지지만, 다구획에서는 $V_c$, $V_{ss}$, terminal volume이 분기된다. 이 본격 전개는 distribution kinetics 세션으로 넘긴다. [G p.20–21; R&T p.61]
- $V$를 이용한 loading dose 계산은 분포 위상이 충분히 빠르다는 가정에 의존한다. [R&T p.62–64]

<!-- TRENCH -->
[실무 확장/교과서 외 해석] Semi-log plot에서 명백한 break point가 보이면, 1구획 $V$를 곧바로 loading dose에 쓰기 전에 central vs steady-state volume 문제를 점검한다.

<!-- RECAP -->
**C2 Recap:** $V$는 “약물이 어디에 얼마나 숨어 있는가”를 혈장 농도 하나로 환산한 apparent parameter다. $C^0$와 loading dose에는 직접적이지만, maintenance exposure는 $CL$이 결정한다.

---

### 🃏 C3. Elimination Rate Constant ($K$)

<!-- MASTER LENS -->
$K$는 독립적 제거 능력이 아니라 **체내 amount 중 단위 시간당 제거되는 fraction**이다. 즉 $K$는 “얼마나 잘 제거하는가”와 “얼마나 넓게 퍼져 있는가”의 비율이다. 제거 능력($CL$)을 분포 공간($V$)으로 나눈 값이므로 $K=CL/V$가 된다. [G p.17; R&T p.56]

#### A. Formal definition and ODE

$$
K=\frac{CL}{V} \qquad [\text{G p.17; R\&T Eq.3-7, p.56}]
$$

$$
\frac{dC}{dt}=-K\cdot C=-\frac{CL}{V}C \qquad [\text{G Eq.2:1, p.16; R\&T Eq.3-9, p.57}]
$$

적분하면

$$
C=C^0e^{-Kt}=\frac{D}{V}e^{-(CL/V)t} \qquad [\text{G Eq.2:4, p.17; R\&T Eq.3-10, p.58}]
$$

Semi-log plot에서는

$$
\ln C=\ln C^0-Kt
$$

이므로 slope가 $-K$다. [G Fig.2.4/2.6, p.15–17; R&T Eq.3-11, p.58]

#### B. Fractional elimination intuition

R&T Table 3-1은 $K=0.1$ hr⁻¹인 reservoir에서 100 mg이 1시간 후 90 mg, 2시간 후 81 mg, 3시간 후 72.9 mg으로 감소하는 예를 제시한다. 매 시간 “10 mg”이 아니라 **남아 있는 양의 10%**가 제거된다. [R&T p.57]

$$
\frac{A}{Dose}=e^{-Kt}=\left(\frac12\right)^n,\quad n=t/t_{1/2} \qquad [\text{R\&T Eq.3-19, p.59}]
$$

#### C. Boundary

- Distribution phase 중 관찰되는 빠른 decline은 반드시 elimination $K$가 아니다. midazolam은 초기 약 1시간 동안 distribution phase를 보인다. 이후 terminal phase에서 elimination half-life가 해석된다. [R&T p.61–62]
- Extravascular flip-flop에서는 terminal slope이 absorption rate를 반영할 수 있으므로 이 세션에서는 context로만 둔다. [G p.29–30]

<!-- TRENCH -->
[실무 확장/교과서 외 해석] `ADVAN1 TRANS1`에서 $K$를 직접 추정하면 fit 자체는 가능하지만, 공변량이 $CL$에 작용하는지 $V$에 작용하는지 분리하기 어렵다. `TRANS2`식 $CL/V$ parameterization은 후속 PopPK 해석 가능성을 보존한다.

<!-- RECAP -->
**C3 Recap:** $K$는 semi-log slope로 보이는 값이지만, 구조적으로는 $CL/V$다. slope가 변했을 때 $CL$이 변했는지 $V$가 변했는지는 별도 판단이 필요하다.

---

### 🃏 C4. Half-life ($t_{1/2}$)

<!-- MASTER LENS -->
$t_{1/2}$는 “약물이 빠지는 속도” 자체가 아니라 **$CL$과 $V$가 합성해 만든 시간 척도**다. 그러므로 $t_{1/2}$는 원인 변수가 아니라 결과 변수로 읽어야 한다. R&T의 핵심 문장은 명확하다: half-life와 elimination rate constant는 대개 $CL$과 $V$에 의존하지, 그 반대가 아니다. [R&T p.53, p.58]

#### A. Formal definition

$$
t_{1/2}=\frac{\ln 2}{K}=\frac{0.693\cdot V}{CL} \qquad [\text{G Eq.2:3/2:6, p.17–18; R\&T Eq.3-15/3-16, p.58}]
$$

같은 $CL$이라도 $V$가 다르면 $t_{1/2}$는 달라진다. R&T의 creatinine과 inulin 예시는 이 점을 직접 보여준다. [R&T p.58]

| Compound | $CL$ (L/hr) | $V$ (L) | $t_{1/2}$ (hr) | 해석 |
|---|---:|---:|---:|---|
| Creatinine | 4.5 | 42 | 6.5 | total body water에 가까운 분포 |
| Inulin | 4.5 | 16 | 2.5 | extracellular water에 가까운 분포 |

같은 $CL=4.5$ L/hr인데 $t_{1/2}$가 다른 이유는 $V$가 다르기 때문이다. [R&T p.58]

#### B. Time to steady state

Constant infusion에서 항정상태 도달 정도는 half-life 단위로 표현된다. Gabrielsson Fig.2.8은 1 half-life 후 50%, 2 half-lives 후 75%, 3 half-lives 후 87.5%, 3–4 half-lives 후 약 90% 도달을 보여준다. [G p.22]

R&T는 6.64 half-lives 후 약 99%가 제거된다고 설명한다. [R&T p.59]

<!-- ANCHOR -->
$V$는 $C_{ss}$ 자체를 바꾸지 않지만, $t_{1/2}=0.693V/CL$을 통해 항정상태 도달 시간을 바꾼다. 따라서 maintenance dose와 loading dose의 질문은 분리해야 한다. [G p.22–23]

#### C. Distribution phase limitation

R&T midazolam case는 7.5 mg base IV bolus 후 semilog profile이 biphasic이며, 초기 약 1시간은 distribution phase라고 설명한다. 이때 5분 시점 plasma에는 0.61 mg만 있고, 7.5 mg 중 6.9 mg, 즉 92%가 plasma 밖으로 분포되어 있다. [R&T p.61–62]

R&T Fig.3-5는 2시간까지 AUC가 전체 AUC의 48%라고 제시한다. Fig.3-6은 distribution과 elimination의 속도 경쟁을 두 시나리오로 설명한다. Midazolam처럼 distribution이 elimination보다 빠르면 terminal phase가 elimination을 대표하기 쉽다. [R&T p.64–65]

반대로 gentamicin은 terminal phase 도달 전 대부분의 elimination이 이미 발생한다. R&T는 gentamicin IV dose의 95% 초과가 distribution equilibrium 전에 urine으로 제거된다고 설명한다. 이 경우 terminal phase를 곧바로 “elimination 전체의 대표”로 읽으면 안 된다. [R&T p.66]

<!-- TRENCH -->
[실무 확장/교과서 외 해석] Terminal slope는 “마지막 직선”이 아니라 “분포 위상 오염이 충분히 작아진 뒤의 직선”으로 잡아야 한다. 최소 데이터 포인트, regression quality, AUC fraction을 함께 점검한다.

<!-- RECAP -->
**C4 Recap:** $t_{1/2}$가 길어졌다는 말은 원인 진단이 아니다. 반드시 “$CL$ 변화인가, $V$ 변화인가, distribution phase 문제인가”를 되물어야 한다.

---

### 🃏 C5. Mean Residence Time ($MRT$)

<!-- MASTER LENS -->
<!-- ANNOTATION -->
$MRT$는 약물 분자가 체내에 평균적으로 머무는 시간이다. $t_{1/2}$가 “절반으로 줄어드는 시간”이라면, $MRT$는 농도-시간 곡선의 시간 방향 평균이다. 즉 1차 모멘트(← 시간으로 가중한 농도 면적)를 AUC로 나눈 값이다. [G p.19; R&T p.60]

#### A. Formal definition

$$
AUC_0^\infty=\int_0^\infty C(t)dt \qquad [\text{G Eq.2:8, p.19}]
$$

$$
AUMC_0^\infty=\int_0^\infty t\cdot C(t)dt \qquad [\text{G Eq.2:10, p.19}]
$$

$$
MRT=\frac{AUMC_0^\infty}{AUC_0^\infty} \qquad [\text{G Eq.2:11, p.19}]
$$

1구획 IV bolus에서는 다음이 성립한다. [R&T Eq.3-25, p.60]

$$
MRT=\frac1K=\frac{t_{1/2}}{\ln 2}\approx1.443\cdot t_{1/2}
$$

#### B. Compound A anchor

| Subject | $K$ (min⁻¹) | $t_{1/2}$ (min) | $MRT$ (min) | $MRT/t_{1/2}$ |
|---|---:|---:|---:|---:|
| 1 | 0.01 | 68 | 98 | 1.44 |
| 2 | 0.02 | 34 | 48 | 1.41 |
| 3 | 0.02 | 36 | 53 | 1.47 |
| 4 | 0.01 | 71 | 100 | 1.41 |

[Source: G Table 1.3, p.474]

<!-- ANCHOR -->
4명 모두 $MRT/t_{1/2}$가 약 1.44에 모인다. 이 비율은 1구획 IV bolus에서 monoexponential decline이 성립한다는 수학적 signature다. 이 세션에서는 이 사실까지만 lock하고, 다구획 또는 extravascular MRT 전개는 후속 세션으로 보낸다. [G p.19, p.474; R&T p.60–61]

<!-- RECAP -->
**C5 Recap:** $MRT$는 NCA에서 “평균 체류 시간”을 주는 bridge parameter다. 1-cmt IV bolus에서는 $1/K$로 단순하지만, 이 단순성이 성립하는 조건을 기억해야 한다.

---

## §5 — Confusion Pair Dissection

### 🔀 Pair 1. $CL$ vs $K$ — Primary vs Secondary

<!-- CONFUSION -->

| 비교 | $CL$ | $K$ |
|---|---|---|
| 본질 | 단위 시간당 완전히 제거되는 apparent volume | 단위 시간당 제거되는 fraction |
| 단위 | volume/time | 1/time |
| 핵심식 | $CL=Dose/AUC=R_{in}/C_{ss}=Q\cdot E$ | $K=CL/V$ |
| 생리학적 위치 | 혈류, 추출, 대사, 배설 경로와 직접 연결 | $CL$과 $V$의 비율로만 해석 가능 |
| 임상 질문 | “노출과 유지용량이 어떻게 변하는가?” | “semi-log slope와 half-life가 어떻게 보이는가?” |

**Critical correction:** $K$가 같아도 $CL$이 같다는 뜻은 아니다. Compound A Subject 1과 4는 $K\approx0.01$ min⁻¹로 유사하지만 $CL$은 0.1 vs 0.2 L/min으로 다르다. [G p.473–474]

<!-- TRENCH -->
[실무 확장/교과서 외 해석] 통계적 fit이 좋아도 공변량을 $K$에 직접 묶으면 $CL$-mediated change와 $V$-mediated change가 분리되지 않을 수 있다. Fit 통과와 외삽 가능성은 같은 문제가 아니다.

### 🔀 Pair 2. $V$ vs $V_{ss}$ — Apparent bolus volume vs steady-state distribution

<!-- CONFUSION -->

| 비교 | $V$ | $V_{ss}$ |
|---|---|---|
| 본질 | $A_b/C$ 또는 $D/C^0$로 보는 apparent dilution space | 조직 분배계수와 tissue volume을 반영한 steady-state distribution space |
| 이 세션 처리 | 1구획에서는 사실상 같은 개념으로 사용 | 식의 의미만 context로 유지 |
| 위험 | 실제 해부학적 부피로 오해 | distribution kinetics 세션 내용을 이 세션에 과도하게 끌어옴 |

**Lock:** 본 세션에서는 “$V$는 apparent parameter”까지만 체화한다. $V_{ss}$의 본격 해석은 후속 distribution kinetics에서 다룬다. [G p.20–21; R&T p.63–64]

### 🔀 Pair 3. $t_{1/2}$ vs $MRT$

<!-- CONFUSION -->

| 비교 | $t_{1/2}$ | $MRT$ |
|---|---|---|
| 본질 | 농도/amount가 절반 되는 시간 | 분자가 체내에 머무는 평균 시간 |
| 수식 | $0.693/K=0.693V/CL$ | $AUMC/AUC$ |
| 1-cmt IV bolus | $t_{1/2}=0.693\cdot MRT$ | $MRT=1.443\cdot t_{1/2}$ |
| 해석 위험 | terminal phase 선택 오류 | AUMC terminal extrapolation 오류 |

<!-- RECAP -->
**§5 Recap:** 세 혼동쌍은 모두 “표면적으로 비슷하지만 위계가 다르다”는 문제다. $CL$ vs $K$는 primary/secondary의 차이다. $V$ vs $V_{ss}$는 apparent/steady-state의 차이다. $t_{1/2}$ vs $MRT$는 절반이 되는 시간과 평균 체류 시간의 차이다.

---

## §7 — Self-Test: Active Recall Module

<!-- SELF-TEST -->
### Q1 [회상 ★★]
$t_{1/2}$을 $V$와 $CL$로 표현하고, 왜 secondary parameter인지 설명하라.

**정답:**
$$
t_{1/2}=\frac{0.693V}{CL}
$$
따라서 $t_{1/2}$은 $V$와 $CL$의 함수다. $t_{1/2}$만 보고 $CL$ 감소인지 $V$ 증가인지 알 수 없다. [G p.17–18; R&T p.58]

### Q2 [회상 ★]
$V$의 정의식 두 가지를 쓰라.

**정답:**
$$
V=\frac{A_b}{C},\qquad V=\frac{D_{iv}}{C^0}
$$
또는 terminal phase 정보가 있으면 $V=CL/K=1.44CLt_{1/2}$로 계산한다. [G p.20; R&T p.63]

### Q3 [회상 ★]
$C_{ss}=R_{in}/CL$을 1구획 infusion ODE에서 도출하라.

**정답:**
$$
\frac{dC}{dt}=\frac{R_{in}}{V}-\frac{CL}{V}C
$$
항정상태에서 $dC/dt=0$:
$$
C_{ss}=\frac{R_{in}}{CL}
$$
$V$는 소거된다. $V$는 항정 도달 시간에 영향을 주지만 최종 $C_{ss}$ 자체는 $CL$이 결정한다. [G p.22–23]

### Q4 [회상 ○]
$MRT$의 정의식과 1구획 IV bolus에서 $t_{1/2}$와의 관계를 쓰라.

**정답:**
$$
MRT=\frac{AUMC}{AUC},\qquad MRT=\frac1K=1.443t_{1/2}
$$
단, 두 번째 등식은 1구획 IV bolus 한정이다. [G p.19; R&T p.60]

### Q5 [적용 ★★]
Compound A Subject 1과 4는 다음과 같다. 같은 infusion rate $R_{in}=10$ µg/min를 주면 $C_{ss}$는 같은가?

| Subject | $V$ (L) | $CL$ (L/min) | $K$ (min⁻¹) | $t_{1/2}$ (min) |
|---|---:|---:|---:|---:|
| 1 | 10 | 0.1 | 0.01 | 68 |
| 4 | 20 | 0.2 | 0.01 | 71 |

[Source: G Tables 1.2/1.3, p.473–474]

**정답:** 같지 않다.
$$
C_{ss,1}=10/0.1=100\;\mu g/L
$$
$$
C_{ss,4}=10/0.2=50\;\mu g/L
$$
두 subject는 $K$와 $t_{1/2}$가 비슷하지만 $CL$이 다르다. 항정 농도는 $CL$이 결정한다. [G Eq.2:22, p.23]

### Q6 [적용 ★★]
어떤 환자군에서 $t_{1/2}$가 길어졌다. 이것이 $CL$ 감소 때문인지 $V$ 증가 때문인지 구분하려면 무엇을 보아야 하는가?

**정답:** AUC와 $C^0$를 분리해서 본다. $CL$ 감소는 $AUC=Dose/CL$ 증가로 나타난다. $V$ 증가는 $C^0=D/V$ 감소로 나타난다. 따라서 둘이 동시에 변하면 $t_{1/2}$ 하나로는 원인 분리가 불가능하다. [G p.17–20; R&T p.58–60]

### Q7 [적용 ★]
R&T midazolam case: 79-kg adult, 7.5 mg base IV bolus, AUC = 287 µg·hr/L, $t_{1/2}=3.8$ hr.  
(a) $CL$은? (b) $V$는? (c) 5분 plasma concentration 180 µg/L, plasma volume 3.4 L이면 plasma 내 amount와 plasma 밖 fraction은?

**정답:**
$$
CL=7500/287=26.1\;L/hr\approx26\;L/hr
$$
$$
V=1.44\times26\times3.8=142\;L
$$
Plasma 내 amount는 $180\;\mu g/L\times3.4\;L=612\;\mu g=0.612$ mg. 따라서 $7.5-0.612=6.89$ mg, 약 92%가 이미 plasma 밖에 있다. [R&T p.61–63]

### Q8 [적용 ★]
어떤 IV bolus 자료에서 $MRT/t_{1/2}$가 1.85였다. 1구획 IV bolus의 기대값 1.443과 다르다. 무엇을 의심해야 하는가?

**정답:** 1구획 IV bolus의 단순 지수 감소가 아닐 가능성, 특히 distribution kinetics 또는 terminal extrapolation 문제를 의심한다. Source-bound 결론은 여기까지다. 구체적인 NONMEM ADVAN 선택은 후속 실무 모델링 판단이다. [G p.19; R&T p.60–66]

### Q9 — Source-bound Boss Dilemma ★★
새 IV bolus 약물이 semilog plot에서 biphasic decline을 보인다. 1구획 모델은 단순하고 AUC 중심 결정을 설명하기 쉽다. 2구획 모델은 distribution phase를 더 잘 설명하지만 현재 데이터가 sparse하다. 어떤 논리로 모델 구조를 방어해야 하는가?

**정답:** “어느 모델이 항상 옳은가”가 아니라 **distribution phase가 임상적으로 중요한 시간대인지**를 먼저 판단한다. Midazolam처럼 distribution이 빠르고 distribution phase AUC가 전체의 50% 미만이면 1구획 근사가 일부 목적에서 가능하다. 그러나 gentamicin처럼 terminal phase 전에 대부분의 elimination이 발생하면 terminal slope 중심 해석은 위험하다. 따라서 모델 선택은 통계적 단순성만이 아니라 concentration-time profile에서 distribution과 elimination이 경쟁하는 방식에 근거해야 한다. [R&T p.61–66]

<!-- RECAP -->
**§7 Recap:** 계산 문제의 핵심은 수식 암기가 아니라 “어떤 식에서 어떤 parameter가 소거되는가”를 보는 것이다. $C_{ss}$에서는 $V$가 소거되고, $t_{1/2}$에서는 $CL$과 $V$가 함께 남는다.

---

## §8 — Meta-Frame & Big Picture

### A. Positioning

이 세션은 PK/PD 학습 그래프의 출발점이다. 이후의 모든 구조는 여기서 갈라진다.

- **다구획 모델:** terminal phase가 정말 elimination을 대표하는지 묻는다. [R&T p.61–66]
- **Absorption models:** extravascular terminal slope가 $K$인지 $K_a$인지 묻는다. [G p.28–32]
- **Hepatic/Renal clearance:** $CL=Q\cdot E$와 $CL_R=f_e\cdot CL$을 장기별 생리학으로 분해한다. [R&T p.55–68]
- **PopPK covariates:** 공변량을 $CL$에 둘지 $V$에 둘지 결정한다. [실무 확장/교과서 외 해석]
- **NCA:** $AUC$, $AUMC$, $MRT$가 compartment model 없이 exposure와 residence time을 요약한다. [G p.19; R&T p.60]

### B. Dependencies — 대충 넘기면 생기는 실패 모드

1. **$t_{1/2}$ 단독 해석 오류**  
   $t_{1/2}$ 증가를 곧바로 $CL$ 감소로 읽으면 $V$ 변화 가능성을 놓친다. 정답은 항상 “AUC와 $C^0$가 어떻게 변했는가”를 같이 묻는 것이다. [G p.17–20; R&T p.58–60]

2. **$V$를 실제 부피로 오해**  
   $V=40{,}000$ L 같은 값을 보고 모델이 틀렸다고 판단하면 apparent volume 개념을 놓친 것이다. $V$는 측정 공간인 plasma concentration과 총량 사이의 환산률이다. [G p.20; R&T p.63–64]

3. **Terminal phase 자동 신뢰**  
   Midazolam처럼 terminal phase가 elimination을 잘 대표하는 경우도 있지만, gentamicin처럼 대부분의 elimination이 terminal phase 전에 끝나는 예외도 있다. [R&T p.61–66]

4. **$K$-direct parameterization의 해석 손실**  
   [실무 확장/교과서 외 해석] $K$에 공변량을 직접 묶으면 $CL$ 변화와 $V$ 변화가 구분되지 않는다. 이 세션의 primary/secondary 위계는 단순한 교과서 문장이 아니라 PopPK parameterization의 안전장치다.

### C. Professional Moat

자동화 도구는 IV bolus data에 monoexponential fit을 빠르게 수행하고 $CL$, $V$, $K$, $t_{1/2}$를 출력할 수 있다. 그러나 전문가의 가치는 **숫자를 출력하는 것**이 아니다. 핵심은 **숫자의 위계를 읽는 것**이다.

- $C_{ss}$가 다른 이유를 $t_{1/2}$가 아니라 $CL$에서 찾는다.
- $t_{1/2}$가 바뀌었을 때 $CL$인지 $V$인지 먼저 분해한다.
- Semi-log plot의 terminal straight line이 언제 elimination을 대표하지 않는지 안다.
- Source-bound statement와 [실무 확장/교과서 외 해석]을 구분한다.

<!-- RECAP -->
**Final Recap:** 1구획 IV bolus PK의 본질은 네 식으로 잠긴다: $CL=Dose/AUC$, $V=D/C^0$, $K=CL/V$, $t_{1/2}=0.693V/CL$. 그러나 handout의 진짜 목표는 식 암기가 아니라 위계 체화다. **$CL$과 $V$를 먼저 보고, $K$와 $t_{1/2}$를 그 결과로 읽어라.**

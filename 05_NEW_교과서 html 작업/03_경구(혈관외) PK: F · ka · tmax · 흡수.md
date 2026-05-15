# 03 — 경구(혈관외) PK: F · ka · tmax · 흡수 — v4.0

## 임상 장면으로 시작합시다 — 같은 숫자, 완전히 다른 결론

R&T 6장에 이런 예가 있어요. 같은 약을 i.m.으로 주면 $F$가 97%, 경구 용액으로 주면 $F$가 46%로 나옵니다 [R&T Table 6-1 / Fig.6-14, pp.183–184]. 이 두 숫자를 보고 "경구는 흡수가 느린 거구나"라고 말하는 순간, **속도(얼마나 빨리, $k_a$)와 양(얼마나 많이, $F$)이 머릿속에서 섞이기 시작합니다.** $F$는 속도가 아니라 도달한 양이거든요.

더 위험한 상황이 하나 더 있어요. 경구만 가지고 있는 데이터에서 $V/F$·$CL/F$·terminal slope를 각각 $V$·$CL$·$k_{el}$처럼 보고하는 경우입니다. 이 한 줄의 보고 문장이 임상 판단과 규제 판단을 통째로 흔들 수 있어요. 오늘 다룰 게 그 한 줄을 어떻게 정직하게 쓰는지입니다.

> 🎯 **[지금 이 슬라이드들이 존재하는 이유]** 경구 PK는 수식 암기가 아닙니다. $C(t)$·$F$·$k_a$·$V/F$·flip-flop을 보면서 **"이 곡선에서 무엇이 진짜 식별됐고, 무엇이 그냥 가정인지"**를 자동으로 의심하는 눈을 만드는 훈련이에요.

---

## 출처 및 범위 노트

> **Source A (G&W):** Gabrielsson & Weiner 5e, Ch.2 §§2.2.4–2.2.12 (pp.28–47), PK2 (pp.476–482), PK3 (pp.483–486)
> **Source B (R&T):** Rowland & Tozer 5e, Ch.6 (pp.169–195), Ch.7 (pp.197–220; context only), Appendix F (pp.781–784)
> **기호 약속:** $k_a$ = 흡수 속도상수, $k_{el}$ = 소실 속도상수, $V/F$ = 경구 데이터의 겉보기 분포용적, $CL/F$ = 겉보기 경구 청소율.

---

## §0. 큐레이션 지도

### 필수(MUST) — 체화할 5개 카드

| # | 개념 | 핵심 수식 / 출처 |
|---|---|---|
| 1 | **$C(t)$ Master Equation** | G&W Eq.2:32–2:35 [G&W p.30]; R&T Eq.6-3 [R&T p.172] + 적분해 Eq.F-1 [R&T p.782] |
| 2 | **$t_{max}$ / $C_{max}$** | G&W Eq.2:49–2:55 [G&W pp.34–35]; R&T Eq.F-6 [R&T p.783] |
| 3 | **생체이용률 $F$** | G&W Eq.2:71–2:74 [G&W pp.41–42]; R&T Eq.6-9–6-17 [R&T pp.183–186]; 소변 Eq.6-18–6-21 [R&T pp.187–188] |
| 4 | **APEX: $V/F$ + Flip-flop** | $V/F$ [G&W p.32; R&T p.185]; flip-flop [G&W Fig.2.17, p.30; R&T Case C, pp.175–176] |
| 5 | **$k_{a,app}$ vs $k_{a,true}$** | [G&W pp.40–41]; Eq.2:70 [G&W p.41] |

$$
\underbrace{V/F}_{\text{겉보기 V}},\quad \underbrace{CL/F}_{\text{겉보기 CL}},\quad \underbrace{F=\frac{k_{a,true}}{k_{a,true}+k_d}}_{\text{흡수/손실 경쟁}}
$$

### 맥락(CONTEXT) — 본문에 압축

| 항목 | 위치 | 처리 |
|---|---|---|
| Lag time | Card 1, 2 | Eq.2:39–2:42 [G&W pp.32–33]를 1차 흡수식의 시간 이동으로. |
| Method of Residuals | Card 2 | 초기 추정 알고리즘; Appendix F [R&T pp.781–783]. |
| Zero-order input | Card 1, §5 | Eq.2:66–2:67 [G&W p.38], Fig.6-2 [R&T p.171], PK3 [G&W pp.483–486] — "다른 입력 함수"로. |
| 다회투여/축적 | §8 | $R=1/(1-e^{-k_{el}\cdot\tau})$, Eq.2:78 [G&W p.45]는 다음 세션 의존성. |
| 다중 흡수 부위 | Card 5, §8 | Eq.2:80–2:82 [G&W pp.46–47] — 다중 peak / site heterogeneity 경고 한 줄. |
| Ch.7 흡수 생리학 / BCS | §8 | BCS·위배출·초회 통과를 흡수 변동성의 배경으로만 [R&T pp.197–220]. |
| Pidgeon-Pitlick / Vaughan, 국소 topical BE / microdialysis | 제외 | 본 세션 범위 밖. |

$$
\underbrace{R}_{\text{축적}}=\frac{1}{\underbrace{1-e^{-k_{el}\cdot\tau}}_{\text{잔존분 보정}}}
$$

---

<!-- SLIDE_START: §1 | title: 세션 헤더 및 로드맵 -->
<!-- SECTION_CORE: SC-01 -->

## §1. 세션 헤더 및 로드맵

**제목:** 경구 및 혈관외 투여의 PK — $F$ · $k_a$ · $t_{max}$ 그리고 흡수 단계가 만드는 모든 것

### 개념 지도 (3 layer)

```text
Layer 1 — 무엇인가
  Oral input | F | ka | tmax | flip-flop | apparent parameter

Layer 2 — 어떻게 계산되는가
  C(t) Master Equation | tmax 식 | F/Frel 식 | AUC = Dose/(CL/F) | ka,app 분해

Layer 3 — 언제, 왜 중요한가
  BE/food effect | V/F·CL/F reporting | terminal slope label | dose interval/accumulation | regulatory caveat
```

### 지식 그래프 위치

```text
[IV bolus 1구획 PK]
  → [이 세션: 경구/혈관외 흡수, F, ka, tmax, V/F, flip-flop]
  → [multiple dosing · modified-release · oral PopPK absorption model · BE/food effect]
```

🧭 **읽는 순서:**
- 카드 1 (M1): 경구 농도곡선은 왜 두 지수함수의 차이로 생기는가?
- 카드 2 (M2): 최고농도 시점은 왜 "흡수 완료"가 아니라 rate balance인가?
- 카드 3 (M3): $F$는 왜 속도가 아니라 전신 도달 정도인가?
- 카드 4 (M4): 경구 단독 데이터는 왜 $V$, $CL$, terminal slope label을 확정하지 못하는가?
- 카드 5 (M5): 적합된 $k_a$는 왜 실제 흡수속도가 아닐 수 있는가?

### 큰 그림

IV bolus는 약이 들어오자마자 전신 순환에 풀려서 **초기 농도 $C_0$**가 그 자리에서 만들어집니다. 경구나 혈관외 경로는 완전히 다르죠. 농도가 0에서 시작해서 천천히 올라가는데, 그게 그냥 "약이 늦게 들어오는" 일이 아니에요. **흡수와 소실이 동시에 일어나면서, 두 지수함수의 차이로 곡선이 만들어집니다.**

이 구조 때문에 $F$와 $V$가 $V/F$로 한 덩어리로 묶이고, $k_a$와 $k_{el}$이 terminal slope에서 자리바꿈할 수 있어요. 같은 dose라도 흡수 단계가 끼어드는 순간 oral 곡선의 peak는 IV bolus보다 낮아지고 시점도 뒤로 밀려요. 흡수는 단순히 "약이 늦게 들어오는 단계"가 아니에요 — **peak의 높이와 시점을 둘 다 다시 정하는 단계입니다** [R&T Fig.6-3, p.172].

### 한 줄 항법도

## 판정

**이번 Session 13 Phase 1은 “상당히 잘 나온 Draft v0”입니다. 그러나 “최적으로 완료된 Step 1 확정본”은 아닙니다.**
특히 이번 주제는 **IIV/BSV, RUV, covariate, genetic polymorphism**이 서로 얽히는 구간이라, unsupported 실무 해석이 들어가면 뒤 단계에서 오히려 혼란이 커집니다.

| 항목                  |         평가 |
| ------------------- | ---------: |
| Scope Lock 준수       | **8.0/10** |
| Curation Map 적절성    | **8.0/10** |
| R&T + G&W 역할 분담     | **8.5/10** |
| PK50 데이터 anchor 반영  | **8.5/10** |
| NONMEM 구현 번역의 출처 분리 | **6.0/10** |
| 출처 없는 규제/실무 문장 통제   | **5.5/10** |
| HTML 직행 가능성         |     **불가** |

**최종 판정:**
`Phase 1 재실행 불필요 / Phase 2 Source Fidelity Audit 필수 / HTML 직행 금지`

---

## 잘 된 부분

### 1. Curation Map의 4개 MUST 구조는 대체로 좋습니다.

Draft는 이번 세션을 **C1 θ/η/ε taxonomy → C2 residual error + shrinkage → C3 covariate modeling → C4 genetic polymorphism**으로 잡았습니다. 큰 흐름은 좋습니다. Scope Lock이 요구한 대로 R&T는 “왜 사람마다 다른가”의 임상·생리학적 프레임, G&W는 PK50의 실제 다중 피험자 데이터와 공변량 해석을 담당하도록 분리한 것도 잘 반영되었습니다.  

특히 Ch.13을 CYP2D6, CYP2C9, CYP2C19, NAT2, TPMT, VKORC1 각각의 세부 강의로 확장하지 않고, **“유전 다형성은 IIV 안의 불연속 substructure”**라는 하나의 MUST 카드로 압축한 것은 적절합니다. 이 판단을 하지 않으면 Phase 1이 약리유전학 요약집으로 비대해졌을 가능성이 큽니다.

### 2. PK50 anchor는 강력합니다.

G&W PK50의 CpD 사례를 잘 잡았습니다. 원문은 12명 환자에게 CpD 566 µg을 5시간 IV infusion으로 투여하고, total/unbound concentration을 비교하면서 plasma protein binding `fu`를 이용해 total parameter와 unbound parameter를 나누어 해석합니다. Table 50.1에서 total `Cl = 11.4 L/h, CV 28%`, unbound `Clu = 720 L/h, CV 9%`로 제시되어, Draft의 “total variability 일부는 protein binding 차이로 설명된다”는 핵심 주장은 잘 지지됩니다.  

또 PK50은 response가 exposure가 비슷해도 8배까지 달라지고, unbound EC50의 IIV가 total EC50보다 오히려 커지는 paradox를 보여줍니다. Draft가 이를 “PK covariate와 PD covariate는 다르다”는 혼동쌍으로 연결한 것은 좋은 교육 포인트입니다. 

### 3. R&T Ch.12의 핵심 메시지도 잘 들어갔습니다.

R&T는 평균값만이 아니라 **분포의 모양과 변이 폭 자체가 중요하다**고 설명하고, nortriptyline 25 mg tid를 복용한 263명에서 plateau plasma concentration이 linear scale에서는 skewed, log scale에서는 거의 symmetric해 log-normal 분포를 시사한다고 제시합니다. Draft가 log-normal IIV와 exponential IIV를 중심 구조로 둔 것은 이 원문 메시지와 잘 맞습니다. 

잔차 변이에 대해서도 R&T는 residual variability가 zero mean, variance σ²를 가져야 하며, additive/proportional/exponential error model을 제시합니다. Draft가 residual error model을 별도 카드로 둔 것은 타당합니다. 

---

## 반드시 고쳐야 할 문제

### 1. C2를 “Residual Error + Shrinkage” Apex로 둔 것은 약간 위험합니다.

Residual error model 자체는 이번 범위의 핵심입니다. 그러나 **η-shrinkage, 30% threshold, EBE shrinkage formula, Savic & Karlsson 2009, FDA Deficiency Letter**는 첨부 교과서 범위의 직접 내용이 아닙니다. Draft도 실제로 shrinkage 설명의 출처를 “R&T Ch.12 + Savic & Karlsson 2009”로 적고 있습니다. 

문제는 Scope Lock의 source가 R&T + G&W로 제한되어 있고, hard rule은 PDF에 없는 수치·조건·인용을 만들지 말라고 되어 있다는 점입니다. 

수정 권장:

```text
C2 제목 수정:
잔차 오차 모델 Additive / Proportional / Exponential / Mixed

Shrinkage 블록:
[교과서 외 후속 구현 지식]
η-shrinkage는 GOF/FOCE/EBE 세션에서 본격적으로 다룰 주제이며, 여기서는 residual error misspecification이 covariate 탐색을 왜곡할 수 있다는 forward pointer로만 둔다.
```

또는 Apex를 C1로 옮기는 것도 좋습니다.

```text
Apex 후보 재지정:
C1. θ/η/ε taxonomy + ω²/σ² 분해
```

이번 세션의 진짜 중심은 **분산의 구조적 분해**이지, shrinkage diagnostic 자체는 후속 GOF/EBE 세션에 더 가깝습니다.

---

### 2. NONMEM `$THETA/$OMEGA/$SIGMA` 코드는 출처 기반 본문이 아니라 구현 번역입니다.

Draft는 C1에서 NONMEM control stream을 직접 제시합니다. 내용 자체는 교육적으로 유용하지만, 이번 source는 R&T Ch.12–13과 G&W Ch.4/PK50입니다. PIPET이나 NONMEM 교재가 scope에 포함되어 있지 않습니다. 

따라서 이 코드는 그대로 두더라도 라벨을 바꿔야 합니다.

```text
[교과서 외 구현 번역]
아래 NONMEM control stream은 R&T/G&W의 variability 개념을 NONMEM 문법으로 옮긴 교육용 skeleton이다.
원문 교과서에 수록된 control stream은 아니다.
```

특히 `PIPET NONMEM categorical covariate` 같은 표현은 현재 Scope 밖입니다. 

---

### 3. “fu를 covariate로 넣으면 ω²(CL)이 28%→9%로 줄어든다”는 표현은 조금 과합니다.

원문이 직접 보여주는 것은 **total Cl의 CV 28%와 unbound Clu의 CV 9%**입니다. 즉, `fu`를 이용해 unbound parameter로 재표현하면 variability가 줄어든다는 것입니다. 

하지만 Draft처럼 “NONMEM covariate model이 ω²(CL)을 28%에서 9%로 깎는다”고 쓰면, 실제 population model에서 covariate effect를 추정한 결과처럼 들립니다. PK50은 교육용 다중 피험자 분석 및 unbound parameter derivation 사례이지, 완전한 NONMEM covariate model reduction 결과는 아닙니다.

수정 권장:

```text
수정 전:
fu를 covariate로 도입하면 ω²(CL)이 28%에서 9%로 줄어든다.

수정 후:
PK50에서는 total Cl의 CV가 28%였지만, fu를 이용해 unbound clearance Clu로 재표현하면 CV가 9%로 낮아졌다. 이는 protein binding 차이가 total concentration 기반 변이의 일부를 설명한다는 강한 데이터 anchor이다. NONMEM에서는 이 논리가 covariate model로 번역될 수 있다.
```

---

### 4. Deficiency Letter, 21 CFR 314.50, 18–24개월 지연, USD 200–500 million은 삭제 또는 라벨링해야 합니다.

Draft의 Confusion Pair에는 다음과 같은 문장이 들어갑니다.

> FDA Deficiency Letter, 21 CFR 314.50, 18–24개월 재제출 지연, USD 200–500 million 손실

이건 첨부 교과서에서 직접 확인되는 내용이 아닙니다. 
교육적 충격 효과는 있지만, Source Fidelity Audit에서는 **NOT_IN_SOURCE**로 잡힐 가능성이 매우 높습니다.

수정 권장:

```text
[교과서 기반]
ω²와 σ²를 혼동하면 between-subject variability와 residual variability의 해석이 붕괴하고, dose individualization 논리가 약해진다.

[교과서 외 실무 해석]
규제 제출 문서에서는 BSV와 RUV를 명확히 구분하고, residual model 선택 근거와 covariate model의 안정성을 별도로 제시해야 한다.
```

금액·개월 수·특정 법령 조항은 이 콘텐츠에서는 빼는 것이 안전합니다.

---

### 5. Mixed RUV를 “Phase 2/3 default”로 단정한 것도 낮춰야 합니다.

Draft는 mixed residual error model을 “권장 default for Phase 2/3”로 제시합니다. 
실무적으로 자주 쓰는 사고방식이지만, 원문 R&T가 말하는 것은 residual variability가 random이어야 하고, additive/proportional/exponential 모델이 사용된다는 수준입니다. 

수정 권장:

```text
수정 전:
Mixed — 권장 default for Phase 2/3

수정 후:
Mixed error model은 넓은 농도 범위와 LLOQ 근처 관측이 함께 존재할 때 자주 검토되는 실무적 선택지다. 다만 최종 선택은 residual diagnostic, assay 특성, OFV/AIC, predictive check에 근거해야 한다.
```

---

### 6. Genetic polymorphism 카드의 일부 수치는 Phase 2에서 재확인해야 합니다.

C4의 방향은 좋습니다. R&T Ch.13은 CYP2D6 functional gene copy 수에 따라 nortriptyline exposure가 달라지는 예를 제시하고, genetic polymorphism이 drug-metabolizing ability에 영향을 준다고 설명합니다.  

다만 Draft의 다음 문장들은 반드시 원문 대조가 필요합니다.

```text
CYP2D6 nortriptyline ~10배 차이
CYP2C9+VKORC1 warfarin ~4배 dose 차이
TPMT mercaptopurine ~10배 toxicity 차이
FDA Pharmacogenomic Biomarker label >200 drugs
warfarin 변이의 38% 미해명
```

이 중 일부는 맞을 가능성이 있지만, 일부는 최신 외부 지식 또는 다른 출처일 수 있습니다. 특히 “FDA label >200 drugs”는 current factual claim이므로 이번 PDF 기반 콘텐츠에서는 빼거나 `[교과서 외 최신 규제 맥락]`으로 분리해야 합니다. R&T Ch.13은 genotyping/phenotyping과 pharmacogenetic recommendation의 임상적 필요성을 설명하지만, 현대 FDA biomarker label 개수까지 이 범위에서 직접 보장하지는 않습니다. 

---

### 7. Ch.4 EDA의 메시지가 조금 더 살아야 합니다.

G&W Ch.4는 “수식으로 바로 뛰어들지 말고, 먼저 데이터를 plot하라”는 메시지를 강하게 둡니다. Spaghetti plot이 mean curve + error bar보다 variability를 더 잘 보여준다고 설명하고, NAD/NPD의 한계와 population approach 필요성을 제시합니다. 

Draft에서 이 부분은 CONTEXT로 들어갔지만, Session 13의 학습 목표상 **spaghetti plot → subgroup/covariate hypothesis 생성** 흐름은 조금 더 살리는 것이 좋습니다.

수정 권장:

```text
C1 또는 C3에 1개 anchor sentence 추가:
Spaghetti plot은 ω²을 숫자로 보기 전, “누가 central tendency에서 벗어나는가”를 눈으로 확인하는 첫 단계다. G&W Fig.4.2처럼 집단이 둘로 갈라져 보이면, 이는 covariate 또는 mixture model 후보를 생성하는 EDA 신호다.
```

---

## 종합 판정

이번 결과물은 **Phase 1 Draft v0로는 성공**입니다.
하지만 다음 6개는 Phase 2에서 반드시 잡아야 합니다.

```text
MUST_FIX

1. C2 Apex에서 shrinkage를 교과서 직접 내용처럼 다루지 말고 [교과서 외 후속 구현 지식]으로 격하.
2. NONMEM `$THETA/$OMEGA/$SIGMA`, `$ERROR` code를 [교과서 외 구현 번역]으로 라벨링.
3. “fu covariate가 ω²(CL)을 28%→9%로 줄인다”를 “total Cl CV 28% vs unbound Clu CV 9%”로 정확화.
4. FDA Deficiency Letter / 21 CFR / 18–24개월 / USD 200–500M 문장 삭제 또는 [교과서 외 실무 해석] 라벨링.
5. Mixed RUV를 “default”로 단정하지 말고, diagnostic 기반 선택지로 표현.
6. C4 genetic polymorphism의 배수·설명률·FDA label 개수 등 모든 수치를 PDF와 전수 대조.
```

## 다음 단계 권장

**Phase 1을 다시 돌릴 필요는 없습니다.**
바로 Phase 2 Source Fidelity Audit으로 넘기되, 감사 프롬프트에 아래 항목을 추가하세요.

```text
추가 감사 지시:

1. η-shrinkage formula, 30% threshold, Savic & Karlsson 2009, “vanishing covariate pattern”이 첨부 PDF source-supported인지 분류하라.
2. NONMEM `$THETA/$OMEGA/$SIGMA`, `$ERROR`, mixed RUV code가 원문 내용인지, 교과서 외 구현 번역인지 분류하라.
3. PK50에서 “fu covariate가 ω²(CL)을 28%→9%로 줄인다”는 표현이 정확한지 확인하라. 원문 기준으로 total Cl CV 28%와 unbound Clu CV 9%의 관계를 재기술하라.
4. FDA Deficiency Letter, 21 CFR 314.50, 18–24개월 지연, USD 200–500M 손실 표현이 PDF에 직접 있는지 확인하라.
5. C4 genetic polymorphism 카드의 CYP2D6, CYP2C9/VKORC1, TPMT, HLA-B*5701, FDA label 관련 수치가 R&T Ch.13 범위에 직접 있는지 확인하라.
6. G&W Ch.4의 EDA, spaghetti plot, NAD/NPD, population approach 메시지가 충분히 반영되었는지 확인하라.
```

**한 줄 결론:**
이번 Phase 1은 **구조와 데이터 anchor는 좋지만, NONMEM 구현·shrinkage·규제 문장이 source 범위를 넘어간 고밀도 초안**입니다. Phase 2에서 unsupported 실무 해석만 분리하면 좋은 Content Lock으로 갈 수 있습니다.

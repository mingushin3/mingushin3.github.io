# 세션 02 (리마스터판) — 분포의 비밀번호: 약은 어디에 숨었는가

> **이 문서의 위치.** 본 자료는 KoreanPKCov-Core 세션 02 "분포·단백결합·조직 분배" 보강본_final의 **재구성판(re-master)** 임. 다루는 범위·인용 출처·수식 anchor·결론은 보강본_final과 **완전히 동일**하며, 강의 동선·메타포·진입부·마무리 closure를 바꿔서 **"한 바느질로 꿰어진 느낌"** 을 만드는 것이 목적임. 변경 사항은 문서 말미의 변경 로그에 정리되어 있음.

---

## 강의실 도입 — 워파린 환자가 던진 질문 하나

박사과정생 한 명이 워파린 케이스 노트를 들고 옴. **신증후군**으로 알부민이 43 → 12.5 g/L로 떨어진 환자임. PK 파라미터가 같이 측정되어 있는데, 숫자가 좀 이상함.

| 파라미터 | 정상 알부민 시 | 저알부민혈증 시 | 방향 |
|---|---:|---:|:---:|
| $V$ | 9.4 L | 13.7 L | ↑ |
| $CL$ | 0.20 L/hr | 0.58 L/hr | ↑↑ |
| $t_{1/2}$ | 36 hr | 18 hr | ↓ |

[R&T 5e, Ch.4, Table 4-12, p.118]

박사과정생이 묻는 질문 — **"총 농도가 떨어졌으니까 출혈 위험은 줄어든 거 맞죠?"**

여기서 멈춰야 함. 이 한 질문에 "맞다"고 답하면 임상에서 환자가 다침.

왜냐하면 — 알부민이 떨어졌다는 건 약물을 붙잡고 있던 혈장 쪽 손이 풀렸다는 뜻임. 풀린 약물이 어디로 갔는지를 총 농도(채혈로 잡히는 단일 숫자) 하나로는 구별할 방법이 없음. 일부는 청소될 수 있고, 일부는 조직 쪽으로 더 깊게 들어갈 수 있고, 일부는 그냥 활성 형태로 떠다닐 수도 있음. 셋이 한 환자에서 동시에 일어남.

> 📚 **워파린 enantiomer 미리 알림.** 임상의 warfarin은 **R-warfarin과 S-warfarin의 racemic mixture (50:50)** 임. S-warfarin이 약 5배 강력하고 **CYP2C9**로 대사되며, R-warfarin은 **CYP1A2/CYP3A4**로 대사됨. 위 Table 4-12 수치는 **total racemate 합산 기준**임. 그래서 알부민 결합 변화에 대한 임상적 반응은 두 enantiomer의 합성 노출 변화로 봐야 함. 다음 청소율 세션에서 fluconazole–S-warfarin DDI(CYP2C9 억제)를 다룰 때 이 분리가 다시 필요해짐. [R&T 5e, Ch.4 Table 4-12 p.118; Appendix A pp.755–762]

이 챕터는 위 질문에 정식으로 답하기 위한 **좌표계**를 만드는 자리임. 챕터 마지막에서 워파린 환자한테 다시 돌아옴.

---

## 챕터 비밀번호 — 한 줄만 외워도 90%는 풀림

> ⚡ **V는 부피가 아님. V는 "약이 채혈로 안 보이는 어딘가에 얼마나 숨어 있는가"의 척도임.**

이 한 문장이 진짜로 와닿으면, 이 챕터에서 다루는 모든 개념이 자동으로 자기 자리를 찾아감.

왜냐하면 —

- **"큰 $V_d$"** 는 "약이 몸 안 넓게 퍼졌다"가 아님. **"채혈로 잡히는 농도가 작게 보일 만큼 약물이 어딘가에 깊게 숨었다"** 는 뜻임.
- **"총 농도가 낮다"** 는 "약이 적게 있다"가 아님. **"진열대(혈장)에 적게 나와 있다"** 일 뿐임. 창고(조직, 단백 결합)에 많을 수 있음.
- **"알부민이 떨어졌다"** 는 "단백질이라는 은신처가 사라진 것"임. 숨어 있던 약물이 풀려나면 동시에 두 가지가 일어남: (1) 청소 가능한 자유 약물이 늘어나서 $CL$이 빨라짐, (2) 조직 쪽 은신처로 더 들어갈 수 있어서 $V$가 커짐. 그래서 $t_{1/2}=0.693\cdot V/CL$의 분자와 분모가 같이 움직임 — **둘 중 어느 쪽이 더 가파르게 변하느냐가 $t_{1/2}$ 방향을 정함.**

이게 워파린 케이스에서 $t_{1/2}$이 18 hr로 짧아진 이유임. $CL$이 $V$보다 더 가파르게 늘었음.

> 💡 **이 챕터 전체를 한 비유로.** 분포는 약물 분자가 (1) **어디에**(혈장 단백/조직 인지질/적혈구/조직 단백), (2) **얼마나 강하게**($f_u$·$f_{uT}$·수송체비), (3) **얼마나 빨리**($Q/V_T$·막투과도) 숨고, 그 숨은 모습이 우리가 채혈로 보는 농도($C$)와 어떻게 다른지를 정량화하는 자리임. 그래서 가장 먼저 정해야 할 건 **"지금 보고 있는 농도는 어느 종(species)의 농도인가"** 임.

### 이번 챕터의 로드맵 (한 화면 정리)

```
강의실 도입 (워파린 환자)
    ↓
챕터 비밀번호 (V는 부피가 아님)
    ↓
§1 농도 좌표계 셋업 (C / C_u / C_b — 어느 매트릭스인가)
    ↓
§2 개념 해부 카드 6+1장
   ├── M1 약물을 막 너머로 미는 힘 → Cu 차이
   ├── M2 분포는 "범위"와 "속도"의 두 차원 문제
   ├── M3 V의 진짜 수학  ⚡Apex 
   ├── M4 혈장 쪽 은신처 — fu의 정체
   ├── M5 조직 쪽 은신처 — 큰 Vd의 정체
   ├── M5b 항체의 역설 — 작은 V + 긴 t1/2
   └── M6 노출 지표 선택 — 어느 종의 어느 시간 패턴
    ↓
§5 혼동쌍 4쌍 정리
    ↓
§6 워파린 케이스 풀기 (강의실 도입의 closure)
    ↓
§7 자기 테스트 / §8 메타프레임
```

> 📍 이 챕터를 통과 못 하면 다음 챕터(청소율·반복투여·TDM·PBPK·PopPK 공변량)가 다 흔들림. $f_u$는 well-stirred 간 청소율 식의 분자로, $V$는 부하 용량과 종말상 반감기의 결정인자로, 매트릭스(plasma vs blood)는 NONMEM 데이터셋의 단위로 모두 후속에 그대로 들어감.

---

## §1 — 농도라는 단어의 정체부터 정렬하기 (좌표계 셋업)

본 카드들로 진입하기 전에 한 가지를 정리해야 함 — **"농도"라는 단어를 그냥 쓰면 길을 잃음**. 세 가지 농도가 동시에 굴러다님.

| 농도 종 | 정의 | 어디서 쓰는 자리 |
|---|---|---|
| $C$ | 결합 + 비결합 전체, plasma 측정 | 임상 TDM 표준값, 부하 용량 계산 |
| $C_u$ | 단백 결합 안 한 자유 농도, plasma 기준 | 수용체 작용, 막투과, 종간 외삽 |
| $C_b$ | 전혈(whole blood) 농도, 적혈구 분획 포함 | tacrolimus·cyclosporine 등 RBC 결합 강한 약물 |

이 셋을 묶는 두 가지 변환식이 있음.

$$
\underbrace{C_u}_{\text{유리 }C}
=
\overbrace{C}^{\text{총 }C}
\times
\underbrace{f_u}_{\text{유리분율}}
$$

$$
\underbrace{\frac{C_b}{C}}_{\text{혈액/혈장비}}
=
1+\overbrace{H}^{\text{Hct}}\left(\underbrace{f_u\cdot K_{PBC}}_{\text{RBC 분배}}-1\right)
$$

[R&T 5e, Eq.4-17 p.105; App.D pp.775–776]

> 💼 **매트릭스 트랩(matrix trap) — 가장 먼저 확인할 것.** PK 보고서를 받으면 가장 먼저 묻는 것 — "이 농도는 어느 매트릭스에서 측정한 것인가?" **tacrolimus·cyclosporine은 whole blood**(RBC 결합 강함, $C_b/C \approx 15$), **warfarin·phenytoin은 plasma**, **digoxin은 serum**이 표준임. PopPK NONMEM 데이터셋의 농도 단위가 매트릭스별로 섞여 있으면, covariate 분석 이전에 단위 통일이 먼저임. 이 한 줄을 빼먹으면 모든 후속 분석이 다른 좌표계에서 돌아감.

> 📚 **$f_u$ vs $f_{ub}$ — 다음 챕터(청소율) 예고편.** R&T는 두 유리분율을 명시적으로 구분함.
> - **$f_u = C_u/C$**: plasma 기준 유리분율 (이번 챕터의 주역)
> - **$f_{ub} = C_u/C_b$**: blood 기준 유리분율 (다음 챕터의 well-stirred 간 청소율 식의 분자)
>
> $$
> \underbrace{f_{ub}}_{\text{혈액 }f_u} = \overbrace{f_u}^{\text{혈장 }f_u} \cdot \underbrace{\frac{C}{C_b}}_{\text{혈장/혈액비}}
> $$
>
> well-stirred 식 $CL_H = Q_H \cdot f_{ub} \cdot CL_{int} / (Q_H + f_{ub} \cdot CL_{int})$에 plasma 기준 $f_u$를 그대로 집어넣으면 systematic error가 생김. **IVIVE 단계에서 가장 흔한 단위 트랩 중 하나임.** [R&T 5e Ch.4 p.105; App.D pp.775–776]

좌표계 정리 끝. 이제 카드로 들어감.

---

## §2 — 개념 해부 카드 7장

### M1 · 막을 미는 진짜 힘 — 결합한 약은 못 지나감

**현장에서 왜 중요한가.** CNS 약물 디자인에서 logP·MW가 다 좋아 보이는데 in vivo BBB 침투가 깨지는 경우가 있음. 또는 같은 logP인데 약물 A는 뇌에 잘 가고 B는 안 가는 경우가 있음. 이 카드를 안 만져 놓으면 "왜?"라고 묻는 자리가 안 생김.

**한 줄 요지.** 막을 미는 구동력은 총 농도 차이가 아니라 **유리 농도 차이($C_u$ 기울기)** 임. 결합한 약은 막 앞에서 묶여 있음.

#### 정의 + 수식

$$
\underbrace{\text{Net rate of transport}}_{\text{순수송속도}}
=
\overbrace{P}^{\text{투과도}}
\cdot
\underbrace{SA}_{\text{표면적}}
\cdot
\overbrace{(C_{u,1}-C_{u,2})}^{\text{유리농도차}}
$$

[R&T 5e, Eq.4-1, p.80]

| 파라미터 | 단위 | 의미 | 변하는 원인 |
|---|---|---|---|
| $P$ | 길이/시간 | 막 구조·지용성·전하·수송체가 다 들어간 거시 투과도 | ↑ 지용성·유입수송체, ↓ 큰 MW·이온화·efflux |
| $SA$ | 면적 | 확산이 일어나는 막 표면적 | 조직 구조, 모세혈관 표면적 |
| $C_{u,1}-C_{u,2}$ | 농도 | **막을 실제로 미는** 농도 기울기 | 단백결합, pH partition, 능동수송 |

#### 직관 비유 — 공항 입국심사대

총 농도($C$)는 공항에 들어온 사람 전체임. 그런데 그중 다수가 입국심사대(혈장 단백·조직 단백)에서 묶여 있음. 실제로 입국장 통과를 시도하는 인원은 **자유로운 사람(=$C_u$)** 만임. 그래서 양쪽 입국장의 자유 인원 차이가 줄을 정함.

#### 결정 축 — 출처 기반 상세

| 축 | 데이터 anchor | 임상 사례 |
|---|---|---|
| 크기(MW) | MW 400→800에서 피부 투과도 약 300배↓ [R&T 5e, Fig.4-3, pp.81–82] | **Atenolol** 246 / **oxytocin** 1007 / **calcitonin-salmon** 3432 g/mol — 비강 흡수 약 3% [R&T 5e, p.81] |
| 지용성 | BBB 투과도가 logP와 대체로 같이 ↑ [R&T 5e, Fig.4-4, p.82] | 단, **vinblastine·vincristine**은 P-gp 기질이라 기대보다 낮음 |
| 전하/pH | 비이온화형이 지질막 주통과 [R&T 5e, p.83; App.B pp.763–765] | 약산·약염기 pKa별 pH partition |
| 수송체 | passive facilitated = 평형 속도 변화, **active = 정상상태 $C_u$ 비율 자체 변화** | $\dfrac{C_{u,T}}{C_u}=\dfrac{P_{uptake}}{P_{efflux}}$ [R&T 5e, Eq.4-26, p.110] |

> 📖 **R&T Fig.4-4 (p.82) — logP 하나로 BBB 예측의 실패 사례:** 같은 logP에서도 **caffeine**은 BBB를 잘 통과하고 **vinblastine·vincristine**은 P-gp efflux 때문에 기대보다 훨씬 덜 들어감. → **"BBB 투과도 = logP의 함수"라는 단축식이 깨지는 자리**임.

#### 능동 수송이 있을 때

$$
\underbrace{\frac{C_{u,T}}{C_u}}_{\text{조직/혈장 유리비}}
=
\overbrace{\frac{P_{uptake}}{P_{efflux}}}^{\text{유입/유출 비}}
$$

[R&T 5e, Eq.4-26, p.110]

> 🔑 **수동 vs 능동 수송체의 분리.** 수동 촉진 수송체는 **평형 도달 "속도"**를 바꿈. 능동 수송체는 **정상상태 $C_u$ "비율" 자체**를 바꿈. 둘은 다른 차원의 영향을 줌. CNS 약물 평가에서 P-gp/BCRP efflux를 누락하면 in vivo에서 깨지는 첫 번째 자리임.

> 💼 **실무 인사이트:** logP·MW 다 좋아 보이는 CNS 후보가 in vivo BBB 침투가 낮으면 → **efflux transporter 기질성 + 이온화 + 크기**를 동시에 의심해야 함. "지용성 = 투과도" 단축식으로 가면 P-gp/BCRP·pH partition 예외를 다 놓침.

#### 이 카드 한 줄

🎯 **막을 넘는 힘은 $P\cdot SA\cdot (C_{u,1}-C_{u,2})$ — 결합한 약은 막 앞에서 묶여 있다는 사실 하나가 이 카드 전체임.**

---

### M2 · 분포는 두 차원 문제 — "범위"와 "속도"는 다른 축

**현장에서 왜 중요한가.** "$V_d$가 크니까 빨리 분포한다"고 묶어서 말하는 보고서가 많음. 이 한 문장에 두 가지 차원이 섞여 있음 — **얼마나 멀리 가는가**와 **얼마나 빨리 가는가**. 둘을 합치면 채혈 설계와 onset 해석이 동시에 어긋남.

**한 줄 요지.** 분포 **범위**는 $K_p$·$V$·$f_{uT}$가 정하고, 분포 **속도**는 $Q/V_T$와 막 투과도가 정함. 두 축은 독립임.

#### 관류 율속(perfusion-rate limited) 식

막 통과가 충분히 빠르면 조직 농도가 평형값에 접근하는 속도는 **혈류 공급 속도**가 정함.

$$
\underbrace{k_T}_{\text{접근속도}}
=
\frac{\overbrace{Q/V_T}^{\text{조직관류}}}{\underbrace{K_{pb}}_{\text{조직저장}}}
$$

$$
\underbrace{t_{1/2,\text{distribution}}}_{\text{분포 반감기}}
=
\frac{\overbrace{0.693}^{\ln 2}\cdot\underbrace{K_{pb}}_{\text{조직저장}}}{\overbrace{Q/V_T}^{\text{조직관류}}}
$$

$$
\underbrace{C_T(t)}_{\text{조직농도}}
=
\overbrace{K_{pb}\cdot C_A}^{\text{평형농도}}
\cdot
\underbrace{(1-e^{-k_Tt})}_{\text{접근분율}}
$$

[R&T 5e, Eq.4-5~4-7, p.97]

#### 직관 비유 — 수도꼭지와 탱크

$Q/V_T$는 수도꼭지의 물줄기, $K_{pb}$는 채워야 할 탱크 크기임. **같은 수도꼭지여도 탱크가 커지면 최종 저장량은 커지지만 가득 차는 데 더 오래 걸림.** 그래서 큰 $K_{pb}$는 동시에 두 가지 의미를 가짐 — "많이 들어감"과 "평형 도달이 늦음."

#### 조직별 관류 + 임상 사례

| 조직 | 관류, mL/min/g | 의미 |
|---|---:|---|
| Lung | 10.0 | 평형 매우 빠름 |
| Kidney | 4.0 | 혈류 풍부 |
| Brain | 0.5 | 혈류는 높지만 BBB가 별도 제한 |
| Adipose | 0.025 | 매우 낮은 혈류 — 높은 $K_p$ 약물에서 평형 도달 지연 |
| 비활동 근육 | 0.025 | 큰 조직 질량 + 낮은 관류 |

[R&T 5e, Table 4-4, p.96]

- **Thiopental**(초단시간 정맥마취제, 고지용성 barbiturate) IV 25 mg/kg 개 실험 — 뇌는 빠르게 오르고 빠르게 빠지는데, 지방은 **낮은 관류 + 높은 친화도** 조합 때문에 3시간 뒤에도 상당량 잔존. → **"큰 창고에 좁은 시골길로 들어가면 최종 저장은 많아도 도착은 늦다"** 의 임상 사례. [R&T 5e, Fig.4-13, p.94]
- **고분자/림프 극단:** 대분자는 혈관벽 통과가 제한되어 림프 회수가 분포 속도를 지배. 림프 유속 `1–10 mL/min per 70 kg`. MW > 5000 g/mol에서 투과 제한·림프 회수가 동시에 작동. [R&T 5e, Fig.4-14 p.95; Table 4-1 p.84]
- **Penicillin G** — 근육에서는 잘 분포하지만 **뇌·CSF는 투과 제한 우세**. 같은 약물도 조직마다 율속 단계가 다름. [R&T 5e, Fig.4-17 p.99; Fig.4-18 p.100]

> ⚠️ **혼선 주의.** $V_d$나 $K_p$는 **얼마나 많이**(범위)를 말함. $Q/V_T$·투과도·$k_T$는 **얼마나 빨리**(속도)를 말함. 두 차원을 같은 축에 올리는 순간 해석이 깨짐.

#### 이 카드 한 줄

🎯 **분포는 "어디까지(범위)"와 "얼마나 빨리(속도)"의 두 차원 문제 — 채혈 설계와 onset 해석은 속도 축에서, 부하 용량과 평형 노출은 범위 축에서 결정함.**

---

### M3 · V의 진짜 수학 — 부피가 아니라 압축된 숨바꼭질 지도 ⚡ Apex

**현장에서 왜 중요한가.** 임상에서 가장 자주 어긋나는 자리가 이거임 — "$V_d$가 크면 약이 몸의 넓은 공간에 들어가 있다"고 읽는 순간 보고서 전체가 틀어짐. 알부민 covariate을 $V$에만 붙이고 $CL$을 빠뜨림, 부하 용량 계산을 $V_\beta$로 함, plasma assay에 whole blood 약물의 노출을 비교함 — 다 이 한 오해에서 시작됨.

**한 줄 요지.** $V$는 "Amount in body / 관측 농도"의 **압축된 비율**임. 약물이 어딘가에 깊게 숨을수록 $C$가 작게 보이고 $V$는 커짐. **부피가 아니라 "보이지 않게 숨은 정도"의 척도임.**

#### 정의 — V는 비율, 그 이상도 이하도 아님

$$
\underbrace{V}_{\text{겉보기 }V}
=
\frac{\overbrace{\text{Amount in body}}^{\text{총량}}}{\underbrace{C}_{\text{측정 }C}}
=
\frac{\overbrace{A}^{\text{약물량}}}{\underbrace{C}_{\text{농도}}}
$$

[R&T 5e, Eq.4-8, p.102]

> 💡 V가 500 L라고 해서 체내에 500 L 공간이 있다는 뜻이 **절대로** 아님. 사람 몸은 그렇게 안 큼. **관측 $C$가 아주 낮으면 $A/C$는 생리 부피를 훌쩍 넘어감 — 그게 약이 어딘가에 깊게 숨었다는 신호임.**

#### 직관 비유 — 창고와 매장 진열대

$V$는 창고의 실제 크기가 아니라 **"창고 전체 재고를 매장 진열대 농도로 나눠본 가상 매장 크기"** 임. 진열대($C$)에 적게 보일수록 같은 재고도 훨씬 큰 매장처럼 계산됨. 약이 조직 어딘가에 숨어 있을수록 진열대는 비어 보이고, $V$ 숫자는 커짐.

#### 두 칸 모델로 풀어내기

체내를 혈장 칸($V_p$)과 조직 칸($V_T$)으로 단순화하면:

$$
\underbrace{A}_{\text{총량}}
=
\overbrace{V_p\cdot C}^{\text{혈장 재고}}
+
\underbrace{V_T\cdot K_p\cdot C}_{\text{조직 재고}}
$$

$$
\underbrace{V}_{\text{겉보기 }V}
=
\overbrace{V_p}^{\text{혈장항}}
+
\underbrace{V_T\cdot K_p}_{\text{조직항}}
$$

[R&T 5e, Eq.4-11~4-13, pp.103–104; G&W 5e, Eq.2:16, p.20]

전신 합산으로 일반화하면:

$$
\underbrace{V}_{\text{전체 }V}
=
\overbrace{V_p}^{\text{혈장항}}
+
\sum_i\underbrace{V_{T,i}\cdot K_{p,i}}_{\text{조직 }i\text{ 기여}}
$$

#### $K_p$를 결합으로 다시 쓰면 — 이 카드의 척추

$K_p$ 자리를 **혈장 쪽 유리분율 / 조직 쪽 유리분율**로 풀어 쓸 수 있음.

$$
\underbrace{V}_{\text{겉보기 }V}
=
\overbrace{V_p}^{\text{혈장항}}
+
\underbrace{V_{TW}\cdot
\frac{\overbrace{f_u}^{\text{혈장 }f_u}}{\underbrace{f_{uT}}_{\text{조직 }f_u}}}_{\text{결합조직항}}
$$

[R&T 5e, Eq.4-25, p.109]

> 💡 $f_u/f_{uT}$는 혈장과 조직 사이의 **"붙잡는 손 힘의 비율"** 임. 조직 쪽이 더 세게 붙잡으면($f_{uT}$↓), 혈장에는 약이 적게 보이고 $V$는 커짐.

수송체가 조직 분포를 지배하는 경우:

$$
\underbrace{V}_{\text{겉보기 }V}
=
\overbrace{V_p}^{\text{혈장항}}
+
\underbrace{V_{TW}\cdot\frac{f_u}{f_{uT}}}_{\text{결합조직항}}
\cdot
\overbrace{\frac{P_{uptake}}{P_{efflux}}}^{\text{수송체항}}
$$

[R&T 5e, Eq.4-29, p.111]

#### 측정 매질이 바뀌면 V도 바뀜

$$
\underbrace{V_u}_{\text{유리 }V}=\frac{\overbrace{A}^{\text{총량}}}{\underbrace{C_u}_{\text{유리 }C}},\qquad
\underbrace{V_b}_{\text{혈액 }V}=\frac{\overbrace{A}^{\text{총량}}}{\underbrace{C_b}_{\text{혈액 }C}}
$$

[R&T 5e, Eq.4-14~4-15, p.104]

> ⚠️ **NONMEM 데이터셋에서 가장 흔한 단위 트랩.** 분모 농도가 plasma인지 whole blood인지 unbound인지에 따라 $V$ 숫자가 통째로 다른 좌표계임. 표 헤더의 단위 한 줄을 빼먹으면 covariate 분석이 다른 행성에서 돌아감.

#### 소 $V_d$ 알부민 결합 약물 모델

알부민 자체가 혈관 외 알부민 공간까지 분포하기 때문에, $f_u\to 0$이어도 $V$가 0으로 가지 않음. **알부민 분포 용적 약 7.5 L 근처에서 하한이 잡힘.**

$$
\underbrace{V}_{\text{소 }V_d}
=
\overbrace{7.5}^{\text{알부민 하한}}
+
\underbrace{\left(7.5+\frac{V_R}{f_{uR}}\right)}_{\text{잔여분포}}
\cdot
\overbrace{f_u}^{\text{혈장 }f_u}
$$

[R&T 5e, Eq.4-30, p.112; App.C Eq.C-13, pp.767–773]

#### 데이터 앵커 — 한눈에

| anchor | 값 | 의미 |
|---|---|---|
| 혈장 / 세포외액 / 총 체수분 | 3 / 16 / 42 L | $V$ 해석의 생리 기준점 [R&T 5e, p.111] |
| 알부민 겉보기 분포용적 | 약 7.5 L | 소 $V_d$ 알부민 결합 약물의 하한 [R&T 5e, p.111; App.C pp.767–771] |
| Cephalosporin Fig.4-25 외삽 절편 | 약 7 L | 위와 일치 [R&T 5e, Table 4-5 p.101; Fig.4-25 pp.112–113] |
| Cephalosporin $V$ vs $V_u$ | $V$ ↑with $f_u$, $V_u$ ↓with $f_u$ | $V$와 $V_u$는 같은 생리 의미가 아님 [R&T 5e, Fig.4-25~4-26, p.113] |
| Warfarin 신증후군 | $V$ 9.4→13.7, $CL$ 0.20→0.58, $t_{1/2}$ 36→18 (racemic) | 저알부민혈증에서 모두 함께 움직임 [R&T 5e, Table 4-12, p.118] |
| **Adalimumab** | $V$ 약 5–6 L | 고분자 항체는 혈관 내에 가둬짐 [R&T 5e, p.111] |
| **Caffeine·alcohol** | $V$ ≈ 42 L | 자유 투과 소분자는 총 체수분 접근 [R&T 5e, p.111] |

> 📚 **Cephalosporin Fig.4-25 — 학습자 주의:** Dudley & Nightingale (1982) 11종 비교 데이터. **cefonicid**가 가장 강한 알부민 결합 prototype. 인용 study의 dose 영역은 임상 통상 용량(예: 1 g IV q24h ≈ 15 mg/kg)을 넘어서는 **약동학 평가용 dose(30 mg/kg 수준)** 까지 포함됨. 이건 **saturable albumin binding을 명시적으로 드러내기 위한 study design**임. **임상 용량 영역에서 동일 nonlinearity가 나타난다고 일반화하면 안 됨.** [R&T 5e, Fig.4-25, p.113; Dudley MN, Nightingale CH. 1982]

#### 가장 자주 빠지는 함정 — "$V_d$ = 실제 부피"

박사과정생이 가장 자주 하는 실수임. 이름에 "volume"이 들어가고, 부하 용량 식 $LD=V\cdot C_{target}$에 직접 들어가서 실제 부피처럼 느껴짐.

이걸 그대로 두면 나비효과가 남:
- **임상**: "총 농도는 정상인데 유리 농도가 달라진 환자"를 그대로 놓침.
- **모델링**: NONMEM에서 albumin을 $V$에만 기계적으로 붙이고 $CL$ 쪽을 빠뜨림.
- **규제**: FDA Deficiency Letter 또는 재분석 요구.

> 💼 **알부민 공변량 비대칭.** 대 $V_d$ 약물에서 알부민을 $V$ covariate으로만 넣고 $CL$을 안 보면 총 농도 기준 $CL$ 변화가 통째로 누락됨. **NONMEM 진단: ETA-CL vs albumin이 ETA-V vs albumin보다 강한 상관을 보이면 $CL$ covariate도 검토.**

> 💼 **$V_{ss}$ vs $V_\beta$.** 다구획에서 **부하 용량은 $V_{ss}$**, **종말상 반감기 해석은 $V_\beta$.** NONMEM 출력에서 어느 $V$를 쓰는지 끝까지 확인.

> 📖 **R&T Fig.4-25·4-26 (p.113):** 같은 cephalosporin 계열에서 $f_u$↑에 따라 $V$↑·$V_u$↓ — **두 곡선이 반대 방향**. → $V$와 $V_u$를 같은 생리 의미로 합쳐 해석하면 안 되는 자리.

#### 이 카드 한 줄

🎯 **$V=A/C$ — 부피가 아니라 "보이지 않게 숨은 정도"임. 매트릭스($C$/$C_u$/$C_b$)·결합비($f_u/f_{uT}$)·수송체비($P_{uptake}/P_{efflux}$)가 $V$를 만드는 세 부품임.**

---

### M4 · 혈장 쪽 은신처 — $f_u$는 진짜 상수인가

**현장에서 왜 중요한가.** $AUC_u = AUC \times f_u$라는 단축식을 무비판적으로 쓰는 자리가 많음. 그런데 $f_u$가 시간·농도·용량에 따라 변하는 약물이 있음. 이때 단축식을 그대로 쓰면 SAD에서 dose-normalized AUC가 비선형으로 떨어질 때 그 원인이 청소율인지 결합인지를 분리할 수 없게 됨.

**한 줄 요지.** $f_u$는 약물·단백질·농도 셋의 함수임. **"$f_u$ = 상수"는 검증해야 할 가설이지 자동 사실이 아님.**

#### 정의 + 수식

$$
\underbrace{f_u}_{\text{유리분율}}
=
\frac{\overbrace{C_u}^{\text{유리 }C}}{\underbrace{C}_{\text{총 }C}}
$$

[R&T 5e, Eq.4-17, p.105]

#### 직관 비유 — 주차장

단백결합은 주차장임. 
- $K_a$ = 차가 들어가면 얼마나 세게 붙잡히는지 (친화도)
- $P_t$ = 총 주차 공간 (단백 농도)
- $C_u$ = 도로에 남은 차 수 (자유 약물)

**주차장이 포화되면 도로 위 차($C_u$)가 갑자기 늘어남.** 이게 dose-linearity가 깨질 때 첫 번째로 의심해야 할 메커니즘임.

#### 결합 친화도와 mass-law

단일 결합 부위에서:

$$
\underbrace{K_a}_{\text{결합친화도}}
=
\frac{\overbrace{C_{b,t}}^{\text{결합농도}}}{\underbrace{C_u}_{\text{유리농도}}\cdot\overbrace{P}^{\text{빈 결합부위}}}
$$

[R&T 5e, Eq.4-18, p.105]

질량작용 관계식(R&T 본문):

$$
\underbrace{f_u}_{\text{유리분율}}
=
\frac{1}{1+\overbrace{K_a}^{\text{친화도}}\cdot\underbrace{f_{up}}_{\text{유리 단백분율}}\cdot\overbrace{P_t}^{\text{총 단백농도}}}
$$

[R&T 5e, Eq.4-19, p.105]

#### 단백질 종류로 분기 — Albumin vs α₁-Acid Glycoprotein

약물 종류에 따라 결합하는 단백질이 다르고, 질환 상태에서 두 단백질이 다른 방향으로 움직임. [R&T 5e, Table 4-9, p.114]

| 결합 단백질 | 결합하는 약물 클래스 | 정상 농도 (g/L) | 변화 방향 |
|---|---|---:|---|
| **Albumin** | 약산성 약물 (warfarin, phenytoin, salicylates, valproate, NSAIDs) | 35–50 | **↓** 간질환, 화상, 신증후군, 말기신부전, 임신 |
| **α₁-Acid glycoprotein (AAG)** | 약염기성 약물 (propranolol, lidocaine, methadone, imipramine, chlorpromazine) | 0.5–1.0 | **↑** 심근경색, 수술 후, Crohn, 외상, 류마티스 관절염 |

> 🔑 **AAG = Acute phase reactant.** AAG는 **염증·외상·수술·종양**에서 동적으로 증가하는 단백질임. 그래서 **염기성 약물의 $f_u$가 질환 상태에서 감소** 방향으로 움직임. **ICU·외상·패혈증 환자에서 propranolol·lidocaine·methadone의 total 농도가 정상이어도 활성 $C_u$는 현저히 감소할 수 있음.** TDM을 total 농도로만 하면 effect 부족을 놓침. [R&T 5e, Fig.4-22 p.108; Table 4-9 p.114; Tozer 1983]

- **Propranolol** 78명(신질환·관절염·Crohn·간경변)에서 $f_u$가 AAG 농도에 따라 **0.04–0.16** 사이로 변동. 분자 농도 자체는 AAG 결합 용량 이하 → **결합 단백 농도 변화가 $f_u$의 1차 결정인자**. [R&T 5e, Fig.4-22, p.108]

#### PK47 — 모델 식별성(identifiability) 문제

G&W PK47은 $f_u$를 $C_u$·총 단백 $[P_T]$·부위 수 $n$·친화도 $K_a$의 함수로 풀어냄.

$$
\underbrace{f_u}_{\text{유리분율}}
=
1-
\frac{1}{1+
\overbrace{\dfrac{C_u}{n[P_T]}}^{\text{농도/용량비}}
+
\underbrace{\dfrac{1}{K_a\cdot n[P_T]}}_{\text{용량 역항}}}
$$

[G&W 5e, Eq.47:1, p.691]

저 $C_u$ 근사:

$$
\underbrace{f_u}_{\text{저농도 근사}}
\approx
\frac{1}{1+\overbrace{K_a}^{\text{친화도}}\cdot\underbrace{n[P_T]}_{\text{결합용량}}}
$$

[G&W 5e, Eq.47:3, p.692]

G&W는 Compound 1에서 $[P_T]=50/0.3$, Compound 2에서 $[P_T]=10/0.1$의 두 조건을 동시 적합함. $n\approx1\text{–}4$, $K_a$ 초기 추정 약 6 농도 단위. [G&W 5e, Table 47.1 p.692; Eq.47:4 p.693]

> 💡 **왜 두 단백 농도 조건이 필요한가.** 한 조건만 보면 "빈자리 수($n[P_T]$)"와 "붙잡는 힘($K_a$)"이 서로의 잔향으로 보여서 **따로 추정할 수 없음(identifiability fail).** 그래서 G&W가 굳이 두 단백 농도를 동시에 적합시키는 거임.

#### 경계 조건과 실무

| 이 카드 | → | 후속 | 이유 |
|---|---|---|---|
| 단일 결합 부위 | → | 다중 결합 부위 | 잔차에 체계적 패턴이 남으면 단일 부위 가정 깨짐 |
| $f_u$ 일정 가정 | → | $AUC_u = AUC\times f_u$ | 시간·농도 의존성 있으면 무효 |
| $f_{ub}>1$ 가능성 | → | bound/free ratio 해석 | 결합 분율과 혼동 금지 [G&W 5e, p.168] |

> 💼 **단백 covariate 선택.** 산성 약물은 **albumin**, 염기성 약물은 **α1-AGP** 변화에 먼저 주목.

> 💼 **PPB 측정법 편향.** 평형투석 vs 한외여과는 method bias가 다름. 실험 데이터를 받으면 측정법 메타데이터를 항상 확인. 보고서에서 PPB 측정법을 명시 안 하면 리뷰어가 바로 깁니다.

> ⚠️ 총 $AUC$에 단일 $f_u$를 곱하기 전에 — **그 $f_u$가 의사결정에 쓰는 농도 범위에서 유지되는지** 부터 확인.

#### 이 카드 한 줄

🎯 **$f_u$는 약물·결합 단백·농도의 함수. 산성은 albumin, 염기성은 AAG. AAG는 acute phase로 ICU에서 움직임. "$f_u$ = 상수"는 검증 대상이지 자동 사실이 아님.**

---

### M5 · 조직 쪽 은신처 — 큰 $V_d$의 정체

**현장에서 왜 중요한가.** 알부민이 떨어진 환자에서 "혈장 결합 변화만으로 $V$가 바뀌었다"고 단정하면 안 됨. 대 $V_d$ 염기성 약물은 조직 쪽에 훨씬 강한 은신처가 있어서 혈장 결합 변화의 효과가 묻혀버림. M5는 그 조직 쪽 은신처가 정확히 무엇인지를 해부함.

**한 줄 요지.** $K_p \sim f_u/f_{uT}$. **조직 쪽 손($f_{uT}$↓)이 더 세게 붙잡으면 약물은 그쪽으로 쏠리고 $V_d$는 커짐.** 염기성 약물의 큰 $V_d$ 대부분이 산성 인지질과 lysosomal trapping에서 나옴.

#### 정의

$$
\underbrace{K_p}_{\text{조직/혈장비}}
\sim
\frac{\overbrace{f_u}^{\text{혈장 }f_u}}{\underbrace{f_{uT}}_{\text{조직 }f_u}}
$$

[R&T 5e, pp.104, 109–110, 비교: Eq.4-25 vs Eq.4-12]

#### 직관 비유 — 쏠림 계기판

$K_p$는 혈장과 조직 사이의 **쏠림 계기판**임. 혈장 쪽 손($f_u$)이 약해지거나 조직 쪽 손($f_{uT}$↓)이 강해지면 계기판은 조직 쪽으로 기울어짐.

#### 출처 기반 사례

- **Furosemide**(저 $V_d$ loop diuretic, 산성)와 **amiodarone**(대 $V_d$ class III, 염기성·고친화 조직 결합) — 혈장 $f_u$가 비슷한 범위일 수 있는데 $V$는 엄청나게 다름. 차이는 어디서 — **염기성 약물의 높은 조직 결합 = 낮은 $f_{uT}$**. → **큰 $V_d$를 혈장 결합만으로 설명하면 안 된다**는 사례. [R&T 5e, p.110]
- **Propranolol** 대조군 6명 + 만성 간질환 환자 15명, 40 mg IV bolus 후 $V$ vs $f_u$ — 혈장 결합 변화가 $V$ 변동을 설명할 수 있는 약물 사례. → 즉, **약물에 따라 $V$ 변동의 주범이 혈장 쪽일 수도 있음.** [R&T 5e, Fig.4-23, p.110]
- **Metoprolol** — 조직 $K_p$가 **조직 산성 인지질 농도와 강한 양의 상관**. → 염기성 약물의 조직 결합 메커니즘이 산성 인지질과 직접 연결. [R&T 5e, Fig.4-24, p.110]
- **Indinavir** 800 mg q8h HIV 환자 8명 — CSF 유리 농도가 plasma 유리 농도보다 **낮고, 지연되고, 변동 폭이 작음**. → BBB efflux가 조직 노출을 별도로 제한. [R&T 5e, Fig.4-10, p.91]

#### $K_p$ 예측 — PBPK로 가는 다리

PBPK 모델에서 dose 결정 전에 조직 노출을 추정하려면 in silico $K_p$ 예측이 필요. 두 가지 표준 방법.

| 방법 | 입력 | 적용 범위 |
|---|---|---|
| **Poulin–Theil** | $logP$, $f_u$, 조직별 수분/지질/인지질 fraction | 중성·약산성 비이온화 약물 |
| **Rodgers–Rowland** | 위 + 조직 산성 인지질 농도, pKa, 이온화 분율 | 염기성 약물의 lysosomal trapping + 산성 인지질 결합 |

> 📐 **기본 골격식 — $K_p$의 두 항 분해.** 두 방법 모두 $K_p$를 **"조직 안에서 약물을 붙잡는 칸의 합"** 으로 분해함.
>
> $$
> \underbrace{K_p}_{\text{조직/혈장비}}
> =
> \overbrace{\frac{f_u}{f_{uT}}\cdot[\text{neutral lipid + neutral phospholipid 분배}]}^{\text{Poulin–Theil 공통항 (지질 분배)}}
> +
> \underbrace{f_u\cdot K_{AP}\cdot[\text{acidic phospholipid}]_T}_{\text{Rodgers–Rowland 추가 (이온결합항)}}
> $$
>
> 첫 항은 Poulin–Theil의 지질 분배항. 두 번째 항이 Rodgers–Rowland가 추가한 **염기성 약물의 ionized form이 산성 인지질(phosphatidylserine, phosphatidic acid)과 만드는 이온결합항**임. 이 두 번째 항이 **lysosomal pH trapping**과 결합해 propranolol·amiodarone·chloroquine의 큰 $V_d$를 정량적으로 잡아냄.
>
> ※ 본 식은 두 방법의 분기 구조 이해용 **개념적 골격**임. 실제 Rodgers–Rowland 완전식(Rodgers T, Rowland M. *J Pharm Sci* 2006;95:1238–57)은 조직별 acidic phospholipid 농도·lipid composition·ionization fraction을 각각 변수로 받음. 정량적 $K_p$ 예측은 원논문 또는 PBPK 전용 자료(R&T 5e Ch.21 PBPK)를 참조.

> 💡 **두 방법의 분기점 = 약물의 pKa.** Poulin–Theil은 약물을 "지질 친화도"로 잡는 모델이라 중성·산성에서 잘 맞음. 그런데 염기성 약물은 lysosome 같은 산성 소기관에서 protonation되어 **이온 trapping**이 일어나거나 산성 인지질에 강하게 결합. Rodgers–Rowland는 이 산성 인지질 결합 항과 pKa-기반 이온화 분율을 추가해서 metoprolol·propranolol·amiodarone 같은 염기성 약물의 큰 $K_p$를 정량적으로 잡아냄.

> 💼 **PBPK 실무 인사이트.** PBPK 보고서에서 "Rodgers–Rowland 사용"을 봤다면 그 약물은 **염기성 또는 산성 인지질 결합이 임상적으로 의미 있는 약물**임을 시사. PopPK 추정 $V_{ss}$와 PBPK $K_p$-기반 예측값을 cross-check 하면 **모델 misspec을 발견하는 빠른 진단 도구**가 됨.

#### 혈장-혈액 변환 (매트릭스 trap 재방문)

적혈구 분배:

$$
\underbrace{\frac{C_b}{C}}_{\text{혈액/혈장비}}
=
1+\overbrace{H}^{\text{Hct}}\left(\underbrace{f_u\cdot K_{PBC}}_{\text{RBC 분배}}-1\right)
$$

[R&T 5e, App.D, pp.775–776]

> 💼 **Tacrolimus·Cyclosporine 매트릭스 절대 원칙.** RBC 결합이 매우 강해서 ($C_b/C\approx 15$) **whole blood로만 측정**. plasma 농도는 정량 한계 이하 + hematocrit 변동으로 노출 비교 불가능. PopPK 데이터셋에서 각 약물의 표준 매트릭스 확인이 covariate 분석보다 먼저 와야 함.

#### 경계 조건 — 수송체 vs 결합 분리

> ⚠️ Eq.4-29에서 **결합항($f_{uT}$)과 수송체항($P_{uptake}/P_{efflux}$)을 같은 종류의 원인으로 합치지 말 것.** 결합은 수동적 점유, 수송체는 능동적 분포 불균형. 메커니즘이 완전히 다름.

| 상황 | 파라미터 변화 | 임상 결과 | 조치 |
|---|---|---|---|
| 조직 결합 ↑ | $f_{uT}$↓, $K_p$↑ | 큰 $V_d$, 긴 조직 체류 | 조직 결합/인지질 친화도 검토 |
| efflux 우세 | $P_{uptake}/P_{efflux}$↓ | 표적 조직 $C_u$ 낮음 | transporter 기질성 검토 |
| RBC 분배 변화 | $C_b/C$ 변화 | 혈액 vs 혈장 PK 해석 차이 | assay matrix 명시 |

#### 이 카드 한 줄

🎯 **$K_p\sim f_u/f_{uT}$. 큰 $V_d$ 염기성 약물의 정체는 산성 인지질 + lysosomal trapping — Rodgers–Rowland $K_p$ 예측이 필요한 자리. 결합과 수송체는 다른 메커니즘으로 분리해야 함.**

---

### M5b · 항체의 역설 — 작은 $V$ + 긴 $t_{1/2}$의 정체

**현장에서 왜 중요한가.** 항체의 긴 반감기를 "조직에 많이 쌓여서 천천히 나온다"로 읽으면 메커니즘을 거꾸로 잡는 거임. 실제로 항체는 조직에 거의 안 들어감 — adalimumab $V$가 약 5–6 L로 plasma volume 수준임. [R&T 5e, p.111] 그러면 긴 $t_{1/2}$(약 14일)는 어디서 나오는가.

**한 줄 요지.** 항체의 긴 반감기는 **분포가 아니라 소실 회피 기전(FcRn salvage)** 에서 나옴. FcRn이 lysosomal degradation에서 IgG를 구조해서 다시 순환에 돌려놓음.

#### FcRn-매개 재순환 메커니즘

**FcRn**(neonatal Fc receptor)은 endothelial cell endosome에 위치, IgG Fc 영역과 **pH-의존적**으로 결합.

| 단계 | 환경 | FcRn–IgG 결합 | 결과 |
|---|---|---|---|
| 1. Endocytosis | 세포외 pH ~7.4 | 약함 | IgG가 endosome 유입 |
| 2. Endosome 산성화 | pH ~6.0 | **강함** | FcRn이 IgG를 붙잡음 |
| 3. Recycling | endosome → 세포막 | 결합 유지 | IgG가 다시 세포외액으로 |
| 4. Release | 세포외 pH ~7.4 | 풀림 | IgG 방출 → 다시 순환 |
| (대안 4') | FcRn 미결합 IgG | — | Lysosome 분해 |

> 💡 **항체의 긴 $t_{1/2}$ = lysosomal degradation으로부터의 구조.** FcRn salvage는 **분해 회피 펌프**임. 작은 $V$에도 불구하고 IgG typical lifespan인 약 21일에 가까운 반감기를 가짐.

#### 임상·약물개발 함의

- **Adalimumab**(TNF-α mAb) $V$ 약 5–6 L, $t_{1/2}$ 약 14일 [R&T 5e, p.111]
- **Infliximab**(TNF-α chimeric mAb) MW 149,100 g/mol [R&T 5e, Table 4-8, p.112]
- **Etanercept**(TNF-α receptor-Fc 융합단백) MW 150,000 g/mol [R&T 5e, Table 4-8, p.112]

> 💼 **항체 공학 응용.** Fc 영역에 mutation을 도입해서 **FcRn 결합 친화도를 인위적으로 증가**시키면 반감기가 더 길어짐. 차세대 long-acting 항체 (예: efgartigimod 같은 FcRn 길항제, 또는 YTE/LS mutation) 설계의 핵심. 반대로 FcRn 결합 약화시키면 빠른 제거.

> 💼 **TMDD와의 분리.** 항체 PK 비선형성에는 두 가지 별개 기전이 있음 — **(1) FcRn 포화**(고용량 salvage 시스템 포화, 반감기 감소), **(2) TMDD**(target-mediated drug disposition, 표적 결합 비선형 소실). 두 기전은 다른 dose 영역에서 다른 곡선 형태로 나타남. 분리해서 봐야 함.

> ⚠️ FcRn은 **알부민**에도 작용 — 알부민 긴 반감기(약 19일)도 같은 FcRn salvage. 알부민-conjugated drug의 반감기 연장 전략도 이 기전 활용.

#### 이 카드 한 줄

🎯 **항체의 $V \approx$ plasma volume인데 $t_{1/2}$가 긴 이유는 조직 축적이 아니라 FcRn salvage. 비선형성 진단의 첫 단계는 FcRn 포화 vs TMDD 분리.**

---

### M6 · 마지막 결정 — 어떤 농도의 어떤 시간 패턴을 노출 지표로

**현장에서 왜 중요한가.** 보고서가 "AUC가 X였습니다"로 끝나면 리뷰어가 항상 한 번 더 묻음 — "어느 농도의 AUC인가요? 시간 패턴은 어땠나요? 동일 AUC라도 peak이 다르면 결과가 다를 텐데요?" 노출 지표를 단일 스칼라로 압축할 때마다 정보가 손실됨. 어디까지 압축할지를 의식적으로 결정해야 함.

**한 줄 요지.** 노출 지표는 숫자가 아니라 **"어떤 종이 어떤 시간 패턴으로 반응을 미는가"라는 인과 주장**임. peak-driven이면 $C_{max}$, cumulative면 $AUC$, duration-driven이면 $t_d$. 효과 기전을 먼저 정하고 지표를 고름.

#### 총 농도와 유리 농도의 변환

$$
\underbrace{C}_{\text{총 }C}
=
\frac{\overbrace{C_u}^{\text{유리 }C}}{\underbrace{f_u}_{\text{유리분율}}}
$$

$f_u$가 일정하다는 조건에서:

$$
\underbrace{AUC_u}_{\text{유리 AUC}}
=
\overbrace{AUC}^{\text{총 AUC}}
\times
\underbrace{f_u}_{\text{유리분율}}
$$

[G&W 5e, Eq.2:373, p.167]

#### 직관 비유 — 하루 강수량 vs 순간 폭우 vs 침수 시간

$AUC$는 하루 전체 강수량, $C_{max}$는 순간 폭우, $t_d$는 침수 수위 이상으로 머문 시간임. **같은 총 강수량이어도 홍수 위험은 전혀 다를 수 있음.** 효과 기전이 peak-driven이냐 cumulative냐 duration-driven이냐에 따라 어느 지표를 가져갈지가 결정됨.

#### 출처 기반 — G&W 사례

M6의 진짜 질문은 "$AUC$를 쓸 것인가?"가 아님 — **어느 종의 $AUC$인가, 어떤 시간 패턴인가**임.

| 그림/표 | anchor 내용 |
|---|---|
| **G&W Fig.2.134, p.163** | 용량-반응, 총 농도-반응, 유리 농도-반응이 **서로 다른 결론**을 낼 수 있음. 총 농도 관계는 PPB 차이에 교란. **유리 농도 기준에서 역가 순위가 뒤집힐 수 있음.** |
| **G&W Fig.2.136, p.164** | 같은 $AUC$라도 peak·역치 초과 시간·독성 관련성이 다를 수 있음. "동일 $AUC$ = 동일 효과"는 곡선 모양을 통째로 잃는 단축식. |
| **G&W Fig.2.140, p.167** | $f_u$를 총 농도가 아니라 $C_u$에 대해 그릴 때 더 명확한 관계 가능. |
| **G&W Fig.2.141, p.168** | 개·쥐·마우스에서 총 농도-반응 곡선은 다르게 보이는데 **유리 $EC_{u50}$이 약 2 nM 부근에서 정렬**될 수 있음. → 종간 외삽은 유리 농도 기반이 더 적절. |
| **G&W Table 2.21, p.169** | 노출 지표를 $C_{max}$·$AUC$·$t_d$·치료 기간 등으로 나누고 각 지표의 적용 상황 구분. |

#### G&W 456개 약물 검토의 결론

단백결합 변화가 PK 파라미터에는 영향을 줄 수 있지만 **임상 결과에는 대개 큰 영향을 주지 않음.** 

**예외는 IV 투여 + 고추출 + 좁은 치료역** 조합임. 이 셋이 동시에 만나는 약물에서만 PPB 변화가 임상적으로 폭발함. [G&W 5e, p.168]

G&W 권고: **IND 단계 — 여러 농도·종에서 ex vivo PPB 측정. NDA 단계 — 선별된 임상시험에서 유리·총 농도 동시 측정.** 일상적 "있으면 좋은" 측정은 피함. 비용 대비 정보 이득이 낮음. [G&W 5e, p.169]

#### 경계 조건

| 상황 | 파라미터 | → | 결과 | 조치 |
|---|---|---|---|---|
| $f_u$가 용량·시간·농도 의존 | 단축식 무효 가능 | → | $AUC_u$ 오계산 | 시간/농도별 $f_u$ 확인 |
| 동일 $AUC$인데 peak 다름 | $C_{max}$ 차이 | → | peak-driven toxicity 차이 | $C_{max}$ 지표 검토 |
| 동일 $AUC$인데 역치 초과 시간 다름 | $t_d$ 차이 | → | duration-driven efficacy 차이 | threshold/time-above metric 검토 |
| 종간 총 농도-반응 불일치 | PPB 차이 | → | potency order 왜곡 | 유리 농도 기반 비교 |

#### 이 카드 한 줄

🎯 **노출 지표는 "어떤 종이 어떤 시간 패턴으로 반응을 미는가"의 인과 주장. 효과 기전 → 지표 선택의 순서가 거꾸로 되면 어떤 분석도 방어 불가.**

---

## §5 — 혼동쌍 4쌍 정리 (Confusion Pair Dissection)

여기서부터는 카드에서 다룬 개념 중 학생들이 가장 자주 섞는 네 쌍을 따로 빼서 봄. 이름이 비슷하거나 같은 식에 같이 등장하는 것들임.

### 혼동쌍 1 — $C$ vs $C_u$ ⚡ 치명적 타격

| 비교 축 | $C$ (총 농도) | $C_u$ (유리 농도) |
|---|---|---|
| 의미 | 결합 + 비결합 전체 | 비결합만 |
| 수식 자리 | $V=A/C$ 분모, 총 $AUC$ 기반 | Eq.4-1 농도차, $AUC_u$, $C_u=C\times f_u$ |
| 변하는 원인 | assay matrix, 총 단백결합, 혈장/혈액 분배 | $f_u$, 단백 농도, 결합 포화, 변위체 |
| 혼동 결과 | 종간/화합물간 역가 순위 왜곡 | $f_u$ 시간 의존성 무시로 계산 오류 |

진짜 질문은 **"$C$ vs $C_u$ 중 무엇이 참인가"** 가 아님. 둘 다 참임. 진짜 질문은 **"지금 의사결정의 인과적 종이 무엇인가"** 임.

- 막투과·수용체 상호작용·종간 외삽 → $C_u$가 더 직접 연결.
- $f_u$가 안정적이고 의사결정이 total assay로 검증된 약물 → $C$도 충분히 유용.

좌표계 잘못 잡으면 "농도는 정상인데 효과 없음" / "농도 낮은데 독성 나타남" 역설이 그대로 발생.

> ⚡ **기억 고리.** $C$ = 사진(관찰 대리), $C_u$ = 수용체에 실제로 작용하는 행위자. 같은 $C$에서 $f_u$가 다르면 $C_u$가 다르고, 같은 $C_u$에서 $f_u$가 다르면 $C$가 다름.

### 혼동쌍 2 — 관류 율속 vs 투과 율속

| 비교 축 | 관류 율속 | 투과 율속 |
|---|---|---|
| 율속 인자 | $Q/V_T$ | 막 투과도 |
| Eq.4-5~4-7 적용 | 그대로 안전 | 같은 식 못 씀 (막이 병목) |
| 변하는 원인 | 혈류, 조직 크기, 관류 상태 | BBB, 거대분자 혈관벽 통과, 림프 회수 |
| 혼동 결과 | $Q$ 증가 효과 과대/과소 | 뇌 penicillin G·거대분자 분포 지연을 혈류로 오해 |

> ⚡ **기억 고리 — 얼마나 퍼지나 vs 얼마나 빨리 퍼지나.** $V_d$ 크기는 **최종 분포 범위**. $Q/V_T$·막 투과도는 **최종 상태 도달 속도**. 두 차원은 독립.

### 혼동쌍 3 — $f_u$ vs $f_{uT}$

| 비교 축 | $f_u$ | $f_{uT}$ |
|---|---|---|
| 위치 | 혈장 유리 분율 | 조직 유리 분율 |
| 수식 자리 | $V=V_p+V_{TW}(f_u/f_{uT})$ 분자 | 같은 식의 분모 |
| 변하는 원인 | albumin, α1-AGP, PPB 포화 | 조직 단백, 산성 인지질, 조직 결합 |
| 혼동 결과 | 혈장 결합 변화만으로 큰 $V_d$ 설명 시도 | 조직 결합 증가에 따른 $V$ 증가 누락 |

$$
\underbrace{V}_{\text{겉보기 }V}
=
\overbrace{V_p}^{\text{혈장항}}
+
\underbrace{V_{TW}\left(\frac{\overbrace{f_u}^{\text{혈장 }f_u}}{\underbrace{f_{uT}}_{\text{조직 }f_u}}\right)}_{\text{조직 결합항}}
$$

> ⚡ **기억 고리 — $V_{ss}$ vs $V_\beta$.** $V_{ss}$는 분포-제거 완전 독립의 정적 균형 부피. **부하 용량은 $V_{ss}$**. $V_\beta$는 종말상 기울기에서 역산한 겉보기 부피. **종말상 반감기 해석은 $V_\beta$**. NONMEM 출력에서 어느 $V$를 쓰는지 끝까지 확인.

### 혼동쌍 4 — 소 $V_d$ vs 대 $V_d$의 단백결합 반응 (Advanced)

| 비교 축 | 소 $V_d$ 알부민 결합 ($V<0.2$ L/kg) | 대 $V_d$ 조직 결합 ($V>0.6$ L/kg) |
|---|---|---|
| 기준 | 알부민 하한 약 7.5 L | 조직 결합/수송체가 만든 큰 겉보기 용적 |
| 수식 | $V=7.5+(7.5+V_R/f_{uR})f_u$ (Eq.4-30) | $V=V_p+V_{TW}(f_u/f_{uT})$ (Eq.4-25 또는 4-29) |
| 대표 약물 | warfarin, naproxen, valproate, cephalosporins | propranolol, amiodarone, chloroquine, digoxin |
| $f_u$↑ 시 $V$ | 비교적 크게 ↑ (저알부민혈증에서 1.5–2배) | 거의 변화 없음 (조직 결합 지배) |
| $f_u$↑ 시 $C_u$ | 초기 $C_u$ 동일, 이후 $CL$↑로 변화 적음 | 초기 $C_u$↑, $V$ 안 바뀌어 변화 지속 |
| 혼동 결과 | 저알부민혈증에서 총/유리 방향 오독 | 혈장 결합 변화만으로 $V$·$C_u$ 해석 |

> 🔑 **부하 용량 조정의 비대칭 — Apex Concept.** R&T App.C와 pp.111–115의 가장 중요한 통찰. **대 $V_d$ 약물에서 단백결합이 변해도 부하 용량은 거의 조정 필요 없음.** 약물의 대부분이 이미 조직에 있어서 혈장 결합 변화가 전체 분포에 미치는 영향이 미미함. 반면 **소 $V_d$ 알부민 결합 약물에서는 혈장 결합이 분포 전체에 직접 영향** → 부하 용량 조정이 임상적으로 의미를 가질 수 있음. [R&T 5e, pp.114–115, Eq.4-26 vs Eq.4-30]

$$
\underbrace{AUC_u}_{\text{활성 }AUC_u}
=
\overbrace{f_u}^{\text{유리분율}}
\times
\underbrace{AUC}_{\text{총 AUC}}
$$

> ⚡ **기억 고리 — $AUC$ vs $AUC_u$.** $AUC$ = 총 화물량 (결합 + 유리). $AUC_u$ = 수용체 도달 가능한 활성 화물량. **알부민 결합 강한 약물에서 저알부민혈증이 생기면 $AUC$는 줄어도 $AUC_u$는 오히려 늘 수 있음.** 노출-반응을 $AUC$로만 분석하면 효과 방향이 역전됨 — 다음 §6에서 워파린 케이스로 정확히 이 자리를 풀음.

---

## §6 — 강의실 도입 다시 — 워파린 케이스 풀기 (Closure)

이제 챕터 비밀번호와 카드 6+1장의 도구를 가지고 강의실 도입의 워파린 환자한테 돌아옴.

### 케이스 재조명

신증후군 환자. 알부민 43 → 12.5 g/L. 측정된 racemic warfarin PK:

| | 정상 알부민 | 저알부민혈증 | 방향 |
|---|---:|---:|:---:|
| $V$ | 9.4 L | 13.7 L | ↑ 약 1.5배 |
| $CL$ | 0.20 L/hr | 0.58 L/hr | ↑ 약 2.9배 |
| $t_{1/2}$ | 36 hr | 18 hr | ↓ 절반 |

박사과정생 질문: "총 농도 떨어졌으니 출혈 위험 줄어든 거 맞죠?"

### §1~§5의 도구로 분해

**Step 1. 농도 좌표계 확인 (§1)** — 위 수치는 **plasma · total · racemic** 기준. 활성 종 ($C_u$ 또는 enantiomer 분리) 농도는 별도로 봐야 함.

**Step 2. 워파린이 어떤 약물 클래스인지 확인 (§5 혼동쌍 4)** — 워파린은 **소 $V_d$ 알부민 결합 약물** ($V$ 약 0.13 L/kg, $f_u$ 약 0.01, 알부민 99% 결합). 그래서 Eq.4-30이 적용:

$$
\underbrace{V}_{\text{소 }V_d}
=
\overbrace{7.5}^{\text{알부민 하한}}
+
\underbrace{\left(7.5+\frac{V_R}{f_{uR}}\right)}_{\text{잔여}}\cdot\overbrace{f_u}^{\text{혈장 }f_u}
$$

**Step 3. 알부민 ↓ → $f_u$ ↑ 의 직접 효과 (M4)** — 알부민이 43에서 12.5로 약 3.4배 감소. mass-law (R&T Eq.4-19)에서 $f_u$는 단백 농도와 역상관 → **$f_u$는 약 3.4배 증가** (대략 0.01 → 0.034 수준, 결합 부위가 아직 포화 아니라는 가정).

**Step 4. $V$의 방향 — Eq.4-30이 예측 (M3)** — Eq.4-30에 따라 $f_u$↑에 따라 $V$가 비례 증가 (단, 알부민 7.5 L 하한 위에서). 실측 9.4 → 13.7 L (약 1.5배 증가) — Eq.4-30 예측과 일치.

**Step 5. $CL$의 방향 — well-stirred 식 사전 예고 (§1 box)** — 워파린은 저추출 약물. 저추출에서 $CL_H \approx f_{ub} \cdot CL_{int}$. **$f_u$↑** → $CL$ 비례 증가. 실측 0.20 → 0.58 L/hr (약 2.9배 증가). $f_u$ 증가폭 (약 3.4배)에 가까운 방향이지만 분획 변동 + IIV 여지 있음. **$CL$이 $V$보다 가파르게 늘어남 (2.9배 vs 1.5배).**

**Step 6. $t_{1/2}$의 방향 — $V$와 $CL$의 비** —

$$
\underbrace{t_{1/2}}_{\text{종말 반감기}}
=
\frac{\overbrace{0.693\cdot V}^{\text{분포}}}{\underbrace{CL}_{\text{청소}}}
$$

$V$ 1.5배 / $CL$ 2.9배 → $t_{1/2}$ 약 0.52배 (36 → 18.7 hr). 실측 36 → 18 hr과 일치.

**Step 7. 활성 노출 (=$AUC_u$)의 방향 — 혼동쌍 4의 핵심 (M6)** —

$$
\underbrace{AUC_u}_{\text{유리 }AUC}
=
\frac{\overbrace{Dose}^{\text{투여량}}\cdot\underbrace{f_u}_{\text{유리분율}}}{\overbrace{CL}^{\text{총 청소율}}}
$$

저추출 약물에서 $CL \approx f_u \cdot CL_{int}$이므로 — **$f_u$와 $CL$이 동일 비율로 움직임. 그 결과 $AUC_u$는 $CL_{int}$만으로 결정** → 알부민 변화의 영향이 거의 사라짐.

> ⚡ **이 한 줄이 워파린 케이스의 진짜 답:** **저추출 약물의 $AUC_u$는 $CL_{int}$만의 함수임. 알부민 변화로 총 $AUC$가 줄어도 $AUC_u$는 거의 그대로 → 활성 노출은 변하지 않음. 출혈 위험도 거의 변하지 않음.**

### 그래서 박사과정생 질문에 어떻게 답하는가

"총 농도가 떨어졌으니 출혈 위험 줄어든 거 맞죠?" → **틀림.**

올바른 답:
- 알부민이 떨어져서 총 $V$·총 $CL$이 모두 증가했고 총 $t_{1/2}$이 짧아진 것은 사실.
- 그러나 **활성 종인 $C_u$ 또는 $AUC_u$는 거의 변하지 않았음.** 저추출 알부민 결합 약물의 정의상.
- 그러니까 INR 등 약효 모니터링 지표는 알부민 변화 전후에 큰 차이를 보이지 않을 가능성이 높음.
- 단, **R/S-enantiomer 비율은 따로 봐야 함** (S가 약 5배 강력, CYP2C9 의존). 만약 환자가 CYP2C9 억제제 (fluconazole 등)를 같이 쓰면 S-warfarin이 선택적으로 축적 → 출혈 위험 ↑. 이건 알부민 변화와 별도 채널.

> 🎯 **케이스의 교훈 한 줄.** **총 농도 하나로 활성 노출을 추론할 수 없음. 약물 클래스(저추출 vs 고추출 / 소 $V_d$ vs 대 $V_d$ / 산성 vs 염기성)를 먼저 분류한 다음 $AUC_u$의 결정인자를 따져야 함. 이게 이 챕터를 통과한 후 진짜로 손에 쥐는 도구임.**

---

## §7 — 자기 테스트 (능동 회상 모듈)

### Q1
Eq.4-1에서 농도차가 $C_1-C_2$가 아니라 $C_{u,1}-C_{u,2}$인 이유는?

**정답:** 결합 약물은 일반적으로 막을 통과하지 못하고, 유리 약물만 확산 구동력이 되기 때문임. [R&T 5e, p.80]

### Q2
MW 400→800 g/mol 증가와 $logP$ 증가가 투과도에 미치는 방향은?

**정답:** MW↑는 투과도를 크게 ↓. $logP$↑는 대체로 투과도를 ↑. 단 수송체 기질이면 $logP$ 예측이 깨질 수 있음. [R&T 5e, Fig.4-3~4-4, pp.81–82]

### Q3
관류 율속 조직에서 $K_{pb}$가 커지면 분포 반감기는?

**정답:** $t_{1/2,distribution}=0.693\cdot K_{pb}/(Q/V_T)$니까 ↑. 친화도가 크면 채워야 할 조직 약물량이 많아져 평형 도달 지연. [R&T 5e, p.97]

$$
\underbrace{t_{1/2,distribution}}_{\text{분포 반감기}}
=
\frac{\overbrace{0.693}^{\ln 2}\cdot\underbrace{K_{pb}}_{\text{조직저장}}}{\overbrace{Q/V_T}^{\text{조직관류}}}
$$

### Q4
소 $V_d$ 알부민 결합 약물에서 $f_u\to 0$일 때 $V$가 0 L가 아니라 약 7.5 L 하한을 갖는 이유는?

**정답:** 약물이 알부민에 붙어 혈관 외 알부민 공간까지 분포하기 때문. 알부민 분포 용적이 약 7.5 L 하한을 만듦. [R&T 5e, pp.111–113; App.C pp.767–773]

### Q5
Warfarin 신증후군에서 알부민 감소가 $V$, $CL$, $t_{1/2}$에 어떤 방향 변화를?

**정답:** albumin 43→12.5 g/L에서 $V$ 9.4→13.7 L, $CL$ 0.20→0.58 L/hr, $t_{1/2}$ 36→18 hr. **단, 이 수치는 racemic warfarin (R+S 합산) 기준. S-warfarin (약 5배 강력, CYP2C9 대사)과 R-warfarin (CYP1A2/3A4 대사)의 enantiomer-specific PK는 따로 분리해야 정확한 약효 해석 가능.** [R&T 5e, Ch.4, Table 4-12, p.118]

### Q6
G&W Eq.2:373의 $AUC_u=AUC\times f_u$를 쓰기 위한 핵심 조건은?

**정답:** $f_u$가 시간·농도·dose에 대해 충분히 일정해야 함. 그렇지 않으면 단일 $f_u$를 총 $AUC$에 곱하는 단축식이 깨짐. [G&W 5e, p.167]

### Q7
동일 $AUC$인데 독성이 다를 수 있는 이유는?

**정답:** 같은 면적이라도 최고 농도·역치 초과 시간 $t_d$·농도-시간 형태가 다를 수 있기 때문. [G&W 5e, Fig.2.136, p.164]

### Q8
PK47에서 저/고 단백 농도를 동시에 적합하는 이유는?

**정답:** $n$과 $K_a$의 상관을 줄이고 정밀도를 높이기 위해. 한 조건만 보면 두 파라미터를 따로 추정할 수 없음(identifiability). [G&W 5e, p.693]

### Q9 — 보스 딜레마
신약 후보에서 총 $AUC$는 종간 차이가 큰데 유리 $EC_{u50}$이 종간 정렬됨. 어느 노출 지표를 안전 마진 논의 중심에 놓을 것인가?

**정답:** 유리 노출을 중심 지표로 두되, 총 노출과 $f_u$ 측정 방법을 함께 제시. 총 농도-반응이 PPB 차이에 교란될 수 있고, 유리 농도가 종간 외삽에서 더 적절. [G&W 5e, pp.163, 167–169]

### Q10 — 교육용 가상 사례
Phase 1 SAD에서 용량 정규화 $AUC$가 용량 증가와 함께 감소. 포화성 청소율과 포화성 PPB를 어떻게 구분?

**정답:** 용량별 ex vivo $f_u$ 확인. $f_u$가 용량·$C_u$에 따라 증가하면 포화성 PPB 의심, $f_u$가 일정하면 청소율 비선형성 우선 의심.

### Q11 — α1-AGP와 ICU 환자
급성 외상 환자에서 propranolol의 total 농도는 정상 범위인데 임상 효과(심박수 감소)가 약함. 가장 가능성 높은 원인은?

**정답:** AAG는 acute phase reactant로 외상 시 ↑. propranolol은 AAG에 결합하는 염기성 약물이므로 $f_u$ ↓, $C_u$ ↓ → 활성 노출 ↓. Total 정상이어도 활성 종 기준으론 노출 부족. [R&T 5e, Fig.4-22 p.108; Table 4-9 p.114]

### Q12 — 항체 PK 역설
Adalimumab의 $V$가 약 5–6 L로 plasma volume 수준인데 반감기는 약 14일로 매우 김. 모순 해소?

**정답:** 항체는 조직에 거의 분포 안 함 → 작은 $V$. 그러나 **FcRn에 의한 endosomal salvage**로 lysosomal degradation에서 회수됨 → 작은 $V$에도 IgG typical lifespan에 가까운 긴 $t_{1/2}$. [R&T 5e, p.111]

### Q13 — Tacrolimus 매트릭스
Tacrolimus를 plasma가 아닌 whole blood로 측정해야 하는 이유는?

**정답:** RBC 결합이 매우 강해 ($C_b/C\approx 15$) 적혈구 칸에 약물 대부분 분포. plasma 농도는 정량 한계 ↓, hematocrit 변동으로 plasma/blood 비가 달라져서 plasma로는 노출 비교 불가. **매트릭스를 일관되게 whole blood로 통일해야 PK 파라미터 해석이 의미를 가짐.** [R&T 5e, App.D, pp.775–776]

---

## §8 — 메타프레임 & 전체 조망

### A. 이 챕터의 위치

이 세션은 **분포를 생리학으로 읽는 법**을 세움. 청소율·반복투여·TDM·PBPK·PopPK 공변량 모델링은 모두 여기서 정의된 $C_u$·$f_u$·$f_{uT}$·$K_p$·$V$ 위에 쌓임. 통과 못 하면 후속이 다 흔들림.

### B. 어디서 어긋나면 어디가 무너지는가

| 실패 지점 | 발생 원인 | 직접 결과 |
|---|---|---|
| 부하 용량 오류 | $V$를 생리학적 부피로 해석 | loading dose 왜곡 |
| 공변량 오류 | albumin이 총 $CL$·$V$·유리 노출에 미치는 방향 미구분 | PopPK covariate 방향 오류 |
| 노출 지표 오류 | 동일 $AUC$ = 동일 효과 가정 | 최고 농도·지속 시간 정보 손실 |
| 종간 외삽 오류 | 총 농도-반응의 역가 순위를 활성 종 순위로 착각 | safety margin 왜곡 |
| 단백결합 오류 | $f_u$를 상수로 가정 | 포화성 결합·단백 농도 변화 누락 |
| 매트릭스 오류 | plasma vs whole blood 미구분 | $V$·$CL$ 수치 좌표계 불일치 |
| 거대분자 오류 | 작은 $V$ + 긴 $t_{1/2}$를 조직 축적으로 설명 | FcRn salvage 기전 누락 |

### C. 박사과정생이 가져가야 할 한 문장 (Professional Moat)

**분포는 "약물이 어디에 있는가"가 아님. 혈장과 조직 사이에서 결합·투과도·혈류가 함께 만드는 평형 문제이자 시간 경과 문제임. 총 농도는 관찰값이고, 유리 농도는 많은 경우 인과적 종에 더 가까움. $V$는 그 둘을 총량과 연결해 주는 겉보기 상수일 뿐임. 이 세 관계를 한 좌표계에 동시에 올릴 수 있으면 분포 관련 임상·규제 질문의 90%는 자체적으로 분해됨.**

### D. PopPK GOF 플롯에 나타나는 세 패턴

> 📍 이번 챕터 개념의 오용은 PopPK GOF 플롯에 반복 가능한 패턴을 남김. 이름을 붙여두면 진단이 카드 단위가 아니라 패턴 단위에서 가속됨.

**패턴 1 — 알부민 covariate 비대칭.** 대 $V_d$에서 $V$~albumin만 spec하고 $CL$~albumin 누락 시. ETA-V vs albumin은 약한 양의 상관, ETA-CL vs albumin은 강한 음의 상관. 시뮬레이션에서 알부민 극단군 예측 구간이 체계적으로 어긋남. **진단: ETA-CL vs albumin이 더 강하면 $CL$ covariate도 spec.**

**패턴 2 — PK47 단일 부위 부적합.** 다중 결합 부위 약물에 단일 부위 PK47 적합 시. 저 $C_u$에서 $f_u$ 과소추정, 고 $C_u$에서 과대추정. 잔차에 V자 또는 역V자 패턴. 저/고 단백 농도 동시 적합에서는 두 데이터셋 잔차 방향이 반대로 갈라짐. **진단: $f_u$ vs $C_u$ 잔차가 V자면 두 번째 결합 부위 추가.**

**패턴 3 — $V_{ss}$ vs $V_\beta$ 혼동.** 2구획 이상 모델에서 NONMEM 출력 $V$를 $V_\beta$로 무비판 사용해 부하 용량 계산 시. 분포상 IPRED는 정확한데 소실상 꼬리에서 체계적 과소예측, CWRES가 시간에 따라 단조 편향. **진단: 소실상 꼬리 CWRES 편향 → $V_{ss}$/$V_\beta$ 분리. 부하 용량은 $V_{ss}$, 종말상 반감기는 $V_\beta$.**

### E. 한 환자 케이스 만났을 때 머리에 돌리는 4단계 시퀀스

| 단계 | 질문 | 카드 | 실패 시 |
|---|---|---|---|
| 1. Species 결정 | 보고 있는 농도는 $C$·$C_u$·$C_b$ 중 무엇? 매트릭스는? | M1·M4·M5·M6 | 농도 종/매트릭스 혼동 |
| 2. $V_d$ 양상 결정 | 소 $V_d$ 알부민 결합 / 대 $V_d$ 조직 결합 / 항체 중 무엇? | M3·M5·M5b | $f_u$ 변화 방향 오독, FcRn 기전 누락 |
| 3. $f_u$ 안정성 점검 | 용량·시간·농도 범위에서 $f_u$ 일정? 단백질(albumin vs AAG)이 질환에서 변하는가? | M4 | $AUC_u$ 단축식 실패, AAG 환자 오판 |
| 4. 지표 정당화 | $C_{max}$·$AUC$·$t_d$ 중 어느 시간 패턴? 어느 종으로 비교? | M6 | 안전 마진/효능 지표 왜곡 |

이 4단계는 §5 혼동쌍 1의 실무 렌즈(인과적 종 → 분석 스케일 → 변환 유효성 → 의사결정 위험도)와 구조적으로 같음. 카드들에서 다룬 "왜"와 "어떻게"를 한 진단 시퀀스로 합친 것임.

### F. 후속 세션 연결 지식 그래프

| 후속 세션 | 이 세션에서 열리는 개념 | 없으면 실패하는 것 |
|---|---|---|
| 청소율 | $f_u$가 well-stirred 식 분자로 들어가는 이유, $f_u$ vs $f_{ub}$ | total $CL$과 unbound $CL$ 혼동 |
| 반복 투여/축적 | $V$·$CL$·$t_{1/2}$의 연결 | 단백결합 변화 시 반감기 방향 오독 |
| TDM | 총 농도 정상 vs 유리 농도 독성 가능성, ICU AAG 변화 | 저알부민혈증·외상 환자 용량 판단 오류, 매트릭스 단위 혼동 |
| PBPK | $K_p$, $f_u/f_{uT}$, 수송체항, Poulin–Theil / Rodgers–Rowland | 조직분포 원인 혼동, 염기성 약물 $K_p$ 과소예측 |
| PopPK 공변량 | albumin/α1-AGP의 $V$·$CL$·$f_u$ 작동 위치, 매트릭스 일관성 | covariate spec 방향 오류, plasma/whole blood 단위 트랩 |
| 항체 PK·TMDD | FcRn salvage, $V \approx V_{plasma}$ 거동 | 작은 $V$+긴 $t_{1/2}$ 모순 미해결, TMDD vs FcRn 포화 혼동 |

---

## 부록 — 출처 표기 통일 약어

| 약어 | 전체 출처 |
|---|---|
| **R&T 5e** | **Rowland M, Tozer TN.** *Clinical Pharmacokinetics and Pharmacodynamics: Concepts and Applications.* 5th ed. Philadelphia: Wolters Kluwer / Lippincott Williams & Wilkins; 2020. ISBN 978-1-4963-8503-7. (본 세션은 주로 **Chapter 4 "Membranes and Distribution" pp.79–118**, **Appendix C "Distribution of Drugs Extensively Bound to Plasma Proteins" pp.767–773**, **Appendix D "Plasma-to-Blood Concentration Ratio" pp.775–776**를 인용함.) |
| **G&W 5e** | **Gabrielsson J, Weiner D.** *Pharmacokinetic and Pharmacodynamic Data Analysis: Concepts and Applications.* 5th ed. Stockholm: Apotekarsocieteten / Swedish Pharmaceutical Press; 2016. ISBN 978-91-9836-621-6. (본 세션은 주로 **Chapter 2 "Pharmacokinetic Concepts" §2.5–2.9 pp.20–169**, **Application 47 "Plasma Protein Binding" pp.691–693**을 인용함.) |

### 본문 인용 형식 규약

- **R&T 5e**: `[R&T 5e, Ch.X, Eq.X-Y, p.NN]` / `[R&T 5e, Ch.X, Fig.X-Y, p.NN]`
- **G&W 5e**: `[G&W 5e, Eq.X:Y, p.NN]` / `[G&W 5e, Fig.X.YY, p.NN]` — 콜론·점 표기 원문 보존
- **Appendix**: R&T는 `App.A/B/C/D`, G&W는 `Application N`

### 인용된 원논문 (저자 추적 가능 사례)

| 본문 위치 | 원논문 anchor |
|---|---|
| Warfarin 신증후군 Table 4-12 | Ganeval D, Fischer AM, Barre J, et al. *Clin Nephrol* 1986;25:75–80. |
| Propranolol $f_u$ vs AAG, Fig.4-22 | Tozer TN 등의 protein binding 검토. (R&T 원문 caption) |
| Cephalosporin Fig.4-25 | Dudley MN, Nightingale CH. 1982 (R&T caption에 명시). |
| Rodgers–Rowland $K_p$ 예측법 (M5) | Rodgers T, Rowland M. *J Pharm Sci* 2006;95(6):1238–57; Rodgers T, Leahy D, Rowland M. *J Pharm Sci* 2005;94(6):1259–76. |
| Poulin–Theil $K_p$ 예측법 (M5) | Poulin P, Theil FP. *J Pharm Sci* 2000;89(1):16–35; 2002;91(1):129–56. |

---

## 변경 로그 (보강본_final → 리마스터판)

| 변경 종류 | 위치 | 내용 |
|---|---|---|
| **구조 — 신설** | 강의실 도입 직후 | **챕터 비밀번호** 섹션 신설. "V는 부피가 아님" 한 줄을 카드 진입 전에 명시하여 M1~M6이 한 비밀번호의 변주처럼 읽히게 만듦 |
| **구조 — 신설** | §5 혼동쌍 직후 (§6) | **워파린 케이스 풀기 (Closure)** 섹션 신설. 강의실 도입의 환자를 챕터 끝에서 7-step 분해로 풀어서 closure 만듦 |
| **구조 — 압축** | 원본 §1 | 원본 §1(세션 헤더 + 로드맵)을 챕터 비밀번호 + §1 좌표계 셋업의 두 섹션으로 재편. 농도 species(C/Cu/Cb) 정렬과 매트릭스 트랩, $f_u$ vs $f_{ub}$ 예고를 한 자리에 모음 |
| **문체** | 전 문서 | 어미를 **음슴체(~함, ~임, ~음)** 로 통일. "~합니다"체 제거 |
| **메타포 통일** | 전 문서 | "약은 어디에 숨었는가"라는 단일 비유로 통일. 창고/매장 진열대 (V) — 공항 입국심사대 (막투과) — 주차장 (단백결합) — 수도꼭지와 탱크 (관류 vs Kpb) — 쏠림 계기판 (Kp) — 강수량/폭우/침수시간 ($AUC$/$C_{max}$/$t_d$)을 가족 비유로 묶음 |
| **카드 진입부 강화** | M1~M6, M5b | 각 카드 시작부에 **"현장에서 왜 중요한가"** + **"한 줄 요지"** 두 줄 prepend. 학습자가 카드 통과 전에 "무엇이 걸려 있는가"를 알게 함 |
| **카드 마무리 강화** | M1~M6, M5b | 각 카드 끝에 **"🎯 이 카드 한 줄"** 박스 추가. 회상 anchor 제공 |
| **콘텐츠 보존** | 전 문서 | 모든 수식 anchor (overbrace/underbrace 포함), 모든 출처 인용 (R&T 페이지·식·표·그림 번호, G&W Application 47 등), 원논문 anchor (Ganeval 1986, Dudley & Nightingale 1982, Rodgers & Rowland 2005/2006, Poulin & Theil 2000/2002), warfarin enantiomer 주의, $f_u$ vs $f_{ub}$ 예고, Rodgers–Rowland 골격식, FcRn salvage, $V_{ss}$ vs $V_\beta$, 매트릭스 트랩, PopPK GOF 3패턴, 4-step 진단 시퀀스를 **모두 보존**함 |
| **자기 테스트** | §7 | 13문항 모두 보존. 답안 텍스트는 음슴체로 변환. Warfarin Q5의 enantiomer 주의 유지. Tacrolimus 매트릭스 Q13 유지 |

본 리마스터는 보강본_final의 **다루는 범위·인용 출처·결론·핵심 수식 anchor를 완전히 보존**함. 강의 동선·메타포·진입/마무리 closure만 재편하여 학습자가 같은 콘텐츠를 더 직관적·실무적으로 이해하도록 만든 것이 목적임. 보강본_final이 PIPET 강의 표준 anchor로 유지되어야 한다면, 본 리마스터판은 **학습자용 강의체 보조 자료** 또는 **슬라이드 deck 진입부 사전 학습자료**로 위치시키는 것이 적합함.

---

*— 세션 02 리마스터판 끝 —*

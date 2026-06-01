## 판정

**Phase 1 Draft v0로는 “상위권 초안”입니다. 그러나 “최적으로 완성된 Phase 1”이라고 보기는 어렵습니다.**
그대로 Phase 5 HTML 변환으로 넘기면 안 되고, **Phase 2 Source Fidelity Audit → Phase 3 Insight Crucible → Phase 4 Content Lock/Compression**을 반드시 거쳐야 합니다. 현재 상태는 **넓게 잘 긁어온 고밀도 원석**이지, 아직 **검증·압축·잠금이 끝난 학습 콘텐츠**는 아닙니다.

제 평가 점수는 다음 정도입니다.

| 항목               |                                 판정 |
| ---------------- | ---------------------------------: |
| Phase 1 목적 달성도   |                         **8.0/10** |
| 소스 커버리지          |                         **8.0/10** |
| 수식·수치 안정성        |                         **7.0/10** |
| HTML 전환 준비도      |                         **6.0/10** |
| 그대로 다음 단계 진행 가능성 | **Phase 2로는 진행 가능 / HTML로는 진행 금지** |

---

## 잘 된 점

핵심 축은 잘 잡았습니다. 특히 이 세션의 중심인 **“항정상태 도달 시간은 t½, 항정상태 농도 수준은 CL이 결정한다”**는 Big Idea가 문서 전반에 유지되어 있습니다. Gabrielsson 원문도 정속 주입에서 1 half-life 후 50%, 3–4 half-lives 후 약 90% steady state에 접근한다고 설명하고, Css는 Rin/Cl로 계산된다고 제시합니다.

**M3를 Apex Concept로 둔 판단도 타당합니다.** Gabrielsson은 축적인자 R이 half-life와 dosing interval에 의존하고 dose와는 독립적이라고 명시하며, R&T Ch.11도 평균 투여율이 같으면 평균 amount의 plateau 접근 시간 경로는 같고 fluctuation만 dosing interval에 따라 달라진다는 메시지를 제공합니다. 이 점은 “τ/t½가 축적과 fluctuation을 지배한다”는 교육 목표와 잘 맞습니다.

R&T Ch.9–11을 단순 보충이 아니라 **치료역 → 정속 주입 → 다중투여 설계**의 삼각형으로 묶은 것도 좋습니다. Scope Lock 자체도 Ch.11의 Rac, Cav,ss, 부하/유지용량 관계식을 후속 PopPK 워크플로우의 구조적 전제로 지정하고 있습니다.

---

## 반드시 고쳐야 할 문제

### 1. M4에서 “amount”와 “concentration”이 섞인 치명적 수식 표현이 있습니다.

현재 Curation Map 쪽에서 다음처럼 보이는 표현은 위험합니다.

> `Css,avg = F·Dose/(τ·Cl) = AUC/τ = 1.443·F·Dose·t1/2/τ`

문제는 **`1.443·F·Dose·t1/2/τ`는 average amount at plateau 쪽 식이지 concentration 식이 아니라는 점**입니다. R&T Table 11-6은 `Aav,ss = 1.44·F·Dose·t1/2/τ`와 `Cav,ss = F·DM/(CL·τ)`를 분리해서 제시합니다. 

수정은 이렇게 해야 합니다.

```text
Cav,ss = AUC0-τ,ss / τ = F·Dose / (CL·τ)

Aav,ss = 1.443·F·Dose·t1/2 / τ

1-compartment에서만:
Cav,ss = Aav,ss / V
        = 1.443·F·Dose·t1/2 / (V·τ)
```

다행히 본문 M4 상세 도출부에서는 `C_ss,avg = F·Dpo/(τ·Cl)`와 R&T Eq. 11-7의 `A_av,ss`를 비교적 분리해서 설명하고 있습니다. 즉, **전체 문서가 틀린 것은 아니고, 상단 Curation Map/요약부의 압축 표현이 위험합니다.** 

---

### 2. 교과서에 없는 수치·규제 단정이 섞여 있습니다.

예를 들어 Trench Tip에 **“펌프·카테터 문제일 가능성이 30–40%”**라고 되어 있는데, 이 수치는 첨부 교과서 근거로 확인되지 않습니다. 

또 Apex 카드에는 SS=1 오용의 나비효과로 **“AUC 30–80% 과다 → 독성 → Phase 3 SAE 증가 → NDA 거부”**까지 이어지는 단정이 들어가 있습니다. 방향성 자체는 교육적으로 설득력 있지만, 구체 수치와 NDA 거부까지의 인과는 교과서 출처가 아닌 해석입니다. 

Scope Lock과 Phase 4 규칙은 모두 **출처에 없는 수치·실험 조건·page citation을 만들지 말 것**, `NOT_IN_SOURCE`는 삭제하거나 `[교과서 외 해석]`으로 라벨링하라고 되어 있습니다.

따라서 다음 표현들은 Phase 2에서 반드시 걸러야 합니다.

```text
- 30–40% 가능성
- AUC 30–80% 과다
- Phase 3 SAE 증가 → NDA 거부
- FDA Clinical Pharmacology Section의 직접 언어
- NDA 표준 진술
```

이런 문장은 삭제하거나, 다음처럼 낮춰야 합니다.

```text
[교과서 외 실무 해석] SS=1을 부적절하게 적용하면 초기 축적 구간의 농도 예측이 왜곡되어 CL 추정과 용량 설계 판단에 영향을 줄 수 있다.
```

---

### 3. Scope Lock이 두 개가 병존해 Phase 2에서 혼선이 날 수 있습니다.

첨부된 Scope Lock에는 첫 번째 블록에서 R&T 페이지가 `[확인 필요]` 상태이고, Phase 1은 G 소스를 주 텍스트로 처리하라고 되어 있습니다. 이후 두 번째 블록에서는 R&T Ch.9–11과 Appendix I의 페이지가 p.267–358 + p.795–797로 확정되어 있습니다.

Draft는 두 번째 Scope Lock을 기준으로 작업한 것으로 보이고, R&T 통합도 실제로 잘 수행했습니다. 그러나 **Phase 2 감사자에게는 최종 Scope Lock 하나만 주는 것이 안전합니다.**

권장 조치:

```text
07_scope_lock_final.md를 새로 만들고,
첫 번째 [확인 필요] 블록은 삭제 또는 “superseded” 처리.
최종 범위는 다음으로 고정:
G: p.22–46, p.528–531, p.537–539
R&T: Ch.9 p.267–281, Ch.10 p.283–318, Ch.11 p.319–358, Appendix I p.795–797
```

---

### 4. PK13 앵커가 아직 약합니다.

Scope Lock은 PK11·PK13의 실제 수치를 §4 시뮬레이터 기본값 및 §6 시나리오에 반드시 인용하라고 명시합니다. 특히 PK13은 bolus 400 µg/kg + infusion 800 µg/kg over 26 min, Vc=2.0 L/kg, Cl=1.0 L/min/kg, Cld=1.0 L/min/kg, Vt=5.0 L/kg가 핵심입니다.

현재 Draft는 PK13을 Source-of-Record에 포함하고, Vss 추정법을 C3로 언급하지만, 실제 교육적 anchor로는 R&T의 heparin/eptifibatide/t-PA 및 sirolimus/doxycycline/digoxin 쪽이 더 강하게 들어가 있습니다.

Phase 1에서 §4·§6은 후속 단계 대기라고 되어 있으므로 fatal error는 아닙니다. 다만 Phase 4에서 다음을 강제해야 합니다.

```text
§4 Simulator 기본값:
- PK11 repeated oral dosing 기본값
- PK13 bolus + infusion 기본값

§6 Pragmatic Scenarios:
- PK13을 “bolus + infusion two-compartment implementation” 예제로 1개 배치
```

---

### 5. 압축이 아직 충분하지 않습니다.

현재 Draft는 Phase 1의 “많이 모으기”에는 성공했지만, Content Lock용으로는 과밀합니다. 워크플로우 자체도 Phase 1 이후 Source Fidelity Audit, Insight Crucible, Content Lock, Visual Pedagogy, HTML QA를 분리하도록 설계되어 있고, Phase 4에서는 CONTEXT-tier 항목을 1문장으로 압축하고 중복 내용을 한 위치에만 남기라고 지시합니다.

특히 다음은 압축 후보입니다.

```text
- M6 Therapeutic Window의 PD 사례 나열
- M7 loading dose 사례 표
- M8 TW-driven algorithm의 모든 식 나열
- §8 Professional Moat의 규제 언어 반복
- Zettelkasten Atom의 과도한 태그/별칭
```

목표는 **정보량을 줄이는 것**이 아니라, **MUST / CONTEXT / 적용 예시의 위계를 분명히 하는 것**입니다.

---

### 6. Phenobarbital R 값은 Phase 2에서 육안 확인이 필요합니다.

Draft에는 phenobarbital 예시에서 `t½ = 4 days`, `τ = 1 day`, `R = 5.8`이 들어가 있습니다. 그런데 수식 `R = 1/(1−2^{-τ/t½})`에 τ/t½ = 0.25를 넣으면 약 6.29입니다. R&T 본문은 plateau maximum/minimum이 약 630/530 mg이라고 설명하므로 100 mg dose 기준 maximum accumulation은 약 6.3에 가깝습니다.

다만 OCR/표기 맥락 때문에 단정적으로 오류라고 하기보다는, Phase 2에서 **R&T Ch.11 p.325–326 원문을 육안으로 확인**해야 합니다.

---

## 진행 판단

**Phase 1을 다시 처음부터 돌릴 필요는 없습니다.**
현재 결과물은 충분히 좋은 원석입니다. 다만 **“최종 Step 1”로 믿고 바로 HTML화하면 안 됩니다.**

가장 안전한 다음 순서는 다음입니다.

```text
1. 07_scope_lock_final.md 정리
2. Phase 2 Source Fidelity Audit 실행
   - M4 amount vs concentration 차원 오류 최우선 확인
   - NOT_IN_SOURCE 수치·규제 단정 전수 검출
   - phenobarbital R 값 육안 확인
   - PK11/PK13 수치 반영 위치 확인
   - Figure/Table T6 inventory 수행
3. Phase 3 Insight Crucible
   - 추가보다 삭제 후보를 강하게 요구
4. Phase 4 Content Lock
   - M4 수식 수정
   - unsupported 수치 삭제/라벨링
   - CONTEXT 압축
5. Phase 4C Figure Pointer 설계
6. 그 다음 HTML Compile
```

## 최종 결론

**이 Phase 1은 실패작이 아니라, 꽤 잘 나온 Draft v0입니다.**
하지만 “최적 작업 완료본”은 아닙니다. 핵심 개념 축과 소스 커버리지는 강하지만, **수식 차원 혼합 1개, 출처 없는 실무 수치/규제 단정, Scope Lock 병존, PK13 anchor 약화, 과밀도**가 남아 있습니다.

따라서 판정은:

```text
GO to Phase 2.
NO-GO to HTML.
Phase 1 redo 불필요.
Phase 2에서 MUST_FIX 잡고 Phase 4에서 압축·잠금 필요.
```

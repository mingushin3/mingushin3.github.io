# PK/PD Card-News HTML Generator
# 프로젝트 전역 지침 — Claude Code 자동 로드

---

## ① 역할 및 태도 (직접 지침 — 원문 그대로 적용)

당신은 임상약리학자이자 탁월한 미감을 지닌 S+급 교육 컨텐츠 디자이너입니다.

- 첨부한 md 파일의 내용/출처 손실 없이(최대한 잘 살려서), 가독성과 미감, 학습효율을 최대화한 카드뉴스형 슬라이드 html 생성해주세요.
- md 파일 원문 내용 한 글자도 생략하지 마세요.
- 수식 underbrace/overbrace annotation 렌더링 잘 되도록 해주세요(깨지거나 중첩되거나, 네모박스 생성 등 되지 않도록)
- 마크다운 서식 마감없이 그대로 노출되지 않도록 해주세요
- 슬라이드 수가 좀 늘어도 되니까(단, 전체 30개 정도 분량 이내), 폰트 크기도 큼직큼직하게 해주세요.
- 서체도 좀 세련되고 고급스러운거로 해주세요
- 주의: 다크 카드 내부의 텍스트는 반드시 흰색/앰버/코랄 등을 사용해서 눈에 선명하게 보이게 색상 신경써주세요(다크카드 내부 텍스트 색상 검정색/회색 계열 사용 절대금지)

---

## ② 기술 명세 참조 (필수)

이 프로젝트 폴더의 **PROMPT.md** 파일을 반드시 **전체** 읽고, 섹션 0~9의 모든 명세를 빠짐없이 적용한다.
- 절대 요약하거나 일부만 읽지 않는다
- PROMPT.md의 어떤 섹션도 건너뛰지 않는다
- 각 HTML 생성 전에 PROMPT.md를 처음부터 끝까지 다시 확인한다

---

## ③ 절대 원칙 (위반 시 즉시 재작업)

| 항목 | 규칙 |
|---|---|
| 내용 보존 | MD 원문 한 글자도 생략·축약·변형 금지 |
| 출처 | 모든 출처 표기를 인라인 칩으로 100% 보존 |
| 수식 구분자 | `$$...$$` / `\(...\)` 만 허용. `$...$` 단일 달러 전면 금지 |
| 다크 카드 텍스트 | 흰색(`#faf9f5`) / 앰버(`#e8a55a`) / 코랄(`#cc785c`) 계열만. 검정·회색 절대금지 |
| 마크다운 노출 | `#`, `**`, `*`, `>`, `` ` ``, `---` 등 기호가 렌더된 화면에 보이면 안 됨 |
| overflow | `.formula-card` 및 그 직계 조상에 `overflow: hidden` 절대 사용 금지 |
| 슬라이드 수 | 30개 이내 (내용 보존 위해 분할 허용) |
| 폰트 크기 | 제목 `clamp(26px, 3vw, 42px)` 이상으로 큼직하게 |

---

## ④ 출력 규칙

- **저장 위치**: 이 파일(CLAUDE.md)이 있는 폴더, 즉 현재 디렉토리
  - 경로: `/Users/min9/Documents/GitHub/mingushin3.github.io/05_NEW_교과서 html 작업/remastered_new/html 2차/`
- **파일명**: `{세션번호}_{topic}_cardnews.html`
  - 예시: `00_modeling_philosophy_cardnews.html`, `14_Allometry_cardnews.html`
  - 세션번호는 MD 파일명의 앞 두 자리 숫자를 따른다
- **형식**: 단일 HTML 파일 (CSS·JS 전부 인라인, 외부 파일 분리 없음)

---

## ⑤ 배치 자동 처리 규칙 (가장 중요 — 반드시 준수)

### 처리 대상 파일 목록 (00번부터 16번까지, 순서대로)

아래 경로의 MD 파일을 번호 순서대로 하나씩 처리한다.
이전 파일이 완전히 완료(저장+검증)된 후에만 다음 파일로 넘어간다.

```
/Users/min9/Documents/GitHub/mingushin3.github.io/05_NEW_교과서 html 작업/remastered_new/00_modeling_philosophy_remastered.md
/Users/min9/Documents/GitHub/mingushin3.github.io/05_NEW_교과서 html 작업/remastered_new/01_1cmt_IV_kinetics_remastered.md
/Users/min9/Documents/GitHub/mingushin3.github.io/05_NEW_교과서 html 작업/remastered_new/02_distribution_remastered.md
/Users/min9/Documents/GitHub/mingushin3.github.io/05_NEW_교과서 html 작업/remastered_new/03_oral_PK_remastered.md
/Users/min9/Documents/GitHub/mingushin3.github.io/05_NEW_교과서 html 작업/remastered_new/04_clearance_remastered.md
/Users/min9/Documents/GitHub/mingushin3.github.io/05_NEW_교과서 html 작업/remastered_new/05_two_compartment_remastered.md
/Users/min9/Documents/GitHub/mingushin3.github.io/05_NEW_교과서 html 작업/remastered_new/06_NCA_remastered.md
/Users/min9/Documents/GitHub/mingushin3.github.io/05_NEW_교과서 html 작업/remastered_new/07_T_치료역_항정상태_다중투여_축적_remastered.md
/Users/min9/Documents/GitHub/mingushin3.github.io/05_NEW_교과서 html 작업/remastered_new/08_nonlinearPK_remastered.md
/Users/min9/Documents/GitHub/mingushin3.github.io/05_NEW_교과서 html 작업/remastered_new/09_TMDD_remastered.md
/Users/min9/Documents/GitHub/mingushin3.github.io/05_NEW_교과서 html 작업/remastered_new/10_pkpd_emax_hill_auec_remastered.md
/Users/min9/Documents/GitHub/mingushin3.github.io/05_NEW_교과서 html 작업/remastered_new/11_indirect_response_remastered.md
/Users/min9/Documents/GitHub/mingushin3.github.io/05_NEW_교과서 html 작업/remastered_new/12_delay_hidden_states_remastered.md
/Users/min9/Documents/GitHub/mingushin3.github.io/05_NEW_교과서 html 작업/remastered_new/13_IIV_covariate_remastered.md
/Users/min9/Documents/GitHub/mingushin3.github.io/05_NEW_교과서 html 작업/remastered_new/14_Allometry_재구성판_final.md
/Users/min9/Documents/GitHub/mingushin3.github.io/05_NEW_교과서 html 작업/remastered_new/15_model_building_diagnostics_remastered.md
/Users/min9/Documents/GitHub/mingushin3.github.io/05_NEW_교과서 html 작업/remastered_new/16_clinical_capstone_remastered.md
```

### 파일 1개 처리 절차 (매 파일마다 반드시 이 순서로)

```
Step 1. CLAUDE.md 전체를 다시 읽는다 (Read tool 사용)
Step 2. PROMPT.md 전체를 다시 읽는다 (Read tool 사용)
Step 3. 해당 MD 파일을 읽는다
Step 4. HTML을 생성하고 현재 디렉토리에 저장한다
Step 5. PROMPT.md 섹션 9 체크리스트 전 항목을 검증한다
Step 6. 실패 항목이 있으면 수정 후 다시 저장한다
Step 7. "✓ {파일명} 완료 ({슬라이드 수}슬라이드)" 메시지를 출력한다
Step 8. 다음 파일로 넘어간다
```

**Step 1~2(지침 재독)는 생략할 수 없다. 매 파일마다 반드시 실행한다.**
지침을 이미 알고 있다고 판단해서 건너뛰는 것은 금지된다.
컨텍스트가 길어져도 지침 재독 단계는 절대 생략하지 않는다.

### 진행 상황 출력 형식

각 파일 완료 시 아래 형식으로 출력한다:
```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
✓ [03/17] 02_distribution_cardnews.html 완료
   슬라이드: 18개 | 검증: 전항목 통과
   다음: 03_oral_PK_remastered.md
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

## ⑥ 검증 (각 HTML 저장 전 필수 자체 점검)

PROMPT.md 섹션 9의 체크리스트 전 항목을 확인한다.
실패 항목이 하나라도 있으면 즉시 수정 후 최종본을 저장한다.

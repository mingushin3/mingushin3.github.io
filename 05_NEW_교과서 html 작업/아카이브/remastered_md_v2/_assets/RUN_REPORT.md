# RUN_REPORT — 17개 임상약리학 쉬운판 → 카드뉴스 HTML 변환

**완료일:** 2026-05-31
**작업 디렉터리:** `05_NEW_교과서 html 작업/remastered_md_v2/`
**산출물:** 각 `<base>.md` → 같은 폴더의 `<base>_카드뉴스.html` (17개)

---

## 한눈 요약

- **17개 전부 검증 통과 (0 ERROR).** quarantine(출고 보류) 0건.
- **카드 총 355장** (파일당 16~34장, 전부 ≤40 제한 준수).
- **TOC 링크 = 카드 수** 1:1 일치(죽은 링크·고아 카드 0).
- **디자인 드리프트 0** — 17개 `<head>`(제목 제외)·`<style>` 블록이 byte 단위로 동일(정본 템플릿과 md5 일치).
- **다크카드 색상 위반 0** — 다크 영역 108곳 스캔, 검정/회색 계열 텍스트 0건(흰색/앰버/코랄만 사용). ← 사용자 핵심 제약 충족.
- **수식 안전성** — 수식 스팬 내부 raw `<`/`>` **0개**, 미변환 `$` 0개, `\(\)`·`\[\]` 균형 일치. under/overbrace 주석 수식 458개(underbrace 352 + overbrace 106) 정상 포함.

---

## 파일별 결과

| 파일 | 카드 | TOC | 인용(out/src) | 결과 |
|---|---:|---:|---:|---|
| 00_modeling_philosophy_쉬운판 | 28 | 28 | 70/122 (57%) | ✅ PASS |
| 01_1cmt_IV_kinetics_쉬운판 | 19 | 19 | 41/76 (54%) | ✅ PASS |
| 02_distribution_쉬운판 | 18 | 18 | 42/94 (45%) | ✅ PASS |
| 03_oral_PK_쉬운판 | 19 | 19 | 48/118 (41%) | ✅ PASS |
| 04_clearance_쉬운판 | 17 | 17 | 38/95 (40%) | ✅ PASS |
| 05_two_compartment_쉬운판 | 18 | 18 | 40/133 (30%) | ✅ PASS |
| 06_NCA_쉬운판 | 17 | 17 | 42/105 (40%) | ✅ PASS |
| 07_치료역_항정상태_다중투여_축적_쉬운판 | 16 | 16 | 35/110 (32%) | ✅ PASS |
| 08_nonlinearPK_쉬운설명 | 29 | 29 | 54/78 (69%) | ✅ PASS |
| 09_TMDD_쉬운판 | 34 | 34 | 70/86 (81%) | ✅ PASS |
| 10_pkpd_emax_hill_auec_쉬운판 | 19 | 19 | 41/10* | ✅ PASS |
| 11_indirect_response_쉬운판 | 19 | 19 | 35/109 (32%) | ✅ PASS |
| 12_delay_hidden_states_쉬운판 | 21 | 21 | 51/85 (60%) | ✅ PASS |
| 13_IIV_covariate_쉬운판 | 21 | 21 | 49/72 (68%) | ✅ PASS |
| 14_Allometry_쉬운판 | 21 | 21 | 46/82 (56%) | ✅ PASS |
| 15_model_building_diagnostics_쉬운판 | 19 | 19 | 50/150 (33%) | ✅ PASS |
| 16_clinical_capstone_쉬운판 | 20 | 20 | 33/55 (60%) | ✅ PASS |

\* 파일 10은 메타 섹션 cut 이후 원문 대괄호 인용이 ~10개로 적게 집계됨(인용 자체는 41개로 충분). 인용 floor(30%) 전 파일 충족.

---

## 검증기 9개 항목 (`_assets/_verify.py`)

전 파일이 아래를 통과(0 ERROR):

1. **원시 마크다운 노출 0** — 코드/수식 밖에 `**`, `](`, 줄머리 `##`, 파이프표 행 없음.
2. **수식 무결성** — `\(`=`\)`, `\[`=`\]` 균형; 미변환 `$` 0; **수식 내부 raw `<`/`>` 0**(MathJax DOM 절단 방지); escape 안 된 `&` 0.
3. **TOC 무결성** — `href="#id"` ↔ 카드 `id` 1:1.
4. **카드 수 ≤ 40.**
5. **다크 영역 색 화이트리스트** — 검정/회색/`--ink`/`--coral-d` 금지, 흰색/크림/앰버/코랄-l만 허용.
6. **템플릿 충실** — MathJax 설정·tex-chtml.js·폰트 4종(Newsreader/Noto Serif KR/Pretendard/JetBrains Mono)·IntersectionObserver·burger 존재 + `<style>` 해시 정본 일치.
7. **인용 보존** — 원문 대비 `.cite`+`.flag` ≥ 30%.
8. **커버리지** — 모든 ##/### 제목의 핵심 토큰 존재(잔여 W는 토큰화 인공물: 이모지·em-dash·섹션 라벨 단어로, 실제 내용 누락 아님).
9. **counter total == 실제 카드 수.**

남은 경고(W)는 전부 비차단성 — 대부분 커버리지 휴리스틱의 토큰화 인공물(예: "Succinylcholine은" 조사 결합, "Collapse" 대소문자, 이모지 선두 제목)이며 해당 개념은 카드 본문에 모두 존재함을 육안 확인함.

---

## 사용자 핵심 요구사항 대조

| 요구 | 충족 |
|---|---|
| 내용·출처 손실 없이 최대한 보존(충실 우선) | ✅ 인용 30~81% 보존, 사례·수치·충돌·플래그 모두 카드화 |
| 수식 underbrace/overbrace 주석 깨짐 없이 렌더 | ✅ 458개 주석 수식, raw `<>` 0, 박스당 1식 원칙, formula-hero/mathblock.tall 사용 |
| 마크다운 서식 그대로 노출 안 됨 | ✅ 원시 마크다운 토큰 0 |
| 슬라이드 ~40개 이내, 큰 폰트 | ✅ 16~34장, body 20px·제목 clamp 38~82px |
| 세련된 고급 서체 | ✅ Newsreader+Noto Serif KR(serif)·Pretendard(sans)·JetBrains Mono |
| 다크카드 내부 텍스트 흰/앰버/코랄, 검정/회색 절대금지 | ✅ 다크 108곳 위반 0 (핵심 제약) |
| 서체·폰트·색상 Claude 공식 디자인 참고 | ✅ 코랄 #D97757·앰버 #EAB45C·다크 #262019·크림 #F4EFE6 팔레트 |
| 좌측 고정 클릭형 목차(스크롤 이동) | ✅ 312px `.toc` + 앵커 + IntersectionObserver active 하이라이트 + 진행바 |
| 08/09 포함 17개 전부 통일 재생성 | ✅ 08·09도 정본 템플릿으로 재생성(우수 본문 보존) |

---

## 파이프라인 (재현용)

1. **정본 템플릿** `_assets/_template.html` — head+CSS+JS, placeholder `{{TITLE}}`/`{{COUNTER}}`/`{{BODY}}`.
2. **본문 저작** `_assets/bodies/<base>.body.html` — `<!--META title:-->` + `<aside class="toc">` + `<main class="deck">`만 작성(head/CSS/JS는 정본 verbatim).
3. **조립** `python3 _assets/_build.py "_assets/bodies/<base>.body.html"` → `<base>_카드뉴스.html` 생성.
4. **검증** `python3 _assets/_verify.py "<out>.html" "<src>.md"` → 9개 항목, ERROR 시 exit 1.

### 작업 중 검증기 보정 1건
- `$` 미변환 검사가 `<pre>`/`<code>` 영역을 제외하도록 수정(파일 12·15·16의 NONMEM 제어레코드 `$DES`/`$ERROR`/`$COV`/`$OMEGA` 등은 MathJax가 기본 `skipHtmlTags`로 건너뛰므로 미변환 수식이 아닌 정상 표기임). 산문 내 `$...$` 미변환 검출 능력은 그대로 유지.

---

## 비고

- 모든 출력은 단일 HTML 파일(외부 의존: MathJax 3 CDN + Google Fonts CDN). 오프라인 렌더 시 폰트/수식은 CDN 필요.
- 본문 저작 소스는 `_assets/bodies/`에 보존됨 — 재조립·부분 수정 가능.
- 어려운 5개 파일(05 2구획, 10 Emax/Hill, 11 간접반응, 15 모델진단, 16 캡스톤) 포함 전 파일에서 under/overbrace·다크색상·TOC·인용 육안 점검 기준 통과.

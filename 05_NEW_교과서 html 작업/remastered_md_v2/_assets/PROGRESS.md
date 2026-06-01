# 카드뉴스 변환 — 진행 메모 (continuity)

## 목표
17개 `*_쉬운판.md`(00~16) → 각 `<base>_카드뉴스.html` (카드뉴스 슬라이드덱). 충실 보존 우선, ≤40 카드, 큰 폰트, Claude 팔레트, 좌측 고정 클릭 TOC, MathJax under/overbrace 정상 렌더, raw 마크다운 0, 다크카드 텍스트=흰/앰버/코랄만.

## 파이프라인 (자산: `_assets/`)
- `_template.html` — 동결 정본(head+CSS+JS). 플레이스홀더 `{{TITLE}} {{COUNTER}} {{BODY}}`.
- 각 파일은 **body fragment**만 저작 → `_assets/bodies/<base>.body.html` (형식: `<!--META\ntitle: …\n-->` + `<aside class="toc">…</aside>` + `<main class="deck">…</main>`).
- 빌드: `python3 _assets/_build.py "_assets/bodies/<base>.body.html"` → `<base>_카드뉴스.html` 생성(카드수로 counter 자동).
- 검증: `python3 _assets/_verify.py "<base>_카드뉴스.html" "<base>.md"` → `RESULT: PASS`(0 ERROR) 목표. WARN(coverage/cites)은 허용하되 최소화.
- 매니페스트(선택): `python3 _assets/_manifest.py "<base>.md"`.

## 방식
**메인 루프에서 직접 저작**(서브에이전트는 장시간 stall로 실패함 — 쓰지 말 것). 예시본 `_assets/bodies/00_modeling_philosophy_쉬운판.body.html`(검증 통과)이 디자인/컴포넌트/밀도 기준. 핵심 규칙:
- 수식 내부 `<`→`&lt;`, `>`→`&gt;`, 단독 `&`→`&amp;` (MathJax 디코드). `$…$`→`\(…\)`, `$$…$$`→`<div class="formula-hero"><div class="mathblock [tall][wide]">\[ … \]</div></div>`. 인용은 수식 밖으로.
- 산문 `&`→`&amp;`(G&W→G&amp;W), `**`→`<strong>`/`<b>`, `[cite]`→`<span class="cite">`, `[교과서 외]/[확인 필요]`→`<span class="flag">`.
- 다크카드 내부 inline `color:` 검정/회색 금지(CSS 기본=strong→amber, b→#fff).

## 상태
- [x] 00 exemplar (28 cards, PASS)
- [ ] 01 02 03 04 05 06 07 10 11 12 13 14 15 16 — 직접 저작
- [ ] 08 09 — 기존 우수 HTML 본문을 정본 템플릿으로 정규화(내용 보존)
- [ ] 최종: 17개 전체 검증 + RUN_REPORT.md + 최난도(05/10/11/15/16) 점검

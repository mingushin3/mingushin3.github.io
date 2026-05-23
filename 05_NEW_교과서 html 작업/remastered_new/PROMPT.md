# 카드뉴스형 슬라이드 HTML 생성 프롬프트 — 최종안
# 기술 명세 전체 (섹션 0~9) — 원문 그대로 적용

---

당신은 의학·과학 교육 콘텐츠를 전문으로 하는 시니어 프론트엔드 엔지니어다. 인터랙티브 슬라이드 구현, LaTeX 수식 렌더링, 교육용 UI 설계 모두에 능숙하다. 첨부된 마크다운 파일을 읽고, 아래 명세를 전부 충족하는 **단일 HTML 파일**을 생성하라.

출력 파일명은 `세션번호_topic_cardnews.html`로 한다.

---

## 0. 불변 원칙 (최우선)

**내용 보존이 모든 다른 원칙보다 우선한다.** 본문 텍스트·수식·출처·인용·경고문·표 데이터를 포함한 모든 내용은 단 한 글자도 삭제·축약·변형하지 않는다. 구조와 시각적 표현만 재설계한다.

### 0-1. 마크다운 잔재 완전 제거 (필수)

원본 마크다운의 문법 기호는 HTML 파일에 그대로 노출하지 않는다. 모든 마크다운 서식은 반드시 해당 HTML/CSS 컴포넌트로 변환한다:

| 마크다운 | 변환 대상 |
|---|---|
| `# 제목` / `## 소제목` | `slide-header h1` / `<h2 class="sub-title">` |
| `**굵게**` | `<strong>` |
| `*이탤릭*` | `<em>` |
| `` `인라인 코드` `` | `<code>` 태그 (수식 내용 제외) |
| `> 인용` | callout 스트립 컴포넌트 |
| `---` 구분선 | `<hr class="header-rule">` |
| `- 항목` / `1. 항목` | `<ul>` / `<ol>` |
| `| 표 |` | 테이블 컴포넌트 |

### 0-2. 내용 손실 vs 한 화면 충돌 해결 규칙

두 원칙이 충돌할 경우 **내용 보존을 우선**하되, 아래 순서로 한 화면 맞춤을 시도한다:

1. **레이아웃 재구성**: 2열 grid, compact 카드 배열, 섹션 분리
2. **슬라이드 분할**: 해당 섹션을 두 슬라이드로 나눈다 (총 슬라이드 수는 16개 이상으로 가변)
3. **접기 처리**: 표의 부가 열을 `<details>` 요소로 감싸 기본 접힘 상태로 제공
4. **font-size 축소**: 위 방법으로도 불가능할 때만 `clamp()` 하한까지 축소

내용을 생략하는 것은 어떤 상황에서도 허용하지 않는다.

---

## 1. 전체 레이아웃

화면은 세 영역으로 나뉜다.

### ① 왼쪽 고정 사이드바

`position: fixed`, 너비 260px, 배경 `#f5f0e8`, 전체 뷰포트 높이, 독립 스크롤(`overflow-y: auto`).

**상단 워드마크**: Anthropic 스파이크 마크 SVG(4방향 방사형 기호, 아래 SVG 코드 사용)

```html
<!-- 스파이크 마크 SVG -->
<svg width="18" height="18" viewBox="0 0 18 18" fill="none" xmlns="http://www.w3.org/2000/svg">
  <path d="M9 1v16M1 9h16M3.22 3.22l11.56 11.56M14.78 3.22L3.22 14.78"
        stroke="#cc785c" stroke-width="1.6" stroke-linecap="round"/>
</svg>
```

**목차 리스트**: §0~§10이며 §6은 하위 5개 항목(6-1 Maturation, 6-2 LBW/TBW, 6-3 Organ Function, 6-4 Dosing Strategy, 6-5 Pregnancy)을 8px 들여쓰기로 표시한다. 항목 클릭 시 해당 슬라이드로 즉시 이동한다. 현재 슬라이드의 목차 항목은 `border-left: 2px solid #cc785c`, 텍스트도 `#cc785c`로 강조한다.

### ② 중앙 슬라이드 뷰어

사이드바 오른쪽 나머지 영역 전체. 한 번에 슬라이드 하나만 표시한다. 슬라이드 전환 시 opacity 0→1 페이드 전환(duration 220ms)을 적용한다.

**한 화면 맞춤 CSS 규칙:**

```css
/* 뷰어 컨테이너 */
.viewer {
  position: fixed;
  left: 260px;
  top: 0;
  right: 0;
  bottom: 52px;           /* 내비바 높이 제외 */
  display: flex;
  flex-direction: column;
  overflow: hidden;       /* 뷰어 자체는 hidden */
}

/* 개별 슬라이드 */
.slide {
  position: absolute;
  inset: 0;
  display: flex;
  flex-direction: column;
  padding: 32px 48px 24px;
  overflow: hidden;       /* 슬라이드 자체 hidden */
  opacity: 0;
  pointer-events: none;
  transition: opacity 220ms ease;
}
.slide.active {
  opacity: 1;
  pointer-events: auto;
}

/* 수식 카드 예외: 조상 overflow 재선언 */
.slide .formula-card,
.slide .formula-card-wrap {
  overflow: visible !important;   /* KaTeX overbrace 클리핑 방지 */
}
```

**콘텐츠 밀도별 레이아웃 규칙** (아래 §1-A 참조):

- 콘텐츠가 적은 슬라이드: 1열, 여백 넉넉히
- 콘텐츠가 많은 슬라이드: 2열 `grid(gap: 16px)` 또는 compact 카드 배열

**font-size**: `body` 기본 14px, 제목 `clamp(26px, 3vw, 42px)`, 본문 `clamp(13px, 1.2vw, 16px)`.
고밀도 슬라이드(§6-intro, §6-2, §6-3)는 카드 padding을 12px, 섹션 간 margin을 8px로 축소한다.

### ① - A. 슬라이드별 레이아웃 지정

| 슬라이드 | 레이아웃 | 구성 |
|---|---|---|
| §0 | 1열 | 타이틀 + 핵심 요약 callout |
| §1 | 1열 | 서론 텍스트 + callout |
| §2 | 1열 | 개념 설명 |
| §3 | **2열** | 좌: 개념 설명 / 우: 수식 카드 |
| §4 | 1열 | |
| §5 | 1열 | |
| §6-intro | **2열** | 좌: 마스터 공식 설명 / 우: 수식 카드 2개 |
| §6-1 | **2열** | 좌: 설명+callout / 우: 수식 카드 |
| §6-2 | **2열** | 좌: LBW 설명+수식 / 우: TBW 설명+수식 |
| §6-3 | **2열** | 좌: 수식 카드 / 우: 표 |
| §6-4 | **2열** | 좌: 전략비교 수식 / 우: 알고리즘 박스 |
| §6-5 | **2열** | 좌: 설명 / 우: 수식+callout |
| §7 | 1열 | |
| §8 | 1열 | |
| §9 | 1열 | |
| §10 | 1열 | Closer 카드 |

*(원본 MD 내용에 따라 행 구성을 최적화하되, 위 2열/1열 방향은 유지한다)*

### ③ 하단 고정 내비게이션 바

`position: fixed; bottom: 0; left: 260px; right: 0; height: 52px`, `border-top: 1px solid #e6dfd8`, 배경 `#faf9f5`.

- 좌: `"← 이전"` 버튼
- 우: `"다음 →"` 버튼
- 중앙: `N / 16` 텍스트 + coral 프로그레스 바(높이 3px, `background: #cc785c`)
- 첫·마지막 슬라이드에서 해당 버튼은 `disabled` + `opacity: 0.35`

**슬라이드 단위 (총 16개, 분할 시 가변):**
§0, §1, §2, §3, §4, §5, §6-intro, §6-1, §6-2, §6-3, §6-4, §6-5, §7, §8, §9, §10

키보드 `←` `→` 방향키로도 슬라이드를 이동할 수 있다.

---

## 2. 디자인 시스템 — Claude / Anthropic 공식 토큰 기반

아래는 Anthropic의 공식 디자인 시스템 토큰이다. **모든 색상·타이포그래피·간격은 이 토큰을 기준으로 구현한다.**

### 2-1. 컬러 토큰

```
/* Surface */
canvas:               #faf9f5   /* 기본 페이지 바닥 — 따뜻한 크림, 절대 순백 사용 안 함 */
surface-soft:         #f5f0e8   /* 섹션 구분, 사이드바 배경 */
surface-card:         #efe9de   /* 콘텐츠 카드 배경 */
surface-cream-strong: #e8e0d2   /* 강조 섹션 밴드 */
surface-dark:         #181715   /* 코드 블록, 다크 카드, 알고리즘 박스 */
surface-dark-elevated:#252320   /* 다크 카드 내부 승격 패널 */
surface-dark-soft:    #1f1e1b   /* 코드 블록 내부 배경 */
hairline:             #e6dfd8   /* 1px 보더 */
hairline-soft:        #ebe6df   /* 같은 밴드 내 구분선 */

/* Brand */
coral:                #cc785c   /* 시그니처 액센트 — 기본 CTA, 워드마크 */
coral-active:         #a9583e   /* 호버/프레스 다크 변형 */
coral-pale:           #f4e4dc   /* 연한 배경 강조 */
coral-disabled:       #e6dfd8   /* 비활성 상태 */
accent-teal:          #5db8a6   /* 보조 포인트 */
accent-amber:         #e8a55a   /* 카테고리 배지, 인라인 하이라이트 */

/* Text */
ink:                  #141413   /* 헤드라인, 주요 텍스트 */
body-strong:          #252523   /* 강조 단락 */
body:                 #3d3d3a   /* 본문 */
muted:                #6c6a64   /* 보조 텍스트 */
muted-soft:           #8e8b82   /* 캡션, 미주 */
on-primary:           #ffffff   /* 코랄 버튼 위 텍스트 */
on-dark:              #faf9f5   /* 다크 서피스 위 텍스트 */
on-dark-soft:         #a09d96   /* 다크 서피스 보조 텍스트 */

/* Semantic */
warn-bg:              #fcf0ef   warn-border: #c64545
amber-bg:             #fdf4e0   amber-border:#d4a017
teal-bg:              #e6f4f0   teal-border: #5db8a6
success:              #5db872
```

### 2-2. 타이포그래피 토큰

Anthropic 공식 서체는 라이선스 전용(Copernicus / StyreneB)이므로, Google Fonts에서 제공하는 **공식 대체 폰트**를 사용한다.

```
디스플레이(서체):  Cormorant Garamond → 'Cormorant Garamond', Georgia, 'Times New Roman', serif
                   weight 400, letter-spacing: -0.02em
                   (Copernicus / Tiempos Headline의 공식 대체)

본문·UI(서체):     Inter + Noto Sans KR → 'Inter', 'Noto Sans KR', 'Apple SD Gothic Neo',
                   -apple-system, BlinkMacSystemFont, sans-serif
                   weight 400 / 500 / 600
                   (StyreneB의 공식 대체)

코드·수식·배지:    JetBrains Mono → 'JetBrains Mono', 'Courier New', monospace
                   weight 400 / 500
```

**Google Fonts 로드 (head 내):**
```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,400;0,500;1,400;1,500&family=Inter:wght@400;500;600&family=JetBrains+Mono:wght@400;500&family=Noto+Sans+KR:wght@400;500;600&display=swap" rel="stylesheet">
```

**타이포그래피 스케일:**

| 역할 | 크기 | Weight | Letter-spacing | 서체 |
|---|---|---|---|---|
| 슬라이드 제목 | clamp(26px, 3vw, 42px) | 400 | -0.02em | Cormorant Garamond |
| 소제목 | clamp(17px, 1.8vw, 24px) | 500 | 0 | Inter |
| 본문 | clamp(13px, 1.2vw, 16px) | 400 | 0 | Inter / Noto Sans KR |
| 강조 본문 | 상동 | 500 | 0 | Inter |
| 코드·출처·배지 | 11–13px | 400/500 | 0–1.5px | JetBrains Mono |
| 버튼 | 14px | 500 | 0 | Inter |

### 2-3. 간격·모서리

```
모서리(radius): 콘텐츠 카드 12px / 버튼 8px / 배지·pill 9999px
섹션 간격:      기본 16px / 고밀도 슬라이드 8px
카드 padding:   기본 20px 24px / 고밀도 12px
헤더 높이:      최대 72px
```

---

## 3. 카드 컴포넌트 명세

### 일반 카드
배경 `#efe9de`, border `1px solid #e6dfd8`, radius 12px, padding `20px 24px`.

### 소프트 카드
배경 `#f5f0e8`, border `1px solid #e6dfd8`, radius 12px, padding `20px 24px`.

### 수식 카드 (`.formula-card`)
배경 `#f5f0e8`, border `1px solid #e6dfd8`, radius 12px.
padding: top 36px, bottom 28px, left/right 20px.
`text-align: center`, `overflow-x: auto`, **`overflow-y: visible`** (절대 hidden 아님).
수식 아래에 출처를 `JetBrains Mono` 11px `#6c6a64`로 표시한다.

**⚠️ 수식 카드와 그 직계 조상 요소 전체에 `overflow: hidden`을 쓰지 않는다.**
대신 `.formula-card-wrap { overflow: visible !important }`를 명시한다.
수식이 포함된 슬라이드의 상단 padding은 최소 48px 이상으로 확보해 `\overbrace` 레이블 공간을 보장한다.

### 다크 카드
배경 `#181715`, radius 12px, padding `20px 24px`.
**이 카드 내 모든 텍스트 색상을 명시적으로 선언한다 (`color: inherit`에만 의존하지 않음):**
```css
.dark-card p     { color: #a09d96; }
.dark-card strong{ color: #faf9f5; }
.dark-card em    { color: #a09d96; }
.dark-card li    { color: #a09d96; }
.dark-card li::marker { color: #cc785c; }
.dark-card h2, .dark-card h3 { color: #faf9f5; }
```

### 알고리즘 박스
배경 `#181715`, 텍스트 색상 `#a09d96` (반드시 명시), `font-family: 'JetBrains Mono', monospace`, font-size 12px, line-height 1.8, `white-space: pre`, `overflow-x: auto`, radius 12px.

### Callout 스트립
`border-left: 3px solid [색상]`, radius `0 8px 8px 0`, padding `13px 17px`.

| 종류 | 배경 | 보더 |
|---|---|---|
| 기본 강조 | `#f4e4dc` | `#cc785c` |
| 경고 | `#fcf0ef` | `#c64545` |
| 주의 | `#fdf4e0` | `#d4a017` |
| 포인트 | `#e6f4f0` | `#5db8a6` |

### Closer 카드
다크 카드 기반. 상단에 `JetBrains Mono` 10px coral 레이블(`letter-spacing: 1.5px; text-transform: uppercase`). 본문은 `Cormorant Garamond` 이탤릭 17px `#a09d96`.

### 테이블
`div` 래퍼: border `1px solid #e6dfd8`, radius 12px, `overflow: clip` (**`hidden` 아님** — KaTeX 수식 보호). `thead` 배경 `#efe9de`. 행 구분선 `#ebe6df`. font-size 13px. `thead` 첫 행 `padding-top: 16px` (수식 annotation 공간 확보).

### 출처 칩
`JetBrains Mono` 10.5px, 배경 `#efe9de`, padding `1px 6px`, radius 4px, 인라인 배치.

---

## 4. 수식 렌더링 — KaTeX (엄수 사항)

### 4-1. 스크립트 로딩 순서

`<head>`에 KaTeX CSS **만** 배치한다 (스크립트 없음):
```html
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/katex.min.css">
```

`</body>` 닫기 태그 **직전**에 아래 순서대로, **`defer`·`async` 속성 없이** 동기 로드한다:
```html
<script src="https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/katex.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/contrib/auto-render.min.js"></script>
<script>
/* ← 여기에 앱 스크립트 전체 (슬라이드 로직 + renderMath) */
</script>
```

### 4-2. renderMathInElement 호출 패턴

```js
function renderMath() {
  renderMathInElement(document.body, {
    delimiters: [
      { left: '$$',  right: '$$',  display: true  },
      { left: '\\(', right: '\\)', display: false }
    ],
    throwOnError: false,
    strict: false
  });
}
if (document.readyState === 'loading') {
  document.addEventListener('DOMContentLoaded', renderMath);
} else {
  renderMath();
}
```

### 4-3. 구분자 규칙 — 엄격히 적용

| 용도 | 사용 | 금지 |
|---|---|---|
| 디스플레이 수식 | `$$...$$` (수식 카드 안, 별도 줄) | `\[...\]` |
| 인라인 수식 | `\(...\)` | `$...$` 단일 달러 |

**`$...$` 단일 달러 구분자는 HTML 파일 전체에 단 한 곳도 사용하지 않는다.**

### 4-4. 수식 배치 금지 위치

`<code>`, `<pre>` 태그 안에 `\(...\)` 또는 `$$...$$`를 배치하지 않는다.
KaTeX auto-render가 해당 태그를 건너뛰어 날것 문자로 노출된다.

### 4-5. 수식 컨테이너 CSS

```css
/* 수식 카드 자체 */
.formula-card {
  overflow-x: auto;
  overflow-y: visible;   /* 절대 hidden 아님 */
}

/* KaTeX 전역 오버라이드 */
.katex-display {
  overflow-y: visible !important;
  margin: 0 !important;
  padding: 4px 0 !important;
}
.katex-display > .katex {
  overflow-y: visible !important;
}

/* 수식이 포함된 슬라이드: overbrace 상단 레이블 공간 */
.slide.has-formula {
  padding-top: 48px;
}
```

슬라이드 컨테이너(`.slide`)는 `overflow: hidden`을 사용하되,
`.formula-card-wrap`과 `.formula-card`에는 `overflow: visible !important`를 명시해 KaTeX가 생성하는 절대위치 레이블 요소가 클리핑되지 않도록 한다.

---

## 5. Annotation 겹침 방지 규칙

`\overbrace`·`\underbrace` 레이블이 **수직으로 3단 이상 중첩**되는 수식은 `aligned` 환경으로 분리해 한 줄에 2단 이하만 남긴다.

**§6-intro 마스터 공식** — backbone 항 첫째 줄, 보정 계수 5개 둘째 줄:

```
$$\underbrace{Dose_{patient}}_{\text{환자 dose}}=
\overbrace{\underbrace{Dose_{std}}_{\text{표준}}\cdot\left(\frac{BW}{70}\right)^{0.75}}^{\text{C5 backbone}}
\cdot\overbrace{F_{mat}}^{\text{성숙}}\cdot\overbrace{f_{size}}^{\text{LBW/TBW}}$$
$$\cdot\;\overbrace{[RF\cdot fe+(1-fe)\cdot\text{age factor}]}^{\text{장기 기능}}
\cdot\overbrace{f_{strategy}}^{\text{전략}}\cdot\overbrace{f_{preg}}^{\text{임신}}$$
```

**§6-4 전략 비교식** — `aligned`로 세로 배열:

```
$$\begin{aligned}
&\overbrace{\underbrace{Dose_{mg/kg}}_{\text{체중 비례}}=k_1\cdot BW}^{\text{Strategy 1}}\\[1.2em]
&\overbrace{\underbrace{Dose_{mg/m^2}}_{\text{BSA 비례}}=k_2\cdot BSA}^{\text{Strategy 2}}\\[1.2em]
&\overbrace{\underbrace{Dose_{allom}}_{\text{알로메트릭}}=k_3\cdot BW^{0.75}}^{\text{Strategy 3}}
\end{aligned}$$
```

**§6-3 R_d 식** — `\overbrace` 제거, `\underbrace` 1단만 유지:

```
$$R_d=\underbrace{RF\cdot fe(t)}_{\text{신장 경로}}
+\underbrace{\left[1-fe(t)\right]\cdot\frac{(140-Age)\cdot Wt^{0.75}}{1936}}_{\text{간 경로}}$$
```

그 외 분수 내부에 `\overbrace`·`\underbrace`가 2단 이상 중첩된 수식은 레이블을 변수 약어로 단순화하고, 수식 카드 아래 각주로 설명을 추가한다.

---

## 6. 슬라이드 헤더 구조

각 슬라이드 최상단에 다음 구조를 배치한다:

```html
<div class="slide-header">
  <span class="sec-badge">§ N</span>
  <!-- coral(#cc785c) 배경, white(#fff) 텍스트, JetBrains Mono 11px, letter-spacing 1px -->
  <h1 class="slide-title">제목</h1>
  <!-- Cormorant Garamond, clamp(26px,3vw,42px), weight 400, color #141413 -->
</div>
<hr class="header-rule">
<!-- height: 1.5px, background: #e6dfd8, margin-bottom: 14px -->
```

**헤더 전체 높이는 최대 72px**를 넘지 않도록 margin·padding을 제어한다.

---

## 7. 슬라이드 구현 JavaScript

```js
var TOTAL = 16;   // 슬라이드 분할 시 실제 총 수로 업데이트
var cur = 0;
var slides = document.querySelectorAll('.slide');
var tocBtns = document.querySelectorAll('.toc-btn');
var progText = document.getElementById('prog-text');
var progFill = document.getElementById('prog-fill');
var btnPrev = document.getElementById('btn-prev');
var btnNext = document.getElementById('btn-next');

function goTo(n) {
  if (n < 0 || n >= TOTAL) return;
  slides[cur].classList.remove('active');
  tocBtns[cur].classList.remove('active');
  cur = n;
  slides[cur].classList.add('active');
  tocBtns[cur].classList.add('active');
  tocBtns[cur].scrollIntoView({ block: 'nearest', behavior: 'smooth' });
  progText.textContent = (cur + 1) + ' / ' + TOTAL;
  progFill.style.width = ((cur + 1) / TOTAL * 100) + '%';
  btnPrev.disabled = (cur === 0);
  btnNext.disabled = (cur === TOTAL - 1);
}

btnPrev.addEventListener('click', function() { goTo(cur - 1); });
btnNext.addEventListener('click', function() { goTo(cur + 1); });
document.addEventListener('keydown', function(e) {
  if (e.key === 'ArrowLeft')  goTo(cur - 1);
  if (e.key === 'ArrowRight') goTo(cur + 1);
});

goTo(0);
```

---

## 8. 시각 디자인 원칙 (Claude / Anthropic 브랜드 가이드 준수)

1. **캔버스는 항상 크림색** — `#faf9f5`. 순백(`#ffffff`)이나 쿨 그레이는 브랜드에 어긋난다.
2. **디스플레이 헤드라인은 Cormorant Garamond weight 400** — 굵게(700) 쓰지 않는다. 부정적 자간(-0.02em)은 필수.
3. **Coral은 희소하게** — 배지·버튼·헤더 강조에만 사용. 대면적은 다크 카드(#181715)나 소프트 카드(#f5f0e8)로 처리.
4. **크림 → 소프트카드 → 다크** 서피스 교차 리듬으로 슬라이드 흐름의 시각적 박자를 만든다.
5. **코드·알고리즘은 반드시 다크 카드** 위에 올린다 — 제품 크롬을 직접 보여주는 방식.
6. **시원하게 = 여백을 과감히** — 각 슬라이드에서 콘텐츠가 뷰포트의 85% 이상을 차지하지 않도록 상하 여백을 유지한다.

---

## 9. 검증 체크리스트

생성 완료 후 다음 항목을 자체 검증한다:

**수식 렌더링**
- [ ] `$...$` 단일 달러 구분자가 HTML 파일 전체에 없다
- [ ] `\(...\)` 인라인 수식이 `<code>`, `<pre>` 태그 안에 없다
- [ ] `katex.min.js` → `auto-render.min.js` → 앱 스크립트 순서가 지켜졌고 `defer`/`async`가 없다
- [ ] `renderMath` 호출이 `readyState` 분기를 포함한다
- [ ] §6-intro 마스터 공식, §6-3 Rd식, §6-4 전략식이 §5의 분리된 형태로 작성되었다
- [ ] `.formula-card`와 그 직계 조상에 `overflow: hidden`이 없다 (`overflow: visible` 명시)

**마크다운 잔재**
- [ ] `#`, `**`, `*`, `>`, `` ` ``, `---` 등 마크다운 기호가 렌더된 HTML에 보이지 않는다
- [ ] 모든 마크다운 서식이 대응 HTML 컴포넌트로 변환되었다

**내용 보존**
- [ ] 원본 MD의 모든 출처 표기가 인라인 칩 형태로 존재한다
- [ ] 원본 MD의 모든 경고·주의 문구가 callout 카드로 존재한다
- [ ] 생략·축약된 내용이 없다

**레이아웃**
- [ ] 모든 슬라이드가 내부 스크롤 없이 한 화면에 완전히 표시된다
- [ ] §1-A 표에 지정된 2열/1열 레이아웃이 적용되었다
- [ ] 다크 카드 내 `p`, `li`, `strong`, `em`, `h2` 각각에 밝은 색이 명시되어 있다
- [ ] 슬라이드가 총 16개(분할 시 그 이상)이고 TOC 항목과 1:1 대응된다
- [ ] 헤더 높이가 72px를 넘지 않는다

**브랜드**
- [ ] 캔버스 색상이 `#faf9f5`(크림)이다. 순백 `#fff`이 아니다
- [ ] 디스플레이 헤드라인에 Cormorant Garamond weight 400이 적용되어 있다
- [ ] font-family 선언 전체에 system fallback이 포함되어 있다
- [ ] 출력 파일명이 `세션번호_topic_cardnews.html`이다

---

이 명세와 지정된 마크다운 파일을 사용하여 단일 `.html` 파일을 생성하라.

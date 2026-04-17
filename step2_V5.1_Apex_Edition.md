# PK/PD MASTERY PROTOCOL — STEP 2: HTML COMPILER
# V5.1 Apex Edition | 28-Session Mastery Framework
# ─────────────────────────────────────────────────────────────
# [변경 이력] V5.0 → V5.1: 인터랙티브 시뮬레이터 그래프 팽창 버그 4종 수정
# [사용법] "계속" 입력 직후 이 프롬프트 전체를 새 메시지로 붙여넣기
# [역할] Step 1 전체(§1·§2·§5·§7·§8) + §3·§4·§6을 단일 완성 HTML로 통합 출력
# ─────────────────────────────────────────────────────────────

---

## ⚑ V5.1 버그 픽스 노트 — 슬라이더 조작 시 그래프 팔레트 무한 팽창 수정

아래 4가지 버그가 복합적으로 작용하여 슬라이더를 특정 구간에서 조작하면 canvas가
무한히 아래로 늘어지는 현상이 발생했다. V5.1에서 모두 수정한다.

### 버그 ① — 치명 (주원인): mousemove 리스너 누적
**원인**: `updateChart()` 내부에서 `simChart.canvas.addEventListener('mousemove', ...)` 를
매 호출마다 등록한다. `chartObj.destroy()` 후 `new Chart()` 로 차트를 재생성해도
canvas DOM 엘리먼트 자체는 유지되므로, 슬라이더를 N번 조작하면 리스너가 N개
누적된다. 누적된 리스너 각각이 Chart.js 내부 resize 감지를 트리거하여 canvas
높이가 기하급수적으로 증가한다.

**수정**: 이벤트 리스너를 `updateChart()` 밖 초기화 단계(DOMContentLoaded 또는
최초 1회)에서 단 한 번만 등록한다. `updateChart()` 내부에서 리스너를 절대 등록
하지 않는다.

```javascript
// ❌ V5.0 잘못된 코드 — updateChart() 내부에서 매번 등록
function updateChart() {
  // ... 차트 생성 코드 ...
  simChart.canvas.addEventListener('mousemove', e => { ... }); // ← 누적 버그
}

// ✅ V5.1 수정 코드 — 초기화 단계에서 단 한 번만 등록
// updateChart() 완전히 밖에 위치
simChart.canvas.addEventListener('mousemove', e => {
  if (!state._currentCurve) return;
  const rect = simChart.canvas.getBoundingClientRect();
  const t = (e.clientX - rect.left) / rect.width * X_MAX;
  const idx = Math.min(Math.floor(t / DT), state._currentCurve.ts.length - 2);
  const C = state._currentCurve.cs[idx] || 0;
  document.getElementById('cursorLabel').textContent =
    `t = ${t.toFixed(1)} min | C = ${C.toFixed(4)} µg/mL`;
});
// state._currentCurve 는 updateChart()가 호출될 때마다 갱신
```

---

### 버그 ② — 중요: Y_MAX 동적 재계산으로 Anti-Jitter 원칙 위반
**원인**: `Y_MAX = Math.max(C0 * 1.5, 3)` 가 슬라이더마다 재계산되므로 축 범위가
슬라이더 값에 따라 변한다. 고용량(dose=10000) 프리셋 → 저용량 복귀 시 Y축이
수축하지 않거나, 특정 dose/vol 조합에서 `C0*1.5` 값이 이전 chartObj의 내부 max
와 충돌하여 canvas layout을 재측정하게 만든다.

**수정**: Y_MAX를 모듈 최상단에서 상수(HARD_Y_MAX)로 선언하고 절대 변경하지 않는다.
실제 C0가 HARD_Y_MAX를 초과하는 경우 경고 배너로 알리되 축은 고정 유지한다.
Log 스케일 전환 시에도 `min`/`max`를 하드코딩된 값으로 지정한다.

```javascript
// ✅ V5.1: 모듈 최상단 상수 선언 — 절대 변경 금지
const X_MAX    = 90;    // min, 고정
const HARD_Y_MAX = 10;  // µg/mL, 고정 (PK17 C0 최대값 10000/500=20이지만 슬라이더 max에서 1800/500=3.6)
const LOG_Y_MIN  = 0.001;
const LOG_Y_MAX  = 100;
const DT         = 0.5; // Runge-Kutta 적분 step, min

// updateChart() 내부
scales: {
  x: { type:'linear', min:0, max:X_MAX },          // ← 슬라이더 이벤트 내부 재선언 금지
  y: {
    type: state.logScale ? 'logarithmic' : 'linear',
    min:  state.logScale ? LOG_Y_MIN : 0,
    max:  state.logScale ? LOG_Y_MAX : HARD_Y_MAX,  // ← 상수 사용, 절대 C0*1.5 금지
  }
}

// C0 > HARD_Y_MAX 초과 시 경고 배너만 표시
if (C0 > HARD_Y_MAX * 0.9) {
  warnBanner.textContent = '⚠ C₀가 Y축 범위 상한에 근접 — 고농도 영역은 Log 스케일로 전환하세요';
  warnBanner.classList.add('show');
}
```

---

### 버그 ③ — 중요: destroy/recreate 루프에서 canvas 높이 재측정 충돌
**원인**: `responsive: true` + `maintainAspectRatio: false` 조합에서 Chart.js는
매 destroy/new Chart() 사이클마다 부모 컨테이너의 clientHeight를 재측정한다.
canvas의 CSS height가 `320px`으로 고정되어 있어도, Chart.js가 destroy 직전
canvas.style.height를 수정하면 다음 new Chart()가 더 큰 높이를 측정하고,
이것이 반복되면서 canvas가 단계적으로 팽창한다.

**수정**: destroy/recreate 패턴을 `chart.data`와 `chart.update()` 패턴으로
교체한다. 최초 1회만 Chart 인스턴스를 생성하고, 이후 슬라이더 조작 시에는
`chartObj.data.datasets[n].data = newData` + `chartObj.update('none')` 으로
데이터만 교체한다. 이렇게 하면 canvas DOM이 재생성되지 않아 크기가 안정된다.
`update('none')`은 애니메이션을 끄므로, 별도 `animation: {duration: 200}` 설정은
초기 Chart 생성 시 옵션으로 지정한다 (슬라이더 이벤트와 무관하게 적용됨).

canvas 크기 안정화를 위해 `.canvas-wrap`에 명시적 height를 설정하고
`overflow: hidden`을 추가한다:

```css
/* ✅ V5.1 추가 CSS */
.canvas-wrap {
  position: relative;
  height: 320px;        /* ← 명시적 고정 높이 */
  overflow: hidden;     /* ← Chart.js 크기 탈출 방지 */
  flex-shrink: 0;       /* ← flex 부모에서 수축 방지 */
}
#simCanvas {
  width: 100% !important;
  height: 100% !important;  /* ← canvas-wrap 높이에 종속 */
  display: block;
  cursor: crosshair;
}
```

```javascript
// ❌ V5.0 잘못된 패턴 — 매번 destroy/recreate
function updateChart() {
  if (chartObj) chartObj.destroy();
  chartObj = new Chart(ctx, { type:'line', data:{datasets}, options:{...} });
}

// ✅ V5.1 수정 패턴 — 초기 1회 생성 + data만 교체
let chartObj = null;

function initChart() {
  chartObj = new Chart(simChart.ctx, {
    type: 'line',
    data: { datasets: buildDatasets() },
    options: {
      animation: { duration: 200 },
      responsive: true,
      maintainAspectRatio: false,
      scales: {
        x: { type:'linear', min:0, max:X_MAX, /* ... */ },
        y: { type:'linear', min:0, max:HARD_Y_MAX, /* ... */ }
      },
      // ...
    }
  });
}

function updateChart() {
  if (!chartObj) { initChart(); return; }
  
  // ① 데이터만 교체 (DOM 변경 없음)
  const ds = buildDatasets();
  chartObj.data.datasets = ds;
  
  // ② Y축 타입만 교체 (log 토글 시)
  chartObj.options.scales.y.type = state.logScale ? 'logarithmic' : 'linear';
  chartObj.options.scales.y.min  = state.logScale ? LOG_Y_MIN : 0;
  chartObj.options.scales.y.max  = state.logScale ? LOG_Y_MAX : HARD_Y_MAX;
  
  // ③ 애니메이션 없이 즉시 업데이트 — canvas 크기 재측정 없음
  chartObj.update('none');
}
```

---

### 버그 ④ — 보통: normCanvas drawNorm()에서 canvas 크기 재할당
**원인**: `drawNorm()` 내부에서 `canvas.width = canvas.offsetWidth * devicePixelRatio`
를 실행한다. `canvas.width` 를 변경하면 canvas 전체가 리셋되는 것 외에도,
부모 레이아웃의 reflow를 유발한다. `resize` 이벤트 핸들러에서 이를 반복 호출하면
normCanvas뿐 아니라 인접 DOM 요소(simCanvas 포함)의 크기가 재측정된다.

**수정**: normCanvas는 CSS `width:100%`, `height:260px` 고정을 유지하되,
`canvas.width`/`canvas.height` 할당을 초기화 단계에서 1회만 수행한다.
이후 `resize`에서는 scale만 재적용하고 canvas 크기는 변경하지 않는다.
또한 `normCtx.scale(1,1)` 호출도 제거한다(누적 transform 버그 방지).

```javascript
// ❌ V5.0 잘못된 코드 — drawNorm() 내부 매번 재할당
function drawNorm() {
  const canvas = document.getElementById('normCanvas');
  const W = canvas.width  = canvas.offsetWidth  * window.devicePixelRatio; // ← 재할당 버그
  const H = canvas.height = canvas.offsetHeight * window.devicePixelRatio; // ← 재할당 버그
  const ctx = normCtx;
  ctx.scale(1, 1); // ← 누적 transform 버그
  // ...
}

// ✅ V5.1 수정 코드 — 초기화 단계 1회 할당 + 그리기만 반복
let normW, normH;
function initNormCanvas() {
  const canvas = document.getElementById('normCanvas');
  const dpr = window.devicePixelRatio || 1;
  normW = canvas.width  = Math.floor(canvas.offsetWidth  * dpr);
  normH = canvas.height = Math.floor(canvas.offsetHeight * dpr);
  // context state 고정
  normCtx.setTransform(1, 0, 0, 1, 0, 0); // identity 초기화
}
function drawNorm() {
  if (!normW || !normH) return;
  normCtx.clearRect(0, 0, normW, normH);
  // ... 그리기 코드 (W=normW, H=normH 사용) ...
}
// resize 시에는 initNormCanvas() + drawNorm() 순서로 호출
// simCanvas에는 영향 없도록 분리
window.addEventListener('resize', () => {
  initNormCanvas();
  drawNorm();
  // chartObj의 resize는 Chart.js가 자체 처리 — 수동 개입 금지
});
```

---

## TASK

Step 1에서 분석한 소스 내용과 생성된 모든 텍스트를 바탕으로, **완전한 단일
self-contained HTML 파일 하나를 지금 즉시 생성한다.**

포함 섹션 순서: §1 → §2 → §3 → §4 → §5 → §6 → §7 → §8

- **§1·§2·§5·§7·§8**: Step 1 텍스트를 100% HTML 태그 안에 복원 (요약·플레이스홀더 절대 금지)
- **§3·§4·§6**: 아래 명세에 따라 신규 생성

---

## ⚑ LANGUAGE & FONT DIRECTIVE

- 산문: 한국어 / 수식·코드·고유명사: 영어
- Noto Sans KR Google Fonts CDN 필수:
  `https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@300;400;500;700`
- Cormorant Garamond (제목 serif, CDN):
  `https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@400;600;700`
- IBM Plex Mono (코드·파라미터, CDN):
  `https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:wght@400;500`

---

## DESIGN REQUIREMENTS

**Dark Academic 테마:**

```css
:root {
  --bg:         #09090e;
  --surface:    #0c0c12;
  --text:       #ede8df;
  --muted:      #8a8070;
  --accent:     #c9a84c;
  --accent-dim: rgba(201, 168, 76, 0.08);
  --danger:     #c0392b;
  --info:       #4098e8;
  --phantom:    rgba(220, 60, 60, 0.55);
}
```

### §2 개념 카드 스타일
- **[개념 Big Idea: 거장의 시각] 블록**: 금색 좌측 보더 4px + `rgba(201,168,76,0.08)` 배경. §2 각 카드 최상단.
- **[⚡ Apex Concept] 배지**: 금색 배경 + 어두운 텍스트 인라인 배지.
- **C-2 Plausible Fallacy 블록**: 붉은 좌측 보더 + `rgba(192,57,43,0.08)` 배경. C항목 바로 아래.
- **Micro-citation 태그**: `font-size: 0.78em; color: var(--muted); font-style: italic;` 인라인. 수식·코드 바로 옆 또는 아래.

### §5 테이블 스타일
- **Critical Blow 행**: 테이블 내 해당 행 배경 `rgba(192,57,43,0.12)`, 텍스트 볼드.
- **기억 고리 행**: 금색 텍스트 `var(--accent)`, 배경 `rgba(201,168,76,0.06)`.

### MathJax 설정 (반드시 `<head>` 내 포함):

```html
<script>
MathJax = {
  tex: {
    inlineMath: [['$','$']],
    displayMath: [['$$','$$']],
    processEscapes: true
  },
  options: { skipHtmlTags: ['script','noscript','style','textarea','pre'] }
};
</script>
<script async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-chtml.js"></script>
```

`$`·`$$` 구분자는 렌더링 후 절대 노출 금지.

---

## Navigation Sidebar (고정)

- 너비 240px, 모바일 접이식 (`< 768px` 숨김·전폭)
- §1–§8 한국어 레이블 + §2 각 개념카드·§5 각 혼동쌍 서브아이템
- **IntersectionObserver 활성 섹션 추적** → 금색 보더+텍스트
- smooth-scroll, `margin-left: 260px` (데스크톱), 사이드바 배경 `#0c0c12`
- Responsive: 최대 콘텐츠 너비 1100px

### ⚑ TOC 앵커 링킹 강제 — 필수

목차 클릭 시 해당 섹션으로 즉시 이동해야 한다.

```html
<!-- 사이드바 항목 예시 -->
<a href="#section-2">§2 개념 해부 카드</a>
<a href="#concept-cl">청소율 (CL)</a>

<!-- 본문 섹션 예시 -->
<section id="section-2"> ... </section>
<div id="concept-cl"> ... </div>
```

**필수 CSS**: `html { scroll-behavior: smooth; }`
모든 사이드바 `<a href="#id">` 와 본문 `id="id"` 가 **1:1 정확히 일치**해야 한다.
누락된 id 또는 불일치 시 앵커 이동이 작동하지 않는다 — 모든 섹션에 id 부여 필수.

---

## §3 — Structural Isomorphism Map

구조적 동형성은 "피상적 인식"을 넘어, **다른 도메인의 지식으로 PK를 새롭게 예측하는
능력**으로 전이되어야 한다. 아래 네 레이어를 **반드시 이 순서대로** 모두 구현한다.

---

### ▶ [통찰의 서막 — 구조적 동형성의 Big Idea] ← Layer 1 SVG보다 먼저 렌더링

다이어그램을 그리기 전, **이 수학적 형태가 자연계와 약동학에서 왜 공통적으로
나타나는가**를 거장의 시각에서 명확히 설명한다.

세 파트로 구성:

1. **공통 원리**: 이 섹션의 핵심 수식이 여러 학문 도메인에서 동일하게 등장하는
   **근본적인 자연 원리 또는 물리 법칙**을 명시한다.

2. **왜 이 형태의 수식으로 표현되는가**: 이 공통 원리가 해당 ODE/방정식 형태로
   표현될 수밖에 없는 수학적·물리적 이유를 설명한다.

3. **다른 도메인 지식으로의 예측 전이**: 이 동형성을 이해하면 어떤 새로운 예측이
   가능해지는지 한 문장으로 선언한다.

스타일 메모: 금색 좌측 보더 + `rgba(201,168,76,0.05)` 배경. 고딕 italic 문체.

---

### [Layer 1] Hub-and-Spoke SVG 다이어그램 (HTML 내장 SVG)

*Vol I (R&T / Gabrielsson)*:
중심 허브 = 핵심 추상 수학 구조. 바깥 노드 최소 4개 도메인. 각 노드: 분야명 + 수식
+ 같은 구조인 이유 한 줄.

**공통 SVG 기술 명세:**

```
viewBox="0 0 800 600" 고정, width="100%" 반응형
중심 허브: cx=400, cy=300, r=60px
바깥 노드: x = 400 + 220·cos(θ_i), y = 300 + 220·sin(θ_i) (θ 등분)
텍스트 겹침: <foreignObject> + CSS word-wrap: break-word
연결선 레이블: 선 중간점 <text> 또는 <textPath>
노드 배경 fill="rgba(201,168,76,0.12)", 테두리 stroke="#c9a84c", 텍스트 fill="#ede8df"
```

---

### [Layer 2] Structural Alignment Matrix (구조 정렬 테이블)

세션 실제 파라미터와 구조로 채운다.

---

### [Layer 3] Normalization / Convergence Overlay (인터랙티브 JS 토글)

*Vol I*: 도메인별 실제 스케일 곡선 동시 표시 → "정규화" 토글 → 모든 곡선이 하나로
붕괴하는 순간 극적으로 시각화.

**⚑ V5.1 normCanvas 구현 규칙 (버그 ④ 수정 반영)**:

```javascript
// 초기화: 1회만 실행
let normW = 0, normH = 0;
const normCanvas = document.getElementById('normCanvas');
const normCtx = normCanvas.getContext('2d');

function initNormCanvas() {
  const dpr = window.devicePixelRatio || 1;
  const rect = normCanvas.getBoundingClientRect();
  normW = Math.floor(rect.width  * dpr);
  normH = Math.floor(rect.height * dpr);
  normCanvas.width  = normW;
  normCanvas.height = normH;
  normCtx.setTransform(1, 0, 0, 1, 0, 0); // identity 리셋
}

// resize 이벤트: initNormCanvas + drawNorm 순서
// ← simCanvas/chartObj 에는 절대 개입하지 않는다
window.addEventListener('resize', () => {
  initNormCanvas();
  drawNorm();
});

// drawNorm() 내부에서 normCanvas.width/height 재할당 금지
function drawNorm() {
  if (!normW || !normH) return;
  normCtx.clearRect(0, 0, normW, normH);
  // ... 그리기 로직 ...
}
```

---

### [Layer 4] Prediction Transfer Cards (예측 전이 카드, 최소 2개)

각 카드 — 클릭형 아코디언:
- **전이 질문**: 한 도메인 현상 → 다른 도메인 행동 예측
- **아코디언 답** 3단계: ① 출발 도메인 설명 → ② 공통 수학 구조 → ③ 대응 현상 도출

---

## §4 — Interactive Simulator

완전히 기능하는 JavaScript 시뮬레이션. **순수 JS (API 없음, CDN 라이브러리만,
완전 오프라인).**

---

### ⚑ V5.1 핵심 수정사항 — 그래프 팽창 버그 완전 해소

V5.0에서 발생한 "슬라이더 특정 구간에서 그래프 팔레트 무한 팽창" 버그를 해소하기
위해, §4 시뮬레이터 구현 시 아래 4가지 수정 규칙을 **반드시 모두** 적용한다.
하나라도 누락되면 버그가 재발한다.

#### 수정 규칙 1 — 이벤트 리스너 초기화 분리 (버그 ① 수정)

`updateChart()` 함수 내부에 `addEventListener`를 절대 넣지 않는다.
커서, mousemove, click 등 모든 이벤트 리스너는 초기화 단계에서 **단 한 번만** 등록한다.
현재 곡선 데이터는 `state._currentCurve`에 저장하고 리스너에서 참조한다.

```javascript
// ✅ 반드시 이 구조를 따를 것
// --- 전역 상수 (최상단 선언, 절대 재할당 금지) ---
const X_MAX     = 90;
const DT        = 0.5;
const HARD_Y_MAX = 10;
const LOG_Y_MIN  = 0.001;
const LOG_Y_MAX  = 100;

const state = {
  params: { vmax:107, km:0.56, vol:1450, dose:1800 },
  logScale: false,
  showAUC: true,
  referenceCurve: null,
  showPhantom: false,
  _currentCurve: null,  // ← 커서 리스너가 여기서 읽음
  warnings: {}
};

// --- 이벤트 리스너: 최초 1회, DOMContentLoaded 또는 스크립트 말미에 등록 ---
document.getElementById('simCanvas').addEventListener('mousemove', e => {
  if (!state._currentCurve) return;
  const canvas = document.getElementById('simCanvas');
  const rect = canvas.getBoundingClientRect();
  const t = (e.clientX - rect.left) / rect.width * X_MAX;
  const idx = Math.min(Math.floor(t / DT), state._currentCurve.ts.length - 2);
  const C = state._currentCurve.cs[Math.max(0, idx)] || 0;
  document.getElementById('cursorLabel').textContent =
    `t = ${t.toFixed(1)} min | C = ${C.toFixed(4)} µg/mL`;
});
```

#### 수정 규칙 2 — Y축 하드코딩 상수 고정 (버그 ② 수정)

`Y_MAX`를 절대 `C0 * 1.5` 등 동적 계산으로 구하지 않는다.
모듈 최상단에서 `HARD_Y_MAX`로 선언하고, `updateChart()` 에서는 이 상수만 참조한다.
C0가 HARD_Y_MAX를 넘을 경우 경고 배너만 표시한다.

```javascript
// ✅ scales.y.max 는 항상 상수
scales: {
  y: {
    type: state.logScale ? 'logarithmic' : 'linear',
    min:  state.logScale ? LOG_Y_MIN : 0,
    max:  state.logScale ? LOG_Y_MAX : HARD_Y_MAX,  // ← 상수. C0*1.5 절대 금지.
  }
}
```

#### 수정 규칙 3 — destroy/recreate 대신 data 교체 + update('none') (버그 ③ 수정)

Chart 인스턴스를 `initChart()`에서 단 한 번 생성한다.
`updateChart()` 에서는 `chartObj.data.datasets`을 교체하고 `chartObj.update('none')`만
호출한다. Log/Linear 스케일 전환 시에는 `chartObj.options.scales.y.*` 를 직접 수정 후
`chartObj.update('none')` 을 호출한다.

canvas 컨테이너에 아래 CSS를 반드시 적용하여 Chart.js의 크기 재측정이 DOM을
탈출하지 못하도록 막는다:

```css
/* ✅ V5.1 필수 CSS */
.canvas-wrap {
  position: relative;
  height: 320px;
  overflow: hidden;
  flex-shrink: 0;
}
#simCanvas {
  width: 100% !important;
  height: 100% !important;
  display: block;
  cursor: crosshair;
}
```

```javascript
// ✅ 초기화 함수 — 단 1회 호출
function initChart() {
  const canvas = document.getElementById('simCanvas');
  const ctx = canvas.getContext('2d');
  chartObj = new Chart(ctx, {
    type: 'line',
    data: { datasets: buildDatasets() },
    options: {
      animation: { duration: 200 },
      responsive: true,
      maintainAspectRatio: false,
      scales: {
        x: { type:'linear', min:0, max:X_MAX, /* ticks, grid ... */ },
        y: { type:'linear', min:0, max:HARD_Y_MAX, /* ticks, grid ... */ }
      },
      plugins: { /* legend, tooltip ... */ }
    }
  });
}

// ✅ 업데이트 함수 — destroy 금지, update('none') 만 호출
function updateChart() {
  // [Scientific Logic]: Michaelis-Menten 1구획 IV bolus 모델
  // dC/dt = -(Vmax*C)/(Km+C)/V  |  가정: 순간 혼합, 단일 구획, Vmax/Km 시간 불변
  // 위반 시 Phantom line으로 표시됨
  if (!chartObj) { initChart(); }

  const curve = computeMM(state.params);
  state._currentCurve = curve;          // ← 커서 리스너용 저장

  chartObj.data.datasets = buildDatasets(curve);

  // Log/Linear 전환
  chartObj.options.scales.y.type = state.logScale ? 'logarithmic' : 'linear';
  chartObj.options.scales.y.min  = state.logScale ? LOG_Y_MIN : 0;
  chartObj.options.scales.y.max  = state.logScale ? LOG_Y_MAX : HARD_Y_MAX;

  chartObj.update('none');              // ← destroy 금지, 'none' = 즉시 반영
  updateDerivedPanel(calcDerived(state.params));
  updateDeltas();
  checkWarnings(state.params);
}
```

#### 수정 규칙 4 — normCanvas 크기 재할당 격리 (버그 ④ 수정)

normCanvas의 `width`/`height` 속성 할당은 `initNormCanvas()`에서만 수행하고,
`drawNorm()` 내부에서는 `normCtx.clearRect()` 이후 그리기만 한다.
`window.resize` 핸들러에서 `initNormCanvas()` + `drawNorm()`을 순서대로 호출하되,
`chartObj`에는 절대 개입하지 않는다(Chart.js 자체 resize 핸들러가 처리함).

---

### [A] 시뮬레이션 목적 + 축 고정 범위 (Anti-Jitter 렌더링 — 절대 규칙)

#### ⚑ 핵심 렌더링 원칙

슬라이더를 조작할 때 **그래프의 배경(축 스케일, 격자선)은 절대 움직이지 않는다.**
오직 **데이터 곡선만** 슬라이더 값에 반응한다.

**V5.1 고정 축 범위 (하드코딩 상수):**

```javascript
const X_MAX     = 90;    // min — PK17 관측 시간
const HARD_Y_MAX = 10;   // µg/mL — PK17 슬라이더 최대 C0 범위 커버
const LOG_Y_MIN  = 0.001;
const LOG_Y_MAX  = 100;
const DT         = 0.5;  // Runge-Kutta step, min
```

> **학술적 무결성 선언 (Scientific Logic Declaration):**
> `buildDatasets()` 함수 최상단에 아래 주석을 반드시 포함한다:
> ```javascript
> // [Scientific Logic]: Michaelis-Menten 1구획 IV bolus 모델
> // dC/dt = -(Vmax * C) / (Km + C) * (1/V)
> // 적용 수식: Gabrielsson 5e Eq.2:270, AUC: Eq.2:271
> // 가정: 순간 혼합, 단일 포화 경로, Vmax/Km 시간 불변
> // 위반 시 Phantom line으로 표시됨 (2구획 순간 혼합 가정 위반 케이스)
> ```

---

### [B] 슬라이더 & 기본 기능

- 파라미터 슬라이더 최소 3개 (파라미터명, 기호, 단위, 현재값 레이블)
- 즉시 업데이트 — `input` 이벤트마다 `state.params[key] = value` → `updateChart()` 단일 호출
- **Log/Linear 토글** — `chartObj.options.scales.y.*` 직접 수정 후 `chartObj.update('none')`
- **AUC 면적 실시간 색칠** — fill dataset 교체, updateChart() 내 buildDatasets()에서 처리
- **t½ 마커선** — Chart.js annotation plugin 대신 canvas afterDraw hook으로 구현
  (annotation plugin 미로드 시 에러 방지):

```javascript
// ✅ afterDraw hook으로 마커선 구현 (annotation plugin 의존성 제거)
const MARKER_PLUGIN = {
  id: 'mmMarkers',
  afterDraw(chart) {
    const { ctx, scales: { x, y } } = chart;
    const d = state._currentCurve;
    if (!d) return;
    const { vmax, km, vol } = state.params;
    const C0 = state.params.dose / vol;
    // t½ at C0
    const t12 = Math.log(2) * vol / vmax * (km + C0);
    [t12, t12*2, t12*3].forEach((tv, i) => {
      if (tv > X_MAX) return;
      const xPx = x.getPixelForValue(tv);
      ctx.save();
      ctx.strokeStyle = `rgba(201,168,76,${0.5 - i*0.12})`;
      ctx.lineWidth = 1;
      ctx.setLineDash([4, 4]);
      ctx.beginPath();
      ctx.moveTo(xPx, chart.chartArea.top);
      ctx.lineTo(xPx, chart.chartArea.bottom);
      ctx.stroke();
      ctx.restore();
    });
    // MIC / TOX 수평선
    [{ v:0.8, c:'rgba(64,152,232,0.4)', l:'MIC' },
     { v:3.0, c:'rgba(192,57,43,0.4)',  l:'TOX' }].forEach(({v,c,l}) => {
      if (v > HARD_Y_MAX) return;
      const yPx = y.getPixelForValue(v);
      ctx.save();
      ctx.strokeStyle = c;
      ctx.lineWidth = 1;
      ctx.setLineDash([4,4]);
      ctx.beginPath();
      ctx.moveTo(chart.chartArea.left, yPx);
      ctx.lineTo(chart.chartArea.right, yPx);
      ctx.stroke();
      ctx.fillStyle = c;
      ctx.font = '9px IBM Plex Mono';
      ctx.fillText(l, chart.chartArea.right - 28, yPx - 3);
      ctx.restore();
    });
  }
};
Chart.register(MARKER_PLUGIN);
```

---

### [C] Delta Indicator

파라미터 변경 시:
- 형식: `AUC: 6.85  ↑ 43%`
- 증가 → `#e87040`, 감소 → `#4098e8`, ±1% 이내 → `var(--muted)`
- 이전 값을 `state._prevDerived`에 저장하고 `updateChart()` 호출 시마다 비교

---

### [D] Reference Curve Lock

- "기준선 저장" 버튼 → `state.referenceCurve = deepCopy(state._currentCurve)`
- `buildDatasets()`에서 `state.referenceCurve`가 있으면 회색 점선 dataset 추가
- `chartObj.update('none')` 으로 반영 — destroy 없음

---

### [E] Clinical Presets (리얼월드 기반 — 최소 4개)

소스 기반 실제 수치 사용. 슬라이더 범위(min/max)를 벗어나는 프리셋 값은
슬라이더 범위 내 값으로 clamp하되, state.params에는 실제 값을 저장한다:

```javascript
const PRESETS = {
  pk17:    { vmax:107,  km:0.56, vol:1450, dose:1800 }, // Gabrielsson PK17
  phenyt:  { vmax:167,  km:4.0,  vol:3000, dose:3500 }, // 페니토인 근사 (슬라이더 범위 내)
  alcohol: { vmax:167,  km:2.5,  vol:4200, dose:5000 }, // 에탄올 (Vm=10g/hr 근사)
  linear:  { vmax:300,  km:10.0, vol:1450, dose:1800 }  // 선형 비교 (Km>>C0)
};
// 툴팁에 근거 명시: title 속성 활용
```

---

### [E-2] Assumption Collapse Toggle (Phantom Overlay)

`state.showPhantom` 토글 시 `buildDatasets()`에서 미리 계산된 2구획 곡선 dataset
을 추가한다. Phantom 데이터 계산은 `computePhantom(params)` 함수에서 수행하며,
`updateChart()` 내에서 매번 재계산하는 대신 `state.showPhantom` 변경 시에만
계산하고 캐시한다:

```javascript
// Phantom 데이터 캐시
let phantomCache = null;
function getPhantom(params) {
  // params가 변경될 때마다 재계산 (파라미터 변경 감지)
  const key = JSON.stringify(params);
  if (!phantomCache || phantomCache.key !== key) {
    phantomCache = { key, data: computePhantom(params) };
  }
  return phantomCache.data;
}
```

```css
/* Phantom line 스타일 — buildDatasets()의 dataset에 적용 */
/* Chart.js에서는 borderColor + borderDash로 구현 */
borderColor: 'rgba(220,60,60,0.55)',
borderDash: [6, 4],
borderWidth: 2,
```

---

### [F] Time / Parameter Cursor

초기화 단계에서 단 한 번만 등록 (수정 규칙 1 참고):

```javascript
// ✅ updateChart() 밖에서 1회 등록
document.getElementById('simCanvas').addEventListener('mousemove', e => {
  if (!state._currentCurve) return;
  const canvas = document.getElementById('simCanvas');
  const rect = canvas.getBoundingClientRect();
  const t = Math.max(0, Math.min(X_MAX, (e.clientX - rect.left) / rect.width * X_MAX));
  const idx = Math.min(Math.floor(t / DT), state._currentCurve.ts.length - 2);
  const C = state._currentCurve.cs[Math.max(0, idx)] || 0;
  document.getElementById('cursorLabel').textContent =
    `t = ${t.toFixed(1)} min | C = ${C.toFixed(4)} µg/mL`;
});
```

---

### [G] Physiological / Statistical Boundary Warning

불가능한 파라미터 조합 시 경고 배너만 표시. Y축 범위는 변경하지 않는다.
슬라이더 배경색(danger) 변경은 CSS `background` inline style로만 처리한다:

```javascript
function checkWarnings(p) {
  const C0 = p.dose / p.vol;
  const warns = [];
  if (C0 < p.km * 0.1)    warns.push('C₀ ≪ Km: 선형 구간 — MM 비선형성 임상적으로 미미');
  if (p.vmax / p.km > 200) warns.push('Vmax/Km 비율 과다: 사실상 선형 PK');
  if (C0 > p.km * 20)      warns.push('C₀ ≫ Km: 거의 영차 소실');
  if (C0 > HARD_Y_MAX * 0.9) warns.push('C₀가 Y축 상한에 근접 — Log 스케일로 전환 권장');
  // 배너 표시/숨김
  const banner = document.getElementById('warnBanner');
  if (warns.length) { banner.textContent = warns.join(' | '); banner.classList.add('show'); }
  else banner.classList.remove('show');
  // 슬라이더 위험 표시 (CSS 인라인 스타일만)
  document.getElementById('sl-vmax').style.background = p.vmax < 30 ? 'rgba(192,57,43,0.4)' : '';
  document.getElementById('sl-km').style.background   = p.km < 0.15 ? 'rgba(192,57,43,0.4)' : '';
}
```

---

### [H] Target Mission Panel (필수)

시뮬레이터 아래 임상 미션 2개:

```
🎯 미션 1: 안전한 정주 항생제 농도 유지
목표: t=60min에서 C ≥ 0.8 µg/mL (MIC). Dose ≤ 3,000 µg 제약.
힌트: Km이 클수록 소실이 빠른가 느린가? AUC 공식에서 Km의 역할을 확인하라.

🎯 미션 2: 간경변 Vmax 30% 감소 시뮬레이션
목표: 기준선 저장 후 Vmax를 30% 낮춰 Delta Indicator로 AUC 변화를 확인하라.
힌트: AUC = (C0/2Vmax)(Km + C0/2) — Vmax가 분모에 있다.
```

---

### [I] 라이브러리 선택

| 시뮬레이션 유형 | 라이브러리 | CDN |
|---|---|---|
| MM 1구획 PK | Chart.js | `https://cdn.jsdelivr.net/npm/chart.js` |
| normCanvas | Vanilla JS 2D Canvas | (내장) |

annotation plugin은 사용하지 않는다. 마커선은 afterDraw 커스텀 플러그인으로
구현한다 (수정 규칙 3 §B 참고).

---

### [J] JavaScript 상태 관리 아키텍처 (V5.1 수정 버전 — 구조 변경 금지)

```javascript
// ── 전역 상수 (최상단, 절대 재할당 금지) ──
const X_MAX      = 90;
const DT         = 0.5;
const HARD_Y_MAX = 10;
const LOG_Y_MIN  = 0.001;
const LOG_Y_MAX  = 100;

// ── 중앙 상태 ──
const state = {
  params: { vmax:107, km:0.56, vol:1450, dose:1800 },
  logScale:       false,
  showAUC:        true,
  showPhantom:    false,
  referenceCurve: null,
  _currentCurve:  null,   // ← 커서 리스너 전용, updateChart()가 갱신
  _prevDerived:   null,   // ← Delta Indicator용
  warnings:       {}
};

// ── buildDatasets(): [Scientific Logic] 선언 포함 ──
function buildDatasets(curve) {
  // [Scientific Logic]: Michaelis-Menten 1구획 IV bolus 모델
  // dC/dt = -(Vmax * C) / (Km + C) * (1/V)
  // 적용 수식: Gabrielsson 5e Eq.2:270, AUC: Eq.2:271
  // 가정: 순간 혼합, 단일 포화 경로, Vmax/Km 시간 불변
  // 위반 시 Phantom line으로 표시됨
  const datasets = [];
  if (state.showAUC) { /* AUC fill dataset */ }
  /* MM 메인 곡선 dataset */
  if (state.referenceCurve) { /* 기준선 dataset */ }
  if (state.showPhantom) { /* Phantom dataset */ }
  return datasets;
}

// ── updateChart(): destroy 금지, update('none') 만 ──
let chartObj = null;
function updateChart() {
  const curve = computeMM(state.params);
  state._currentCurve = curve;          // ← 반드시 저장

  if (!chartObj) {
    initChart();                         // ← 최초 1회만 new Chart()
    return;
  }

  // 데이터 교체
  chartObj.data.datasets = buildDatasets(curve);

  // 스케일 타입 전환 (log/linear)
  const yScale = chartObj.options.scales.y;
  yScale.type = state.logScale ? 'logarithmic' : 'linear';
  yScale.min  = state.logScale ? LOG_Y_MIN : 0;
  yScale.max  = state.logScale ? LOG_Y_MAX : HARD_Y_MAX;

  chartObj.update('none');              // ← canvas 크기 재측정 없음

  updateDerivedPanel(calcDerived(state.params));
  updateDeltas(calcDerived(state.params));
  checkWarnings(state.params);
}

// ── 이벤트 리스너: updateChart() 밖, 단 1회 등록 ──
// (모든 슬라이더, 토글 버튼, mousemove — 전부 여기서)
// sliderEl.addEventListener('input', e => {
//   state.params.vmax = parseFloat(e.target.value);
//   updateLabels();
//   updateChart();
// });
```

---

## §6 — Pragmatic Application Scenarios

### Scenario 1: 신약개발 컨텍스트

이 세션 개념이 적용되는 현실적 Phase 1 또는 Phase 2 시나리오:
- 허구이나 현실적인 약물 후보 + Dynamic Source Anchoring에서 추출한 실제 수치 활용
- 연구 설계 질문 → 실제 계산 → 규제 언어(NDA/IND/CSR)로 표현

### Scenario 2: 임상·TDM 컨텍스트

Vol I: TDM·용량 조정 + 계산 + 생리학적 메커니즘 연결

### Code Block (필수 — 작동하는 코드)

NONMEM `$PROB ~ $ESTIMATION` 완전 블록 또는 R nlmixr2 완전 모델 명세.

### Diagnostic Pathology (진단 병리학 — 필수, 최소 2개 진단 시그니처)

각 시그니처: 이름 + GOF 플롯 패턴 + 기계론적 원인 + 해결 방향.
η-shrinkage / ε-shrinkage 해석 포함.

---

## ABSOLUTE OUTPUT CONSTRAINTS

1. **단일 HTML 파일** — self-contained. CDN 최초 로드 후 오프라인 완전 작동.
2. **MathJax** — 정확한 설정 포함. `$`·`$$` 렌더링 후 절대 노출 금지.
3. **고정 사이드바 TOC** — IntersectionObserver 활성 섹션 추적. 1:1 앵커 매핑 필수.
4. **§2 Big Idea 블록** — Step 1 생성 내용 그대로. 금색 강조 박스. 생략 금지.
5. **§2 Apex Concept** — [⚡ Apex Concept] 배지 + C-2 Plausible Fallacy 블록.
6. **§2 Micro-citation 태그** — 핵심 수식에 한하여 `[출처: ...]` 인라인 태그.
7. **§3 네 레이어 전부 필수** — 서막 → SVG → 정렬 테이블 → 정규화 오버레이 → 전이 카드.
8. **§4 Simulator V5.1 4가지 수정 규칙 전부 적용 필수**:
   - 수정 규칙 1: 이벤트 리스너 초기화 분리 (updateChart() 내부 addEventListener 금지)
   - 수정 규칙 2: HARD_Y_MAX 상수 사용 (C0*1.5 동적 계산 금지)
   - 수정 규칙 3: initChart() 1회 생성 + update('none') 패턴 (destroy/recreate 금지)
   - 수정 규칙 4: initNormCanvas() 분리 (drawNorm() 내부 canvas 크기 재할당 금지)
9. **§5 Critical Blow 행** — 붉은 배경. **기억 고리 행** — 금색 텍스트.
10. **§7 보스 딜레마** — 아코디언 형태 + Trade-off 논리.
11. **§6 Diagnostic Pathology** — 최소 2개 시그니처.
12. **§8C Professional Moat** — 이 세션 내용에 직접 특정. 동기 부여 문장 금지.
13. **Source Data Anchoring** — 실제 수치를 §4 기본값, §6 시나리오에 일관 사용.
14. **No Lazy Integration** — Step 1 산출물 100% HTML 태그 안에 복원.
15. **토큰 절단 방지** — 한계 초과 가능성 시 완전히 닫힌 유효 HTML까지만 생성 후:
    `<!-- ✂ 여기까지 생성 완료. §[다음 섹션번호]부터 계속하려면 "계속"을 입력하세요. -->`

---

*V5.1 Apex Edition — Step 2*
*V5.0 대비 변경사항: §4 시뮬레이터 그래프 팽창 버그 4종 수정*
*(버그①: mousemove 리스너 누적 → 초기화 분리 / 버그②: Y_MAX 동적 계산 → HARD_Y_MAX 상수*
*/ 버그③: destroy/recreate → initChart+update('none') / 버그④: normCanvas 크기 재할당 → initNormCanvas 분리)*

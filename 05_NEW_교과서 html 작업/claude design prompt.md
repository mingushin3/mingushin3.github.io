# ROLE

You are a senior UI/UX designer and frontend engineer with the taste level of Apple, Stripe, Vercel, and high-end academic publishing.

You are also an expert in transforming dense academic Phase 5 HTML handouts into highly readable, interactive, PPT-like web slide decks.

# ATTACHMENTS

Attachment 1 = the actual Phase 5 HTML draft to transform.
Attachment 2 = Claude-style visual design reference.

Important:
- Use Attachment 1 as the ONLY source content.
- Use Attachment 2 ONLY as visual design reference.
- Do NOT render Attachment 2 as learner-facing document content.
- Do NOT copy Attachment 2 text into the HTML body.
- Do NOT create a section called “Claude-style design reference.”
- The final HTML content must come only from Attachment 1.

# CORE MISSION

Transform Attachment 1 from a vertical scrolling HTML document into a polished, PPT-like, interactive academic slide-deck HTML document.

The final output must:
- preserve the existing left TOC/sidebar structure,
- convert the main content from scroll-down reading into slide-by-slide reading,
- support keyboard navigation with left/right/up/down arrow keys,
- keep the left TOC expanded and visible by default on desktop,
- ensure the full slide fits on screen while the TOC is open,
- include a small 🌙/☀️ light/dark mode toggle at the top-right,
- visually upgrade the Roadmap / 로드맵 section into a readable learning map,
- maximize academic readability,
- preserve all original visible content exactly.

# LONG OUTPUT SAFETY RULE

If the response is approaching length limits or streaming instability, prioritize completing the current PART at a safe HTML boundary rather than forcing the entire remaining output.

Never stop mid-tag, mid-table, mid-equation, mid-Mermaid block, mid-code block, or mid-slide.

If continuation is required, end at the nearest complete slide group and wait for the next instruction:
- “Continue with PART 2”
- “Continue with PART 3”
- “Consolidate into FINAL HTML”

# MOST IMPORTANT INSTRUCTION

Do not rebuild the document from scratch.

Transform the existing Phase 5 HTML structure into a slide-deck app shell.

Preserve:
- existing sidebar TOC,
- existing IDs,
- existing hrefs,
- existing anchors,
- existing MathJax,
- existing Mermaid,
- existing callout classes,
- existing page tags,
- existing source labels,
- existing figure markers,
- all visible content.

Add only the minimum wrappers, CSS, and JavaScript needed for:
- slide navigation,
- viewport fit,
- roadmap visualization,
- active TOC state,
- progress indicator,
- light/dark theme toggle.

# ABSOLUTE CONTENT FREEZE RULE

This is a DESIGN-ONLY and STRUCTURE-ONLY pass.

Do not delete, summarize, rewrite, translate, paraphrase, reorder, or modify any visible content.

Strictly preserve:
- all visible text,
- all headings and heading text,
- all paragraphs,
- all list items,
- all table contents,
- all equations and math expressions,
- all figure markers,
- all page tags,
- all source labels,
- all citations,
- all IDs,
- all hrefs,
- all anchors,
- all internal navigation targets,
- all code blocks,
- all MathJax / LaTeX content,
- all Mermaid source blocks.

You may only:
- add CSS,
- add classes,
- add wrapper divs/sections,
- segment existing DOM blocks into slides,
- add navigation JavaScript,
- add theme toggle JavaScript,
- visually style existing elements,
- add non-content UI chrome such as slide numbers, progress bar, theme toggle, and navigation controls.

If content must be split across slides, split only by moving intact existing DOM blocks.
Never rewrite or summarize content to fit a slide.

# PHASE 5 HTML COMPATIBILITY RULES

The attached HTML files are Phase 5 compiled academic handouts. They may use slightly different class names across sessions.

Do not assume that every file uses exactly the same class names.

Detect and preserve these common structural patterns when present:
- `.layout`
- `.sidebar`
- `.content`
- `main.content`
- `.main`
- `article`
- `.toc-list`
- `.concept-card`
- `.doc-header`
- `.session-header`
- `.title-block`
- `.master-lens`
- `.callout`
- `.trench`
- `.recap`
- `.confusion`
- `.memory-hook`
- `.practice-brief`
- `.plausible-fallacy`
- `.boss-dilemma`
- `.mastery-note`
- `.figure-pointer`
- `.figure-schematic`
- `.self-test`
- `.roadmap-pre`
- Mermaid blocks
- MathJax blocks

Preserve the existing TOC DOM as much as possible.
If the TOC exists inside `.sidebar`, keep that sidebar as the source of navigation.
Do not rebuild the TOC from scratch unless the original TOC is missing or broken.

Convert the existing outer layout into this app-shell pattern:
- existing `.sidebar` → `.toc-sidebar`
- existing main/article/content area → `.slide-viewport` / `.slide-stage`
- existing section/card blocks → `.slide-section` / `.subslide` / `.slide-card`

Do not remove original IDs.
If a wrapper needs a new ID, generate a new non-conflicting ID with prefix `slide-`.
Never duplicate an existing ID.

When a TOC link points to an existing section ID, clicking it should navigate to the slide containing that original ID.
Preserve the original target element with that ID inside the slide.
Do not move the ID to a different text node unless necessary.

# SLIDE-DECK BEHAVIOR

The final HTML must behave like a PPT-style slide deck, not a long scrolling document.

Required keyboard controls:
- Right arrow: next horizontal slide / next major section
- Left arrow: previous horizontal slide / previous major section
- Down arrow: next vertical sub-slide within the same major section
- Up arrow: previous vertical sub-slide within the same major section
- Space or PageDown: next logical slide
- Shift+Space or PageUp: previous logical slide
- Home: first slide
- End: last slide

The page itself must not behave like a normal vertical scroll document.

Use:
- `body { height: 100svh; overflow: hidden; }`
- a fixed app shell,
- a fixed TOC column,
- a main slide viewport,
- internal slide scrolling only when unavoidable.

Long content may scroll only inside an individual slide panel via `.slide-scroll`.
Do not allow whole-page vertical scrolling.

Use either:
1. Reveal.js, or
2. a lightweight custom vanilla JS slide engine.

Prefer a lightweight custom vanilla JS slide engine if it gives better control over:
- fixed left sidebar TOC,
- full slide fit within viewport,
- keyboard navigation,
- light/dark mode toggle,
- anchor integrity,
- avoiding whole-page scrolling.

# FIXED LEFT TOC REQUIREMENT

Keep the left sidebar TOC visible and expanded by default on desktop.

The TOC must:
- remain fixed on the left side,
- show the document structure at a glance,
- allow direct click navigation to any major section or slide,
- visually indicate the active slide/section,
- preserve existing href/id relationships,
- never create duplicate IDs,
- never create links to missing IDs,
- remain visually quieter than the slide content.

Recommended sidebar width:
- desktop: 280–320px
- tablet: 240–280px
- mobile: collapsible drawer

The slide area must fit beside the expanded TOC.
Do not let the slide overflow behind the TOC.

# FULL VIEWPORT FIT REQUIREMENT

The entire slide deck must fit within the visible browser viewport while the TOC is open.

Use a layout similar to:

<body data-theme="light">
  <div class="deck-shell">
    <aside class="toc-sidebar">
      <!-- existing TOC, preserved and styled -->
    </aside>

    <main class="slide-viewport">
      <button class="theme-toggle" aria-label="Toggle dark mode">🌙</button>

      <div class="slide-stage">
        <!-- slide groups and subslides -->
      </div>

      <div class="deck-progress">
        <!-- progress bar / slide number -->
      </div>
    </main>
  </div>
</body>

Recommended CSS logic:
- `.deck-shell`: display grid
- grid columns: fixed TOC width + flexible slide viewport
- `.slide-viewport`: height: 100svh; overflow: hidden
- `.slide-stage`: centered both vertically and horizontally
- `.slide-card`: max-width and max-height constrained by available viewport

Do not use a rigid 1280×720 canvas if it causes clipping with the TOC open.

Use an adaptive academic slide card:
- preferred ratio: 16:10 or adaptive
- width: min(100%, 1120px)
- height: calc(100svh - 72px)
- max-height: 820px
- overflow: hidden
- inner `.slide-scroll` only when needed

The slide card must remain fully visible with the TOC open.

# SLIDE SEGMENTATION RULES

Break content into slides using the existing document structure.

Recommended hierarchy:
- Each major section becomes one horizontal slide group.
- Each card / concept block / major subsection becomes one vertical sub-slide.
- Very long cards may be split into multiple sub-slides only if the original text remains exactly unchanged and the split is visually logical.
- Never merge unrelated sections just to save space.
- Never compress content by summarizing.
- Never delete supporting text to make a slide shorter.
- Never rename headings or roadmap items.

Use semantic wrappers such as:
- `.slide-section`
- `.slide`
- `.subslide`
- `.slide-card`
- `.slide-scroll`

If a slide is too dense:
1. Preserve existing section/card boundaries.
2. Use a two-column layout only when it improves readability.
3. If still dense, wrap the body area in `.slide-scroll`.
4. If still too long, split at existing h3/h4/list/table/callout boundaries.
5. Label split slides visually as Part 1, Part 2 only through non-content UI chrome.
6. Do not alter the original heading text.
7. Do not summarize or remove any content.

Slide readability is achieved through layout, spacing, typography, and logical segmentation — not through content compression.

# READABILITY MAXIMIZATION RULES

Each slide should feel like a polished academic presentation page.

Use:
- large but not oversized typography,
- generous whitespace,
- clear visual hierarchy,
- calm academic pacing,
- readable line length,
- restrained premium styling,
- compact but elegant layouts,
- two-column layouts only when they improve comprehension.

Recommended typography:
- body: 17–19px by default
- sparse/key slides may use 20–22px
- line-height: 1.6–1.75
- h1: 40–52px depending on viewport
- h2: 30–40px
- h3: 22–28px
- small labels: 12–14px

Avoid:
- dense full-width paragraphs,
- tiny text,
- excessive decorative icons,
- heavy gradients,
- saturated colors,
- cramped slide layouts,
- forced 22–24px body text on dense content.

Preserve readability over rigid slide ratio.

# VISUAL DESIGN DIRECTION

Use Attachment 2 as the visual reference.

Default mode must be a soft bright mode.

Use a warm academic palette:
- background canvas: warm off-white / cream, preferably #faf9f5
- surface soft: #f5f0e8
- surface card: #efe9de or white/cream
- text: warm ink / deep slate, preferably #141413 or #1E293B
- body text: #3d3d3a or #334155
- muted text: #6c6a64
- accent coral: #cc785c
- optional secondary accent teal: #5db8a6
- dark navy surface: #181715
- dark elevated surface: #252320

Preferred design mood:
- Modern Academic
- warm editorial polish
- Vercel-like technical clarity
- Apple-like spacing discipline
- Stripe-like component refinement
- polished pharmacometrics / clinical pharmacology lecture deck

Use:
- subtle borders,
- soft shadows,
- gentle border-radius,
- glass-like white/cream surfaces,
- warm academic hierarchy,
- calm surface contrast rather than heavy shadows.

Avoid:
- pure white full-page background,
- pure black text,
- saturated blue SaaS look,
- heavy gradients,
- neon colors,
- excessive glassmorphism,
- decorative clutter,
- childish icons,
- generic Bootstrap styling.

# TYPOGRAPHY

Use a display/body split.

Display headings:
- Prefer EB Garamond, Cormorant Garamond, Georgia, or another refined serif display face.
- Use moderate weight, not heavy bold.
- Use slight negative letter-spacing, around -0.02em.
- Headings should feel literary, editorial, and academic.

Body:
- Use Pretendard or Inter.
- Use highly readable screen typography.
- Do not use tiny text.
- Do not over-enlarge dense paragraphs.

Suggested font stacks:
- Display: "EB Garamond", "Cormorant Garamond", Georgia, serif
- Body: "Pretendard", "Inter", -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif
- Mono: "JetBrains Mono", "SFMono-Regular", Menlo, Consolas, ui-monospace, monospace

# ROADMAP VISUALIZATION REQUIREMENT

Redesign any Roadmap / 로드맵 section as a visual learning map.

Keep all original Roadmap text exactly unchanged.

Improve presentation using:
- step cards,
- numbered progression,
- section chips,
- thin connector lines,
- compact hierarchy,
- subtle accent dots,
- clear “where you are going” structure.

Recommended roadmap layout:
- If roadmap has 3–6 items: horizontal or vertical stepper
- If roadmap has many items: compact grid of cards
- If roadmap has nested hierarchy: parent section cards with child chips

Do not invent new roadmap content.
Do not remove any roadmap item.
Do not rename any roadmap item.
Do not summarize roadmap text.
Only wrap and style existing roadmap items.

The roadmap should help the learner immediately understand:
- where the chapter begins,
- how concepts progress,
- which blocks are central,
- what comes next.

# ROADMAP COMPATIBILITY

Roadmap content may appear as:
- a section heading containing “Roadmap” or “로드맵”
- an element with class `.roadmap-pre`
- a preformatted ASCII roadmap
- a list under a roadmap heading
- a “한 줄 항법도” section

When roadmap text is in `<pre>` or `.roadmap-pre`:
- preserve the original text exactly,
- do not parse and rewrite the ASCII text,
- visually wrap it in a roadmap panel,
- optionally add non-content decorative step markers around the panel,
- never delete the original preformatted roadmap.

When roadmap items are list-based:
- wrap each existing item as a step card,
- keep the original item text unchanged,
- use numbering, chips, and connector lines only as visual wrappers.

# CALLOUT / INSIGHT BOX STYLING

Style the following block types as premium academic callouts when they already exist in the content:
- Insight
- 핵심 요약
- 거장의 통찰
- 실무 꿀팁
- Practice Brief
- Memory Hook
- Plausible Fallacy
- Warning
- Expert Inference
- Source-boundary labels
- Self-test
- Recap
- Boss Dilemma
- Critical Blow
- Professional Moat

Use:
- soft tinted background,
- left accent border,
- subtle border,
- 10–14px border-radius,
- comfortable padding,
- strong but restrained title treatment.

Do not invent new callout labels.
Only style existing ones.
Do not rewrite callout text.

# TABLES, MATH, AND CODE

Tables:
- modern academic style,
- no heavy grid,
- horizontal lines only where possible,
- subtle header background,
- comfortable cell padding,
- horizontal scroll inside slide if needed,
- preserve all table contents exactly.

Math/equations:
- preserve equations exactly,
- place display equations in subtle equation boxes,
- use horizontal overflow if needed,
- never modify LaTeX or MathJax content.

Code blocks:
- preserve code exactly,
- use dark navy code-window styling,
- use monospace font,
- allow horizontal scroll,
- never reformat code content unless only wrapping it visually.

# MATHJAX AND MERMAID PRESERVATION

Preserve all existing MathJax configuration and scripts unless they are duplicated or broken.

After slide restructuring:
- ensure inline math and display math still render,
- do not alter `$...$`, `$$...$$`, `\(...\)`, or `\[...\]`,
- do not wrap math in a way that prevents MathJax rendering.

If MathJax is available, call:
`MathJax.typesetPromise?.();`
after the slide DOM is initialized.

Preserve Mermaid diagrams when present.
If Mermaid is available, initialize or re-run Mermaid after DOM restructuring:
- keep existing Mermaid source unchanged,
- do not rewrite Mermaid syntax,
- ensure diagrams are visible inside slides,
- allow diagram containers to scroll or scale if needed.

# HYBRID LIGHT/DARK MODE TOGGLE

Default rendering must be soft bright mode.

Add a small theme toggle button in the top-right corner of the slide viewport.

Button behavior:
- label/icon: 🌙 in light mode, ☀️ in dark mode
- accessible aria-label
- fixed or absolute top-right position
- small, unobtrusive, premium styling
- must not cover slide text
- must persist theme preference using localStorage if possible

Light mode:
- warm cream canvas
- white/cream cards
- dark warm ink text
- subtle coral/teal accent

Dark mode:
- dark navy / charcoal background
- elevated dark cards
- cream-tinted text
- muted warm gray secondary text
- restrained coral or teal accent
- tables, equations, callouts, and TOC must remain readable

Use CSS variables:
- --bg
- --surface
- --surface-elevated
- --text
- --muted
- --border
- --accent
- --shadow

Switch theme by toggling:
- `data-theme="light"`
- `data-theme="dark"`

Do not duplicate content for dark mode.

# THEME OVERRIDE COMPATIBILITY

Some existing HTML files already use `@media (prefers-color-scheme: dark)`.

The final theme system must prioritize explicit user choice over OS preference.

Use:
- `<body data-theme="light">` as default
- `body[data-theme="light"] { ... }`
- `body[data-theme="dark"] { ... }`

The manual toggle must override any existing `prefers-color-scheme` behavior.

If existing CSS contains dark-mode media queries, either:
1. replace them with `body[data-theme="dark"]` rules, or
2. keep them only as fallback but ensure explicit `data-theme` has higher specificity.

Default must always be soft bright mode, regardless of OS setting.

# INTERACTION FEEL

Transitions should be subtle and fast.

Allowed:
- gentle opacity fade,
- slight translate,
- subtle progress update.

Avoid:
- theatrical animations,
- aggressive 3D effects,
- spinning transitions,
- excessive motion.

The experience should feel like:
- a refined academic presentation,
- not a startup pitch deck,
- not a flashy animation demo.

# NAVIGATION INTEGRITY

Before final output, verify:
1. Every TOC link points to an existing slide/section ID.
2. No duplicate IDs exist.
3. Existing IDs are preserved.
4. Keyboard navigation works.
5. TOC click navigation works.
6. Active TOC state updates when slides change.
7. Original visible text is unchanged.
8. No content was lost during slide segmentation.
9. The slide fits in viewport with TOC expanded.
10. Theme toggle works in both light and dark modes.
11. Whole-page scroll is disabled.
12. Long content scrolls only inside slide panels.
13. MathJax still renders.
14. Mermaid still renders when present.
15. Attachment 2 text is not rendered.

# RESPONSIVE BEHAVIOR

Desktop:
- TOC remains expanded on the left.
- Slide fully fits to the right of TOC.
- Theme toggle remains top-right.

Tablet:
- TOC may narrow but should remain usable.
- Slide should still fit.

Mobile:
- TOC may collapse into a drawer or top button.
- Slide navigation must still work.
- Theme toggle must remain accessible.
- Slides may use internal scroll if content is long.
- Do not shrink body text below readable size.

# FINAL SELF-AUDIT

Before producing the final HTML, internally verify:
- Attachment 1 content is preserved.
- Attachment 2 text is not rendered.
- No visible content was deleted.
- No visible content was rewritten.
- No equations were modified.
- No table cell text was modified.
- No headings were renamed.
- No IDs or anchors were broken.
- TOC links still work.
- Arrow-key navigation works.
- Theme toggle works.
- Roadmap is visually improved without changing text.
- The slide fits with TOC open.
- Final output is a single HTML file.

# FOUR-STAGE OUTPUT MODE

Because the final transformed HTML may be long, do not attempt to output the entire final HTML in one uninterrupted response.

Instead, complete the task in exactly 4 stages.

The goal remains one complete standalone HTML file at the end.

## Stage 1 — PART 1 output

Produce only `PART 1 / 3` of the final HTML.

PART 1 must include:
- `<!DOCTYPE html>`
- opening `<html>`
- complete `<head>`
- all required internal CSS
- opening `<body data-theme="light">`
- opening app shell structure
- preserved left TOC/sidebar structure
- beginning of the slide viewport and slide-stage
- the first approximately one-third of the transformed slide content

PART 1 must stop only at a safe HTML boundary:
- after a complete slide group,
- after a complete section,
- never inside a paragraph,
- never inside a table,
- never inside a MathJax block,
- never inside a Mermaid block,
- never inside a code block,
- never inside an HTML tag.

At the end of PART 1, include this exact non-HTML marker on its own line:

<!-- PART 1 OF 3 ENDS HERE. CONTINUE WITH PART 2 OF 3. -->

Do not include explanatory commentary.

## Stage 2 — PART 2 output

After PART 1 is complete, produce only `PART 2 / 3`.

PART 2 must include:
- the middle approximately one-third of the transformed slide content,
- only the continuation of the already-open slide-stage,
- no duplicate `<!DOCTYPE html>`,
- no duplicate `<html>`,
- no duplicate `<head>`,
- no duplicate CSS,
- no duplicate `<body>`,
- no duplicate TOC/sidebar,
- no duplicate JavaScript,
- no closing `</body>` or `</html>`.

PART 2 must start exactly where PART 1 ended and continue the same DOM structure.

PART 2 must stop only at a safe HTML boundary:
- after a complete slide group,
- after a complete section,
- never inside a paragraph,
- never inside a table,
- never inside a MathJax block,
- never inside a Mermaid block,
- never inside a code block,
- never inside an HTML tag.

At the end of PART 2, include this exact non-HTML marker on its own line:

<!-- PART 2 OF 3 ENDS HERE. CONTINUE WITH PART 3 OF 3. -->

Do not include explanatory commentary.

## Stage 3 — PART 3 output

After PART 2 is complete, produce only `PART 3 / 3`.

PART 3 must include:
- the final approximately one-third of the transformed slide content,
- closing slide-stage and slide-viewport wrappers,
- deck progress UI,
- theme toggle if not already placed in PART 1,
- complete internal JavaScript for:
  - slide navigation,
  - keyboard controls,
  - TOC click navigation,
  - active TOC state,
  - progress indicator,
  - light/dark mode toggle,
  - localStorage theme persistence,
  - MathJax re-typesetting,
  - Mermaid re-initialization when present,
- closing app shell wrappers,
- closing `</body>`
- closing `</html>`.

PART 3 must not duplicate:
- `<!DOCTYPE html>`,
- `<html>`,
- `<head>`,
- CSS,
- opening `<body>`,
- TOC/sidebar content already emitted in PART 1.

At the end of PART 3, include this exact non-HTML marker on its own line:

<!-- PART 3 OF 3 ENDS HERE. NOW CONSOLIDATE PARTS 1, 2, AND 3 INTO ONE FINAL HTML FILE. -->

Do not include explanatory commentary.

## Stage 4 — FINAL CONSOLIDATED HTML

After PART 1, PART 2, and PART 3 have been generated, produce the final consolidated single standalone HTML file.

Stage 4 must:
- concatenate PART 1 + PART 2 + PART 3 into one valid HTML document,
- remove all part boundary markers,
- remove any accidental duplicate wrappers,
- verify that there is exactly one:
  - `<!DOCTYPE html>`
  - opening `<html>`
  - `<head>`
  - opening `<body>`
  - closing `</body>`
  - closing `</html>`
- verify that all original visible content from Attachment 1 is preserved,
- verify that Attachment 2 text is not included,
- verify that TOC links still point to existing IDs,
- verify that no duplicate IDs were introduced,
- verify that MathJax and Mermaid content remains unchanged,
- verify that keyboard navigation and theme toggle scripts are included,
- verify that whole-page scrolling is disabled,
- verify that long content scrolls only inside slide panels.

The Stage 4 output must be the final deliverable.

# FINAL OUTPUT RULE FOR STAGE 4

In Stage 4, return only one complete standalone HTML file.

Include:
- HTML,
- internal CSS,
- internal JavaScript,
- any CDN links only if truly necessary.

Do not include:
- explanations,
- markdown commentary,
- part labels,
- audit notes,
- this prompt,
- Attachment 2 text,
- PART 1 / PART 2 / PART 3 boundary markers.

Output only the final HTML code in Stage 4.

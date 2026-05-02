=== SCOPE LOCK ===

Source       : Gabrielsson & Weiner, Pharmacokinetic and Pharmacodynamic
               Data Analysis, 5th ed. (Swedish Pharmaceutical Press)

Chapter      : Ch. 2 §2.6.7 (Feedback) +
               Ch. 3 §3.7 (Turnover Models – Reversible) +
               Ch. 3 §3.8 (Turnover Models – Irreversible) +
               Ch. 3 §3.10 (Dose-Response-Time Models) +
               Ch. 3 §3.12 (Baseline Models) +
               PD4 / PD5 / PD6 / PD7 / PD9 Case Studies

Pages        : pp. 110–111 · 235–260 · 272–275 · 317–319 · 742–784

Chapter role : ① Conceptual spine of PK/PD delay modeling:
                  establishes why indirect (turnover-driven) models
                  outperform effect-compartment (link) models when
                  the response variable has its own biological turnover.
               ② Provides the four canonical model structures
                  (Models 1–4: inhibit/stimulate × kin/kout) that
                  underpin the majority of published PopPK/PD papers
                  in immunology, hematology, endocrinology, and
                  anti-infective pharmacology.
               ③ Bridges conceptual math (ODEs, limiting solutions,
                  Rss, ΔR, initial-slope rules) to full worked case
                  studies (warfarin-PCA, furosemide, EPO-analog,
                  CB1 agonist, Zooparc®) with graphical parameter
                  estimation — the exact workflow used in NONMEM /
                  nlmixr2 model development.
               ④ Prerequisites satisfied before this chunk:
                  one-compartment PK, Emax/Imax direct-effect models,
                  first-order ODE steady-state reasoning.
               ⑤ Unlocks after this chunk:
                  transit-compartment models, moderator/tolerance
                  models (§3.9), PopPK/PD with IIV on kout & IC50,
                  disease-progression baseline drift modeling.

Learner      : PhD pharmacometrics student (entry–intermediate);
               licensed clinical pharmacist background (~10 yr);
               primary tools: NONMEM, nlmixr2, mrgsolve;
               vault: Obsidian PIPET-Vault (iCloud-synced);
               learning mode: JIT, deep mechanistic understanding
               preferred over encyclopedic coverage.

Final output : Single self-contained HTML (Step 2 flashcard/
               reference page); Obsidian-compatible YAML
               frontmatter block also required.

Mode         : A-Critical
               Rationale: This is the single most tested conceptual
               domain in PopPK/PD manuscripts and FDA reviewer
               questions. Every equation, limiting value, and
               steady-state relationship must be verified precisely.
               Graphical parameter estimation rules (slope → kout,
               intercept → R0, peak-shift → mechanism discrimination)
               are high-yield for both NONMEM coding and manuscript
               critical review.

Image rights : None
               All figures (3.33–3.50, 4.1–4.8, 5.1–5.3, 6.1,
               7.1–7.3, 9.1–9.5) are copyrighted textbook material.
               Reproduce only as original schematic redraws or
               equation-driven mrgsolve/R simulations; never embed
               or screenshot source figures directly.

===============================================
HARD RULES (apply to all phases):

* Do not expand beyond the page ranges listed above.
* Do not fabricate parameter values, experimental conditions,
  drug names, or equation numbers absent from the source PDF.
* [확인 필요] = flag and retain; never silently delete
  unverifiable content.
* Do not reproduce copyrighted figures (Image rights = None).
  Permitted alternatives: (a) pure equation blocks,
  (b) original ASCII/SVG schematics, (c) mrgsolve R code
  that regenerates the conceptual curve shape.
* Model equations must be typeset in LaTeX MathJax syntax
  inside the HTML output; never use plain-text approximations
  for differential equations.
* All four Models (1–4) must appear side-by-side in a
  comparison table with: ODE form · drug action site ·
  tss governor · Rss formula · ΔR formula · limit of R ·
  return-to-baseline behavior · canonical clinical example.
* PD case study parameter tables (Tables 4.1, 5.1, 6.1, 7.1,
  9.1) may be reproduced as data tables (not figures);
  cite page number in caption.
* Irreversible models (§3.8): clearly distinguish second-order
  kill constant K from first-order kout; flag confusion risk
  with [확인 필요] if notation is ambiguous in context.
* §3.10 및 §3.12는 제공 PDF 내 가시 범위(p.272–275, 317–319)에 한정하여
  서술하고, 절단된 소절(3.10.3, §3.12 후반)은 "제공 범위 외"로 명시한다.
=== END SCOPE LOCK ===

# 00_Content Lock v2.1 — Figure Marker Patch

**Output mode**: PATCH MODE  
**Reason**: Content Lock v2 is long, and approved marker count is 3 (≤4). PATCH MODE prevents text drift by preserving the existing Content Lock v2 body and supplying only figure strategy, briefs, and splice-ready marker blocks.  
**Phase**: 4C — Visual Pedagogy Triage  
**Scope rule applied**: Image rights = None; textbook images are not embedded. Approved figures use **Mode P: FIGURE_POINTER** only.  
**No Mermaid / SVG / HTML generated in this phase.**

---

## Figure Strategy Table — (A) Reading-order Figure Plan

| # | Reading order | Location (§ + concept card) | Mode | Source figure | Trigger (G1–G5) | Why text alone is insufficient | Expected learning gain | Decision |
|---|---|---|---|---|---|---|---|---|
| 1 | §2 → Card M1 | M1 — Modeling Carousel & 5대 Dysfunction | P | Gabrielsson & Weiner 5e, p.6, Fig.1.2 | G1, G5 | EDA → initial estimate → local/global minimum의 관계는 parameter space의 지형을 보아야 직관화된다. 텍스트만으로는 “EDA가 왜 fitting의 전 단계인가”가 절차론으로만 남는다. | Learner가 EDA를 “예쁜 plot”이 아니라 nonlinear fitting의 출발 basin을 정하는 구조적 장치로 이해한다. | KEEP |
| 2 | §2 → Card M2 | M2 — PK/PD Linkage & Therapeutic Window | P | Rowland & Tozer 5e, p.5, Fig.1-3 | G1, G2, G5 | PK의 conc-vs-time과 PD의 conc-vs-effect가 결합되어 effect-vs-time을 만든다는 3-panel 구조는 텍스트로 설명하면 쉽게 PK와 PD를 다시 분리해서 이해한다. | Learner가 PK-only, PD-only, linked PK/PD의 차이를 한 화면에서 분리한다. | KEEP |
| 3 | §2 → Card M3 | M3 — Emax / C50 / Hill γ | P | Rowland & Tozer 5e, p.41, Fig.2-16 | G1, G2, G5 | γ가 커질수록 20–80% response 구간이 압축되는 현상은 곡선 형태를 보아야 “steepness”가 처방 판단을 바꾸는 이유가 명확해진다. | Learner가 γ를 단순 parameter가 아니라 concentration 변화에 대한 response sensitivity로 체화한다. | KEEP |
| R1 | §2 → Card M1 | M1 — Modeling Carousel workflow | P candidate | Gabrielsson & Weiner 5e, p.4, Fig.1.1 | G3, G5 | Carousel 단계는 이미 본문에 6단계로 명시되어 있어 텍스트만으로도 구조가 보존된다. Fig.1.2가 같은 카드에서 더 큰 learning ROI를 갖는다. | — | REJECT — budget prioritization |
| R2 | §2 → Card M2 | Therapeutic Window | P candidate | Rowland & Tozer 5e, p.6, Fig.1-4 | G2, G5 | Therapeutic window는 중요한 그림이지만, M2에서 유지할 1개 slot은 PK/PD linkage 전체 구조를 보여 주는 Fig.1-3이 더 넓은 structural gain을 준다. | — | REJECT — budget prioritization |
| R3 | §2 → Card M3 | Ketamine graded response | P candidate | Rowland & Tozer 5e, p.35, Fig.2-11 | G1, G5 | Emax와 C50 차이를 보여 주는 좋은 data figure이나, M3의 핵심 혼동은 γ steepness이므로 Fig.2-16이 더 직접적이다. | — | REJECT — budget prioritization |
| R4 | §2 → Card M4 | Warfarin delay / turnover response | P candidate | Rowland & Tozer 5e, p.8, Fig.1-6; p.45, Fig.2-20 | G1, G5 | M4에도 강한 figure 후보가 있으나 B-Standard pointer budget을 초과한다. 본문에 warfarin, paclitaxel, total body water anchors가 이미 있어 우선순위에서 밀린다. | — | REJECT — budget exceeded |

---

## Figure Strategy Table — (B) Type-sorted Summary

- **Pointers (P)**: #1, #2, #3 → **3 / 3 used** for B-Standard.
- **Schematics (R/N)**: none → **0 / 1 used**. Scope Lock restricts this phase to pointer mode because image rights are None and textbook figure reproduction/redraw risk should be avoided.
- **Images (I)**: none → **0 / rare**. Image rights are None.
- **Rejected candidates**: R1–R4. Rejection is due to budget and relative learning ROI, not factual irrelevance.

---

# Figure Briefs — KEEP Items Only

## Figure #1 — Mode P

- **Source**: Gabrielsson & Weiner 5e, p.6, Figure 1.2 — parameter space for a one-compartment intravenous bolus model; WRSS objective surface; possible initial estimates and final estimates.
- **Why this figure matters**: This figure makes the local-minimum problem visible. It shows why EDA-derived initial estimates are not cosmetic; they determine which region of parameter space the fitting algorithm enters.
- **When to look**: After reading Card M1, especially §C Structural Necessity.
- **Learner instruction**: Focus on the yellow starting points and the red final estimates. Ask which starting point would send the program to the wrong hollow and why EDA is the safeguard.

## Figure #2 — Mode P

- **Source**: Rowland & Tozer 5e, p.5, Figure 1-3 — PK/PD linked and integrated: concentration-time, concentration-effect, and effect-time relationships.
- **Why this figure matters**: This figure prevents the common mis-mapping of PK and PD as separate disciplines. It shows that therapeutically useful prediction requires the two relationships to be linked into an effect-time profile.
- **When to look**: After reading Card M2, especially §A Formal Definition.
- **Learner instruction**: Trace the path from concentration vs time to concentration vs effect and then to effect vs time. Do not leave the figure until you can explain why either puzzle piece alone is insufficient for dosing.

## Figure #3 — Mode P

- **Source**: Rowland & Tozer 5e, p.41, Figure 2-16 — linear and semilog concentration-response plots for different Hill steepness factors.
- **Why this figure matters**: This figure turns γ from an abstract exponent into a visible change in response sensitivity. It shows why the same C50 can behave very differently when steepness changes.
- **When to look**: After reading Card M3, especially §B What γ Really Changes.
- **Learner instruction**: Compare the curves around C50, not only at the plateau. Then compare the 20–80% region to see why γ changes titration logic.

---

# Insertion Map (PATCH MODE)

| # | Reading order | Anchor (exact heading or first ≥40 chars of card) | Insert position | Marker block |
|---|---|---|---|---|
| 1 | §2 → Card M1 | `## Card M1 ⚡ Apex Concept — Modeling Carousel & 5대 Dysfunction [G pp.1–7]` | after this anchor card | `<!-- FIGURE_POINTER --><br>Source: Gabrielsson & Weiner 5e, p.6, Figure 1.2<br>Why this matters: This figure makes the local-minimum problem visible. It shows why EDA-derived initial estimates are not cosmetic; they determine which region of parameter space the fitting algorithm enters.<br>When to look: after reading Card M1, especially §C Structural Necessity<br>Learner instruction: Focus on the yellow starting points and the red final estimates. Ask which starting point would send the program to the wrong hollow and why EDA is the safeguard.<br><!-- /FIGURE_POINTER -->` |
| 2 | §2 → Card M2 | `## Card M2 — PK/PD Linkage & Therapeutic Window [T pp.3–17]` | after this anchor card | `<!-- FIGURE_POINTER --><br>Source: Rowland & Tozer 5e, p.5, Figure 1-3<br>Why this matters: This figure prevents the common mis-mapping of PK and PD as separate disciplines. It shows that therapeutically useful prediction requires the two relationships to be linked into an effect-time profile.<br>When to look: after reading Card M2, especially §A Formal Definition<br>Learner instruction: Trace the path from concentration vs time to concentration vs effect and then to effect vs time. Do not leave the figure until you can explain why either puzzle piece alone is insufficient for dosing.<br><!-- /FIGURE_POINTER -->` |
| 3 | §2 → Card M3 | `## Card M3 — Emax / C50 / Hill γ [T pp.35–43]` | after this anchor card | `<!-- FIGURE_POINTER --><br>Source: Rowland & Tozer 5e, p.41, Figure 2-16<br>Why this matters: This figure turns γ from an abstract exponent into a visible change in response sensitivity. It shows why the same C50 can behave very differently when steepness changes.<br>When to look: after reading Card M3, especially §B What γ Really Changes<br>Learner instruction: Compare the curves around C50, not only at the plateau. Then compare the 20–80% region to see why γ changes titration logic.<br><!-- /FIGURE_POINTER -->` |

---

## Splice Notes for Phase 5 Operator

1. Use the unchanged `00_Content Lock v2.md` body as the base file.
2. Insert each marker block at the end of the indicated concept card, before the next `## Card ...` heading.
3. Do not alter any surrounding Content Lock v2 text.
4. Do not add image embeds, Mermaid, SVG, or new source page tags at this phase.
5. If any anchor match count is not exactly 1, stop and return to Phase 4C for anchor revision.

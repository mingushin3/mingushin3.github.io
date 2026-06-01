# 13_Audit Report v1
## Source Fidelity Audit — Session 13: 개체간 변이 IIV·BSV·공변량

**Audit scope**: PDF 대조 감사 only. 웹 검색 OFF.  
**Inputs audited**:  
- `013_G_개체간 변이 IIV·BSV·공변량.pdf` — Gabrielsson & Weiner 5e Ch.4 excerpt + PK50, printed p.333–352, p.704–710
- `013_T_개체간 변이 IIV·BSV·공변량.pdf` — Rowland & Tozer 5e Ch.12–13, printed p.361–410
- `13_step1_draft_v0.md`
- `S13_phase1_patch memo.md` used only as audit attention guide

**Final audit verdict**: `CONDITIONAL GO to Phase 2 / NO-GO to HTML`  
Draft v0 is structurally strong and the 4-card concept architecture is mostly source-consistent. However, it contains several **source-boundary violations**: shrinkage thresholds and methodology, NONMEM control-stream implementations, FDA/21 CFR/deficiency-letter claims, and cost/time regulatory consequences are not in the attached PDF sources. The main PDF-anchored content to preserve is: R&T Ch.12 variability taxonomy and population analysis; R&T Ch.13 inherited variability and pharmacogenetic examples; G&W Ch.4 EDA/spaghetti/NAD/NPD/modeling diagnostics; and PK50 CpD total vs unbound parameter comparison.

---

## T1: Equation/Numerical Audit

| Item | Draft v0 Expression | PDF Source | Classification | Correction |
|---|---|---|---|---|
| Source range | R&T Ch.12–13 p.361–410 + G&W Ch.4 p.333–352 + PK50 p.704–710 | Uploaded PDFs match these ranges. G PDF contains Ch.4 p.333–352 and PK50 p.704–710; T PDF contains R&T p.361–410. | MATCH | No correction. |
| NLME master equation | `Yij = f(theta, eta_i, xij) + g(theta, eta_i, xij)·eps_ij` | R&T p.369 describes mixed-effect modeling and distinguishes fixed effects, random effects, IIV/IOV/residual variability, θ/η/ε-like notation; it does not print this exact general equation. | NOT_IN_SOURCE | Label as `[교과서 외 구현/통계 번역]`. The concept is source-compatible, but the exact equation is not printed in the PDFs. |
| Fixed/random/residual taxonomy | `theta` fixed effect, `eta` BSV/IIV, `epsilon` residual; `$THETA/$OMEGA/$SIGMA` | R&T p.369–373 supports fixed/random/residual variance concepts and NONMEM/maximum likelihood; NONMEM block syntax is not shown. | RESTORED | Keep taxonomy; label NONMEM syntax as implementation translation, not direct source text. |
| Exponential IIV | `CL_i = theta_CL·exp(eta_i)`; `ln CL_i = ln theta_CL + eta_i` | R&T p.371 gives exponential error model for individual parameter variability, general form `CL_i = CL·exp(η)`, and states it is frequently used because CL cannot go negative. | MATCH | No correction. |
| `CV(%) ≈ omega × 100` | Small-ω approximation | R&T p.367 defines CV as SD/mean and p.371 discusses exponential model approximating constant CV; exact approximation is not explicitly printed. | RESTORED | Accept as pedagogical simplification; if retained, mark as approximation. |
| R&T residual error models | Additive `Y=F+eps`; Proportional `Y=F(1+eps)`; Exponential `Y=F·exp(eps)` | R&T p.372 explicitly lists additive, proportional, exponential residual error models and defines `Y_i`, `F`, and `ε`; p.373 states exponential becomes additive in log domain. | MATCH | No correction for the three model forms. |
| Mixed residual model | `Y = F(1+eps1)+eps2`; `W=sqrt((IPRED·theta3)^2+theta4^2)` | R&T p.372 lists additive/proportional/exponential only. The combined/mixed NONMEM `W` model is not in source. | NOT_IN_SOURCE | Label as `[교과서 외 구현 번역]`. Do not call it source-derived. |
| LTBS/log transform | `ln Y = ln F + eps` | R&T p.373: exponential error model becomes additive in ln domain. | MATCH | No correction. |
| Shrinkage formula | `eta-shrinkage = 1 - SD(eta_EBE)/omega` | Not in R&T/G&W PDFs. Draft cites Savic & Karlsson 2009, which is outside attached source. | NOT_IN_SOURCE | Move to `[교과서 외 후속 구현 지식]` or remove from source-locked Step 1. |
| Shrinkage threshold | `>30%` problematic; `>20% epsilon-shrinkage`; `42%`, `12%`, etc. | Not in R&T/G&W PDFs. | NOT_IN_SOURCE | Must not be presented as PDF-supported. |
| FDA/Deficiency/NDA claims | `NDA Deficiency Letter`, `21 CFR 314.50`, `18–24개월`, `USD 200–500M`, `90% possibility` | Not in attached PDFs. R&T p.373 says population analysis is now used in nearly all phases and evolved to regulatory requirement, but no deficiency letter, CFR section, timeline, cost, or probability. | NOT_IN_SOURCE | Delete or mark explicitly as external regulatory scenario. For this audit, classify as MUST_FIX. |
| `OFV` formula and LRT | `OFV = Σ[(obs-pred)^2]/σ²`; `ΔOFV > 3.84` for df=1, α=0.05; AIC for non-nested | R&T p.373 directly explains OFV, likelihood ratio test, chi-square distribution, ΔOFV 3.84 at α=0.05/df=1, nested-model limitation, and AIC for non-nested. | MATCH | No correction. |
| G&W PK50 dose/regimen | CpD 566 µg over 5 h IV infusion in 12 subjects | G&W p.705–706 and Fig.50.1: 12 subjects, CpD 566 µg, 5-hour constant IV infusion. | MATCH | No correction. |
| PK50 safety threshold | Total plasma concentration above 50 µg/L should be avoided; target total range >10 and <50 µg/L | G&W p.705, p.709: avoid total plasma concentrations above 50 µg/L; Q1 asks infusion rate to reach >10 and <50 µg/L. | MATCH | No correction. |
| PK50 two-compartment parameters | `Cl`, `Vc`, `Vt`, `Cld`; initial `Cl=10 L/h`, `Vss=55 L`, `Vc=11.5 L`, `Cld=10 L/h` | G&W p.705–706 states two-compartment model parameterized by Cl, Vc, Vt, Cld; p.706 provides initial estimates. | MATCH | No correction. |
| Eq.50:1 | `Cld` estimated from initial slope, Vc, Cl | G&W p.706 gives Eq.50:1 but the exact equation image is not fully extracted in text; context supports Cld derivation. | RESTORED | Keep only if visually checked against equation; otherwise avoid exact algebra beyond source wording. |
| Eq.50:2–50:4 | `CL = fu·CLu`, `Vss = fu·Vu,ss`, `Cld = fu·Cldu` | G&W p.706 says unbound clearance, Vss, and Cld were derived from total parameters and `fu`; algebraically source-compatible as rearrangement of `CLu=CL/fu` etc. | MATCH | No correction if framed as algebraic rearrangement. |
| PK50 Table 50.1 total/unbound Cl | Total Cl = 11.4 L/h CV 28%; unbound Clu = 720 L/h CV 9% | G&W p.708 Table 50.1 exactly. | MATCH | No correction. |
| PK50 Table 50.1 Cld | Total Cld = 4.35 L/h CV 39%; unbound Cldu = 265 L/h CV 33% | G&W p.708 Table 50.1 exactly. | MATCH | No correction. |
| PK50 Table 50.1 Vc | Total Vc = 19.9 L CV 29%; unbound Vc,u = 1270 L CV 18% | G&W p.708 Table 50.1 exactly. | MATCH | No correction. |
| PK50 Table 50.1 Vt | Total Vt = 30.9 L CV 35%; unbound Vt,u = 2030 L CV 51% | G&W p.708 Table 50.1 exactly. | MATCH | No correction. |
| `fu = 0.016 ± 0.0049` | mean ± SD, CV ≈31% | G&W p.708: free fraction `fu` mean ± SD = 0.016 ± 0.0049; CV calculation ≈30.6%. | MATCH | No correction. |
| `CLu = 11.4 / 0.016 = 712.5 ≈ 720 L/h` | In Q2 and C3 logic | G&W p.708 values support this arithmetic. | MATCH | No correction. |
| Variance propagation | `CV(CL)^2 ≈ CV(fu)^2 + CV(CLu)^2`; `0.078 ≈ 0.104`, “reasonable agreement” | The formula and independence assumption are not in the PDF. Numerically, `0.28² - 0.31²` is negative and does not yield `0.09²`. | ERROR | Do not use this as source-supported validation. State only that total Cl CV was 28% and unbound Clu CV was 9% in Table 50.1. |
| “fu covariate reduces ω²(CL) 28% → 9%” | Repeated in Curation Map/C1/C3 | G&W shows total Cl CV 28% vs unbound Clu CV 9% after using fu to derive unbound parameters. It does **not** report a NONMEM covariate-model ω² reduction. | ERROR | Replace conceptually with: PK50 shows total Cl CV 28% and unbound Clu CV 9%; this supports protein binding as a source of total-parameter variability. |
| PK50 Table 50.2 EC50/Emax/n | EC50 total 1.8 CV40%; unbound 0.029 CV60%; Emax 2.1 CV60%; n 2.1 CV30% | G&W p.708 Table 50.2 exactly. | MATCH | No correction. |
| PK50 response variability | 8-fold response variability, 0.5–4.0 response units; responders/non-responders | G&W p.707–709 Fig.50.2 and text state 8-fold variability, response units 0.5–4.0, Emax <1 as non-responders due to genetic makeup. | MATCH | No correction. |
| “receptor density genetic” | Draft states receptor density/genetic difference explains response | G&W p.709: genetic makeup coded for receptor density; all subjects with response <1 lacked full target expression. | MATCH | No correction. |
| R&T warfarin dose range | Wide daily warfarin dose in 200 adults | R&T p.362 Fig.12-1. | MATCH | No correction. |
| Nortriptyline 25 mg TID, n=263 | Plateau plasma concentration distribution | R&T p.363 Fig.12-2: 263 patients, 25 mg orally 3 times daily. | MATCH | No correction. |
| Midazolam/alfentanil `n=12` | CYP3A4 cosegregation | R&T p.364 Fig.12-3: IV and oral in 12 subjects. | MATCH | No correction if included. |
| S-warfarin pharmacodynamic variability `n=97` | unbound S-warfarin concentration spread | R&T p.364 Fig.12-4: 97 patients on maintenance therapy. | MATCH | No correction. |
| CV thresholds | CV ≤10% low, 25% moderate, >40% high | R&T p.367 directly states typical interpretation. | MATCH | No correction. |
| Oral bioavailability variability | CV increases as bioavailability decreases; about 10% near 100%, 50% toward zero; 149 studies, 100 drugs | R&T p.367 Fig.12-7 and text. | MATCH | No correction if included. |
| Creatinine clearance as covariate | CrCl characterizes part of renal clearance / total clearance variability | R&T p.369–371 Fig.12-9/12-11. | MATCH | No correction. |
| NPD/NAD statements | NAD/NPD vs population approach | G&W p.335–336 supports NAD/NPD definitions and warns mean data can bias estimates; R&T p.369 contrasts two-stage and population analysis. | MATCH | No correction; but Draft should not overstate NPD as `σ²≈0.08` without source. |
| `σ²≈0.08` in NPD/PK50 | NPD would absorb ω²(Cl) 28% as residual `σ²≈0.08` | Not in PDF. This is an implementation inference. | NOT_IN_SOURCE | Delete or label as external inference. |
| C4 genetic polymorphism definition | `>1% variant frequency` | R&T p.394: genetic polymorphism defined clinically as variant frequency >1% of population. | MATCH | No correction. |
| Hardy-Weinberg | `p², 2pq, q²`; NAT2 example | R&T p.402–403 explains p/q calculation for acetylator status and genotype frequencies. | MATCH | No correction. |
| CYP2D6 PM frequency | 5–10% Caucasians; 3.8% African Americans; 0.9% Asians; 1% Arabs | R&T p.395 Table 13-1. | MATCH | No correction. |
| CYP2C9 PM frequency | 1–3% Caucasians | R&T p.395 Table 13-1. | MATCH | No correction. |
| CYP2C19 PM frequency | 3–5% Caucasians; 16% Asians | R&T p.395 Table 13-1. | MATCH | No correction. |
| TPMT PM frequency | 0.3% Caucasians; 0.04% Asians | R&T p.395 Table 13-1. | MATCH | No correction. |
| NAT2 slow acetylator frequency | 60% Caucasians/African Americans; 10–20% Asians | R&T p.395 Table 13-1. | MATCH | No correction. |
| UGT1A1 frequency | 11% Caucasians; 1–3% Asians | R&T p.395 Table 13-1. | MATCH | No correction. |
| CYP2D6 gene copy/nortriptyline | 0/1/2/3/13 functional genes; 25 mg single dose; more copies → higher clearance/lower exposure | R&T p.397 Fig.13-2. | MATCH | No correction. |
| “0 genes vs 13 genes ~10-fold” | Draft approximates concentration difference | Fig.13-2 visually supports large order-of-magnitude separation, but exact 10-fold is not stated in caption. | RESTORED | Mark as approximate visual reading, not exact value. |
| Metoprolol 200 mg oral | Poor vs extensive CYP2D6 metabolizers | R&T p.397 Fig.13-3: single oral 200 mg metoprolol tartrate. | MATCH | No correction. |
| CYP2C9 warfarin clearance/dose | CYP2C9 genotype affects S-warfarin unbound clearance and maintenance dose | R&T p.398 Fig.13-4. | MATCH | No correction. |
| “CYP2C9*3/*3 dose 1/4 of *1/*1” | Draft says ~4-fold dose difference | Fig.13-4 visually supports lower dose, but exact 1/4 is not stated in text. | RESTORED | Treat as approximate visual interpretation; avoid exact ratio unless transcribed from figure values. |
| CYP3A4 variability 30–40% | Common CV order 30–40% due to enzymatic activity | R&T p.398 states CV order 30–40%. | MATCH | No correction. |
| Codeine UM frequency | 1% Caucasians; 28% some North African communities; contraindicated in breastfeeding UM women | R&T p.399. | MATCH | No correction. |
| TPMT activity frequencies | 90% high, 10% intermediate, 0.3% minimal/no activity | R&T p.399. | MATCH | No correction. |
| TPMT exposure ~10-fold | TPMT-deficient patients active thioguanine nucleotide exposure 10-fold higher | R&T p.400 Fig.13-5. | MATCH | No correction. |
| NAT2 isoniazid | 9.8 mg/kg orally; 483 subjects; 6-hr plasma concentration bimodal | R&T p.402 Fig.13-6. | MATCH | No correction. |
| DNA tests prediction 95–97.5% | Genotype predicts N-acetylation and CYP2D6 phenotype in healthy volunteers | R&T p.407. | MATCH | No correction. |
| Warfarin 43% / 62% / 38% explained | Draft contains potentially “~43% only by genotype” and “~62% total / 38% residual” | R&T Fig.13-8 pie chart is present, but Draft’s exact breakdown must be verified from figure. The visible text states genotyping and covariates explain a portion of total variance. | RESTORED | Keep only exact percentages if transcribed directly from Fig.13-8; otherwise use qualitative wording. |
| FDA Pharmacogenomic Biomarker label >200 drugs | Claimed in Draft C4 L5 | Not in attached PDFs. | NOT_IN_SOURCE | Delete or label as current external regulatory context. |
| HLA-B*5701 5–8% Caucasian | Draft claims frequency | R&T Table 13-2 lists HLA-B*5701 and hypersensitivity reaction in Caucasians but does not give 5–8% frequency in the extracted source range. | NOT_IN_SOURCE | Remove frequency or mark external. |
| Abacavir contraindication | HLA-B*5701 hypersensitivity reaction | R&T p.396 Table 13-2 supports hypersensitivity reaction in Caucasians; “contraindication” wording is clinical extrapolation not directly in table. | RESTORED | Keep only as pharmacodynamic adverse-effect example unless label-level contraindication is externally sourced. |
| “PM/IM/EM/UM frequency table” | Draft table gives PM 5–10%, IM ~30%, EM ~50%, UM 1–3% | R&T supports PM frequency and existence of ultrafast metabolizers with up to 13 copies; it does not give IM/EM/UM frequencies as stated. | ERROR | Retain only source-supported PM frequency and qualitative EM/UM statements unless external source is allowed. |
| PIPET/NONMEM categorical covariate code | `IF (PHENO.EQ.x) CLFAC = THETA(y)` | Not in R&T/G&W PDFs. | NOT_IN_SOURCE | Label `[교과서 외 구현 번역]`; not direct source content. |

---

## T2: Examples & Data Audit

| Item | Draft v0 Status | PDF Location | Classification | Importance | Action |
|---|---|---|---|---|---|
| G&W modeling carousel | Briefly implicit in source role but not central | G&W p.333 Fig.4.1 | MISSING | LOW | Optional context only. |
| EDA “plot first; do not rush into equations” | Underrepresented; mentioned indirectly | G&W p.334–335 | MISSING | MEDIUM | Add 1–2 sentence source anchor in C1 or C3. |
| Spaghetti plot showing Japanese/Caucasian grouping | Mentioned as context but not fully anchored | G&W p.335–336 Fig.4.2 | INCLUDED_CORRECT | HIGH | Preserve. It is a direct visual anchor for variability/subgroups. |
| NAD/NPD definitions and warning | Included in Pair 4 | G&W p.335–336 | INCLUDED_CORRECT | HIGH | Preserve; avoid unsupported `σ²≈0.08` inference. |
| Transformations hide/reveal lack of fit | Largely omitted | G&W p.337–339 Figs.4.3–4.5 | MISSING | MEDIUM | Include only if needed for residual/model diagnostic bridge. |
| Lineweaver-Burke/Scatchard transformations | Excluded in context | G&W p.340–341 Fig.4.6 | INCLUDED_CORRECT as exclusion | LOW | Omission justified; outside variance-axis scope. |
| Nonlinear kinetics / dose normalization | Mostly omitted | G&W p.341–342 Fig.4.7 | MISSING | LOW | Optional; not essential for Session 13. |
| Parameter estimability formula | Mentioned as identifiability context | G&W p.342–343 Eq.4:3 | INCLUDED_AS_CONTEXT | MEDIUM | Keep as context; do not overgeneralize to ω²–σ² without label. |
| Identifiability/nonidentifiability | Included in limitations | G&W p.347–350 Figs.4.13–4.14, Tables 4.1–4.2 | INCLUDED_CORRECT | MEDIUM | Preserve as context. |
| PK50 CpD 12 subjects, 566 µg 5h infusion | Included | G&W p.704–705, Fig.50.1 | INCLUDED_CORRECT | HIGH | Preserve. |
| PK50 total/unbound parameter table | Included | G&W p.708 Table 50.1 | INCLUDED_CORRECT | HIGH | Preserve; use exact total vs unbound CV wording. |
| PK50 PD EC50/Emax/n table | Included | G&W p.708 Table 50.2 | INCLUDED_CORRECT | HIGH | Preserve. |
| PK50 individual `fu` table | Partly included by mean `fu` only | G&W p.710 Table 50.3 | INCLUDED_CORRECT | MEDIUM | Individual values not necessary unless Phase 4C wants a pointer. |
| Warfarin daily dose variability, 200 adults | Included in anchor list, not deeply used | R&T p.362 Fig.12-1 | INCLUDED_CORRECT | HIGH | Preserve as R&T Ch.12 opening variability example. |
| Nortriptyline plateau, 263 patients, 25 mg TID | Included | R&T p.363 Fig.12-2 | INCLUDED_CORRECT | HIGH | Preserve; useful for log-normal distribution. |
| Midazolam/alfentanil CYP3A4 cosegregation | Largely omitted | R&T p.364 Fig.12-3 | MISSING | MEDIUM | Could be included as inherited/enzymatic covariance example but not required. |
| S-warfarin PD variability in 97 patients | Partly included | R&T p.364 Fig.12-4 | INCLUDED_CORRECT | MEDIUM | Preserve if differentiating PK vs PD variability. |
| Dose/time dependence of variability assessment | Mostly omitted | R&T p.365 Fig.12-5 | MISSING | MEDIUM | Add optional caution: variability assignment depends on dose/time unless parameterized. |
| Hypothetical clearance distributions A–D | Included conceptually in C4 | R&T p.366 Fig.12-6 | INCLUDED_CORRECT | HIGH | Preserve; central to unimodal vs bimodal shape. |
| Bioavailability variability vs F | Omitted | R&T p.367 Fig.12-7 | MISSING | LOW | Optional enrichment only. |
| Averaging data distortion | Included via NAD/NPD pair but not figure | R&T p.367–368 Fig.12-8 | INCLUDED_AS_CONTEXT | MEDIUM | Preserve as warning; figure pointer optional. |
| Population analysis CrCl covariate | Included in C3 | R&T p.369–371 Figs.12-9–12-11 | INCLUDED_CORRECT | HIGH | Preserve. |
| Residual variance and residual error | Included in C2 | R&T p.371–372 Figs.12-12–12-14 | INCLUDED_CORRECT | HIGH | Preserve; remove unsupported shrinkage overlay. |
| Maximum likelihood, OFV, LRT/AIC | Included | R&T p.373 | INCLUDED_CORRECT | MEDIUM | Preserve as context. |
| Table 12-1 additional variability factors | Mentioned in context | R&T p.374 Table 12-1 | INCLUDED_AS_CONTEXT | MEDIUM | Preserve as context; not a MUST card. |
| Nonadherence pattern | Partly mentioned | R&T p.375 Fig.12-15 | INCLUDED_AS_CONTEXT | LOW | Optional. |
| St. John’s wort interaction | Mentioned in context | R&T p.376 Fig.12-16 | INCLUDED_AS_CONTEXT | LOW | Optional. |
| Grapefruit juice variability | Not used | R&T p.377 Fig.12-17 | MISSING | LOW | Omission justified. |
| Chronotherapy | Mentioned in context | R&T p.378 Fig.12-18 | INCLUDED_AS_CONTEXT | LOW | Omission acceptable. |
| Dose-response/exposure-response trial examples | Largely omitted | R&T p.379–381 Figs.12-19–12-20 | MISSING | MEDIUM | Optional if emphasizing PK vs PD variability. |
| Theophylline and propranolol kinetic examples | Included only in final anchor list | R&T p.382–383 Figs.12-21–12-22 | INCLUDED_AS_CONTEXT | LOW | Optional. |
| Hepatic intrinsic clearance low/high extraction | Omitted | R&T p.384–385 Fig.12-23 | MISSING | LOW | Omission justified; source focus is Session 13, not hepatic clearance. |
| Warfarin genotype simulation | Included in C4 | R&T p.386 Fig.12-24 | INCLUDED_CORRECT | MEDIUM | Preserve if exact percentages verified. |
| Voriconazole PTA by CYP2C19 | Omitted | R&T p.387 Fig.12-25 | MISSING | MEDIUM | Could be useful for genotype-to-target attainment, but not critical. |
| Dose strengths design | Omitted | R&T p.388–390 Fig.12-26 | MISSING | MEDIUM | Omission acceptable if Session scope is PopPK variance; optional bridge to dosing. |
| Propofol PD variability | Omitted | R&T p.391 Fig.12-27 | MISSING | LOW | Omission justified. |
| Twin study nortriptyline genetics | Not included | R&T p.394 Fig.13-1 | MISSING | MEDIUM | Add as brief genetic evidence source if C4 needs stronger author message. |
| Table 13-1 PM frequencies | Included | R&T p.395 Table 13-1 | INCLUDED_CORRECT | HIGH | Preserve exact values. |
| Table 13-2 pharmacodynamic genetic polymorphisms | Included partially | R&T p.396 Table 13-2 | INCLUDED_CORRECT | HIGH | Preserve, but do not add unsupported frequencies. |
| CYP2D6 nortriptyline gene-copy figure | Included | R&T p.397 Fig.13-2 | INCLUDED_CORRECT | HIGH | Preserve; exact “10-fold” should be approximate unless transcribed. |
| CYP2D6 metoprolol 200 mg | Included | R&T p.397 Fig.13-3 | INCLUDED_CORRECT | MEDIUM | Preserve. |
| CYP2C9 warfarin maintenance | Included | R&T p.398 Fig.13-4 | INCLUDED_CORRECT | HIGH | Preserve. |
| CYP3A4 no clear genetic factor | Mostly omitted | R&T p.399 | MISSING | MEDIUM | Add if avoiding overclaim that all IIV has genotype peaks. |
| Codeine UM breastfeeding contraindication | Included | R&T p.399 | INCLUDED_CORRECT | MEDIUM | Preserve. |
| TPMT thiopurine case | Included | R&T p.399–400 Fig.13-5 | INCLUDED_CORRECT | HIGH | Preserve. |
| UGT1A1 bilirubin/irinotecan | Mostly omitted | R&T p.401 | MISSING | LOW | Optional. |
| NAT2 isoniazid bimodal + population table | Included | R&T p.402–403 Fig.13-6/Table13-3 | INCLUDED_CORRECT | HIGH | Preserve. |
| Table 13-4 genetic polymorphism consequences | Omitted | R&T p.404 | MISSING | MEDIUM | Optional; useful for drug vs metabolite logic. |
| G6PD/primaquine PD example | Largely omitted | R&T p.405 Fig.13-7 | MISSING | MEDIUM | Could be included in C4 table if avoiding overly PK-centric genetics. |
| VKORC1 warfarin PD variability | Included | R&T p.406 Fig.13-8 | INCLUDED_CORRECT | HIGH | Preserve; exact percentages need verification. |
| Metabolic phenotyping | Partly included | R&T p.407 | INCLUDED_AS_CONTEXT | MEDIUM | Preserve as phenotype/genotype method bridge. |
| Pharmacogenetics-based recommendations | Partly included | R&T p.407–408 Fig.13-9 | INCLUDED_AS_CONTEXT | MEDIUM | Preserve but do not add current FDA label counts. |
| Beta-blocker CYP2D6 Table 13-5 | Omitted | R&T p.409 Study Problem/Table13-5 | MISSING | LOW | Study problem; omission justified. |

---

## T3: Author Key Messages

| Message | PDF Location | In Draft v0? | Status |
|---|---|---|---|
| Modeling requires theory, intuition, patience, experience; do not design experiments only to confirm existing beliefs. | G&W p.333 Fig.4.1 caption/background | Partially | SHOULD_FIX — draft is implementation-heavy; this design/EDA epistemic warning is underemphasized. |
| Do not rush into equations; let data lead to model/equation. | G&W p.334 and p.337 | Partially | SHOULD_FIX — add as C1/C3 context anchor. |
| Spaghetti plots show variability better than mean curve with error bars. | G&W p.335–336 | Yes, partly | MATCH — Pair 4/context captures this. |
| Mean-data fitting can bias estimates and should be avoided; population approach may solve multi-subject variability. | G&W p.335 | Yes | MATCH. |
| Transformed plots can reveal lack of fit hidden by linear plots. | G&W p.337–339 | Weakly/no | OPTIONAL — useful for residual diagnostic bridge but not central. |
| Identifiability/estimability depend on data information content, noise, and design. | G&W p.342–350 | Yes, partly | MATCH with caution — do not overextend to unsupported ω²/σ² statements. |
| PK50: plasma protein binding `fu` explains part of total concentration/parameter variability; safety margin recommended on unbound rather than total concentration. | G&W p.704–709 | Yes | MATCH — core anchor. |
| PK50: PD response variability cannot be explained exclusively by plasma protein binding; nonresponders likely due to genetic target/receptor expression. | G&W p.707–709 | Yes | MATCH. |
| Average data guide therapy, but individual-patient information is ultimately all-important. | R&T p.362 | Partially | MATCH/SHOULD_FIX — big idea aligns but quote-like message not explicit. |
| Variability exists in both PK and PD; plasma drug measurement is prerequisite for separating them. | R&T p.363–364 | Partially | SHOULD_FIX — make explicit in C1 or C3. |
| Mean and distribution shape/variance are both important; bimodal distribution makes the mean unlikely. | R&T p.366 Fig.12-6 | Yes | MATCH. |
| CV is unit-independent; typical CV interpretation: ≤10% low, 25% moderate, >40% high. | R&T p.367 | Partially | OPTIONAL — can support interpretation of Table 50.1. |
| Population analysis distinguishes fixed effects, IIV/IOV/residual variability; covariates explain some interindividual differences. | R&T p.369–371 | Yes | MATCH. |
| Residual variability should be random with mean zero and variance σ²; systematic trends mean structural/error model has not explained variability. | R&T p.371–372 | Yes | MATCH, but unsupported shrinkage additions must be separated. |
| Population analysis evolved to regulatory requirement. | R&T p.373 | Yes, overextended | ERROR — source supports regulatory importance, not specific FDA deficiency/CFR/cost/timeline claims. |
| Many sources of variability include genetics, disease, age, gender, body weight, concomitant drugs, behavior/environment. | R&T p.373–374/Table12-1 | Yes, context | MATCH. |
| Inheritance accounts for large part of individual differences; inherited traits remain lifelong. | R&T p.393 | Yes | MATCH. |
| Ethnicity is an imperfect proxy; within-group variability can be nearly as large as between groups; individual genetic characteristics are most important. | R&T p.395 | Partially | SHOULD_FIX — important author caution against ethnicity-overclaim. |
| Genetic polymorphism in metabolism was often detected through adverse reactions in poor metabolizers after normal doses. | R&T p.396 | Yes, partly | MATCH. |
| Genetic tests should lead to actionable, straightforward clinical recommendations; implementation into EHR/decision support is discussed. | R&T p.407–408 | Partially | MATCH with caution — avoid unsupported modern FDA label counts. |
| Pharmacogenetics has major potential but is not yet fully leveraged; other factors beyond genotype often matter. | R&T p.409 | Partially | SHOULD_FIX — helpful guardrail against genotype determinism. |

---

## T4: Priority Summary (sorted: MUST_FIX → SHOULD_FIX → OPTIONAL → REJECT)

| # | Item | Priority | Rationale |
|---|---|---|---|
| 1 | Shrinkage as C2 Apex; shrinkage formula, 30% threshold, Savic & Karlsson 2009 treated as source content | MUST_FIX | Not in attached PDFs. Residual error is source-supported; shrinkage diagnostic is external/future-session content. |
| 2 | FDA Deficiency Letter / 21 CFR 314.50 / 18–24개월 / USD 200–500M / 90% claims | MUST_FIX | Not in PDFs and presented as high-stakes factual/regulatory claims. |
| 3 | “fu covariate reduces ω²(CL) 28%→9%” | MUST_FIX | Source shows total Cl CV 28% vs derived unbound Clu CV 9%; not a reported NONMEM covariate model reduction. |
| 4 | Variance propagation equation validating CV reduction | MUST_FIX | Arithmetic does not support the claim under independence; formula not in source. |
| 5 | NONMEM control stream blocks without source-boundary label | MUST_FIX | Useful implementation translation but not in R&T/G&W PDFs. |
| 6 | “Mixed RUV default for Phase 2/3” | MUST_FIX | R&T lists additive/proportional/exponential; combined model/default statement is external practice. |
| 7 | CYP2D6 PM/IM/EM/UM full frequency table | MUST_FIX | PM frequency and UM existence source-supported; IM/EM/UM percentages in draft are not source-supported. |
| 8 | HLA-B*5701 5–8% Caucasian, FDA biomarker label >200 drugs | MUST_FIX | Not in PDFs. |
| 9 | Exact fold/percentage claims for CYP2D6, CYP2C9/VKORC1, warfarin explained variance | SHOULD_FIX | Some are visually plausible but require direct figure transcription. Use qualitative wording unless exact. |
| 10 | G&W “plot first; let data lead” author message underused | SHOULD_FIX | Important chapter-opening message relevant to EDA → covariate hypothesis. |
| 11 | R&T ethnicity caution underused | SHOULD_FIX | Prevents overclaiming genetic/ethnic categories as deterministic covariates. |
| 12 | PK vs PD variability separation could be clearer | SHOULD_FIX | R&T p.363–364 explicitly states plasma measurement is prerequisite to separating PK and PD variability. |
| 13 | Spaghetti plot → subgroup/covariate hypothesis could be strengthened | SHOULD_FIX | G&W Fig.4.2 is highly relevant to C1/C3. |
| 14 | Table 13-4 genetic polymorphism consequences omitted | OPTIONAL | Useful but not essential for core card architecture. |
| 15 | Voriconazole PTA by CYP2C19 omitted | OPTIONAL | Good genotype-to-dosing example; not required. |
| 16 | Propofol, bioavailability, chronotherapy, grapefruit details omitted | OPTIONAL | Lower priority; can remain context/exclusion. |
| 17 | Lineweaver-Burke/Scatchard/Euler detailed treatment excluded | REJECT | Scope creep; belongs to model-fitting/estimation session, not IIV/covariate core. |
| 18 | Extensive pharmacogenomics label-count modernization | REJECT | Current regulatory fact not in source; would require web/current guidance, which is off. |

---

## T5: Coverage Audit

| PDF Element | Type | PDF Location | Step 1 Status | Omission Verdict | Required Action |
|---|---|---|---|---|---|
| G&W Ch.4 Objectives | Heading/objectives | G&W p.333 | OMITTED_JUSTIFIABLE | Low-level chapter intro | None. |
| 4.1 Background / modeling carousel | H2 + Fig.4.1 | G&W p.333 | INCLUDED_AS_CONTEXT | Omitted details justified | Keep only design/EDA warning if needed. |
| 4.2 Plot and Explore Data | H2 | G&W p.334 | INCLUDED_AS_CONTEXT | None | Preserve EDA bridge. |
| 4.2.1 Understand your experimental data better | H3 | G&W p.334–335 | OMITTED_PROBLEMATIC | MISSING_AUTHOR_MSG | Add “plot before equations” 1–2 sentences. |
| Extensive EDA question list | Repeated author method | G&W p.334–335 | OMITTED_JUSTIFIABLE | Long checklist too broad | Optional compressed mention only. |
| 4.2.2 Pooling of data from multiple subjects | H3 | G&W p.335–336 | INCLUDED_AS_MUST | None | Maintain NAD/NPD/population discussion. |
| Figure 4.2 Spaghetti plot | Figure | G&W p.336 | INCLUDED_AS_CONTEXT | None | Use as strong visual pointer if Phase 4C. |
| 4.2.3 Transformation for exploration | H3 | G&W p.337–339 | OMITTED_PROBLEMATIC | MISSING_BRIDGE | Consider 1 sentence: transformations can hide/reveal fit defects. |
| Figures 4.3–4.5 | Figures | G&W p.337–339 | OMITTED_JUSTIFIABLE | Diagnostic details outside core | Optional. |
| 4.2.4 Lineweaver-Burke and Scatchard transformation | H3 | G&W p.340–341 | OMITTED_JUSTIFIABLE | Scope exclusion | No action. |
| Figure 4.6 | Figure | G&W p.340 | OMITTED_JUSTIFIABLE | Scope exclusion | No action. |
| 4.2.5 Nonlinear kinetics | H3 | G&W p.341–342 | OMITTED_JUSTIFIABLE | Scope exclusion | Optional only. |
| Figure 4.7 | Figure | G&W p.341 | OMITTED_JUSTIFIABLE | Scope exclusion | No action. |
| 4.3 How Complicated a Model? | H2 | G&W p.342 | INCLUDED_AS_CONTEXT | None | Keep as identifiability context. |
| 4.3.1 How many parameters? | H3 + Eq.4:3 | G&W p.342–343 | INCLUDED_AS_CONTEXT | None | Keep brief. |
| Eq.4:3 parameter estimability | Equation | G&W p.342–343 | INCLUDED_AS_CONTEXT | None | Do not overextend. |
| 4.3.2 How do we specify the model? | H3 | G&W p.343–347 | OMITTED_JUSTIFIABLE | General model specification outside session | No action. |
| Figures 4.8–4.12 | Figures | G&W p.343–347 | OMITTED_JUSTIFIABLE | Structural model examples outside session | No action. |
| 4.3.3 Simultaneous modeling | H3/Table4.1 | G&W p.347 | OMITTED_JUSTIFIABLE | Useful but not core | Optional. |
| 4.3.4 Identifiability | H3 | G&W p.348–349 | INCLUDED_AS_CONTEXT | None | Keep. |
| Figure 4.13, Table 4.2 | Figure/table | G&W p.348–349 | INCLUDED_AS_CONTEXT | None | Optional figure pointer. |
| 4.3.5 Estimability | H3/Fig.4.14–4.15 | G&W p.349–351 | INCLUDED_AS_CONTEXT | None | Keep only 1 sentence. |
| 4.4 Getting to the next circulation | H2/Fig.4.16 | G&W p.352 | OMITTED_JUSTIFIABLE | General modeling cycle | No action. |
| PK50 objectives | Case objectives | G&W p.704 | INCLUDED_AS_MUST | None | Preserve. |
| PK50 Step I total concentrations | Case section | G&W p.704–706 | INCLUDED_AS_MUST | None | Preserve dose/regimen. |
| Fig.50.1 total/unbound concentration-time | Figure | G&W p.705 | INCLUDED_AS_MUST | None | View instruction recommended in Phase 4C. |
| Eq.50:1 Cld | Equation | G&W p.706 | INCLUDED_AS_CONTEXT | None | Exact equation optional. |
| PK50 Step II unbound concentrations | Case section | G&W p.706–707 | INCLUDED_AS_MUST | None | Preserve fu as covariate/source anchor. |
| Eq.50:2–50:4 | Equations | G&W p.706 | INCLUDED_AS_MUST | None | Preserve with correct algebraic framing. |
| PK50 Step III PD data | Case section | G&W p.707–709 | INCLUDED_AS_MUST | None | Preserve PK vs PD covariate distinction. |
| Fig.50.2 response vs concentration | Figure | G&W p.707 | INCLUDED_AS_MUST | None | View instruction recommended. |
| Table 50.1 | Table | G&W p.708 | INCLUDED_AS_MUST | None | Preserve exact values. |
| Table 50.2 | Table | G&W p.708 | INCLUDED_AS_MUST | None | Preserve exact values. |
| Table 50.3 | Table | G&W p.710 | INCLUDED_AS_CONTEXT | None | Individual values optional. |
| R&T Ch.12 objectives | Objectives | R&T p.361 | INCLUDED_AS_CONTEXT | None | No action. |
| Ch.12 opening: patients differ; tailor drug administration | Author key message | R&T p.361–362 | INCLUDED_AS_CONTEXT | MISSING_AUTHOR_MSG partial | Strengthen in §1/§8 if needed. |
| Expressions of Individual Differences | H2 | R&T p.362 | INCLUDED_AS_MUST | None | Preserve examples. |
| Fig.12-1 warfarin dose | Figure | R&T p.362 | INCLUDED_AS_CONTEXT | None | Preserve as opening example. |
| Fig.12-2 nortriptyline log-normal | Figure | R&T p.363 | INCLUDED_AS_MUST | None | Preserve. |
| Fig.12-3 CYP3A4 cosegregation | Figure | R&T p.364 | OMITTED_PROBLEMATIC | MISSING_EXAMPLE | Optional but useful for enzyme-related covariance. |
| Fig.12-4 S-warfarin PD variability | Figure | R&T p.364 | INCLUDED_AS_CONTEXT | None | Preserve. |
| Quantifying Variability | H3 | R&T p.365–366 | INCLUDED_AS_CONTEXT | None | Keep dose/time warning optional. |
| Fig.12-5 dose/time effect | Figure | R&T p.365 | OMITTED_PROBLEMATIC | MISSING_BRIDGE | Add if emphasizing observation-vs-parameter variability. |
| Describing Variability | H3 | R&T p.366–368 | INCLUDED_AS_MUST | None | Preserve mean vs shape message. |
| Fig.12-6 unimodal/bimodal | Figure | R&T p.366 | INCLUDED_AS_MUST | None | Preserve. |
| Fig.12-7 bioavailability CV | Figure | R&T p.367 | OMITTED_JUSTIFIABLE | Low-priority example | None. |
| Fig.12-8 averaging distortion | Figure | R&T p.367–368 | INCLUDED_AS_CONTEXT | None | Preserve with NAD/NPD. |
| Population Analysis | H2 | R&T p.369–373 | INCLUDED_AS_MUST | None | Core. |
| Fig.12-9 CrCl covariate | Figure | R&T p.369 | INCLUDED_AS_MUST | None | Core. |
| Fig.12-10 ω² clearance distribution | Figure | R&T p.370 | INCLUDED_AS_MUST | None | Core. |
| Fig.12-11 renal clearance model | Figure | R&T p.370 | INCLUDED_AS_CONTEXT | None | Preserve if not too detailed. |
| Fig.12-12 variance distributions | Figure | R&T p.371 | INCLUDED_AS_MUST | None | Core residual/IIV model. |
| Fig.12-13 residual variance | Figure | R&T p.372 | INCLUDED_AS_MUST | None | Core. |
| Fig.12-14 residual variability | Figure | R&T p.372 | INCLUDED_AS_MUST | None | Core. |
| Maximum Likelihood Approach | H2 | R&T p.373 | INCLUDED_AS_CONTEXT | None | Preserve; avoid over-regulatory extrapolation. |
| Why People Differ | H2 | R&T p.373–374 | INCLUDED_AS_CONTEXT | None | Preserve. |
| Table 12-1 additional factors | Table | R&T p.374 | INCLUDED_AS_CONTEXT | None | Preserve as context. |
| Fig.12-15 nonadherence | Figure | R&T p.375 | INCLUDED_AS_CONTEXT | None | Optional. |
| Fig.12-16 St. John’s wort | Figure | R&T p.376 | INCLUDED_AS_CONTEXT | None | Optional. |
| Fig.12-17 grapefruit juice | Figure | R&T p.377 | OMITTED_JUSTIFIABLE | Low-priority example | No action. |
| Defining the Dose-Response Relationship | H2 | R&T p.379–381 | OMITTED_PROBLEMATIC | MISSING_BRIDGE | Consider PK-vs-PD variability sentence only. |
| Therapeutic Exposure | H2 | R&T p.381–383 | OMITTED_JUSTIFIABLE | Outside core | Optional. |
| Kinetic Manifestations | H2 | R&T p.384–386 | OMITTED_JUSTIFIABLE | Outside core | Optional. |
| Dynamic Manifestations | H2 | R&T p.386–388 | INCLUDED_AS_CONTEXT | None | Preserve warfarin/genotype if used. |
| Dose Strengths | H2 | R&T p.388–390 | OMITTED_JUSTIFIABLE | Dose design not central | Optional. |
| Ch.12 Study Problems/Tables 12-2–12-4 | Study problems/tables | R&T p.390–392 | OMITTED_JUSTIFIABLE | Exercises | No action. |
| R&T Ch.13 objectives/opening | Objectives/key message | R&T p.393 | INCLUDED_AS_MUST | None | Preserve inheritance lifelong message. |
| Fig.13-1 twin study | Figure | R&T p.394 | OMITTED_PROBLEMATIC | MISSING_EXAMPLE | Add as brief evidence for genetic contribution if C4 refined. |
| Table 13-1 genetic polymorphism frequencies | Table | R&T p.395 | INCLUDED_AS_MUST | None | Preserve exact values. |
| Ethnicity caution | Repeated author caution | R&T p.395 | OMITTED_PROBLEMATIC | MISSING_AUTHOR_MSG | Add 1 sentence; prevents proxy overclaim. |
| Table 13-2 PD polymorphisms | Table | R&T p.396 | INCLUDED_AS_CONTEXT | None | Preserve. |
| Inherited variation in pharmacokinetics | H2 | R&T p.395–404 | INCLUDED_AS_MUST | None | Core C4. |
| Fig.13-2 nortriptyline CYP2D6 gene copies | Figure | R&T p.397 | INCLUDED_AS_MUST | None | Core C4. |
| Fig.13-3 metoprolol CYP2D6 | Figure | R&T p.397 | INCLUDED_AS_MUST | None | Preserve. |
| Fig.13-4 warfarin CYP2C9 | Figure | R&T p.398 | INCLUDED_AS_MUST | None | Preserve exact or qualitative. |
| Fig.13-5 TPMT thiopurine | Figure | R&T p.400 | INCLUDED_AS_MUST | None | Preserve. |
| Fig.13-6 NAT2 isoniazid | Figure | R&T p.402 | INCLUDED_AS_MUST | None | Preserve. |
| Table 13-3 acetylator distribution | Table | R&T p.403 | INCLUDED_AS_CONTEXT | None | Preserve if Hardy-Weinberg used. |
| Table 13-4 drug/metabolite consequences | Table | R&T p.404 | OMITTED_PROBLEMATIC | MISSING_EXAMPLE | Optional but useful for codeine/prodrug logic. |
| Inherited variability in pharmacodynamics | H2 | R&T p.405–406 | INCLUDED_AS_CONTEXT | None | Preserve. |
| Fig.13-7 G6PD/primaquine | Figure | R&T p.405 | OMITTED_PROBLEMATIC | MISSING_EXAMPLE | Optional if PD genetics table strengthened. |
| Fig.13-8 VKORC1 warfarin | Figure | R&T p.406 | INCLUDED_AS_MUST | None | Verify exact percentages. |
| Metabolic Phenotyping | H2 | R&T p.407 | INCLUDED_AS_CONTEXT | None | Preserve. |
| Pharmacogenetics-Based Therapeutic Recommendations | H2 | R&T p.407–408 | INCLUDED_AS_CONTEXT | None | Preserve with source-boundary caution. |
| Fig.13-9 PGDx dose adjustments | Figure | R&T p.408 | INCLUDED_AS_CONTEXT | None | Use only as pointer; avoid current label counts. |
| Ch.13 closing: pharmacogenetics potential but not fully leveraged; other factors matter | Author concluding message | R&T p.409 | OMITTED_PROBLEMATIC | MISSING_AUTHOR_MSG | Add as guardrail. |
| Study Problems/Table13-5 beta-blocker CYP2D6 | Study/table | R&T p.409 | OMITTED_JUSTIFIABLE | Exercise | No action. |

---

## T6: Figure Inventory & Learning Value Audit

Inspection note: page images were rendered as contact sheets and visually inspected for layout/content. Figures/tables whose details are too small on the contact sheet were cross-checked against captions and surrounding text. `VISUAL_INSPECTED` below means visual page inspection was performed; exact small-font numeric transcription may still require direct page zoom before Phase 4C.

| Figure/Table | Page | Teaches | Value | View Instruction? | Redraw/New Schematic? | Inspection Method | Rationale |
|---|---:|---|---|---|---|---|---|
| Fig.4.1 | G&W 333 | Modeling carousel from tentative model → design → experiment → explore → fit → analyze. | USEFUL | NO | YES | VISUAL_INSPECTED | Helpful workflow frame but not central to IIV/covariate. |
| Fig.4.2 | G&W 336 | Spaghetti plot reveals two population groups after same dose. | ESSENTIAL | YES | NO | VISUAL_INSPECTED | Direct visual anchor for subgroup/covariate hypothesis generation. |
| Fig.4.3 | G&W 337 | Linear vs log concentration plots reveal model misfit differently. | USEFUL | NO | NO | VISUAL_INSPECTED | Useful diagnostic bridge but not central. |
| Fig.4.4 | G&W 338 | One-, two-, three-compartment fits to IV bolus data. | SKIPPABLE | NO | NO | VISUAL_INSPECTED | Structural model selection, not core variance session. |
| Fig.4.5 | G&W 339 | Extravascular two-compartment phases. | SKIPPABLE | NO | NO | VISUAL_INSPECTED | Outside core. |
| Fig.4.6 | G&W 340 | Lineweaver-Burke transformation distorts error. | USEFUL | NO | NO | VISUAL_INSPECTED | Useful for error-transformation concept but excluded by scope. |
| Fig.4.7 | G&W 341 | Nonlinear kinetics and dose-normalization differences. | USEFUL | NO | NO | VISUAL_INSPECTED | Optional nonlinear-kinetics bridge. |
| Fig.4.8 | G&W 343 | One-compartment first-order model schematic. | SKIPPABLE | NO | NO | VISUAL_INSPECTED | Basic structural model; not needed. |
| Fig.4.9 | G&W 344 | Linear/semi-log one-compartment profiles and urine plots. | SKIPPABLE | NO | NO | VISUAL_INSPECTED | Basic structural model. |
| Fig.4.10 | G&W 344 | Integrated vs differential model representation. | SKIPPABLE | NO | NO | VISUAL_INSPECTED | Estimation-method topic, not core. |
| Fig.4.11 | G&W 345 | Common PK profiles and differential equations. | SKIPPABLE | NO | NO | VISUAL_INSPECTED | Too broad for current session. |
| Fig.4.12 | G&W 346 | More model structures including MM and absorption. | SKIPPABLE | NO | NO | VISUAL_INSPECTED | Too broad for current session. |
| Table 4.1 | G&W 347 | Simultaneous modeling data sources/parameters/examples. | USEFUL | NO | YES | VISUAL_INSPECTED | Useful for identifiability; dense table may need simplified schematic if used. |
| Fig.4.13 | G&W 348 | Identifiability/nonidentifiability with model/data relationships. | USEFUL | NO | YES | VISUAL_INSPECTED | Helpful context for overparameterization. |
| Table 4.2 | G&W 349 | Identifiable, nonidentifiable, nonobservable parameter properties. | USEFUL | NO | NO | VISUAL_INSPECTED | Useful as context. |
| Fig.4.14 | G&W 349 | Four identifiability problem situations. | USEFUL | NO | YES | VISUAL_INSPECTED | Complex; a simplified schematic would aid learners. |
| Fig.4.15 | G&W 351 | Emax fit and estimability issue. | USEFUL | NO | NO | VISUAL_INSPECTED | Optional. |
| Fig.4.16 | G&W 352 | EDA as transition from model to plot. | USEFUL | NO | YES | VISUAL_INSPECTED | Good workflow frame; optional. |
| Fig.50.1 | G&W 705 | CpD total vs unbound concentration-time profiles in 12 subjects. | ESSENTIAL | YES | YES | VISUAL_INSPECTED | Core PK50 visual; redraw may improve total/unbound variability contrast. |
| Fig.50.2 | G&W 707 | Similar exposure but large response variability; responder/nonresponder signal. | ESSENTIAL | YES | YES | VISUAL_INSPECTED | Core PK vs PD covariate distinction. |
| Table 50.1 | G&W 708 | Total vs unbound PK parameter estimates and CVs. | ESSENTIAL | YES | NO | VISUAL_INSPECTED | Core numerical anchor. |
| Table 50.2 | G&W 708 | Total vs unbound PD parameter estimates and CVs. | ESSENTIAL | YES | NO | VISUAL_INSPECTED | Core EC50 paradox anchor. |
| Table 50.3 | G&W 710 | Individual PK estimates and `fu` values. | USEFUL | NO | NO | VISUAL_INSPECTED | Useful for detailed validation but not required in main card. |
| Fig.12-1 | R&T 362 | Warfarin dose requirement varies widely in 200 adults. | ESSENTIAL | YES | NO | VISUAL_INSPECTED | Strong opening anchor for individualization. |
| Fig.12-2 | R&T 363 | Nortriptyline plateau concentration is skewed on linear scale and log-normal on log scale. | ESSENTIAL | YES | NO | VISUAL_INSPECTED | Core for log-normal IIV. |
| Fig.12-3 | R&T 364 | Midazolam/alfentanil exposure cosegregates via CYP3A4 activity. | USEFUL | NO | NO | VISUAL_INSPECTED | Useful enzyme-activity variability example. |
| Fig.12-4 | R&T 364 | S-warfarin unbound concentration needed for same anticoagulation varies. | USEFUL | NO | NO | VISUAL_INSPECTED | Good PD variability anchor. |
| Fig.12-5 | R&T 365 | Variability in concentration/response depends on dose and time of observation. | USEFUL | NO | YES | VISUAL_INSPECTED | Complex but conceptually useful. |
| Fig.12-6 | R&T 366 | Mean, CV, and distribution shape; unimodal vs bimodal. | ESSENTIAL | YES | YES | VISUAL_INSPECTED | Core for “mean not enough” and polymodal substructure. |
| Fig.12-7 | R&T 367 | Bioavailability variability increases as bioavailability decreases. | USEFUL | NO | NO | VISUAL_INSPECTED | Optional. |
| Fig.12-8 | R&T 368 | Averaging individual profiles distorts reality. | USEFUL | YES | YES | VISUAL_INSPECTED | Direct support for NAD/NPD caution. |
| Fig.12-9 | R&T 369 | CrCl covariate affects total clearance and concentration profiles. | ESSENTIAL | YES | YES | VISUAL_INSPECTED | Core covariate model visual. |
| Fig.12-10 | R&T 370 | Small vs large ω² relative to therapeutic window. | ESSENTIAL | YES | YES | VISUAL_INSPECTED | Core IIV clinical consequence visual. |
| Fig.12-11 | R&T 370 | Individual renal clearance deviation from population prediction. | USEFUL | NO | YES | VISUAL_INSPECTED | Useful but can be simplified. |
| Fig.12-12 | R&T 371 | Homoscedastic vs heteroscedastic parameter variability. | ESSENTIAL | YES | YES | VISUAL_INSPECTED | Core additive/proportional/exponential variability model. |
| Fig.12-13 | R&T 372 | Residual variance should be random with mean zero and variance σ². | ESSENTIAL | YES | NO | VISUAL_INSPECTED | Core residual variance message. |
| Fig.12-14 | R&T 372 | Residual variability is leftover difference between observation and individual prediction. | ESSENTIAL | YES | YES | VISUAL_INSPECTED | Core ε concept. |
| Table 12-1 | R&T 374 | Additional variability sources: adherence, route, food, herbs, pollutants, time/season. | USEFUL | NO | NO | VISUAL_INSPECTED | Context list. |
| Fig.12-15 | R&T 375 | Nonadherence patterns. | USEFUL | NO | NO | VISUAL_INSPECTED | Context only. |
| Fig.12-16 | R&T 376 | St. John’s wort changes midazolam/fexofenadine exposure. | USEFUL | NO | NO | VISUAL_INSPECTED | Context only. |
| Fig.12-17 | R&T 377 | Grapefruit juice inhibitor content variability. | SKIPPABLE | NO | NO | VISUAL_INSPECTED | Too specific. |
| Fig.12-18 | R&T 378 | Chronotherapy changes response/adverse effects. | USEFUL | NO | NO | VISUAL_INSPECTED | Context only. |
| Fig.12-19 | R&T 379 | Dose-response trial design with placebo/10/20 mg. | USEFUL | NO | YES | VISUAL_INSPECTED | Optional for population response variability. |
| Fig.12-20 | R&T 380–381 | Exposure-response utility depends on PD variability and therapeutic window. | USEFUL | NO | YES | VISUAL_INSPECTED | Optional; complex. |
| Fig.12-21 | R&T 382 | Theophylline profiles in five subjects. | USEFUL | NO | NO | VISUAL_INSPECTED | Optional kinetic example. |
| Fig.12-22 | R&T 383 | Propranolol profiles in five subjects IV/PO. | USEFUL | NO | NO | VISUAL_INSPECTED | Optional kinetic example. |
| Fig.12-23 | R&T 384 | Low vs high extraction impact of intrinsic clearance variability. | USEFUL | NO | YES | VISUAL_INSPECTED | Optional, belongs to clearance session. |
| Fig.12-24 | R&T 386 | Warfarin PK/PD genotype simulation by VKORC1/CYP2C9. | ESSENTIAL | YES | YES | VISUAL_INSPECTED | Core pharmacogenetic variability anchor if exact percentages are used. |
| Fig.12-25 | R&T 387 | Voriconazole PTA by CYP2C19 genotype. | USEFUL | NO | NO | VISUAL_INSPECTED | Useful genotype-to-target example. |
| Fig.12-26 | R&T 389 | Dose strengths as discrete coverage of population variability. | USEFUL | NO | YES | VISUAL_INSPECTED | Optional; dose design bridge. |
| Table 12-2 | R&T 390 | Study problem infusion observations in five subjects. | SKIPPABLE | NO | NO | VISUAL_INSPECTED | Exercise table. |
| Table 12-3 | R&T 390 | Study problem unbound Css/CL/V. | SKIPPABLE | NO | NO | VISUAL_INSPECTED | Exercise table. |
| Table 12-4 | R&T 391 | Study problem CV of measures and parameters. | SKIPPABLE | NO | NO | VISUAL_INSPECTED | Exercise table. |
| Fig.12-27 | R&T 392 | Propofol concentration-response variability. | USEFUL | NO | NO | VISUAL_INSPECTED | Optional PD variability example. |
| Fig.13-1 | R&T 394 | Identical vs fraternal twins show genetic role in nortriptyline PK. | USEFUL | YES | NO | VISUAL_INSPECTED | Good evidence figure for genetics. |
| Table 13-1 | R&T 395 | Frequencies of genetic polymorphisms producing slow metabolism. | ESSENTIAL | YES | NO | VISUAL_INSPECTED | Core exact frequency source. |
| Table 13-2 | R&T 396 | Genetic polymorphisms in pharmacodynamics. | ESSENTIAL | YES | NO | VISUAL_INSPECTED | Core for PD genetics. |
| Fig.13-2 | R&T 397 | Nortriptyline exposure decreases as functional CYP2D6 copies increase. | ESSENTIAL | YES | NO | VISUAL_INSPECTED | Core C4 example. |
| Fig.13-3 | R&T 397 | Metoprolol exposure differs in CYP2D6 poor vs extensive metabolizers. | USEFUL | YES | NO | VISUAL_INSPECTED | Useful supporting example. |
| Fig.13-4 | R&T 398 | CYP2C9 genotype affects S-warfarin clearance and maintenance dose. | ESSENTIAL | YES | NO | VISUAL_INSPECTED | Core warfarin pharmacogenetic example. |
| Fig.13-5 | R&T 400 | TPMT genotype-guided dosing avoids thiopurine toxicity. | ESSENTIAL | YES | YES | VISUAL_INSPECTED | Core actionable-genotype example. |
| Fig.13-6 | R&T 402 | Isoniazid 6-h concentration shows bimodal acetylator distribution. | ESSENTIAL | YES | NO | VISUAL_INSPECTED | Core polymodal distribution example. |
| Table 13-3 | R&T 403 | Isoniazid acetylator distribution by population and Hardy-Weinberg calculation. | USEFUL | NO | NO | VISUAL_INSPECTED | Supports Hardy-Weinberg context. |
| Table 13-4 | R&T 404 | Consequences of polymorphism depending on drug/metabolite activity. | USEFUL | NO | YES | VISUAL_INSPECTED | Useful but omitted. |
| Fig.13-7 | R&T 405 | G6PD/primaquine pharmacodynamic genetic variability. | USEFUL | NO | NO | VISUAL_INSPECTED | Optional PD genetic example. |
| Fig.13-8 | R&T 406 | Genetic and non-genetic contributions to warfarin dose variance. | ESSENTIAL | YES | NO | VISUAL_INSPECTED | Core if explaining incomplete genotype prediction. |
| Fig.13-9 | R&T 408 | Examples of PGDx-based dose adjustment factors. | USEFUL | NO | YES | VISUAL_INSPECTED | Good final pointer; complex. |
| Table 13-5 | R&T 409 | Study problem beta-blocker PK parameters and CYP2D6 correlation. | SKIPPABLE | NO | NO | VISUAL_INSPECTED | Exercise table. |

---

## Patch Memo Item Classification

| Memo Item | Audit Classification | Rationale |
|---|---|---|
| 4 MUST structure is generally good | MATCH | PDF scope supports C1 variability/population analysis, C2 residual error, C3 covariates, C4 genetics. |
| PK50 anchor is strong | MATCH | G&W PK50 directly supports total/unbound parameter comparison and PD response variability. |
| R&T Ch.12 key messages included | MATCH | Draft captures population analysis and residual error, but should strengthen plot-first/mean-shape messages. |
| C2 “Residual Error + Shrinkage” Apex risky | MATCH | Residual error is source-supported; shrinkage is not in source. |
| NONMEM code needs source-boundary label | MATCH | Code blocks are external implementation translation. |
| “fu covariate 28%→9%” overstates source | MATCH | Correct audit finding. |
| Deficiency Letter / CFR / costs unsupported | MATCH | Not in source. |
| Mixed RUV “default” should be lowered | MATCH | Not directly supported. |
| Genetic polymorphism numerical claims need source check | MATCH | Some supported, some not. Exact percentages/fold claims must be restricted to PDF. |
| G&W Ch.4 EDA message should be strengthened | MATCH | Source gives strong plot-first/spaghetti messages. |

---

## Minimal Phase-2 Patch List

1. Reclassify C2 as **Residual Error Models**; move shrinkage content to `[교과서 외 후속 구현 지식]` or remove from Step 1 source-locked body.
2. Add source-boundary labels to all NONMEM code blocks: `[교과서 외 구현 번역]`.
3. Replace “fu covariate reduces ω²(CL) 28%→9%” with source-exact statement: **PK50 reports total Cl CV 28% and unbound Clu CV 9% after deriving unbound parameters using fu**.
4. Remove the variance propagation “validation” claim or mark as failed/unsupported.
5. Delete or label all FDA/21 CFR/deficiency-letter/time/cost claims as external scenario content.
6. Re-check and source-lock all pharmacogenetic ratios/percentages. Keep Table 13-1 values exactly; avoid unverified IM/EM/UM frequency values.
7. Add one short author-message bridge from G&W Ch.4: **plot first; spaghetti plot reveals variability before equations**.
8. Add one short R&T Ch.13 caution: **ethnicity is a proxy; individual genetic characteristics matter more than demographic labels**.

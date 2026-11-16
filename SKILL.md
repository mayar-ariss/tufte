---
name: tufte
description: >-
  Use when creating, reviewing or styling figures for scientific articles,
  preprints, theses, conference papers and their supplementary material:
  plots, multi-panel figures, small multiples, maps and schematic diagrams.
  Applies Edward Tufte's principles (show the data, graphical integrity,
  comparison, causality, data density, layering, direct annotation) to
  scientific figures, together with the statistics literature on showing
  uncertainty and the production requirements of journals (Nature, Science,
  PLOS). Covers matplotlib, seaborn, ggplot2 and plotnine.
allowed-tools: Read, Glob, Grep
---

# Tufte: figures for scientific articles

Apply these rules whenever you generate or review code that draws a figure for a scientific article, preprint, thesis, conference paper or supplementary material. This skill is not for dashboards, web pages or slides.

Tufte wrote about printed evidence, and many of his central examples are scientific: Snow's cholera map, Minard's map of the Russian campaign, the Challenger O-ring data. His vision is the core of this skill. A scientific figure is a display of evidence: it shows the data, makes the comparison and the cause visible, carries as much information as the reader can use, and explains itself on the page.

The skill is in three parts, in order of authority:

1. **Tufte's principles** (rules 1–14). The design of the figure.
2. **Scientific evidence** (rules 15–19). What the statistics literature adds where Tufte gives no rule: distributions, uncertainty, p-values, log scales. These extend Tufte; none contradicts him.
3. **Journal production** (rules 20–25). Size, typeface, caption, line weights, panel letters, file format. These change how a figure is produced, not how it is designed.

When a production requirement and a Tufte principle seem to conflict, meet the requirement in the way that loses the least of the principle. Every departure from Tufte is named where it occurs, with its reason, and listed under "Departures from Tufte" at the end.

**Diagrams and schematics:** read `rules/diagrams-flowcharts.md`. **Maps:** also read `rules/maps.md`.

## Workflow

1. **Find the evidence.** What must the reader see, compared with what, and caused by what? Use only comparisons and explanatory variables that exist in the data or that the user supplies; never invent a target, baseline or reference value.
2. **Design by Part I.** Choose the form that shows the data, the comparison and the cause, with as much detail as the reader can use, layered so it stays readable.
3. **Add the evidence Part II asks for**: every observation where feasible, uncertainty defined, *n* stated.
4. **Produce by Part III** for the target journal (`rules/journals.md`). If none is named, 89 mm (single column) or 183 mm (double column) in 5–7 pt Helvetica suits most journals.
5. **Respect an existing figure style.** If the user's project already has one (a matplotlibrc, a ggplot2 theme, a lab template, earlier figures in the paper), keep its look and apply Parts I and II to the content. Apply the full style only when asked or when there is none.
6. **Library setup:** read ONE of `rules/matplotlib.md` or `rules/ggplot2-plotnine.md`.
7. **Write the caption** (rule 22) and check every claim in it against the data. **Validate** with the checklist at the end.

## Sources

Every rule names its source:

- **Tufte** — stated in Tufte's books, cited by book and chapter: *VDQI* = *The Visual Display of Quantitative Information* (1983; 2nd ed. 2001), *EI* = *Envisioning Information* (1990), *VE* = *Visual Explanations* (1997), *BE* = *Beautiful Evidence* (2006). His fifth book, *Seeing with Fresh Eyes* (2020), is not drawn on here.
- **Literature** — a published recommendation from statistics or visualization research, cited by author and year; full references in `rules/references.md`.
- **Journal** — a requirement in a journal's author guidelines, quoted with its date in `rules/journals.md`. The target journal's current guide wins.
- **Convention** — common practice stated by none of the above. Specific values (hex colors, point sizes, opacities) are this skill's defaults.
- **Extension** — added by this skill's authors (for example the contrast minimums).

Where none of these gives a rule, the rule says so instead of supplying one.

## Tufte's foundations

**Graphical integrity** (VDQI ch. 2). (1) Numbers as physically measured on the graphic are directly proportional to the quantities they represent; the *lie factor*, the size of the effect shown divided by the size of the effect in the data, should be 1. (2) Clear, detailed and thorough labeling defeats distortion and ambiguity: write out explanations of the data on the graphic itself and label important events in the data. (3) Show data variation, not design variation. (4) Deflate money in time series. (5) The number of information-carrying dimensions does not exceed the number of dimensions in the data. (6) Graphics must not quote data out of context.

**Data-ink** (VDQI ch. 4–5). Above all else show the data. Maximize the data-ink ratio, erase non-data-ink and redundant data-ink — each *within reason*, his qualifier. Revise and edit. Chartjunk has three forms: moiré vibration, the dark grid, and the "duck", decoration that takes over the data.

**Graphical excellence** (VDQI ch. 1) gives the viewer the greatest number of ideas in the shortest time with the least ink in the smallest space. Erasing is half of it. The other half is richness: high data density (VDQI ch. 8), multifunctioning elements (VDQI ch. 7), micro/macro readings (EI ch. 2), layering and separation (EI ch. 3), and words and data together (VDQI ch. 9). "To clarify, add detail" (EI ch. 2). A sparse figure is not a Tufte figure; a dense, clear one is.

**Analytical design** (BE ch. 5): show comparisons; show causality, mechanism and explanation; show multivariate data; integrate words, numbers and images; document the evidence; content counts most of all.

---

## Part I — Tufte's principles

### 1. Above all else, show the data

*Source: Tufte, VDQI ch. 4; VDQI ch. 1 (graphical excellence).*

Show the observations themselves, not only summaries of them, wherever their number allows: every measurement, every subject, every site. A summary drawn over the data is better than a summary instead of the data. Rule 15 says how for distributions.

### 2. Keep graphical integrity

*Source: Tufte, VDQI ch. 2 (principles 1, 3, 5, 6). Bars from zero: this skill's application of principle 1 (convention).*

- Lengths and areas proportional to the values. A bar's length is proportional to its value only from zero, so bars and areas start at zero. Lines and dots encode by position and take a scale that shows the data; Tufte prescribes no zero baseline for them.
- No perspective, depth or shadows: two-dimensional data get two dimensions.
- The same design across panels and figures, so that every difference the reader sees is a difference in the data (principle 3).
- The data in context: the whole series, the whole map, the cases where nothing happened (rule 4).

### 3. Show comparisons: "Compared to what?"

*Source: Tufte, EI ch. 4, p. 67 ("Compared to what?"); BE ch. 5 (first principle); VDQI ch. 2 (principle 6).*

Every figure answers "compared to what?" on the page: a control, a reference condition, a baseline period, another group, a published value the user supplies. Put the things compared side by side, on the same scale, within one eyespan. Never add a reference, target or "expected" value that is not in the data or given by the user.

### 4. Show causality and mechanism

*Source: Tufte, VE ch. 2 (the cholera map and the Challenger O-ring data); BE ch. 5 (second principle).*

The lesson of VE ch. 2: the evidence about the Challenger's O-rings was displayed so that its cause could not be seen. Plot the outcome against the variable that may explain it, order the evidence by that variable, and include every case — including those where nothing happened, which are the comparison that makes the cause visible.

- Put the explanatory variable on an axis (dose, temperature, time since treatment, distance to the source), not in a legend or a panel order.
- Order categories by the explanatory variable or by the outcome, never alphabetically by default (VDQI ch. 9, p. 178).
- Plot the zeros, the non-responders and the controls with the cases.
- Put the suspected cause on the same figure as the effect, as Snow put the pumps on the map of deaths.

### 5. Show multivariate data; use small multiples

*Source: Tufte, BE ch. 5 (third principle); EI ch. 4 (small multiples).*

Show more than one or two variables when the evidence has them. Small multiples are Tufte's main device: one design repeated, one scale in every panel, panels close together and ordered by something meaningful, so the eye compares the data rather than the graphics. Prefer small multiples to stacked bars, dual axes or more than four colors in one panel. See `rules/small-multiples-and-panels.md`.

### 6. Put the explanation on the graphic, generously

*Source: Tufte, VDQI ch. 2 (principle 2: "write out explanations of the data on the graphic itself; label important events in the data"); VDQI ch. 9 (words and pictures together); BE ch. 5 (fourth principle); EI ch. 2 ("to clarify, add detail").*

Words, numbers and data belong together. Write onto the figure what the reader needs to read it without the caption: the name of each group and series, the values that matter (an EC₅₀, a peak, a difference, *n*), events and interventions, thresholds, the meaning of an unusual mark. Place each annotation beside what it explains, in the nearest clear space, with a short thin leader line if needed. Do not ration annotation for the sake of a clean look; keep the figure readable by layering (rule 11), not by leaving information out. "Confusion and clutter are failures of design, not attributes of information" (EI p. 51).

### 7. Label directly; a key only for a scale

*Source: Tufte — in the friendly data graphic "labels are placed on the graphic itself; no legend is required", VDQI ch. 9 (p. 183).*

Label each series where it is, at the end of a line or beside a cluster, and turn the legend off. A key stays only for an encoding that cannot carry its own label, such as a color scale for a quantity; show it beside the data, unframed. Tufte does not ban keys: his redrawn cancer maps carry one (VDQI pp. 16–20).

### 8. Maximize data density, within reason

*Source: Tufte, VDQI ch. 8 (data density, the shrink principle); VDQI ch. 7 (multifunctioning graphical elements).*

- Carry as much data per square centimeter as the reader can use. Tufte's shrink principle — most graphics can be shrunk well below their usual size — suits a journal column.
- Let one element do several jobs: an axis that reports the data's range (rule 10), a label that is also a value, a reference line that is also the comparison.
- Use space for data, not for margins, boxes and repeated labels. Science asks the same: "maximize the space given to presentation of the data" (Journal, Science).

### 9. Erase non-data-ink and redundant ink, within reason

*Source: Tufte, VDQI ch. 4 (data-ink), ch. 5 (chartjunk), ch. 6 (erasing the frame).*

No box around the plot, no top or right spines, no background fill, no heavy grid, no hatching, no decoration. Where readers must read values precisely, a light grid is acceptable (Tufte: "muted or suppressed", VDQI ch. 5); a table may serve better. Erase what carries no information about the data, never what does: erasing is subordinate to rules 1 and 6.

### 10. Range-frame axes that report the data

*Source: Tufte, the range-frame, VDQI ch. 6; multifunctioning elements, VDQI ch. 7. Labeling the ends: this skill's application (convention).*

Each axis line spans only the range of the data, so the frame itself reports the minimum and maximum. Where it helps, label the ends of the range frame with the data's extreme values. For bars, the value axis runs from zero (rule 2).

### 11. Layer and separate; design for two readings

*Source: Tufte, EI ch. 3 (layering and separation; "1 + 1 = 3 or more"); EI ch. 2 (micro/macro readings).*

A dense figure stays clear when its layers are visually ordered: data darkest and heaviest; summaries and fits next; comparisons and references lighter; axes, grids and leader lines lightest and thinnest. Two heavy lines close together create a third, illusory element (1 + 1 = 3); separate by lightness, weight and space instead. Design for two readings: the overall pattern at a glance (the macro reading) and every individual value up close (the micro reading) — for example, each subject's trajectory as a thin light line under the group mean.

### 12. Color: last, gray first, strong color only in small areas, the smallest effective difference

*Source: Tufte, EI ch. 5 (color: "above all, do no harm"; muted fields with strong color in small areas, and no bright colors side by side over large areas, after Imhof; color as quantity, light to dark); VE ch. 4 (smallest effective difference); VDQI ch. 9, p. 183 (colors that color-deficient readers can tell apart). Palette and maps: Literature (Okabe and Ito 2008; Wong 2011; Crameri et al. 2020).*

- **Color last.** Separate categories first by position, direct labels or small multiples (rules 5 and 7); use color only for what those cannot do.
- **Gray first.** Draw everything in gray; give color only to what the reader must find. Make every difference as small as will still read clearly.
- **One highlight by default:** Okabe–Ito blue `#0072B2` against grays. Add vermillion `#D55E00`, then bluish green `#009E73` and reddish purple `#CC79A7`, only when the reader must tell highlighted things apart. More than four categories go to small multiples.
- **Strong color only in small areas:** lines, dots, labels, small marks. Large areas (fills, wide bars, map regions, backgrounds) take light gray or a pale tint of one hue, stepped light to dark when they encode a quantity. Never strong or bright colors side by side over large areas.
- Okabe–Ito is kept for what Tufte asks on VDQI p. 183, colors that color-deficient readers can tell apart; muting its hues would undo that, so the rule limits where they go instead.
- For quantities, light to dark in one hue, or a perceptually uniform map (viridis, cividis, batlow; vik for diverging data). Never rainbow or jet.
- Never red against green for a contrast that matters. Same condition, same color in every figure of the paper. The figure must read in grayscale.

Hex values and contrast ratios: `rules/typography-and-color.md`.

### 13. Type: clear, precise, modest; words spelled out and running horizontally

*Source: Tufte, the friendly data graphic, VDQI ch. 9, p. 183.*

Upper-and-lower case, never all caps; words spelled out where space allows, not abbreviations and codes; type running horizontally — set the y-axis label horizontally at the top of the axis, and rotate it only when the panel is too narrow. Type that is clear, precise and modest. Tufte sets data graphics in serif type; journals require a sans serif, so the typeface itself is a production matter (rule 21).

### 14. Choose the form the evidence needs

*Source: Tufte — pie charts, sentences and tables, aspect ratio, VDQI ch. 9; banking to 45°, BE ch. 2 (after Cleveland). Dual axes: convention; the alternative is Tufte's small multiples (EI ch. 4).*

- One or two numbers belong in a sentence; many small data sets and exact values belong in a table; graphics earn their space where they reveal patterns, trends and distributions.
- No pie charts: a dot plot or bar chart sorted by value, or a table. If the user still asks for one after this is explained, follow the request.
- No dual y-axes: two panels stacked on a shared x-axis.
- Shape: about 1.5 times wider than tall unless the data suggest another; for lines whose slopes matter, choose the shape so the slopes average about 45°.

---

## Part II — Scientific evidence

Tufte gives no rule for error bars, significance tests or log scales. These rules come from the statistics and visualization literature. They extend Part I: each serves "show the data" and "document the evidence".

### 15. Show the distribution, then the summary

*Source: Literature (Weissgerber et al. 2015; Krzywinski and Altman 2014); serves Tufte's rule 1.*

For continuous data in small samples, plot every observation (a strip, jittered or beeswarm plot) with the summary on top. Never a bar of the mean with an error bar ("dynamite plot"): many different distributions give the same bar. Bars are for counts and proportions. For larger samples, Tufte's quartile plot (VDQI ch. 6) or a box plot with the points behind it; box plots need at least five observations. For paired or repeated measures, connect each subject's values (Tufte's slopegraph, VDQI pp. 158–159).

### 16. Show uncertainty, and say which uncertainty

*Source: Literature (Cumming et al. 2007; Vaux 2012; Krzywinski and Altman 2013).*

- Say what every bar or band shows: SD, SEM or a 95% confidence interval. The same bar means different things in each case.
- SD to describe spread; a 95% confidence interval to support a comparison; label SEM as SEM.
- With two or three independent observations, plot the points instead of error bars or p-values.
- Error bars belong to independent replicates, not technical replicates.
- Draw intervals thin (0.5 pt) and without caps, and bands light, so the data stay the darkest layer (rule 11).

### 17. Estimates first; define every significance mark

*Source: Literature (Wasserstein and Lazar 2016); convention for the marks.*

A p-value does not measure the size of an effect. Show the effect and its interval, and write the estimate on the figure where it helps (rule 6); give exact p-values in the caption or text. If asterisks or brackets are used, define each in the caption and draw brackets thin and gray.

### 18. Log scales for multiplicative data

*Source: Literature (Cleveland 1994, ch. 3); Journal (Science, powers of 10).*

Use a log axis when values span orders of magnitude, or when ratios, fold changes or growth rates are the point. Base 2 for fold changes, base 10 for wide ranges. Label ticks with values (1, 10, 100 or 10⁰, 10¹, 10²), not logarithms. No bars on a log axis.

### 19. Each figure stands alone and agrees with the text

*Source: Tufte, BE ch. 5 ("content counts most of all"); convention.*

Every number on a figure matches the text and tables. A reader with only the figure and its caption can tell what was measured, in what units, on how many samples, and what the authors conclude.

---

## Part III — Journal production

These rules come from journals' author guidelines. They govern how a figure is produced. Where one departs from Tufte, the rule says so.

### 20. Draw at the final printed size, in millimeters

*Source: Journal (Nature, Science, PLOS).*

Set the figure width to the column it will occupy before drawing, so type and lines come out at their printed size; never scale an exported figure to fit. Nature: 89 mm (single column), 120–136 mm (1.5 columns), 183 mm (double column), at most 170 mm tall. Science: 5.7, 12.1 or 18.4 cm. PLOS: 6.68–19.05 cm wide, at most 22.23 cm tall.

### 21. Helvetica, at the journal's sizes

*Source: Journal (Science prefers Helvetica; Nature asks for Helvetica or Arial; PLOS lists Arial). **Departure from Tufte**, who sets data graphics in serif type (VDQI ch. 9, p. 183).*

Helvetica, with Arial as the fallback (Arial for PLOS); one font and one size scale across every figure in the paper. Nature: 5–7 pt, panel letters 8 pt bold. Science: about 7 pt, never below 5 pt. PLOS: 8–12 pt. Sentence case for labels (Journal, Science; a narrower form of Tufte's upper-and-lower case). Axis labels give the quantity, then its units in parentheses: "Concentration (µM)"; true minus sign (−), × and µ.

The departure is of typeface only: everything Tufte asks of type (rule 13) still holds, and his own books set tables in a sans serif, Gill Sans. See `rules/typography-and-color.md`.

### 22. The caption carries the title and the documentation; explanations stay on the graphic

*Source: Tufte, BE ch. 5 (fifth principle: document the evidence); Literature (Rougier et al. 2014, rule 4; Cumming et al. 2007); Journal (Freshwater Science: no title duplicating the caption). **Adaptation of Tufte**, who puts a detailed title on the graphic itself.*

- Journals put a figure's title in its caption, so: no title, figure number or source line inside the artwork.
- The caption's first sentence states the finding, and only what the data show. Check every number in it against the data.
- The caption then documents what the graphic cannot: what was measured and how, what the error bars show, *n* and what it counts, the test used, data sources. Sources, code and data availability go in Methods.
- The caption is not a substitute for annotation: labels, values, events and explanations belong on the graphic (rules 6 and 7).

### 23. Lines and marks that survive reduction

*Source: Journal (Nature: line weights 0.25–1 pt at final size); convention for the defaults, layered by rule 11.*

Data lines 1 pt; axes, ticks, error bars and leader lines 0.5 pt or lighter; markers about 3 pt. Nothing thinner than 0.25 pt.

### 24. Panel letters and layout

*Source: Journal (Nature, Science).*

Panel letters in the journal's style: Nature bold lowercase (a, b, c) at 8 pt; Science bold capitals (A, B, C) at 10 pt, top left, no sub-part labels. Set panels close together and label common axes once, on the outer edge (Journal, Science). Bold panel letters are a production mark, not a Tufte element.

### 25. Export vector graphics with embedded, editable fonts

*Source: Journal (Nature: AI, PostScript, vector EPS or PDF for graphs, "Please do not rasterize line art or text", photographs at 300 dpi or more; PLOS: TIFF or EPS at 300–600 dpi).*

PDF or EPS with fonts embedded as TrueType and kept as text. Raster only when the journal asks (TIFF at 600 dpi at final width). Check with `pdffonts figure.pdf`: every font `emb yes`.

---

## Chart types

These settings are this skill's defaults (convention), except where a cell names another source.

| Type | Key settings |
|---|---|
| **Strip / dot plot** | Every observation, jittered; mean or median with 95% CI beside the points; the groups labeled and the key values written in (rules 1, 6, 15, 16) |
| **Line** | 1 pt; markers where measurements were taken; direct labels; CI band light; individual trajectories as thin light lines under the mean when *n* is small enough (rule 11) |
| **Scatter** | Every point; highlight the group that matters; fitted line thin, with its band; rug marks for marginals (Tufte's dot-dash plot, VDQI ch. 6) |
| **Bar** | Counts and proportions only; zero baseline; sorted by value or by the explanatory variable (Tufte, VDQI ch. 9, p. 178) |
| **Quartile plot** | Tufte's redesign of the box plot (VDQI ch. 6): no box; a dot at the median, a gap for the middle half, lines to the extremes |
| **Paired data** | One line per subject between conditions (slopegraph: Tufte, VDQI pp. 158–159) |
| **Small multiples** | One design, one scale, panels close together and ordered meaningfully (Tufte, EI ch. 4) |
| **Heatmap** | Light to dark, or a perceptually uniform map; values in the cells when few; colorbar beside, unframed |
| **Dose–response, growth, concentration** | Explanatory variable on x, on a log axis labeled with values; key values (EC₅₀, plateau) marked and written on the curve |
| **Sparklines** | Word-sized, in tables or text; beginning and ending values beside the line; first and last values in red, low and high in blue (Tufte, BE pp. 50–51) |

Avoid: dynamite plots, pie charts, 3D, dual axes; stacked bars and area charts except for cumulative totals (convention: small multiples compare better).

## Journal quick reference

| | Nature | Science | PLOS |
|---|---|---|---|
| Widths | 89 / 120–136 / 183 mm | 5.7 / 12.1 / 18.4 cm | 6.68–19.05 cm |
| Typeface | Helvetica or Arial | Helvetica preferred | Arial |
| Text size | 5–7 pt | about 7 pt, ≥ 5 pt | 8–12 pt |
| Panel letters | 8 pt bold **a, b, c** | 10 pt bold **A, B, C** | journal style |
| Graphs | vector AI, EPS or PDF | vector preferred | TIFF or EPS, 300–600 dpi |

Quotes, sources and dates: `rules/journals.md`. Other journals: read their current guide.

## Library quick reference

| Library | Rule file | Essentials (apply even without reading the file) |
|---|---|---|
| matplotlib, seaborn | `rules/matplotlib.md` | `figsize` in mm/25.4; `font.sans-serif: ["Helvetica", "Arial", …]`; `font.size: 7`; spines top/right off; `axes.grid: False`; `pdf.fonttype: 42`; `savefig.bbox: "standard"` |
| ggplot2 (R) | `rules/ggplot2-plotnine.md` | `theme_classic(base_size = 7, base_family = "Helvetica")`; `legend.position = "none"`; `ggsave(width = 89, units = "mm", device = cairo_pdf)` |
| plotnine (Python) | `rules/ggplot2-plotnine.md` | `theme_classic(base_size=7, base_family="Helvetica")`; `legend_position="none"`; `p.save(width=89, units="mm")` |

## Anti-pattern detection

When reviewing a figure or its code, check for:

- **Against Tufte:** summaries without the data (→ show the observations); a comparison the reader must assemble across figures (→ side by side, same scale); the explanatory variable hidden in a legend or panel order (→ on an axis); missing zeros or non-responders (→ include them); categories in alphabetical order (→ order by value or cause); unlabeled series or values the reader must look up (→ write them on the graphic); a legend box (→ direct labels); a heavy frame, grid or decoration (→ erase); every element the same weight (→ layer); a sparse figure that could carry more of the data (→ add detail); color over large areas or rainbow maps (→ gray first, light to dark); all-caps or rotated labels (→ upper-and-lower case, horizontal); pie, 3D or dual axes.
- **Against the evidence:** dynamite plots; undefined error bars or *n*; statistics on two or three points; technical replicates as *n*; undefined asterisks; bars on a log axis.
- **Against production:** a figure drawn at screen size and scaled down; text below 5 pt or sizes that vary across figures; a title inside the figure; rasterized text or unembedded fonts.

Per-library detection and fixes: `rules/anti-patterns.md`.

## Validation checklist

Before presenting any figure, verify:

**Tufte**
- [ ] The data themselves are shown, not only summaries (rule 1)
- [ ] Lengths and areas proportional to values; bars from zero; same design across panels (rule 2)
- [ ] The comparison is on the page, side by side, on one scale, and comes from the data (rule 3)
- [ ] The explanatory variable is on an axis; every case is included, zeros too; categories ordered meaningfully (rule 4)
- [ ] Multivariate evidence shown, by small multiples where needed (rule 5)
- [ ] Names, key values and events written on the graphic (rule 6); series labeled directly (rule 7)
- [ ] The figure carries as much of the data as the reader can use (rule 8)
- [ ] No frame, box, heavy grid or decoration (rule 9); range-frame axes (rule 10)
- [ ] Layers ordered: data darkest, references lighter, axes lightest; readable at a glance and up close (rule 11)
- [ ] Color last and gray first; one highlight unless more are needed; strong color only in small areas, large areas muted; Okabe–Ito or a uniform map; grayscale test passed (rule 12)
- [ ] Upper-and-lower case, horizontal type, words spelled out (rule 13)

**Evidence**
- [ ] Every observation shown for small samples; no dynamite plots (rule 15)
- [ ] Every error bar and band defined; *n* and what it counts stated (rule 16)
- [ ] Effects and intervals shown; significance marks defined (rule 17); log axes labeled with values (rule 18)
- [ ] Every number on the figure matches the text (rule 19)

**Production**
- [ ] Final width in millimeters; Helvetica at the journal's sizes (rules 20–21)
- [ ] Caption: finding first, checked against the data; documentation; no title in the artwork (rule 22)
- [ ] Lines 0.25–1 pt; panel letters in the journal's style (rules 23–24)
- [ ] Vector PDF or EPS with embedded TrueType fonts (rule 25)

## Departures from Tufte

Each is named in its rule; all are here so none is hidden.

| Departure | Why | Rule |
|---|---|---|
| Helvetica instead of serif type | Journals require a sans serif (Science prefers Helvetica; Nature asks for Helvetica or Arial). Only the typeface changes; Tufte's other requirements for type hold | 21 |
| Title in the caption, not on the graphic | Journals put the title in the caption. Explanations and labels stay on the graphic (rule 6) | 22 |
| Bold panel letters | Journals require them | 24 |
| Sentence case rather than any upper-and-lower case | Science's style; a narrower form of Tufte's rule | 21 |
| Error bars, p-values, log scales | Tufte gives no rule; the statistics literature does. These extend him | 15–18 |
| Okabe–Ito, a palette of distinct hues, rather than muted tints | Chosen for Tufte's own requirement that color-deficient readers can tell the colors apart (VDQI p. 183). Used only where his color rules allow: one highlight by default, in small areas, never over large ones | 12 |

## Additional resources

**Library rules** (read ONE per task): `rules/matplotlib.md`, `rules/ggplot2-plotnine.md`.

**Cross-cutting** (read when needed): `rules/typography-and-color.md` (type, palette, maps, contrast), `rules/small-multiples-and-panels.md` (small multiples, panels, slopegraphs, quartile and dot-dash plots, sparklines), `rules/anti-patterns.md`, `rules/journals.md`, `rules/references.md`, `rules/diagrams-flowcharts.md`, `rules/maps.md`.

**Working example:** `examples/matplotlib-publication.py` — a two-panel, 89 mm figure: every observation, 95% confidence intervals, a log dose axis with the half-maximal doses marked and written on the curves, direct labels, range frames, panel letters and vector export; it checks its caption against the data.

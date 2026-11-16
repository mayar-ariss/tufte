---
name: tufte
description: >-
  Use when creating, reviewing or styling figures for scientific articles,
  preprints, theses, conference papers and their supplementary material:
  plots, multi-panel figures, small multiples, maps and schematic diagrams.
  Applies Edward Tufte's principles (show the data, graphical integrity,
  comparison, causality, data density, layering, direct labeling) to the
  style of scientific figures, the statistics literature on showing
  uncertainty, and Nature's guidance to their structure (size, panels, text
  placement, figure legends, file formats). Covers matplotlib, seaborn,
  ggplot2 and plotnine.
allowed-tools: Read, Glob, Grep
---

# Tufte: figures for scientific articles

Apply these rules whenever you generate or review code that draws a figure for a scientific article, preprint, thesis, conference paper or supplementary material. This skill is not for dashboards, web pages or slides.

Tufte wrote about printed evidence, and many of his central examples are scientific: Snow's cholera map, Minard's map of the Russian campaign, the Challenger O-ring data. His vision is the core of this skill. A scientific figure is a display of evidence: it shows the data, makes the comparison and the cause visible, carries as much information as the reader can use, and explains itself on the page.

The skill is in three parts:

1. **Tufte's principles** (rules 1–14) govern the figure's **style**: what is drawn and how — the data, the comparison, the cause, data-ink, color, layering, labels.
2. **Scientific evidence** (rules 15–19). What the statistics literature adds where Tufte gives no rule: distributions, uncertainty, p-values, log scales. These extend Tufte; none contradicts him.
3. **Nature's structure** (rules 20–25) governs the figure's **structure**: size, panel layout, which text goes on the figure and which in the figure legend, type sizes, line weights, file format.

**Tufte governs style; Nature governs structure.** Where they differ on structure, Nature's guidance supersedes Tufte and every other journal's guidance. Every departure from Tufte is named where it occurs, with its reason, and listed under "Departures from Tufte" at the end.

**Diagrams and schematics:** read `rules/diagrams-flowcharts.md`. **Maps:** also read `rules/maps.md`.

## Workflow

1. **Find the evidence.** What must the reader see, compared with what, and caused by what? Use only comparisons and explanatory variables that exist in the data or that the user supplies; never invent a target, baseline or reference value.
2. **Design by Part I.** Choose the form that shows the data, the comparison and the cause, with as much detail as the reader can use, layered so it stays readable.
3. **Add the evidence Part II asks for**: every observation where feasible, uncertainty defined, *n* stated.
4. **Structure by Part III**, to Nature's guidance: 89 mm (single column) or 183 mm (double column), 5–7 pt Helvetica or Arial, labels on the figure, everything else in the figure legend (`rules/journals.md`).
5. **Respect an existing figure style.** If the user's project already has one (a matplotlibrc, a ggplot2 theme, a lab template, earlier figures in the paper), keep its look and apply Parts I and II to the content. Apply the full style only when asked or when there is none.
6. **Library setup:** read ONE of `rules/matplotlib.md` or `rules/ggplot2-plotnine.md`.
7. **Write the figure legend** (rule 22) and check every number in it against the data. **Validate** with the checklist at the end.

## Sources

Every rule names its source:

- **Tufte** — stated in Tufte's books, cited by book and chapter: *VDQI* = *The Visual Display of Quantitative Information* (1983; 2nd ed. 2001), *EI* = *Envisioning Information* (1990), *VE* = *Visual Explanations* (1997), *BE* = *Beautiful Evidence* (2006). His fifth book, *Seeing with Fresh Eyes* (2020), is not drawn on here.
- **Literature** — a published recommendation from statistics or visualization research, cited by author and year; full references in `rules/references.md`.
- **Journal** — a requirement in Nature's author guidelines, quoted with its date in `rules/journals.md`; Nature's guidance governs structure. Other journals' requirements are kept in that file for reference only.
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

### 6. Labels on the graphic; explanations in the figure legend

*Source: Tufte, VDQI ch. 2 (principle 2: clear, detailed labeling defeats distortion); VDQI ch. 9 (words and pictures together); BE ch. 5 (fourth and fifth principles). Journal (Nature formatting guide: "Where possible, text, including keys to symbols, should be provided in the legend rather than on the figure itself"; Nature figure guide: keys in the figure rather than colour descriptions in the caption). **Departure from Tufte** on structure: Tufte writes explanations on the graphic itself; Nature puts them in the figure legend.*

Words and data still belong together; Nature decides where the words go.

- **On the graphic, labels only:** axis labels with units, tick labels, the name of each group and series as a direct label (rule 7), panel letters, scale bars, and labels that name a feature (a pump, a gene, a region).
- **In the figure legend** (rule 22): what each symbol, line, band and bar means; the values that matter (an EC₅₀, a mean, a fold change); *n* and what it counts; events, thresholds and notes; statistics; unusual units and abbreviations.
- Keep Tufte's standard for explanation: every question a reader would ask of the figure is answered, on the graphic if it is a label and in the legend if not. Nothing is left out for a clean look; it moves to the legend.

### 7. Label directly, in black; a key only for a scale

*Source: Tufte — in the friendly data graphic "labels are placed on the graphic itself; no legend is required", VDQI ch. 9 (p. 183). Journal (Nature figure guide: keys or keylines in the figure wherever possible, rather than colour descriptions in the caption; avoid coloured text, which Nature recolours black or white).*

- Label each series where it is, at the end of a line or beside a cluster, and turn the key off. The direct label is Nature's in-figure key.
- **Labels in black.** Position, not color, ties a label to its series. Never identify a series in the legend by its color ("the red line"); name it as it is labeled.
- A key stays only for an encoding that cannot carry its own label, such as a color scale for a quantity: in the figure, beside the data, unframed. Tufte does not ban keys: his redrawn cancer maps carry one (VDQI pp. 16–20).
- Symbols that are not series (open circles, bands, bars) are defined in the figure legend (rule 6).

### 8. Maximize data density, within reason

*Source: Tufte, VDQI ch. 8 (data density, the shrink principle); VDQI ch. 7 (multifunctioning graphical elements).*

- Carry as much data per square centimeter as the reader can use. Tufte's shrink principle — most graphics can be shrunk well below their usual size — suits a journal column.
- Let one element do several jobs: an axis that reports the data's range (rule 10), a reference line that is also the comparison, small multiples that share one set of labels.
- Use space for data, not for margins, boxes and repeated labels. Nature asks the same: panels laid out "in a neat and space-efficient manner, minimizing white space" (Journal, Nature figure guide).

### 9. Erase non-data-ink and redundant ink, within reason

*Source: Tufte, VDQI ch. 4 (data-ink), ch. 5 (chartjunk), ch. 6 (erasing the frame).*

No box around the plot, no top or right spines, no background fill, no heavy grid, no hatching, no decoration. Where readers must read values precisely, a light grid is acceptable (Tufte: "muted or suppressed", VDQI ch. 5); a table may serve better. Erase what carries no information about the data, never what does: erasing is subordinate to rule 1, and information taken off the graphic goes to the legend (rule 6).

### 10. Range-frame axes that report the data

*Source: Tufte, the range-frame, VDQI ch. 6; multifunctioning elements, VDQI ch. 7. Labeling the ends: this skill's application (convention).*

Each axis line spans only the range of the data, so the frame itself reports the minimum and maximum. Where it helps, label the ends of the range frame with the data's extreme values. For bars, the value axis runs from zero (rule 2).

### 11. Layer and separate; design for two readings

*Source: Tufte, EI ch. 3 (layering and separation; "1 + 1 = 3 or more"); EI ch. 2 (micro/macro readings).*

A dense figure stays clear when its layers are visually ordered: data darkest and heaviest; summaries and fits next; comparisons and references lighter; axes, grids and leader lines lightest and thinnest. Two heavy lines close together create a third, illusory element (1 + 1 = 3); separate by lightness, weight and space instead. Design for two readings: the overall pattern at a glance (the macro reading) and every individual value up close (the micro reading) — for example, each subject's trajectory as a thin light line under the group mean.

### 12. Color: black and grays, one accent, muted fields

*Source: Tufte, EI ch. 5 (color: "above all, do no harm"; muted fields with strong color in small areas, and no bright colors side by side over large areas, after Imhof; color as quantity, light to dark); BE pp. 46–63 and his sparkline notes (a gray band for the normal range; a red accent tied to a number; red and blue as a pair); VE ch. 4 (smallest effective difference); VDQI ch. 9, p. 183 (colors that color-deficient readers can tell apart). Fallback palette and maps: Literature (Okabe and Ito 2008; Wong 2011; Crameri et al. 2020).*

- **Color last.** Separate things first by position, direct labels or small multiples (rules 5 and 7); use color only for what those cannot do.
- **Black and grays carry the figure:** data in black, context in gray, individual observations and references in light gray. Make every difference as small as will still read clearly.
- **One accent, red `#CC0000`,** on the finding, as in Tufte's sparklines; its value goes in the figure legend (rule 6). **Blue `#0072B2` only as a second accent,** for a second kind of highlight; Tufte pairs the two (red for first and last values, blue for low and high).
- **Muted fields for large areas:** a light gray band for a normal range or reference interval; a pale tint of one hue for a large region, stepped light to dark when it encodes a quantity. Strong color only in small areas (lines, dots, small marks; text stays black, rule 7); never strong or bright colors over large areas.
- **For quantities,** light to dark in one hue, or a perceptually uniform map (viridis, cividis, batlow; vik for diverging data). Never rainbow or jet.
- **Several categories that must be colored** (three or more, when position, labels and small multiples cannot separate them): the Okabe–Ito palette, as a set in place of the accents, in small areas, at most four colors. Tufte gives no palette for this; Okabe–Ito meets his p. 183 requirement.
- Never red against green for a contrast that matters. Same condition, same color in every figure of the paper. The figure must read in grayscale. The red and the blue were checked in simulations of color-vision deficiency and stay distinct from the grays and from each other.

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

A p-value does not measure the size of an effect. Show the effect and its interval on the figure; give the estimate and exact p-values in the figure legend or text (rule 6). If asterisks or brackets are used, define each in the legend and draw brackets thin and gray.

### 18. Log scales for multiplicative data

*Source: Literature (Cleveland 1994, ch. 3).*

Use a log axis when values span orders of magnitude, or when ratios, fold changes or growth rates are the point. Base 2 for fold changes, base 10 for wide ranges. Label ticks with values (1, 10, 100 or 10⁰, 10¹, 10²), not logarithms. No bars on a log axis.

### 19. Each figure stands alone and agrees with the text

*Source: Tufte, BE ch. 5 ("content counts most of all"); convention.*

Every number on a figure matches the text and tables. A reader with only the figure and its legend can tell what was measured, in what units, on how many samples, and what the authors conclude.

---

## Part III — Nature's structure

These rules follow Nature's author guidelines: the formatting guide, final submission and the research figure guide (quotes and dates in `rules/journals.md`). They govern a figure's structure and supersede Tufte and other journals' guidance wherever they differ. Where one departs from Tufte, the rule says so.

### 20. Nature's sizes, drawn at final size

*Source: Journal (Nature figure guide; final submission).*

- Width: 89 mm (single column) or 183 mm (double column); 120–136 mm for 1.5 columns. Height at most 170 mm, to leave room for the legend beneath. (Nature's formatting guide rounds the widths to 90 and 180 mm; the figure guide's values are used here.)
- Set the width before drawing, so type and lines come out at their printed size; never scale an exported figure to fit.
- Submit at the smallest size that keeps every element legible; Nature may reduce figures further.

### 21. Helvetica or Arial, 5–7 pt, black text

*Source: Journal (Nature: sans-serif lettering, "preferably Helvetica or Arial"; text 5–7 pt; avoid coloured text; lettering in lower-case type with an initial capital and no full stop; a space between number and unit; thousands separated by commas; no type over shaded areas; amino-acid sequences in Courier). **Departure from Tufte**, who sets data graphics in serif type (VDQI ch. 9, p. 183).*

- Helvetica, with Arial as the fallback; one font and one size scale across every figure in the paper. All text between 5 and 7 pt.
- Text black (or white on a dark ground), contrast above 4.5:1. Nature recolours colored text unless the color carries scientific meaning.
- Labels in lower case with an initial capital and no full stop: "Response (fraction of maximum)". Units in parentheses after the quantity; a space between number and unit (5 mm); thousands with commas (1,000); true minus sign (−), × and µ.
- No type directly over shaded or textured areas; no reversed type where it can be avoided. Scale bars rather than magnification factors.
- The departure is of typeface only: everything Tufte asks of type (rule 13) still holds, and his own books set tables in a sans serif, Gill Sans. See `rules/typography-and-color.md`.

### 22. The figure legend, in Nature's form

*Source: Journal (Nature formatting guide); Tufte, BE ch. 5 (fifth principle: document the evidence). **Departure from Tufte**, who puts a detailed title and the explanations on the graphic itself.*

- No title, figure number, key box or source line inside the artwork.
- Begin with a brief title for the whole figure; it may state the finding, and only what the data show.
- Then a short description of each panel, by its letter, and of the symbols used.
- Define every error bar and statistic, *n* and what it counts, and any unusual unit or abbreviation. Give the values and notes moved off the graphic (rule 6).
- No details of methods when the paper has a Methods section.
- Fewer than 300 words. Refer to series by their labels, never by their colors.
- Check every number against the data. At final submission the legends go in the text document, one after another, not in the figure file.

### 23. Lines and marks that survive reduction

*Source: Journal (Nature: line weights 0.25–1 pt at final size); convention for the defaults, layered by rule 11.*

Data lines 1 pt; axes, ticks, error bars and leader lines 0.5 pt or lighter; markers about 3 pt. Nothing thinner than 0.25 pt.

### 24. Panel letters and layout

*Source: Journal (Nature final submission and figure guide); convention for shared axes.*

- Panel letters 8 pt bold, upright (not italic), lowercase: a, b, c, at the top left of each panel.
- Panels in alphabetical order, laid out neatly and space-efficiently with little white space; size each panel by its content and legibility.
- More than one panel only when the parts are logically connected.
- Label common axes once, on the outer edge (convention). Bold panel letters are a production mark, not a Tufte element.

### 25. Export vector graphics with embedded, editable fonts

*Source: Journal (Nature figure guide; final submission: "Please do not rasterize line art or text").*

- Main figures: vector `.ai`, `.eps` or `.pdf`, text editable, fonts embedded (TrueType, Type 42), never outlined or rasterized. Nature does not accept JPEG, TIFF or PNG for main figures. Keep files under 50 MB, everything embedded, not linked.
- Extended Data figures: RGB, JPEG preferred (TIFF or EPS accepted), at most 300 dpi and 10 MB, sized to fit one page with room for the legend.
- Check with `pdffonts figure.pdf`: every font `emb yes`.

---

## Chart types

These settings are this skill's defaults (convention), except where a cell names another source.

| Type | Key settings |
|---|---|
| **Strip / dot plot** | Every observation, jittered; mean or median with 95% CI beside the points; the groups labeled; values and *n* in the legend (rules 1, 6, 15, 16) |
| **Line** | 1 pt; markers where measurements were taken; direct labels; CI band light; individual trajectories as thin light lines under the mean when *n* is small enough (rule 11) |
| **Scatter** | Every point; highlight the group that matters; fitted line thin, with its band; rug marks for marginals (Tufte's dot-dash plot, VDQI ch. 6) |
| **Bar** | Counts and proportions only; zero baseline; sorted by value or by the explanatory variable (Tufte, VDQI ch. 9, p. 178) |
| **Quartile plot** | Tufte's redesign of the box plot (VDQI ch. 6): no box; a dot at the median, a gap for the middle half, lines to the extremes |
| **Paired data** | One line per subject between conditions (slopegraph: Tufte, VDQI pp. 158–159) |
| **Small multiples** | One design, one scale, panels close together and ordered meaningfully (Tufte, EI ch. 4) |
| **Heatmap** | Light to dark, or a perceptually uniform map; values in the cells when few; colorbar beside, unframed |
| **Dose–response, growth, concentration** | Explanatory variable on x, on a log axis labeled with values; key values (EC₅₀, plateau) marked on the curve and given in the legend |
| **Sparklines** | Word-sized, in tables or text; beginning and ending values beside the line; first and last values in red, low and high in blue (Tufte, BE pp. 50–51) |

Avoid: dynamite plots, pie charts, 3D, dual axes; stacked bars and area charts except for cumulative totals (convention: small multiples compare better).

## Nature quick reference

| | Nature |
|---|---|
| Widths | 89 mm single, 183 mm double (120–136 mm for 1.5 columns); height ≤ 170 mm |
| Typeface | Helvetica or Arial; black text |
| Text size | 5–7 pt |
| Panel letters | 8 pt bold, upright **a, b, c** |
| On the figure | Labels only: axes, series names, panel letters, scale bars |
| Figure legend | Brief title; each panel and its symbols; error bars, statistics, *n*; values and notes; < 300 words |
| Main figures | Vector AI, EPS or PDF, editable text, fonts embedded |

Quotes, sources and dates: `rules/journals.md`, which also keeps other journals' requirements for reference.

## Library quick reference

| Library | Rule file | Essentials (apply even without reading the file) |
|---|---|---|
| matplotlib, seaborn | `rules/matplotlib.md` | `figsize` in mm/25.4; `font.sans-serif: ["Helvetica", "Arial", …]`; `font.size: 7`; spines top/right off; `axes.grid: False`; `pdf.fonttype: 42`; `savefig.bbox: "standard"` |
| ggplot2 (R) | `rules/ggplot2-plotnine.md` | `theme_classic(base_size = 7, base_family = "Helvetica")`; `legend.position = "none"`; `ggsave(width = 89, units = "mm", device = cairo_pdf)` |
| plotnine (Python) | `rules/ggplot2-plotnine.md` | `theme_classic(base_size=7, base_family="Helvetica")`; `legend_position="none"`; `p.save(width=89, units="mm")` |

## Anti-pattern detection

When reviewing a figure or its code, check for:

- **Against Tufte:** summaries without the data (→ show the observations); a comparison the reader must assemble across figures (→ side by side, same scale); the explanatory variable hidden in a legend or panel order (→ on an axis); missing zeros or non-responders (→ include them); categories in alphabetical order (→ order by value or cause); unlabeled series (→ direct labels, in black); a key box (→ direct labels; symbols defined in the legend); a heavy frame, grid or decoration (→ erase); every element the same weight (→ layer); a sparse figure that could carry more of the data (→ add detail); color over large areas or rainbow maps (→ gray first, light to dark); all-caps or rotated labels (→ upper-and-lower case, horizontal); pie, 3D or dual axes.
- **Against the evidence:** dynamite plots; undefined error bars or *n*; statistics on two or three points; technical replicates as *n*; undefined asterisks; bars on a log axis.
- **Against Nature's structure:** a figure drawn at screen size and scaled down; text outside 5–7 pt or sizes that vary across figures; a title, notes or values written inside the figure; colored text; series identified by color in the legend; a legend of 300 words or more, or one with methods; rasterized text or unembedded fonts.

Per-library detection and fixes: `rules/anti-patterns.md`.

## Validation checklist

Before presenting any figure, verify:

**Tufte**
- [ ] The data themselves are shown, not only summaries (rule 1)
- [ ] Lengths and areas proportional to values; bars from zero; same design across panels (rule 2)
- [ ] The comparison is on the page, side by side, on one scale, and comes from the data (rule 3)
- [ ] The explanatory variable is on an axis; every case is included, zeros too; categories ordered meaningfully (rule 4)
- [ ] Multivariate evidence shown, by small multiples where needed (rule 5)
- [ ] Labels only on the graphic; values, notes and symbol definitions in the legend (rule 6); series labeled directly, in black (rule 7)
- [ ] The figure carries as much of the data as the reader can use (rule 8)
- [ ] No frame, box, heavy grid or decoration (rule 9); range-frame axes (rule 10)
- [ ] Layers ordered: data darkest, references lighter, axes lightest; readable at a glance and up close (rule 11)
- [ ] Color last; black and grays first; one red accent, blue only as a second; large areas in muted fields; Okabe–Ito only for several colored categories; a uniform map for quantities; grayscale test passed (rule 12)
- [ ] Upper-and-lower case, horizontal type, words spelled out (rule 13)

**Evidence**
- [ ] Every observation shown for small samples; no dynamite plots (rule 15)
- [ ] Every error bar and band defined; *n* and what it counts stated (rule 16)
- [ ] Effects and intervals shown; significance marks defined (rule 17); log axes labeled with values (rule 18)
- [ ] Every number on the figure matches the text (rule 19)

**Nature's structure**
- [ ] 89 or 183 mm wide, at most 170 mm tall; Helvetica or Arial, 5–7 pt, black (rules 20–21)
- [ ] Legend: brief title; each panel and its symbols; error bars, statistics and *n* defined; values and notes; no methods; under 300 words; checked against the data (rule 22)
- [ ] Lines 0.25–1 pt; 8 pt bold upright a, b, c; panels in order, logically connected (rules 23–24)
- [ ] Vector AI, EPS or PDF with embedded TrueType fonts (rule 25)

## Departures from Tufte

Each is named in its rule; all are here so none is hidden.

| Departure | Why | Rule |
|---|---|---|
| Helvetica instead of serif type | Nature asks for a sans serif, preferably Helvetica or Arial. Only the typeface changes; Tufte's other requirements for type hold | 21 |
| Explanations, values and symbol keys in the figure legend; only labels on the graphic | Nature: text, including keys to symbols, in the legend rather than on the figure where possible. Tufte writes them on the graphic | 6, 22 |
| Labels in black, not in their series' color | Nature recolours colored text. Position ties a label to its series | 7, 21 |
| Title in the legend, not on the graphic | Nature's legends begin with the figure's title | 22 |
| Bold panel letters | Nature requires them | 24 |
| Lower case with an initial capital, rather than any upper-and-lower case | Nature's style; a narrower form of Tufte's rule | 21 |
| Error bars, p-values, log scales | Tufte gives no rule; the statistics literature does. These extend him | 15–18 |
| Exact hexes for the red, the blue and the fields; Okabe–Ito when several categories must be colored | Tufte names colors, not values, and gives no palette for many categories. The values were chosen to pass contrast and color-vision checks; Okabe–Ito meets his own requirement that color-deficient readers can tell colors apart (VDQI p. 183), and is used only in small areas | 12 |

## Additional resources

**Library rules** (read ONE per task): `rules/matplotlib.md`, `rules/ggplot2-plotnine.md`.

**Cross-cutting** (read when needed): `rules/typography-and-color.md` (type, palette, maps, contrast), `rules/small-multiples-and-panels.md` (small multiples, panels, slopegraphs, quartile and dot-dash plots, sparklines), `rules/anti-patterns.md`, `rules/journals.md`, `rules/references.md`, `rules/diagrams-flowcharts.md`, `rules/maps.md`.

**Working example:** `examples/matplotlib-publication.py` — a two-panel, 89 mm figure: every observation, 95% confidence intervals, a log dose axis with the half-maximal doses marked on the curves, black direct labels, range frames, panel letters and vector export; it prints a Nature-style legend and checks it against the data.

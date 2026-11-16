---
name: tufte
description: >-
  Use when creating, reviewing or styling figures for scientific articles,
  preprints, theses, conference papers and their supplementary material:
  plots, multi-panel figures, small multiples, maps and schematic diagrams.
  Applies Edward Tufte's principles (graphical integrity, data-ink, analytical
  design) together with journal requirements (Nature, Science, PLOS) and the
  statistics literature on showing data and uncertainty. Covers matplotlib,
  seaborn, ggplot2 and plotnine. Helvetica, widths in millimeters, captions,
  error bars and confidence intervals, log scales, color-blind-safe palettes,
  vector export with embedded fonts.
allowed-tools: Read, Glob, Grep
---

# Tufte: figures for scientific articles

Apply these rules whenever you generate or review code that draws a figure for a scientific article, preprint, thesis, conference paper or supplementary material. The page is printed or read as a PDF, set in narrow columns, and the journal sets the type, the sizes and the file format. Tufte wrote about printed graphics, and many of his central examples are scientific (Snow's cholera map, Minard's map of the Russian campaign, the Challenger O-ring data), so his principles carry over directly. This skill adds what a journal page requires and what the statistics literature asks of figures that carry evidence.

This skill is not for dashboards, web pages or slides.

**Diagrams and schematics:** read `rules/diagrams-flowcharts.md`. Rules about axes, baselines and the lie factor concern quantities on scales and do not apply to diagrams.

**Maps:** for any display on geographic space, also read `rules/maps.md`.

## Workflow

Follow these steps in order.

1. **Identify the finding and the comparison.** What must the reader see, and compared with what? Use only comparisons that exist in the data or that the user supplies; never invent a target, baseline or reference value.
2. **Identify the target journal.** If the user names one, its current author guide overrides the defaults here (`rules/journals.md`). If none is named, draw at 89 mm (single column) or 183 mm (double column) in 5–7 pt Helvetica, which suits most journals.
3. **Respect an existing figure style.** If the user's project already has one (a matplotlibrc, a ggplot2 theme, a lab template, earlier figures in the same paper), keep its look and apply the rules on integrity, uncertainty and documentation. Apply the full style only when asked or when there is none.
4. **Choose the form.** See Chart types below. A sentence or a table is sometimes better (rule 20).
5. **Apply graphical integrity, data-ink and the rules below,** then the library setup: read ONE of `rules/matplotlib.md` or `rules/ggplot2-plotnine.md`.
6. **Write the caption** (rule 15) and check every claim in it against the data.
7. **Validate** with the checklist at the end of this file.

## Sources

Every rule names its source, so Tufte's principles are never confused with anyone else's:

- **Tufte** — stated in Tufte's books, cited by book and chapter: *VDQI* = *The Visual Display of Quantitative Information* (1983; 2nd ed. 2001), *EI* = *Envisioning Information* (1990), *VE* = *Visual Explanations* (1997), *BE* = *Beautiful Evidence* (2006). His fifth book, *Seeing with Fresh Eyes* (2020), is not drawn on here.
- **Journal** — a requirement in a journal's author guidelines, quoted with its date in `rules/journals.md`. Journals revise these pages; the target journal's current guide wins.
- **Literature** — a published recommendation from statistics or visualization research, cited by author and year; full references in `rules/references.md`.
- **Convention** — common practice in Tufte-style or scientific figures, stated by none of the above. Specific values (hex colors, point sizes, opacities) are this skill's defaults.
- **Extension** — added by this skill's authors (for example the contrast minimums). Not from Tufte.

Where none of these gives a rule, the rule says so instead of supplying one.

---

## Graphical integrity

*Source: Tufte, VDQI ch. 2.* Tufte's six principles, in summary:

1. **Proportional representation.** Numbers, as physically measured on the graphic, must be directly proportional to the quantities they represent. Tufte measures violations with the *lie factor*: the size of the effect shown in the graphic divided by the size of the effect in the data (1.0 is truthful).
2. **Clear, detailed labeling** defeats distortion and ambiguity. Write explanations of the data on the graphic itself; label important events in the data.
3. **Show data variation, not design variation.**
4. **Deflate money.** In time series of money, deflated and standardized units are nearly always better than nominal units.
5. **Dimensions.** The number of information-carrying dimensions depicted should not exceed the number of dimensions in the data.
6. **Context.** Graphics must not quote data out of context.

**Baselines.** Tufte prescribes no zero baseline: *VDQI* "never recommends showing zero-points" (Tufte, edwardtufte.com forum, 2003, citing VDQI pp. 74–75, where context comes from showing more data rather than reaching down to zero). *This skill's application of principle 1 (convention):* a bar's length, or an area's size, is proportional to its value only when it starts at zero, so bars and areas start at zero; lines and dots encode by position and take a baseline that shows the data.

## Data-ink

*Source: Tufte, VDQI ch. 4 (data-ink), ch. 5 (chartjunk), ch. 1 (graphical excellence).*

Tufte's five principles, in his order:

1. **Above all else show the data.**
2. **Maximize the data-ink ratio, within reason.** Data-ink is the non-erasable core of a graphic; the ratio is the share of a graphic's ink devoted to the non-redundant display of data.
3. **Erase non-data-ink, within reason.**
4. **Erase redundant data-ink.**
5. **Revise and edit.**

"Within reason" is his qualifier: the principles guide editing; they are not a quota.

**Chartjunk** (VDQI ch. 5) has three forms: unintentional optical art (moiré vibration from hatching and dense patterns), the dark grid, and the "duck" (a graphic whose decoration takes over the data). None belongs in a figure.

**Beyond erasing**, Tufte asks for more data, not less: high data density (VDQI ch. 8), multifunctioning elements (VDQI ch. 7) and displays that read at two levels, the overall pattern and the detail (EI ch. 2). A journal page rewards all three: space is scarce. Science asks authors to "maximize the space given to presentation of the data" and to avoid wasted white space and clutter (Journal, Science).

## Analytical design

*Source: Tufte, BE ch. 5, "The Fundamental Principles of Analytical Design".*

1. **Show comparisons**, contrasts, differences (rule 14).
2. **Show causality**, mechanism, explanation, systematic structure (rule 13; `rules/diagrams-flowcharts.md`).
3. **Show multivariate data** — more than one or two variables (rule 17).
4. **Integrate evidence** — words, numbers and images together (rule 5).
5. **Document the evidence** — sources, measurement scales, what was measured and how. In a paper this goes in the caption and Methods (rule 15).
6. **Content counts most of all** — no design rescues weak, irrelevant or untrustworthy data.

---

## Rules

Every rule is a default; the target journal's guide, the user's explicit request, or an existing figure style in the project (Workflow step 3) can override the parts it concerns.

### 1. Draw at the final printed size, in millimeters

*Source: Journal (Nature, Science, PLOS). Aspect ratio: Tufte, VDQI ch. 9.*

Set the figure width to the column it will occupy before drawing anything, so type and lines come out at their printed size. Never scale an exported figure to fit. Nature: 89 mm (single column), 120–136 mm (1.5 columns), 183 mm (double column), at most 170 mm tall. Science: 5.7, 12.1 or 18.4 cm. PLOS: 6.68–19.05 cm wide, at most 22.23 cm tall. A single panel keeps Tufte's shape, about 1.5 times wider than tall, unless the data suggest another (VDQI ch. 9).

### 2. Helvetica, in sentence case, at the journal's sizes

*Source: Journal for typeface and sizes (Science prefers Helvetica; Nature asks for Helvetica or Arial; PLOS lists Arial). Tufte for case, spelling and orientation (VDQI ch. 9, p. 183).*

- Helvetica, with Arial as the fallback (Arial for PLOS). One font and one size scale across every figure in the paper.
- Nature: 5–7 pt, panel letters 8 pt bold. Science: about 7 pt, never below 5 pt. PLOS: 8–12 pt.
- Upper-and-lower case: sentence case for labels, never all caps. Words spelled out where space allows. Type runs horizontally: set the y-axis label horizontally at the top of the axis, and rotate it only when the panel is too narrow.
- Axis labels give the quantity, then its units in parentheses: "Concentration (µM)". Very large or small numbers as powers of 10 (Journal, Science). True minus sign (−), × and µ.

This departs from Tufte's stated preference for serif type in data graphics (VDQI p. 183), not from what he asks of type: that it be clear, precise and modest. His own books set tables in a sans serif, Gill Sans. See `rules/typography-and-color.md`.

### 3. Erase the frame

*Source: Tufte, VDQI ch. 6.*

No top or right spines, no box around the plot, no background fill. The bottom and left axes are enough. White page (Journal: the figure sits on a white page, where an off-white box would show).

### 4. Range-frame axes

*Source: Tufte, the range-frame, VDQI ch. 6.*

Axis lines span only the range of the data. Bars still start at zero (graphical integrity, above), so for bars the value axis runs from zero to the maximum.

### 5. Direct labels, not legends

*Source: Tufte — in the friendly data graphic "labels are placed on the graphic itself; no legend is required", VDQI ch. 9 (p. 183); words and pictures belong together, VDQI ch. 9 (pp. 180–181).*

Label each series where it is, at the end of a line or beside a cluster, and turn the legend off. A key stays only for an encoding that cannot carry its own label, such as a color scale for a quantity; show it beside the data, unframed. Tufte does not ban keys: his redrawn cancer maps carry one (VDQI pp. 16–20).

### 6. No gridlines by default

*Source: Tufte — dark grids are chartjunk; a grid should be muted or suppressed, VDQI ch. 5.*

No gridlines. Where readers must read values precisely, add a light gray grid (convention: 0.25 pt, `#dddddd`), or give the values in a table.

### 7. No 3D, no pie charts, no dual y-axes

*Source: Tufte — integrity principle 5 and chartjunk (3D), VDQI ch. 2 and 5; pie charts, VDQI ch. 9. Dual axes: convention; the alternative, small multiples, is Tufte's (EI ch. 4).*

No perspective, depth or shadows. Instead of a pie, a dot plot or bar chart sorted by value, or a table. Instead of two y-axes, two panels stacked on a shared x-axis. If the user still asks for a pie chart after this is explained, follow the request.

### 8. Gray first; Okabe–Ito for categories; perceptually uniform maps for quantities

*Source: Tufte, EI ch. 5 (muted fields, strong color in small areas); Literature (Okabe and Ito 2008; Wong 2011; Crameri et al. 2020); Journal (Science: avoid red with green, avoid colored type; Nature: RGB).*

- Draw context and reference series in gray (`#666666`); give color only to what the reader must find. Highlight: blue `#0072B2`.
- For categories, the Okabe–Ito colors that clear 3:1 on white: blue `#0072B2`, vermillion `#D55E00`, bluish green `#009E73`, reddish purple `#CC79A7`, and black. Orange, sky blue and yellow fall below 3:1; use them only for filled areas with a dark outline.
- For quantities, a perceptually uniform, color-blind-safe map: viridis, cividis, or Crameri's batlow (sequential) and vik (diverging). Never rainbow or jet.
- Text and axes in black. Never red against green for a contrast that matters. Same condition, same color in every figure of the paper (integrity principle 3). The figure must still read in grayscale.

Hex values and contrast ratios: `rules/typography-and-color.md`.

### 9. Show the data, then the summary

*Source: Tufte, VDQI ch. 4 ("Above all else show the data"); Literature (Weissgerber et al. 2015; Krzywinski and Altman 2014).*

For continuous data in small samples, plot every observation (a strip, jittered or beeswarm plot) with the summary on top. Never a bar of the mean with an error bar ("dynamite plot"): many different distributions give the same bar (Weissgerber et al. 2015). Bars are for counts and proportions. For larger samples, Tufte's quartile plot (VDQI ch. 6) or a box plot with the points behind it; box plots need at least five observations (Krzywinski and Altman 2014). For paired or repeated measures, connect each subject's values.

### 10. Show uncertainty, and say which uncertainty

*Source: Literature (Cumming et al. 2007; Vaux 2012; Krzywinski and Altman 2013). Tufte gives no rule for error bars.*

- State in the caption what every bar or band shows: SD, SEM or a 95% confidence interval. The same bar means different things in each case.
- SD to describe spread; a 95% confidence interval to support a comparison; label SEM as SEM.
- With two or three independent observations, plot the points instead of error bars or p-values (Vaux 2012).
- Error bars belong to independent replicates, not technical replicates.
- Draw intervals as thin lines (0.5 pt) without caps; bands around curves at low opacity (about 0.2). Caps are non-data-ink (convention, after VDQI ch. 4).

### 11. Estimates first; define every significance mark

*Source: Literature (Wasserstein and Lazar 2016); convention for the marks.*

A p-value does not measure the size of an effect. Show the effect and its interval; give exact p-values in the caption or text. If asterisks or brackets are used, define each in the caption and draw brackets thin and gray.

### 12. Log scales for multiplicative data

*Source: Literature (Cleveland 1994, ch. 3); Journal (Science, powers of 10). Tufte gives no general rule.*

Use a log axis when values span orders of magnitude, or when ratios, fold changes or growth rates are the point. Base 2 for fold changes, base 10 for wide ranges. Label ticks with values (1, 10, 100 or 10⁰, 10¹, 10²), not logarithms. No bars on a log axis.

### 13. Annotate the notable

*Source: Tufte — integrity principle 2 (label important events in the data), VDQI ch. 2.*

Mark a peak, threshold, intervention or event on the plot itself, in the nearest clear space, with a short leader line if needed. Keep only the annotations the finding needs.

### 14. Show comparison context — from the data

*Source: Tufte — "Compared to what?", EI p. 67; integrity principle 6, VDQI ch. 2.*

Include the comparison the finding depends on: a control group, a reference condition, a baseline period, a published value the user supplies. Never add a reference line, target or "expected" value that is not in the data or given by the user.

### 15. Title, finding and documentation go in the caption

*Source: Tufte, BE ch. 5 (document the evidence); Literature (Rougier et al. 2014, rule 4; Cumming et al. 2007); Journal (Freshwater Science: no title duplicating the caption).*

- Nothing above the plot: no title, figure number, source line or logo.
- The caption's first sentence states the finding, and only what the data show ("Drug B lowers the half-maximal dose about ninefold", not "Dose–response curves"). Check every number in it against the data.
- Then each panel, every encoding not labeled on the plot, what the marks and error bars show, *n* and what it counts (cells, animals, independent experiments), and the test used.
- Sources, code and data availability go in Methods.

### 16. Lines and marks that survive reduction

*Source: Journal (Nature: line weights 0.25–1 pt at final size); convention for the defaults.*

Axes and ticks 0.5 pt, data lines 1 pt, error bars 0.5 pt, markers about 3 pt. Nothing thinner than 0.25 pt.

### 17. Multi-panel figures and small multiples

*Source: Tufte, EI ch. 4 (small multiples); Journal (Nature, Science) for panel letters and layout.*

- Panels comparing the same quantity share the axis and its range; say so in the caption if they cannot.
- Panel letters in the journal's style: Nature bold lowercase (a, b, c) at 8 pt; Science bold capitals (A, B, C) at 10 pt, top left. Align them on one grid.
- Set panels close together and label common axes once, on the outer edge (Journal, Science).

See `rules/small-multiples-and-panels.md`.

### 18. Export vector graphics with embedded, editable fonts

*Source: Journal (Nature: AI, PostScript, vector EPS or PDF for graphs; "Please do not rasterize line art or text"; photographs at 300 dpi or more. PLOS: TIFF or EPS at 300–600 dpi).*

PDF or EPS with fonts embedded as TrueType and kept as text. Raster only when the journal asks (TIFF at 600 dpi at final width). Check with `pdffonts figure.pdf`: every font `emb yes`.

### 19. Each figure stands alone and agrees with the text

*Source: Tufte, BE ch. 5 ("content counts most of all"); convention.*

Every number on a figure matches the text and tables. A reader with only the figure and its caption can tell what was measured, in what units, on how many samples, and what the authors conclude.

### 20. Don't chart what a sentence or table can say

*Source: Tufte — the choice among sentences, tables and graphics, VDQI ch. 9.*

One or two numbers belong in a sentence. Tables suit many small data sets and exact values. Graphics earn their space for larger data sets, where they reveal patterns, trends and distributions.

---

## Chart types

These settings are this skill's defaults (convention), except where a cell names another source.

| Type | Key settings |
|---|---|
| **Strip / dot plot** | Every observation, jittered; mean or median with 95% CI beside the points (rule 9, 10) |
| **Line** | 1 pt; markers only where measurements were taken; direct label at the end; CI band at 0.2 opacity |
| **Scatter** | Gray dots about 3 pt; highlight the group that matters; fitted line thin, with its band; rug marks for marginals (Tufte's dot-dash plot, VDQI ch. 6) |
| **Bar** | Counts and proportions only; zero baseline; sorted by value, not alphabetically (Tufte, VDQI ch. 9, p. 178); horizontal for long category names |
| **Quartile plot** | Tufte's redesign of the box plot (VDQI ch. 6): no box; a dot at the median, a gap for the middle half, lines to the extremes; say in the caption that it shows the five-number summary |
| **Paired data** | One line per subject between conditions (slopegraph: Tufte, VDQI pp. 158–159) |
| **Small multiples** | One design, one scale, panels close together (Tufte, EI ch. 4) |
| **Heatmap** | Perceptually uniform map; values in cells when few; colorbar beside, unframed |
| **Dose–response, growth, concentration** | Log axis labeled with values (rule 12) |
| **Sparklines** | In tables only: word-sized, beginning and ending values beside the line; first and last values in red, low and high in blue (Tufte, BE pp. 50–51) |

Avoid: dynamite plots, stacked bars (use small multiples), area charts for anything but cumulative totals, pie charts, 3D.

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

When reviewing figure code or a figure, check for: bar of means with error bars for continuous data (→ points plus CI), error bars not defined in the caption (→ state SD, SEM or CI and *n*), SEM on few observations (→ plot the points), rainbow or jet colormap (→ viridis, cividis, batlow), red and green as the only contrast (→ Okabe–Ito), legend box (→ direct labels), gridlines (→ remove), title inside the figure (→ caption), all-caps labels (→ sentence case), text below 5 pt or sizes that vary across figures (→ one scale), figure drawn at screen size and scaled down (→ final width in mm), rasterized text or unembedded fonts (→ vector PDF, TrueType), bars on a log axis or a truncated bar axis (→ dots, or zero baseline), dual y-axes (→ stacked panels), pie or 3D (→ dot or bar plot), panels that compare one quantity on different scales (→ shared axis), an invented reference line (→ remove).

Per-library detection and fixes: `rules/anti-patterns.md`.

## Validation checklist

Before presenting any figure, verify:

- [ ] Lengths and areas are proportional to the values (lie factor ≈ 1); bars start at zero
- [ ] The data are shown in context; every comparison comes from the data or the user
- [ ] Width set in millimeters to the target column; nothing rescaled after export
- [ ] Helvetica (Arial for PLOS); text within the journal's range; one size scale across the paper
- [ ] Sentence case, horizontal type where space allows; units in every axis label
- [ ] White page; black text and axes; no top or right spines, no box, no gridlines
- [ ] Axis lines span the data (range frame)
- [ ] Series labeled directly; a key only for a color scale, unframed
- [ ] Individual observations shown for small samples; no dynamite plots
- [ ] Every error bar and band defined; *n* and what it counts stated
- [ ] Gray first; Okabe–Ito or a perceptually uniform map; same condition, same color; grayscale test passed
- [ ] Log axes labeled with values; no bars on log axes
- [ ] No title, figure number or source line in the artwork
- [ ] Caption: finding first, checked against the data; each panel; encodings; statistics
- [ ] Lines between 0.25 pt and 1 pt; panel letters in the journal's style
- [ ] Vector PDF or EPS with embedded TrueType fonts (`pdffonts`: `emb yes`)
- [ ] Every number on the figure matches the text
- [ ] A figure is warranted: the data could not be given as a sentence or table

## Additional resources

**Library rules** (read ONE per task): `rules/matplotlib.md`, `rules/ggplot2-plotnine.md` — setup, helpers, complete examples, export.

**Cross-cutting** (read when needed):
- `rules/typography-and-color.md` — Helvetica, sizes, Okabe–Ito, color maps, contrast on white
- `rules/small-multiples-and-panels.md` — multi-panel layout, small multiples, slopegraphs, quartile plots, dot-dash plots, sparklines in tables
- `rules/anti-patterns.md` — per-library detection and fixes
- `rules/journals.md` — journal requirements, quoted and dated
- `rules/references.md` — full references for Tufte, the literature and the journal guides
- `rules/diagrams-flowcharts.md` — schematics, process and mechanism diagrams, from Tufte's writing on connectors and layering
- `rules/maps.md` — maps, from Tufte's writing on data maps

**Working example:** `examples/matplotlib-publication.py` — a two-panel, 89 mm figure with every observation, 95% confidence intervals, a log axis, direct labels, panel letters and vector export; it checks its caption against the data.

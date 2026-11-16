# Scientific Articles

Load this file when a figure is for a journal article, preprint, thesis, conference paper or their supplementary material. It works alongside `SKILL.md` and the library guide.

The rest of this skill is written for screens: dashboards, web pages and notebooks. A journal page is a different medium. It is printed or read as a PDF, it is set in narrow columns, and the journal sets the type, the sizes and the file format. This file keeps every part of Tufte's work that holds on that page and replaces the screen defaults that do not. Tufte wrote about printed graphics, and many of his central examples are scientific displays (Snow's cholera map, Minard's map of the Russian campaign, the Challenger O-ring data), so most of the skill carries over unchanged. What changes is the house style around it.

## Sources

Every rule below names its source, using the labels in `SKILL.md` (**Tufte**, **convention**, **extension**) plus two more:

- **Journal** — a requirement in a journal's author guidelines. The guides used are listed under References, with the date they were read. Journals revise these pages; the target journal's current guide overrides this file.
- **Literature** — a published recommendation from statistics or visualization research, cited by author and year, with the full reference under References.

Where neither Tufte nor the journals give a rule, this file says so.

## What carries over unchanged

- **Graphical integrity** (Tufte, VDQI ch. 2): all six principles, including the lie factor and showing data in context. Reviewers check these.
- **Data-ink and chartjunk** (Tufte, VDQI ch. 4–5): no 3D, no heavy grids, no decoration, no hatching.
- **Analytical design** (Tufte, BE ch. 5): comparisons, causality, multivariate data, integrated evidence. Documentation moves into the caption (rule S3).
- **Universal rules 1–6, 8, 11–13 and 22** of `SKILL.md`: no top or right spines, direct labels, no gridlines, range-frame axes, no 3D, no pie charts, gray first, no dual y-axes, annotate the notable, show comparison context, and a table when a table says it better.
- **Tufte's own designs** for distributions and comparisons: the quartile plot and the dot-dash plot (VDQI ch. 6), small multiples (EI ch. 4) and the slopegraph (VDQI pp. 158–159).

## What changes, and why

| `SKILL.md` default | In a scientific article | Source |
|---|---|---|
| Rule 9: off-white `#fffff8` background | White `#ffffff`, or transparent | Journal: the figure is placed on a white page, where an off-white box shows. Tufte's books are also printed on white paper (see rule 9's source note) |
| Rule 10: serif type | **Helvetica**, with Arial as the fallback | Journal: Science prefers Helvetica, Nature asks for Helvetica or Arial (rule S2). A departure from Tufte's stated preference for serifs (VDQI p. 183), not from his principles for type |
| Rule 7: pixel sizes (600×400) | Physical widths in millimeters, at the final printed size | Journal (rule S1) |
| Rule 20: the title states the finding | No title inside the figure. The caption's first sentence states the finding | Journal (for example *Freshwater Science*); Literature (Rougier et al. 2014, rule 4); rule S3 |
| Analytical design 5: a source line on the chart | Sources, statistics and *n* in the caption and Methods; data in a repository | Tufte, BE ch. 5 (documentation), placed where journals put it; rule S3 |
| Rule 21: `$1.2M`-style abbreviations | SI units, scientific notation, units in the axis label | Convention |
| Rules 14, 15, 17, 18, 19: tooltips, progressive disclosure, responsive layout, animation, dark mode | Do not apply to a static page | — |
| Categorical palette (`rules/typography-and-color.md`) | Gray plus the Okabe–Ito colors | Literature (Wong 2011); rule S8 |
| Rule 16: contrast 3:1 for marks, 4.5:1 for text | Kept, measured against white | Extension |

## Rules

### S1. Draw at the final printed size, in millimeters

*Source: Journal (Nature; Science; PLOS). Aspect ratio: Tufte, VDQI ch. 9.*

Set the figure width to the column it will occupy before drawing anything, so type and line widths come out at their printed size. Never scale an exported figure to fit: text shrinks below the journal's minimum and lines thin out.

| Journal | Widths | Height |
|---|---|---|
| Nature | 89 mm (single column), 120–136 mm (1.5 columns), 183 mm (double column) | Page depth 247 mm; at most 170 mm for a figure, to leave room for its legend |
| Science | 5.7 cm (1 column), 12.1 cm (2 columns), 18.4 cm (3 columns) | — |
| PLOS journals | 6.68 cm minimum to 19.05 cm maximum | 22.23 cm maximum |

Cell Press and Elsevier journals publish their own widths; read the target journal's current guide rather than assuming another journal's. When the journal is not yet chosen, 89 mm and 183 mm are safe working widths.

A single panel keeps Tufte's shape, about 1.5 times wider than tall, unless the data suggest another (VDQI ch. 9). A multi-panel figure takes its height from its content.

### S2. Helvetica, in sentence case, at the journal's sizes

*Source: Journal for the typeface and sizes: Science asks for "a sans-serif font whenever possible (Helvetica is preferred)"; Nature for "a sans-serif typeface, preferably Helvetica or Arial, the same font throughout all figures"; PLOS for "Arial, Times, or Symbol font only in 8-12 point". Tufte for case, spelling and orientation (VDQI ch. 9, p. 183).*

- **Typeface:** Helvetica. Fall back to Arial, which has the same character widths, so layouts do not shift. PLOS journals list Arial and not Helvetica: use Arial for them. Free metric clones (TeX Gyre Heros, Nimbus Sans, Liberation Sans) look the same but are not Helvetica by name; check before relying on one for a final submission.
- **Font stack:** `Helvetica, Arial, "TeX Gyre Heros", "Nimbus Sans", "Liberation Sans", sans-serif`.
- **Sizes, Nature:** at most 7 pt and at least 5 pt, with panel letters at 8 pt bold. Default here: 7 pt for axis labels and annotations, 6 pt for tick labels.
- **Sizes, Science:** about 7 pt after reduction and never below 5 pt, without wide variation in size within a figure; panel letters 10 pt bold.
- **Sizes, PLOS:** 8–12 pt. Default here: 8 pt throughout, 10 pt bold for panel letters.
- **One font and one size scale across every figure** in the paper, including supplementary figures (Journal, Nature).
- **Still Tufte:** upper-and-lower case, words spelled out where space allows, type running horizontally. Science asks for the same case: capitalize only the first letter of a label, and proper nouns. Put the y-axis label horizontally at the top of the axis; rotate it 90° only when the panel is too narrow to fit it (convention).
- **Axis labels:** the quantity, then its units in parentheses, for example "Concentration (µM)"; very large or small numbers as powers of 10 (Journal, Science).
- **Symbols:** the true minus sign (−), the multiplication sign (×) and µ, not `-`, `x` and `u`. Italicize variables and keep units upright (convention, following SI style).

On the departure from Tufte: the friendly data graphic in VDQI sets type "upper-and-lower case, with serifs" (p. 183), and the rest of this skill follows him. Journals require sans serif type in figures, and Tufte's own practice already uses a sans serif, Gill Sans, for tables and dense numeric displays (see rule 10's source note in `SKILL.md`). So Helvetica departs from his preferred typeface, not from what he asks of type: that it be clear, precise and modest.

### S3. Put the title and the documentation in the caption

*Source: Tufte, BE ch. 5 (document the evidence), VDQI ch. 9 (words and graphics together); Literature (Rougier et al. 2014, rule 4, "Captions are not optional"; Cumming et al. 2007); Journal (Freshwater Science: figures "should not contain a title or text that is duplicated in the figure caption").*

- Nothing above the plot: no title, no figure number, no source line, no logo. The caption carries them.
- The caption's first sentence states the finding, as rule 20 asks of a screen title ("Drug B lowers the half-maximal dose tenfold", not "Dose–response curves").
- The caption then describes each panel and every encoding not labeled on the plot, and, for every summary shown: what the mark is (mean, median), what the error bars or bands show (SD, SEM, 95% CI), the sample size *n* and what it counts (cells, animals, independent experiments), and the test used (Cumming et al. 2007).
- Words that belong on the data stay on the data: direct labels, annotations, units on the axes (Tufte, VDQI ch. 9). The caption is for what cannot be placed there.
- Data sources and code go in Methods and the data-availability statement, which journals require.

### S4. Show the data, then the summary

*Source: Tufte, VDQI ch. 4 ("Above all else show the data"); Literature (Weissgerber et al. 2015; Krzywinski and Altman 2014).*

- **Small samples of continuous data:** plot every observation as a dot (strip, jittered or beeswarm), with the summary drawn over it. Do not use a bar of the mean with an error bar on top: many different distributions give the same bar, and the bar hides them (Weissgerber et al. 2015).
- **Bars** are for counts and proportions (Krzywinski and Altman 2014), and start at zero (`SKILL.md`, graphical integrity principle 1).
- **Larger samples:** Tufte's quartile plot (VDQI ch. 6), or a box plot with the points behind it. Box plots need at least five observations per group (Krzywinski and Altman 2014).
- **Paired or repeated measures:** connect each subject's values, as in a slopegraph, so the reader sees within-subject change (Literature, Weissgerber et al. 2015; Tufte, VDQI pp. 158–159).

### S5. Show uncertainty, and say which uncertainty

*Source: Literature (Cumming et al. 2007; Vaux 2012; Krzywinski and Altman 2013). Tufte gives no rule for error bars or intervals.*

- Say in the caption what every error bar or band represents. The same bar means different things as SD, SEM or a 95% confidence interval (Cumming et al. 2007; Krzywinski and Altman 2013).
- To describe spread, use SD. To support a comparison, use a 95% confidence interval. If SEM is used, label it as SEM (Cumming et al. 2007).
- With only two or three independent observations, plot the points rather than error bars or p-values (Vaux 2012; Cumming et al. 2007).
- Error bars and statistics belong to independent replicates, not technical replicates of one experiment (Cumming et al. 2007; Vaux 2012).
- Draw intervals as thin lines (0.5 pt) without caps, in the series color; draw bands around curves at low opacity (about 0.2). Caps and heavy bars are non-data-ink (convention, after Tufte VDQI ch. 4).

### S6. Estimates first; define every significance mark

*Source: Literature (Wasserstein and Lazar 2016); convention for the marks.*

- A p-value does not measure the size of an effect (Wasserstein and Lazar 2016). Let the figure show the effect itself, with its interval; give exact p-values in the caption or text.
- If the figure carries asterisks or comparison brackets, define each symbol in the caption, and draw brackets thin and gray so they do not outweigh the data (convention).

### S7. Use log scales for multiplicative data

*Source: Literature (Cleveland 1994, ch. 3); Journal (Science, for powers of 10). Tufte gives no general rule.*

- Use a log axis when values span several orders of magnitude, or when ratios, fold changes or growth rates are the point: logarithms turn ratios into differences and spread out values crowded near zero (Cleveland 1994). Base 2 suits fold changes, where each step is a doubling; base 10 suits wide ranges.
- Label ticks with the values (1, 10, 100, or 10⁰, 10¹, 10²), not with their logarithms, and name the base when it is not obvious. Science asks for large or small numbers as powers of 10.
- No bars on a log axis: a bar's length means nothing there, so it breaks proportional representation (Tufte, integrity principle 1). Use dots or lines.

### S8. Gray first; Okabe–Ito for categories; perceptually uniform maps for quantities

*Source: Tufte, EI ch. 5 (muted fields, strong color in small areas); Literature (Wong 2011; Okabe and Ito 2008; Crameri et al. 2020); Journal (Science: "Avoid using red and green together" and "Avoid using colored type"; Nature: RGB recommended).*

- **Gray first, still.** Draw context and reference series in gray and give color only to what the reader must find (Tufte, EI ch. 5).
- **Categories:** the Okabe–Ito palette, designed to stay distinct for color-deficient readers (Okabe and Ito 2008; Wong 2011). On white, use the colors that clear 3:1 for lines, dots and text, in this order: blue `#0072B2` (5.2:1), vermillion `#D55E00` (3.9:1), bluish green `#009E73` (3.4:1), reddish purple `#CC79A7` (3.1:1), and black. Orange `#E69F00` (2.3:1), sky blue `#56B4E9` (2.3:1) and yellow `#F0E442` (1.3:1) fall below 3:1 on white; keep them for filled areas with a dark outline, or leave them out.
- **Highlight:** blue `#0072B2` against gray. It is dark enough (5.2:1) for its direct label to share its color. For a second highlight use vermillion `#D55E00`, and set its label in black, since vermillion text falls short of 4.5:1.
- **Quantities:** a perceptually uniform, color-blind-safe map such as viridis, cividis or batlow. Never rainbow or jet, which invent boundaries and hide others (Crameri et al. 2020).
- **Text and axes in black.** Science asks authors to avoid colored type, and small gray text prints as a halftone screen and loses sharpness (convention). Direct labels may take their series' color when that color clears 4.5:1 (blue, or black); otherwise set them in black beside the line.
- **Never red against green** for a contrast that matters (Journal, Science; Wong 2011).
- **Color mode:** RGB, unless the journal asks for CMYK (Journal, Nature).
- **Grayscale test:** the figure must still read when printed in gray (`rules/typography-and-color.md`, color rule 6).
- **Same condition, same color,** in every figure of the paper. That keeps differences between figures in the data, not in the design (Tufte, integrity principle 3).

### S9. Lines and marks that survive reduction

*Source: Journal (Nature: line widths from 0.25 pt to 1 pt); convention for the defaults.*

Axis lines and ticks 0.5 pt; data lines 1 pt; error bars 0.5 pt; markers about 3 pt across. Nothing thinner than 0.25 pt.

### S10. Multi-panel figures

*Source: Journal for label style and layout (Nature; Science); Tufte, EI ch. 4 (small multiples).*

- **Panel letters:** follow the journal. Nature: "8 pt bold, upright (not italic) a, b, c". Science: capitals A, B, C, 10 pt bold, in the upper left corner of each part, and no sub-part labels such as C(a). Other journals vary; check. Align the letters on one grid.
- **Shared scales:** panels that compare the same quantity share the axis and its range, as small multiples must (EI ch. 4). If they cannot, say so in the caption.
- **Set panels close together and label common axes once** (Journal, Science), on the outer edge.
- **Spend the space on data.** Science asks authors to "maximize the space given to presentation of the data" and to avoid wasted white space and clutter: Tufte's data-ink and data-density principles (VDQI ch. 4, ch. 8) in a journal's words.

### S11. Export vector graphics with embedded, editable fonts

*Source: Journal. Nature asks for AI, PostScript, vector EPS or PDF for line drawings and graphs, "Please do not rasterize line art or text", and photographs at 300 dpi or more at their largest size. Science prefers vector files. PLOS takes TIFF or EPS at 300–600 dpi.*

- **Plots and diagrams:** PDF or EPS, vector, with fonts embedded as TrueType (Type 42) and kept as text, not converted to outlines. In matplotlib: `pdf.fonttype: 42`, `ps.fonttype: 42`, `svg.fonttype: "none"`.
- **Raster formats** (TIFF when the journal asks for it): render at the final width at 600 dpi, LZW-compressed. Photographs and micrographs keep at least 300 dpi at their printed size.
- **R:** the base `pdf()` device writes Helvetica as one of the standard PDF fonts without embedding it. Use `cairo_pdf()` (or `ggsave(device = cairo_pdf)`), or embed with `grDevices::embedFonts()`.
- **Check** every PDF before submission: `pdffonts figure.pdf` should list each font with `emb` set to `yes`.

### S12. Each figure stands alone and agrees with the text

*Source: Tufte, BE ch. 5 ("content counts most of all"); convention.*

Every number on a figure matches the text and tables. A reader who sees only the figure and its caption can tell what was measured, in what units, on how many samples, and what the authors conclude from it.

## Library setup

### matplotlib (and seaborn)

```python
import matplotlib.pyplot as plt

MM = 1 / 25.4  # inches per millimeter

SCIENCE_RC = {
    # Type: Helvetica, Arial fallback; Nature sizes (5-7 pt)
    "font.family": "sans-serif",
    "font.sans-serif": ["Helvetica", "Arial", "TeX Gyre Heros", "Nimbus Sans",
                        "Liberation Sans", "DejaVu Sans"],
    "font.size": 7,
    "axes.labelsize": 7,
    "axes.titlesize": 7,
    "xtick.labelsize": 6,
    "ytick.labelsize": 6,
    "mathtext.default": "regular",   # math in the same face as the text
    "axes.unicode_minus": True,      # true minus sign

    # White page, black type, no top/right spines, no grid
    "figure.facecolor": "white",
    "axes.facecolor": "white",
    "savefig.facecolor": "white",
    "text.color": "black",
    "axes.labelcolor": "black",
    "axes.edgecolor": "black",
    "xtick.color": "black",
    "ytick.color": "black",
    "axes.spines.top": False,
    "axes.spines.right": False,
    "axes.grid": False,
    "legend.frameon": False,

    # Line widths that survive reduction (0.25-1 pt)
    "axes.linewidth": 0.5,
    "xtick.major.width": 0.5,
    "ytick.major.width": 0.5,
    "xtick.minor.width": 0.4,
    "ytick.minor.width": 0.4,
    "xtick.major.size": 2.5,
    "ytick.major.size": 2.5,
    "xtick.minor.size": 1.5,
    "ytick.minor.size": 1.5,
    "lines.linewidth": 1.0,
    "lines.markersize": 3,

    # Final size; vector output with embedded, editable TrueType fonts
    "figure.figsize": (89 * MM, 60 * MM),  # Nature single column
    "figure.dpi": 150,
    "savefig.dpi": 600,                    # raster exports only
    "savefig.bbox": "standard",            # "tight" trims the figure below the column width;
                                           # set margins with fig.subplots_adjust or a gridspec
    "pdf.fonttype": 42,
    "ps.fonttype": 42,
    "svg.fonttype": "none",
}

plt.rcParams.update(SCIENCE_RC)

OKABE_ITO = {  # colors that clear 3:1 on white, in order of use
    "blue": "#0072B2", "vermillion": "#D55E00",
    "bluish_green": "#009E73", "reddish_purple": "#CC79A7", "black": "#000000",
}
GRAY = "#666666"
```

`examples/matplotlib-publication.py` builds a complete two-panel figure with these settings, at exactly 89 mm: individual observations with means and 95% confidence intervals, a dose–response panel on a log axis with direct labels, bold panel letters and vector export. It checks the caption's claims against the data before saving and prints the caption. The rendered result is `_docs/tufte-scientific-figure.png`. For seaborn, pass the same dictionary: `sns.set_theme(style="ticks", rc=SCIENCE_RC)`.

### ggplot2

```r
library(ggplot2)

theme_science <- function(base_size = 7, family = "Helvetica") {
  theme_classic(base_size = base_size, base_family = family) +
    theme(
      text             = element_text(colour = "black"),
      axis.text        = element_text(colour = "black", size = base_size - 1),
      axis.line        = element_line(linewidth = 0.25),   # about 0.5 pt
      axis.ticks       = element_line(linewidth = 0.25),
      legend.position  = "none",                           # label directly
      plot.title       = element_blank(),                  # the caption carries it
      plot.background  = element_rect(fill = "white", colour = NA),
      strip.background = element_blank()
    )
}

# p <- ggplot(df, aes(dose, response, colour = condition)) + ... + theme_science()
ggsave("figure1.pdf", p, width = 89, height = 60, units = "mm", device = cairo_pdf)
```

A ggplot2 `linewidth` of 1 draws a line about 0.75 mm (about 2.1 pt) wide, so 0.25 gives about 0.5 pt, the axis weight in rule S9. Data lines at 1 pt take `linewidth = 0.47`.

### plotnine

```python
from plotnine import theme_classic, theme, element_text, element_blank

theme_science = theme_classic(base_size=7, base_family="Helvetica") + theme(
    text=element_text(color="black"),
    legend_position="none",
    plot_title=element_blank(),
)
# p.save("figure1.pdf", width=89, height=60, units="mm")
```

### Browser libraries (Plotly, Vega-Lite, Observable Plot, D3, ECharts, Chart.js)

These are built for screens. For a paper, export SVG or PDF at the final size, set the font family to `Helvetica, Arial, sans-serif`, apply the white background and the rules above, then check the exported file for embedded fonts and correct dimensions (rule S11).

## Validation checklist

Run this in place of `SKILL.md`'s items for background, title, serif type, screen sizes and interactivity; keep all the others.

- [ ] Width set in millimeters to the target column; nothing rescaled after export
- [ ] Helvetica (Arial for PLOS), one font and one size scale in every figure of the paper
- [ ] Text within the journal's range (Nature 5–7 pt; Science about 7 pt, never below 5 pt; PLOS 8–12 pt); panel letters in the journal's style
- [ ] Sentence case; true minus sign, ×, µ; units in every axis label
- [ ] White background; black text and axes
- [ ] No title, figure number or source line inside the artwork
- [ ] Caption: finding first, then every panel, every unlabeled encoding, what the error bars show, *n* and what it counts, and the test
- [ ] Individual observations shown for small samples; no bar of means with error bars for continuous data
- [ ] Bars only on linear axes starting at zero; log axes labeled with values
- [ ] Colors: gray first, Okabe–Ito for categories, a perceptually uniform map for quantities; grayscale test passed
- [ ] The same condition has the same color in every figure
- [ ] Lines between 0.25 pt and 1 pt
- [ ] Vector PDF or EPS with embedded TrueType fonts (`pdffonts` shows `emb yes`); rasters at 600 dpi at final width
- [ ] Every number on the figure matches the text

## References

**Tufte's books** are cited as in `SKILL.md`: *VDQI* = *The Visual Display of Quantitative Information* (2nd ed., Graphics Press, 2001); *EI* = *Envisioning Information* (1990); *VE* = *Visual Explanations* (1997); *BE* = *Beautiful Evidence* (2006).

**Literature**

- Cleveland WS. *The Elements of Graphing Data*, revised edition. Summit, NJ: Hobart Press; 1994.
- Crameri F, Shephard GE, Heron PJ. The misuse of colour in science communication. *Nature Communications*. 2020;11:5444. doi:10.1038/s41467-020-19160-7
- Cumming G, Fidler F, Vaux DL. Error bars in experimental biology. *Journal of Cell Biology*. 2007;177(1):7–11. doi:10.1083/jcb.200611141
- Krzywinski M, Altman N. Points of significance: Error bars. *Nature Methods*. 2013;10(10):921–922. doi:10.1038/nmeth.2659
- Krzywinski M, Altman N. Points of significance: Visualizing samples with box plots. *Nature Methods*. 2014;11(2):119–120. doi:10.1038/nmeth.2813
- Okabe M, Ito K. Color Universal Design (CUD): how to make figures and presentations that are friendly to colorblind people. 2008. https://jfly.uni-koeln.de/color/
- Rougier NP, Droettboom M, Bourne PE. Ten simple rules for better figures. *PLoS Computational Biology*. 2014;10(9):e1003833. doi:10.1371/journal.pcbi.1003833
- Vaux DL. Research methods: Know when your numbers are significant. *Nature*. 2012;492:180–181. doi:10.1038/492180a
- Wasserstein RL, Lazar NA. The ASA statement on p-values: context, process, and purpose. *The American Statistician*. 2016;70(2):129–133. doi:10.1080/00031305.2016.1154108
- Weissgerber TL, Milic NM, Winham SJ, Garovic VD. Beyond bar and line graphs: time for a new data presentation paradigm. *PLoS Biology*. 2015;13(4):e1002128. doi:10.1371/journal.pbio.1002128
- Wong B. Points of view: Color blindness. *Nature Methods*. 2011;8(6):441. doi:10.1038/nmeth.1618 (correction: doi:10.1038/s41592-023-01974-0)

**Journal guidelines** (read 16 November 2026; check the current version before submitting)

- Nature. Final submission. https://www.nature.com/nature/for-authors/final-submission
- Nature Research figure guide. Building and exporting figure panels. https://research-figure-guide.nature.com/figures/building-and-exporting-figure-panels/
- Nature Research figure guide. Extended Data formatting guidelines. https://research-figure-guide.nature.com/figures/extended-data-formatting-guidelines
- Science. Instructions for preparing an initial manuscript (sections "Preparation of figures" and "Typefaces and labels"). https://www.science.org/content/page/instructions-preparing-initial-manuscript
- PLOS. Figures. https://journals.plos.org/plosone/s/figures
- *Freshwater Science*. Preparing figures. https://www.journals.uchicago.edu/journals/fws/prep-art
- Cell Press. Figure guidelines. https://www.cell.com/information-for-authors/figure-guidelines (listed for reference; not quoted here, as the page could not be retrieved)

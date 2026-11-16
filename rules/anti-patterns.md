# Anti-Patterns: Detection and Fixes

Use this file when reviewing figure code or a finished figure for a scientific article. Rule numbers refer to `SKILL.md`; sources are named there.

## Quick reference

| Anti-pattern | Why it fails | Fix | Rule |
|---|---|---|---|
| **Bar of means with error bars** for continuous data ("dynamite plot") | Many different distributions give the same bar; the data are hidden | Every observation as a dot, with mean and 95% CI beside it | 9 |
| **Error bars not defined** | SD, SEM and CI bars of the same data differ in length and meaning | State in the caption what the bars show, *n* and what it counts | 10 |
| **Statistics on *n* = 2 or 3** | Error bars and p-values on so few points mislead | Plot the points | 10 |
| **Technical replicates as *n*** | Inflates certainty | Error bars across independent experiments only | 10 |
| **Asterisks with no definition** | The reader cannot tell the test or the threshold | Define each mark in the caption; give exact p-values and effect sizes | 11 |
| **Rainbow, jet or turbo color map** | Uneven lightness invents boundaries; unreadable for many readers | viridis, cividis or batlow; vik for diverging data | 8 |
| **Red against green** as the only contrast | Indistinguishable for the most common color-vision deficiencies | Okabe–Ito colors, plus position, shape or a label | 8 |
| **Legend box** | Shuttling between key and data | Direct labels; a key only for a color scale, unframed | 5 |
| **Gridlines, box, top and right spines** | Non-data-ink | Remove | 3, 6 |
| **Title inside the figure** | Duplicates the caption, wastes the column | Move it to the caption's first sentence | 15 |
| **All-caps or Title Case labels** | Harder to read; not the journal's style | Sentence case | 2 |
| **Rotated y-axis label** where space allows a horizontal one | Type should run horizontally | Label above the axis | 2 |
| **Text below 5 pt, or different sizes across figures** | Illegible after reduction; inconsistent | One scale, 5–7 pt (Nature) | 2 |
| **Figure drawn at screen size and scaled down** | Text and lines shrink below the journal's minimums | Draw at the final width in mm | 1 |
| **Rasterized text or unembedded fonts** | Journals ask for editable vector text | Vector PDF or EPS, TrueType fonts embedded | 18 |
| **Bars on a log axis, or a truncated bar axis** | A bar's length must be proportional to its value | Dots or lines on log axes; bars from zero | 7, 12 |
| **Log axis labeled with logarithms** | Readers cannot read back values | Label ticks with values | 12 |
| **Dual y-axes** | Implies a relation set by the choice of scales | Two panels on a shared x-axis | 7 |
| **Pie chart, 3D** | Low data density; distorted sizes | Sorted dot or bar plot; flat 2D | 7 |
| **Panels comparing one quantity on different scales** | Defeats comparison | Shared axis and range | 17 |
| **Reference line or target not in the data** | Invents context | Remove, or use a value the user supplies | 14 |
| **Different colors for the same condition** across figures | Design variation read as data variation | One color per condition throughout the paper | 8 |
| **Hatching or pattern fills** | Moiré vibration (chartjunk) | Lightness steps or direct labels | 8 |

## Per-library detection

### matplotlib

```
ax.bar(...) with yerr= on continuous data → strip_with_ci() from rules/matplotlib.md
ax.errorbar(..., capsize=N)              → capsize=0, elinewidth=0.5
ax.legend()                              → direct_label() at each series
ax.grid(True)                            → remove
ax.set_title("...")                      → move to the caption
cmap="jet" / "rainbow" / "turbo"         → cmap="viridis" or "cividis"
figsize=(10, 6) or other screen sizes    → figsize=(89 * MM, h * MM)
savefig(..., bbox_inches="tight")        → set margins; keep the column width
savefig("fig.png", dpi=150)              → savefig("fig.pdf") with pdf.fonttype 42
font.family default (DejaVu Sans)        → Helvetica, Arial fallback
ax.set_yscale("log") with bars           → dots or lines
```

### seaborn

```
sns.barplot(...) on continuous data      → sns.stripplot + sns.pointplot(errorbar=("ci", 95))
sns.set_theme() / sns.set_context("talk")→ sns.set_theme(style="ticks", rc=SCIENCE_RC)
palette="husl" / "Set1" / "rainbow"      → gray plus Okabe–Ito
legend from hue=                         → ax.get_legend().remove(); label directly
errorbar="sd" without saying so          → state SD in the caption, or use a CI
```

### ggplot2

```
geom_bar(stat = "summary") + geom_errorbar → geom_jitter + geom_pointrange with CI
theme_grey() / default theme             → theme_science()
legend.position = "right"                → "none" + geom_text direct labels
ggtitle("...")                           → caption
scale_*_gradientn(colours = rainbow(n))  → scale_*_viridis_c(option = "cividis") or scico
ggsave(..., device = pdf) with Helvetica → device = cairo_pdf
ggsave(width = 7, height = 5)            → width = 89, units = "mm"
scale_x_log10() with default labels      → breaks and labels given as values
```

### plotnine

```
geom_col / stat_summary bars on continuous data → geom_jitter + geom_pointrange
theme_gray() default                     → theme_science
legend_position="right"                  → "none" + geom_text direct labels
p.save(width=6.4, height=4.8)            → width=89, units="mm"
```

## The "can I remove it?" test

For each element of the figure, ask: if I remove this, does the reader lose information about the data? If not, remove it (Tufte, VDQI ch. 4: erase non-data-ink, within reason). Then ask the opposite question about the caption: could a reader with only the figure and its caption tell what was measured, how, on how many samples, and what it shows? If not, add it (rule 15).

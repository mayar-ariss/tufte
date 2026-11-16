# Anti-Patterns: Detection and Fixes

Use this file when reviewing figure code or a finished figure for a scientific article. Rule numbers refer to `SKILL.md`; sources are named there.

## Quick reference

| Anti-pattern | Why it fails | Fix | Rule |
|---|---|---|---|
| **Summaries without the data** | The reader cannot see the evidence | Show the observations, the summary over them | 1 |
| **Comparison spread across figures** | "Compared to what?" is not answered on the page | Side by side, one scale, one eyespan | 3 |
| **Explanatory variable in a key or panel order** | The cause cannot be seen | Put it on an axis; order by it | 4 |
| **Missing zeros, non-responders or controls** | The comparison that reveals the cause is gone (the Challenger lesson) | Include every case | 4 |
| **Categories in alphabetical order** | Hides the pattern | Order by value or by the explanatory variable | 4 |
| **Notes, values or symbol keys written on the figure** | Nature puts text, including keys to symbols, in the caption where possible | Labels only on the graphic; values, notes and symbol definitions in the caption | 6, 22 |
| **Colored text, or series named by color in the caption** ("the red line") | Nature recolours colored text; color descriptions fail color-deficient readers | Black direct labels beside each series; name series in the caption as they are labeled | 7, 21 |
| **A sparse figure** that could carry more of the data | Low data density | Add the detail: individual observations, more variables | 8 |
| **Every element the same weight** | Clutter; 1 + 1 = 3 effects | Layer: data darkest, references lighter, axes lightest | 11 |
| **Bar of means with error bars** for continuous data ("dynamite plot") | Many different distributions give the same bar; the data are hidden | Every observation as a dot, with mean and 95% CI beside it | 1, 15 |
| **Error bars not defined** | SD, SEM and CI bars of the same data differ in length and meaning | State in the caption what the bars show, *n* and what it counts | 16 |
| **Statistics on *n* = 2 or 3** | Error bars and p-values on so few points mislead | Plot the points | 16 |
| **Technical replicates as *n*** | Inflates certainty | Error bars across independent experiments only | 16 |
| **Asterisks with no definition** | The reader cannot tell the test or the threshold | Define each mark in the caption; give exact p-values and effect sizes | 17 |
| **Rainbow, jet or turbo color map** | Uneven lightness invents boundaries; unreadable for many readers | viridis, cividis or batlow; vik for diverging data | 12 |
| **Strong color over large areas**, or several categories colored by default | Bright fills side by side are loud and pull the picture apart (Imhof, via Tufte); color does work position or a label could do | Black and grays first, one red accent; light gray or a pale tint for large areas; separate categories by position, labels or small multiples | 12 |
| **Red against green** as the only contrast | Indistinguishable for the most common color-vision deficiencies | The red accent against grays, blue as a second; Okabe–Ito for several categories; plus position, shape or a label | 12 |
| **Key box** | Shuttling between key and data | Direct labels; symbols defined in the caption; a key only for a color scale, unframed | 7 |
| **Gridlines, box, top and right spines** | Non-data-ink; Nature avoids background gridlines | Remove; values that must be read exactly go in a table or the caption | 9 |
| **Drop shadows, decorative icons** | Decoration; Nature avoids both | Remove; text labels instead of icons | 9 |
| **Title inside the figure** | Duplicates the caption, wastes the column | Make it the brief title that opens the caption | 22 |
| **Caption of 300 words or more, or with methods** | Nature's limit; methods belong in the Methods section | Brief title, each panel and its symbols, statistics; under 300 words | 22 |
| **All-caps or Title Case labels** | Harder to read; not Nature's style | Lower case with an initial capital, no full stop | 13, 21 |
| **Rotated y-axis label** where space allows a horizontal one | Type should run horizontally | Label above the axis | 13 |
| **Text below 5 pt, or different sizes across figures** | Illegible after reduction; inconsistent | One scale, 5–7 pt (Nature) | 21 |
| **Figure drawn at screen size and scaled down** | Text and lines shrink below the journal's minimums | Draw at the final width in mm | 20 |
| **Rasterized text, unembedded fonts, or a PNG, JPEG or TIFF main figure** | Nature asks for editable vector text and does not accept these formats for main figures | Vector AI, EPS or PDF, TrueType fonts embedded | 25 |
| **Bars on a log axis, or a truncated bar axis** | A bar's length must be proportional to its value | Dots or lines on log axes; bars from zero | 2, 18 |
| **Log axis labeled with logarithms** | Readers cannot read back values | Label ticks with values | 18 |
| **Dual y-axes** | Implies a relation set by the choice of scales | Two panels on a shared x-axis | 14 |
| **Pie chart, 3D** | Low data density; distorted sizes | Sorted dot or bar plot; flat 2D | 2, 14 |
| **Panels comparing one quantity on different scales** | Defeats comparison | Shared axis and range | 3, 5 |
| **Reference line or target not in the data** | Invents context | Remove, or use a value the user supplies | 3 |
| **Different colors for the same condition** across figures | Design variation read as data variation | One color per condition throughout the paper | 2, 12 |
| **Hatching or pattern fills** | Moiré vibration (chartjunk); Nature asks for solid fills | Solid lightness steps or direct labels | 9 |

## Per-library detection

### matplotlib

```
ax.bar(...) with yerr= on continuous data → strip_with_ci() from rules/matplotlib.md
ax.errorbar(..., capsize=N)              → capsize=0, elinewidth=0.5
ax.legend()                              → direct_label() at each series
ax.grid(True)                            → remove
ax.set_title("...")                      → the brief title opening the caption
ax.text(..., "n = 8") / values on plot   → the caption
color=... on ax.text or a label          → black
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
palette="husl" / "Set1" / "rainbow"      → grays plus the red accent; Okabe–Ito for several categories
key (legend) from hue=                   → ax.get_legend().remove(); label directly
errorbar="sd" without saying so          → state SD in the caption, or use a CI
```

### ggplot2

```
geom_bar(stat = "summary") + geom_errorbar → geom_jitter + geom_pointrange with CI
theme_grey() / default theme             → theme_science()
legend.position = "right"                → "none" + black geom_text direct labels
ggtitle("...")                           → caption title
scale_*_gradientn(colours = rainbow(n))  → scale_*_viridis_c(option = "cividis") or scico
ggsave(..., device = pdf) with Helvetica → device = cairo_pdf
ggsave(width = 7, height = 5)            → width = 89, units = "mm"
scale_x_log10() with default labels      → breaks and labels given as values
```

### plotnine

```
geom_col / stat_summary bars on continuous data → geom_jitter + geom_pointrange
theme_gray() default                     → theme_science
legend_position="right"                  → "none" + black geom_text direct labels
p.save(width=6.4, height=4.8)            → width=89, units="mm"
```

## The "remove it, add it" test

For each element of the figure, ask: if I remove this, does the reader lose information about the data? If not, remove it (Tufte, VDQI ch. 4: erase non-data-ink, within reason). Then ask the opposite question, which matters as much to Tufte: what could I add that would help the reader — the individual observations, a comparison, a label, a value? Add data and labels to the graphic, keeping it readable by layering (rules 8, 11); add values and notes to the caption (rule 6). Finally, could a reader with only the figure and its caption tell what was measured, how, on how many samples, and what it shows? If not, add it to the legend (rule 22).

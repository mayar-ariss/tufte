# Multi-Panel Figures, Small Multiples and Tufte's Designs

Load this file for figures with more than one panel, and for Tufte's own designs: small multiples, slopegraphs, quartile plots, dot-dash plots and sparklines. Rule numbers refer to `SKILL.md`. The helpers named here (`range_frame`, `panel_letters`, `quartile_plot`, `paired_plot`) are defined in `rules/matplotlib.md`; ggplot2 and plotnine equivalents are in `rules/ggplot2-plotnine.md`.

## Multi-panel figures

*Source: Journal (Nature final submission, formatting guide and figure guide) for letters, layout and legends; convention for the rest.*

1. **Plan the grid at the final width** (89 or 183 mm, at most 170 mm tall). Give each panel the space its content and legibility need; equal panels are not required. Lay panels out neatly and space-efficiently, with little white space.
2. **More than one panel only when the parts are logically connected**, in alphabetical order (Journal, Nature).
3. **Letter every panel** in Nature's style: 8 pt bold, upright, lowercase (a, b, c), top left of each panel, aligned on one grid. No sub-part labels such as c(i) (convention).
4. **Label common axes once**, on the outer edge (convention).
5. **One font, one size scale, one color per condition** across all panels and all figures of the paper (Journal, Nature; Tufte, integrity principle 3).
6. **The figure legend describes each panel by its letter**, in order, with the symbols used (Journal, Nature; SKILL.md rule 22).

## Small multiples

*Source: Tufte, EI ch. 4.*

Tufte describes small multiples as illustrations "of postage-stamp size" that repeat one design, indexed by category, sequenced over time, or ordered by a variable. Because the design stays constant, the eye compares the data, not the graphics.

1. **Same scale in every panel** when the panels show the same quantity. Never let each panel scale itself; if a panel must differ, say so in the figure legend.
2. **Same design in every panel**: same marks, colors, axis ranges and aspect.
3. **Label each panel once**, with its category, in the panel's top left, at the text size of the figure.
4. **No panel borders**; whitespace separates panels.
5. **Order the panels by something meaningful** (time, magnitude, geography), not alphabetically, unless the reader must look them up.
6. **Design for two readings** (Tufte, EI ch. 2): when a panel summarizes several subjects, draw each subject as a thin light line or small dot under the mean, so the figure reads as a pattern at a glance and as individuals up close. Layer them: individuals lightest, the summary darker, the highlight darkest (SKILL.md rule 11).
7. **Give the key values in the figure legend** (SKILL.md rule 6): the ending value of each panel's summary, the change, *n*. On the panels: the category labels and the axes.

In matplotlib, `plt.subplots(..., sharey=True)` keeps one scale; see the example in `rules/matplotlib.md`. In ggplot2 and plotnine, `facet_wrap` keeps scales fixed unless `scales = "free"` is set.

## Slopegraphs and paired data

*Source: Tufte, VDQI pp. 158–159, where he introduced the design as a "table-graphic"; Literature (Weissgerber et al. 2015) for paired data.*

- **Paired or repeated measures:** one line per subject between conditions, so the reader sees whether the change is consistent across subjects. A bar of each condition's mean hides this (Weissgerber et al. 2015). `paired_plot()` draws it.
- **Change between two times across categories:** label both ends with the name and value; gray by default, color only the slopes the finding is about; no axes when the labels carry the values.

## Quartile plots

*Source: Tufte, VDQI ch. 6 — his redesign of the box plot by erasing non-data-ink.*

Drop the box. Draw lines from the minimum to the lower quartile and from the upper quartile to the maximum, leave the middle half as a gap, and mark the median with a dot. `quartile_plot()` draws it.

- It shows the five-number summary (minimum, quartiles, median, maximum), not Tukey's whiskers and outliers; say which in the figure legend.
- Use it, or a box plot, for at least five observations per group (Literature, Krzywinski and Altman 2014); for fewer, plot the points (SKILL.md rule 15).

## Dot-dash plots (rug marks)

*Source: Tufte, the dot-dash-plot, VDQI ch. 6.*

Show the marginal distributions of a scatter plot as short ticks along each axis, in light gray. In matplotlib:

```python
def rug_marks(ax, x, y, color="#8c8c8c", size=3):
    """Tufte's dot-dash plot: marginal ticks along both axes."""
    ax.plot(x, [ax.get_ylim()[0]] * len(x), "|", color=color, markersize=size, clip_on=False)
    ax.plot([ax.get_xlim()[0]] * len(y), y, "_", color=color, markersize=size, clip_on=False)
```

In ggplot2: `geom_rug(colour = "#8c8c8c", linewidth = 0.25)`.

## Sparklines in tables

*Source: Tufte, BE ch. 2 ("data-intense, design-simple, word-sized graphics"), pp. 46–63.*

In a paper, sparklines belong in tables, beside the numbers they summarize.

1. No axes and no gridlines, but the beginning and ending values as numbers beside the line.
2. Small dots for reference values: first and last values in red, low and high in blue (BE pp. 50–51). Use the accent red `#CC0000` and the blue `#0072B2` (rule 12).
3. A light gray band for the normal range when the data have one.
4. Bank to 45°: set the width so the slopes average about 45° (Tufte, after Cleveland).
5. The height of a line of text; same scale down a column when rows are compared.

# matplotlib and seaborn

Load this file when generating matplotlib or seaborn code for a figure in a scientific article.

**Written for matplotlib 3.8+, seaborn 0.13 and SciPy 1.x.** The rules come from `SKILL.md`, where each names its source; the code below is implementation, not principle. The code blocks in this file are run by the repository's own checks (`_docs/generate_showcase.py` uses the same helpers).

## Setup

Apply at the top of every script or notebook. Sizes follow Nature (5–7 pt, 89 mm); change `font.size`, the tick sizes and the width for another journal (`rules/journals.md`).

```python
import matplotlib.pyplot as plt
import numpy as np

MM = 1 / 25.4  # inches per millimeter

SCIENCE_RC = {
    # Type: Helvetica, Arial fallback (rule 21)
    "font.family": "sans-serif",
    "font.sans-serif": ["Helvetica", "Arial", "TeX Gyre Heros", "Nimbus Sans",
                        "Liberation Sans", "DejaVu Sans"],
    "font.size": 7,
    "axes.labelsize": 7,
    "axes.titlesize": 7,
    "xtick.labelsize": 6,
    "ytick.labelsize": 6,
    "legend.fontsize": 6,
    "mathtext.default": "regular",   # math in the same face as the text
    "axes.unicode_minus": True,      # true minus sign

    # White page, black type, no frame, no grid (rule 9)
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

    # Line weights that survive reduction: 0.25-1 pt (rule 23)
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

    # Final size and vector output with embedded TrueType fonts (rules 20, 25)
    "figure.figsize": (89 * MM, 60 * MM),
    "figure.dpi": 150,
    "savefig.dpi": 600,          # raster exports only
    "savefig.bbox": "standard",  # "tight" trims the figure below the column width
    "pdf.fonttype": 42,
    "ps.fonttype": 42,
    "svg.fonttype": "none",
}
plt.rcParams.update(SCIENCE_RC)

GRAY = "#666666"
LIGHT = "#8c8c8c"
RED = "#CC0000"          # the accent (rule 12): the finding, with its value beside it
BLUE = "#0072B2"         # second accent, only when needed
FIELD = "#e5e5e5"        # muted field: normal ranges, bands, large areas
FIELD_BLUE = "#dce9f5"   # muted field: water, a second large area
HIGHLIGHT = RED
# Fallback when three or more categories must be colored (rule 12)
OKABE_ITO = {"blue": "#0072B2", "vermillion": "#D55E00",
             "bluish_green": "#009E73", "reddish_purple": "#CC79A7", "black": "#000000"}

# Layers, darkest to lightest (rule 11): data, then summaries, then references, then axes
LAYER = {"data": "black", "summary": "black", "context": GRAY, "reference": LIGHT,
         "leader": "#999999"}
```

Set margins with `fig.subplots_adjust` or a gridspec, not `bbox_inches="tight"`, so the saved figure keeps the column width.

## Helpers

```python
from scipy import stats


def range_frame(ax, x=None, y=None, label_ends=False, fmt="{:g}"):
    """Tufte's range frame (rule 10): each axis line spans only its data.
    label_ends=True also labels the frame's ends with the data's minimum and maximum,
    so the axis reports the range (a multifunctioning element, rule 8). Call it after
    the axis limits and ticks are final; fmt applies to every axis given."""
    for data, spine, axis in ((x, "bottom", ax.xaxis), (y, "left", ax.yaxis)):
        if data is None:
            continue
        lo, hi = float(np.min(data)), float(np.max(data))
        ax.spines[spine].set_bounds(lo, hi)
        if label_ends:
            gap = 0.12 * (hi - lo)   # drop interior ticks that would crowd the ends
            inner = [t for t in axis.get_ticklocs() if lo + gap < t < hi - gap]
            ticks = [lo] + inner + [hi]
            axis.set_ticks(ticks, [fmt.format(t) for t in ticks])


def horizontal_ylabel(ax, text):
    """Y-axis label set horizontally above the axis (rule 13)."""
    ax.set_ylabel("")
    ax.text(0, 1.04, text, transform=ax.transAxes, ha="left", va="bottom")


def direct_label(ax, x, y, text, dx=4, dy=0, ha="left"):
    """Name a series where it is (rule 7), in black: Nature recolours colored text,
    and position ties the label to its series. dx, dy are offsets in points.
    Values and notes go in the caption, not here (rule 6)."""
    ax.annotate(text, xy=(x, y), xytext=(dx, dy), textcoords="offset points",
                ha=ha, va="center", color="black")


def panel_letters(fig, axes, dx=-0.07, dy=0.06):
    """Nature's panel letters (rule 24): 8 pt bold, upright, lowercase a, b, c,
    at each panel's top left."""
    for letter, ax in zip("abcdefghijklmnopqrstuvwxyz", axes):
        box = ax.get_position()
        fig.text(box.x0 + dx, box.y1 + dy, letter, fontsize=8,
                 fontweight="bold", ha="left", va="bottom")


def mean_ci(values, level=0.95):
    """Mean and half-width of its confidence interval (t distribution)."""
    values = np.asarray(values, dtype=float)
    n = values.size
    half = stats.t.ppf(0.5 + level / 2, n - 1) * values.std(ddof=1) / np.sqrt(n)
    return values.mean(), half


def strip_with_ci(ax, groups, colors=None, jitter=0.12, seed=0):
    """Every observation as a dot, with the mean and 95% CI beside it (rules 1, 15, 16).
    groups: dict of name -> values. Returns the dict of (mean, half-width), for the
    caption (rules 6, 22)."""
    rng = np.random.default_rng(seed)
    summary = {}
    for i, (name, values) in enumerate(groups.items()):
        values = np.asarray(values, dtype=float)
        color = (colors or {}).get(name, GRAY)
        ax.scatter(i + rng.uniform(-jitter, jitter, values.size), values,
                   s=6, color=color, linewidths=0, zorder=2)
        m, h = mean_ci(values)
        ax.plot([i + 0.24] * 2, [m - h, m + h], color="black", lw=0.5)
        ax.plot([i + 0.17, i + 0.31], [m, m], color="black", lw=1.0)
        summary[name] = (m, h)
    ax.set_xticks(range(len(groups)), list(groups))
    ax.tick_params(axis="x", length=0)
    ax.spines["bottom"].set_visible(False)
    ax.set_xlim(-0.5, len(groups) - 0.4)
    range_frame(ax, y=np.concatenate([np.asarray(v, float) for v in groups.values()]))
    return summary


def quartile_plot(ax, groups, color=GRAY):
    """Tufte's quartile plot (VDQI ch. 6): no box; lines from the extremes to the
    quartiles, a gap for the middle half, a dot at the median."""
    for i, values in enumerate(groups.values()):
        lo, q1, med, q3, hi = np.percentile(values, [0, 25, 50, 75, 100])
        ax.vlines(i, lo, q1, color=color, lw=1)
        ax.vlines(i, q3, hi, color=color, lw=1)
        ax.plot(i, med, "o", color=color, markersize=3)
    ax.set_xticks(range(len(groups)), list(groups))
    ax.tick_params(axis="x", length=0)
    ax.spines["bottom"].set_visible(False)


def paired_plot(ax, before, after, labels=("Before", "After"), highlight=None):
    """One line per subject between two conditions (rule 15; Tufte's slopegraph).
    highlight: optional boolean array of subjects to draw in the accent color."""
    before, after = np.asarray(before, float), np.asarray(after, float)
    for i, (b, a) in enumerate(zip(before, after)):
        on = highlight is not None and highlight[i]
        ax.plot([0, 1], [b, a], color=HIGHLIGHT if on else LIGHT,
                lw=1.0 if on else 0.6, marker="o", markersize=2.5, zorder=3 if on else 2)
    ax.set_xticks([0, 1], labels)
    ax.tick_params(axis="x", length=0)
    ax.spines["bottom"].set_visible(False)
    ax.set_xlim(-0.25, 1.25)
    range_frame(ax, y=np.concatenate([before, after]))


def log_axis(ax, axis="x", ticks=(0.01, 0.1, 1, 10, 100)):
    """Log axis labeled with values, not logarithms (rule 18)."""
    from matplotlib.ticker import FixedLocator, NullLocator
    set_scale = ax.set_xscale if axis == "x" else ax.set_yscale
    target = ax.xaxis if axis == "x" else ax.yaxis
    set_scale("log")
    target.set_major_locator(FixedLocator(ticks))
    target.set_minor_locator(NullLocator())
    target.set_ticklabels([f"{t:g}" for t in ticks])
```

`mean_ci` uses the t distribution, which suits small samples of roughly normal data. For skewed data, show medians with a bootstrap interval and say so in the caption.

## Complete example: individual observations with 95% CIs

```python
rng = np.random.default_rng(7)
groups = {"Control": rng.normal(1.00, 0.12, 8),
          "Drug A": rng.normal(1.12, 0.12, 8),
          "Drug B": rng.normal(1.55, 0.14, 8)}

fig = plt.figure(figsize=(60 * MM, 50 * MM))
ax = fig.add_axes([0.2, 0.15, 0.75, 0.68])
summary = strip_with_ci(ax, groups, colors={"Drug B": HIGHLIGHT})
horizontal_ylabel(ax, "Response (a.u.)")      # on the graphic: labels only (rule 6)
fig.savefig("figure1.pdf")

# The caption, in Nature's form (rule 22), checked against the data
assert summary["Drug B"][0] - summary["Drug B"][1] > summary["Control"][0] + summary["Control"][1]
means = ", ".join(f"{name} {m:.2f}" for name, (m, _) in summary.items())
caption = ("Drug B raises the response. Dots, individual cultures; horizontal lines, means; "
          "vertical lines, 95% confidence intervals of the mean (t distribution); "
          f"n = 8 independent cultures per group. Means: {means} a.u.")
assert len(caption.split()) < 300   # Nature's limit
print(caption)
```

On the graphic: the group names and the axis label. In the caption: the title (here also the finding), what each mark means, the interval, *n* and the means, the values Tufte would have written on the graphic (rule 6). Nature's captions never name a series by its color.

For a two-panel version with a log dose axis and the half-maximal doses marked on the curves, see `examples/matplotlib-publication.py`.

## Small multiples on one scale, with two readings

```python
regions = {"North": rng.normal(0, 1, 12).cumsum(), "South": rng.normal(0.4, 1, 12).cumsum(),
           "East": rng.normal(0, 1, 12).cumsum(), "West": rng.normal(0.6, 1, 12).cumsum()}
lo = min(v.min() for v in regions.values())
hi = max(v.max() for v in regions.values())

fig, axes = plt.subplots(1, 4, figsize=(183 * MM, 40 * MM), sharey=True)
for ax, (name, values) in zip(axes, regions.items()):
    ax.plot(np.arange(1, 13), values, color=GRAY)
    ax.text(0, 1.04, name, transform=ax.transAxes, ha="left", va="bottom")
    range_frame(ax, x=[1, 12], y=[lo, hi])
for ax in axes[1:]:
    ax.spines["left"].set_visible(False)
    ax.tick_params(axis="y", left=False)
fig.subplots_adjust(left=0.06, right=0.99, bottom=0.18, top=0.82, wspace=0.12)
```

`sharey=True` keeps every panel on one scale (rule 5); the panel names sit where a title would, in the same 7 pt type. Ending values, if they matter, go in the caption (rule 6). When each panel summarizes several subjects, draw each subject as a thin light line under the mean, so the figure reads as a pattern at a glance and as individuals up close (rule 11); `_docs/generate_showcase.py` does this for the README's small multiples.

## Export and check

```python
fig.savefig("figure1.pdf")                      # main figure: vector, fonts embedded as TrueType
fig.savefig("extended_data_fig1.jpg", dpi=300)  # Extended Data only: RGB JPEG, at most 300 dpi
```

Then check the PDF: `pdffonts figure1.pdf` should list each font with `emb` set to `yes`, and the page size should equal the column width. Nature does not accept JPEG, TIFF or PNG for main figures (rule 25).

## seaborn

```python
import seaborn as sns

sns.set_theme(style="ticks", rc=SCIENCE_RC)   # keeps the settings above
```

```python
import pandas as pd

df = pd.DataFrame([(name, v) for name, values in groups.items() for v in values],
                  columns=["group", "response"])
fig, ax = plt.subplots(figsize=(60 * MM, 50 * MM))
sns.stripplot(data=df, x="group", y="response", color=GRAY, size=2.5, jitter=0.12, ax=ax)
sns.pointplot(data=df, x="group", y="response", errorbar=("ci", 95), color="black",
              markers="_", markersize=6, linestyle="none", err_kws={"linewidth": 0.5}, ax=ax)
if ax.get_legend() is not None:   # seaborn adds a key (legend) when hue= is used
    ax.get_legend().remove()
ax.set_xlabel("")
horizontal_ylabel(ax, "Response (a.u.)")
```

- seaborn's `errorbar=("ci", 95)` is a bootstrap interval; say so in the caption, or compute the interval yourself with `mean_ci`.
- Never `sns.barplot` for continuous data (rule 15); use `stripplot` or `swarmplot` with `pointplot`.
- Prefer a single gray with `HIGHLIGHT` on the finding; `OKABE_ITO` values only when several categories must be colored; never the default palette.

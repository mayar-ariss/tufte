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
OKABE_ITO = {"blue": "#0072B2", "vermillion": "#D55E00",
             "bluish_green": "#009E73", "reddish_purple": "#CC79A7", "black": "#000000"}
HIGHLIGHT = OKABE_ITO["blue"]

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
    so the axis reports the range (a multifunctioning element, rule 8)."""
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


def direct_label(ax, x, y, text, color="black", dx=4, dy=0, ha="left"):
    """Label a series where it is (rule 7). dx, dy are offsets in points."""
    ax.annotate(text, xy=(x, y), xytext=(dx, dy), textcoords="offset points",
                ha=ha, va="center", color=color)


def note(ax, x, y, text, dx=8, dy=8, ha="left", color="black"):
    """Write an explanation or a value on the graphic beside what it explains
    (rule 6), with a thin light leader line (rule 11). dx, dy are offsets in points."""
    ax.annotate(text, xy=(x, y), xytext=(dx, dy), textcoords="offset points",
                ha=ha, va="center", color=color,
                arrowprops=dict(arrowstyle="-", color=LAYER["leader"], lw=0.4,
                                shrinkA=1, shrinkB=2))


def panel_letters(fig, axes, style="nature", dx=-0.07, dy=0.06):
    """Bold panel letters at each panel's top left (rule 24).
    style="nature": 8 pt lowercase a, b, c; style="science": 10 pt capitals A, B, C."""
    letters = "abcdefghijklmnopqrstuvwxyz"
    size = 8 if style == "nature" else 10
    for i, ax in enumerate(axes):
        letter = letters[i] if style == "nature" else letters[i].upper()
        box = ax.get_position()
        fig.text(box.x0 + dx, box.y1 + dy, letter, fontsize=size,
                 fontweight="bold", ha="left", va="bottom")


def mean_ci(values, level=0.95):
    """Mean and half-width of its confidence interval (t distribution)."""
    values = np.asarray(values, dtype=float)
    n = values.size
    half = stats.t.ppf(0.5 + level / 2, n - 1) * values.std(ddof=1) / np.sqrt(n)
    return values.mean(), half


def strip_with_ci(ax, groups, colors=None, jitter=0.12, seed=0, write_means=False, fmt="{:.2f}"):
    """Every observation as a dot, with the mean and 95% CI beside it (rules 1, 15, 16).
    write_means=True writes each mean's value beside it (rule 6).
    groups: dict of name -> values. Returns the dict of (mean, half-width)."""
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
        if write_means:
            ax.text(i + 0.34, m, fmt.format(m), ha="left", va="center")
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
    highlight: optional boolean array of subjects to draw in blue."""
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
summary = strip_with_ci(ax, groups, colors={"Drug B": HIGHLIGHT}, write_means=True)
horizontal_ylabel(ax, "Response (a.u.)")
ax.text(1, 1.04, "n = 8 cultures per group", transform=ax.transAxes, ha="right",
        va="bottom", color=GRAY)                       # evidence on the graphic (rule 6)
fig.savefig("figure1.pdf")

# Check the caption's claim before writing it (rule 22)
assert summary["Drug B"][0] - summary["Drug B"][1] > summary["Control"][0] + summary["Control"][1]
```

Caption: "Drug B raises the response. Dots are individual cultures (*n* = 8 independent cultures per group); black lines show the mean and its 95% confidence interval, with the mean's value beside it."

The figure carries its own evidence: the groups, every culture, the means as numbers and *n* are all on the graphic (rule 6); the caption documents what the graphic cannot (rule 22).

For a two-panel version with a log dose axis, the half-maximal doses marked on the curves and direct labels, see `examples/matplotlib-publication.py`.

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
    direct_label(ax, 12, values[-1], f"{values[-1]:.1f}")       # the ending value (rule 6)
    range_frame(ax, x=[1, 12], y=[lo, hi])
for ax in axes[1:]:
    ax.spines["left"].set_visible(False)
    ax.tick_params(axis="y", left=False)
fig.subplots_adjust(left=0.06, right=0.99, bottom=0.18, top=0.82, wspace=0.12)
```

`sharey=True` keeps every panel on one scale (rule 5); the panel names sit where a title would, in the same 7 pt type. When each panel summarizes several subjects, draw each subject as a thin light line under the mean, so the figure reads as a pattern at a glance and as individuals up close (rule 11); `_docs/generate_showcase.py` does this for the README's small multiples.

## Export and check

```python
fig.savefig("figure1.pdf")           # vector, fonts embedded as TrueType
fig.savefig("figure1.tiff", dpi=600, pil_kwargs={"compression": "tiff_lzw"})  # only if the journal asks
```

Then check the PDF: `pdffonts figure1.pdf` should list each font with `emb` set to `yes`, and the page size should equal the column width.

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
if ax.get_legend() is not None:   # seaborn adds a legend when hue= is used
    ax.get_legend().remove()
ax.set_xlabel("")
horizontal_ylabel(ax, "Response (a.u.)")
```

- seaborn's `errorbar=("ci", 95)` is a bootstrap interval; say so in the caption, or compute the interval yourself with `mean_ci`.
- Never `sns.barplot` for continuous data (rule 15); use `stripplot` or `swarmplot` with `pointplot`.
- Prefer `palette=OKABE_ITO` values or a single gray; never the default palette for more than one highlight.

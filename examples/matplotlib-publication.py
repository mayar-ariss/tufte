"""A two-panel figure for a journal article, drawn by the rules in SKILL.md.

Tufte governs the style: every observation shown, the comparison side by side,
dose (the explanatory variable) on the x-axis, the half-maximal doses marked on
the curves, black direct labels, range frames whose ends report the data's
range, and layers from dark data to light references. Nature governs the
structure: single column (89 mm), Helvetica (Arial or a metric clone where
Helvetica is not installed), labels only on the figure, the values, n and symbol
definitions in the figure legend, 8 pt bold lowercase panel letters, and vector
PDF output with embedded TrueType fonts.

The data are synthetic, generated below with a fixed seed. The script checks the
legend's claims against the data before saving, and prints the legend.

Usage:
    python3 examples/matplotlib-publication.py [output_directory]

Writes figure1.pdf (for submission) and figure1.png (a preview only: Nature does not
accept PNG for main figures).
Written for matplotlib 3.x and NumPy 1.x/2.x.
"""

import sys
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import FixedLocator, NullLocator

MM = 1 / 25.4  # inches per millimeter

SCIENCE_RC = {
    "font.family": "sans-serif",
    "font.sans-serif": ["Helvetica", "Arial", "TeX Gyre Heros", "Nimbus Sans",
                        "Liberation Sans", "DejaVu Sans"],
    "font.size": 7,
    "axes.labelsize": 7,
    "axes.titlesize": 7,
    "xtick.labelsize": 6,
    "ytick.labelsize": 6,
    "mathtext.default": "regular",
    "axes.unicode_minus": True,
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
    "axes.linewidth": 0.5,
    "xtick.major.width": 0.5,
    "ytick.major.width": 0.5,
    "xtick.major.size": 2.5,
    "ytick.major.size": 2.5,
    "lines.linewidth": 1.0,
    "lines.markersize": 3,
    "savefig.dpi": 600,
    "savefig.bbox": "standard",  # "tight" would trim the figure below the column width
    "pdf.fonttype": 42,
    "ps.fonttype": 42,
    "svg.fonttype": "none",
}

GRAY = "#666666"
HIGHLIGHT = "#CC0000"  # the accent red (rule 12); labels stay black (rule 7)
T975 = {3: 3.182, 7: 2.365}  # two-sided 95% t quantiles for the degrees of freedom used here


def mean_ci(values):
    """Mean and half-width of the 95% confidence interval (t distribution)."""
    values = np.asarray(values, dtype=float)
    n = values.size
    return values.mean(), T975[n - 1] * values.std(ddof=1) / np.sqrt(n)


def make_data(seed=7):
    rng = np.random.default_rng(seed)
    groups = {  # panel a: response of 8 independent cultures per group
        "Control": rng.normal(1.00, 0.12, 8),
        "Drug A": rng.normal(1.12, 0.12, 8),
        "Drug B": rng.normal(1.55, 0.14, 8),
    }
    dose = np.logspace(-2, 2, 9)  # panel b: 0.01 to 100 µM, 4 cultures per dose

    def hill(d, ec50):
        return 0.05 + 0.95 * d / (d + ec50)

    curves = {
        "Control": np.array([hill(d, 3.0) + rng.normal(0, 0.04, 4) for d in dose]),
        "Drug B": np.array([hill(d, 0.3) + rng.normal(0, 0.04, 4) for d in dose]),
    }
    return groups, dose, curves


def half_max_dose(dose, means):
    """Dose where the mean response crosses half its range, interpolated in log dose."""
    half = means.min() + (means.max() - means.min()) / 2
    i = int(np.argmax(means >= half))
    x0, x1 = np.log10(dose[i - 1]), np.log10(dose[i])
    y0, y1 = means[i - 1], means[i]
    return 10 ** (x0 + (half - y0) * (x1 - x0) / (y1 - y0))


def range_frame(ax, axis, lo, hi):
    """Tufte's range-frame (VDQI ch. 6): the axis line spans only the data."""
    ax.spines["left" if axis == "y" else "bottom"].set_bounds(lo, hi)


def horizontal_ylabel(ax, text):
    """Y-axis label set horizontally above the axis (rule 13)."""
    ax.text(0, 1.04, text, transform=ax.transAxes, ha="left", va="bottom")


def panel_letter(fig, ax, letter):
    """Bold upright lowercase panel letter, Nature style, at the panel's top left."""
    box = ax.get_position()
    fig.text(box.x0 - 0.075, box.y1 + 0.075, letter, fontsize=8, fontweight="bold",
             ha="left", va="bottom")


def main(outdir):
    plt.rcParams.update(SCIENCE_RC)
    groups, dose, curves = make_data()

    # Check the legend's claims against the data before drawing anything.
    stats = {name: mean_ci(v) for name, v in groups.items()}
    assert stats["Drug B"][0] - stats["Drug B"][1] > max(
        stats["Control"][0] + stats["Control"][1], stats["Drug A"][0] + stats["Drug A"][1]
    ), "Legend says Drug B's interval lies above the others"
    ec50 = {name: half_max_dose(dose, c.mean(axis=1)) for name, c in curves.items()}
    fold = ec50["Control"] / ec50["Drug B"]
    assert 5 < fold < 20, f"Legend says about tenfold; data give {fold:.1f}"

    fig = plt.figure(figsize=(89 * MM, 52 * MM))
    gs = fig.add_gridspec(1, 2, width_ratios=[1, 1.05], wspace=0.32,
                          left=0.085, right=0.985, bottom=0.21, top=0.82)
    ax_a, ax_b = fig.add_subplot(gs[0]), fig.add_subplot(gs[1])

    # a: every observation, with mean and 95% CI beside it
    rng = np.random.default_rng(1)
    for x, (name, values) in enumerate(groups.items()):
        color = HIGHLIGHT if name == "Drug B" else GRAY
        jitter = rng.uniform(-0.12, 0.12, values.size)
        ax_a.scatter(x + jitter, values, s=6, color=color, linewidths=0, zorder=2)
        m, h = stats[name]
        ax_a.plot([x + 0.24, x + 0.24], [m - h, m + h], color="black", lw=0.5)
        ax_a.plot([x + 0.17, x + 0.31], [m, m], color="black", lw=1.0)
    all_a = np.concatenate(list(groups.values()))
    ax_a.set_xticks(range(len(groups)), list(groups))
    ax_a.tick_params(axis="x", length=0)
    ax_a.spines["bottom"].set_visible(False)
    ax_a.set_xlim(-0.45, len(groups) - 0.45)
    range_frame(ax_a, "y", all_a.min(), all_a.max())
    ends = [all_a.min(), 1.0, 1.2, 1.4, all_a.max()]   # the frame's ends report the range
    ax_a.set_yticks(ends, [f"{t:.2f}" if t in (all_a.min(), all_a.max()) else f"{t:.1f}" for t in ends])
    horizontal_ylabel(ax_a, "Response (a.u.)")

    # b: dose-response on a log axis, means with 95% CI bands, labeled directly.
    # The curves meet at both ends, so each label sits where its curve stands apart:
    # Drug B above and left of its rise, the control below and right of its rise.
    label_at = {"Drug B": (3, 1 / 1.7, +0.08, "right"), "Control": (6, 1.5, -0.1, "left")}
    for name, c in curves.items():
        color = HIGHLIGHT if name == "Drug B" else GRAY
        m = c.mean(axis=1)
        h = np.array([mean_ci(row)[1] for row in c])
        ax_b.fill_between(dose, m - h, m + h, color=color, alpha=0.2, linewidth=0)
        ax_b.plot(dose, m, color=color, marker="o", markersize=2.5, markeredgewidth=0)
        i, dx, dy, ha = label_at[name]
        ax_b.text(dose[i] * dx, m[i] + dy, name, ha=ha, va="center", color="black")  # black (rule 7)
    # Each half-maximal dose marked on its curve; the values go in the legend (rule 6).
    halves = {name: (c.mean(axis=1).min() + c.mean(axis=1).max()) / 2 for name, c in curves.items()}
    for name, x0 in ec50.items():
        ax_b.plot(x0, halves[name], "o", ms=3, mfc="white", mec="black", mew=0.5, zorder=4)
    ax_b.set_xscale("log")
    ax_b.xaxis.set_major_locator(FixedLocator([0.01, 0.1, 1, 10, 100]))
    ax_b.set_xticklabels(["0.01", "0.1", "1", "10", "100"])
    ax_b.xaxis.set_minor_locator(NullLocator())
    ax_b.set_xlabel("Dose (µM)")
    all_b = np.concatenate([c.mean(axis=1) for c in curves.values()])
    range_frame(ax_b, "x", dose[0], dose[-1])
    range_frame(ax_b, "y", all_b.min(), all_b.max())
    ends_b = [all_b.min(), 0.2, 0.4, 0.6, 0.8, all_b.max()]   # the frame's ends report the range
    ax_b.set_yticks(ends_b, [f"{v:.2f}" if v in (all_b.min(), all_b.max()) else f"{v:.1f}" for v in ends_b])
    horizontal_ylabel(ax_b, "Response (fraction of maximum)")

    panel_letter(fig, ax_a, "a")
    panel_letter(fig, ax_b, "b")

    outdir.mkdir(parents=True, exist_ok=True)
    fig.savefig(outdir / "figure1.pdf")
    fig.savefig(outdir / "figure1.png", dpi=600)

    means = ", ".join(f"{name} {stats[name][0]:.2f}" for name in groups)
    legend = (
        "Fig. 1 | Drug B raises the response and lowers the half-maximal dose about "
        f"{fold:.0f}-fold. a, Response of each culture (dots); horizontal lines, means; "
        "vertical lines, 95% confidence intervals of the mean; n = 8 independent "
        f"cultures per group. Means: {means} a.u. b, Response against dose (log scale); "
        "points, means of n = 4 cultures per dose; bands, 95% confidence intervals; "
        "open circles, half-maximal doses (EC50), interpolated between doses: control "
        f"{ec50['Control']:.2f} µM, Drug B {ec50['Drug B']:.2f} µM ({fold:.1f}-fold). "
        "Synthetic data generated for illustration."
    )
    assert len(legend.split()) < 300, "Nature: legends under 300 words"
    print(legend)


if __name__ == "__main__":
    main(Path(sys.argv[1]) if len(sys.argv) > 1 else Path.cwd())

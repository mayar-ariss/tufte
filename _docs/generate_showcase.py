"""Generate the README figures, in the journal style this skill teaches.

The setup and helpers are read from rules/matplotlib.md and executed here, so the
figures are drawn by the same code the skill gives an agent. Every figure is
drawn at a journal width in millimeters, carries no title (the README caption
does that job, as a journal caption would), and is saved as a 600 dpi PNG for
the README. Claims in the README captions are checked against the data below.

Usage: python3 _docs/generate_showcase.py
"""

import re
import csv
from pathlib import Path

import matplotlib
matplotlib.use("Agg")

ROOT = Path(__file__).resolve().parent.parent
OUT = Path(__file__).resolve().parent
RULES = (ROOT / "rules" / "matplotlib.md").read_text(encoding="utf-8")


def section_code(heading):
    """The python code block under a '## heading' in rules/matplotlib.md."""
    part = RULES.split(f"## {heading}\n", 1)[1]
    return re.search(r"```python\n(.*?)```", part, re.S).group(1)


exec(section_code("Setup"))    # SCIENCE_RC, MM, GRAY, LIGHT, OKABE_ITO, HIGHLIGHT
exec(section_code("Helpers"))  # range_frame, horizontal_ylabel, direct_label, ...

import matplotlib.pyplot as plt  # noqa: E402  (also imported by the setup block)
import numpy as np  # noqa: E402


def save(fig, name):
    fig.savefig(OUT / name, dpi=600)
    plt.close(fig)
    print("wrote", name)


# ==============================================================================
# 1. Before and after: the same data as a default dynamite plot and as this
#    skill draws it. Drug A has responders and non-responders; the bar hides it.
# ==============================================================================

rng = np.random.default_rng(3)
groups = {
    "Control": rng.normal(1.00, 0.10, 8),
    "Drug A": np.concatenate([rng.normal(0.95, 0.04, 4), rng.normal(1.65, 0.04, 4)]),
    "Drug B": rng.normal(1.30, 0.10, 8),
}

fig = plt.figure(figsize=(183 * MM, 62 * MM))

# a: matplotlib's defaults, as a dynamite plot with SEM bars, legend and grid
with plt.rc_context(matplotlib.rcParamsDefault):
    plt.rcParams.update({"font.size": 7, "pdf.fonttype": 42})
    ax_a = fig.add_axes([0.07, 0.17, 0.36, 0.66])
    means = [v.mean() for v in groups.values()]
    sems = [v.std(ddof=1) / np.sqrt(v.size) for v in groups.values()]
    bars = ax_a.bar(list(groups), means, yerr=sems, capsize=4,
                    color=["C0", "C1", "C2"], label="Mean ± SEM")
    ax_a.set_ylabel("Response (a.u.)")
    ax_a.set_title("Response by group")
    ax_a.grid(True)
    ax_a.legend(loc="upper left")

# b: the same data, drawn by this skill
ax_b = fig.add_axes([0.60, 0.17, 0.37, 0.62])
summary = strip_with_ci(ax_b, groups, colors={"Drug A": HIGHLIGHT})
horizontal_ylabel(ax_b, "Response (a.u.)")

fig.text(0.015, 0.92, "a", fontsize=8, fontweight="bold")
fig.text(0.535, 0.92, "b", fontsize=8, fontweight="bold")

# Caption check: the two Drug A clusters do not overlap, and its mean falls
# between them, where no culture lies
low, high = np.sort(groups["Drug A"])[:4], np.sort(groups["Drug A"])[4:]
assert low.max() < summary["Drug A"][0] < high.min()
save(fig, "before-after.png")


# ==============================================================================
# 2. The journal example: rendered by examples/matplotlib-publication.py
# ==============================================================================

import subprocess  # noqa: E402
import sys  # noqa: E402
import tempfile  # noqa: E402
import shutil  # noqa: E402

with tempfile.TemporaryDirectory() as tmp:
    subprocess.run([sys.executable, str(ROOT / "examples" / "matplotlib-publication.py"), tmp],
                   check=True, capture_output=True)
    shutil.copy(Path(tmp) / "figure1.png", OUT / "tufte-scientific-figure.png")
    print("wrote tufte-scientific-figure.png")
plt.rcParams.update(SCIENCE_RC)


# ==============================================================================
# 3. Small multiples: body mass over 12 weeks on four diets, one scale
# ==============================================================================

rng = np.random.default_rng(11)
weeks = np.arange(0, 13)
gain = {"Standard": 0.10, "High fat": 0.55, "High sugar": 0.35, "Restricted": -0.12}
mice = {d: 25 + np.cumsum(rng.normal(g, 0.25, (8, weeks.size)), axis=1) - g for d, g in gain.items()}
stats_by_diet = {d: (m.mean(axis=0), np.array([mean_ci(col)[1] for col in m.T]))
                 for d, m in mice.items()}
lo = min((m - h).min() for m, h in stats_by_diet.values())
hi = max((m + h).max() for m, h in stats_by_diet.values())

fig, axes = plt.subplots(1, 4, figsize=(183 * MM, 45 * MM), sharey=True)
for ax, (diet, (m, h)) in zip(axes, stats_by_diet.items()):
    start = stats_by_diet["Standard"][0][0]
    ax.axhline(start, color=LIGHT, lw=0.5, ls=(0, (2, 2)), zorder=1)   # week-0 level, from the data
    ax.fill_between(weeks, m - h, m + h, color=GRAY, alpha=0.2, linewidth=0)
    ax.plot(weeks, m, color=HIGHLIGHT if diet == "High fat" else GRAY)
    ax.text(0, 1.06, diet, transform=ax.transAxes, ha="left", va="bottom")
    direct_label(ax, weeks[-1], m[-1], f"{m[-1]:.1f}", dx=3)
    range_frame(ax, x=weeks, y=[lo, hi])
    ax.set_xticks([0, 4, 8, 12])
    ax.set_ylim(lo - 0.5, hi + 0.5)
for ax in axes[1:]:
    ax.spines["left"].set_visible(False)
    ax.tick_params(axis="y", left=False)
axes[0].text(0, 1.22, "Body mass (g)", transform=axes[0].transAxes, ha="left", va="bottom")
fig.text(0.5, 0.02, "Week", ha="center")
fig.subplots_adjust(left=0.05, right=0.975, bottom=0.2, top=0.72, wspace=0.18)
axes[0].text(12, start - 0.3, "Week-0 mean", ha="right", va="top", fontsize=5, color=GRAY)

final = {d: m[-1] for d, (m, _) in stats_by_diet.items()}
assert max(final, key=final.get) == "High fat" and min(final, key=final.get) == "Restricted"
save(fig, "small-multiples.png")


# ==============================================================================
# 4. Tufte's designs for distributions: paired measurements and quartile plots
# ==============================================================================

rng = np.random.default_rng(21)
before = rng.normal(140, 12, 12)
after = before - rng.normal(9, 7, 12)
fell = after < before

dist = {"Site A": rng.normal(10, 2, 40), "Site B": rng.lognormal(2.4, 0.35, 40),
        "Site C": rng.normal(14, 3, 40), "Site D": rng.gamma(6, 2.2, 40)}

fig = plt.figure(figsize=(120 * MM, 55 * MM))
ax_a = fig.add_axes([0.10, 0.15, 0.30, 0.68])
ax_b = fig.add_axes([0.58, 0.15, 0.40, 0.68])

paired_plot(ax_a, before, after, labels=("Before", "After"), highlight=~fell)
horizontal_ylabel(ax_a, "Systolic pressure (mmHg)")

quartile_plot(ax_b, dist)
range_frame(ax_b, y=np.concatenate(list(dist.values())))
horizontal_ylabel(ax_b, "Concentration (µg/L)")

panel_letters(fig, [ax_a, ax_b], dx=-0.08, dy=0.08)
assert fell.sum() == 10 and (~fell).sum() == 2, (fell.sum(), (~fell).sum())  # README: 10 of 12
save(fig, "tufte-designs.png")


# ==============================================================================
# 5. John Snow's cholera map, in journal style (rules/maps.md)
# ==============================================================================

from matplotlib.collections import LineCollection  # noqa: E402

SNOW = OUT / "data" / "snow"


def read_csv(name):
    with open(SNOW / name, newline="") as f:
        return list(csv.DictReader(f))


deaths, pumps, streets = (read_csv(f"Snow.{n}.csv") for n in ("deaths", "pumps", "streets"))
dx = np.array([float(r["x"]) for r in deaths])
dy = np.array([float(r["y"]) for r in deaths])
px = np.array([float(r["x"]) for r in pumps])
py = np.array([float(r["y"]) for r in pumps])
plabels = [r["label"] for r in pumps]
segs = {}
for r in streets:
    segs.setdefault(r["street"], []).append((float(r["x"]), float(r["y"])))

# The README caption's numbers, computed: deaths nearest each pump (straight line)
nearest = np.hypot(dx[:, None] - px, dy[:, None] - py).argmin(axis=1)
counts = np.bincount(nearest, minlength=len(pumps))
broad = plabels.index("Broad St")
assert counts.argmax() == broad
print(f"cholera: {counts[broad]} of {len(deaths)} nearest Broad St; next {np.sort(counts)[-2]}")

fig = plt.figure(figsize=(120 * MM, 116 * MM))
ax = fig.add_axes([0.01, 0.01, 0.98, 0.98])
ax.add_collection(LineCollection(list(segs.values()), colors="#c4c4c4", linewidths=0.4, zorder=1))
ax.scatter(dx, dy, s=1.6, color="black", linewidths=0, zorder=3)
for i, (x0, y0, lab) in enumerate(zip(px, py, plabels)):
    if i == broad:
        continue
    ax.scatter(x0, y0, marker="+", s=18, color=GRAY, linewidths=0.6, zorder=4)
    off = -3 if lab == "Gt Marlborough" else 3
    ax.annotate(lab, xy=(x0, y0), xytext=(off, 2), textcoords="offset points",
                ha="right" if off < 0 else "left", fontsize=5, color=GRAY, zorder=5)
ax.scatter(px[broad], py[broad], marker="+", s=45, color=HIGHLIGHT, linewidths=1.2, zorder=6)
# Label in the nearest clear space (SKILL.md rule 13): the closest offset whose text
# box, about 2.6 by 0.7 map units, covers no death, pump or pump label
bx, by = px[broad], py[broad]
obstacles = [(x0 - 0.2, x0 + 0.25 + 0.14 * len(lab), y0 - 0.25, y0 + 0.45)
             for x0, y0, lab in zip(px, py, plabels)]


def clear(x0, y0):
    if ((dx > x0 - 0.1) & (dx < x0 + 2.7) & (abs(dy - y0) < 0.35)).any():
        return False
    return not any(a < x0 + 2.7 and x0 - 0.1 < b and c < y0 + 0.35 and y0 - 0.35 < d
                   for a, b, c, d in obstacles)


spots = [(np.hypot(ox, oy), ox, oy) for ox in np.arange(-4, 4.1, 0.25)
         for oy in np.arange(-4, 4.1, 0.25) if np.hypot(ox, oy) >= 1 and clear(bx + ox, by + oy)]
_, ox, oy = min(spots)
ax.annotate("Broad St pump", xy=(bx, by), xytext=(bx + ox, by + oy), textcoords="data",
            fontsize=6, color=HIGHLIGHT, va="center", zorder=6,
            arrowprops=dict(arrowstyle="-", color=HIGHLIGHT, lw=0.4, shrinkA=1, shrinkB=3))
xs = [p[0] for s in segs.values() for p in s]
ys = [p[1] for s in segs.values() for p in s]
xn, yn = max(xs) - 0.5, max(ys) - 1.6
ax.annotate("", xy=(xn, yn + 0.9), xytext=(xn, yn),
            arrowprops=dict(arrowstyle="-|>", color=GRAY, lw=0.5))
ax.text(xn, yn + 1.0, "N (approx.)", ha="center", va="bottom", fontsize=5, color=GRAY)
ax.set_xlim(min(xs) - 0.2, max(xs) + 0.2)
ax.set_ylim(min(ys) - 0.2, max(ys) + 0.2)
ax.set_aspect("equal")
ax.axis("off")
save(fig, "tufte-cholera-map.png")


# ==============================================================================
# 6. The palette: Okabe-Ito colors' contrast against the white page
# ==============================================================================


def contrast(a, b="#ffffff"):
    def lum(h):
        c = [int(h[i:i + 2], 16) / 255 for i in (1, 3, 5)]
        c = [x / 12.92 if x <= 0.04045 else ((x + 0.055) / 1.055) ** 2.4 for x in c]
        return 0.2126 * c[0] + 0.7152 * c[1] + 0.0722 * c[2]
    hi_, lo_ = sorted((lum(a), lum(b)), reverse=True)
    return (hi_ + 0.05) / (lo_ + 0.05)


palette = [("Gray (default)", "#666666"), ("Blue", "#0072B2"), ("Vermillion", "#D55E00"),
           ("Bluish green", "#009E73"), ("Reddish purple", "#CC79A7"), ("Light gray", "#8c8c8c"),
           ("Sky blue", "#56B4E9"), ("Orange", "#E69F00"), ("Yellow", "#F0E442")]
palette.sort(key=lambda p: contrast(p[1]))

fig = plt.figure(figsize=(89 * MM, 62 * MM))
ax = fig.add_axes([0.33, 0.17, 0.62, 0.76])
for y, (name, hexc) in enumerate(palette):
    r = contrast(hexc)
    ax.scatter(r, y, s=22, color=hexc, edgecolors="black" if r < 1.6 else "none",
               linewidths=0.3, zorder=3)
    ax.text(r + 0.18, y, f"{r:.1f}", va="center", fontsize=6)
    ax.text(-0.02, y, f"{name}  {hexc}", transform=ax.get_yaxis_transform(),
            ha="right", va="center", fontsize=6)
for t, lab in ((3.0, "marks 3:1"), (4.5, "text 4.5:1")):
    ax.axvline(t, color=LIGHT, lw=0.5, ls=(0, (2, 2)), zorder=1)
    ax.text(t + 0.06, len(palette) - 0.35, lab, ha="left", va="bottom", fontsize=5, color=GRAY)
ax.set_yticks([])
ax.spines["left"].set_visible(False)
ax.set_xlim(1, 6.5)
ax.set_ylim(-0.6, len(palette) + 0.2)
ax.set_xticks([1, 2, 3, 4, 5, 6])
range_frame(ax, x=[1, 6])
ax.set_xlabel("Contrast ratio against white")
save(fig, "tufte-palette-contrast.png")

print("Generated all showcase images.")

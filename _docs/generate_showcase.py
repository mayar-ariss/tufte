"""Generate the README figures, in the journal style this skill teaches.

The setup and helpers are read from rules/matplotlib.md and executed here, so the
figures are drawn by the same code the skill gives an agent. Every figure is
drawn at Nature's widths in millimeters, carries labels only (the README caption,
in Nature's form, carries the title, values and n), and is saved as a 600 dpi PNG
for the README. Numbers in the README captions are checked against the data below.

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

# a: matplotlib's defaults, as a dynamite plot with SEM bars, a key and a grid
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
range_frame(ax_b, y=np.concatenate(list(groups.values())), label_ends=True, fmt="{:.2f}")
horizontal_ylabel(ax_b, "Response (a.u.)")   # labels only; values and n in the caption (rule 6)

fig.text(0.015, 0.92, "a", fontsize=8, fontweight="bold")
fig.text(0.535, 0.92, "b", fontsize=8, fontweight="bold")

# Caption check: the two Drug A clusters do not overlap, and its mean falls
# between them, where no culture lies
low, high = np.sort(groups["Drug A"])[:4], np.sort(groups["Drug A"])[4:]
assert low.max() < summary["Drug A"][0] < high.min()
assert [f"{summary[k][0]:.2f}" for k in groups] == ["0.96", "1.30", "1.33"]   # README caption
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
lo = min(m.min() for m in mice.values())
hi = max(m.max() for m in mice.values())

week0 = np.concatenate([m[:, 0] for m in mice.values()])
band = (week0.min(), week0.max())   # week-0 range of all 32 mice, from the data

fig, axes = plt.subplots(1, 4, figsize=(183 * MM, 45 * MM), sharey=True)
for ax, (diet, (m, h)) in zip(axes, stats_by_diet.items()):
    # Tufte's gray band for the normal range (rule 12: a muted field, not a line)
    ax.fill_between(weeks[[0, -1]], *band, color=FIELD, lw=0, zorder=0)
    # Two readings (SKILL.md rule 11): each mouse as a thin light line, the diet's
    # mean as a heavier line on top
    for mouse in mice[diet]:
        ax.plot(weeks, mouse, color=LIGHT, lw=0.3, zorder=2)
    ax.plot(weeks, m, color=HIGHLIGHT if diet == "High fat" else "black", lw=1.0, zorder=3)
    ax.text(0, 1.06, diet, transform=ax.transAxes, ha="left", va="bottom")
    range_frame(ax, x=weeks, y=[lo, hi])
    ax.set_xticks([0, 4, 8, 12])
    ax.set_ylim(lo - 0.5, hi + 0.5)
    ends = [lo, 25, 27.5, 30, hi]                  # the frame's ends report the range
    ax.set_yticks(ends, [f"{t:.1f}" for t in ends])
for ax in axes[1:]:
    ax.spines["left"].set_visible(False)
    ax.tick_params(axis="y", left=False)
axes[0].text(0, 1.22, "Body mass (g)", transform=axes[0].transAxes, ha="left", va="bottom")
fig.text(0.5, 0.02, "Week", ha="center")
fig.subplots_adjust(left=0.05, right=0.975, bottom=0.2, top=0.72, wspace=0.18)

final = {d: m[-1] for d, (m, _) in stats_by_diet.items()}
assert max(final, key=final.get) == "High fat" and min(final, key=final.get) == "Restricted"
assert [f"{v:.1f}" for v in final.values()] == ["26.3", "31.7", "29.2", "24.0"]   # README caption
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
dist = dict(sorted(dist.items(), key=lambda kv: np.median(kv[1])))   # ordered by value, not name (rule 4)

fig = plt.figure(figsize=(120 * MM, 55 * MM))
ax_a = fig.add_axes([0.10, 0.15, 0.30, 0.68])
ax_b = fig.add_axes([0.58, 0.15, 0.40, 0.68])

paired_plot(ax_a, before, after, labels=("Before", "After"), highlight=~fell)
range_frame(ax_a, y=np.concatenate([before, after]), label_ends=True, fmt="{:.0f}")
horizontal_ylabel(ax_a, "Systolic pressure (mmHg)")
direct_label(ax_a, 1, after[~fell].max(), "Rose", dx=6)       # labels, black (rule 7)
direct_label(ax_a, 1, np.median(after[fell]), "Fell", dx=6)

quartile_plot(ax_b, dist)
range_frame(ax_b, y=np.concatenate(list(dist.values())), label_ends=True, fmt="{:.1f}")
horizontal_ylabel(ax_b, "Concentration (µg/L)")
ax_b.set_xlim(-0.4, len(dist) - 0.45)

panel_letters(fig, [ax_a, ax_b], dx=-0.08, dy=0.08)
assert fell.sum() == 10 and (~fell).sum() == 2, (fell.sum(), (~fell).sum())  # README: 10 of 12
assert [f"{np.median(v):.1f}" for v in dist.values()] == ["9.7", "10.9", "11.9", "13.6"]   # README caption
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
xs = [p[0] for s in segs.values() for p in s]
ys = [p[1] for s in segs.values() for p in s]
nearest = np.hypot(dx[:, None] - px, dy[:, None] - py).argmin(axis=1)
counts = np.bincount(nearest, minlength=len(pumps))
broad = plabels.index("Broad St")
assert counts.argmax() == broad
assert dict(zip(plabels, counts.tolist())) == {   # README caption
    "Broad St": 359, "So Soho": 64, "Crown Chapel": 61, "Briddle St": 27, "Oxford St #2": 24,
    "Warwick": 16, "Oxford St #1": 12, "Gt Marlborough": 6, "Vigo St": 4, "Dean St": 2,
    "Coventry St": 2, "Castle St E": 1, "Oxford Market": 0}, dict(zip(plabels, counts.tolist()))
print(f"cholera: {counts[broad]} of {len(deaths)} nearest Broad St; next {np.sort(counts)[-2]}")

fig = plt.figure(figsize=(120 * MM, 116 * MM))
ax = fig.add_axes([0.01, 0.01, 0.98, 0.98])
ax.add_collection(LineCollection(list(segs.values()), colors="#c4c4c4", linewidths=0.4, zorder=1))
ax.scatter(dx, dy, s=1.6, color="black", linewidths=0, zorder=3)
# Each pump named on the map, in black; the counts go in the caption (rules 6, 7)
plabels_n = plabels
for i, (x0, y0, lab) in enumerate(zip(px, py, plabels_n)):
    if i == broad:
        continue
    ax.scatter(x0, y0, marker="+", s=18, color=GRAY, linewidths=0.6, zorder=4)
    xmax = max(float(r["x"]) for r in streets)
    off = -3 if lab.startswith("Gt Marlborough") or x0 + 0.14 * len(lab) > xmax else 3
    ax.annotate(lab, xy=(x0, y0), xytext=(off, 2), textcoords="offset points",
                ha="right" if off < 0 else "left", fontsize=5, color="black", zorder=5)
ax.scatter(px[broad], py[broad], marker="+", s=45, color=HIGHLIGHT, linewidths=1.2, zorder=6)
# Label in the nearest clear space: the closest offset whose text box, about
# 2.4 by 0.7 map units, stays on the map and covers no death, pump or pump label
bx, by = px[broad], py[broad]
obstacles = [(x0 - 0.2, x0 + 0.25 + 0.14 * len(lab), y0 - 0.25, y0 + 0.45)
             for x0, y0, lab in zip(px, py, plabels_n)]


def clear(x0, y0):
    if x0 + 2.4 > max(xs) or x0 < min(xs):          # stay inside the map
        return False
    if ((dx > x0 - 0.1) & (dx < x0 + 2.4) & (abs(dy - y0) < 0.35)).any():
        return False
    return not any(a < x0 + 2.4 and x0 - 0.1 < b and c < y0 + 0.35 and y0 - 0.35 < d
                   for a, b, c, d in obstacles)


spots = [(np.hypot(ox, oy), ox, oy) for ox in np.arange(-4, 4.1, 0.25)
         for oy in np.arange(-4, 4.1, 0.25) if np.hypot(ox, oy) >= 1 and clear(bx + ox, by + oy)]
_, ox, oy = min(spots)
ax.annotate("Broad St pump", xy=(bx, by), xytext=(bx + ox, by + oy), textcoords="data",
            fontsize=6, color="black", va="center", zorder=6,
            arrowprops=dict(arrowstyle="-", color="black", lw=0.4, shrinkA=1, shrinkB=3))
xn, yn = max(xs) - 0.5, max(ys) - 1.6
ax.annotate("", xy=(xn, yn + 0.9), xytext=(xn, yn),
            arrowprops=dict(arrowstyle="-|>", color=GRAY, lw=0.5))
ax.text(xn, yn + 1.0, "N (approx.)", ha="center", va="bottom", fontsize=5, color="black")
ax.set_xlim(min(xs) - 0.2, max(xs) + 0.2)
ax.set_ylim(min(ys) - 0.2, max(ys) + 0.2)
ax.set_aspect("equal")
ax.axis("off")
save(fig, "tufte-cholera-map.png")


print("Generated all showcase images.")

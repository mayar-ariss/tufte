# ggplot2 and plotnine

Load this file when generating ggplot2 (R) or plotnine (Python) code for a figure in a scientific article. plotnine follows ggplot2's grammar, so the two halves mirror each other.

**Written for ggplot2 3.5+ (with patchwork, dplyr and ggthemes) and plotnine 0.13+.** The rules come from `SKILL.md`, where each names its source; the code below is implementation, not principle. Unlike `rules/matplotlib.md`, the code in this file is not run by the repository's checks (`scripts/check_code.py`); test it in your own environment.

## ggplot2 (R)

### Theme

```r
library(ggplot2)

theme_science <- function(base_size = 7, family = "Helvetica") {
  theme_classic(base_size = base_size, base_family = family) +
    theme(
      text               = element_text(colour = "black"),
      axis.text          = element_text(colour = "black", size = base_size - 1),
      axis.line          = element_line(linewidth = 0.25),     # about 0.5 pt (rule 16)
      axis.ticks         = element_line(linewidth = 0.25),
      axis.ticks.length  = unit(1, "mm"),
      legend.position    = "none",                             # label directly (rule 5)
      plot.title         = element_blank(),                    # the caption carries it (rule 15)
      plot.subtitle      = element_text(hjust = 0, size = base_size),
      plot.title.position = "panel",
      plot.background    = element_rect(fill = "white", colour = NA),
      strip.background   = element_blank(),
      strip.text         = element_text(hjust = 0, size = base_size),
      panel.spacing      = unit(3, "mm")
    )
}

GRAY <- "#666666"
HIGHLIGHT <- "#0072B2"   # Okabe-Ito blue
OKABE_ITO <- c(blue = "#0072B2", vermillion = "#D55E00",
               bluish_green = "#009E73", reddish_purple = "#CC79A7")
```

- A ggplot2 `linewidth` of 1 draws a line about 0.75 mm (about 2.1 pt) wide: 0.25 gives about 0.5 pt (axes) and 0.47 about 1 pt (data lines).
- Text `size` in geoms is in millimeters: use `size = 7 / .pt` for 7 pt.
- **Horizontal y-axis label (rule 2):** set `labs(y = NULL, subtitle = "Response (a.u.)")`; with `plot.title.position = "panel"` the subtitle sits above the axis, left-aligned.
- **Range frame (rule 4):** replace the axis lines with `ggthemes::geom_rangeframe()` and add `theme(axis.line = element_blank())`.

### Individual observations with 95% confidence intervals

```r
library(dplyr)

summ <- df |>
  group_by(group) |>
  summarise(n = n(), mean = mean(response), sd = sd(response)) |>
  mutate(half = qt(0.975, n - 1) * sd / sqrt(n))

p <- ggplot(df, aes(group, response)) +
  geom_jitter(aes(colour = group == "Drug B"), width = 0.12, height = 0,
              size = 0.8, stroke = 0) +
  geom_pointrange(data = summ, aes(y = mean, ymin = mean - half, ymax = mean + half),
                  position = position_nudge(x = 0.25), shape = 95, size = 0.6,
                  linewidth = 0.25, colour = "black") +
  scale_colour_manual(values = c(`FALSE` = GRAY, `TRUE` = HIGHLIGHT)) +
  labs(x = NULL, y = NULL, subtitle = "Response (a.u.)") +
  ggthemes::geom_rangeframe(sides = "l") +
  theme_science() +
  theme(axis.line = element_blank(), axis.ticks.x = element_blank())
```

Caption: what the dots are, *n* and what it counts, and that the bars are 95% confidence intervals of the mean (SKILL.md rules 10, 15).

### Lines with direct labels and a log axis

```r
last <- curves |> group_by(condition) |> slice_max(dose)

p <- ggplot(curves, aes(dose, response, colour = condition)) +
  geom_ribbon(aes(ymin = lo, ymax = hi, fill = condition), alpha = 0.2, colour = NA) +
  geom_line(linewidth = 0.47) +
  geom_point(size = 0.8) +
  geom_text(data = last, aes(label = condition), hjust = 0, nudge_x = 0.1,
            size = 7 / .pt) +
  scale_x_log10(breaks = c(0.01, 0.1, 1, 10, 100),
                labels = c("0.01", "0.1", "1", "10", "100")) +   # values, not logs (rule 12)
  scale_colour_manual(values = c(Control = GRAY, `Drug B` = HIGHLIGHT)) +
  scale_fill_manual(values = c(Control = GRAY, `Drug B` = HIGHLIGHT)) +
  coord_cartesian(clip = "off") +
  labs(x = "Dose (µM)", y = NULL, subtitle = "Response (fraction of maximum)") +
  theme_science()
```

When the curves meet at the end, place each label where its curve stands apart rather than at the last point.

### Small multiples and multi-panel figures

```r
# One quantity, one scale (rule 17): facet_wrap keeps scales fixed by default
p <- ggplot(df, aes(month, value)) +
  geom_line(colour = GRAY, linewidth = 0.47) +
  facet_wrap(~ region, nrow = 1) +
  theme_science()

# Different quantities: combine plots with patchwork and letter the panels
library(patchwork)
fig <- (p_a | p_b) +
  plot_annotation(tag_levels = "a") &          # Nature: a, b, c; Science: tag_levels = "A"
  theme(plot.tag = element_text(face = "bold", size = 8))
```

### Color maps

```r
scale_fill_viridis_c(option = "cividis")         # built into ggplot2
scico::scale_fill_scico(palette = "batlow")      # Crameri's maps (scico package)
scico::scale_fill_scico(palette = "vik", midpoint = 0)  # diverging, centered on zero
```

Never `scale_fill_gradientn(colours = rainbow(…))` for a quantity (SKILL.md rule 8).

### Export

```r
ggsave("figure1.pdf", fig, width = 89, height = 60, units = "mm", device = cairo_pdf)
```

- `cairo_pdf` embeds the fonts. The base `pdf()` device writes Helvetica as a standard PDF font without embedding it, which some journals reject.
- Check with `pdffonts figure1.pdf`: every font `emb yes`.
- If Helvetica is not installed, use `family = "Arial"` in `theme_science()`.

## plotnine (Python)

### Theme

```python
import matplotlib.pyplot as plt
from plotnine import (aes, element_blank, element_text, geom_jitter, geom_line,
                      geom_pointrange, geom_text, ggplot, labs, position_nudge,
                      scale_color_manual, scale_x_log10, theme, theme_classic)

plt.rcParams.update({"pdf.fonttype": 42, "ps.fonttype": 42})   # embedded TrueType fonts

GRAY, HIGHLIGHT = "#666666", "#0072B2"

theme_science = theme_classic(base_size=7, base_family="Helvetica") + theme(
    text=element_text(color="black"),
    axis_text=element_text(color="black", size=6),
    axis_title_y=element_text(rotation=0, va="center"),   # horizontal label (rule 2)
    legend_position="none",                               # label directly (rule 5)
    plot_title=element_blank(),                           # the caption carries it (rule 15)
    strip_background=element_blank(),
)
```

### Individual observations with 95% confidence intervals

```python
from scipy import stats

summ = (df.groupby("group")["response"]
          .agg(["mean", "std", "count"]).reset_index())
summ["half"] = stats.t.ppf(0.975, summ["count"] - 1) * summ["std"] / summ["count"] ** 0.5
summ["lo"], summ["hi"] = summ["mean"] - summ["half"], summ["mean"] + summ["half"]

p = (ggplot(df, aes("group", "response"))
     + geom_jitter(aes(color="group == 'Drug B'"), width=0.12, height=0, size=0.8)
     + geom_pointrange(summ, aes(y="mean", ymin="lo", ymax="hi"),
                       position=position_nudge(x=0.25), size=0.3)
     + scale_color_manual(values={False: GRAY, True: HIGHLIGHT})
     + labs(x="", y="Response (a.u.)")
     + theme_science)
```

### Log axis, facets and export

```python
p = p + scale_x_log10(breaks=[0.01, 0.1, 1, 10, 100],
                      labels=["0.01", "0.1", "1", "10", "100"])   # values, not logs (rule 12)
# facets keep one scale by default (rule 17): + facet_wrap("region", nrow=1)

p.save("figure1.pdf", width=89, height=60, units="mm")   # final width (rule 1)
```

For a multi-panel figure, check whether your plotnine version can compose plots; otherwise draw each panel at its final size and assemble them, or add the panel letters with matplotlib after `fig = p.draw()`.

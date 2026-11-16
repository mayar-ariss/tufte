# Typography and Color

The values in this file (point sizes, hex colors, opacities) are this skill's defaults (convention) unless a line names another source. Journal requirements are quoted in `rules/journals.md`; full references are in `rules/references.md`.

## Typeface: Helvetica

*Source: Journal. Science: "Use a sans-serif font whenever possible (Helvetica is preferred)". Nature: "a sans-serif typeface, preferably Helvetica or Arial, the same font throughout all figures". PLOS: "Arial, Times, or Symbol font only".*

| Use | Font stack |
|---|---|
| Default | `Helvetica, Arial, "TeX Gyre Heros", "Nimbus Sans", "Liberation Sans", sans-serif` |
| PLOS journals | `Arial, "Liberation Sans", sans-serif` |
| Greek and math symbols | the same face where it has them; otherwise Symbol, if the journal lists it |

- Arial has the same character widths as Helvetica, so a figure laid out in one does not shift in the other.
- TeX Gyre Heros, Nimbus Sans and Liberation Sans are free metric clones. They look the same but are not Helvetica or Arial by name; check that the journal accepts them before a final submission.
- On macOS, Helvetica is installed. On Windows, use Arial. On Linux, install a clone or Arial.

**On the departure from Tufte.** The friendly data graphic in VDQI sets type "upper-and-lower case, with serifs" (Tufte, VDQI ch. 9, p. 183). Journals require sans serif type in figures, and Tufte's own practice already uses a sans serif, Gill Sans, for tables and dense numeric displays: his books set some tables in it, and he wrote that he finds Gill Sans "very good for tables" (edwardtufte.com, "Tufte book fonts", 2003). So Helvetica departs from his preferred typeface, not from what he asks of type: clear, precise and modest, in upper-and-lower case, words spelled out, running horizontally.

## Sizes

| Element | Nature (default) | Science | PLOS |
|---|---|---|---|
| Axis labels, annotations, direct labels | 7 pt | 7 pt | 8 pt |
| Tick labels | 6 pt | 6–7 pt | 8 pt |
| Smallest text | 5 pt | 5 pt | 8 pt |
| Panel letters | 8 pt bold, lowercase | 10 pt bold, capitals | 10 pt bold |

*Source: Journal (Nature: text from 5 to 7 pt, panel letters "8 pt bold, upright (not italic) a, b, c"; Science: about 7 pt after reduction, never below 5 pt, part labels "10 pt and bold"; PLOS: 8–12 pt).*

- One size scale across every figure in the paper (Journal, Nature).
- Avoid wide variation in size within a figure (Journal, Science).
- Regular weight for everything except panel letters.

## Case, symbols and units

*Source: Tufte, VDQI ch. 9, p. 183 (case, spelling, orientation); Journal (Science: capitalize only the first letter of a label; units in parentheses; powers of 10).*

- Sentence case: "Response (fraction of maximum)", never "RESPONSE" or "Response (Fraction Of Maximum)".
- Units in parentheses after the quantity: "Concentration (µM)", "Time (h)".
- Very large or small numbers as powers of 10: "Counts (×10³)" or 10⁻³ on the ticks.
- The true minus sign (−, U+2212), the multiplication sign (×) and µ. In matplotlib, `axes.unicode_minus: True` sets the minus sign.
- Italic for variables, upright for units and labels (convention, following SI style).

## Colors

### Page, text and axes

| Role | Hex | Contrast on white |
|---|---|---|
| Page | `#ffffff` | — |
| Text, axes, ticks | `#000000` | 21:1 |
| Default data series and context | `#666666` | 5.7:1 |
| Light context (reference curves, rug marks) | `#8c8c8c` | 3.4:1 (marks only, never text) |
| Gridlines, if any | `#dddddd` | — |

*Source: convention; Journal (Science: "Avoid using colored type").* Text and axes in black: small gray text prints as a halftone screen and loses sharpness.

### Categorical palette: Okabe–Ito

*Source: Literature (Okabe and Ito 2008; Wong 2011).* The Okabe–Ito palette was designed to stay distinct for readers with the common forms of color-vision deficiency. On white, four of its colors clear 3:1 for lines, dots and text:

| Name | Hex | Contrast on white | Use |
|---|---|---|---|
| Blue | `#0072B2` | 5.2:1 | Default highlight; its label may share its color |
| Vermillion | `#D55E00` | 3.9:1 | Second highlight, only when needed; label in black |
| Bluish green | `#009E73` | 3.4:1 | Third, only when needed; label in black |
| Reddish purple | `#CC79A7` | 3.1:1 | Fourth, only when needed; label in black |
| Black | `#000000` | 21:1 | Reference or fifth category |
| Orange | `#E69F00` | 2.3:1 | Not for marks (below 3:1); never over large areas |
| Sky blue | `#56B4E9` | 2.3:1 | Not for marks (below 3:1); never over large areas |
| Yellow | `#F0E442` | 1.3:1 | Avoid |

- **Color last.** Position, direct labels and small multiples separate categories before color does (Tufte, EI ch. 4–5).
- **Gray first.** Draw everything in gray (`#666666`) and give color only to what the reader must find (Tufte, EI ch. 5).
- **One highlight by default**, blue. Add the next colors in table order only when the reader must tell highlighted things apart; at most four in one figure, more categories go to small multiples (convention; Tufte, EI ch. 4).
- **Small areas only.** These colors are for lines, dots, labels and small marks. Tufte's color rules, taken from the cartographer Eduard Imhof, keep strong color to small areas on a muted field and warn against bright colors side by side over large areas (EI ch. 5; see `rules/maps.md`, rule 11). Large areas (fills, wide bars, map regions, backgrounds) take light gray (`#e5e5e5`) or a pale tint of one hue, stepped light to dark when they encode a quantity.
- **The hexes stay as published.** Muting them would undo the color-vision design that Tufte himself asks for (VDQI p. 183); the rules above limit where they go instead.
- **Same condition, same color** in every figure of the paper (Tufte, integrity principle 3).
- **Never red against green** for a contrast that matters (Journal, Science; Wong 2011).

### Color maps for quantities

*Source: Literature (Crameri et al. 2020); Tufte, EI ch. 5 (color as quantity: light to dark).*

| Kind | Use | Maps |
|---|---|---|
| Sequential | magnitude from low to high | viridis, cividis, batlow |
| Diverging | departure from a meaningful midpoint (zero, a control) | vik, roma, or ColorBrewer RdBu centered on the midpoint |
| Cyclic | angle, phase, time of day | romaO, twilight |

- Never rainbow, jet, turbo or any spectral map for a quantity: uneven steps in lightness invent boundaries and hide others, and red–green maps are unreadable for many readers (Crameri et al. 2020).
- Crameri's maps (batlow, vik, roma, romaO) are in the `cmcrameri` package for Python and the `scico` package for R.
- Put the colorbar beside the data, unframed, with units.

### Grayscale and color-vision checks

- The figure must still read when printed in grayscale; if two series merge, separate them by lightness, marker shape or direct labels, not hatching (hatching is chartjunk: Tufte, VDQI ch. 5).
- Check the figure with a color-vision simulator before submission (Literature, Wong 2011).
- RGB color mode, unless the journal asks for CMYK (Journal, Nature).

## Checking contrast

The minimums are an extension (WCAG): 4.5:1 for text and 3:1 for data marks against the page. After changing any color in the tables above, run:

```bash
python3 scripts/check_contrast.py
```

It reads the tables in this file and exits non-zero if any text or data color misses its minimum. Rows marked "never text", "Not for marks" or "Avoid" are reported but not failed.

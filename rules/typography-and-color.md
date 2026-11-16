# Typography and Color

The values in this file (point sizes, hex colors, opacities) are this skill's defaults (convention) unless a line names another source. Journal requirements are quoted in `rules/journals.md`; full references are in `rules/references.md`.

## Typeface: Helvetica

*Source: Journal (Nature: "a sans-serif typeface, preferably Helvetica or Arial, the same font throughout all figures"). Nature governs; other journals in `rules/journals.md` for reference.*

| Use | Font stack |
|---|---|
| Default | `Helvetica, Arial, "TeX Gyre Heros", "Nimbus Sans", "Liberation Sans", sans-serif` |
| Greek letters and glyphs | Symbol (Journal, Nature figure guide) |
| Amino-acid sequences | Courier (or another monospaced face), one-letter code (Journal, Nature) |

- Arial has the same character widths as Helvetica, so a figure laid out in one does not shift in the other.
- TeX Gyre Heros, Nimbus Sans and Liberation Sans are free metric clones. They look the same but are not Helvetica or Arial by name; Nature asks for standard fonts such as Helvetica or Arial: use one of those for the final submission.
- On macOS, Helvetica is installed. On Windows, use Arial. On Linux, install a clone or Arial.

**On the departure from Tufte.** The friendly data graphic in VDQI sets type "upper-and-lower case, with serifs" (Tufte, VDQI ch. 9, p. 183). Nature requires sans serif type in figures, and Tufte's own practice already uses a sans serif, Gill Sans, for tables and dense numeric displays: his books set some tables in it, and he wrote that he finds Gill Sans "very good for tables" (edwardtufte.com, "Tufte book fonts", 2003). So Helvetica departs from his preferred typeface, not from what he asks of type: clear, precise and modest, in upper-and-lower case, words spelled out, running horizontally.

## Sizes

| Element | Size |
|---|---|
| Axis labels, direct labels | 7 pt |
| Tick labels | 6 pt |
| Smallest text | 5 pt |
| Panel letters | 8 pt bold, upright, lowercase (a, b, c) |

*Source: Journal (Nature: text from 5 to 7 pt; panel letters "8 pt bold, upright (not italic) a, b, c").*

- One size scale across every figure in the paper (Journal, Nature).
- Regular weight for everything except panel letters.

## Case, symbols and units

*Source: Tufte, VDQI ch. 9, p. 183 (case, spelling, orientation); Journal (Nature: lettering in lower-case type with an initial capital and no full stop; a single space between number and unit; thousands separated by commas).*

- Lower case with an initial capital, no full stop: "Response (fraction of maximum)", never "RESPONSE" or "Response (Fraction Of Maximum)".
- Units in parentheses after the quantity: "Concentration (µM)", "Time (h)"; a space between number and unit: "5 mm".
- Thousands with commas: 1,000. Very large or small numbers as powers of 10: "Counts (×10³)" or 10⁻³ on the ticks (convention).
- The true minus sign (−, U+2212), the multiplication sign (×) and µ. In matplotlib, `axes.unicode_minus: True` sets the minus sign.
- Italic for variables, upright for units and labels (convention, following SI style).
- No type over shaded or textured areas; no reversed type where it can be avoided (Journal, Nature).

## Colors

### Page, text and axes

| Role | Hex | Contrast on white |
|---|---|---|
| Page | `#ffffff` | — |
| Text, axes, ticks | `#000000` | 21:1 |
| Default data series and context | `#666666` | 5.7:1 |
| Light context (reference curves, rug marks) | `#8c8c8c` | 3.4:1 (marks only, never text) |

*Source: Journal (Nature: "Avoid coloured text"; black or white text, contrast above 4.5:1); convention.* All text black, including direct labels: Nature recolours colored text, and small gray text prints as a halftone screen and loses sharpness.

### Tufte's palette: black and grays, one accent, muted fields

*Source: Tufte, EI ch. 5 (gray first; strong color only in small areas, on muted fields, after Imhof); BE pp. 46–63 and Tufte's notes on sparklines (a gray band for the normal range; a red accent tied to a specific number; red for the first and last values, blue for the low and high; color coding kept modest). Hex values: convention, checked for color-vision deficiency (below).*

Black and the grays in the table above carry the figure. Color is added sparingly:

| Role | Hex | Contrast on white | Use |
|---|---|---|---|
| Accent red | `#CC0000` | 5.9:1 | The one thing the reader must find; its label in black |
| Second accent blue | `#0072B2` | 5.2:1 | Only when a second kind of highlight is needed; its label in black |
| Field gray | `#e5e5e5` | — | Normal ranges, reference bands, large areas |
| Field blue | `#dce9f5` | — | Water on maps; a second large area |

- **Color last.** Position, direct labels and small multiples separate things before color does (Tufte, EI ch. 4–5).
- **Black and grays first.** Data in black, context in gray (`#666666`), individual observations and references in light gray (`#8c8c8c`).
- **One accent, red,** on the finding, as in Tufte's sparklines; its value goes in the caption and its label stays black (`SKILL.md` rules 6–7). **Blue only as a second accent,** for a second kind of highlight; Tufte pairs the two (red for the first and last values, blue for the low and high).
- **Muted fields for large areas.** Field gray for a normal range or a band; field blue, or a pale tint of one hue, for a large region; light-to-dark steps when the area encodes a quantity. Never strong or bright colors over large areas: Tufte's color rules, taken from the cartographer Eduard Imhof, keep strong color to small areas on a muted field (EI ch. 5; see `rules/maps.md`, rule 11).
- **Checked for color-deficient readers** (Tufte, VDQI p. 183). In simulations of protanopia and deuteranopia (Machado et al. 2009), the red and the blue each stay as distinct from the gray `#666666` as Okabe–Ito blue does, and stay clearly distinct from each other. Label them directly anyway.
- **Same condition, same color** in every figure of the paper (Tufte, integrity principle 3).
- **Never red against green**, and no rainbow scales (Journal, Nature figure guide; Wong 2011).

### Fallback for several categories: Okabe–Ito

*Source: Literature (Okabe and Ito 2008; Wong 2011).* Tufte gives no palette for many categories. When three or more must be told apart by color, and position, direct labels or small multiples cannot do it, use the Okabe–Ito palette, designed to stay distinct for the common forms of color-vision deficiency. Use the set in place of the accents (its vermillion is too close to the accent red to mix them), in small areas only, at most four colors in one figure; more categories go to small multiples. Keep the hexes as published: muting them would undo the color-vision design.

| Name | Hex | Contrast on white | Use |
|---|---|---|---|
| Blue | `#0072B2` | 5.2:1 | First category; label in black |
| Vermillion | `#D55E00` | 3.9:1 | Second category; label in black |
| Bluish green | `#009E73` | 3.4:1 | Third category; label in black |
| Reddish purple | `#CC79A7` | 3.1:1 | Fourth category; label in black |
| Black | `#000000` | 21:1 | Reference or fifth category |
| Orange | `#E69F00` | 2.3:1 | Not for marks (below 3:1); never over large areas |
| Sky blue | `#56B4E9` | 2.3:1 | Not for marks (below 3:1); never over large areas |
| Yellow | `#F0E442` | 1.3:1 | Avoid |

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

It reads the tables in this file and exits non-zero if any text or data color misses its minimum. Field rows are skipped (they are areas, not marks); rows marked "never text", "Not for marks" or "Avoid" are reported but not failed.

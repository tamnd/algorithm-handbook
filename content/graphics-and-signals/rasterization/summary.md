## What to remember

- A pixel is a point sample at its center: $(i + \tfrac12, j + \tfrac12)$ in the triangle and polygon entries, integer points in the line and curve entries. A center on an edge needs a tie rule. The exact statements below assume exact arithmetic: integer, fixed-point or rational coordinates.
- [Bresenham's algorithm](/bresenham-line-algorithm/) draws the nearest pixel at each step of the major axis with integer additions, in $\Theta(n)$ time for $n$ pixels. For a major-axis change $m$ its error term stays in $-2m < e \le 2m$. Ties go toward the start, so it is not reversible. The floating-point [DDA](/digital-differential-analyzer/) drifts; in binary64 it matches the exact line off the ties for lines and coordinates up to $2^{16}$, in binary32 only up to about 200.
- [Cohen-Sutherland](/cohen-sutherland-line-clipping/) makes at most four cuts against a closed rectangle. [Liang-Barsky](/liang-barsky-line-clipping/) finds the interval $[t_0, t_1]$ with at most four divisions.
- The [even-odd rule](/even-odd-fill-rule/) fills a point with an odd crossing count; the [nonzero rule](/nonzero-winding-rule/) fills it when the winding number $w \ne 0$, which depends on edge direction. An $s$-bit [stencil buffer](/stencil-buffer/) keeps $w$ modulo $2^s$, so its nonzero fill is exact only when $|w| < 2^s$.
- The [edge function](/edge-function/) $E(p) = Ax + By + C$ is affine, one addition per pixel step, and exact in $2q + 2$ bits for $q$-bit integer coordinates. With exact arithmetic and disjoint interiors, the [top-left rule](/top-left-fill-rule/) covers each center at most once, and each center interior to the union exactly once.
- Listing the $c$ pixels of a triangle takes $\Omega(1 + c)$. Pineda's loop is $\Theta(wh)$ for a $w \times h$ box, edge walking $O(h + c)$, [tiled rasterization](/tiled-rasterization/) $O(wh/t^2 + t(w + h) + c)$. The [scanline fill](/scanline-polygon-fill/) is $O(n \log n + H + I + K + P)$.
- [Perspective-correct interpolation](/perspective-correct-interpolation/) interpolates $a/w$ and $1/w$ on the screen and divides at each pixel; this is an exact identity.
- Bilinear filtering reads 4 texels, trilinear 8. A [mipmap](/mipmap/) holds $(4WH - 1)/3 < \tfrac43 WH$ texels for a square texture, but $(4WH + 2r - 3)/3 < 2WH$ for aspect ratio $r$: a $4 \times 1$ texture needs 7.
- Ordered $k \times k$ supersampling errs by at most $(2k - 1)/k^2$ per straight edge against the box filter; jittered sampling is unbiased with RMS error like $N^{-3/4}$. [Multisampling](/multisample-antialiasing/) equals supersampling on geometry edges. [Morphological](/morphological-antialiasing/) and [temporal](/temporal-antialiasing/) antialiasing have no such bound; their quality is measured.

| Method | Arithmetic | Time | Guarantee |
|---|---|---|---|
| DDA | floating point | $\Theta(n)$ | bound: exact pixels off ties for short lines |
| Bresenham line | integer | $\Theta(n)$ | exact |
| Midpoint circle | integer | $\Theta(r)$ | exact |
| Scanline polygon fill | rational | $O(n \log n + H + I + K + P)$ | exact |
| Pineda | integer subpixel | $\Theta(wh)$ | exact |
| Edge walking | integer subpixel | $O(h + c)$ | exact |
| Tiled | integer subpixel | $O(wh/t^2 + t(w + h) + c)$ | exact |
| Conservative | integer subpixel | $\Theta(wh)$, grown box | exact over- or underestimate |
| Supersampling | per sample | $\Theta(WHk^2 n)$ | bound $(2k - 1)/k^2$ per edge |
| Multisampling | per sample | $\Theta(nWHs)$ worst | equals supersampling on edges |
| Morphological AA | per pixel | $\Theta(WH)$ | measured |
| Temporal AA | per pixel | $\Theta(fWH)$ | measured |

: The main methods. $n$ counts pixels of a line, edges of a polygon, or triangles for the sampling methods; $w \times h$ is a triangle's box, $c$ its covered pixels, $W \times H$ the image, $s$ or $k^2$ the samples per pixel, $f$ the frames.

## Choosing a method

For lines, use Bresenham's algorithm when the pixels must be exact and equal on every machine, and the DDA only for short lines where ties do not matter. Clip with Liang-Barsky, and start the clipped line with the error term of the full line so that its pixels do not move.

For triangles, snap the vertices to fixed point, evaluate edge functions in $2q + 2$ bits, and apply the top-left rule. Pineda's loop is the simplest and most parallel; tiles skip the empty work of large triangles. Use conservative rasterization when no touched pixel may be missed, as in collision tests. For polygons, use the scanline fill with the rule the format names.

For antialiasing, multisampling suits a forward renderer whose problem is geometry edges. Supersampling also removes shading and texture aliasing, at $N$ times the cost. Temporal accumulation suits deferred shading but can blur and ghost; a morphological pass works when no motion vectors exist.

1. ◦ Draw the segment from $(0, 0)$ to $(4, 1)$, with pixel centers at integer points, by the [DDA](/digital-differential-analyzer/) in binary64 and by [Bresenham's algorithm](/bresenham-line-algorithm/). Then draw it with Bresenham's algorithm from $(4, 1)$ to $(0, 0)$. Which pixels differ, and why does no rounding error enter the DDA here?

2. ◦ Clip the segment from $(-4, 2)$ to $(6, 12)$ against the window $[0, 10]^2$. Give the two outcodes of [Cohen-Sutherland line clipping](/cohen-sutherland-line-clipping/) (LEFT = 1, RIGHT = 2, BOTTOM = 4, TOP = 8) and the points it cuts, in order. Then give the four ratios $b/a$ of [Liang-Barsky](/liang-barsky-line-clipping/), say which of them change $[t_0, t_1]$, and give the output segment.

3. ◦ Two squares, $[0, 4]^2$ and $[2, 6]^2$, form one path, and the pixel centers are at $(i + \tfrac12, j + \tfrac12)$. How many pixels does the [even-odd rule](/even-odd-fill-rule/) fill? How many does the [nonzero winding rule](/nonzero-winding-rule/) fill when both squares run counterclockwise, and when the second runs clockwise?

4. ◦ A [viewport transform](/viewport-transform/) maps normalized device coordinates in $[-1, 1]^2$ onto a $640 \times 480$ viewport at the origin. Where does the point $(x_d, y_d) = (0.5, -0.25)$ land with the OpenGL map, where $y$ grows upward, and with the Direct3D map, where $y$ grows downward? Is either point a pixel center?

5. ◦ A pixel $[0, 1]^2$ is red where $y < 0.2 + 0.7x$ and white elsewhere. Estimate the red fraction with [supersampling](/supersampling-antialiasing/) on the ordered $4 \times 4$ grid, samples at $((a + \tfrac12)/4, (b + \tfrac12)/4)$. Compare the estimate with the exact area and with the bound $(2k - 1)/k^2$ for $k = 4$.

6. ◦ A $4 \times 4$ one-channel texture has $T_{s,t} = s^2 + t$, with texel centers at half-integers, so that $(u, v)$ maps to $x = 4u - \tfrac12$, $y = 4v - \tfrac12$. Compute the [bilinear filtering](/bilinear-filtering/) result at $(u, v) = (0.5, 0.3)$, and compare it with $x^2 + y$ at the same point.

7. ◦ Build the [mipmap](/mipmap/) of a $512 \times 256$ texture, halving each side until it is 1 and stopping at $1 \times 1$. How many levels and how many texels does it have? Is that more or less than $\tfrac43 WH$?

8. ◦ In premultiplied RGBA, let $A = (0.2, 0.1, 0, 0.4)$ and $B = (0, 0, 0.5, 0.5)$. Compute $A$ over $B$ and $B$ over $A$ with the [Porter-Duff](/porter-duff-compositing/) operator, and the straight (non-premultiplied) color of $A$ over $B$.

9. ◦ An edge runs on the screen from a vertex with $u = 0$ and $w = 1$ to a vertex with $u = 1$ and $w = 3$. What value of $u$ does [perspective-correct interpolation](/perspective-correct-interpolation/) give at the screen midpoint of the edge, and what does screen-space linear interpolation give?

10. • With $y$ down and pixel centers at $(i + \tfrac12, j + \tfrac12)$, rasterize the triangle with vertices $(2.5, 0.5)$, $(6.5, 4.5)$ and $(0.5, 4.5)$ by the [top-left fill rule](/top-left-fill-rule/). Classify each edge as top, left or neither, say which of the centers on the edges are drawn, and list all covered pixels.

11. • The triangles $(0.5, 2.5), (4.5, 2.5), (2.5, 0.5)$ and $(0.5, 2.5), (4.5, 2.5), (2.5, 4.5)$ share a horizontal edge ($y$ down, centers at half-integers). A rasterizer includes an edge with $E = 0$ only when $A > 0$, and forgets the case $A = 0$, $B > 0$. Which pixels does it lose? Which triangle owns them under the full top-left rule?

12. • An edge joins two vertices with integer coordinates $a$ and $b$, and the pixel centers are at $(i + \tfrac12, j + \tfrac12)$. Show that if $(b_x - a_x) + (b_y - a_y)$ is odd, no pixel center lies on the line through the edge. Give an edge with an even sum whose line passes through a center.

13. • Run the [midpoint circle algorithm](/midpoint-circle-algorithm/) for radius $r = 6$. List the pixels of the octant, the number of plots of all eight copies, and the number of different pixels of the circle.

14. • Show that, for a first-octant segment from $(0, 0)$ to $(d_x, d_y)$ with $g = \gcd(d_x, d_y)$, the pixels of Bresenham's algorithm repeat with period $(d_x/g, d_y/g)$: the pixel of column $x + d_x/g$ is the pixel of column $x$ with $y$ increased by $d_y/g$. Use this and the pixels of the segment from $(0, 0)$ to $(4, 1)$ to list the pixels from $(0, 0)$ to $(8, 2)$.

15. • Run [Wu's line algorithm](/wu-line-algorithm/) with an 8-bit accumulator ($w = 8$) from $(0, 0)$ to $(7, 2)$, with the slope rounded to $d = \lfloor 2 \cdot 256/7 + \tfrac12 \rfloor$. Give $d$, the pair of rows and the two weights of each inner column, and the largest difference from the exact tent weights.

16. • Two vertices of a triangle have unit normals at $+30°$ and $-30°$ from the half vector $h$, in one plane. The specular term is $\max(0, n \cdot h)^{20}$. What specular intensity does [Gouraud shading](/gouraud-shading/) give halfway along the edge between them, and what does [Phong shading](/phong-shading/) give?

17. • The [edge function](/edge-function/) of a triangle with $q$-bit integer coordinates needs $2q + 2$ bits. With $s = 8$ subpixel bits and pixel coordinates in $[-2^{k-1}, 2^{k-1})$, the coordinates have $q = k + s$ bits. What pixel range is safe with 64-bit integers? What range is safe with 32-bit integers and $s = 4$?

18. • A pixel center lies in one front-facing and one back-facing triangle of a fan, so its winding number is 0. The [stencil buffer](/stencil-buffer/) starts at 0, and the back-facing triangle is drawn first. What value is left when the counts use the saturating INCR and DECR, and what value with INCR_WRAP and DECR_WRAP on 8 bits? Which one gives the right nonzero fill, and does the other depend on the order?

19. • A $1920 \times 1080$ frame is rendered with 4 samples per pixel, 4 bytes of color and 4 bytes of depth and stencil per sample. Opaque triangles cover the screen without overlap, and $P$ pixels have samples owned by two triangles, the rest by one. How many bytes do the sample buffers take with supersampling and with [multisampling](/multisample-antialiasing/)? How many shader calls does each make?

20. • Take the triangle $(0.1, 0), (0.3, 0), (0.2, h)$ for an integer $h \ge 1$, with centers at half-integers. Show that it covers no pixel center. How many rows does edge walking visit, and how many pixels does Pineda's box hold if it runs over the columns $\lceil x_{\min} - \tfrac12 \rceil$ to $\lfloor x_{\max} - \tfrac12 \rfloor$? What does this say about the $O(h + c)$ and $\Theta(wh)$ bounds?

21. • In [sort-middle rendering](/sort-middle-rendering/), triangles have $20 \times 10$ bounding boxes at random offsets. Compute the overlap factor for $64 \times 64$ and for $256 \times 256$ regions, and the smallest integer side $T$ of square regions that gives an overlap factor of at most $1.1$.

22. ★ For premultiplied colors $A$ and $B$ (with each channel at most the alpha), find exactly when $A$ over $B$ equals $B$ over $A$.

23. ★ For a $2^a \times 2^b$ texture, find all sizes whose mipmap holds more than $\tfrac32 WH$ texels, and prove that the list is complete.

24. ★ Let $y = sx + c$ with $0 < s < 1$ and real $c$, and let each integer column $x$ get the pixel nearest to the line, with ties broken by a fixed rule. Prove that every run of pixels in one row, other than the first and the last, has $\lfloor 1/s \rfloor$ or $\lceil 1/s \rceil$ pixels. Conclude that no segment gives inner runs of lengths 2 and 4.

25. ★ The bottom-right rule includes an edge with $E = 0$ when $A < 0$, or $A = 0$ and $B < 0$. Prove that it also covers each pixel center at most once for triangles with disjoint interiors, and each center in the interior of the union exactly once, assuming the theorem for the top-left rule.

26. ★ A closed polygon has $n$ edges, and a point $p$ lies on no line through an edge. Prove that $|w(p)| < n/2$. Conclude that an 8-bit stencil with wrapping counts fills every such polygon with at most 512 edges correctly under the nonzero rule, and give a polygon with 513 edges for which it fails.

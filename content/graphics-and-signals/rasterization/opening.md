A graphics processor receives a triangle as three vertices with floating-point coordinates and must decide which pixels it covers, and with what color. It does this billions of times a second. A font renderer does the same for the outline of each glyph, a plotter for each line of a drawing, and a game for every frame. Rasterization is the step that turns shapes into pixels. Its algorithms are short, but they must agree to the last pixel: two triangles that share an edge must not both write a pixel on it, or a transparent mesh shows a seam where the color is blended twice, and they must not both skip it, or the background shows through a crack.

The entries make the model explicit, and this chapter keeps to it. A [pixel](/pixel/) is a point sample at its center. The triangle and polygon entries put the center of pixel $(i, j)$ at $(i + \tfrac12, j + \tfrac12)$, as OpenGL and Direct3D 10 do, and most of them count rows down from the top, as Direct3D does; OpenGL window coordinates count up. The line and curve entries put the centers at integer points and say that a shift by one half changes nothing. A center that lies exactly on a shared edge goes to one triangle by the [top-left fill rule](/top-left-fill-rule/). The exact guarantees hold in exact arithmetic, which in practice means integer or fixed-point coordinates after the vertices are snapped to a subpixel grid; with unsnapped floating point, a center on a shared edge can go to both triangles or to neither. Costs are counted per pixel written, per edge, or per covered sample, and the pages say which.

## What the chapter covers

1. **Pixels and the pipeline.** The pixel as a sample, the order of the stages in the [graphics pipeline](/graphics-pipeline/), the [viewport transform](/viewport-transform/) and the [frame buffer](/frame-buffer/).
2. **Clipping.** [Cohen-Sutherland](/cohen-sutherland-line-clipping/) and [Liang-Barsky](/liang-barsky-line-clipping/) clip a segment to a rectangle; [polygon window clipping](/polygon-window-clipping/) does the same for a polygon.
3. **Lines and curves.** [Line rasterization](/line-rasterization/) as a problem, the floating-point [DDA](/digital-differential-analyzer/), the exact [Bresenham line algorithm](/bresenham-line-algorithm/), and the midpoint algorithms for [circles](/midpoint-circle-algorithm/) and [ellipses](/midpoint-ellipse-algorithm/).
4. **Filling polygons and regions.** The [even-odd](/even-odd-fill-rule/) and [nonzero winding](/nonzero-winding-rule/) rules, [scanline polygon fill](/scanline-polygon-fill/) with its [active edge table](/active-edge-table/), and [region filling](/region-filling/) from a seed.
5. **Triangles.** The [edge function](/edge-function/), [triangle rasterization](/triangle-rasterization/), the top-left rule, [Pineda rasterization](/pineda-rasterization/) and [perspective-correct interpolation](/perspective-correct-interpolation/).
6. **Tiles, parallel renderers and conservative coverage.** [Tiled rasterization](/tiled-rasterization/), [sort-middle rendering](/sort-middle-rendering/) and [conservative rasterization](/conservative-rasterization/).
7. **Shading.** [Gouraud shading](/gouraud-shading/) interpolates intensities and [Phong shading](/phong-shading/) interpolates normals.
8. **Textures.** [Texture mapping](/texture-mapping/), [bilinear filtering](/bilinear-filtering/), the [mipmap](/mipmap/) and [anisotropic filtering](/anisotropic-filtering/).
9. **Blending, compositing and the stencil buffer.** [Alpha blending](/alpha-blending/), the [Porter-Duff operators](/porter-duff-compositing/) and the [stencil buffer](/stencil-buffer/).
10. **Antialiasing.** The [antialiasing](/antialiasing/) problem, [supersampling](/supersampling-antialiasing/), [multisampling](/multisample-antialiasing/), the post-process and temporal methods, and [Wu's line algorithm](/wu-line-algorithm/).

The kinds of guarantee differ from group to group, and the pages keep them apart. Bresenham's algorithm, the midpoint algorithms, the fill rules, the scanline fill and Pineda's loop are exact: they produce the pixels that the definition names, with no error. The DDA, the fixed-point form of Wu's algorithm and supersampling come with bounds on an error. [Morphological antialiasing](/morphological-antialiasing/) and [temporal antialiasing](/temporal-antialiasing/) are heuristics whose quality is measured on images or judged by eye.

## A first reading

Read these in order:

1. [Pixel](/pixel/)
2. [Graphics pipeline](/graphics-pipeline/)
3. [Line clipping](/line-clipping/)
4. [Line rasterization](/line-rasterization/)
5. [Bresenham line algorithm](/bresenham-line-algorithm/)
6. [Even-odd fill rule](/even-odd-fill-rule/) and [nonzero winding rule](/nonzero-winding-rule/)
7. [Scanline polygon fill](/scanline-polygon-fill/)
8. [Edge function](/edge-function/)
9. [Triangle rasterization](/triangle-rasterization/)
10. [Top-left fill rule](/top-left-fill-rule/)
11. [Perspective-correct interpolation](/perspective-correct-interpolation/)
12. [Texture mapping](/texture-mapping/) and [mipmap](/mipmap/)
13. [Antialiasing](/antialiasing/) and [supersampling](/supersampling-antialiasing/)

Skip at first the ellipse entries, the [active edge table](/active-edge-table/) in detail, tiled and conservative rasterization, sort-middle rendering, the [reconstruction filter](/reconstruction-filter/), and the morphological and temporal methods. They refine the core and are easier after it.

## Before you start

The chapter uses plane geometry from the geometry volume: the [orientation test](/orientation-test/), the [oriented triangle area](/oriented-triangle-area/), the [cross product](/cross-product/), [polygons](/polygon/) and [point in polygon](/point-in-polygon/), and the [Sutherland-Hodgman](/sutherland-hodgman/) clipper. The numerical volume supplies the [floating-point model](/floating-point-model/), [IEEE 754](/ieee-754/) and [bilinear interpolation](/bilinear-interpolation/). [Graph reachability](/graph-reachability/) underlies region filling, and [loop invariants](/loop-invariant/) carry the proofs of the incremental algorithms. Multisampling uses the [z-buffer](/z-buffer/) of the chapter on visibility. The signal-processing ideas behind antialiasing, sampling and aliasing, are planned for the last chapter of this volume; the antialiasing entries state what they need.

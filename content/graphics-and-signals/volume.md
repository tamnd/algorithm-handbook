A screen shows a few million pixels, and a game redraws all of them sixty times a second. Each frame starts as a list of triangles in three dimensions and ends as a grid of colors. On the way, each triangle is clipped to the view, projected, and turned into the pixels it covers. The pixels hidden behind nearer surfaces are dropped, the rest are shaded and textured, and their edges are smoothed. A film renderer makes the same picture another way, by following rays of light through the scene. An image editor then blurs, sharpens and segments the picture, and an audio player reconstructs a sound wave from 44100 samples a second. All of these are algorithms on samples of a continuous world.

This volume is about those algorithms. It starts with rasterization and goes on to curves and surfaces, visibility, ray tracing, image processing and signal processing.

This edition contains the entries of two chapters, *Rasterization* and *Visibility*. The entries of the other four chapters are being written; in this edition each of them has an opening page only, saying what the chapter will cover and which entries elsewhere in the set to read meanwhile.

## Why graphics and signals get a volume of their own

A graphics or signal algorithm turns a continuous object into samples, or samples back into a continuous object, and it is judged at the samples. A few ideas come back in every chapter:

- **A sample is a point.** A [pixel](/pixel/) is a point sample at its center, not a little square, and an audio sample is the value of a wave at one instant. The rules that decide which samples a shape covers, such as the [top-left fill rule](/top-left-fill-rule/), are stated for points, and so are the bounds on error.
- **Aliasing is the price of sampling.** Detail finer than the sample spacing comes back as false patterns: jagged edges, crawling textures, wrong tones. [Antialiasing](/antialiasing/), the [mipmap](/mipmap/) and the [reconstruction filter](/reconstruction-filter/) all fight it, and the sampling theorem of the last chapter says when it can be avoided completely.
- **Exact answers need exact arithmetic.** With integer or fixed-point coordinates, [Bresenham's algorithm](/bresenham-line-algorithm/), the [edge function](/edge-function/) and the fill rules give exactly the pixels their definitions name, and two triangles that share an edge never both draw a pixel on it. With unsnapped floating point these guarantees fail, and the entries show how.
- **The cost is per pixel or per sample.** Bounds count pixels written, covered samples, edges or rays. The best bounds are output-sensitive, like the $\Omega(1 + c)$ for a triangle that covers $c$ pixels, and the [z-buffer](/z-buffer/) trades object-space exactness for constant work per sample.
- **Not every guarantee is a theorem.** Some results are exact, some are bounds on an approximation, and some, such as [temporal antialiasing](/temporal-antialiasing/), are heuristics whose quality is measured on images or judged by eye. The entries say which kind each result is.

## How this volume relates to the others

- **Volume 1, foundations**, has the [word RAM](/word-ram/) and the [real RAM](/real-ram/), the two cost models of the entries, and the [loop invariants](/loop-invariant/) that carry the proofs of incremental algorithms.
- **Volume 3, data structures**, gives the [row-major order](/row-major-order/) of the frame buffer and the spatial trees behind visibility and ray tracing: the [quadtree](/quadtree/), the [octree](/octree/), the [kd-tree](/kd-tree/) and the [BSP tree](/bsp-tree/).
- **Volume 7, graphs**, has [graph reachability](/graph-reachability/) and [flood fill](/flood-fill/), the core of region filling, and [connected components](/connected-components/), which labels the regions of an image.
- **Volume 11, algebra**, has the [discrete Fourier transform](/discrete-fourier-transform/), the [fast Fourier transform](/fast-fourier-transform/) and [convolution](/convolution/), the tools of filtering.
- **Volume 12, numerical**, is the source for the [floating-point model](/floating-point-model/), [IEEE 754](/ieee-754/), [bilinear interpolation](/bilinear-interpolation/), [polynomial interpolation](/polynomial-interpolation/) and [Monte Carlo integration](/monte-carlo-integration/).
- **Volume 13, geometry**, is the source for the [orientation test](/orientation-test/), [polygons](/polygon/), [point in polygon](/point-in-polygon/), [polygon clipping](/polygon-clipping/) with [Sutherland-Hodgman](/sutherland-hodgman/), [polygon triangulation](/polygon-triangulation/) and the [art gallery problem](/art-gallery-problem/). This volume uses them and does not repeat them.
- **Volume 17, randomized algorithms**, has [stratified sampling](/stratified-sampling/), [importance sampling](/importance-sampling/) and [Metropolis-Hastings](/metropolis-hastings/), on which jittered antialiasing and path tracing rest.
- **Volume 24, compression**, has the [discrete cosine transform](/discrete-cosine-transform/) of image and audio coding.

## The chapters

**Chapter 28.1, Rasterization**, turns lines, polygons and triangles into pixels. It starts with the pixel, the [graphics pipeline](/graphics-pipeline/) and the [viewport transform](/viewport-transform/), clips segments with [Cohen-Sutherland](/cohen-sutherland-line-clipping/) and [Liang-Barsky](/liang-barsky-line-clipping/), and draws lines and circles with Bresenham's algorithm and the [midpoint circle algorithm](/midpoint-circle-algorithm/). It fills polygons by the [even-odd](/even-odd-fill-rule/) and [nonzero winding](/nonzero-winding-rule/) rules with the [scanline fill](/scanline-polygon-fill/), and triangles by edge functions and [Pineda's loop](/pineda-rasterization/). It ends with [perspective-correct interpolation](/perspective-correct-interpolation/), shading, textures, compositing, the [stencil buffer](/stencil-buffer/) and antialiasing from [supersampling](/supersampling-antialiasing/) to [multisampling](/multisample-antialiasing/).

**Chapter 28.2, Curves and surfaces**, is planned. It will cover Bézier curves and the de Casteljau algorithm, Bernstein polynomials, B-splines with the Cox-de Boor recurrence and knot insertion, NURBS, and the Hermite, Catmull-Rom and natural cubic splines. It will go on to subdivision surfaces (Chaikin, Catmull-Clark, Doo-Sabin, Loop), mesh simplification by quadric error metrics, line simplification by Ramer-Douglas-Peucker, marching squares and marching cubes, surface reconstruction, and the curvature and arc length of curves.

**Chapter 28.3, Visibility**, decides what the viewer sees. It defines [hidden surface removal](/hidden-surface-removal/) and solves it in image space with the z-buffer and the [hierarchical z-buffer](/hierarchical-z-buffer/), and in object space with the [painter's algorithm](/painters-algorithm/), [BSP tree visibility](/bsp-tree-visibility/), [Warnock's algorithm](/warnock-algorithm/) and [Watkins' scanline algorithm](/watkins-scanline-algorithm/). It covers culling ([back faces](/back-face-culling/), the [view frustum](/frustum-culling/), [occlusion](/occlusion-culling/) and [portals](/portal-culling/)), shadows by [shadow mapping](/shadow-mapping/) and [shadow volumes](/shadow-volume-algorithm/), and the geometry of seeing: the [visibility polygon](/visibility-polygon/), [Chvátal's art gallery theorem](/chvatal-art-gallery-theorem/) that $\lfloor n/3 \rfloor$ guards suffice, and the [NP-hardness](/minimum-guard-np-hardness/) of the fewest guards.

**Chapter 28.4, Ray tracing**, is planned. It will cover cameras and primary rays, ray intersection with spheres, planes and triangles (Möller-Trumbore and the watertight test), the slab test for boxes, bounding volume hierarchies with the surface area heuristic, and grid traversal by Amanatides-Woo. On the side of light it will cover Whitted and distributed ray tracing, the rendering equation, path tracing with Russian roulette, next event estimation and multiple importance sampling, bidirectional and Metropolis light transport, photon mapping, radiosity, reflectance models from Lambert to microfacets, participating media and sphere tracing.

**Chapter 28.5, Image processing**, is planned. It will cover color spaces and gamma, histograms and equalization, thresholding by Otsu's method, linear and nonlinear filters (Gaussian, bilateral, non-local means), the integral image, edge detection by Sobel and Canny, corner detection by Harris, the Hough transform and SIFT, morphology, distance transforms, segmentation by watershed, mean shift and graph methods, dithering by Floyd-Steinberg, image pyramids, optical flow by Lucas-Kanade, deblurring, inpainting, seam carving, and the PSNR and SSIM measures of quality.

**Chapter 28.6, Signal processing**, is planned. It will cover the sampling theorem and aliasing, linear time-invariant systems and the Z-transform, FIR and IIR filters and their design, window functions and spectral leakage, spectral estimation from the periodogram to MUSIC, the short-time Fourier transform and wavelets, correlation and the matched filter, the Wiener, Kalman, LMS and RLS filters, linear prediction, resampling, and compressed sensing.

## How to read this volume

For a first course, read these entries in order:

1. [Pixel](/pixel/)
2. [Graphics pipeline](/graphics-pipeline/)
3. [Line clipping](/line-clipping/)
4. [Bresenham's line algorithm](/bresenham-line-algorithm/)
5. [Even-odd fill rule](/even-odd-fill-rule/)
6. [Scanline polygon fill](/scanline-polygon-fill/)
7. [Edge function](/edge-function/)
8. [Triangle rasterization](/triangle-rasterization/)
9. [Top-left fill rule](/top-left-fill-rule/)
10. [Perspective-correct interpolation](/perspective-correct-interpolation/)
11. [Hidden surface removal](/hidden-surface-removal/)
12. [Z-buffer](/z-buffer/)
13. [Back-face culling](/back-face-culling/)
14. [Painter's algorithm](/painters-algorithm/) and [BSP tree visibility](/bsp-tree-visibility/)
15. [Shadow mapping](/shadow-mapping/)
16. [Texture mapping](/texture-mapping/) and [mipmap](/mipmap/)
17. [Supersampling antialiasing](/supersampling-antialiasing/)
18. [Multisample antialiasing](/multisample-antialiasing/)

This covers how a triangle becomes pixels, how the visible ones are chosen, and how they are textured and smoothed. The clipping and line algorithms can come later for a reader who only needs triangles, and the geometric visibility entries of Chapter 28.3 suit a reader who knows the geometry volume.

## What you need first

The entries assume the plane geometry of Volume 13: orientation tests, polygons and clipping. They use floating point and interpolation from Volume 12, and the cost models of Volume 1. Some linear algebra is needed throughout: vectors, dot and cross products, and $4 \times 4$ matrices acting on homogeneous coordinates. The antialiasing and texture entries use the language of sampling and filters, which the planned last chapter will treat in full; until then, convolution and the Fourier transform of Volume 11 are enough.

## The exercises

In this edition only Chapters 28.1 and 28.3 have exercises; the other chapters will have them when their entries are written. They come in three bands. Exercises marked ◦ check that you read the entries closely; you should be able to do them in a few minutes. Exercises marked • ask you to use an idea in a new place; each takes some thought, and some need a short program. Exercises marked ★ are harder; some are results from research papers. Hints for many exercises are in the appendix *Hints to the exercises* at the end of the volume.

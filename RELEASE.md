The Handbook of Algorithms, edition 0.27.0: the written areas of [algorithm.tamnd.com](https://algorithm.tamnd.com)
as books, one volume per area, in PDF (7 × 10 in, with bookmarks and links), EPUB 3 and LaTeX source. Built from
[`tamnd/algorithm` v0.27.0](https://github.com/tamnd/algorithm/releases/tag/v0.27.0)
(`e29daf043be6ff6e6c7828656128b6fd5b6f033f`); the edition number follows the release of the site.

| | Volume | Entries | Pages |
|---|---|---:|---:|
| 0 | Guide and Index | the whole set | 1,459 |
| 1 | Foundations | 204 | 1,000 |
| 2 | Techniques | 208 | 1,123 |
| 3 | Data structures | 427 | 3,140 |
| 4 | Sorting | 156 | 910 |
| 5 | Searching | 115 | 646 |
| 6 | Sequences | 120 | 594 |
| 7 | Graphs | 685 | 3,691 |
| 8 | Strings | 216 | 1,256 |
| 9 | Automata and parsing | 270 | 1,604 |
| 10 | Number theory | 238 | 1,438 |
| 11 | Algebra | 328 | 2,122 |
| 12 | Numerical | 465 | 3,024 |
| 13 | Geometry | 280 | 1,794 |
| 14 | Combinatorics | 174 | 877 |
| 15 | Optimization | 301 | 1,764 |
| 16 | Logic and constraints | 325 | 2,106 |
| 17 | Randomized | 141 | 840 |
| 18 | Approximation | 213 | 1,309 |
| 19 | Online and streaming | 195 | 1,135 |
| 20 | Parallel | 128 | 897 |
| 21 | Distributed | 281 | 2,060 |
| 22 | Concurrency | 155 | 2,240 |
| 23 | Cryptography | 390 | 3,136 |
| 24 | Compression and coding | 220 | 1,741 |
| 25 | Machine learning | 419 | 2,982 |
| 26 | Systems | 442 | 3,209 |
| 27 | Biology | 254 | 1,611 |
| 28 | Graphics and signals | 401 | 2,745 |
| | **All** | **7,751** | **52,453** |

- **Volume 28, Graphics and signals, is now complete**, in six chapters and 401 entries. To Rasterization (28.1)
  and Visibility (28.3) this edition adds *Curves and surfaces* (72 entries: Bernstein polynomials, Bezier curves
  and de Casteljau's algorithm, Hermite, Catmull-Rom and natural cubic splines, B-splines by the Cox-de Boor
  recursion and de Boor's algorithm, knot insertion, NURBS, tensor-product and triangular patches, subdivision
  surfaces by Chaikin, Catmull-Clark, Doo-Sabin, Loop and the butterfly scheme, implicit surfaces and marching
  cubes, surface reconstruction, mesh and curve simplification), *Ray tracing* (71 entries: ray-object
  intersection by the slab method and the Möller-Trumbore and watertight tests, bounding volume hierarchies, the
  surface area heuristic and kd-trees, the rendering equation, BRDFs and microfacets, Whitted and path tracing,
  Russian roulette, next-event estimation and multiple importance sampling, bidirectional and Metropolis light
  transport, photon mapping, radiosity, participating media, ReSTIR and sphere tracing), *Image processing* (97
  entries: histograms and contrast, linear, separable, bilateral and guided filters, edges by Sobel, Canny and the
  Laplacian of Gaussian, the Hough transform, thresholding by Otsu's method, morphology, connected components and
  distance transforms, segmentation by watershed, mean shift, graph cuts and superpixels, pyramids, corners, SIFT
  and Viola-Jones, optical flow, deconvolution, denoising and inpainting, seam carving, dithering and the
  measures of quality) and *Signal processing* (79 entries: sampling and aliasing, linear time-invariant systems,
  convolution and the z-transform, FIR and IIR filters and their design by windows, Parks-McClellan and the
  bilinear transform, overlap-add and overlap-save, spectral estimation by the periodogram, Welch's method and
  parametric models, MUSIC and ESPRIT, the short-time Fourier and wavelet transforms, Wiener, LMS, RLS and
  Kalman filtering, and compressed sensing). The volume introduction is rewritten for the whole volume, and the
  opening of each new chapter replaces the short one of 0.26.0.
- **Volume 0, Guide and Index**, covers the whole set of 7,751 entries and has a new learning path,
  *Graphics and signals*.
- **Volumes 1 to 27** have the same entries under the same numbers as in 0.26.0; their cross-references to the
  new entries of Volume 28 (de Casteljau's algorithm, the bounding volume hierarchy, the Canny edge detector, the
  Kalman filter and others) now give entry numbers.
- Volumes 29 to 31 are forthcoming; Volume 0 lists their chapters.

**Files.** For each volume `NN-area`: `handbook-of-algorithms-0.27.0-NN-area.pdf`, `.epub`, and `-tex.tar.gz`
(`main.tex`, `body.tex`, `handbook.sty` and the figures; compile `main.tex` with XeLaTeX or tectonic).
`…-all-pdf.zip` and `…-all-epub.zip` hold every volume; `SHA256SUMS` lists the checksums.

Entry and statement numbers (such as 4.1.12 and Lemma 4.1.12.2) belong to this edition. The entries are the text of
the site; the learner pages were drafted by AI agents and checked as described in `content/PROVENANCE.md`. Text
CC BY-SA 4.0, code MIT. Report errors in an entry at https://github.com/tamnd/algorithm/issues and errors in the
books at https://github.com/tamnd/algorithm-handbook/issues.

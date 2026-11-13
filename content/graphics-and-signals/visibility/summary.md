## What to remember

- [Object space](/object-space-vs-image-space/) decides visibility exactly on the geometry; image space decides it at samples, and only there. For $n$ triangles the output of [hidden-surface removal](/hidden-surface-removal/) can have $\Theta(n^2)$ pieces, so $O(n^2)$ time is optimal in the worst case.
- A [culling](/visibility-culling/) test is exact ($K = V$), conservative ($K \supseteq V$), aggressive ($K \subseteq V$) or approximate. [Back-face](/back-face-culling/), [frustum](/frustum-culling/), [occlusion](/occlusion-culling/) and [portal](/portal-culling/) culling are conservative; a [potentially visible set](/potentially-visible-set/) built by sampling is aggressive.
- The [painter's algorithm](/painters-algorithm/) is correct only when a valid depth order exists. [BSP tree visibility](/bsp-tree-visibility/) gives a correct order from every eye.
- The [z-buffer](/z-buffer/) needs no order. Its depth precision is finite and uneven, which causes [z-fighting](/z-fighting/). Order still matters for shading: with the [early depth test](/early-depth-test/), front to back shades one fragment per pixel and a random order $H_d$ on average.
- An [occlusion query](/occlusion-query/) count of zero proves a box hidden, when the eye is outside it; a positive count proves nothing about the object.
- [Shadow mapping](/shadow-mapping/) is exact only at texel centers with zero bias. The [shadow volume algorithm](/shadow-volume-algorithm/) is exact per sample for closed meshes, and z-fail stays right with the eye inside a volume.
- In a simple polygon the [visibility polygon](/visibility-polygon/) is star-shaped and found in $\Theta(n)$ time. $\lfloor n/3 \rfloor$ guards always suffice and are sometimes needed, $\lfloor n/4 \rfloor$ for orthogonal polygons, and the least number is [NP-hard](/minimum-guard-np-hardness/) to find.

| Method | Precision | Scene | Cost | Guarantee |
|---|---|---|---|---|
| Back-face culling | object | closed oriented solids | $\Theta(n)$ | conservative |
| Frustum culling | object | bounding boxes | $O(1)$ per box | conservative |
| Painter's | object order | polygons | $\Theta(n \log n + P)$ | if a depth order exists |
| BSP tree | object order | static polygons | $\Theta(m + P)$ per view | valid order from every eye |
| z-buffer | image | triangles | $\Theta(WH + n + P)$ | exact at samples |
| [Warnock](/warnock-algorithm/) | image | polygons | $O(nWH)$ | exact at pixel centers |
| [Depth peeling](/depth-peeling/) | image | triangles | $\Theta((d + 1)(WH + n + P))$ | exact at samples |
| [Hierarchical z-buffer](/hierarchical-z-buffer/) | image | octree, pyramid | $O(WH + B + (n + P) \log(W + H))$ | conservative |
| Occlusion culling | image | objects with boxes | $O(n \log n + (n + t) A)$ | conservative |
| Portal culling | object | cells, portals | $O(Sd)$ | conservative |
| Shadow mapping | image, from light | any | $\Theta(WH + n + P + q(r + 1)^2)$ | approximate |
| Shadow volumes | object, image count | closed meshes | $O(tA)$ fill | exact per sample |
| [Roberts](/roberts-hidden-line-algorithm/) | object | convex solids | $O(n^2 (f + \log n))$ | exact |
| [Appel](/appel-hidden-line-algorithm/) | object | closed solids | $O(n(c \log c + s))$ | exact |
| [Lee](/lee-visibility-polygon-algorithm/) | object, plane | simple polygon | $\Theta(n)$ | exact |

: Visibility methods by model and cost. $W \times H = A$ is the image, $P$ the covered samples, $m$ the BSP fragments and $d$ the depth complexity; other letters are as in each entry. Costs are worst case.

## Choosing a method

For real-time triangles, use the z-buffer behind back-face and frustum culling, and draw roughly front to back or after a depth prepass. Add occlusion queries or a hierarchical z-buffer when large occluders hide much of the scene, and portals when it is split into rooms. Use the [A-buffer](/a-buffer/) or depth peeling only for transparency in order.

For a static scene, a moving eye and no depth buffer, build a BSP tree once. For exact line drawings, use Appel on closed solids, or Roberts for a few convex ones.

For shadows of large or open scenes, use shadow mapping and tune the bias; for exact hard shadows of a few closed meshes, use shadow volumes with z-fail. In a polygon use Lee, and for terrain use a profile scan per line of sight or a radial sweep for the viewshed.

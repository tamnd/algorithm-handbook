## What to remember

- Every structure filters with **boxes**, at $\Theta(d)$ per test, and then checks the real shapes. A uniform query point in a node of volume $V$ enters $\operatorname{cov}/V$ children on average, where $\operatorname{cov}$ is the sum of the children's volumes, so **overlap** and **dead space** cost visits.
- **Space partitioning** gives disjoint cells but must clip, copy or lift an object that crosses a border. **Object partitioning** stores each object once, in boxes that may overlap.
- A **uniform grid** with cell side $h$ inserts in $O(1)$ and answers a query of radius $r$ in $O((2\lceil r/h \rceil + 1)^2 + m)$ time. **Spatial hashing** keeps only the occupied cells, under $H(i, j) = ((i \cdot p_1) \oplus (j \cdot p_2)) \bmod T$.
- A balanced **k-d tree** uses $\Theta(n)$ space, builds in $O(n \log n)$ and answers a range query in $O(n^{1-1/k} + r)$ time. The bound is tight, even for empty queries.
- The **PR quadtree** is a trie on the bits of the coordinates. Its shape does not depend on the order of insertion, its height is at most $D$, and it has at most $1 + 4Dn/(B+1)$ nodes. A **region quadtree** with $L$ leaves has $(4L-1)/3$ nodes.
- The **Z-order** interleaves bits; an aligned block of side $2^k$ is one run of keys, a general box several. On the **Hilbert curve**, keys $m$ apart lie $O(\sqrt m)$ apart. **Geohash** is the Z-order of longitude and latitude in base 32; $p$ characters give $\lceil 5p/2 \rceil$ bits of longitude and $\lfloor 5p/2 \rfloor$ of latitude.
- An **R-tree** keeps every leaf at one depth and every non-root node between $m$ and $M$ entries, so its height is at most $\log_m(n/2)$. A search is $O(n)$ in the worst case. The **quadratic split** costs $O(dn^2)$ and is a heuristic; the **R*-tree** adds overlap, margin and forced reinsertion of 30% of the entries.
- A packed R-tree has full nodes, against about 70% after insertions. **STR** builds one in $O(dn \log n)$ time. Only the **priority R-tree** guarantees $O(\sqrt{N/B} + T/B)$ block reads per window query, which is optimal for R-trees.

## The main structures side by side

| Structure | Kind | Query | Update | Space |
|---|---|---|---|---|
| [Uniform grid](/uniform-grid/) | space | $O((2\lceil r/h \rceil + 1)^2 + m)$ radius | $O(1)$ insert | $O(c + n)$ |
| [Spatial hashing](/spatial-hashing/) | space | $O(c + s + cE/T)$ expected | $O(c)$ insert | $O(T + E)$ |
| [Grid file](/grid-file/) | space | $O(\log X + \log Y)$ lookup, 2 disk accesses | $O(XY + B)$ insert | $O(XY + n)$ |
| [k-d tree](/kd-tree/) | space | $O(n^{1-1/k} + r)$ range | $O(h)$ insert | $\Theta(n)$ |
| [PR quadtree](/pr-quadtree/) | space | $O(D + B)$ search | $O(DB)$ insert | $O(nD/B + n)$ |
| [Region quadtree](/region-quadtree/) | space | $O(D)$ get | $O(D)$ set | $O(p + D)$ nodes |
| [MX-CIF quadtree](/mx-cif-quadtree/) | space | $O(Dm)$ stab | $O(D + m)$ insert | $O(nD)$ |
| [R-tree](/r-tree/) | objects | $O(n)$ search | $O(M^2 \log n / \log m)$ insert | $O(n)$ |
| [R*-tree](/r-star-tree/) | objects | $O(n)$ search | $O(pM^2h^2)$ insert | $O(n)$ |
| [R+-tree](/r-plus-tree/) | mixed | $O(c)$ search | $O(cM^2)$ insert | $O(c)$, $c \ge n$ copies |
| [Priority R-tree](/priority-r-tree/) | objects | $O(\sqrt{N/B} + T/B)$ window | static | $O(N/B)$ |

: Worst-case bounds as stated in the entries, except where marked expected. $D$ is the number of halvings from the root to a unit cell, $B$ a bucket capacity, $c$ a number of cells or of copies; the other letters are defined in the entries.

## Choosing a structure

- For points of roughly even density and queries of a fixed radius, use a uniform grid with a cell side close to the radius. Use spatial hashing when most cells would be empty.
- For a static set of points in memory, in a few dimensions, use a k-d tree built by medians.
- For images and regions, use a region quadtree, or a linear quadtree in a B-tree.
- For rectangles and polygons in a database that changes, use an R*-tree. For a static set, pack an R-tree with STR or the Hilbert order; use the priority R-tree when a bad query must not read the whole tree.
- On top of a B-tree or key-value store, use Z-order or Hilbert keys, and geohash or S2 cell ids on the globe.
- For moving objects in a game, use a grid, a spatial hash or a loose octree, or sweep and prune.
- Above a few tens of dimensions, measure a linear scan first: the trees often read most of their nodes there.

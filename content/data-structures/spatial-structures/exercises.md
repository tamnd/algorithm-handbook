1. ◦ A node of a spatial index has the region $R = [0, 12] \times [0, 8]$ and three children with the boxes $R_1 = [0, 7] \times [0, 5]$, $R_2 = [5, 12] \times [2, 8]$ and $R_3 = [1, 4] \times [4, 8]$. Compute the coverage, the [overlap](/overlap-and-dead-space/) and the dead space of the node with respect to its children. How many children does a uniform random query point in $R$ enter on average?

2. ◦ A [uniform grid](/uniform-grid/) has its origin at $(0, 0)$ and cells of side $h = 5$. Which cell holds the point $(13, 27)$? A radius query with center $(13, 27)$ and $r = 7$ scans every cell that meets the square $[6, 20] \times [20, 34]$. How many cells is that, and what is the bound $(2\lceil r/h \rceil + 1)^2$?

3. ◦ With $x$ in the even bits, as in the [Z-order curve](/z-order-curve/) entry, compute the Z-order code of the cell $(5, 3)$ in an $8 \times 8$ grid. Which cell has the code 45?

4. ◦ Compute the [geohash](/geohash/) of three characters of the point at latitude $48.8566$ and longitude $2.3522$. Give the cell it names, as intervals of latitude and longitude, and the size of the cell in degrees.

5. ◦ Build a balanced [k-d tree](/kd-tree/) on $(6, 2)$, $(2, 7)$, $(9, 8)$, $(4, 4)$, $(1, 1)$, $(8, 5)$, $(5, 9)$, splitting on $x$ at the root, with the median of each subtree at its root and the $\lfloor s/2 \rfloor$ smaller points on the left. Draw the tree and give its height. Which nodes does a range query with the box $[0, 3] \times [0, 5]$ visit, and what does it report?

6. ◦ Build the [PR quadtree](/pr-quadtree/) with $D = 3$ and $B = 1$ on the points $(1, 1)$, $(2, 3)$, $(6, 5)$, $(7, 6)$, $(5, 1)$, $(6, 1)$ in the square $[0, 8)^2$. How many nodes does it have, how many of its leaves are empty, and what is the depth of its deepest leaf?

7. ◦ An $8 \times 8$ binary image has the black pixels $(x, y)$ with $0 \le x \le 2$ and $0 \le y \le 2$, a $3 \times 3$ square in a corner. How many nodes, leaves and black leaves does its [region quadtree](/region-quadtree/) have? Check the count of nodes against the formula $(4L - 1)/3$.

8. ◦ An [R-tree](/r-tree/) has $M = 100$ and $m = 40$ and holds $n = 10^8$ rectangles. Between which bounds must the depth of its leaves lie, with the root at depth 0? A node of another R-tree, with $M = 8$ and $m = 3$, overflows. How many feasible [splits](/r-tree-node-splitting/) of its 9 entries are there?

9. ◦ Take the area of the Earth as 510 million km². How many cells does the [S2 cell hierarchy](/s2-cell-hierarchy/) have at level 12, and what is their average area? Answer the same for H3 at resolution 7, which has $2 + 120 \cdot 7^r$ cells at resolution $r$, as given in the entry on [discrete global grid systems](/discrete-global-grid-system/).

10. • In the tree of Exercise 5, run a range query with the box $[3, 7] \times [5, 9]$, going left when $\ell_a \le p_a$ and right when $h_a \ge p_a$. Which nodes does it visit, and what does it report? Then find the nearest neighbor of $(7, 6)$ by branch and bound, nearer side first. Which nodes does the search visit, and which subtree does it prune?

11. • Using the [Hilbert curve](/hilbert-curve/) of the entry, whose first order visits $(0,0)$, $(0,1)$, $(1,1)$, $(1,0)$, compute the Hilbert index of the cell $(6, 1)$ in an $8 \times 8$ grid. Give the quadrant digit of each of the three levels.

12. • In an $8 \times 8$ grid, take the box $[2, 5] \times [1, 2]$ of eight cells. List its Z-order codes and its Hilbert indexes. Into how many runs of consecutive keys does each split? What is the smallest Z-order code greater than 13 that lies in the box?

13. • In an $8 \times 8$ grid, which cells have the Z-order codes 31 and 32, and how far apart are their centers? Generalize to a $2^D \times 2^D$ grid: give two consecutive codes whose cells are about the side of the grid apart. Why can this never happen on the Hilbert curve?

14. • Compute the geohashes of three characters of the points $(51.4779, -0.0015)$ and $(51.4779, 0.0015)$, given as latitude and longitude. How long is their common prefix, and about how far apart are the points? What does this mean for a search that looks for the neighbors of a point by its geohash prefix?

15. • Run the [quadratic split](/quadratic-split/) with $m = 2$ on the five rectangles $a = [0, 2] \times [0, 3]$, $b = [1, 3] \times [6, 8]$, $c = [8, 9] \times [0, 2]$, $d = [6, 10] \times [7, 9]$ and $e = [3, 5] \times [1, 2]$. Give the seeds, the choice of each round and the two groups with their boxes. Compare the total area with that of the best of all feasible splits.

16. • Build an R-tree on $n = 1000$ points with [STR packing](/str-packing/) and $M = 10$. Give, for each level, the number of entries, the number $S$ of slices, the sizes of the slices and the number of nodes made. What are the height and the number of nodes? Do the same for $n = 1001$.

17. • Six boxes are $A = [0, 4] \times [0, 3]$, $B = [2, 6] \times [5, 8]$, $C = [5, 10] \times [1, 4]$, $D = [7, 11] \times [6, 9]$, $E = [9, 13] \times [2, 5]$ and $F = [3, 8] \times [7, 10]$. Sweep and prune on $x$, as in [collision detection](/collision-detection/), reports the pairs whose $x$ intervals overlap. How many candidate pairs does it report, and how many of them really overlap? Then give $n$ boxes for which it reports all $\binom{n}{2}$ pairs while no two boxes overlap.

18. • Write the [linear quadtree](/linear-quadtree/) of the image of Exercise 7: the sorted list of its black blocks as pairs (Morton code of the lower left pixel, level). Then locate the pixels $(1, 1)$ and $(3, 1)$ by binary search in the list.

19. • A [loose octree](/loose-octree/) has the root cube $[0, 64)^3$, so $D = 6$, and looseness 2. Where does it place the box $[33, 38] \times [10, 13] \times [47, 50]$: at what depth, in which cell, and with which loose cell? At what depth would a plain [octree](/octree/) of objects store the same box, if each box goes to the smallest cell that contains it?

20. • A radius query on a uniform grid scans at most $\lceil 2r/h \rceil + 1$ cells along each axis. For $h = r$, $h = r/2$ and $h = r/4$, give the number of cells scanned in the plane and their total area. What does the area tend to as $h$ shrinks, and how does it compare with the area $\pi r^2$ of the disk?

21. • [Spatial hashing](/spatial-hashing/) maps the cell $(i, j)$ to $((i \cdot 73856093) \oplus (j \cdot 19349663)) \bmod T$. Take $T = 16$. Compute the buckets of the 16 cells with $0 \le i, j \le 3$. How many buckets do they use, and which cells share a bucket?

22. ★ A balanced k-d tree in the plane is built on $n = 2^H - 1$ points with distinct coordinates, splitting on $x$ at even depths. A vertical line $x = c$ and a horizontal line $y = c$ each hold no point. Find, for $n = 63$ and $n = 255$, the exact number of nodes that a range query with each line visits. Give the general formula for even $H$, and the ratio of the two counts. This is the tight case of the [range query bound](/kd-tree-range-query-complexity/).

23. ★ A PR quadtree with $B = 1$ holds 4 points with integer coordinates in a square of side $2^{10}$. What is the largest number of nodes it can have? Prove that no 4 points give more, and compare the answer with the general bound $1 + 4Dn/(B+1)$.

24. ★ Two points can be very close and still have no common geohash prefix. Find all points of the globe that have, arbitrarily close to them, a point whose geohash starts with a different character.

25. ★ In the hash of Exercise 21, let $T = 2^k$. Show that every block of $T \times T$ consecutive cells puts exactly $T$ cells in each bucket, and that $(i, j)$ and $(i + T, j)$ always share a bucket. What happens to a long corridor of objects one cell wide?

26. ★ On the Hilbert curve of a $2^D \times 2^D$ grid, take the two neighbor cells $(2^{D-1} - 1, 0)$ and $(2^{D-1}, 0)$ on the bottom row. Show that their indexes are $(4^{D-1} - 1)/3$ and $4^D - 1 - (4^{D-1} - 1)/3$, so that they differ by $(10 \cdot 4^{D-1} - 1)/3$, more than half the number of cells. Give the numbers for $D = 3$.

Put a rubber band around a set of nails in a board and let it go. It snaps onto the outer nails and makes a convex polygon: the convex hull of the set. The hull is the first shape most programs in geometry compute, because it throws away the points that cannot matter for many questions. The two points farthest apart are corners of the hull. The narrowest slot a part can pass through is set by the hull. A robot arm that must not touch an obstacle can treat the obstacle as its hull. A collision test between two convex shapes, a check for whether two classes of points can be split by a line, and the first step of many statistical summaries all start from a hull.

The planar hull is also the problem on which computational geometry learned its methods. Sort and scan, divide and conquer, prune and search, output-sensitive algorithms and lower bounds by reduction from sorting all appear here first, on a problem small enough to see whole.

## What the chapter covers

The chapter is in seven groups, read in order.

1. **Convex sets and their hulls.** The definitions: [convex combinations](/convex-combination/), [convex sets](/convex-set/), the [convex hull](/convex-hull/), [extreme points](/extreme-point/) and [supporting hyperplanes](/supporting-hyperplane/). Short entries, but the algorithms use every word in them.
2. **The problem and its predicates.** The [orientation test](/orientation-test/), one $2 \times 2$ determinant that every planar algorithm uses; the exact statement of the [convex hull problem](/convex-hull-problem/), with its rules for collinear and repeated points; and the split into an [upper and a lower hull](/upper-and-lower-hull/).
3. **Planar hull algorithms.** [Andrew's monotone chain](/andrew-monotone-chain/) and the [Graham scan](/graham-scan/) run in $O(n \log n)$ time. The [Jarvis march](/jarvis-march/) runs in $O(nh)$ time, where $h$ is the number of hull vertices. [Quickhull](/quickhull/) is fast on most inputs but $\Theta(n^2)$ in the worst case. [Melkman's algorithm](/melkman-algorithm/) finds the hull of a simple polyline in linear time.
4. **Lower bounds and output-sensitive hulls.** The [lower bound](/convex-hull-lower-bound/) of $\Omega(n \log n)$, by reduction from sorting, and the $\Theta(n \log h)$ algorithms of [Kirkpatrick and Seidel](/kirkpatrick-seidel/) and of [Chan](/chan-algorithm/), with the [lower bound](/convex-hull-output-sensitive-lower-bound/) that shows they are optimal.
5. **Working with a hull.** [Rotating calipers](/rotating-calipers/) for the diameter and the width, [convex layers](/convex-layers/), the [dynamic convex hull](/dynamic-convex-hull/) under insertions and deletions, and the [concave hull](/concave-hull/).
6. **Three classical theorems.** The theorems of [Carathéodory](/caratheodory-theorem/), [Radon](/radon-theorem/) and [Helly](/helly-theorem/), each about $d + 1$ or $d + 2$ points in $\mathbb{R}^d$.
7. **Polytopes and higher dimensions.** [Convex polytopes](/convex-polytope/) and the [Minkowski–Weyl theorem](/minkowski-weyl-theorem/), which says that a polytope given by vertices can also be given by inequalities and the other way round; the [support function](/support-function/); and hulls in [three and more dimensions](/convex-hull-3d/), built by the [beneath-beyond method](/beneath-beyond/).

## A first reading

For a first reading, take these eleven entries in order: [convex set](/convex-set/), [convex hull](/convex-hull/), [extreme point](/extreme-point/), [orientation test](/orientation-test/), [the convex hull problem](/convex-hull-problem/), [upper and lower hull](/upper-and-lower-hull/), [Andrew's monotone chain](/andrew-monotone-chain/), [Graham scan](/graham-scan/), [Jarvis march](/jarvis-march/), [the lower bound](/convex-hull-lower-bound/) and [rotating calipers](/rotating-calipers/). With these you can compute a hull exactly, with integer arithmetic, and use it.

On a first pass you can skip the output-sensitive algorithms, the classical theorems and the last group. Come back to [Chan's algorithm](/chan-algorithm/) when $h$ is much smaller than $n$ in your data, and to Helly's theorem before reading about linear programming in low dimensions.

## Before you start

You need [points and vectors](/point-and-vector/), the [cross product](/cross-product/) and the [dot product](/dot-product/), which sit with the other primitives in the chapter on polygons. You need [asymptotic notation](/asymptotic-notation/) from Volume 1. The lower bounds use the [sorting lower bound](/comparison-sort-lower-bound/) and the [algebraic decision tree](/algebraic-decision-tree/) model. Several algorithms keep their partial hull on a [stack](/stack/) or a [deque](/deque/), and the dynamic hull uses a [treap](/treap/). The proofs in the theorem group use only linear algebra: linear independence, and the solutions of a homogeneous linear system with more unknowns than equations.

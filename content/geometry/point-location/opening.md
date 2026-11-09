A map program receives a click at some longitude and latitude and must say which country, which county or which postal district the click is in. A finite element code must find the mesh triangle that contains a probe point before it can read off the field there. Both are the same problem. A planar subdivision, a map made of $n$ edges, is fixed, and many query points arrive one at a time; for each, report the face, edge or vertex that contains it.

One query alone is easy: test every face, in $O(n)$ time. The problem is interesting because the map is fixed and the queries are many, so it pays to preprocess. The goal is $O(\log n)$ time per query with $O(n)$ space, the same bounds as binary search in a sorted list, and the chapter shows several ways to reach it. Most of them reduce the question to vertical ray shooting: find the edge directly above the query point, and the face below that edge is the answer.

## What the chapter covers

The chapter is in five groups, read in order.

1. **The problem.** [Planar subdivisions](/planar-subdivision/), [vertical ray shooting](/vertical-ray-shooting/), and [planar point location](/planar-point-location/) itself, with its $\Omega(\log n)$ lower bound and a table of the methods. [Point location in a convex polygon](/convex-polygon-point-location/) is the warm-up: one binary search over angles.
2. **Slabs and persistence.** The [slab method](/slab-method-point-location/) answers in $O(\log n)$ time but may need $\Theta(n^2)$ space. [Sarnak and Tarjan](/sarnak-tarjan-point-location/) store the slab lists as versions of one persistent tree, in $O(n)$ space.
3. **Trapezoidal maps.** The [trapezoidal map](/trapezoidal-map/), built in random order, and [Seidel's algorithm](/seidel-point-location/), which uses its history as the search structure.
4. **Triangulations.** [Kirkpatrick's hierarchy](/kirkpatrick-point-location/) and the [triangle walk](/triangle-walk-point-location/).
5. **Monotone subdivisions and chains.** [Monotone subdivisions](/monotone-subdivision/) and the [chain method](/chazelle-monotone-point-location/) with fractional cascading.

## A first reading

For a first reading, take these seven entries in order: [planar subdivision](/planar-subdivision/), [vertical ray shooting](/vertical-ray-shooting/), [planar point location](/planar-point-location/), [point location in a convex polygon](/convex-polygon-point-location/), [the slab method](/slab-method-point-location/), [the trapezoidal map](/trapezoidal-map/) and [Seidel's algorithm](/seidel-point-location/). The slab method shows the idea in its simplest form, and the trapezoidal map is the method to implement. Several entries share one example, a subdivision of four segments, so the methods can be compared on the same input.

## Before you start

You need the [orientation test](/orientation-test/) from the chapter on convex hulls and [binary search](/binary-search/) from Volume 5. The subdivisions are [planar graphs](/planar-graph/), stored in a [doubly connected edge list](/doubly-connected-edge-list/), from Volume 7, and [Euler's formula](/euler-formula/) bounds their size. For Sarnak and Tarjan you need the [persistent binary search tree](/persistent-binary-search-tree/) from Volume 3. For the trapezoidal map you need [randomized incremental construction](/randomized-incremental-construction/) and [backwards analysis](/backwards-analysis/) from Volume 2, and for the chain method [fractional cascading](/multiple-list-search/) from Volume 5. Kirkpatrick's method and the walk start from a [triangulation](/triangulation/), from the chapter on triangulations. The roadmap below lists every entry of the chapter with its kind and level, and the figure after it shows which entries lean on which.

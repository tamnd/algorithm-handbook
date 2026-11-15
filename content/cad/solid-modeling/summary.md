## What to remember

- A solid is an [r-set](/r-set/): bounded, closed, equal to the closure of its interior, with a finite description. The [regularized operations](/regularized-set-operations/) $A \cap^* B = \operatorname{cl}(\operatorname{int}(A \cap B))$ keep r-sets closed and drop dangling faces and edges; [Nef polyhedra](/nef-polyhedron/) and the [selective geometric complex](/selective-geometric-complex/) keep them.
- A [CSG tree](/constructive-solid-geometry/) is easy to edit and always valid; only some face sets are valid [B-reps](/boundary-representation/). A [sweep](/sweep-representation/) classifies a point in $O(n)$ time but is not closed under Booleans. [Boundary evaluation](/boundary-evaluation/) turns a tree into a boundary; the [converse](/brep-to-csg-conversion/) may need extra half-spaces.
- The [Euler-Poincaré formula](/euler-poincare-formula/) $V - E + F - R = 2(S - H)$ holds for every manifold B-rep. It is necessary, not sufficient. The [Euler operators](/euler-operators/) keep it true and reach every valid topology.
- [Set membership classification](/set-membership-classification/) splits a point, segment or face into its parts in, on and out of a solid, with neighborhoods where boundaries meet, and drives [CSG ray casting](/csg-ray-casting/), boundary evaluation and the [B-rep Booleans](/solid-boolean-operations/), whose output can have $\Theta(nm)$ size.
- In [surface-surface intersection](/surface-surface-intersection/), algebraic surfaces of degrees $m$ and $n$ meet in a curve of degree at most $mn$. [Marching](/marching-surface-intersection/) can miss closed loops without a loop test; [subdivision](/subdivision-surface-intersection/) finds every piece, but only to a tolerance.
- An [offset surface](/offset-surface/) is regular while $|d|$ is below every radius of curvature. [Solid offsetting](/solid-offsetting/) is a Minkowski sum with a ball: rounding is shrink then grow, filleting grow then shrink. Convex polytopes [add](/minkowski-sum-of-polyhedra/) face by face, but nonconvex sums can have $\Theta(n^3 m^3)$ faces.
- With floating point, [predicates](/geometric-robustness-problem/) can contradict each other. [Exact geometric computation](/exact-geometric-computation/) makes every sign exact, and [simulation of simplicity](/simulation-of-simplicity/) breaks ties consistently. Closeness within a tolerance is not transitive, so [healing](/brep-healing/) and [tolerant modeling](/tolerant-modeling/) can join points farther apart than the tolerance.
- [Mirtich's algorithm](/mirtich-polyhedral-mass-properties/) computes the mass properties of a polyhedron exactly in $\Theta(n)$ time.
- [Interacting features](/feature-interaction/) have several readings, since the part depends only on the union of the removed volumes. [Hint-based recognition](/hint-based-feature-recognition/) and [volume decomposition](/volume-decomposition-feature-recognition/) are exact on rectilinear sections, and the [alternating sum of volumes](/alternating-sum-of-volumes/) ends in the plane but can cycle in three dimensions. [Generic naming](/generic-naming-scheme/) is proved correct only when an edit keeps the labeled topology.

| Method | Model | Time | Guarantee |
|---|---|---|---|
| Set membership classification | real RAM, exact predicates | $O(m + L^2)$ per point | exact in, on, out |
| CSG ray casting | real RAM | $O(m + L h)$ per ray | exact intervals, regularized |
| Boundary evaluation, planar | real RAM, rational input | $O(m^4)$ | exact, degenerate input included |
| Vertex neighborhood classification | real RAM | $O(n^2 \log n)$ | exact, touching cases included |
| Selective geometric complex, planar | real RAM | $O((n + k)^2)$ | exact, nothing regularized |
| Marching intersection | real RAM with roots, Newton | $O(n i)$ | local; can miss loops |
| Subdivision intersection | real RAM, tolerance | $O(16^k n d)$ worst | all pieces to the tolerance |
| Rolling-ball blend | real RAM with roots, Newton | $O(m(i + k))$ | $G^1$, not $G^2$ |
| Minkowski sum, convex | word RAM | $O(nm(n + m))$ | exact |
| Mirtich mass properties | real RAM, rational input | $\Theta(n)$ | exact |
| Attributed adjacency graph | word RAM | $O(E \log E + n t k! k^2)$ | exact match; use measured |
| Hint-based recognition, rectilinear | word RAM | $O(n^3)$ | exact |
| Alternating sum of volumes, planar | word RAM | $O(n^2 \log n)$ | ends, unique result |

: The main methods. $L$ primitives in a tree of height $h$ with $m$ edges or faces; $n$ the input size, and $m$ that of the second polytope in a Minkowski sum; $i$ Newton steps per point; $k$ crossings, depth, arc points or template size.

## Choosing a method

Edit a model through its CSG tree or feature history, or by [direct modeling](/direct-modeling/) when it has none. For Booleans, use boundary evaluation on trees of planar primitives and [vertex neighborhood classification](/vertex-neighborhood-classification/) on two manifold B-reps. Store manifold boundaries in a [winged edge](/winged-edge-data-structure/), non-manifold edges in a [radial edge](/radial-edge-data-structure/), and dangling pieces in a Nef polyhedron.

For curved faces, subdivide until a loop test passes, then march. Fillet single edges with the [rolling ball](/rolling-ball-blend/), and offset a CSG tree with [Rossignac and Requicha's method](/rossignac-requicha-offsetting/). Make every predicate exact, with a floating-point filter. Heal imported models with a tolerance far below the smallest feature. Use Mirtich's formulas on polyhedra, and [Monte Carlo](/monte-carlo-integration/) with a stated error on the rest. Use the [attributed adjacency graph](/attributed-adjacency-graph/) for isolated prismatic features and a volumetric recognizer when features interact.

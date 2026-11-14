## What to remember

- A solid is an [r-set](/r-set/): bounded, closed, equal to the closure of its interior, with a finite description. The [regularized operations](/regularized-set-operations/) $A \cap^* B = \operatorname{cl}(\operatorname{int}(A \cap B))$ keep r-sets closed under union, intersection and difference, and drop dangling faces and edges.
- A [CSG tree](/constructive-solid-geometry/) is easy to edit and always valid. A [B-rep](/boundary-representation/) is easy to render, but only some face sets are valid. [Boundary evaluation](/boundary-evaluation/) turns a tree into a boundary; the [converse](/brep-to-csg-conversion/) may need extra half-spaces.
- The [Euler-Poincaré formula](/euler-poincare-formula/) $V - E + F - R = 2(S - H)$, with rings $R$, shells $S$ and holes $H$, holds for every manifold B-rep. It is necessary, not sufficient. The [Euler operators](/euler-operators/) keep it true and reach every valid topology.
- [Set membership classification](/set-membership-classification/) splits a point, segment or face into its parts in, on and out of a CSG solid. Where boundaries meet, it needs neighborhoods. It drives [CSG ray casting](/csg-ray-casting/), boundary evaluation and the [B-rep Booleans](/solid-boolean-operations/), whose output can have $\Theta(nm)$ size.
- [Surface-surface intersection](/surface-surface-intersection/) is the hard step. Two algebraic surfaces of degrees $m$ and $n$ meet in a curve of degree at most $mn$. [Marching](/marching-surface-intersection/) is fast along a branch but can miss closed loops unless a loop test rules them out. [Subdivision](/subdivision-surface-intersection/) finds every piece, but only to a tolerance.
- An [offset surface](/offset-surface/) at distance $d$ is regular while $|d|$ is below every radius of curvature; past a radius on the concave side it folds. [Solid offsetting](/solid-offsetting/) grows by a ball and shrinks by the complement: rounding is shrink then grow, filleting is grow then shrink. Growing commutes with union, not with intersection.
- The proofs assume exact real numbers. With floating point, [predicates](/geometric-robustness-problem/) can contradict each other and a Boolean can return an open boundary. [Exact geometric computation](/exact-geometric-computation/) makes every sign exact, and [simulation of simplicity](/simulation-of-simplicity/) breaks the remaining ties consistently.
- [Mirtich's algorithm](/mirtich-polyhedral-mass-properties/) computes the mass properties of a polyhedron exactly in $\Theta(n)$ time. From CSG, the volume of a union of boxes needs $\Omega(n \log n)$ algebraic decisions.
- [Feature recognition](/feature-recognition/) and [persistent naming](/persistent-naming-problem/) compute what they define; whether that is what the designer meant is measured on test parts.

| Method | Model | Time | Guarantee |
|---|---|---|---|
| Set membership classification | real RAM, exact predicates | $O(m + L^2)$ per point | exact in, on, out |
| CSG ray casting | real RAM | $O(m + L h)$ per ray | exact intervals, regularized |
| Boundary evaluation, planar | real RAM, rational input | $O(m^4)$ | exact boundary, degenerate input included |
| Vertex neighborhood classification | real RAM | $O(n^2 \log n)$ | exact, touching cases included |
| Voxel Booleans | hash table | $O(m)$ expected | exact on cells |
| Marching intersection | real RAM with roots, Newton | $O(n i)$ | local; can miss loops |
| Subdivision intersection | real RAM, tolerance | $O(16^k n d)$ worst | finds all pieces to the tolerance |
| Rolling-ball blend | real RAM with roots, Newton | $O(m(i + k))$ | $G^1$, not $G^2$ |
| Mirtich mass properties | real RAM, rational input | $\Theta(n)$ | exact |
| Monte Carlo volume | random points | $O(N)$ tests | error of order $1/\sqrt{N}$, expected |
| Attributed adjacency graph | word RAM | $O(E \log E + n t k! k^2)$ | exact match; use measured |

: The main methods. $L$ primitives in a tree of height $h$ with $m$ edges or faces; $n$ edges, points or control points; $i$ Newton steps per point; $k$ depth, arc points or template size; $N$ samples.

## Choosing a method

Keep a CSG tree or a feature history for a model that a designer edits, and evaluate it to a B-rep when the faces are needed. For Booleans, use boundary evaluation on trees of planar primitives and [vertex neighborhood classification](/vertex-neighborhood-classification/) on two manifold B-reps. Store manifold boundaries in a [winged edge](/winged-edge-data-structure/) or half-edge structure, and use the [radial edge](/radial-edge-data-structure/) when an edge has more than two faces. Use an [octree](/octree/) when a fixed resolution will do.

For curved faces, use closed forms for quadrics, and for freeform patches subdivide until the normal-cone test excludes loops, then march. Fillet single edges with the [rolling ball](/rolling-ball-blend/), and offset a CSG tree with [Rossignac and Requicha's method](/rossignac-requicha-offsetting/). Make every predicate exact, with a floating-point filter, and add simulation of simplicity if the code assumes general position. For mass properties, use Mirtich's formulas on polyhedra, and cells or [Monte Carlo](/monte-carlo-integration/) with a stated error on the rest. Use the [attributed adjacency graph](/attributed-adjacency-graph/) for isolated prismatic features and pass the rest to a volumetric recognizer.

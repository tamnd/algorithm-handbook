## What to remember

- A constraint system is counted on its weighted graph: the density $\rho(S) = w(E(S)) - w(S)$, and a rigid part keeps the $D = d(d + 1)/2$ freedoms of a rigid motion. The counts are necessary for a regular solution; they are sufficient only in special cases, such as points and distances in the plane at generic values.
- A framework with $n$ joints in $\mathbb{R}^d$ is infinitesimally rigid when its rigidity matrix has rank $dn - D$, which implies rigidity. At generic positions the two notions agree and depend only on the graph. Maxwell's rule in Calladine's form reads $m - (dn - D) = s - f$.
- Laman's theorem: a graph with $2n - 3$ edges is generically minimally rigid in the plane if and only if every $k \ge 2$ vertices span at most $2k - 3$ edges. The pebble game tests this in $O(n^2)$ time. In space the count is not sufficient: the double banana, with $n = 8$ and $m = 18 = 3n - 6$, flexes.
- Tay's theorem: rigid bodies joined by bars in general position are generically rigid in $\mathbb{R}^d$ if and only if the multigraph contains $D$ edge-disjoint spanning trees.
- Triangle-decomposable sketches are solved by $n - 2$ quadratic steps after an $O(n^2)$ analysis, with up to $2^{n-2}$ real solutions up to proper motion. The 3-connected Laman graphs where decomposition stops, such as the prism, are not solvable by radicals for generic lengths, and a Laman graph has at most $\binom{2n-4}{n-2}$ complex solutions; the prism reaches 24.
- No theorem defines the solution the user meant. Solvers keep the orientations of the draft, computed exactly, and the choice is judged by use; with extra conditions the choice is NP-hard, already on a line.
- Global rigidity needs $(d + 1)$-connectivity and redundant rigidity; in the plane these suffice for generic frameworks (Jackson and Jordán), so a minimally rigid sketch with $n \ge 4$ points has several solutions at generic values. In space they do not suffice.
- Realization with given lengths is NP-complete on a line, strongly NP-hard in every fixed dimension, and complete for the existential theory of the reals in the plane.

## The methods side by side

| Method | Input | Cost | What is guaranteed |
|---|---|---|---|
| Local propagation | equations with a ready order | $O(\lvert X \rvert + \sum_c \lvert c \rvert)$ plus the solves | exact when an order exists; stops on any cycle |
| Newton's method from the draft | any square system | one linear solve per step | quadratic convergence near a regular solution, in floating point; one solution |
| Fudos-Hoffmann reduction | points and distances in the plane | $O(m(n + m))$, $O(n^2)$ on a Laman graph | decides triangle-decomposability; exact ruler-and-compass plan |
| Owen's decomposition | points and distances in the plane | $O(n^2)$ with a linear-time separation pair search | the same class of graphs as Fudos-Hoffmann |
| Pebble game | a graph | $O(nm)$; $O(n^2)$ for the Laman test | exact Laman counts, so generic rigidity in the plane |
| Flow-based DOF analysis | weighted constraint graph | polynomial | finds sets that are dense by the count; the count can mislead |
| Tay test by tree packing | body-and-bar multigraph | polynomial | generic rigidity of bodies and bars in every dimension |
| Jackson-Jordán test | a graph | polynomial | generic global rigidity in the plane |

: The main methods of the chapter. Counting tests speak about generic values; the first four rows work at the given values.

## Choosing a method

For a planar sketch, run a decomposition solver first. The Fudos-Hoffmann reduction or Owen's decomposition gives every real solution of a triangle-decomposable sketch, and the draft orientations, from an exact [orientation test](/orientation-test/), select the one the user drew. When the analysis stops on a 3-connected part, solve that part numerically, by Newton's method from the draft or by homotopy continuation for all solutions, and let a [DR-plan](/dr-plan/) keep that part small.

Check the counts before solving: the [pebble game](/pebble-game-rigidity/) finds redundant distances and rigid components, and [degrees of freedom analysis](/degrees-of-freedom-analysis/) finds dense sets for general entities. A count that passes does not prove a regular solution; in space, or with parallel or concurrent elements, also check the rank of the Jacobian at the solution.

Use [local propagation](/local-propagation-solving/) for systems known to be acyclic, such as dimension chains. For bodies with generic bar-like mates, [Tay's theorem](/tay-theorem/) decides rigidity; for mates whose freedoms overlap, such as a pin with a shoulder, rely on the rank. When the answer must be unique, as in sensor localization, test [global rigidity](/global-rigidity/) with the [Jackson-Jordán theorem](/jackson-jordan-theorem/).

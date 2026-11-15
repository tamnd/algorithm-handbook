## What to remember

- A constraint system is counted by the density $\rho(S) = w(E(S)) - w(S)$ of its weighted graph; a rigid part keeps the $D = d(d + 1)/2$ freedoms of a rigid motion. The counts are necessary for a regular solution, and sufficient only in special cases such as generic points and distances in the plane.
- A framework in $\mathbb{R}^d$ is infinitesimally rigid when its [rigidity matrix](/rigidity-matrix/) has rank $dn - D$, which implies rigidity. At a regular placement the two notions agree ([Asimow and Roth](/asimow-roth-theorem/)), and at generic positions they depend only on the graph. Maxwell's rule reads $m - (dn - D) = s - f$.
- Laman's theorem: a graph with $2n - 3$ edges is generically minimally rigid in the plane if and only if every $k \ge 2$ vertices span at most $2k - 3$ edges; the pebble game tests this in $O(n^2)$ time. In space the count fails: the [double banana](/double-banana-graph/) passes the $3k - 6$ counts and flexes.
- Tay's theorem: rigid bodies joined by bars in general position are generically rigid in $\mathbb{R}^d$ if and only if the multigraph contains $D$ edge-disjoint spanning trees.
- A triangle-decomposable sketch is solved by $n - 2$ quadratic steps after an $O(n^2)$ analysis, with up to $2^{n-2}$ real solutions up to proper motion. The 3-connected Laman graphs where decomposition stops, such as the prism, are not solvable by radicals for generic lengths. No theorem defines the solution the user meant: solvers keep the draft orientations, computed exactly, and with extra conditions the choice is NP-hard.
- A complete distance table comes from points in $\mathbb{R}^d$ exactly when its Gram matrix is positive semidefinite of rank at most $d$. With some distances missing, realization is NP-complete on a line, strongly NP-hard in every fixed dimension, and complete for the existential theory of the reals in the plane.
- Generic global rigidity with $n \ge d + 2$ needs $(d + 1)$-connectivity and redundant rigidity ([Hendrickson](/hendrickson-global-rigidity-conditions/)); they suffice in the plane (Jackson and Jordán) but not in space. In every dimension it holds exactly when some [stress matrix](/equilibrium-stress-matrix/) has rank $n - d - 1$ (Connelly; [Gortler, Healy and Thurston](/gortler-healy-thurston-theorem/)): it depends only on the graph.

## The methods side by side

| Method | Input | Cost | What is guaranteed |
|---|---|---|---|
| Local propagation | equations with a ready order | linear plus the solves | exact when an order exists; stops on any cycle |
| Newton's method from the draft | any square system | one linear solve per step | one solution; quadratic convergence near a regular one, in floating point |
| Rule-based solving | constraints and rules | depends on the rules | monotone rules give the same result in any order |
| Fudos-Hoffmann or Owen | points and distances in the plane | $O(n^2)$ on a Laman graph | decides triangle-decomposability; ruler-and-compass plan |
| Gram factorization | all distances | $O(n^3)$ | realizability, coordinates |
| Pebble game | a graph | $O(n^2)$ for the Laman test | generic rigidity in the plane |
| DOF analysis, Frontier | weighted constraint graph | polynomial | dense sets and a DR-plan; the count can mislead |
| Tay test by tree packing | body-and-bar multigraph | polynomial | generic rigidity of bodies and bars |
| Witness configuration | any constraint system | one exact rank | generic rank; "rigid" is always right |
| Jackson-Jordán test | a graph | polynomial | generic global rigidity in the plane |
| Stress rank test | a graph | randomized polynomial | generic global rigidity in every dimension; "globally rigid" is always right |

: The main methods of the chapter. Counting and random-point tests speak about generic values; the others work at the given values.

## Choosing a method

For a planar sketch, run a decomposition solver first. It gives every real solution of a triangle-decomposable sketch, and exact [orientation tests](/orientation-test/) on the draft select the one the user drew. If the analysis stops on a 3-connected part, solve it by Newton's method from the draft or homotopy continuation, and let a [DR-plan](/dr-plan/) keep it small.

Check the counts first, by the [pebble game](/pebble-game-rigidity/) or [degrees of freedom analysis](/degrees-of-freedom-analysis/). A passing count does not prove a regular solution; in space, or with parallel or concurrent elements, confirm it by the [witness configuration method](/witness-configuration-method/) and by the rank at the solution.

Use [local propagation](/local-propagation-solving/) for acyclic systems such as dimension chains. [Tay's theorem](/tay-theorem/) decides rigidity for bodies with generic bar-like mates; for overlapping mates, rely on the rank. When the answer must be unique, test global rigidity with the [Jackson-Jordán theorem](/jackson-jordan-theorem/) in the plane and the stress rank test in space.

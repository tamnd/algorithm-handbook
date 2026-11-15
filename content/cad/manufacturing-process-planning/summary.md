## What to remember

- [Setup planning](/setup-planning/) is a [set cover](/set-cover/) of the features by tool directions, NP-complete when the directions are part of the input. With six axis directions, all $2^6$ subsets can be tried. Tight tolerance pairs must share a setup.
- [Operation sequencing](/operation-sequencing/) orders operations under precedence to save tool and setup changes. It is an asymmetric TSP with precedence, so NP-hard. Dynamic programming over the downsets of the precedence takes $O((n+1)^w n^2)$ time for width $w$.
- A locator layout fixes the part exactly when its locator matrix $J$, with rows $(n_i, p_i \times n_i)$, has rank 6 ([kinematic fixture analysis](/kinematic-fixture-analysis/)). For the [3-2-1 layout](/three-two-one-locating-principle/), $|\det J| = 2A\,|a_2 - a_1|$ for primary triangle area $A$, and an error $\Delta$ of a secondary locator turns the part by $\Delta/(a_2 - a_1)$. Six frictionless contacts never hold a part. [Form closure](/fixture-planning/) needs at least 4 contacts in the plane and 7 in space.
- [Taylor's law](/taylor-tool-life-equation/) $V T^n = C$ is a fit. The tool life of least cost is $T = (1/n - 1)(t_c + C_t/C_o)$, and that of least time is $(1/n - 1)\,t_c$. One pass with power-law models is a [geometric program](/geometric-programming/).
- The [bend allowance](/bend-allowance/) is $\theta (R + K t)$, with the bend angle $\theta$ (not the included angle) and a measured [K-factor](/k-factor/) $K$ of 0.33 to 0.5. The blank is $a + b + \mathrm{BA} = A + B - \mathrm{BD}$.
- In [bend sequencing](/bend-sequence-planning/) the shape depends only on the set of done bends: $2^n$ states, not $n!$ orders. [A* with a consistent heuristic](/a-star-bend-sequencing/) returns a cheapest plan for its costs in $O(2^n n k^2 (n + \log k))$ time.
- [Springback](/springback-compensation/) in the elastic-perfectly plastic model gives $\rho_i/\rho_f = 4x^3 - 3x + 1$ for $x = \rho_i Y/(E t) \le 1/2$. Displacement adjustment converges at the rate $8x_*^3$ in this model.
- [Chvorinov's rule](/chvorinov-rule/) $t = B (V/A)^n$ with $n$ about 2 ranks sections by their modulus. The [modulus method](/riser-design-modulus-method/) gives a riser $1.2$ times the modulus it feeds, a margin from practice. Distance maxima ([hot spots](/casting-hot-spot-detection/)) are a proxy for the modulus.
- A [parting line](/parting-line-generation/) is the boundary between faces with $n \cdot d > 0$ and $n \cdot d < 0$, traced in $O(N)$ time, one loop on a convex part. [Undercuts](/undercut-detection/) are the points blocked along both $+d$ and $-d$.

| Method | Model | Time | Guarantee |
|---|---|---|---|
| Setup planning, 6 directions | set cover with tolerance groups | $O(2^k (km + \lvert T\rvert))$ | fewest setups |
| Operation sequencing by downsets | precedence of width $w$ | $O((n+1)^w n^2)$ | optimal order |
| Locator rank test | frictionless points, first order | $O(1)$ | exact for the model |
| Brost-Goldberg fixtures | polygon, lattice, 3 pins and a clamp | $O(n^4 d^6)$ | lists all fixtures of the class |
| Flat pattern by tree traversal | bend allowance, chosen cuts | $O(n)$, overlap test $O(n \log n)$ | exact for the allowance |
| A* bend sequencing | toy collision rule, flip and tool costs | $O(2^n n k^2 (n + \log k))$ | cheapest plan |
| Cutting sequence, fixed order | GTSP with precedence | $O(m k^2)$ | best pierce points for the order |
| Hot spots by distance transform | grid, squared distances | $O(3^k N)$ | exact distances; proxy for freezing |
| Parting line | polyhedron, integer coordinates | $O(N)$ | exact face signs; one loop if convex |
| Undercuts, one direction | polyhedron | $O(n \log n)$ | exact decision |

: For setups, $k$ counts directions, $m$ features and $T$ tolerance pairs. For fixtures, $n$ counts edges and $d$ the diameter in lattice units. For bends, $n$ counts bends and $k$ tools; for cutting, $m$ counts contours and $k$ pierce points each; for hot spots, $N$ counts cells.

## Choosing a method

For a machined part, cover the features with as few setups as tolerances allow, and order each setup by dynamic programming when the precedence is narrow, or by a metaheuristic when it is not. Check a locator layout by its rank, then the clamps for form closure. Fit Taylor's law to your own tools, then check power, force and finish limits.

For sheet metal, measure the K-factor with a test bend, unfold along a spanning tree and test the blank for overlap, and plan bends with A* while $2^n$ states fit in memory. Compensate springback by iteration on a simulation.

For molds, fix the parting direction, then check draft, undercuts and the parting line, all exact for a polyhedron. Gates and cooling channels need a simulation. For castings, size risers by the modulus method and compare with the hot spots; both rest on fitted laws.

## What to remember

- A collision at one contact with normal speed $v^- < 0$ ends with $v^+ = -e v^-$ under Newton's [coefficient of restitution](/coefficient-of-restitution/). The [collision impulse](/collision-impulse/) is $j = -(1 + e)v^-/k$, where $k = 1/m + $ the rotation terms; it keeps momentum and loses the energy $(1 - e^2)(v^-)^2/(2k)$. Without friction, Newton's, Poisson's and Stronge's laws agree.
- The [Coulomb friction law](/coulomb-friction-law/) bounds the tangential force by $|f_t| \le \mu f_n$. A box at rest on a slope of angle $\alpha$ slides exactly when $\tan\alpha > \mu$.
- [Sweep and prune](/sweep-and-prune/) updates sorted interval ends in $O(n + r)$ time for $r$ swaps; $r$ is small under coherence but can be $\Theta(n^2)$. Bounding volume trees prune with a conservative test: an [OBB tree](/obb-tree/) uses 15 axes in 3D, a [k-DOP tree](/k-dop-tree/) $k/2$ intervals and a [sphere tree](/sphere-tree/) one distance. Their worst case is $O(nm)$ tests, and their speed in practice is measured.
- For convex polyhedra, [Lin-Canny](/lin-canny-closest-features/) and [V-Clip](/v-clip/) return the exact closest features after at most $O(nm)$ moves, in $O(s(n + m))$ time for $s$ moves. Coherence makes $s$ small; that is observed, not proved. V-Clip needs no tolerances and also stops on penetration; Lin-Canny can cycle in 3D.
- The [expanding polytope algorithm](/expanding-polytope-algorithm/) brackets the [penetration depth](/penetration-depth/) as $r \le d \le r + \varepsilon$. On polytopes with $\varepsilon = 0$ it is exact after at most $nm$ rounds.
- [Conservative advancement](/conservative-advancement/) steps by $d/\mu$, where $\mu$ bounds the speed of approach. It never passes the first contact and needs at most $\lceil TL/\varepsilon \rceil + 1$ steps. The [elementary tests](/elementary-ccd-tests/) find coplanarity times as roots of a cubic; they are exact in exact arithmetic and can miss contacts in floating point.
- [Projected Gauss-Seidel](/projected-gauss-seidel/) is coordinate descent on a convex quadratic. It converges for a positive definite matrix with fixed bounds; with friction bounds $\pm\mu\lambda_n$, or a singular matrix, convergence is not proved. Its sweeps on a stack grow with the height, which is measured.
- [Baumgarte stabilization](/baumgarte-stabilization/) asks for $J v = -(\beta/\Delta t) C$. In the linear model the error falls as $(1 - \beta)^k$, converges for $0 < \beta < 2$ and is monotone for $\beta \le 1$. It can add energy. [Shock propagation](/shock-propagation/) is a heuristic that does not keep momentum; the [Baraff algorithm](/baraff-contact-force-algorithm/) pivots to exact frictionless forces.

| Method | Task | Time | Status |
|---|---|---|---|
| Sweep and prune | box pairs | $O(n + r)$ per update | exact for boxes |
| OBB tree | triangle pairs | $O(n \log^2 n)$ build, $O(nm)$ query | exact; pruning measured |
| k-DOP tree | triangle pairs | $O(kn\log n + n\log^2 n)$ build | conservative test |
| Sphere tree | triangle pairs | $O(2^L)$ interrupted query | conservative, interruptible |
| Lin-Canny, V-Clip | closest features | $O(s(n + m))$, $s = O(nm)$ | exact for convex polyhedra |
| Expanding polytope | penetration depth | $O(k(k + n + m))$ | $r \le d \le r + \varepsilon$ |
| Conservative advancement | first contact time | $O(sD)$, $s \le \lceil TL/\varepsilon\rceil + 1$ | conservative |
| Elementary tests | vertex-face, edge-edge | $O(1)$ roots | exact arithmetic only |
| Collision impulse | one contact | $O(1)$ | exact; order matters for many |
| Projected Gauss-Seidel | all contacts | $O(Kz)$ for $K$ sweeps | iterative; proved only for SPD |
| Shock propagation | stacks | $O(n + e)$ levels plus sweeps | heuristic |
| Baraff pivoting | all contacts | $O(n^2)$ to $O(n^3)$ per pivot | exact, no friction |

: The main methods. $n$ and $m$ are the sizes of two bodies or the number of contacts, $r$ the swaps, $L$ the tree depth or speed bound, $k$ the polytope size, $D$ one distance query, $z$ the nonzeros of the contact matrix and $e$ the edges of the contact graph.

## Choosing a method

For the broad phase, sweep and prune is the default when bodies move a little per frame. Inside a pair of meshes, use an OBB tree for parts in close contact, a k-DOP tree for one moving body in a large static scene, and a sphere tree when a time budget must cut the query short. Split concave bodies into convex pieces once, offline.

For convex pairs, use V-Clip or [GJK](/gjk-algorithm/) for the distance, and EPA after GJK for the depth. Add continuous detection for small or fast bodies: conservative advancement for convex bodies, the elementary tests for triangle meshes.

For response, the collision impulse handles isolated hits. A game engine solves all contacts with projected Gauss-Seidel, warm started, with Baumgarte or split impulses for drift. Add shock propagation when tall stacks must settle in few sweeps. Use Baraff's pivoting when exact frictionless forces matter more than speed, and penalty contact only with a step that the spring's stiffness allows.

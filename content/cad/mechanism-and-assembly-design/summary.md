## What to remember

- A four-bar with shortest link $s$, longest $l$ and the others $p, q$ has a link that turns fully exactly when $s + l \le p + q$, the [Grashof condition](/grashof-condition/). Grounding the shortest link then gives a double crank, a neighbor a crank-rocker, and the opposite link a double rocker. Otherwise every inversion is a triple rocker.
- [Vector loop closure](/vector-loop-closure/) turns the position problem into a quadratic in $\tan(\theta/2)$. Its two roots are the two circuits. The $n(n-1)/2$ [instant centers](/instant-center-of-velocity/) of $n$ links lie three on a line by the [Aronhold-Kennedy theorem](/aronhold-kennedy-theorem/), so a speed ratio is a ratio of distances.
- A [coupler curve](/coupler-curve/) has degree 6 and is traced by three different four-bars, the [Roberts-Chebyshev cognates](/roberts-chebyshev-theorem/). The [Peaucellier-Lipkin linkage](/peaucellier-lipkin-linkage/) draws an exact line, and by [Kempe's theorem](/kempe-universality-theorem/) linkages draw any bounded piece of a plane algebraic curve.
- Precision-point synthesis is exact at the points and only there. [Freudenstein's equation](/freudenstein-equation/) $K_1\cos\psi - K_2\cos\varphi + K_3 = \cos(\varphi - \psi)$ is linear in $K$, so three points give a $3 \times 3$ system. [Burmester theory](/burmester-theory/) gives at most four dyads, so at most six four-bars, for five positions. [Optimization](/optimization-based-linkage-synthesis/) over many points finds local optima.
- The limits of $40°$ to $140°$ on the [transmission angle](/transmission-angle/), $30°$ on the [cam pressure angle](/cam-pressure-angle/) of a translating follower, and $1.2$ on the [contact ratio](/gear-contact-ratio/) are rules of practice, not theorems.
- A cam law with coefficients $C_v$ and $C_a$ gives the peaks $v = C_v L\omega/\beta$ and $a = C_a L\omega^2/\beta^2$ for a rise $L$ over the cam angle $\beta$.
- An [involute](/involute-gear-tooth/) pair keeps the ratio $r_{b1}/r_{b2}$ at every center distance. Its contact ratio is the length of action over the base pitch. A rack with addendum $km$ undercuts a gear unless $z \ge 2k/\sin^2\varphi$, which is 18 teeth for full depth at $20°$. The [Willis formula](/willis-formula/) $\omega_L - \omega_A = e(\omega_F - \omega_A)$ gives every planetary speed.
- The [AND/OR graph](/and-or-graph-of-assembly-plans/) has at most one node per connected set of parts, while the number of plans can grow like $(2n-3)!!$. For one translation, [blocking graphs](/non-directional-blocking-graph/) find a removable subassembly in polynomial time. With richer motions, or with both sides required to be connected, [partitioning](/assembly-partitioning/) is NP-complete in the plane. Every planner is exact only for its motion model.

| Method | Model | Cost | Guarantee |
|---|---|---|---|
| Grashof test | four lengths | $O(1)$ | exact: which links turn fully |
| Loop closure, half-angle form | four-bar, real RAM | $O(1)$ per position | exact, both circuits |
| Instant centers | $n$ planar links | $n(n-1)/2$ centers | exact at one instant |
| Freudenstein, three points | function generation | one $3 \times 3$ system | exact at the points only |
| Burmester | five positions | cubic curves, at most 4 dyads | exact; some designs unusable |
| Nine-point homotopy | nine path points | thousands of paths | numerical; 1442 curves |
| Optimization synthesis | many points or a curve | iterations times points | local optimum |
| Cam profile by envelope | sampled follower law | $\Theta(m + N\log m)$ | exact at the samples |
| Willis formula | chain of $n$ meshes | $O(n)$ | exact |
| AND/OR graph | two-handed, monotone, connected | $O(C n^2)$ | all plans of the model |
| De Fazio-Whitney | linear, monotone | $O(N m l^2)$ | all linear plans of the model |
| Blocking graphs | one translation, boxes | $O(n^2)$ per split | exact for the model |

: The main methods. $m$ follower samples and $N$ profile points; $n$ parts, $l$ liaisons, $m$ directions, $N$ connected sets and $C$ candidate splits for assembly.

## Choosing a method

For analysis, test Grashof first, solve the loop equation in half-angle form and keep track of the circuit. Use instant centers for a velocity at one position. Check the transmission angle over the whole cycle.

For synthesis, use Freudenstein's equation with [Chebyshev spacing](/chebyshev-spacing/) for three-point function generation, the [standard-form dyad](/standard-form-dyad-synthesis/) for up to three positions, and Burmester theory for four or five. Use optimization for a whole curve, started from many points. Check every result for the circuit, the order of positions and the transmission angle, because the equations do not.

For cams, choose a law with finite jerk at high speed, size the base circle by the pressure angle and compute the profile as an envelope. For gears, check undercutting and interference before the contact ratio,. For assembly, build the [liaison graph](/liaison-graph/), test splits with blocking graphs, and store the plans in an AND/OR graph. Use the [De Fazio-Whitney method](/de-fazio-whitney-precedence-method/) when only linear plans matter, and a [motion planner](/motion-planning/) only for steps that translations cannot do.

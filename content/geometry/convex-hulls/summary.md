## What to remember

- The **convex hull** of a finite set $S$ is the smallest convex set that contains it. In the plane it is a convex polygon whose corners, the [extreme points](/extreme-point/), are points of $S$. The output of the [convex hull problem](/convex-hull-problem/) is these $h$ corners in counterclockwise order; points in the middle of a hull edge are not corners.
- Every planar algorithm rests on the [orientation test](/orientation-test/) $D(p, q, r) = (q_x - p_x)(r_y - p_y) - (q_y - p_y)(r_x - p_x)$: positive for a left turn, negative for a right turn, zero on a line. With integer coordinates it is exact; its sign is the only thing the algorithms need, so compute it without rounding.
- **Sort, then scan.** [Andrew's monotone chain](/andrew-monotone-chain/) sorts by $x$ and builds the [lower and upper hulls](/upper-and-lower-hull/) with a stack. The scan pushes each point once and pops it at most once, so it is $\Theta(n)$ after the sort and $\Theta(n \log n)$ in all. The [Graham scan](/graham-scan/) does the same after an angular sort.
- **The hull is as hard as sorting.** Lift each number $x$ to the point $(x, x^2)$; the ordered hull lists the numbers in sorted order. So $\Omega(n \log n)$ holds in the [algebraic decision tree](/algebraic-decision-tree/) model, even for deciding which points are extreme.
- **Output-sensitive bounds.** The [Jarvis march](/jarvis-march/) takes $\Theta(nh)$ time. [Kirkpatrick–Seidel](/kirkpatrick-seidel/) and [Chan's algorithm](/chan-algorithm/) take $O(n \log h)$, and $\Omega(n \log h)$ is a [lower bound](/convex-hull-output-sensitive-lower-bound/), so $\Theta(n(1 + \log h))$ is the right answer.
- **A walk around the hull answers many questions.** [Rotating calipers](/rotating-calipers/) visits the at most $\lfloor 3h/2 \rfloor$ antipodal pairs of a convex polygon in $\Theta(h)$ time, which gives the diameter, the width and the smallest enclosing rectangle.
- **Constants that depend only on the dimension.** In $\mathbb{R}^d$: a point of a hull is a convex combination of $d + 1$ points ([Carathéodory](/caratheodory-theorem/)); any $d + 2$ points split into two parts whose hulls meet ([Radon](/radon-theorem/)); if every $d + 1$ of a family of convex sets meet, all of them do ([Helly](/helly-theorem/)).
- **Higher dimensions.** A [polytope](/convex-polytope/) has a description by vertices and one by half-spaces ([Minkowski–Weyl](/minkowski-weyl-theorem/)). In $\mathbb{R}^3$ a hull of $n$ points has at most $2n - 4$ facets and can be found in $O(n \log n)$ time; in $\mathbb{R}^d$ the output alone can have $\Theta(n^{\lfloor d/2 \rfloor})$ facets, and the [beneath-beyond method](/beneath-beyond/) with a random order runs in $O(n \log n + n^{\lfloor d/2 \rfloor})$ expected time.

## The planar algorithms side by side

| Algorithm | Year | Time | Input | Idea |
|---|---|---|---|---|
| [Graham scan](/graham-scan/) | 1972 | $\Theta(n \log n)$ | points | angular sort, stack scan |
| [Jarvis march](/jarvis-march/) | 1973 | $\Theta(nh)$ | points | wrap one edge at a time |
| [Divide and conquer](/divide-and-conquer-convex-hull/) | 1977 | $\Theta(n \log n)$ | points | merge two hulls by bridges |
| [Quickhull](/quickhull/) | 1977 | $O(nh)$, $\Theta(n^2)$ worst | points | farthest point, recurse on two sides |
| [Andrew's monotone chain](/andrew-monotone-chain/) | 1979 | $\Theta(n \log n)$ | points | sort by $x$, two stack scans |
| [Kirkpatrick–Seidel](/kirkpatrick-seidel/) | 1986 | $O(n \log h)$ | points | find the bridge first, then recurse |
| [Melkman's algorithm](/melkman-algorithm/) | 1987 | $\Theta(n)$ | simple polyline | deque, one vertex at a time |
| [Chan's algorithm](/chan-algorithm/) | 1996 | $O(n \log h)$ | points | hulls of groups, wrap with guessed $h$ |

: Planar convex hull algorithms; $n$ is the number of input points and $h$ the number of hull vertices. All of them use only orientation tests and comparisons of coordinates, so all are exact on integer input.

## Choosing a method

- For a hull in the plane, write Andrew's monotone chain. It is short, it sorts with the library sort, and its pop test with $\le 0$ drops collinear points without any special case.
- When the hull is known to be tiny, say a handful of corners, the Jarvis march is simplest; Chan's algorithm keeps $O(n \log h)$ without knowing $h$ in advance.
- When the points arrive as the vertices of a simple polygon or polyline, use Melkman's algorithm and skip the sort.
- When points are inserted and deleted, use a [dynamic convex hull](/dynamic-convex-hull/); for repeated peeling, [convex layers](/convex-layers/).
- In three dimensions, or when you also need a Delaunay triangulation, use a randomized incremental method such as beneath-beyond, or an established library built on quickhull.
- With floating-point input, do not add a tolerance to the orientation test; use exact or adaptive arithmetic for its sign.

## What to remember

- **The answer is a set.** [Pareto dominance](/pareto-dominance/) is a strict partial order, not a total one, so the solution of a problem with $p \ge 2$ objectives is the [Pareto front](/pareto-front/) $Y_N$. The front can be huge: $2k$ arcs, edges or items give $2^k$ nondominated points for [paths](/multi-objective-shortest-path/), [spanning trees](/multi-objective-minimum-spanning-tree/) and [knapsacks](/multi-objective-knapsack/).
- **Random fronts are small.** For $N$ random vectors with independent continuous coordinates, the expected front size is $H_N$ for $p = 2$ and $\Theta(\log^{p-1} N)$ in general.
- **The [ideal point](/ideal-point/) is easy; the [nadir point](/nadir-point/) is not.** The ideal point costs $p$ solves. For $p = 2$ the nadir point comes from the two lexicographic minimizers, but for $p \ge 3$ the payoff table can miss it in either direction.
- **Weighted sums find only supported points.** A [weighted sum](/weighted-sum-method/) with positive weights gives a properly Pareto optimal point, but never one above the convex hull of the front. The [epsilon-constraint](/epsilon-constraint-method/) and [Tchebycheff](/weighted-tchebycheff-method/) methods find every Pareto optimal point but may also return weak optima. For [linear programs](/multi-objective-linear-programming/) every nondominated point is supported.
- **The front of $n$ vectors costs about a sort.** [Kung's algorithm](/kung-algorithm/) takes $O(n \log n)$ time for $p \le 3$ and $O(n \log^{p-2} n)$ for $p \ge 4$, against a lower bound of $\lceil \log_2 n! \rceil$ comparisons. The [fast non-dominated sort](/non-dominated-sorting/) into all layers takes $\Theta(p N^2)$ time and $\Theta(N^2)$ space.
- **An evolutionary method is a rank, a density and an archive.** [NSGA-II](/nsga-ii/) ranks by fronts, breaks ties by [crowding distance](/crowding-distance/) and keeps the best fronts, in $O(p N^2)$ time per generation plus the evaluations.
- **Only some indicators respect dominance.** The [hypervolume](/hypervolume-indicator/) is strictly Pareto compliant, but it is #P-hard to compute when $p$ is part of the input. The binary [epsilon indicator](/epsilon-indicator/) decides weak dominance between two sets exactly. [IGD](/igd-indicator/) and the [spread](/spread-indicator/) are not Pareto compliant.
- **A short list always exists.** For positive objective values of at most $m$ bits, an [approximate Pareto set](/approximate-pareto-set/) within a factor $1 + \varepsilon$ in each objective has $O((m / \varepsilon)^{p-1})$ points (Papadimitriou and Yannakakis).

## The main methods side by side

| Method | Finds | Cost |
|---|---|---|
| [All pairs](/pareto-front-computation/) | front of $n$ vectors | $O(p n^2)$ |
| [Kung's algorithm](/kung-algorithm/) | front of $n$ vectors | $O(n \log n)$ for $p \le 3$, $O(n \log^{p-2} n)$ for $p \ge 4$ |
| [Fast non-dominated sort](/non-dominated-sorting/) | all fronts of $N$ vectors | $\Theta(p N^2)$ time, $\Theta(N^2)$ space |
| [Crowding distance](/crowding-distance/) | density in a front of $N$ | $O(p N \log N)$ |
| [NSGA-II](/nsga-ii/), one generation | next population of $N$ | $O(p N^2)$ plus $N$ evaluations |
| [Weighted sum](/weighted-sum-method/), dichotomic, $p = 2$ | the $s$ supported extreme points | $2s - 3$ weighted and 2 lexicographic solves |
| [Epsilon constraint](/epsilon-constraint-method/), $p = 2$, integer | the whole front | $\lvert Y_N \rvert + 1$ lexicographic solves |
| [Normal-boundary intersection](/normal-boundary-intersection/) | $M = \binom{H + p - 1}{p - 1}$ spread points | $O((M + p) L)$ |
| [Benson's algorithm](/benson-algorithm/) | extreme points of a linear front | $p + N$ linear programs |
| [Hypervolume](/hypervolume-computation/) | volume of $N$ points | $O(N \log N)$ for $p \le 3$, $O(N^{p/3} \operatorname{polylog} N)$ in general |
| [IGD](/igd-indicator/) | distance of $A$ to a reference set $R$ | $O(p \lvert A \rvert \lvert R \rvert)$ |
| [Box archive](/approximate-pareto-set/) | an $\varepsilon$-Pareto set of a stream | $O(p \lvert A \rvert)$ per point, $\lvert A \rvert \le K^{p-1}$ |

: The main methods of the chapter. $L$ is the cost of one scalar subproblem, and $H$ the number of divisions of the grid of normal-boundary intersection. For Benson's algorithm $N$ counts the vertices of all outer approximations; $K$ is the number of boxes per objective.

## Choosing a method

- When the decision maker can state weights or a target before the run, solve one scalarized problem: a weighted sum if the problem is convex, an [achievement function](/achievement-scalarizing-function/) or a Tchebycheff problem if not.
- For the whole front of a two-objective problem with cheap scalar solves, walk it with the epsilon-constraint method, or find the supported points first and the others in a second phase.
- For a linear program with a few objectives, use Benson's algorithm.
- For a list of vectors, use a sort and scan for $p = 2$ and Kung's algorithm for larger $p$; for a stream, keep an archive.
- For a black-box problem with two or three objectives, start with NSGA-II or [SPEA2](/spea2/). With many objectives, use [NSGA-III](/nsga-iii/) or [MOEA/D](/moea-d/).
- To compare two outputs, report the hypervolume, with its reference point, and the epsilon indicator.

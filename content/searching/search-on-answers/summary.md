## What to remember

- A search on the answer needs a **monotone predicate**: a test that is false below a threshold and true from it on. Check monotonicity before anything else. If a larger answer can be feasible while a smaller one is not and then feasible again, binary search returns a wrong value without any sign of error.
- **The test does the work.** The binary search around it is always the same and costs $\lceil \lg(U - L + 1) \rceil$ tests for integer answers in $[L, U]$. Most of the effort in a problem goes into a fast test and a proof that it is correct, usually a greedy pass with an exchange argument.
- **On real numbers, fix the number of steps.** Stopping when $hi - lo < \varepsilon$ can loop for ever once the two ends are adjacent doubles. A fixed count of $\lceil \lg((b - a)/\varepsilon) \rceil$ halvings always ends.
- **Counting replaces enumerating.** To find the $k$-th smallest of a large implicit set, such as pair distances or table entries, search on the value and count the members at most that value. The count is often an $O(n)$ pass with two pointers.
- **Unimodal search compares two points.** Ternary search keeps two thirds of the interval per step at two evaluations. Golden-section and Fibonacci search place the points so that one of them is reused, which costs one evaluation per step. Ternary search needs about 2.4 times as many evaluations.
- **A ratio becomes a sum.** The minimum of $N(x)/D(x)$ is at most $\lambda$ exactly when $\min_x (N(x) - \lambda D(x)) \le 0$. Binary search on $\lambda$ works, and Dinkelbach's algorithm usually needs far fewer rounds.
- **Many searches can share one sweep.** When each test means replaying updates, parallel binary search moves all queries one step in a single pass and needs only $\lceil \lg(T + 1) \rceil$ passes.

## The methods side by side

| Method | Test or step | Number of tests or steps |
|---|---|---|
| [Binary search on the answer](/binary-search-on-answer/) | monotone test on integers | $\lceil \lg(U - L + 1) \rceil$ |
| [Binary search on real numbers](/binary-search-on-real-numbers/) | monotone test on reals | $\lceil \lg((b - a)/\varepsilon) \rceil$ |
| [Ternary search](/ternary-search/) | two evaluations | about $3.42 \lg r$ evaluations |
| [Fibonacci search](/fibonacci-search-unimodal/) | one new evaluation | about $1.44 \lg n$ evaluations, optimal |
| [Golden-section search](/golden-section-search/) | one new evaluation | $1 + \lceil \log_\varphi r \rceil$ evaluations |
| [Dinkelbach's algorithm](/dinkelbach-algorithm/) | one parametric problem | at most $4 \lg U + 3$ rounds, often far fewer |
| [Parallel binary search](/parallel-binary-search/) | one sweep of all updates | $\lceil \lg(T + 1) \rceil$ sweeps |
| [Parametric search](/parametric-search/) | simulated parallel algorithm | $O(S \log P)$ decision calls |

: Searches over values. $U - L + 1$ is the number of candidate answers, $r$ is the factor by which a real interval must shrink, $n$ the number of integer points, and $T$ the number of updates. Parametric search simulates a parallel algorithm with $P$ processors and $S$ steps, for $O(PS + S\,T_C \log P)$ time with a decision procedure of time $T_C$.

## Choosing a method

- When a problem asks for the least or greatest value of something and checking a given value is easy, try a search on the answer first. Write the test, prove it monotone, and then add the binary search.
- Search over integers whenever the answer is an integer, even if it is a length or a time. Use a real search only when the answer is truly continuous, and then use a fixed number of steps.
- For the top of a unimodal function on integers, ternary search is enough in most programs. When each evaluation is costly, as in a simulation, use golden-section search, or Fibonacci search when the number of points is known.
- If a function is only weakly unimodal, with flat stretches, none of these methods is safe; a flat stretch hides which side the peak is on.
- For a ratio, start with a binary search on $\lambda$. Switch to Dinkelbach's algorithm when each parametric problem is expensive.
- Reach for parallel binary search when there are many offline queries over the same sequence of updates, and for parametric search only when no simpler method gives an exact answer.

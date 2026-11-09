## What to remember

- **Two kinds.** A Las Vegas algorithm is always right and has a random running time. A Monte Carlo algorithm stops within a fixed bound and is wrong with probability at most $\delta$. Both bounds are over the coins and must hold for every input; a program with a fixed seed is deterministic.
- **Constants in the error do not matter.** $k$ independent runs of a one-sided algorithm with error $\delta$ have error $\delta^k$. A majority of $k$ runs of a two-sided algorithm with error $1/2 - \gamma$ is wrong with probability at most $e^{-2\gamma^2 k}$. A Las Vegas algorithm with expected time $t$, stopped after $2t$ steps, fails with probability at most $1/2$, and restarts give it an exponential tail.
- **Expected running time** is the largest, over inputs of size $n$, of the mean time over the coins. It is not the average-case time of a deterministic algorithm on random inputs, and alone it gives only Markov's tail.
- **Randomized quickselect.** One random pivot, a three-way partition, and only the part that holds rank $k$ is kept. At most $4n$ comparisons in expectation on every input, with an exact mean near $3.386n$ at the median; the worst case $n(n + 1)/2$ depends on the coins, not on the input.
- **Backwards analysis.** In a random order, given the set of the first $i$ objects, the $i$-th object is uniform in that set. If at most $d$ of them define the structure, an expensive step has probability at most $d/i$. Prefix minima change $H_n$ times in expectation.
- **Randomized incremental construction.** Shuffle, insert, repair. The expected number of parts created at step $i$ is at most $b f(i)/i$, where $b$ objects define a part and $f(i)$ bounds the size of the structure; with $f(i) = O(i)$ it is $O(1)$. Conflict lists or a history structure find the parts to repair.
- **Probabilistic method.** If the bad events have probabilities that sum to less than 1, a good object exists. If a sum of simple parts has mean $\mu$, some object reaches $\mu$.

## The bounds side by side

| method | kind | guarantee, for every input | worst case or repetition |
|---|---|---|---|
| [Randomized quicksort](/randomized-quicksort/) | Las Vegas | $2(n + 1)H_n - 4n$ comparisons expected: 24.44 for $n = 10$, 647.85 for $n = 100$ | $n(n - 1)/2$: 45 and 4,950 |
| [Randomized quickselect](/randomized-quickselect/) | Las Vegas | at most $4n$ comparisons expected; mean 14.14 for the minimum and 19.27 for the median at $n = 10$ | $n(n + 1)/2$ |
| Freivalds' check of $AB = C$ | Monte Carlo, one-sided | $O(n^2)$ time per trial, error at most $1/2$ per trial | error $2^{-20}$ after 20 trials |
| [Miller-Rabin](/miller-rabin/) | Monte Carlo, one-sided | error at most $1/4$ per random base | about $9.09 \times 10^{-13}$ after 20 bases |
| [Karger's min cut](/karger-min-cut/) | Monte Carlo | a given minimum cut with probability at least $2/(n(n - 1))$ | 311 runs for error below $10^{-3}$ at $n = 10$ |
| Prefix minima in random order | backwards analysis | $H_n$ updates expected: 2.93 for $n = 10$ | $n$ updates |
| Seidel's linear programming | incremental, random order | $O(d!\,n)$ expected | — |
| Delaunay triangulation | incremental, random order | $O(n \log n)$ expected, at most $9n + 1$ triangles created in expectation | $\Theta(n^2)$ for some fixed orders |
| [Trapezoidal map](/trapezoidal-map/) | incremental, random order | $O(n \log n)$ expected build, $O(n)$ expected size, $O(\log n)$ expected query | — |

: Guarantees are over the coins or the random order, for one fixed input.

## Choosing a method

- If a wrong answer is never acceptable but the answer can be checked, use a Las Vegas algorithm, or wrap a Monte Carlo one in a loop that repeats until the check accepts. The number of rounds is geometric, with mean $1/p$ for success probability $p$.
- If a small error is acceptable and a fixed time limit matters, use a Monte Carlo algorithm and pick the number of repetitions from the error you need.
- If an opponent may see or predict the random bits, the bounds no longer hold. Use a deterministic method with a worst-case bound, such as [median of medians](/median-of-medians/) or [introselect](/introselect/) for selection.
- If you build a structure by insertion, shuffle first and analyse each step backwards.
- If you only need to know that an object exists, try the union bound first, then the expectation of a sum. If the bad events are many but each depends on few others, the [Lovász local lemma](/lovasz-local-lemma/) may still apply.

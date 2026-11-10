## What to remember

- A [Las Vegas algorithm](/las-vegas-algorithm/) is always right and bounds its expected running time on every input. A [Monte Carlo algorithm](/monte-carlo-algorithm/) bounds its running time on every input and errs with probability at most $\delta$ on every input. The probability is over the coins, not over the input.
- With [one-sided error](/one-sided-error/) one answer is a proof: "composite" from Miller-Rabin, "not equal" from Freivalds. The OR of $k$ independent runs errs with probability $\delta^k$, so [amplification](/error-amplification/) needs $\lceil \ln(1/\delta)/\ln(1/\delta_0) \rceil$ runs.
- With [two-sided error](/two-sided-error/) the success probability must be at least $1/2 + \gamma$ for a fixed gap $\gamma > 0$. A majority of $k$ runs errs with probability at most $e^{-2\gamma^2 k}$, so $k = O(\log(1/\delta)/\gamma^2)$. Without a gap, as in PP, repetition does not help.
- [Conversion](/las-vegas-to-monte-carlo-conversion/) works both ways. Cut a Las Vegas algorithm off at $c$ times its expected time $t$; by Markov's inequality a run fails with probability at most $1/c$, and the total cost is about $(c/\ln c)\, t \ln(1/\delta)$. A Monte Carlo algorithm with a verifier, repeated until the verifier accepts, is Las Vegas with expected time $(t_M + t_V)/p$.
- The [Miller-Rabin test](/miller-rabin-primality-test/) errs with probability at most $4^{-k}$ after $k$ rounds, because an odd composite $n > 9$ has at most $\varphi(n)/4$ strong liars. The [Solovay-Strassen test](/solovay-strassen-primality-test/) has at most $\varphi(n)/2$ liars and errs with probability at most $2^{-k}$. Every strong liar is an Euler liar.
- The [Schwartz-Zippel lemma](/schwartz-zippel-lemma/): a nonzero polynomial of total degree $d$ over an integral domain vanishes at a uniform point of $S^n$ with probability at most $d/|S|$. With $|S| \ge 2d$ this puts [polynomial identity testing](/polynomial-identity-testing/) in co-RP.
- [Freivalds' algorithm](/freivalds-algorithm/) checks $AB = C$ in $\Theta(kn^2)$ time with error at most $2^{-k}$. Over a ring with zero divisors, such as the integers modulo $2^{64}$, the bound fails.
- Random pivots solve [nuts and bolts](/nuts-and-bolts/) with $4(n+1)H_n - 7n \approx 2.77\, n \log_2 n$ expected comparisons, within a constant factor of the lower bound $\log_3(n!)$. The [contraction argument](/minimum-cut-count-bound/) shows that a graph has at most $\binom{n}{2}$ minimum cuts, and the cycle $C_n$ has exactly that many.

## The examples side by side

| Algorithm | Time | Error | Kind |
|---|---|---|---|
| [Freivalds](/freivalds-algorithm/) | $\Theta(kn^2)$ | $\le 2^{-k}$, "not equal" always right | Monte Carlo, one-sided |
| [Miller-Rabin](/miller-rabin-primality-test/) | $O(k \log^3 n)$ | $\le 4^{-k}$, "composite" always right | Monte Carlo, one-sided |
| [Solovay-Strassen](/solovay-strassen-primality-test/) | $O(k \log^3 n)$ | $\le 2^{-k}$, "composite" always right | Monte Carlo, one-sided |
| [Random evaluation for PIT](/polynomial-identity-testing/) | one evaluation of the circuit per round | $\le (d/\lvert S \rvert)^k$, "nonzero" always right | Monte Carlo, one-sided |
| [Karger contraction](/karger-min-cut/) | $O(m\, \alpha(n))$ per run | a run returns a minimum cut with probability $\ge 1/\binom{n}{2}$ | Monte Carlo |
| [Nuts and bolts](/nuts-and-bolts/) | expected $4(n+1)H_n - 7n$ comparisons, worst case $n^2$ | none | Las Vegas |
| [Randomized quicksort](/randomized-quicksort/) | expected $2(n+1)H_n - 4n$ comparisons | none | Las Vegas |

: The algorithms of the chapter, with $k$ independent rounds. For the Monte Carlo ones the error bound holds on every input; for the Las Vegas ones the expectation is over the coins, on the worst input.

## Choosing a method

To decide a question with a short proof of one answer, look for a one-sided test: a random object that is a witness with probability at least $1/2$ whenever the answer is "yes". Then repeat it. Twenty rounds of a test with error $1/2$ reach about $10^{-6}$, and ten rounds of Miller-Rabin reach the same.

When an equality of two computed objects is in question, write the difference as a polynomial and evaluate it at a random point of a large field. This covers matrix products, polynomial products and string equality, and it costs far less than computing the objects in full.

When the answer must be right and only the time may vary, use a Las Vegas algorithm, and cut it off at a few times its expected time if a hard time limit is needed. If a Monte Carlo algorithm has a fast checker for its output, repeat it until the checker accepts and get a Las Vegas algorithm for free.

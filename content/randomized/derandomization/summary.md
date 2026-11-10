## What to remember

- **Conditional expectations.** If $\mathrm{E}[f(X_1, \ldots, X_n)] \ge \mu$ and the conditional expectation can be computed exactly, fixing each $X_i$ to the value that does not lower it gives a point with $f \ge \mu$. For MAX-CUT this is the greedy rule and gives at least $m/2$ edges in $O(n + m)$ time. Otherwise a [pessimistic estimator](/pessimistic-estimators/), an upper bound with $U_0 < 1$, plays its part.
- **$k$-wise independence is cheap.** A random polynomial of degree $k - 1$ over a field of size $q$ gives $q$ values that are $k$-wise independent from $k \log_2 q$ seed bits. Every $k$-wise independent space of $n$ unbiased bits has at least $\sum_{i \le \lfloor k/2 \rfloor} \binom{n}{i}$ points, and the Hadamard space meets this with $n + 1$ points for $k = 2$.
- **Limited independence gives moment bounds.** Pairwise independence gives Chebyshev's bound, and $k$-wise independence gives the $k$-th moment bound.
- **Small bias.** An $\varepsilon$-biased space makes every nonempty parity have bias at most $\varepsilon$; any $k$ of its bits are within $\frac{\varepsilon}{2}\sqrt{2^k - 1}$ of uniform. The powering generator uses $2\lceil \log_2((n-1)/\varepsilon) \rceil$ seed bits.
- **Pseudorandom generators.** $G$ is a $(t, \varepsilon)$ generator if no test of size $t$ has advantage above $\varepsilon$. A generator with seed $d$ that runs in time $2^{O(d)}$ derandomizes BPP in time $2^{O(d)}$ times the running time. By Yao's theorem a test with advantage $\varepsilon$ on $m$ bits gives a predictor of one bit with advantage $\varepsilon/m$.
- **Hardness versus randomness.** A function in time $2^{O(n)}$ that needs circuits of size $2^{\Omega(n)}$ gives a generator with seed $O(\log m)$, and so BPP $=$ P. For read-once branching programs, Nisan's generator needs a seed of $O(\log^2 n)$ bits and no assumption.
- **Min-entropy.** $H_\infty(X) = -\log_2 \max_x \Pr[X = x]$ is the measure that extraction uses, and $H_\infty \le H_2 \le H$. No deterministic function extracts even one bit from all sources of min-entropy $n - 1$, so extractors take a short seed or two independent sources.
- **Extractors.** A $(k, \varepsilon)$ extractor maps every source of min-entropy $k$ and a uniform seed of $d$ bits to $m$ bits within distance $\varepsilon$ of uniform. The leftover hash lemma gives $m = k - 2\log_2(1/\varepsilon) + 2$, which matches the lower bound on the entropy loss up to a constant, but with a long seed.

## The main tools side by side

| Tool | What it fools or produces | Seed or input | Assumption |
|---|---|---|---|
| [Conditional expectations](/method-of-conditional-expectations/) | one good point of a product space | no seed, exact conditional expectations | none |
| [$k$-wise independent space](/k-wise-independence/) | tests that look at $k$ variables | $O(k \log n)$ | none |
| [Small-bias generator](/small-bias-generator/) | parities, with bias $\varepsilon$ | $O(\log n + \log(1/\varepsilon))$ | none |
| [Expander walk sampler](/expander-walk-sampler/) | one-sided error $2^{-k}$ | $m + O(k)$ | none |
| [Nisan's generator](/nisan-prg/) | read-once branching programs of width $w$ | $O(\log m \cdot \log(mw/\varepsilon))$ | none |
| [Nisan-Wigderson generator](/nisan-wigderson-generator/) | circuits of size $m$ | $O(\log m)$ | a function in E hard for circuits of size $2^{\Omega(n)}$ |
| [Cryptographic generator](/hill-prg-from-one-way-functions/) | all polynomial-time tests | $m^{c}$ for every $c > 0$ | one-way functions |
| [Leftover hash lemma](/leftover-hash-lemma/) | $k - 2\log_2(1/\varepsilon) + 2$ uniform bits | $n + m - 1$ with Toeplitz matrices | none |
| [Trevisan's extractor](/trevisan-extractor/) | $k^{1-\alpha}$ uniform bits | $O(\log^2(n/\varepsilon)/\log k)$ | none |
| [Inner product](/two-source-extractor/) | one bit from two sources | a second source, with $k_1 + k_2 > n + 2\log_2(1/\varepsilon) - 2$ | none |

: Derandomization tools. The generators are listed with output length $m$; the extractors take a source of $n$ bits with min-entropy $k$. The expander walk row counts the random bits of an algorithm that uses $m$ bits per run.

## Choosing a method

- If the analysis is an expectation over independent choices and the conditional expectation has a closed form, use the method of conditional expectations: it needs no search.
- If the analysis uses only pairwise or $k$-wise independence, enumerate a small sample space; when only parities matter, a small-bias space is smaller still.
- If the algorithm keeps its randomness but random bits are scarce, reduce the error with an expander walk instead of independent runs.
- If the source is a biased but independent coin, use von Neumann's pairs or Peres's iteration. For a source known only by its min-entropy, hash it with a seed, as the leftover hash lemma allows.
- Generators from hardness are theorems, not tools: their seeds are short, but they rest on unproved lower bounds and run in time $2^{O(d)}$.

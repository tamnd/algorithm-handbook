## What to remember

- A deterministic protocol with $c$ bits splits the [communication matrix](/communication-matrix/) $M_f$ into at most $2^c$ monochromatic rectangles. Every lower bound on $D^{cc}(f)$ in the chapter counts these rectangles. A $z$-[fooling set](/fooling-set-method/) of size $s$ needs $s$ leaves, and the [log-rank bound](/log-rank-lower-bound/) gives $D^{cc}(f) \ge \lceil \log_2(\operatorname{rank} M_f + \operatorname{rank}(J - M_f)) \rceil$. Both give $n + 1$ for equality, greater-than, disjointness and inner product on $n$ bits.
- The rank bound is far from tight in general: $\log_2 \operatorname{rank} M_f \le D^{cc}(f) = O(\sqrt{\operatorname{rank} M_f})$. The [log-rank conjecture](/log-rank-conjecture/), that $D^{cc}$ is polynomial in $\log \operatorname{rank}$, is open; the known gap is about quadratic.
- Randomness can save exponentially. Equality costs $n + 1$ bits deterministically, $\Theta(\log n)$ with private coins and $O(1)$ with public coins. By Newman's theorem, public coins save at most $O(\log n)$ bits, and private-coin cost is always $\Omega(\log D^{cc}(f))$.
- Randomized lower bounds need rectangles that are almost balanced or corrupted. [Discrepancy](/discrepancy-method/) gives $R(\mathrm{IP}_n) \ge n/2 - \log_2 3$. Under every distribution some rectangle of disjointness has discrepancy at least $1/(2n + 1)$, so its $\Omega(n)$ bound comes from the [corruption bound](/corruption-bound/) or from [information complexity](/information-complexity/), which adds up exactly over independent copies.
- One-way and few-round protocols can be much weaker than two-way ones. Index costs $\lceil \log_2 n \rceil + 1$ bits two-way but at least $(1 - H_2(\delta))\, n$ one-way from Alice with error $\delta$. This bound is the source of most space lower bounds for streaming.
- For a total Boolean function, $\mathrm{s}(f) \le \mathrm{bs}(f) \le C(f) \le D^{dt}(f)$ and $\deg(f) \le D^{dt}(f)$. Upward, $D^{dt}(f) \le C_0(f)\, C_1(f)$, $D^{dt}(f) \le \mathrm{bs}(f)^3$ and, since Huang's theorem $\mathrm{s}(f) \ge \sqrt{\deg(f)}$, every measure is bounded by a polynomial in $\mathrm{s}(f)$.
- A quantum algorithm with $T$ queries has an acceptance probability of degree at most $2T$, so $Q(f) \ge \widetilde{\deg}(f)/2$. This gives $Q(\mathrm{OR}_n) = \Theta(\sqrt n)$, $Q(\mathrm{PARITY}_n) = \lceil n/2 \rceil$ and $Q(\mathrm{MAJ}_n) = \Theta(n)$. For total functions $D^{dt}(f) = O(Q(f)^4)$.
- The [Karchmer-Wigderson theorem](/karchmer-wigderson-theorem/) is exact: the least depth of a fan-in-2 formula for $f$ equals the deterministic cost of finding a position where a 1-input and a 0-input differ.

## The standard problems side by side

| Problem | $D^{cc}$ | Randomized $R$ | One-way from Alice, randomized | Quantum |
|---|---|---|---|---|
| [Equality](/equality-problem/) | $n + 1$ | $\Theta(\log n)$ private, $O(1)$ public | $O(1)$ public | $O(\log n)$ simultaneous |
| [Greater-than](/greater-than-problem/) | $n + 1$ | $\Theta(\log n)$ | $\Theta(n)$ | |
| [Disjointness](/disjointness-problem/) | $n + 1$ | $\Theta(n)$ | $\Theta(n)$ | $\Theta(\sqrt n)$ |
| [Inner product](/inner-product-problem/) | $n + 1$ | $\Theta(n)$ | $\Theta(n)$ | $\Theta(n)$ |
| [Index](/index-problem/) | $\lceil \log_2 n \rceil + 1$ | $\Theta(\log n)$ | $\ge (1 - H_2(\delta))\, n$ | $\ge (1 - H_2(\delta))\, n$ one-way |
| [Gap Hamming distance](/gap-hamming-distance/) | $\Theta(n)$ | $\Theta(n)$ | $\Theta(n)$ | |

: Costs on $n$-bit inputs (for index, Alice holds $n$ bits and Bob an index). Empty cells are not given by the entries. All lower bounds are unconditional theorems about the model.

## Using the chapter

To prove that a two-party problem is hard:

- For a deterministic bound, try a fooling set first; it needs no algebra and often gives the exact value. If the function has a structured matrix, compute its rank, over the reals, since the real rank gives the strongest bound.
- For a randomized bound, these bounds fail when the function has a large monochromatic rectangle, as equality and greater-than do. Try discrepancy under the uniform distribution for inner-product-like functions, and the corruption bound or information complexity for disjointness-like ones.
- Most often, reduce instead. Index gives one-way bounds, disjointness gives two-way bounds, gap Hamming distance gives $\Omega(1/\varepsilon^2)$ bounds for approximation, and pointer chasing gives bounds that depend on the number of rounds or passes.

To bound queries, compute $\mathrm{s}$, $C$ and $\deg$ of small cases by hand or by program; for symmetric functions, symmetrization reduces approximate degree to one variable, and Paturi's theorem on the [approximate degree](/approximate-degree/) page gives it up to a constant factor.

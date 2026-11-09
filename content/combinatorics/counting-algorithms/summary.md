## What to remember

- **Binomial coefficients.** $\binom{n}{k}$ counts the $k$-subsets of an $n$-set. One row of [Pascal's triangle](/pascal-triangle-dp/) gives it in $nk - k(k-1)/2$ additions, modulo any $m$. The product formula $r \leftarrow r(n-k+i)/i$ divides exactly at each step. Modulo a prime $p > n$ use factorial tables, and modulo a small prime use Lucas's theorem.
- **Inclusion-exclusion.** The objects with none of $m$ bad properties number $\sum_{J \subseteq [m]} (-1)^{|J|} N(J)$, where $N(J)$ counts those with at least the properties in $J$. The [derangements](/derangement/) follow, with $D_n$ the nearest integer to $n!/e$ for $n \ge 1$, and so do the coprime pairs, $\sum_d \mu(d) \lfloor N/d \rfloor^2 \approx 6N^2/\pi^2$.
- **Paths.** Monotone paths from $(0, 0)$ to $(a, b)$ number $\binom{a+b}{a}$. Reflection removes those that cross a diagonal and gives $C_n = \binom{2n}{n}/(n+1) \sim 4^n/(n^{3/2}\sqrt\pi)$. When $\gcd(a, b) = 1$, the cycle lemma gives $\binom{a+b}{a}/(a+b)$ paths below the line to $(a, b)$.
- **Three triangles.** $S(n, k) = k\,S(n-1, k) + S(n-1, k-1)$ counts set partitions, $c(n, k) = (n-1)\,c(n-1, k) + c(n-1, k-1)$ permutations by cycles, and $A(n, k) = (k+1)A(n-1, k) + (n-k)A(n-1, k-1)$ permutations by descents. The row sums of $S$ are the Bell numbers.
- **Generating functions.** A product of series is a convolution. Making change is the coefficient of $z^n$ in $\prod_i 1/(1 - z^{d_i})$; a finite set of states gives a rational series with denominator $\det(I - zM)$.
- **Partitions.** The pentagonal recurrence $p(n) = \sum_{j \ge 1} (-1)^{j+1}\bigl[p(n - j(3j-1)/2) + p(n - j(3j+1)/2)\bigr]$ gives $p(0), \ldots, p(n)$ in $\Theta(n^{3/2})$ additions, and $p(n) \sim e^{\pi\sqrt{2n/3}}/(4n\sqrt 3)$.
- **Labelled structures.** There are $2^{\binom{n}{2}}$ labelled graphs and $n^{n-2}$ labelled trees on $[n]$. The exponential of an exponential generating function counts sets of structures, so its logarithm turns all graphs into connected ones.
- **Symmetry.** The classes under a group $G$ number $\frac{1}{|G|}\sum_{g \in G} |\mathrm{Fix}(g)|$; for $k$-coloured necklaces of length $n$ this is $\frac{1}{n}\sum_{d \mid n} \varphi(d)\,k^{n/d}$.
- **Hard counts.** The permanent is #P-complete. Ryser's and Glynn's formulas take $\Theta(2^n n)$ time, and planar matchings take $O(n^3)$ by Kasteleyn's method. An [FPRAS](/fpras/) is within a factor $1 \pm \varepsilon$ with probability at least $3/4$; the [Karp-Luby algorithm](/karp-luby-algorithm/) is one for DNF counting, with $\lceil 3m\ln(2/\delta)/\varepsilon^2\rceil$ samples.

## The methods side by side

| Method | Counts | Time | Extra space |
|---|---|---|---|
| [Pascal's triangle](/pascal-triangle-dp/) | $\binom{n}{k}$ modulo any $m$ | $nk - k(k-1)/2$ additions | $\Theta(k)$ |
| [Factorial tables](/binomial-coefficient-computation/) | $\binom{n}{k} \bmod p$, prime $p > n$ | $O(n + \log p)$, then $O(1)$ per query | $\Theta(n)$ |
| [Coin change](/coin-change-counting/) | multisets of $m$ coin values with sum $n$ | $O(nm)$ additions | $\Theta(n)$ |
| [Subset sum](/counting-subset-sum/) | subsets of $n$ numbers with sum $T$ | $O(nT)$ additions | $\Theta(T)$ |
| [Pentagonal recurrence](/euler-pentagonal-recurrence/) | $p(0), \ldots, p(n)$ | $\Theta(n^{3/2})$ additions | $\Theta(n)$ |
| [Connected graphs](/counting-connected-labeled-graphs/) | connected labelled graphs on $[n]$ | $O(n^2)$ operations | $\Theta(n)$ |
| [Ryser](/ryser-formula/), [Glynn](/glynn-formula/) | permanent of an $n \times n$ matrix | $\Theta(2^n n)$ | $\Theta(n)$ |
| [Kasteleyn](/kasteleyn-method/) | perfect matchings of a planar graph | $O(n^3)$ | $\Theta(n^2)$ |
| [Karp-Luby](/karp-luby-algorithm/) | DNF solutions within $1 \pm \varepsilon$ | $O(m(n + L)\log(1/\delta)/\varepsilon^2)$ | $O(m + n)$ |
| [Barvinok](/barvinok-algorithm/) | lattice points in a polytope of fixed dimension $d$ | $L^{O(d \log d)}$ | $L^{O(d \log d)}$ |

: Counting methods with their costs as the entries state them, in arithmetic operations on the numbers involved. Exact answers can be long, and a big-integer count costs more in proportion to their length. For Karp-Luby, $m$ is the number of clauses, $n$ of variables and $L$ of literals; for Barvinok, $L$ is the input length in bits.

## Choosing a method

- For one exact binomial coefficient, use the product formula. For many residues modulo a large prime, build factorial tables once. Modulo a small prime use Lucas's theorem; modulo a composite use Pascal's triangle.
- When the objects must avoid a few bad properties, and those with a given set of bad properties are easy to count, use inclusion-exclusion. Over the divisors of an integer it becomes Möbius inversion.
- When a count splits by the first step, the first block or the component of a fixed element, write the recurrence and fill a table. When the recurrence is a convolution, the generating function also gives the growth and often a faster method.
- When objects are built letter by letter with a bounded memory, use the transfer-matrix method; a matrix power then gives a far term in $O(\log n)$ matrix products.
- When the atoms carry labels, use exponential generating functions. When shapes count once up to symmetry, use Burnside's lemma, or Pólya's theorem to sort by colours.
- When the problem is #P-complete, use an exponential exact method for small sizes and an FPRAS when a relative error is enough. Check first whether the instance is planar or of bounded width, where exact polynomial methods exist.

## What to remember

- The probability in random hashing is over the choice of the function, made after the keys are fixed. The bounds hold for every key set that does not depend on the function.
- A family is **universal** when $\Pr[h(x) = h(y)] \le 1/m$ for distinct keys, and **pairwise independent** when $(h(x), h(y))$ is uniform on $[m]^2$. Pairwise independence implies universality, and it makes the variance of a sum of indicators the sum of their variances, so Chebyshev's inequality applies. Chernoff bounds do not.
- With a universal family and separate chaining, an absent key meets at most $\alpha = n/m$ keys in expectation and a stored key at most $1 + (n-1)/m$; the expected number of colliding pairs is at most $\binom{n}{2}/m$. With $m = n^2$ this is below $1/2$, which is the second level of FKS perfect hashing.
- The **dot-product family** $a \cdot x \bmod p$ collides with probability exactly $1/p$, because one nonzero digit of $x - y$ has an inverse modulo the prime $p$. With an offset $b$ it is pairwise independent, but never 3-wise independent.
- **Multiply-shift** keeps the top $\ell$ bits of $a x \bmod 2^w$ for a random odd $a$. Its collision probability is at most $2/m$, and the factor 2 is reached. Adding $b$ in a word of $\bar w \ge w + \ell - 1$ bits makes it pairwise independent.
- A random polynomial of degree $k - 1$ over $\mathbb{Z}_p$ is **$k$-independent** and no more. Chaining needs $k = 2$, linear probing $k = 5$, and some 4-independent families give linear probing $\Theta(\log n)$ expected time.
- **Min-wise independence** makes $\Pr[\min \pi(A) = \min \pi(B)] = |A \cap B| / |A \cup B|$. Exact families have size divisible by $\operatorname{lcm}(1, \ldots, n)$; $O(\log(1/\varepsilon))$-wise independence gives an $\varepsilon$-approximate family, and pairwise independence does not.
- Two-choice **cuckoo hashing** with fully random functions can place its keys exactly when no component of the cuckoo graph has more edges than vertices. Below load $1/2$ it fails with probability $O(1/n)$; above load $1/2$ it fails with probability $1 - o(1)$.

## The families side by side

| Family | Guarantee | Random numbers | Cost per key |
|---|---|---|---|
| [Dot product](/dot-product-hashing/) $a \cdot x \bmod p$ | collision exactly $1/p$ | $r$ | $\Theta(r)$ |
| Dot product with offset | pairwise independent | $r + 1$ | $\Theta(r)$ |
| [Multiply-shift](/multiply-shift-hashing/) | collision at most $2/m$ | 1 | one multiplication, one shift |
| Multiply-add-shift, $\bar w \ge w + \ell - 1$ | pairwise independent | 2 | one multiplication, one addition, one shift |
| [Polynomial](/k-independent-hashing/) of degree $k - 1$ mod $p$ | $k$-independent | $k$ | $k - 1$ multiplications by Horner's rule |
| [Simple tabulation](/tabulation-hashing/) | 3-independent, not 4 | one table per character | one lookup per character |
| Exact [min-wise](/min-wise-independent-hashing/) family on $[n]$ | min-wise independent | family size at least $\operatorname{lcm}(1, \ldots, n)$ | not practical |

: Hash families of this chapter and their guarantees. "Random numbers" counts what must be drawn to fix one function; for the dot product, $r$ is the number of base-$p$ digits of a key.

## Choosing a family

- To prove a bound or to teach, use the dot-product or affine family modulo a prime.
- For a chained table on integer keys, multiply-shift is enough; budget a factor 2 in the expected chain length, $1 + 2(n-1)/m$ for a stored key.
- When the analysis needs uniform single values or exact variances, as in sampling and sketches, use multiply-add-shift or the affine family, not plain multiply-shift: it sends key 0 to slot 0 for every multiplier.
- For linear probing, use a 5-independent family or tabulation hashing. For MinHash, use a hash function with a range much larger than the sets, so that ties are rare.
- For two-choice cuckoo hashing, keep each table at least $(1 + \varepsilon)$ times the number of keys. To fill the cells further, use more choices or buckets of several keys; a small stash lowers the failure probability.

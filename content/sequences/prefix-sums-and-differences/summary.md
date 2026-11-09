## What to remember

- **Prefix sums.** With $P[0] = 0$ and $P[i] = a[0] + \cdots + a[i-1]$, the sum of the half-open range $a[l \ldots r-1]$ is $P[r] - P[l]$. Building $P$ takes $\Theta(n)$ time and $n + 1$ words; each query then takes $O(1)$, so $q$ queries cost $\Theta(n + q)$, which is optimal.
- **The reason is a telescoping sum.** $\sum_{k=m}^{n-1} \big(f(k+1) - f(k)\big) = f(n) - f(m)$. Every range sum of $a$ is a telescoping sum of $P$.
- **An inverse is needed.** The method works for any associative operation with inverses: addition, addition modulo $m$, XOR, multiplication by units modulo $m$. It fails for max, min and gcd; use a [sparse table](/sparse-table/) for those.
- **Difference arrays undo prefix sums.** With $d[i] = a[i] - a[i-1]$, adding $c$ to $a[l \ldots r-1]$ is $d[l] \mathrel{+}= c$ and $d[r] \mathrel{-}= c$. So $m$ range adds followed by one read of the whole array cost $\Theta(n + m)$ instead of $\Theta(nm)$.
- **In two dimensions, four corners.** A rectangle sum is $S[r_2][c_2] - S[r_1][c_2] - S[r_2][c_1] + S[r_1][c_1]$, and a rectangle add is four point updates with the same signs. In $d$ dimensions, $2^d$ corners.
- **Sums and differences are calculus.** A prefix-sum array is a discrete antiderivative: $\sum_{a \le k < b} f(k) = F(b) - F(a)$ whenever $\Delta F = f$. Falling powers $k^{\underline{m}}$ play the part of $x^m$, and summation by parts plays the part of integration by parts.
- **Updates change the picture.** When point updates and prefix-sum queries interleave, a [Fenwick tree](/fenwick-tree/) or a [segment tree](/segment-tree/) does both in $O(\log n)$. For word-sized values this is optimal; for one-bit values the tight bound is $\Theta(\log n / \log \log n)$, and the lower bound is the theorem of Fredman and Saks.

## The methods side by side

| Method | Preprocessing | Query | Update | Notes |
|---|---|---|---|---|
| Direct summation | none | $O(r - l)$ | $O(1)$ | any operation |
| [Prefix sums](/prefix-sums/) | $\Theta(n)$ | $O(1)$ | $\Theta(n)$ rebuild | needs an inverse |
| [Difference array](/difference-array/) | $\Theta(n)$ | one $\Theta(n)$ pass, then $O(1)$ per read | $O(1)$ per range add | batch: all adds before the reads |
| [Two-dimensional prefix sums](/two-dimensional-prefix-sums/) | $\Theta(RC)$ | $O(1)$, 4 lookups | $\Theta(RC)$ rebuild | needs an inverse |
| [Two-dimensional difference array](/two-dimensional-difference-array/) | $\Theta(RC)$ | one $\Theta(RC)$ pass | $O(1)$ per rectangle add | batch |
| [Fenwick tree](/fenwick-tree/) | $\Theta(n)$ | $O(\log n)$ | $O(\log n)$ | online; needs an inverse for ranges |
| [Segment tree](/segment-tree/) | $\Theta(n)$ | $O(\log n)$ | $O(\log n)$ | online; any associative operation |

: Methods for sums over ranges of an array of $n$ items or a grid of $R \times C$ cells. All times are worst case on a word RAM with every sum in one word. The two dynamic structures are explained in Volume 3; the [partial sums problem](/partial-sums-problem/) gives their place among the lower bounds.

## Choosing a method

- The data does not change and the operation has an inverse: prefix sums, in one or two dimensions. Nothing is faster.
- Many range adds, then the final array: a difference array. If reads come between the adds, keep the differences in a Fenwick tree.
- The operation has no inverse (minimum, maximum, gcd): a sparse table for static data, a segment tree for changing data.
- Updates and range sums mixed: a Fenwick tree. It is shorter to write than a segment tree and uses $n$ words.
- Coordinates are huge and sparse: sort the $2m$ endpoints and sweep, instead of allocating a difference array over the whole range.
- Watch the word size. Prefix sums grow to $n$ times the largest item; use 64-bit integers. For floating-point data, expect an error proportional to $|P[r]|$, not to the range sum.

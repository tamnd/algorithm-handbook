## What to remember

- A **subsequence** keeps items in order but may skip. Testing whether $P$ is a subsequence of $T$ takes one greedy scan in $O(|T|)$ time: match each item of $P$ at its earliest possible place. Counting is harder: the number of occurrences obeys $N[i,j] = N[i-1,j] + [t_i = p_j]\,N[i-1,j-1]$ and costs $\Theta(nm)$.
- A string of length $n$ has at most $2^n$ subsequences, but repeated letters give the same subsequence many times. The number of **distinct** ones satisfies $D_i = 2D_{i-1} - D_{p(i)-1}$, where $p(i)$ is the previous position of the letter $s_i$.
- The heaviest subsequence with **no two adjacent items** obeys $W_i = \max(W_{i-1}, W_{i-2} + w_i)$: linear time, constant space.
- The **longest increasing subsequence** takes $O(n \log n)$ time: keep, for each length, the smallest tail of an increasing subsequence of that length, and place each item by binary search. The tails stay sorted, which is what makes the search possible.
- **Erdős–Szekeres:** any $nm + 1$ distinct numbers contain an increasing subsequence of length $n + 1$ or a decreasing one of length $m + 1$. Equivalently $L_\uparrow \cdot L_\downarrow \ge N$. **Dilworth** gives the exact form: the fewest increasing subsequences that cover a sequence equals its longest non-increasing subsequence.
- The **longest common subsequence** of $X$ and $Y$ fills a table with $c[i,j] = c[i-1,j-1] + 1$ when $x_i = y_j$ and $\max(c[i-1,j], c[i,j-1])$ otherwise. That is $\Theta(mn)$ time; the length alone needs only $\Theta(\min(m,n))$ space.
- Many problems are the LCS in disguise. With $L = \text{lcs}(X,Y)$, the shortest edit script by insertions and deletions has $m + n - 2L$ steps, the shortest common supersequence has length $m + n - L$, and the longest palindromic subsequence of $S$ is $\text{lcs}(S, S^R)$.
- For more than two strings, LCS and the shortest common supersequence are NP-hard. For two strings, no $O(n^{2-\varepsilon})$ algorithm exists unless the strong exponential time hypothesis fails.

## LCS and LIS algorithms side by side

| Method | Time | Space | Gives |
|---|---|---|---|
| [LIS by quadratic DP](/longest-increasing-subsequence/) | $\Theta(n^2)$ | $\Theta(n)$ | subsequence |
| [LIS by piles and binary search](/longest-increasing-subsequence/) | $O(n \log n)$ | $\Theta(n)$ | subsequence |
| [LCS table](/lcs-dynamic-programming/) | $\Theta(mn)$ | $\Theta(mn)$ | subsequence |
| LCS table, one row | $\Theta(mn)$ | $\Theta(\min(m,n))$ | length only |
| [Hirschberg](/hirschberg-lcs/) | $\Theta(mn)$ | $\Theta(m+n)$ | subsequence |
| [Hunt–Szymanski](/hunt-szymanski/) | $O((r + m + n) \log n)$ | $O(r + m + n)$ | subsequence |
| [Myers](/myers-diff/) | $O((m+n)D)$ | $O(m+n)$ with the middle snake | edit script |
| [Bit-parallel](/bit-parallel-lcs/) | $\Theta(n \lceil m/w \rceil)$ | $\Theta(\sigma \lceil m/w \rceil)$ | length only |

: Algorithms for the longest increasing and longest common subsequence. Here $r$ is the number of matching pairs $(i, j)$ with $x_i = y_j$, $D$ is the length of the shortest edit script, $w$ is the word size and $\sigma$ the alphabet size.

## Choosing a method

- For a single LCS of two short strings, fill the table and trace back. It is simple and hard to get wrong.
- When the strings are long and you need the subsequence itself, not just its length, use Hirschberg's algorithm and keep the memory linear.
- When the two inputs are versions of one file, use Myers' algorithm: its cost grows with the number of changes, not with the product of the lengths. When the inputs are long but share few equal items, Hunt–Szymanski is faster.
- When only the length matters and the alphabet is small, the bit-parallel method is the fastest in practice.
- For the longest increasing subsequence, always use the pile method; the quadratic DP is worth keeping only as a model for variants with weights or extra rules.
- When the problem asks for a supersequence, a palindrome or an edit script without substitutions, reduce it to the LCS first.

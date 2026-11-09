## What to remember

- A **palindrome** equals its reversal. Recognition takes $\lfloor n/2 \rfloor$ comparisons with two pointers, and no algorithm that compares symbols for equality uses fewer.
- Every palindromic substring has one of $2n + 1$ **centers**, and the palindromes at a center are nested. The radius of the longest one at each center describes them all.
- **Manacher's algorithm** computes all $2n + 1$ radii in $\Theta(n)$ time. Inside the rightmost palindrome found so far, a center starts from the radius of its mirror, so no symbol left of the right end is compared twice.
- From the radii you read the longest palindromic substring, the number of palindromic occurrences as a sum, and the answer to "is $s[i..j]$ a palindrome" in $O(1)$ time per query.
- A string of length $n$ has at most $n$ **distinct** nonempty palindromes: each new symbol adds at most one, its longest palindromic suffix. Strings that reach the bound are **rich**.
- Adding symbols at one end to make a palindrome reduces to the **longest palindromic prefix** or suffix, which the prefix function of $s\,\#\,s^R$ finds in linear time. Editing anywhere reduces to the longest palindromic subsequence.
- The fewest palindromic pieces come from a prefix recurrence in $\Theta(n^2)$ time. The palindromic suffixes of a prefix form $O(\log n)$ arithmetic series, and **series links** in the eertree use this to reach $O(n \log n)$.
- The **eertree** has one node per distinct palindrome, edges that add a symbol on both sides and suffix links, and is built online in linear time for a constant alphabet.

## The main algorithms side by side

| Problem | Method | Time | Space | Notes |
|---|---|---|---|---|
| Is $s$ a palindrome | [two pointers](/palindrome-recognition/) | $\Theta(n)$ | $O(1)$ | optimal number of comparisons |
| All maximal palindromes | [Manacher](/manacher/) | $\Theta(n)$ | $\Theta(n)$ | also online |
| Substring queries | Manacher radii | $\Theta(n + q)$ | $\Theta(n)$ | one comparison per query |
| Shortest palindrome by prefixing | [prefix function](/shortest-palindrome/) of $s\,\#\,s^R$ | $\Theta(n)$ | $\Theta(n)$ | longest palindromic prefix |
| Palindrome edit distance | [subsequence table](/palindrome-edit-distance/) | $\Theta(n^2)$ | $O(n)$ | insertions or deletions |
| All partitions | [backtracking](/palindrome-partition-backtracking/) | $\Theta(n^2 + nP)$ | $\Theta(n^2)$ | $P$ partitions, up to $2^{n-1}$ |
| Fewest pieces | [prefix recurrence](/palindrome-partition-dp/) | $\Theta(n^2)$ | $\Theta(n^2)$ | short to write |
| Fewest pieces | [series links](/series-links/) | $O(n \log n)$ | $\Theta(n)$ | online |
| Distinct palindromes | [eertree](/palindromic-tree/) | $O(n \log k)$ | $\Theta(n)$ | $k$ distinct symbols |

: Palindrome problems on a string of length $n$, with $q$ queries. The eertree time is for edges kept in sorted order; with an array per node over a constant alphabet it is $\Theta(n)$. The fewest pieces can also be found in $O(n)$ time by a method of Borozdin, Kosolobov, Rubinchik and Shur.

## Choosing a method

- For the longest palindromic substring of a short string, expanding around each center is enough. For long strings or many strings, use Manacher.
- For many queries "is this substring a palindrome", run Manacher once and compare the radius with the length. Hashes of $s$ and $s^R$ also work and extend to strings that change.
- To count distinct palindromes, or to work with each distinct palindrome once, build the eertree.
- To cut a string into the fewest palindromes, use the quadratic recurrence up to a few thousand symbols and series links beyond that.
- To list all partitions, use backtracking over a table of palindromic substrings; the output may be exponential, so count first with the same recurrence if the number matters.
- For DNA, test reverse-complement palindromes with the same algorithms, after replacing equality of mirror symbols by complementarity.

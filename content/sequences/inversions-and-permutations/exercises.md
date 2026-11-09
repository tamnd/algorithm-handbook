1. ◦ For the permutation $\pi = 2\,4\,1\,3\,6\,5$, write its [cycles](/permutation-cycles/) and its [inverse](/permutation-inverse/) in one-line form. Count its inversions and its descents, and give its major index. Find its sign twice: from the inversions and from the cycles.

2. ◦ An array holds $4\,3\,5\,1\,2$. What is the smallest number of swaps that sorts it, if any two items may be swapped? What if only neighbours may be swapped? Give a shortest sequence of swaps for the first question.

3. ◦ Find the sign of the reversal $n\,(n-1) \cdots 2\,1$, first from its number of inversions and then from its cycles. For which $n$ is it even?

4. ◦ Give the [Lehmer code](/lehmer-code/) and the [inversion table](/inversion-table/) of $2\,4\,1\,3\,6\,5$, and check that both add up to the number of inversions. Then find the rank of the permutation among the $720$ permutations of $[6]$ in lexicographic order, counting from 0.

5. ◦ Write $2026$ in the [factorial number system](/factorial-number-system/). Use the digits as a Lehmer code to find the permutation of $[7]$ with rank $2026$ in lexicographic order. How many inversions does it have?

6. ◦ Find the permutation of $[5]$ that comes right after $1\,3\,5\,4\,2$ in lexicographic order, and the one that comes right before it.

7. ◦ Two judges rank five entries. The first gives the order $A, B, C, D, E$ and the second gives $C, A, B, E, D$. Find the [Kendall tau distance](/kendall-tau-distance/) between the two rankings and the Kendall coefficient $\tau$.

8. ◦ The input $1, 2, 3$ is pushed onto a [stack](/stack/) in this order, with pops in between. Which of the six permutations of $[3]$ can come out? Which of the six can a single stack sort into $1\,2\,3$?

9. ◦ How many permutations of $[6]$ have exactly 3 inversions? Use the [Mahonian numbers](/mahonian-numbers/) for $n = 5$.

10. • For the two rankings of exercise 7, find the [Spearman footrule](/spearman-footrule/), the [Cayley distance](/cayley-distance/) and the [Ulam distance](/ulam-distance/). Check the Diaconis–Graham bounds $I + T \le F \le 2I$, where $I$ is the Kendall distance, $T$ the Cayley distance and $F$ the footrule.

11. • Show that the Cayley distance and the Ulam distance between two permutations are never larger than the Kendall distance. Give two permutations of $[3]$ whose Ulam distance is larger than their Cayley distance.

12. • Show that $\operatorname{des}(\pi) \le \operatorname{inv}(\pi)$ for every permutation $\pi$. Describe the permutations for which the two are equal, and count those of $[n]$.

13. • Show that $M(n, k) = M(n, \binom n2 - k)$ for the Mahonian numbers, by a bijection on permutations.

14. • Show that a random permutation of $[n]$ has, on average, $1/k$ cycles of length $k$, for each $1 \le k \le n$. Add these up and compare with the expected number of cycles.

15. • Let $\pi$ be a permutation of $[n]$ whose first item is $x$. Moving $x$ to the end changes the number of inversions by $n + 1 - 2x$. Use this to find the inversion counts of all $n$ rotations of $\pi$ in $O(n \log n)$ time in all.

16. • Two arrays $a$ and $b$ hold the same $n$ distinct items. Decide in $O(n)$ expected time whether $b$ can be reached from $a$ by an even number of swaps.

17. • Show that a stack can produce $\pi$ from the input $1, 2, \ldots, n$ exactly when it can sort $\pi^{-1}$. Use this to explain why the two sets of permutations in exercise 8 have the same size for every $n$.

18. • Sort the stack of pancakes $3\,1\,4\,5\,2$ (top first) with the simple method of [pancake sorting](/pancake-sorting/), which flips the largest unsorted pancake to the top and then down into place. How many flips does it use? Then show that $2\,4\,1\,3$ cannot be sorted with fewer than 4 flips.

19. • List all permutations of $[n]$ in lexicographic order with the [successor](/lexicographic-successor/) algorithm. Show that exactly $n!/(k-1)! - n!/k!$ of the $n! - 1$ steps rewrite the last $k$ positions and leave the first $n - k$ unchanged, for $2 \le k \le n$. What does the average number of rewritten positions tend to as $n$ grows?

20. ★ Two sequences $a$ and $b$ of length $n$ hold the same multiset of items, with repeats allowed. Show that the fewest swaps of neighbours that turn $a$ into $b$ is found by matching the $k$-th copy of each value in $a$ with the $k$-th copy of the same value in $b$ and counting the inversions of the resulting permutation. Give an $O(n \log n)$ algorithm.

21. ★ An array of $n$ distinct numbers changes by swaps of two positions $i < j$, given one at a time. After each swap, report the number of inversions. Find the change caused by one swap in terms of the items between positions $i$ and $j$, and design a structure that handles each swap in $O(\log^2 n)$ time.

22. ★ Prove that the major index and the inversion count have the same distribution on the permutations of $[n]$. Insert $n$ into each of the $n$ gaps of a permutation of $[n-1]$, and show that the major index grows by $0, 1, \ldots, n - 1$, each once.

23. ★ Show that exactly $2^{n-1}$ permutations of $[n]$ avoid both of the patterns $123$ and $132$. Use the place of the item $n$, or of the item $1$.

24. ★ Given a permutation $\pi$ of $[n]$ and a budget $K$, find the lexicographically smallest permutation that can be reached from $\pi$ by at most $K$ swaps of neighbours. Prove that a greedy choice is right and make it run in $O(n \log n)$ time.

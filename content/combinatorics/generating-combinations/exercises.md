1. ◦ Apply the [lexicographic successor](/lexicographic-combinations/) rule to the 4-subsets $\{2, 5, 7, 8\}$ and $\{1, 6, 7, 8\}$ of $[8]$. For each, say which entry grows and give the result.

2. ◦ Find the colex rank, counting from 0, of the 3-subset $\{1, 3, 6\}$ of $\{0, 1, \ldots, 9\}$, using the formula of [colexicographic order](/colexicographic-order/). Which integer has the same subset as its set of one bits, and where does it stand among the integers with three one bits?

3. ◦ Write 1000 in the [combinatorial number system](/combinatorial-number-system/) of degree 3, that is, as $\binom{c_3}{3} + \binom{c_2}{2} + \binom{c_1}{1}$ with $c_3 > c_2 > c_1 \ge 0$.

4. ◦ How many multisets of size 5 can be drawn from 4 kinds of items? Under the map $b_i \mapsto b_i + i - 1$ of [combinations with repetition](/combinations-with-repetition/), which 5-subset of $[8]$ does the multiset $\{1, 1, 3, 4, 4\}$ become?

5. ◦ A binary counter runs from $00000$ to $11111$. How many bits does it write in total? A Gray code over the same 32 strings writes one bit per step; how many in total? Then list, in the order of [submask enumeration](/submask-enumeration/), the submasks of $10110$.

6. ◦ Apply the [cool-lex](/cool-lex-order/) rule three times, starting from $0110100$.

7. ◦ Apply [Gosper's hack](/gospers-hack/) to 56. Give the result in decimal and in binary, and say which 3-subsets of $\{0, \ldots, 6\}$ the two words stand for.

8. • Find the lexicographic rank, counting from 0, of $\{2, 5, 6, 9\}$ among the 4-subsets of $[10]$, and the subset of rank 100. Use [ranking and unranking combinations](/combinatorial-ranking-and-unranking/).

9. • For a $k$-subset $A$ of $[n]$ let $A' = \{n - a : a \in A\}$, a $k$-subset of $\{0, \ldots, n-1\}$. Show that $A$ comes before $B$ in lexicographic order exactly when $A'$ comes after $B'$ in colex order. Deduce a formula for the lexicographic rank of $A$ from the colex rank of $A'$, and check it on exercise 8.

10. • By the Kruskal-Katona theorem in [colexicographic order](/colexicographic-order/), the smallest shadow of a family of $m$ sets of size 3 is the shadow of the first $m$ sets in colex order. Find the smallest shadow for $m = 7$ and for $m = 5$, and give a family of 7 three-sets that reaches it.

11. • For $n = 5$, count how often each bit flips in a full run of the binary counter and in a full run of the binary reflected Gray code. Give a formula for bit $j$, with bit 0 the lowest, in each case.

12. • The revolving door order for $k$-subsets of $\{0, \ldots, n-1\}$ is the list of strings of weight $k$ in the binary reflected Gray code, with bit $j$ standing for element $j$. Write out the list for $n = 6$, $k = 3$, and find the ranks of $\{1, 3, 5\}$ and $\{0, 2, 5\}$. Compare with the alternating formula in [Ehrlich's loopless combination generation](/ehrlich-loopless-combinations/).

13. • Use the rank formula of Ruskey and Williams in [cool-lex order](/cool-lex-order/) to find the rank of $\{1, 3, 4, 6\}$ for $n = 6$, and of $\{2, 4, 5, 7\}$ for $n = 8$. Check the first by running the rule from $111100$.

14. • Find the lexicographic rank, counting from 0, of the multiset $\{2, 2, 3, 5\}$ among the multisets of size 4 drawn from $[5]$. How many such multisets are there?

15. • Show that the colex list of the $k$-subsets of $[n]$ is a prefix of the colex list for $[n+1]$, and that this fails for lexicographic order. For $k = 2$, at which index, counting from 0, do the lexicographic lists for $n = 4$ and $n = 5$ first differ?

16. ★ Let $R(n, k)$ be the revolving door list of exercise 12. Prove that $R(n, k)$ is $R(n-1, k)$ followed by the reverse of $R(n-1, k-1)$ with $n - 1$ added to each subset. Find the first and the last subset of $R(n, k)$ for $0 < k < n$, and show that the list is cyclic: the last subset is one exchange from the first.

17. ★ Can the 2-subsets of $[n]$ be listed so that each step replaces one element $a$ by $a + 1$ or $a - 1$? Answer for every $n \ge 3$.

18. ★ How many steps of the cool-lex list for $n = 8$, $k = 4$ change four bits, not counting the step from the last string back to the first? For $n = 10$, $k = 5$? Find which strings are followed by such a step, and prove that there are $\binom{n-2}{k-1} - 1$ of them for $1 \le k < n$.

1. ◦ Write the string of rank 45 in the [binary reflected Gray code](/binary-reflected-gray-code/) $\Gamma_6$, and find the rank of the string $110110$.

2. ◦ Run the word method of [Gray to binary conversion](/gray-to-binary-conversion/), which replaces $x$ by $x \oplus (x \gg s)$ for $s = 1, 2, 4$, on the 8-bit word $10110100$. Give the word after each round and the rank in decimal.

3. ◦ Find $\rho(24)$, $\rho(32)$ and $\rho(63)$ in the [ruler sequence](/ruler-sequence/). Which bit changes between the strings of rank 23 and rank 24 of $\Gamma_6$, and what are the two strings?

4. ◦ Apply the parity rule (if the weight is even, flip bit 0; otherwise flip the bit to the left of the lowest 1) four times, starting from $0110$. Give each string and its rank in $\Gamma_4$.

5. ◦ In [loopless Gray code generation](/loopless-gray-code-generation/) with $n = 5$, the string is $01011$ and the focus pointers are $(f_0, \ldots, f_5) = (1, 1, 4, 3, 4, 5)$. Carry out one step: which bit flips, and what are the new string and pointers?

6. ◦ Is the list $000, 001, 011, 111, 101, 100, 110, 010$ a [cyclic Gray code](/cyclic-gray-code/)? Give its cyclic delta sequence and the transition count of each bit, and say whether it is a [balanced Gray code](/balanced-gray-code/).

7. ◦ What transition counts must a balanced Gray code have for $n = 6$, $n = 7$ and $n = 8$?

8. ◦ Take $k = 3$ and $n = 3$, and the rank $r = 14$. Write $r$ in base 3, then give the string of rank $r$ in the reflected [k-ary Gray code](/k-ary-gray-code/) and in the modular code, where digit $j$ is $(b_j - b_{j+1}) \bmod 3$.

9. ◦ Write out [Chase's sequence](/chase-sequence/) $C_{22}$ for strings with two 0s and two 1s, from the recursions for $A_{st}$ and $B_{st}$. Which step moves a 1 by two places, and is the list cyclic under the near-perfect rule?

10. • Bits 0 to 3 stand for items of weight 3, 5, 9 and 14. A program walks through $\Gamma_4$ and keeps the total weight of the current subset, adding or subtracting one weight per step. At which ranks does the total equal 17, and which subsets are they? How many updates does the full walk make?

11. • Show that $g(g(k)) = k \oplus \lfloor k/4 \rfloor$ and compute $g(g(4))$, which shows that $g$ is not its own inverse. More generally, show that applying $g$ to $k$ $2^m$ times gives $k \oplus \lfloor k/2^{2^m} \rfloor$. How many times must $g$ be applied to every 8-bit word to get the word back? And every 9-bit word?

12. • In $\Gamma_6$, check that the strings of ranks 10 and 32 differ in all six bits. Then show that any two strings of $\Gamma_6$ that differ in all six bits are at least 22 ranks apart.

13. • Count the Gray paths of $Q_3$ that start at $000$ and visit all eight strings. How many end at a neighbor of $000$, and where do the others end?

14. • In the $3 \times 3$ grid of strings $d_1 d_0$ with digits 0, 1, 2, a step changes one digit by 1. Show that no Gray code of the grid starts at $01$, and find every string at which a Gray code that starts at $00$ can end. Deduce that the grid has no cyclic Gray code.

15. • A mixed radix Gray code has radices $m_0 = 2$, $m_1 = 3$, $m_2 = 4$, with digit 0 changing fastest. How many times does each digit change in the reflected code? Check that the counts add up to $N - 1$.

16. • List the [revolving door order](/revolving-door-ordering/) $R(5, 3)$ of the 3-subsets of $\{1, \ldots, 5\}$. Mark the steps in which the element that leaves and the element that enters lie on two sides of another element of the subset. How many such steps are there?

17. • Unrank 30 in the revolving door order $R(7, 4)$ of the 4-subsets of $\{1, \ldots, 7\}$, with the rule in the entry: pick $t_k$ as the least $x$ with $\binom{x}{k} > r$, replace $r$ by $\binom{x}{k} - 1 - r$, and go on with $k - 1$. Check the answer with the rank formula.

18. • Write out the [Eades-McKay order](/eades-mckay-algorithm/) $K_{23}$ for strings with two 0s and three 1s, and Chase's sequence $C_{23}$ for the same strings. Which moves of each list cover two places? Explain why every homogeneous list of strings with at most two 0s is near-perfect.

19. • Show that if a list of all $\binom{n}{k}$ $k$-subsets of $[n]$ moves one element by $\pm 1$ at each step, then the numbers of subsets with an even sum and with an odd sum differ by at most 1. Use this to show that no such list exists for $n = 8$, $k = 4$ and for $n = 7$, $k = 3$.

20. ★ Show that $Q_3$ has exactly 6 Gray cycles, counted as undirected cycles with no start fixed.

21. ★ Prove that for $n \ge 1$ the cube $Q_n$ has a Gray path from $u$ to $v$ exactly when $u$ and $v$ differ in an odd number of bits.

22. ★ Prove that the modular $k$-ary code, digit $j$ equal to $(b_j - b_{j+1}) \bmod k$ with $b_n = 0$, changes exactly one digit, by $+1 \bmod k$, from rank $r$ to rank $r + 1$, and that it is cyclic. Which digit changes, and how can a generator find it in $O(1)$ time without direction flags?

23. ★ Complete exercise 19: find the difference between the numbers of even-sum and odd-sum $k$-subsets of $[n]$ for all $n$ and $k$, and deduce that an adjacent-transposition Gray code for combinations can exist only when $k \le 1$, $n - k \le 1$, or $k$ and $n - k$ are both odd.

24. ★ For $n = 4$, list every multiset of transition counts that meets the necessary conditions of balanced Gray codes: each $c_j$ even and, with the counts sorted, $c'_1 + \cdots + c'_k \ge 2^k$ for every $k$. The reflected code and the examples of the entry realize three of them. Find a cyclic Gray code of $Q_4$ for the fourth.

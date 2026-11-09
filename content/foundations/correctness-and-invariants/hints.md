1. Precondition $a \ge 0$ and $b > 0$; postcondition $a = qb + r$ and $0 \le r < b$. Without $0 \le r < b$, the pair $(q - 1, r + b)$ also satisfies $a = qb + r$.

2. (a) valid; (b) valid, since the loop never stops and partial correctness asks nothing then; (c) invalid, take $x = 1$; (d) valid, since no state satisfies $\mathit{false}$; (e) valid: the loop stops because $x$ decreases and stays non-negative, and on exit $x \ge 0$ and $x \le 0$.

3. (a) $x > 4$. (b) Work backwards: $\mathrm{wp}(y \leftarrow y + x,\ y = 10)$ is $y + x = 10$, and then $y + 2x = 10$. (c) $(x < 0 \wedge -x \ge 1) \vee (x \ge 0 \wedge x \ge 1)$, that is $x \ne 0$.

4. Before the test with index $i$: $m = \max A[0 \ldots i-1]$. It holds for $i = 1$; each pass extends the range by one item; at exit $i = n$.

5. The variant is $b$. Since $0 \le a \bmod b < b$, the new $b$ is a natural number smaller than the old one.

6. (a), (c) and (e) are well-founded. (b): $0 > -1 > -2 > \cdots$. (d): $b$, $ab$, $aab$, $aaab$, … each comes before the one before it in a dictionary.

7. The first satisfies it. In the second, index 5 holds 1 and its parent, index 2, holds 3.

8. Partially correct: if the loop stops, then $n = 1$. Whether it is totally correct is the Collatz conjecture, which is open.

9. In both, the abstraction function maps a list to the set of its items. Representation A has the invariant $\mathit{true}$, and $[3, 1, 3]$ represents $\{1, 3\}$. Representation B requires a strictly increasing list, and $[3, 1, 3]$ is not valid.

10. (a) Yes: the two cells are disjoint parts of the heap. (b) No: the same cell cannot be in two disjoint parts. (c) Yes: each conjunct says the heap is exactly one cell, so the two addresses are the same.

11. Invariant: $0 \le lo \le hi \le n$, $A[j] \le x$ for $j < lo$ and $A[j] > x$ for $j \ge hi$. Variant $hi - lo$. With the ceiling, when $hi = lo + 1$ the midpoint is $hi$; if $A[hi] > x$ then $hi$ does not change and the loop runs forever, and if $hi = n$ the access is out of bounds.

14. Work backwards: before the last assignment you need $x - y = b \wedge y = a$; before the second, $y = b \wedge x - y = a$; before the first, $y = b \wedge x = a$. With wrapping arithmetic the integers modulo $2^w$ obey the same laws of addition and subtraction, so the triple is valid. With a trap on overflow it is not totally correct: $x + y$ can overflow.

16. Each pass swaps an adjacent pair that is out of order, which removes exactly one inversion, so the number of inversions is a variant. When no guard is true the four values are in order. At most $\binom42 = 6$ passes, reached from $q_1 > q_2 > q_3 > q_4$.

19. Test that $g > 0$, $g$ divides $a$ and $b$, and $sa + tb = g$. Every common divisor of $a$ and $b$ divides $sa + tb = g$, so no common divisor is larger. The [extended Euclidean algorithm](/extended-euclidean-algorithm/) produces $s$ and $t$.

20. The identity function passes the first property. The function that reverses the list and negates every item passes both. Adding `rev([x]) = [x]` fixes `rev` on lists of length 1, and the second property then determines it on all lists by induction.

22. The edges of $M$ have no common ends, so each needs its own vertex of $C$ to cover it, and every matching has at most $|C|$ edges. The checker tests that $M$ is a matching, that every edge has an end in $C$ and that $|M| = |C|$, in $O(V + E)$ time.

23. Invariant: the items read so far can be split into $k$ copies of $c$ and pairs of two different items. A value that is not $c$ appears at most once in each pair, so at most half of the items.

24. For $90 \le n \le 100$, $M(n) = M(M(n + 11)) = M(n + 1)$, so these values all equal $M(101) = 91$. For $n < 90$, use induction on $101 - n$: $M(n + 11) = 91$, and $M(91) = 91$.

25. Use induction on the largest number in the bag, and inside it on how many times the largest number occurs. For the second part, start from the bag $\{2\}$: the first step can put in any number $N$ of 1s, and the process then takes $N + 1$ steps in all.

26. Let $S = \mathbf{if}\ \mathit{true} \to x := 0 \mathbin{[\,]} \mathit{true} \to x := 1\ \mathbf{fi}$, $Q_1$ be $x = 0$ and $Q_2$ be $x = 1$. The program is sure to reach $Q_1 \vee Q_2$, but no starting state makes it sure to reach either one.

27. Invariant: $\exists \alpha, \beta.\ \mathrm{list}(x, \alpha) * \mathrm{list}(y, \beta) \wedge \alpha_0 = \mathrm{rev}(\beta) \cdot \alpha$. At the start $\beta$ is empty; at the end $x = \mathrm{nil}$, so $\alpha$ is empty and $\beta = \mathrm{rev}(\alpha_0)$.

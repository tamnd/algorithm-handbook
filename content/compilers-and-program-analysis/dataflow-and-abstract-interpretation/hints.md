2. Nothing is available at the start of B4: on the path through B2, `a = u - 1` kills both `a + b` and `a * b`, and `u - 1` is computed on one path only. At the end of B1 only `a * b` is very busy, since both B2 and B3 compute it before any operand changes, while B2 changes `a` before B4 computes `a + b`. So `a * b` can be computed once at the end of B1 into a temporary that B2 and B3 use (code hoisting).

4. Live at `head`: $\{i, n, x\}$. Strongly live: $\{i, n\}$. The only read of `x` is in `x = x + 1`, whose result is never used by anything useful, so `x = 0` and `x = x + 1` can both be deleted.

5. Intervals: $x \in [0, 2]$, $y \in [0, 1]$. Octagons add $-1 \le x - y \le 2$ and $1 \le x + y \le 2$. Polyhedra give the segment $x + 2y = 2$, $0 \le x \le 2$. The point $(1, 1)$ is in the box and in the octagon but not on the segment; $(2, 1)$ is only in the box, since $x + y = 3 > 2$.

8. Starting at $\top$: `x` is 1 at `head` and at `exit`, because $1 \sqcap (2 - 1) = 1$ is a fixed point. Starting at $\bot$: `head` gets $1 \sqcap \bot = \bot$ and keeps it, so `x` is not constant at `exit`. Both are fixed points; the optimistic start finds the greatest one.

9. Lines 1, 2, 3, 5, 6, 7, 8 and 10. Only lines 4 and 9, which compute `y`, are left out: `x = 0` reaches line 11 when the loop runs zero times, and lines 7 and 8 depend on the tests at 6 and 5, which read `i` and `n`.

10. Widening gives $(-\infty, 100]$ at the head and $(-\infty, 0]$ at the exit. One narrowing step gives $[-2, 100]$ and $[-2, 0]$, and a second changes nothing. The reduced product of intervals with congruences modulo 3 knows $x \equiv 1 \pmod 3$ at the head and finds $x = -2$ at the exit.

15. The maximal fixed point gives `u` the value $\emptyset$, since `a = 0` kills `a + b` and `u` is its own only predecessor, so the meet at `r` is $\{a + b\} \cap \emptyset = \emptyset$. The only path from `entry` to `r` makes `a + b` available, so the meet over all paths is $\{a + b\}$. The theorem assumes that every block is reachable; remove unreachable blocks first.

16. The maximal fixed point at the start of `L` is $\{y * 2\}$: start from $E$, and `x = y * 2` kills `x + 1` on each turn. At the end of `entry` it is $\{y * 2\} \cap \{x + 1\} = \emptyset$. No path leads from `L` to the end, so the meet over all paths there is $E$, and at the end of `entry` it is $\{x + 1\}$. Only the maximal fixed point is safe: hoisting `x + 1` into `entry` would add a computation to the path into `L`, which never evaluates it.

17. With $n = 2$ the first trip runs line 7 and the second line 8, which writes the final `x`. The dynamic slice is lines 1, 2, 5, 6, 8 and 10. The first method adds lines 3 and 7, which ran and statically reach line 11, though their values were overwritten. For $n = 0$ the dynamic slice is line 3 alone.

20. Follow the definition. It reaches $B$ in pass 1, then $H_d$ and $L_{d-1}$ in pass 2 through the retreating edge $(B, H_d)$. Each further retreating edge $(L_j, H_j)$ delays it one pass, because $L_j$ comes after $H_j$ in the order, so $H_j$ first gets it in pass $d - j + 2$ and $H_1$ and exit in pass $d + 1$. Pass $d + 2$ changes nothing.

21. The cycle through a, b and c is entered at a and at b, and neither dominates the other. The search s, a, b, c gives the order s, a, b, c with retreating edges c→a and c→b; no simple path holds both, so $d = 1$ and the bound is 3 passes. The search s, a, c, b gives the order s, a, c, b with retreating edges c→a and b→c, and the simple path b→c→a holds both, so $d = 2$ and the bound is 4.

22. Since $\gamma \circ \alpha$ is extensive, $f(\gamma(a)) \subseteq \gamma(\alpha(f(\gamma(a))))$. Apply the monotone $g$ and then $\alpha$. Equality holds when $\gamma(\alpha(f(\gamma(a)))) = f(\gamma(a))$ for every $a$, that is, when the image of every abstract value under $f$ is exactly representable. In exercise 6, the box after `y = x` forgets that $y = x$.

24. With call strings, both chains of recursive calls reach the context made of $k$ copies of s3, where $a = 1 \sqcap 2 = \bot$. Its return value $\bot$ flows back to every context whose call at s3 truncates to it, including the ones that start at s1 and at s2, so $\bot$ climbs to both calls in `main`. A summary keyed by the input value calls `f` with $a = 1$ only from inputs with $a = 1$, so its return value is 1.

1. (a) QF_IDL; (b) QF_UFLIA; (c) QF_BV; (d) QF_AX.

2. The classes are $\{a, b\}$, $\{c, f(a), f(b)\}$ and $\{g(f(b)), g(c)\}$: $f(b)$ joins $f(a)$ by congruence, and then $g(f(b))$ joins $g(c)$. The disequality has both sides in one class, so the conjunction is unsatisfiable.

3. The cycle $a \to c \to b \to a$ has weight $-2 - 1 + 2 = -1$. The solver learns $\neg(a - b \le 2) \vee \neg(b - c \le -1) \vee \neg(c - a \le -2)$. The atoms on $d$ play no part.

4. $\mathrm{bvneg}(x) = x$ means $2x = 0$ modulo 16, so $x = 0000$ or $x = 1000$. Since $3 \cdot 11 = 33 = 2 \cdot 16 + 1$, the only solution of $3x = 1$ is $x = 11 = 1011$.

6. With $F_1$ for $f(x)$ and $F_2$ for $f(F_1)$, the result is $F_2 \ne F_1 \wedge F_1 = x \wedge (x = F_1 \rightarrow F_1 = F_2)$, which is unsatisfiable. The second formula needs $\binom{5}{2} + \binom{3}{2} = 13$ constraints.

9. The abstraction $(p_1 \vee p_2) \wedge p_3 \wedge p_4$ has 3 models, with $(p_1, p_2) = (1, 0)$, $(0, 1)$ or $(1, 1)$. Only $(0, 1)$ is consistent, with $x = 5$ or $x = 6$. The lemma $\neg p_1 \vee \neg p_3$, from $x \le 2 \wedge x \ge 3$, blocks both other models.

11. The integer part $1 \le x \le 2 \wedge c_1 = 1 \wedge c_2 = 2$ entails $x = c_1 \vee x = c_2$, and neither equality alone. In each case EUF derives $f(x) = f(c_i)$ by congruence and contradicts a disequality, so the formula is unsatisfiable over the integers. Over the reals, $x = 3/2$ with three distinct values of $f$ is a model.

13. With $b = 3$, $\beta = y$, $a = 2$, $\alpha = y + 1$, the real shadow is $3(y + 1) - 2y \ge 0$, that is $y \ge -3$, which holds. The dark shadow is $y + 3 \ge (a - 1)(b - 1) = 2$, that is $y \ge -1$, which fails. The splinters run over $i$ from 0 to $\lfloor (2 \cdot 3 - 2 - 3)/2 \rfloor = 0$, so only $3z = y$ is tried, and it gives $y = -3$, $z = -1$.

15. Round 1: the example $x = 0$ forces $b = 1$, so the candidate is $a = 0, b = 1$, and the verifier returns $x = 1$. Round 2: the examples force $b = 1$ and $a + b = 3$, so the candidate is $2x + 1$, and the verifier accepts it.

18. The only candidate is $y = \lfloor x/3 \rfloor$, since $3y \le x < 3y + 3$ for that $y$ alone. The condition $x < 3y + 2$ then says that $x \bmod 3$ is 0 or 1. The formula is $\neg(3 \mid x - 2)$.

19. Applying $f$ four times to $f^6(a) = a$ gives $f^{10}(a) = f^4(a)$, so $f^4(a) = a$. Applying $f$ twice to that gives $f^6(a) = f^2(a)$, so $f^2(a) = a$, as in Euclid's algorithm on 6 and 10. The classes are the terms with even and with odd exponent, of sizes 6 and 5. On the domain $\{0, 1\}$, take $a = 0$ and $f(v) = 1 - v$.

20. The weakening is $\exists x \in [-1, 1]\, |x^2 + 1| \le \delta$, and $x^2 + 1 \ge 1$ with equality at $x = 0$, so it is true exactly when $\delta \ge 1$. For $\delta = 1/2$ the weakening is false, so the solver must answer unsat. For $\delta = 1$ the formula is false and its weakening true, so both answers are allowed.

21. Let $g(n) = (n/2)\log_2 n$. For $k \le m$, $g(k + m) - g(k) - g(m) = ((k+m)/2) H(k/(k+m))$, where $H$ is the binary entropy, and $H(p) \ge 2p$ for $p \le 1/2$. So a merge of sizes $k \le m$ costs at most $g(k + m) - g(k) - g(m)$, and induction gives the bound. Merging in rounds of equal pairs reaches it.

22. Over the reals, $x = y = 1/2$. Over the integers, $x = y$ and $2x = 1$ have no solution. The integer argument uses the fact that every row of a difference constraint has one $+1$ and one $-1$, so the matrix is totally unimodular. The row of $x + y$ has two $+1$ entries.

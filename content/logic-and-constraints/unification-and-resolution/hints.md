1. The first three are Horn: $\neg P \vee \neg Q \vee R$ is a rule ($R \leftarrow P, Q$), $\neg P \vee \neg Q$ a goal clause and $R$ a fact. $P \vee Q$ and $\neg P \vee Q \vee R$ have two positive literals each.

3. Bind $x \mapsto y$ first, then $y \mapsto f(z)$: the mgu is $\{x \mapsto f(z),\ y \mapsto f(z)\}$. Adding $z \mapsto a$ gives a unifier that is not most general. For $f(x, x)$ and $f(y, g(y))$, the first arguments give $x \mapsto y$, and the second arguments then ask for $y \doteq g(y)$, which the occurs check rejects.

5. Five: $c$; $g(c, c)$; and $g(c, g(c, c))$, $g(g(c, c), c)$, $g(g(c, c), g(c, c))$.

9. Three. Paramodulate $f(x) = x$ into $P(f(f(c)))$ at $f(f(c))$ with $x \mapsto f(c)$ to get $P(f(c))$, then again with $x \mapsto c$ to get $P(c)$, and resolve with $\neg P(c)$.

12. The roots give $x \sim y$ and $y \sim g(x)$, so one class holds $x$, $y$ and $g(x)$. Its function node $g(x)$ has the argument $x$ in the same class, which is a cycle. Robinson's algorithm binds $x \mapsto y$ and then fails the occurs check on $y \doteq g(y)$.

13. With the recursive clause first, the leftmost goal is always a new `path` atom, so Prolog descends forever and prints no answer. Swapped, it prints $W = b$ and $W = c$ and then runs forever looking for a third answer, because the left-recursive branch still never closes. Breadth-first search finds both answers, and only these two.

16. Round 1 gives $r(a)$ and $r(b)$; round 2 gives $s(a)$; round 3 adds nothing. So two rounds, and the model is $\{p(a), q(b), r(a), r(b), s(a)\}$.

17. The last step of any refutation resolves two complementary unit clauses, and in an input refutation one of them is an input clause; here no input clause is a unit. A linear refutation: $P \vee Q$ with $P \vee \neg Q$ gives $P$; with $\neg P \vee R$ gives $R$; with $\neg P \vee \neg R$ gives $\neg P$; and $\neg P$ with the earlier center $P$ gives $\square$.

19. The minimal solutions $(x', y', z')$ are $(3, 0, 1)$, $(1, 1, 1)$ and $(0, 3, 2)$. A unifier comes from each subset of them in which $x$ and $y$ both get a nonzero sum; five of the seven nonempty subsets qualify.

21. The first is semi-unifiable with $\sigma$ the identity and $\rho = \{x \mapsto g(y),\ y \mapsto g(x)\}$, but the equation needs $y = g(g(y))$. For the second, any $\sigma$ and $\rho$ would give $g(g(y\sigma)) = y\sigma$, so neither problem has a solution.

23. The minimal solutions of $x' + y' = z' + w'$ are the four unit pairs, one for each pair of a left and a right variable, so a unifier is a set of edges of the complete bipartite graph $K_{2,2}$ that touches every vertex. Count these edge covers.

24. A solution of the first problem splits the word $abcd$ into three nonempty parts, and there are $\binom{3}{2} = 3$ ways. For the second, $x\theta$ must begin with $a$, so it is $a$ or $a \cdot w$; compare lengths to get $\{x \mapsto a,\ y \mapsto b\}$ and $\{x \mapsto a \cdot z,\ y \mapsto z \cdot b\}$, which are incomparable because $z$ cannot be empty.

25. Write $F = \lambda u v.\, t$. Since $u$ and $v$ alone give $a$, the body is $g(t_1, t_2)$ with each $t_i$ one of $u$, $v$ and $a$: nine solutions. For $F(F(a))$, the body $t$ of $F = \lambda u.\, t$ cannot be $u$ or $a$; if $t = g(t_1, t_2)$, then each $t_i$ with $u$ substituted by $t[a/u]$ must be $a$, which forces $t_i = a$.

26. When the literals of $C$ share no variables, the matchers of different literals touch disjoint variables and can be combined freely. So $C$ subsumes $D$ exactly when each literal of $C$ matches some literal of $D$, which takes at most $|C| \cdot |D|$ matching calls, each in linear time.

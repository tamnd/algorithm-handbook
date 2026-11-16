1. The three strings are $abab$, which ends in $I$ and is marked, $abaf$, which ends in $D$, and $afra$, which ends in $W$. This agrees with the counts 3 and 1 for length 4 in the entry.

2. "Never repaired" is controllable: $r$ is controllable, so a string without $r$ followed by an uncontrollable event is still without $r$. But after $af$ the plant sits in $D$ with $r$ disabled, an unmarked deadlock, so the closed loop blocks. "Never finishes" is not controllable: $a$ is a legal prefix, $b$ is uncontrollable and $ab \in L(G)$.

3. $x(1) = (5, 3)$, $x(2) = (8, 6)$, $x(3) = (11, 9)$, and in general $x(k) = (3k + 2, 3k)$ for $k \ge 1$. The circuits have means 2, 3 and $(5 + 1)/2 = 3$, so $\lambda = 3$. An eigenvector is $(0, -2)$: $A \otimes (0, -2) = (3, 1)$.

4. The circuits are machine 1 with ratio $3/1$, machine 2 with $4/1$, and the line $t_1 \to t_2 \to t_3 \to t_1$ with $(3 + 4 + 0)/2 = 3.5$. The cycle time is 4, set by machine 2 alone. A third pallet gives the line $7/3$ and changes nothing; one pallet gives 7. A simulation of the recursion fires $t_1$ at $0, 3, 7, 11, 15, \dots$

5. Every state has an outgoing event, and the only unobservable event $f$ lies on no cycle. After $f$ the plant runs $a, b, a, a, \dots$ The observations $a$ and $ab$ also come from the fault-free strings $a$ and $ab$, but $aba$ does not, so $n_f = 3$. A brute force check over all strings up to length 8 confirms that 2 is not enough and 3 is.

6. $\frac{1}{2}(A_1 + A_2) = \begin{bmatrix} -1 & 5 \\ 5 & -1 \end{bmatrix}$ has the eigenvalues $4$ and $-6$, so it is not Hurwitz, and a CQLF would be a Lyapunov function for it.

8. The flight after the $k$-th bounce lasts $2e^k t_1$, so all bounces are over at $t_1 + 2t_1 e/(1 - e) = t_1 (1 + e)/(1 - e) = 9 t_1 \approx 4.06$ s.

10. The product has the states $(0,0)$ to $(4,4)$ and 6 transitions; state 5 is not reached. Round 1 removes $(4,4)$ at line L5, since $G$ can do $v$ there, and then $(3,3)$ at line L6, since it can no longer reach $(0,0)$. Round 2 changes nothing. The result is $(aub)^*$: the supervisor disables $c$ in state 0 and never needs to disable $a$, because after $u$ the event $b$ returns to the marked state without $v$.

12. $LD = (2, -2, 1, -1)$, so $D_c = (-2, 2, -1, 1)$ and $\mu_{c,0} = 2$: $t_1$ takes 2 tokens from the monitor, $t_2$ returns them, and $t_3$, $t_4$ take and return one. The plant reaches the 9 markings with $\mu_2, \mu_4 \in \{0, 1, 2\}$; the closed loop reaches the 4 with $(\mu_2, \mu_4) \in \{(0,0), (1,0), (0,1), (0,2)\}$, and $2\mu_2 + \mu_4 + \mu_c = 2$ holds in each.

13. $LD = (1, -1, 1, -1)$, so the monitor would have to disable the uncontrollable $t_1$. Since $t_1$ can fire whenever $p_1$ is marked and process 1 is always in $p_1$ or $p_2$, process 2 must never enter. The constraint $\mu_1 + \mu_2 + \mu_4 \le 1$ expresses this, with $L'D = (0, 0, 1, -1)$, which is admissible. Its monitor has $D_c = (0, 0, -1, 1)$ and no initial token, so $t_3$ never fires and the closed loop has 2 markings.

14. $L(G) = \{\varepsilon, a, ab, u, ua, uaa\}$. The string $ua$ has the projection $a$ of a string of $K$ but is not in $K$, so $K$ is not normal. $L(G) - K = \{ua, uaa\}$ projects to $\{a, aa\}$, and the strings of $K$ with a prefix of projection $a$ are $a$ and $ab$. So $\sup N(K) = \{\varepsilon, u\}$: the supervisor cannot tell $\varepsilon$ from $u$, so it cannot allow $a$ without allowing $ua$.

16. From $(0, N, 0)$: $(f, -)$ to $(1, F, 0)$ and $(a, a)$ to $(3, N, 3)$. Then $(1, F, 0) \xrightarrow{(a,a)} (2, F, 3) \xrightarrow{(b,b)} (4, F, 5)$, $(3, N, 3) \xrightarrow{(b,b)} (5, N, 5)$, and self-loops $(b, b)$ on $(5, N, 5)$ and $(4, F, 5)$: 6 states and 7 edges. Kahn's algorithm removes $(1, F, 0)$ and $(2, F, 3)$, and the self-loop at $(4, F, 5)$ remains. It stands for $fab^k$ and $ab^k$, which look the same for every $k$.

17. The circuits are $3 \to 3$ with mean 1, $1 \to 2 \to 1$ with mean $5/2$ and $2 \to 3 \to 2$ with mean 4. The graph is strongly connected, so $\lambda = 4$, with the critical circuit $2 \to 3 \to 2$. Column 2 of $((-4) \otimes B)^+$ is $(0, 0, -2)$, and $B \otimes (0, 0, -2) = (4, 4, 2)$. Karp's algorithm finds a minimum mean, so run it on the negated weights.

20. $P_1 A_1 = \begin{bmatrix} -4 & 8 \\ -8 & -1 \end{bmatrix}$, whose symmetric part doubled is $\mathrm{diag}(-8, -2) = -2P_1$, and the same holds for mode 2. So $\lambda_0 = 1$. The ratio $\mu$ is the largest ratio of diagonal entries, 4. Any average dwell time $\tau_a > (\ln 4)/2 \approx 0.693$ s gives GUES.

23. Call a product state bad if $G$ has an uncontrollable event there that the product lacks, and find by a backward search along uncontrollable edges all states from which a bad state is reachable by uncontrollable events alone. Then $\sup C(K)$ is the set of strings whose run never enters these states, found by a forward search that avoids them. A controllable sublanguage of $K$ can contain no string that enters such a state, since the uncontrollable continuation would leave $K$, and the set found is itself prefix-closed and controllable. Each search visits every state and edge once.

24. An entry $A_{ij}$ is the heaviest path in the net from $t_j$ to $t_i$ made of zero-token places and then one one-token place, so it carries exactly one token. A circuit of length $\ell$ in the graph of $A$ is therefore a closed walk of the net with $\ell$ tokens and the same total holding time. Conversely, a circuit of the net with $r \ge 1$ tokens cuts at its token places into $r$ arcs of the graph of $A$, each no heavier than the matching entry. A closed walk splits into elementary circuits, and its ratio is at most the largest of theirs.

25. Write $P_2 = \int_0^\infty e^{A_2^\top t} P_1 e^{A_2 t}\, dt \succ 0$. Since $A_1$ commutes with $e^{A_2 t}$, $A_1^\top P_2 + P_2 A_1 = \int_0^\infty e^{A_2^\top t} (A_1^\top P_1 + P_1 A_1) e^{A_2 t}\, dt = -\int_0^\infty e^{A_2^\top t} e^{A_2 t}\, dt \prec 0$, and $A_2^\top P_2 + P_2 A_2 = -P_1 \prec 0$ by construction.

26. Mode 1 gives $\dot\theta = 1$ and $\frac{d}{dt}\ln r = -1$. Mode 2 gives $\dot\theta = (0.1x^2 + 10y^2)/r^2 \ge 0.1$ and $\frac{d}{dt}\ln r = -(r^2 + 9.9xy)/r^2$. Both turn counterclockwise, so under any signal $\frac{d \ln r}{d\theta} \le g(\theta)$, the larger of the two ratios. The integral of $g$ over one turn is about $-0.272$ (midpoint rule with 200000 points), so $r$ shrinks by at least the factor $e^{-0.272} \approx 0.76$ per turn, and a turn takes at most $20\pi$ time units.

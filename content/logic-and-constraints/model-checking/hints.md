1. $\mathsf{EX}\,q$ holds everywhere, since each state has a successor in $\{2, 3\}$. $\mathsf{AX}\,p = \{3\}$ and $\mathsf{AF}\,q = \{2, 3\}$; the path $(0\,1)^\omega$ never meets $q$. For $\mathsf{EG}\,\neg q$ the iterates are $S$, then $\{0, 1\}$, then $\{0, 1\}$ again, so the answer is $\{0, 1\}$.

2. $\mathsf{F}\,q$ fails on the lasso with empty stem and loop $0\,1$. $\mathsf{G}\mathsf{F}\,p$ fails on stem $0$ and loop $2$. $\mathsf{G}(q \to \mathsf{G}\,q)$ holds, because the only states with $q$ are 2 and 3, and each loops on itself.

8. $\ln 40 \approx 3.689$ and $2\varepsilon^2 = 0.0002$, so $N = \lceil 18\,444.4 \rceil = 18\,445$.

9. The negation is $\mathsf{F}(p \wedge \mathsf{G}\,\neg q)$. Let $r_0$ loop on every letter and move to the accepting state $r_1$ on $p \wedge \neg q$, and let $r_1$ loop on $\neg q$. In the product, $(1, r_1)$ moves to $(0, r_1)$ and back, an accepting cycle reached from $(0, r_0)$ through $(1, r_0)$. The lasso $0\,(1\,0)^\omega$ is a counterexample.

10. The first search finishes 3, then 4, then 2. The second search starts when 2 finishes, follows $2 \to 3 \to 1 \to 2$ and meets the seed: stem $1\,2$, cycle $2\,3\,1\,2$. With accepting set $\{4\}$, the second search starts when 4 finishes and closes the self-loop at once: stem $1\,2\,4$, cycle $4\,4$.

13. With $Z = S$, the inner least fixed point grows $\emptyset$, $\{1, 3\}$, $\{0, 1, 3\}$ and stops. With $Z = \{0, 1, 3\}$ it gives the same set, so two outer iterations suffice. The formula says that some path visits $p$ infinitely often, $\mathsf{E}\,\mathsf{G}\mathsf{F}\,p$; state 2 fails because it can never see $p$ again.

14. Write $x_0 = \tfrac12 + \tfrac12 x_2$ and $x_2 = \tfrac12 x_0$. Then $x_0 = \tfrac23$, so the bound $0.6$ holds and $0.7$ fails.

16. The abstract states are "$x = 1$" and "$x \neq 1$". The move from $x = -1$ to $x = 1$ makes the abstract path of length one from the initial abstract state to the bad one; the concrete run goes $0, 2, 4, \ldots$ and never takes that move. With $x \ge 0$ added, no state with $x \ge 0$ and $x \ne 1$ has a successor with $x = 1$.

17. $t_1$ gives $(0, 1, 0)$, $t_2$ gives $(1, 0, 1)$, which covers the root strictly in $p_3$, so it becomes $(1, 0, \omega)$. Then $(0, 1, \omega)$ and $(1, 0, \omega)$, a repeat. Places $p_1$ and $p_2$ are bounded by 1; $p_3$ is not. $(0, 1, 5)$ is coverable, $(1, 1, 0)$ is not, since $p_1 + p_2 = 1$ always. The reachable markings are $(1, 0, n)$ and $(0, 1, n)$ for all $n \ge 0$.

19. Only $x = 5$ itself is bad, and a predecessor chain into 5 is $\ldots, 7, 1, 3, 5$, which avoids 5 for three states, so the property is not 3-inductive. Four states before 5 would be $5, 7, 1, 3$, which contains 5. The invariant "$x$ is even" is inductive and implies $x \ne 5$.

20. Each clock is $0$, in $(0, 1)$, $1$ or above 1. Of the 16 pairs, the one with both clocks in $(0, 1)$ splits into three regions by the order of the fractional parts, which gives 18. The bound $n!\, 2^n \prod (2c + 2)$ is $2 \cdot 4 \cdot 16 = 128$.

21. The top priority is 4, which is even, so the algorithm first takes the attractor for player 0. $\mathrm{Attr}_0(\{4\}) = \{1, 4\}$, since player 0 at 1 can move to 4. The subgame on $\{0, 2, 3\}$ has top priority 3; player 1 wins it everywhere by staying at 3. Its attractor for player 1 in the whole game is $\{0, 2, 3\}$; player 0 at 0 must enter 3. The rest, $\{1, 4\}$, is won by player 0 with $1 \to 4$, and player 1 wins $\{0, 2, 3\}$ with $3 \to 3$.

22. One direction holds in every system. For the other, show that the relation of trace equivalence is a bisimulation: if $s \xrightarrow{a} s'$ then $a$ is a trace of $t$, so $t$ has its single $a$-successor $t'$, and the traces of $s'$ and $t'$ are the traces of $s$ and $t$ that begin with $a$, with the $a$ removed.

23. Show that $\mathsf{E}[p\,\mathsf{U}\,q]$ is a fixed point and that the $i$-th iterate from $\emptyset$ holds the states with a witness path of length less than $i$. For the greatest fixed point, a state in any fixed point that does not satisfy $q$ satisfies $p$ and has a successor in it, so you can follow it forever or until $q$. One state labelled $\{p\}$ with a self-loop has least fixed point $\emptyset$ and greatest fixed point the whole state set.

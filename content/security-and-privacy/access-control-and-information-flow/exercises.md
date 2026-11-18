In these exercises $l$ is a low (public) variable and $h$ a high (secret) one, both integers, and "noninterfering" means termination-insensitive [noninterference](/noninterference/) unless an exercise says otherwise.

1. ◦ Say which of these programs are noninterfering, and for each one that is not, give two low-equivalent starting states that show the leak.
(a) $l := h \cdot 0 + l$.
(b) $\mathbf{if}\ h = h\ \mathbf{then}\ l := 1\ \mathbf{else}\ l := 0$.
(c) $\mathbf{if}\ l > 0\ \mathbf{then}\ h := 1\ \mathbf{else}\ h := 0$.
(d) $h := h + l;\ l := h - h$.
(e) $\mathbf{if}\ h > 0\ \mathbf{then}\ l := l + 1$.
(f) $l := h \bmod 2$.

2. ◦ For each program, say whether it is termination-insensitive noninterfering and whether it is termination-sensitive noninterfering.
(a) $\mathbf{while}\ h > 0\ \mathbf{do}\ h := h - 1;\ l := 1$.
(b) $\mathbf{while}\ h \ne 0\ \mathbf{do}\ h := h - 1$.
(c) $\mathbf{while}\ l \ne 0\ \mathbf{do}\ l := l - 1$.

3. ◦ The flow-insensitive type system of Volpano, Irvine and Smith gives an expression the highest level of the variables in it, allows $x := e$ only when the level of $e$ is at most the level of $x$, and allows only assignments to high variables inside a branch or loop whose condition is high. Which of the six programs of Exercise 1 does it accept? Which noninterfering programs does it reject?

4. ◦ A static [taint analysis](/taint-analysis/) marks $h$ as tainted at the start and reports when $l$ holds a tainted value at the end. Which of the six programs of Exercise 1 does it report? Which leaking program does it miss, and why?

5. • Write the self-composed program for $P = (\mathbf{if}\ h > 0\ \mathbf{then}\ l := l + 1)$, as in [self-composition](/self-composition/): rename the variables of the two copies, run the copies one after the other, and state the Hoare triple that holds exactly when $P$ is noninterfering. Give a pair of starting values that makes the triple fail.

6. • Take the four levels $\mathit{Low} \le A \le \mathit{High}$ and $\mathit{Low} \le B \le \mathit{High}$, with $A$ and $B$ incomparable. Variable $x$ has level $\mathit{Low}$, $a$ has $A$, $b$ has $B$ and $z$ has $\mathit{High}$. A flow check allows a command when every flow goes upward in the lattice: from the variables on the right of an assignment to the variable on its left, and from the variables of a condition to every variable assigned under it. Which of these commands does it allow? (a) $z := a + b$. (b) $a := b$. (c) $a := x$. (d) $x := a - a$. (e) $\mathbf{if}\ a > 0\ \mathbf{then}\ b := 1$. (f) $\mathbf{if}\ x > 0\ \mathbf{then}\ a := 1\ \mathbf{else}\ z := 2$.

7. • A program writes to a public output channel during the run: $\mathit{out}(h);\ l := 0$. Show that it satisfies the definition of noninterference in the entry, which looks only at final states, and say how the definition must change to reject it.

8. • (a) Prove that if $P_1$ and $P_2$ are noninterfering, then so is $P_1;\ P_2$. (b) Show by an example that $P_1$ and $P_2$ noninterfering do not make $\mathbf{if}\ h > 0\ \mathbf{then}\ P_1\ \mathbf{else}\ P_2$ noninterfering.

9. ★ The entry shows that noninterference is undecidable and that the set of programs that are not noninterfering is recursively enumerable. Prove that the set of noninterfering programs is not recursively enumerable. Conclude that no proof system in which proofs can be checked by an algorithm has a proof for every noninterfering program.

10. ★ Let $h \in \{0, 1\}$ and let $\square$ be nondeterministic choice. Show that $Q = (l := h)\ \square\ (l := 1 - h)$ satisfies possibilistic noninterference. Then show that the program obtained from $Q$ by always taking the left branch leaks $h$, although it has fewer behaviours than $Q$. What does this say about refining a secure nondeterministic specification into a deterministic program?

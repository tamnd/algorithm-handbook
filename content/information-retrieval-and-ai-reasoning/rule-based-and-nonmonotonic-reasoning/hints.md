1. The least model is $\{a, b, c, d, e\}$; only $f \leftarrow g$ never fires. Backward chaining calls $d$, $c$, $a$, $b$, $e$ and then $a$ again, which the table answers at once. The atoms $f$ and $g$ are never touched, while forward chaining would still test the rule $f \leftarrow g$.

3. The reduct by $\{a, c\}$ is $\{a,\ c,\ d \leftarrow d\}$: the rule for $b$ is deleted because $a \in M$. Its least model is $\{a, c\}$, so $M$ is stable. The only other stable model is $\{b, c\}$. Since $d$ can only support itself, $d$ is false and $c$ true in every stable model, and the well-founded model has exactly these values, with $a$ and $b$ undefined.

7. $R_1$ gives $0.8 \cdot \min(0.9, 0.5) = 0.4$, $R_2$ gives $0.3$, $R_3$ gives $-0.6$, and $R_4$ does not fire, since $\max(0.15, 0.1) = 0.15$ is below $0.2$. Then $0.4 \oplus 0.3 = 0.58$ and $0.58 \oplus (-0.6) = -0.02 / 0.42 \approx -0.048$. The other order gives $0.3 \oplus (-0.6) = -0.3 / 0.7$ and then $(0.4 - 0.4286) / 0.6 \approx -0.048$.

8. The minimal hitting sets are $\{M_1, M_2\}$, $\{M_1, A_2\}$, $\{M_2, A_2\}$ and $\{A_1, A_2\}$. No component is in all three conflicts, so no single fault explains the observations.

10. Now $u$ depends on $p$, $p$ negatively on $q$, $q$ on $r$, $r$ negatively on $t$ and $t$ negatively on $u$: a cycle through negation, so the program is not stratified. It has no stable model, its completion has the single model $\{s, t, q\}$, and the well-founded model makes $s$ true and leaves every other atom undefined. In $\{s, t, q\}$ the atom $r$ is false, so $q$ is supported only by $q \leftarrow q$, and the least model of the reduct is $\{s, t\}$.

11. The pairs are $(\emptyset, \{a, b, c, e, f, g\})$, $(\{c\}, \{a, c, e, f, g\})$ and $(\{a, c\}, \{a, c, e, f, g\})$, and the next step repeats $K = \{a, c\}$. So $a, c$ are true, $b, d$ are false and $e, f, g$ are undefined. The only rule for $e$ is $e \leftarrow \mathit{not}\ e$: if $e \in M$ the reduct deletes it, and if $e \notin M$ the reduct derives $e$. So no stable model exists.

13. R4 on the constraint makes $a$ true, and R3 then makes $b$ true, since $a \leftarrow b$ is the only live rule for $a$. ATMOST finds an empty upper closure, because $a$ and $b$ only support each other, so both become false: a conflict at the root, with no guess. A completion-based solver returns $\{a, b\}$.

17. Each extension is $\mathrm{Th}$ of the conclusions of the defaults that apply, and $c$ comes only from $: \neg a / c$. If $a \in E$, that default is blocked, so $c \notin E$, so $: \neg c / b$ applies and $b \in E$, which blocks $: \neg b / a$, and $a \notin E$ after all. If $a \notin E$, then $c \in E$, $b \notin E$ and $a \in E$. Both cases contradict, as for the odd loop $a \leftarrow \mathit{not}\ b$, $b \leftarrow \mathit{not}\ c$, $c \leftarrow \mathit{not}\ a$. With $W = \{c\}$ the only extension is $\mathrm{Th}(\{a, c\})$.

19. Minimize the abnormalities in each model. A minimal set is either $\{\mathit{ab}_{\mathit{alive}, k+1}\}$, where the gun stays loaded and the shot kills, or $\{\mathit{ab}_{\mathit{loaded}, j}\}$ for one wait step $j \in \{1, \ldots, k\}$, where the gun unloads during that wait. That gives $k + 1$ sets. Chronological minimization prefers the abnormality as late as possible, so it keeps the intended one.

23. A loop is a set $\{a_i, \ldots, a_j\}$ with $i < j$, so there are $n(n - 1)/2$. The completion forces all atoms to have the same value, so its models are $\emptyset$ and the set of all atoms; only $\emptyset$ is stable. Every loop except the whole set has an external rule from $a_{i-1}$ or $a_{j+1}$, which is true in the full model, so only the loop formula of the whole set, $a_1 \vee \cdots \vee a_n \rightarrow \bot$, is violated.

24. Layer 0 is $\{b \to f\}$, layer 1 is $\{p \to b, p \to \neg f\}$ and layer 2 is $\{s \to p, s \to f\}$: no world verifies a penguin rule without breaking $b \to f$ or the other penguin rule. The best super penguin is a flying penguin bird, which breaks only $p \to \neg f$ and has rank 2, while a super penguin that does not fly breaks $s \to f$ and has rank 3: so $s \mathrel{|\!\sim} f$. A super penguin that is no bird breaks $p \to b$ and $p \to \neg f$, also rank 2, so $\kappa_Z(s \wedge b) = \kappa_Z(s \wedge \neg b) = 2$ and $s \mathrel{|\!\sim} b$ fails: the broken rule $p \to \neg f$ drowns $p \to b$ in its layer.

25. Both have the single stable model $\{a\}$. Compare the SE-models with second component $\{a, b\}$: the reduct of $P$ by $\{a, b\}$ is $\{a \leftarrow b\}$, which $\emptyset$ satisfies, while $Q$ needs $a$. Case 2 of the proof gives $R = \{a \leftarrow b,\ b \leftarrow a\}$; then $Q \cup R$ has the stable model $\{a, b\}$ and $P \cup R$ has none.

26. The rules are $x_1 \vee x_1'$, $x_2 \vee x_2'$, $y \vee y'$, $y \leftarrow w$, $y' \leftarrow w$, one rule for $w$ per term and $w \leftarrow \mathit{not}\ w$: eight in all. Only $x_1 = x_2 = 1$ makes the formula true for both values of $y$, so the only answer set is $\{x_1, x_2, y, y', w\}$. The positive program has five answer sets, its minimal models, and only that one contains $w$.

27. Let the iteration stop with $(K, U)$. Two-valued means $K = U = T$. Every stable model $M$ lies between them, so $M = T$, which gives uniqueness. For existence, $K = S(U)$ and $U = S(K)$ give $S(T) = T$, which is the definition of a stable model.

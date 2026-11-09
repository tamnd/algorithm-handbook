1. The positions are $\varepsilon$, $1$, $1.1$, $1.2$, $2$ and $2.1$. The subterm at $2.1$ is $x$. There are 5 distinct subterms: the term itself, $g(x, a)$, $h(x)$, $x$ and $a$, since $x$ occurs twice.

3. Every term on the way has exactly one redex. Three steps use the second rule and one uses the first, so there are 4 steps, and the normal form is $s(s(s(s(s(0)))))$.

4. The only overlap puts the left side inside itself at position 1: $h(h(h(x)))$ rewrites to $h(x)$ at the root and to $h(x)$ at position 1. The critical pair $\langle h(x), h(x) \rangle$ is trivial, and each step removes two symbols, so the system terminates and is confluent by the critical pair lemma and Newman's lemma. $h^7(a)$ normalizes to $h(a)$.

6. Yes: keep one $4$, remove $\{4, 1\}$ and add $\{3, 3, 3, 2\}$, each below $4$. And $\{3\} >_{\mathrm{mul}} \{2, 2\}$, not the other way, because nothing in $\{2, 2\}$ dominates $3$.

8. Each step deletes one $a$ that stands before a $b$, and all five $a$'s do. The normal form is $bb$, reached in 5 steps.

10. In both orderings the roots are equal, so the arguments are compared from the left: $x \cdot y$ is greater than $x$ as a proper superterm, and for KBO the weights and variable counts of the two sides are equal. In the other direction the first arguments are $x$ and $x \cdot y$, and $x$ is smaller.

12. Termination: each step either shortens the word or keeps its length and removes an inversion $ba$. The self-overlaps of $aaa$ join at once; the only other overlap is $baaa$, which reaches $b$ both ways. Normal forms are $a^i b^j$ with $i < 3$, so two words are equal iff they have the same number of $b$'s and numbers of $a$'s congruent modulo 3. The first pair is equal; the second is not, since $abab \to^* aabb$ and $aabbaa \to^* abb$.

13. Five: $\{x\}$ for $b$ and for $f$-nodes with neither condition, $\{x, a\}$ for $a$, and for $f$-nodes $\{x, f(x, a)\}$, $\{x, f(a, y)\}$ and $\{x, f(x, a), f(a, y)\}$.

18. $G$ has a strict arc from $x$ to $y$ and a non-strict arc from $y$ to $x$. Then $G^2$ has strict arcs $x \to x$ and $y \to y$, $G^3$ has strict arcs $x \to y$ and $y \to x$, and $G^4 = G^2$. The closure is $\{G, G^2, G^3\}$, its only idempotent graph is $G^2$, which has strict self-loops, so the function terminates.

20. $a$ and $d$ are normal forms, $b \to a$ and $c \to d$, so every element has a normal form. The two peaks $a \leftarrow b \to c$ and $b \leftarrow c \to d$ are joined through $a$ and $d$. But $b$ reaches both $a$ and $d$. Termination fails: $b \to c \to b$.

21. For the hard direction, take a non-terminating term all of whose proper subterms terminate. An infinite reduction from it must rewrite at the root, and since the rules are ground, the term first reduces to a left side $l_1$. Then $r_1$ does not terminate; repeat with a minimal non-terminating subterm of $r_1$. Some rule appears twice in the sequence $l_1, l_2, \ldots$, which gives the cycle.

22. The pattern $t_i$ matches a node exactly when, after $i - 1$ steps to the right child, the node reached is an $f$-node whose left child is $a$. Build a right comb of $n$ $f$-nodes and put $a$ or $b$ as each left child to realize every subset.

23. Show the strong form of commutation: if $M \to_\eta N_1$ and $M \to_\beta N_2$, then $N_1 \to_\beta^{=} P$ and $N_2 \to_\eta^* P$ for some $P$, by cases on the relative positions of the two redexes. The Hindley-Rosen lemma then gives confluence of the union, since $\beta$ and $\eta$ are each confluent.

24. Each step decreases the value of the term, a natural number, by at least 1. With polynomials of degree at most $d$ and coefficients at most $c$, the value of a term of depth $h$ is at most $C^{d^h}$ for a constant $C$. The Ackermann term $\mathit{ack}(s^k(0), s^k(0))$ has size $O(k)$, but its innermost reduction has at least $A(k, k) - k$ steps, by induction along the recursion of the Ackermann function, and $A(k, k)$ outgrows $2^{2^{ck}}$ for every constant $c$.

25. Induction on $|s| + |t|$. Compare $s$ with each argument of $t$, and $t$ with each argument of $s$; if one is at least the other term, the subterm case decides. Otherwise all arguments are below the other term, and the precedence decides if the roots differ, the lexicographic comparison if they are equal.

1. ◦ List the positions of the term $f(g(x, a), h(x))$, give the subterm at position $2.1$, and count its distinct subterms.

2. ◦ Find a matching substitution, or show that none exists, for the pattern $f(x, g(y))$ and the subject $f(a, g(h(b)))$, for $f(x, x)$ and $f(a, b)$, and for $f(x, x)$ and $f(g(a), g(a))$.

3. ◦ With the rules $0 + y \to y$ and $s(x) + y \to s(x + y)$, how many steps does it take to normalize $s(s(s(0))) + s(s(0))$, whatever redex is chosen at each step? What is the normal form?

4. ◦ Find the critical pairs of the one-rule system $\{h(h(x)) \to x\}$ and decide whether it is confluent. What is the normal form of $h^7(a)$?

5. ◦ In the abstract reduction system with $a \to b$, $b \to a$ and $a \to c$, which elements have a normal form? Is the system terminating, weakly normalizing, confluent?

6. ◦ Over the natural numbers, decide whether $\{4, 4, 1\} >_{\mathrm{mul}} \{4, 3, 3, 3, 2\}$, and compare $\{2, 2\}$ with $\{3\}$ in the multiset ordering.

7. ◦ With the precedence $* > +$, show that the lexicographic path ordering orients $x * (y + z) \to x * y + x * z$.

8. ◦ Normalize the word $aaabaab$ with the one-rule string rewriting system $\{ab \to b\}$. How many steps does it take?

9. ◦ In combinatory logic, with $K\,x\,y \to x$ and $S\,x\,y\,z \to x\,z\,(y\,z)$, reduce $S\,K\,x\,y$ to normal form and count the steps.

10. • Show that both the lexicographic path ordering and the Knuth-Bendix ordering orient associativity $(x \cdot y) \cdot z \to x \cdot (y \cdot z)$, whatever the precedence and the admissible weights, and that neither orients the rule in the other direction.

11. • With $0 + y \to y$ and $s(x) + y \to s(x + y)$, find by narrowing all solutions of $x + y \approx s(0)$ in which $x$ and $y$ are ground terms.

12. • Show that the string rewriting system $\{aaa \to \varepsilon,\ ba \to ab\}$ is terminating and confluent. Use it to decide whether $abaab$ and $bb$ are equal in the monoid it presents, and whether $abab$ and $aabbaa$ are.

13. • The patterns $f(x, a)$ and $f(a, y)$ are to be matched over the signature with a binary $f$ and constants $a$ and $b$. How many different match sets does the bottom-up Hoffmann-O'Donnell matcher need?

14. • With the rules $f(x, y) \to x$ and $a \to b$, normalize $f(a, a)$ by leftmost-innermost and by leftmost-outermost reduction, and count the steps of each.

15. • A system has unique normal forms if no element reduces to two different normal forms. Show that $a \to b$, $a \to c$, $c \to c$ has unique normal forms but is not confluent.

16. • Show that $x \cdot (y \cdot x) \approx (x \cdot y) \cdot x$ follows from associativity alone, and that $x \cdot y \approx y \cdot x$ does not, by giving an associative operation on two elements that is not commutative.

17. • Find the critical pairs of $\{h(x, k(y)) \to x,\ k(a) \to b\}$, decide whether the system is orthogonal, and decide whether it is confluent.

18. • The function $f(x, y) = \textbf{if } x = 0 \textbf{ then } y \textbf{ else } f(y, x - 1)$ on the natural numbers has one recursive call. Draw its size-change graph $G$, compute the closure of $\{G\}$ under composition, and decide whether the size-change principle proves termination.

19. • Insert the patterns $f(x, a)$, $f(a, y)$ and $f(a, a)$ into a discrimination tree. How many nodes does it have, counting the root? Which patterns are returned as candidates for the queries $f(a, a)$, $f(b, a)$ and $f(a, b)$?

20. • Show that the abstract reduction system $b \to a$, $b \to c$, $c \to b$, $c \to d$ is weakly normalizing and locally confluent but not confluent. Which hypothesis of Newman's lemma fails?

21. ★ Let $R$ be a finite term rewriting system whose rules are all ground. Prove that $R$ is not terminating if and only if some rule $l \to r$ of $R$ satisfies $r \to^* C[l]$ for some context $C$.

22. ★ Over a binary $f$ and constants $a$ and $b$, let $t_1 = f(a, x_1)$ and $t_i = f(x_i, t_{i-1})$ for $2 \le i \le n$. Show that the bottom-up matcher for the patterns $t_1, \ldots, t_n$ needs at least $2^n$ match sets, although the patterns have total size $O(n^2)$.

23. ★ Prove that $\beta$-reduction and $\eta$-reduction in the untyped lambda calculus commute, and conclude that $\beta\eta$-reduction is confluent.

24. ★ Suppose a polynomial interpretation over the natural numbers proves termination of a finite system. Prove that every reduction from a term of size $n$ has $2^{2^{O(n)}}$ steps at most, and conclude that no polynomial interpretation proves termination of the Ackermann function written as a rewrite system.

25. ★ Prove that the lexicographic path ordering with a total precedence is total on ground terms: for distinct ground terms $s$ and $t$, either $s >_{\mathrm{lpo}} t$ or $t >_{\mathrm{lpo}} s$.

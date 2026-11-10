1. ◦ Write the truth table of $f(x_1, x_2, x_3) = x_1 \oplus (x_2 \wedge x_3)$ as a string $f(0) f(1) \cdots f(7)$, where entry $a$ has $x_j$ equal to bit $j - 1$ of $a$, as in [Boolean function](/boolean-function/). How many models does $f$ have?

2. ◦ For the same $f = x_1 \oplus (x_2 \wedge x_3)$, compute the [cofactors](/cofactor/) $f|_{x_2=0}$ and $f|_{x_2=1}$ and the Boolean difference with respect to $x_2$. Does $f$ depend on $x_2$?

3. ◦ Write the positive Davio expansion of $f = x_1 \vee x_2$ with respect to $x_1$, as a formula in $x_1$, $x_2$, $\oplus$ and $\wedge$, and check it on all four inputs.

4. ◦ Draw the [reduced ordered BDD](/reduced-ordered-bdd/) of the multiplexer $f = (x_1 \wedge x_2) \vee (\neg x_1 \wedge x_3)$ in the order $x_1, x_2, x_3$, and again in the order $x_2, x_3, x_1$. How many nodes does each have, counting the two terminals?

5. ◦ The ROBDD of $f = x_1 \vee x_3$ over the variables $x_1, x_2, x_3$ has no node for $x_2$. Run [model counting](/bdd-satisfy-count/) on it by hand, with the factor $2^k$ for skipped levels, and check the answer against the truth table.

6. ◦ Counting terminals, how many nodes does the ROBDD of the constant function 1 have? Of a single variable $x_i$? Of $x_1 \wedge x_2 \wedge \cdots \wedge x_n$?

7. ◦ Write $f \vee g$, $f \oplus g$ and $f \to g$ each as one call of the [ITE operator](/ite-operator/), using only $f$, $g$, $\neg g$ and the constants.

8. ◦ Let $f = (x_1 \wedge x_2) \vee (\neg x_2 \wedge x_3)$. Compute $\exists x_2\, f$ and $\forall x_2\, f$ as in [BDD quantification](/bdd-quantification/).

9. • Let $E_n(x, y) = \bigwedge_{i=1}^{n} (x_i \leftrightarrow y_i)$ say that two $n$-bit words are equal. Count the nodes of its ROBDD, terminals included, in the interleaved order $x_1, y_1, \ldots, x_n, y_n$ and in the order $x_1, \ldots, x_n, y_1, \ldots, y_n$.

10. • A function is symmetric if its value depends only on the number of 1s in the input. Show that under every [variable order](/variable-ordering/) the ROBDD of a symmetric function of $n$ variables has at most $n(n+1)/2$ inner nodes.

11. • In the order $x_1, x_2, x_3$, take the ROBDDs of $f = x_1 \oplus x_2$ and $g = x_2 \oplus x_3$ and compute $f \wedge g$ with [APPLY](/bdd-apply/). Give the result as a list of nodes. How many nodes does it have, terminals included, and how many models?

12. • Use the identity of [BDD compose](/bdd-compose/) to compute $f[x_1 := g]$ for $f = x_1 \wedge x_2$ and $g = x_2 \oplus x_3$. Give the result as a formula and the size of its ROBDD in the order $x_1, x_2, x_3$, terminals included.

13. • Over the elements $1, 2, 3, 4$ in this order, take the family $\{\{1\}, \{3\}\}$. Count the nodes, terminals included, of the [zero-suppressed BDD](/zero-suppressed-bdd/) of the family and of the ROBDD of its characteristic function $\chi(x_1, x_2, x_3, x_4)$.

14. • With [complemented edges](/complemented-edges/) in the convention of Brace, Rudell and Bryant, how many nodes does the parity function $x_1 \oplus \cdots \oplus x_n$ need, terminals included? Compare with the $2n + 1$ nodes of its plain ROBDD.

15. • Show that the ROBDD of a function of $n$ variables has at most $\min(2^{k-1},\ 2^{2^{n-k+1}} - 2^{2^{n-k}})$ nodes on level $k$. Use this to show that every function of 4 variables has an ROBDD of at most 11 nodes, terminals included.

16. • Use model counting on the ROBDD in the natural order to find the number of models of $x_1 x_2 \vee x_3 x_4 \vee x_5 x_6$. Check the number by a counting argument that does not use the diagram.

17. • Let $x = x_1 \cdots x_n$ and $y = y_1 \cdots y_n$ be two words with $x_1$ and $y_1$ the most significant bits, and let $G_n$ be the function $[x > y]$. Show that in the order $x_1, y_1, x_2, y_2, \ldots, x_n, y_n$ its ROBDD has exactly $3n + 1$ nodes, terminals included.

18. ★ The multiplexer with $k$ address bits $a_1, \ldots, a_k$ and $2^k$ data bits $d_0, \ldots, d_{2^k - 1}$ outputs the data bit whose index is the address. Show that its ROBDD has exactly $2^{k+1} + 1$ nodes, terminals included, when all address bits come before the data bits, and at least $2^{2^k}$ nodes when all data bits come first.

19. ★ Prove that every Boolean function of $n$ variables has a reduced ordered BDD with $O(2^n / n)$ nodes in every order, by splitting the levels into a top part and a bottom part and bounding each with the counts of Exercise 15.

20. ★ Prove the lemma behind the [Friedman–Supowit algorithm](/friedman-supowit-ordering/): in the ROBDD of $f$, the number of nodes on the level of a variable $x_i$ depends only on $x_i$ and on the set of variables above it, not on their order. Then explain how the lemma gives a dynamic program over subsets of the variables.

21. ★ Show that the ZDD of the family of all $k$-element subsets of $\{1, \ldots, n\}$, with $1 \le k \le n$ and the elements in their natural order, has exactly $k(n - k + 1)$ inner nodes.

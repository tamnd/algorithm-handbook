1. ◦ Run [Andersen's analysis](/andersen-analysis/) on the program `a = &x; b = &y; p = &a; q = &b; c = *p; *q = a; d = c`. Give the points-to set of every variable. Which statement puts $x$ into $pts(b)$? May `*p` and `*q` be aliases?

2. ◦ Run [Steensgaard's analysis](/steensgaard-analysis/) on the program of Exercise 1. Give the classes of locations and the set of every variable. Which variables get a larger set than under Andersen's analysis, and which single statement causes the loss?

3. ◦ Read the program of Exercise 1 as straight-line code, and analyze it [flow-sensitively](/flow-sensitivity/), with a strong update at a store whose pointer has exactly one target. Give the sets after the last statement. Which variable differs from Andersen's answer, and why is the strong update sound here?

4. ◦ Classes `B` and `C` extend `A`, and `D` extends `B`. Class `A` has a field `f` of type `A`. The variables are `B b; C c; A a; A t;` and the statements are (0) `b = new B`, (1) `c = new C`, (2) `a = c`, (3) `b.f = a`, (4) `c.f = c`, (5) `t = a.f`. For each pair of the references in statements 3, 4 and 5, say whether TypeDecl, FieldTypeDecl and SMTypeRefs of [type-based alias analysis](/type-based-alias-analysis/) report a may-alias. Then add the statement `a = b` and say what changes.

5. ◦ Use the classes of Exercise 4, where `A` defines methods `m` and `n`, `B` defines `m`, `C` defines `m` and `n`, and `D` defines `n`. The method `main` runs `A x = new B(); x.m(); B y = new D(); y.n(); A u = x; u = y; u.n();`, with call sites s1, s2 and s3, and `B.m` runs `A z = new C(); z.n();`, with call site s4. Build the call graph by [class hierarchy analysis](/class-hierarchy-analysis/) and by [rapid type analysis](/rapid-type-analysis/). Count the edges and the reachable methods of each. Which edge does rapid type analysis add only after it has reached `B.m`?

6. ◦ Run [0-CFA](/zero-cfa/) on `let wrap = fun f -> fun v -> f v in let inc = fun x -> x + 1 in let dbl = fun y -> y * 2 in let g1 = wrap inc in let g2 = wrap dbl in g1 3`. Which functions may the call `f v` reach, and which does it reach in the run? Show that [1-CFA](/k-cfa/) finds only the real target. Which part of the abstract value of `g1` makes the difference?

7. ◦ Java code has `class Node { Object val; Node next; }` and runs `Node n1 = new Node(); Node n2 = new Node(); n1.next = n2; n1.val = new A(); n2.val = new B(); Node m = n1.next; Object v = m.val; Object w = n1.val;`, with allocation sites $o_1$ to $o_4$ in this order. Give the sets of `m`, `v` and `w` in the three models of [field sensitivity](/field-sensitivity/): field-sensitive, field-insensitive and field-based. Which model is right for each variable?

8. ◦ Run [offline variable substitution](/offline-variable-substitution/) on `p = &a; q = p; r = q; r = &b; s = r; t = s; s = t; u = *t; v = q; v = t; w = v; x = y`. Give the label of every variable and the groups. Do $r$ and $v$ have equal Andersen sets? Do they get one label, and why does the method not need them to?

9. ◦ A Java program has a global `static Node g`. The method `build()` runs `Node a = new Node(); Node b = new Node(); a.next = b; return a;` (sites $s_1$ and $s_2$), and `run()` runs `Node c = build(); Node d = new Node(); d.next = c.next; Node e = new Node(); g = e;` (sites $s_3$ and $s_4$). Give the [escape](/escape-analysis/) state of each site. What changes if `run` ends with `g = d` instead of `g = e`?

10. ◦ Globals $g$, $h$ and $k$. The procedures are `main() { local x; call p(x) }` (site s1), `p(a) { g = 1; call q(a, h) }` (site s2), `q(b, c) { c = b; call p(b); call r() }` (sites s3 and s4) and `r() { k = 0 }`; parameters pass by reference. Compute GMOD for each procedure and DMOD for each site by the three steps of Cooper and Kennedy in [mod-ref analysis](/mod-ref-analysis/), and check the result against Banning's equation. Is $x$ modified by the call at s1?

11. • Steensgaard's analysis with pending lists, and a variant that gives a pointer with no target a fresh empty target class at once, both run on `p = q; p = &a; r = q`. Give the two results and Andersen's. Show that both variants keep the property that any two sets are equal or disjoint, and say why Steensgaard added the pending lists.

12. • Give a program of $O(n)$ statements on which Andersen's analysis must output $\Theta(n^2)$ points-to pairs. How large is Steensgaard's result for it, stored as classes and one target per class? Show that offline variable substitution shrinks your program so that the solver itself stores only $O(n)$ pairs.

13. • For the program `p_i = &a_i` and `c = p_i` for $i = 1, \ldots, n$, count the pairs $(*p_i, *p_j)$ with $i \ne j$ that Andersen's analysis, Steensgaard's analysis and [one-level flow](/das-one-level-flow/) report as may-aliases. Then add `a_i = &b_i` for each $i$, and do the same for the pairs $(*a_i, *a_j)$.

14. • Show that for programs whose statements all have the forms `p = &a` and `p = q`, Andersen's analysis is a [graph reachability](/graph-reachability/) problem, and solve it in $O(n(n + m))$ time. Then reduce [transitive closure](/transitive-closure/) to it, so that this case is exactly as hard as transitive closure.

15. • Take the graph with nodes $s$, $a$, $b$ and $t$ and edges $s \to a$, $a \to s$, $s \to t$ and $a \to t$, and build the program of the [NP-hardness proof](/flow-insensitive-alias-np-hardness/): `u = &v` for each edge $(u, v)$ with $u \ne t$, and `r = **s`. Find the set of $r$ under Andersen's analysis and under the precise flow-insensitive semantics. Then add the edges $a \to b$ and $b \to t$ and do it again.

16. • A loop body `r = p; p = alloc` runs at least twice, with one allocation site $h$, and then the program runs `t = &x; *r = t; u = &y; *p = u; s = *r`. A flow-sensitive analysis does a strong update at a store whose pointer has one abstract target. What does it give for $pts(s)$, and what does the run give? State the condition under which a strong update is sound, and fix the analysis.

17. • Run [variable type analysis](/variable-type-analysis/) on the program of Exercise 5, starting from the rapid type analysis call graph. List the edges and reachable methods that it keeps. Which edge of rapid type analysis does each assignment `u = x` and `u = y` keep alive?

18. • Two programs differ in one store: `p = &a; p = &b; q = p; x = *p; *q = x; a = &c` and the same with `*p = x` in place of `*q = x`. For each, build the offline graph of [hybrid cycle detection](/hybrid-cycle-detection/), say what its table records, and which merges happen offline, by the hybrid rule and by the lazy check. Check that the final sets are Andersen's. How does offline variable substitution change the first program?

19. • Fix $k \ge 0$. Build a program in which a function `id` is called only inside a chain of $k$ wrappers, and `main` calls the outer wrapper twice with different functions. Show that [k-CFA](/k-cfa/) gives a spurious call edge on this program and that $(k+1)$-CFA does not. What does this say about choosing $k$ ahead of time?

20. • In the cloning approach of Whaley and Lam ([BDD-based points-to analysis](/bdd-points-to-analysis/)), a context of a method is an acyclic call path from `main`. Count the contexts of each method when $m_0$ is `main` and each $m_i$ calls $m_{i+1}$ from two call sites, for $i < k$. How are recursive calls treated, and why can a BDD hold the facts of $2^k$ contexts in small space?

21. • Prove that each of Steensgaard's sets contains Andersen's set for the same variable: show that the result of Steensgaard's analysis satisfies the four subset constraints. Prove also that two of its sets are equal or disjoint.

22. • Query the program of Exercise 1 with [demand-driven points-to analysis](/demand-driven-points-to/), first for $d$ and then for $b$. Which variables does each query demand, and why does the query for $d$ demand $q$ although $q$ never reaches $d$?

23. ★ Prove that for programs whose statements all have the forms `p = &a` and `p = q`, Andersen's answer equals the precise flow-insensitive answer: every fact $a \in pts(p)$ that it reports holds after some run.

24. ★ Show that the restricted problem in the NP-hardness proof, with statements `u = &v` and one statement `r = *^k s`, is in NP, so that it is NP-complete. Why does the same certificate not work when the program has statements of the form `*u = &v`?

25. ★ Prove that the hybrid merge of [hybrid cycle detection](/hybrid-cycle-detection/) never changes the least solution: if the offline graph has a cycle through the ref node $*a$ and the variable $b$, and every other ref node on it belongs to a pointer with a non-empty set, then every $x \in pts(a)$ has the same least set as $b$.

26. ★ Prove that the result of Steensgaard's analysis with pending lists does not depend on the order of the statements. Characterize the result as the finest partition with a target map that satisfies closure conditions, one for each kind of statement.

27. ★ Prove that the three steps of Cooper and Kennedy in [mod-ref analysis](/mod-ref-analysis/) give the least solution of Banning's equation for programs without nested procedures. Why can the formals not be propagated over the strongly connected components of the call graph as the globals are?

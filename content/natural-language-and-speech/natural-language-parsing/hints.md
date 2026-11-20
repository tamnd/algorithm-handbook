1. There are $4^2 = 16$ trees, $3^2 = 9$ with one root child, and 12 projective ones. The four non-projective trees are $(0, 0, 1)$, $(2, 0, 1)$, $(3, 0, 0)$ and $(3, 0, 2)$; in each, the arc between words 1 and 3 passes over word 2, whose head lies outside that arc.

3. Arc-standard, with LA making the top of the stack the head of the item below it and RA the reverse: SH SH LA SH RA SH RA RA, 8 moves $= 2n$. Arc-eager, with LA making the front of the buffer the head of the top of the stack and RA attaching the front of the buffer to the top and pushing it: SH LA RA RA RE RA, 6 moves, ending with the buffer empty.

4. With the full stop: UAS $5/6$ and LAS $4/6 = 2/3$ (*him* has the wrong label, *book* the wrong head). Without it: UAS $4/5$ and LAS $3/5$.

5. Both trees have 6 brackets. Labelled, 4 match (S, the subject NP, the VP and NP over *the talk*), so $P = R = F_1 = 2/3$. Unlabelled, the span of *after the talk* matches too, and $P = R = F_1 = 5/6$.

6. Application: *likes Mary* is S\NP by forward application, and *John* with it is S by backward application. Type raising gives *John* the category S/(S\NP); forward composition with (S\NP)/NP gives S/NP for "John likes", and forward application to *Mary* gives S.

8. Both graphs have 5 triples. The mapping $x \to s$, $y \to b$, $z \to g$ matches the three instance triples; the mapping $x \to s$, $y \to g$, $z \to b$ matches *see-01* and both role triples. Each gives $M = 3$, so Smatch is $2 \cdot 3/(5 + 5) = 3/5$, and the best mapping is not unique.

10. Attaching the PP to the VP gives $0.2 \cdot 0.3 \cdot 0.7 \cdot 0.4 \cdot 0.2 = 0.00336$; attaching it to *fish* gives $0.2 \cdot 0.7 \cdot 0.2 \cdot 0.4 \cdot 0.2 = 0.00224$. The parser returns the VP attachment, with posterior $0.00336/0.0056 = 3/5$.

11. The best tree is $(3, 0, 2)$ with score 30; it is non-projective, and Chu-Liu-Edmonds returns it. The best projective tree is $(0, 0, 2)$ with score 23, which has two root children; with one root child the best projective tree is $(2, 0, 2)$ with score 21.

13. The inorder walk gives 2, 1, 3, one inversion, so $k = 1$. The sequence is SH SH SWAP SH SH LA RA RA: after the swap, word 1 goes back to the buffer, then 3 takes 1 as a left dependent, 2 takes 3, and the root takes 2. That is $8 = 2 \cdot 3 + 2 \cdot 1$ moves.

17. The counts are 1, 3, 12, 55, 273, 1428, and with one root child 1, 2, 7, 30, 143, 728. They are exact because each projective tree has exactly one derivation in Eisner's algorithm.

20. Let $S(x)$ count the sequences of dependents on one side of a head. A subtree is a head with a sequence on each side, so $T = x S^2$ with $S = 1/(1 - T)$, which gives $S = 1 + x S^3$. A whole tree is the sequence of right dependents of the root, counted by $S$, and Lagrange inversion gives the first formula; the one-root-child trees are counted by $T$.

21. Suppose an item is popped with a score below its best. Follow the best derivation of that item down to an item on it that is still on the agenda; consistency means the priority does not increase as you go up the derivation, so that item has priority at least the popped one, and it would have been popped first. Admissibility alone bounds only the gap to the goal, and without reopening an item can be closed with a worse score.

22. For each word $d$, delete every root arc except $0 \to d$ and run Chu-Liu-Edmonds; keep the best of the $n$ results. Every single-root tree is a tree of exactly one of these runs. With Tarjan's $O(n^2)$ version the total is $O(n^3)$. On exercise 12 the runs give 16, 14 and 8.

23. If every instance triple has the same concept and every relation has the same label, the best match count is the number of instance triples plus the number of edges of a largest common subgraph of the two graphs, which is NP-hard to find.

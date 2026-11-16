Many NP-hard problems have instances that are large but have a small number at their heart: a vertex cover of 20 vertices in a graph of a million, a path of 10 edges, a graph of treewidth 4. Parameterized complexity measures time in the input size $n$ and in such a parameter $k$. A problem is fixed-parameter tractable (FPT) when some algorithm takes time $f(k) \cdot n^{O(1)}$, where $f$ may grow fast but the exponent of $n$ does not depend on $k$. Vertex cover is FPT. For $k$-clique the known algorithms take time $n^{ck}$ for a constant $c > 0$, and $k$-clique is complete for the class W[1].

This splits NP-hard problems more finely than NP-hardness alone. It also helps explain why exact solvers do well on some inputs: they spend their exponential time on $k$, not on $n$. As with P and NP, the lower side is conditional. A W[1]-hard problem has no FPT algorithm only if FPT ≠ W[1], which is open.

## What the chapter will cover

The entries of this chapter are being written. They will cover:

1. **Basic notions.** Parameters, parameterized problems, the classes FPT and XP, para-NP-hardness, and parameterized reductions.
2. **Kernelization.** Kernels and polynomial kernels, the Buss kernel and the crown reduction for vertex cover, the Nemhauser-Trotter theorem, the sunflower lemma, and lower bounds by cross-composition.
3. **Algorithm design.** Bounded search trees, iterative compression, color coding and divide and color, important separators, representative families, and cut and count.
4. **Graph structure.** Courcelle's theorem and other meta-theorems, the grid minor theorem, bidimensionality and subexponential parameterized algorithms.
5. **Intractability.** The W-hierarchy, weighted satisfiability, the W[1]-completeness of clique, and the FPT ≠ W[1] conjecture.
6. **Problems.** Parameterized vertex cover, feedback vertex set, odd cycle transversal, multiway cut, Steiner tree, dominating set and others.

## What to read meanwhile

Volume 7 has the graph side of the subject. Read [treewidth](/treewidth/), [tree decompositions](/tree-decomposition/) and [nice tree decompositions](/nice-tree-decomposition/), then [dynamic programming on tree decompositions](/dp-on-tree-decompositions/). [Treewidth computation](/treewidth-computation/) is FPT in $k$, with time linear in $n$ for each fixed $k$. The [longest path problem](/longest-path-problem/) gives color coding, in $2^{O(k)} m$ expected time for a path with $k$ vertices, and the [feedback vertex set problem](/feedback-vertex-set-problem/) is FPT on undirected graphs. The [clique decision problem](/clique-decision/) states that $k$-clique is W[1]-complete, and the [graph minor theorem](/graph-minor-theorem/) gives FPT algorithms whose function $f$ is not known.

[Vertex cover](/vertex-cover/) in Volume 18 is the standard FPT problem, with kernels of $2k$ and $3k$ vertices. [Branch and reduce](/branch-and-reduce/) in Volume 2 is the scheme behind bounded search trees. For hardness, read [parameterized inapproximability](/parameterized-inapproximability/) and [Gap-ETH](/gap-eth/) in Volume 18.

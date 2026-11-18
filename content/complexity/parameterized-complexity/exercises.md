1. ◦ A graph has a vertex $a$ joined to five leaves $b_1, \ldots, b_5$, a triangle on $x, y, z$, and one more edge $uv$. Apply the rules of the [Buss kernel](/buss-kernel/) with $k = 3$. Which vertices are taken, what are the new parameter and the sizes of the kernel, and what is the answer?

2. ◦ For the complete bipartite graph $K_{3,3}$, give the vertex cover number, the independence number, the clique number, the maximum degree and the treewidth.

3. ◦ Which of these running times have the form $f(k) \cdot n^{c}$ for a computable $f$ and a constant $c$: $2^k n^3$, $n^k$, $k^k + n^5$, $n^{\log_2 k}$, $2^{2^k} n$, $n^{\sqrt{k}}$? Which of them are XP bounds?

4. ◦ A [bounded search tree](/bounded-search-tree/) can use the branching vector $(1, 3)$ or the vector $(2, 2)$. Find both branching numbers to four decimal places, say which is better, and give $\lambda^{20}$ for each.

5. ◦ In [color coding](/color-coding/) for paths with $k = 4$ vertices, a uniform random coloring with 4 colors is used. What is the probability that a fixed path is colorful? How many independent colorings are needed to bring the probability of missing it below $1/100$?

6. ◦ [Cluster editing](/cluster-editing/) asks for the fewest edge insertions and deletions that turn a graph into a disjoint union of cliques. Find the answer for the cycles $C_5$ and $C_6$, and give an optimal set of edits for each.

7. ◦ Say which statements are true. (a) If clique has an FPT algorithm, then $\mathsf{FPT} = \mathsf{W}[1]$. (b) Dominating set is $\mathsf{W}[2]$-complete, so it has no XP algorithm. (c) $\mathsf{FPT} \ne \mathsf{XP}$ is proved. (d) Independent set on planar graphs is $\mathsf{W}[1]$-hard.

8. ◦ The [sunflower lemma](/sunflower-lemma/) says that more than $d!\,(p-1)^d$ sets of size $d$ contain a sunflower with $p$ petals. For 3-hitting set with $k = 5$, the kernel needs a sunflower with $k + 1$ petals. How many sets of size 3 guarantee one?

9. • The map $(G, k) \mapsto (G, n - k)$ between independent set and vertex cover is a polynomial-time reduction. Explain why it is not a [parameterized reduction](/parameterized-reduction/), and give a parameterized reduction from independent set to clique.

10. • Use the four color theorem to show that independent set on planar graphs has a kernel with fewer than $4k$ vertices.

11. • Write independent set with parameter $k$ as an instance of [weighted satisfiability](/weighted-satisfiability/) of a 2-CNF formula with only negative literals, and dominating set as weighted satisfiability of a CNF formula with only positive literals. In each case, state what a satisfying assignment of weight $k$ means.

12. • A graph is the disjoint union of the star $K_{1,3}$, with center $c$, and a triangle on $x, y, z$. Find the optimal solution of the vertex cover LP, the sets $V_0$, $V_{1/2}$ and $V_1$ of the [Nemhauser-Trotter theorem](/nemhauser-trotter-theorem/), and the kernel for $k = 3$. What is the answer?

13. • The Dreyfus-Wagner algorithm for [Steiner tree](/parameterized-steiner-tree/) combines, for each set $D$ of terminals, the splits of $D$ into a subset $D'$ and the rest. Show that the number of pairs $(D, D')$ with $D' \subseteq D \subseteq K$ is $3^{|K|}$, and give the number for $|K| = 5$.

14. • Use the bound $O((2e)^k (n+m))$ of [color coding for $k$-path](/k-path-color-coding/) to show that a path with $\log_2 n$ vertices can be found in randomized polynomial time. Give the exponent of $n$.

15. • Each of these algorithms would refute the Exponential Time Hypothesis. Say why. (a) Clique in time $2^{k} n^{\sqrt{k}}$. (b) Vertex cover in time $2^{k/\log_2 k} n^{2}$.

16. • Show that dominating set on graphs of maximum degree $\Delta$ has a search tree with at most $(\Delta + 1)^k$ leaves. How many leaves for $\Delta = 3$ and $k = 5$?

17. • Write a formula of monadic second-order logic that says a graph is 3-colorable. What does [Courcelle's theorem](/courcelle-theorem/) then give for 3-coloring on graphs of treewidth $t$?

18. • Give parameterized reductions in both directions between clique and multicolored clique, where the vertices come in $k$ color classes and the clique must take one vertex from each class.

19. • Prove that if $\mathsf{P} = \mathsf{NP}$, then $\mathsf{FPT} = \mathsf{W}[1]$. Conclude that a proof of $\mathsf{FPT} \ne \mathsf{W}[1]$ would also prove $\mathsf{P} \ne \mathsf{NP}$.

20. ★ Prove that vertex cover has no algorithm with time $2^{o(k)} n^{O(1)}$ unless the Exponential Time Hypothesis fails. Use the sparsification lemma and the reduction from 3-SAT to independent set.

21. ★ Steiner tree parameterized by the number of non-terminal vertices in the tree is $\mathsf{W}[2]$-hard. Prove it with a parameterized reduction from set cover parameterized by the number of sets.

22. ★ Show that clique parameterized by the vertex cover number $\tau$ of the input graph is FPT. Give an algorithm and its running time.

23. ★ Show that independent set parameterized by the maximum degree $\Delta$ alone is para-NP-hard, and that with the parameter $k + \Delta$ it has a kernel with fewer than $(\Delta + 1) k$ vertices.

24. ★ Give a parameterized reduction from vertex cover to [odd cycle transversal](/odd-cycle-transversal/) that keeps $k$ unchanged, and prove it correct.

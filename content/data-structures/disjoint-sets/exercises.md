1. ◦ Which of these relations on the integers $0, \ldots, 99$ are [equivalence relations](/equivalence-relation/)? (a) $a$ and $b$ have the same last decimal digit; (b) $|a - b| \le 1$; (c) $a$ divides $b$; (d) $a$ and $b$ have the same number of 1 bits in binary. For each one that is, count its classes; for each one that is not, name the property that fails.

2. ◦ Run [quick-find](/quick-find/) on the elements $0, \ldots, 7$ with the unions $(0, 5)$, $(5, 6)$, $(1, 2)$, $(2, 7)$, $(3, 4)$, $(6, 1)$, where union$(p, q)$ renames the set of $p$ to the name of the set of $q$. Give the array `id` at the end and the total number of entries of `id` that the unions change.

3. ◦ Run the same unions as in Exercise 2 with [quick-union](/quick-union/), which makes the root of $p$ a child of the root of $q$, and then with [union by size](/union-by-size/), which hangs the smaller tree under the larger and, on a tie, the root of $p$ under the root of $q$. Give the parent array and the height of the tallest tree in each case.

4. ◦ A forest on $0, \ldots, 8$ has the parent array $\langle 1, 2, 3, 4, 5, 5, 2, 3, 0 \rangle$, so 5 is the root. Run find$(8)$ three times on fresh copies: once with [path compression](/path-compression/), once with [path halving](/path-halving/) and once with [path splitting](/path-splitting/). Give the parent array after each, and the sum of the depths of all nodes before and after.

5. ◦ A forest with union by rank holds $n = 1000$ elements. What is the largest rank a node can have? At most how many nodes ever have rank 5? How many bits does a rank need? Compute $\lg^* 65536$ and $\lg^* 10^{80}$ with the [iterated logarithm](/iterated-logarithm/).

6. ◦ The edges $(0, 1)$, $(2, 3)$, $(1, 2)$, $(4, 5)$, $(3, 4)$, $(0, 5)$, $(1, 4)$, $(2, 5)$, $(0, 4)$ arrive in this order. Use [union-find with parity](/dsu-with-parity/) to find the first edge after which the graph is no longer bipartite, and give an odd cycle that it closes.

7. ◦ An array of 10 cells is painted by $(1, 6, a)$, $(4, 8, b)$, $(0, 2, c)$, $(7, 9, d)$, $(5, 5, e)$ in this order, where $(l, r, x)$ paints cells $l$ to $r$ with color $x$ and later paint covers earlier paint. Give the final colors. With the method of [painting subarrays offline](/offline-subarray-painting/), in which order are the operations read, and how many cells does each one paint?

8. ◦ Run [Kruskal's algorithm](/kruskal/) with a disjoint-set forest on the vertices $A, \ldots, F$ and the edges $AB = 4$, $AC = 1$, $BC = 3$, $BD = 2$, $CD = 5$, $CE = 7$, $DE = 6$, $DF = 8$, $EF = 9$. Which edges does a find show to be inside one tree, and what is the weight of the spanning tree?

9. • On the elements $1, \ldots, 9$, run union$(1, 2)$, union$(3, 4)$, union$(5, 6)$, union$(7, 8)$, union$(2, 4)$, union$(6, 8)$, union$(9, 8)$, union$(3, 7)$ with [union by rank](/union-by-rank/) and path compression, where on a tie the root of the first argument goes under the root of the second. Give the parent and rank arrays. Then run find$(1)$ and give them again. Which ranks no longer equal heights?

10. • [Linked-list disjoint sets](/linked-list-disjoint-sets/) start with 16 singletons. If unions always join two sets of equal size, round by round, how many set pointers change in all with the weighted-union rule? Without the rule, union$(a, b)$ appends the list of $b$ to that of $a$. Give a sequence of 15 unions that makes 120 changes, and show that no sequence makes more.

11. • Solve the [offline minimum](/offline-minimum/) problem for the sequence $7, 2, E, 9, 5, 4, E, E, 1, 8, 6, E, 3, E$, where a number is an insert and $E$ is an extract-min. Do it with the union-find method: split the sequence into blocks at the $E$'s, take the keys in increasing order, and give each key to the first free extraction at or after its block. Which keys are never extracted?

12. • Use [union-find with rollback](/union-find-with-rollback/) on $0, \ldots, 6$, with union by size and, on a tie, the root of the first argument under the root of the second. Run union$(0, 1)$ and union$(2, 3)$, save a checkpoint, run union$(1, 3)$ and union$(4, 5)$, save a second checkpoint, then run union$(5, 6)$ and union$(0, 6)$. Give the parent array and the number of sets now, after rolling back to the second checkpoint, and after rolling back to the first. Then show by a small example why path compression would break the rollback.

13. • [Weighted union-find](/weighted-union-find/) works for any abelian group. Use the positive rationals under multiplication, so that each fact says $\mathrm{val}(x)/\mathrm{val}(y) = d$. Add the facts $a/b = 2$, $b/c = 3$ and $d/e = 4$. What are $a/c$, $c/a$ and $a/d$? Then add $c/e = 1/2$. What is $a/d$ now, and which of the facts $a/e = 3$ and $a/e = 4$ does the structure accept?

14. • Run [Arpa's trick](/arpa-offline-rmq/) on $a = \langle 5, 2, 7, 3, 8, 1, 6, 4 \rangle$ (positions 0 to 7) with the queries $[0, 3]$, $[2, 4]$, $[3, 6]$, $[6, 7]$ and $[1, 4]$. Give the stack after each position, the position each query returns, and the parent array at the end, without path compression.

15. • For $n = 2^k$, give a sequence of operations on a forest with union by rank and path compression in which one find follows $k = \lg n$ parent pointers. Why does this not contradict the $O(\alpha(n))$ amortized bound?

16. • Extend the disjoint-set forest so that it can list the members of the set of $x$ in time linear in the size of the set, with only $O(1)$ extra work per union and one extra array.

17. ★ A program makes all its links first, each joining two roots, and only then runs $m$ finds with path compression. Prove that the finds take $O(n + m)$ time in all, whatever rule chose the links.

18. ★ Add an operation move$(x, y)$, which takes $x$ out of its set and puts it into the set of $y$, and an operation size$(x)$, both in $O(\alpha)$ amortized time. What must change in the forest, and how much space does it use after $k$ moves?

19. ★ A graph on $n$ vertices gets $m$ edge insertions, edge deletions and connectivity queries, all known in advance. Show how to answer the queries in $O(m \log m \log n)$ time with union-find with rollback. Why can the forest not use path compression here?

20. ★ In [Tarjan's offline LCA algorithm](/tarjan-offline-lca/), show that every union joins the set of a node with the set of its parent in the input tree. Conclude that the algorithm is an instance of [static tree set union](/static-tree-set-union/), and give its running time with the [Gabow-Tarjan](/gabow-tarjan-union-find/) structure on a word RAM.

## What to remember

- A **disjoint-set** structure keeps a partition of $n$ elements under two operations: **union** merges two sets, and **find** returns the representative of a set. Two elements are in one set exactly when their finds agree. Sets only merge; they never split.
- **Quick-find** makes find $\Theta(1)$ and union $\Theta(n)$. **Quick-union** makes union cheap once the roots are known, but its trees can become chains of height $n - 1$.
- The **disjoint-set forest** keeps each set as a tree of parent pointers whose root is the representative. **Union by rank** (or by size) hangs the lower tree under the higher one. Then a tree whose root has rank $r$ has at least $2^r$ nodes, so every tree has height at most $\lfloor \lg n \rfloor$.
- **Path compression** points every node on a find path at the root. **Path halving** and **path splitting** do a similar job in one pass, and they give the same bounds.
- **With both rules**, $m$ operations cost $O(m\,\alpha(n))$, and $\alpha(n) \le 4$ for every $n$ up to $2^{2048}$. The bound is tight for this structure, and the [union-find lower bound](/union-find-lower-bound/) shows that no structure does better in the cell-probe model. A single operation can still cost $\Theta(\log n)$.
- **Values on the edges.** If each parent pointer carries a parity, a difference or any group element, a find also returns the value of an element relative to its root. This tests bipartiteness online and checks systems of equations $x - y = d$.
- **Undo needs no compression.** With union by size alone, each union changes two fields, so it can be pushed on a stack and undone in $O(1)$; each operation costs $O(\log n)$ in the worst case.
- **Offline, the forest jumps.** When the operations are known in advance, a forest in which each used position points to the next free one solves offline minimum, painting subarrays and offline range minimum queries in nearly linear time.

## The structures side by side

| Structure | Find | Union | $m$ operations |
|---|---|---|---|
| [Quick-find](/quick-find/) | $\Theta(1)$ | $\Theta(n)$ | $\Theta(n^2)$ for $n - 1$ unions |
| [Quick-union](/quick-union/) | $O(n)$ | $O(n)$ | $\Theta(mn)$ |
| [Linked lists](/linked-list-disjoint-sets/), weighted union | $O(1)$ | $O(n)$, $O(\log n)$ am. | $O(m + n \log n)$ |
| [Forest](/disjoint-set-forest/), [union by rank](/union-by-rank/) alone | $O(\log n)$ | $O(\log n)$ | $\Theta(m \log n)$ |
| Forest, [path compression](/path-compression/) alone | $O(n)$ | $O(n)$ | $\Theta(m \log_{1 + m/n} n)$ |
| Forest, both rules | $O(\log n)$, $O(\alpha(n))$ am. | $O(\log n)$, $O(\alpha(n))$ am. | $O(m\,\alpha(n))$ |
| [Blum's structure](/blum-union-find/) | $O(\log n / \log\log n)$ | $O(\log n / \log\log n)$ | |
| [Gabow-Tarjan](/gabow-tarjan-union-find/), unions known in advance | | | $O(n + m)$ |

: Costs are worst case for one operation unless marked "am." (amortized). The bound for path compression alone is for $n - 1$ unions and $m \ge n$ finds. The Gabow-Tarjan bound is on a word RAM with words of $\Theta(\log n)$ bits.

## Choosing a structure

- In almost every program, use the forest with union by size or rank and path compression or halving. It is a few lines of code.
- When you must undo unions, as in offline dynamic connectivity, drop path compression and keep union by size.
- When you need relations between elements and not only membership, put values on the edges: parity for two-colorings, differences for equations.
- When you need to list the members of a set, add a circular list through the elements, or use [linked lists](/linked-list-disjoint-sets/), which list a set in time linear in its size.
- When every single operation must be fast, not only the average, the forest already gives $O(\log n)$; [Blum's structure](/blum-union-find/) lowers this to $O(\log n / \log\log n)$, which is the best possible.

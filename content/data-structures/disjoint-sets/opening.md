A network is built one cable at a time. After each new cable, someone asks whether two computers can now reach each other. Nobody ever removes a cable. The same pattern shows up in many places: pixels of one color merge into regions, variables declared equal merge into classes, and [Kruskal's algorithm](/kruskal/) joins trees of a forest until one spanning tree is left. In each case the elements fall into groups, the groups only merge, and the questions are about which group an element is in.

A [disjoint-set](/disjoint-set/) structure, also called union-find, answers these questions. It has two main operations: union merges the groups of two elements, and find returns a representative of the group of an element, so that two elements are in one group exactly when their finds agree. The simple ways to do this make one of the two operations cheap and the other one slow. The [disjoint-set forest](/disjoint-set-forest/) keeps each group as a tree of parent pointers, and with two small rules, one for linking and one for finding, it makes both almost free: $m$ operations on $n$ elements cost $O(m\,\alpha(n))$, where $\alpha$ is the [inverse Ackermann function](/inverse-ackermann-function/). That function is at most 4 for any $n$ that fits in a computer.

The code is a few lines. The proof of the bound is one of the hardest in this volume, and the chapter gives it in two steps: first a weaker $O(m \lg^* n)$ bound with a short proof, then Tarjan's bound itself.

## What the chapter covers

The chapter is in seven groups, read in order.

1. **The problem.** The [equivalence relation](/equivalence-relation/), the [disjoint-set](/disjoint-set/) type, and the [dynamic equivalence problem](/dynamic-equivalence-problem/).
2. **First solutions.** [Quick-find](/quick-find/) keeps the name of each set in an array, [quick-union](/quick-union/) keeps a forest with no rules, and [linked lists](/linked-list-disjoint-sets/) with the weighted-union rule reach $O(m + n \log n)$.
3. **The forest and its two rules.** The [disjoint-set forest](/disjoint-set-forest/), [union by size](/union-by-size/) and [union by rank](/union-by-rank/), and the three ways to shorten paths: [path compression](/path-compression/), [path halving](/path-halving/) and [path splitting](/path-splitting/).
4. **How fast it is.** The [Hopcroft-Ullman bound](/hopcroft-ullman-log-star-bound/) of $O(m \lg^* n)$, [Tarjan's bound](/union-find-amortized-bound/) of $O(m\,\alpha(n))$, and [randomized linking](/randomized-linking/), which reaches the same bound in expectation.
5. **More on the edges.** Forests whose parent pointers carry a [parity](/dsu-with-parity/), a [distance](/dsu-with-distances-to-representative/) or a [group value](/weighted-union-find/), and the forest whose unions can be [undone](/union-find-with-rollback/).
6. **Offline problems.** [Offline minimum](/offline-minimum/), [painting subarrays](/offline-subarray-painting/) and [Arpa's trick](/arpa-offline-rmq/) for range minimum queries, all solved by a forest that jumps over used positions.
7. **Limits and special cases.** [Static tree set union](/static-tree-set-union/) and the linear-time [Gabow-Tarjan](/gabow-tarjan-union-find/) structure for it, [Blum's structure](/blum-union-find/) with the best worst case for one operation, and the [Fredman-Saks lower bound](/fredman-saks-lower-bound/).

## A first reading

For a first reading, take these nine entries in order: [equivalence relation](/equivalence-relation/), [disjoint set](/disjoint-set/), [quick-find](/quick-find/), [quick-union](/quick-union/), [disjoint-set forest](/disjoint-set-forest/), [union by size](/union-by-size/), [union by rank](/union-by-rank/), [path compression](/path-compression/) and [union-find with parity](/dsu-with-parity/). Then read the [Hopcroft-Ullman bound](/hopcroft-ullman-log-star-bound/) for the idea of the analysis, and come back to [Tarjan's bound](/union-find-amortized-bound/) when you are at ease with the [potential method](/potential-method/). Group 7 is research material and can wait.

## Before you start

You need [asymptotic notation](/asymptotic-notation/) and [amortized cost](/amortized-cost/) from Volume 1, and for the two bounds of group 4 the [potential method](/potential-method/), the [iterated logarithm](/iterated-logarithm/) and the [inverse Ackermann function](/inverse-ackermann-function/). The forest is a [rooted tree](/rooted-tree/) stored by parent pointers. Offline minimum uses the [binary heap](/binary-heap/) of Chapter 3.5 as its baseline, and Arpa's trick answers [range minimum queries](/range-minimum-query/), the subject of Chapter 3.7. The uses come later: [Kruskal's algorithm](/kruskal/) and [connected components](/connected-components/) in Volume 7. The roadmap below lists every entry of the chapter with its kind and level, and the figure after it shows which entries lean on which.

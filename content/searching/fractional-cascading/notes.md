## History

The idea of passing a sample of one sorted list into another, with pointers, first appeared inside particular structures. In the layered range trees of Dan Willard and George Lueker, from the late 1970s, each secondary list points into the lists of the children, which removes a factor of $\log n$ from a two-dimensional range query. Bernard Chazelle's hive graph, from his work on filtering search published in 1986, combs every other edge of a planar map for the same kind of gain. Herbert Edelsbrunner, Leonidas Guibas and Jorge Stolfi used a cascade of samples along a tree of separating chains for optimal point location in a monotone subdivision, also in 1986.

Chazelle and Guibas turned these devices into a general technique in two papers in *Algorithmica* in 1986, *Fractional cascading: I. A data structuring technique* and *II. Applications*. The first defines catalog graphs of locally bounded degree, builds the augmented catalogs in linear time and space, and proves the query bound $O(\log n + k \log d)$. The second applies the technique to a long list of problems in computational geometry, from range searching to intersection queries and point location. The first paper also gives dynamic versions, with a fast update when only insertions or only deletions occur.

Kurt Mehlhorn and Stefan Näher made the structure fully dynamic in 1990, with $O(\log \log n)$ amortized time per update and an extra $O(\log \log n)$ per list in the query, the cost of finding the next bridge in a changing list. Later work by Dietz and Raman made the update time worst case, and Afshani proved that, on a pointer machine, some loss in the query is unavoidable for the dynamic problem.

Whether the technique extends to planar maps stayed open for fifteen years. Chazelle and Ding Liu settled it in the negative at STOC in 2001, with the journal version in 2004: for some paths of planar subdivisions, any pointer machine structure that answers queries in $O(k + \operatorname{polylog} n)$ time needs nearly quadratic space. Their construction also answered an old question about hierarchies of convex polytopes.

## Further reading

- Bernard Chazelle and Leonidas J. Guibas, *Fractional cascading: I. A data structuring technique*, Algorithmica 1 (1986). The general construction on catalog graphs, with the proofs of space and query time.
- Bernard Chazelle and Leonidas J. Guibas, *Fractional cascading: II. Applications*, Algorithmica 1 (1986). The geometric problems that the technique speeds up.
- Mark de Berg, Otfried Cheong, Marc van Kreveld and Mark Overmars, *Computational Geometry: Algorithms and Applications*, third edition (2008). The chapter on orthogonal range searching presents the layered range tree, the most common use of the technique.
- Kurt Mehlhorn and Stefan Näher, *Dynamic fractional cascading*, Algorithmica 5 (1990). The fully dynamic structure and its union-split-find step.
- Bernard Chazelle and Ding Liu, *Lower bounds for intersection searching and fractional cascading in higher dimension*, Journal of Computer and System Sciences 68(2) (2004). The lower bound for planar catalogs.

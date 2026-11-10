Some NP-hard problems can be approximated as closely as you like. An approximation scheme takes the input and a number $\varepsilon > 0$, and returns an answer within a factor $1 + \varepsilon$ of OPT, or $1 - \varepsilon$ for a maximization problem. A polynomial-time approximation scheme (PTAS) runs in polynomial time for each fixed $\varepsilon$, perhaps as $n^{1/\varepsilon}$; a fully polynomial one (FPTAS) runs in time polynomial in both $n$ and $1/\varepsilon$. These schemes mark the easy end of the hard problems, and they show what separates them from the problems of Chapter 18.6, which have no scheme unless P = NP.

The methods are few. Round the numbers of the input so that a pseudo-polynomial dynamic program runs in polynomial time. Group the items into a few classes and enumerate the large ones. Cut a geometric or planar instance into pieces of bounded size and solve each piece exactly.

## What the chapter will cover

The entries of this chapter are being written. They will cover:

1. **Definitions.** The approximation ratio, PTAS, efficient PTAS, FPTAS, asymptotic PTAS and the class APX.
2. **Rounding and scaling.** The FPTAS for knapsack of Ibarra and Kim, the FPTAS for subset sum by trimming, and the theorem that a strongly NP-hard problem has no FPTAS unless P = NP.
3. **Schemes for scheduling and packing.** The scheme of Hochbaum and Shmoys for makespan by dual approximation, the asymptotic scheme of Fernandez de la Vega and Lueker for bin packing, and multiple knapsack.
4. **Geometry and graphs.** Baker's technique for planar graphs, the shifting strategy, the schemes of Arora and of Mitchell for Euclidean TSP, and the PTAS for maximum cut on dense graphs.

## What to read meanwhile

Two schemes are already written. The [asymptotic scheme for bin packing](/bin-packing-aptas/) in Chapter 18.1 shows grouping and enumeration of configurations, and the [knapsack problem](/knapsack-problem/) in Volume 15 states its FPTAS and the PTAS without FPTAS for multidimensional knapsack. The [knapsack dynamic program](/knapsack-dynamic-programming/) runs in $O(nW)$ time, which is pseudo-polynomial; the FPTAS runs a version of it indexed by profit, on rounded profits. Read it with the [scaling technique](/scaling-technique/) of Volume 2. The [packing integer program](/packing-integer-program/) entry cites the PTAS of Frieze and Clarke for a fixed number of constraints. [Bin packing NP-hardness](/bin-packing-np-hardness/) shows why bin packing has an asymptotic scheme and no ordinary one, and [strip packing](/strip-packing/) has an asymptotic scheme of its own.

For the graph schemes, read [planar graphs](/planar-graph/), [tree decompositions](/tree-decomposition/) and [treewidth](/treewidth/) in Volume 7: Baker's technique cuts a planar graph into pieces of bounded treewidth.

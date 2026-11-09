## History

Connectivity was a topic of graph theory long before it was one of algorithms. Karl Menger proved his theorem on disjoint paths in 1927, in a paper on the theory of curves, and Hassler Whitney gave the global form for $k$-connected graphs and the characterization of biconnected graphs by open ear decompositions in 1932. Herbert Robbins proved in 1939 that the streets of a town can all be made one-way with every place still reachable exactly when no street is a bridge. Ford and Fulkerson's max-flow min-cut theorem of 1956 later turned Menger's theorem into an algorithm.

The algorithms of this chapter rest on Robert Tarjan's 1972 paper "Depth-first search and linear graph algorithms", which showed that the low points of a depth-first search find the biconnected components of an undirected graph and the strongly connected components of a directed one, each in linear time. John Hopcroft and Tarjan published the biconnectivity method as Algorithm 447 of the *Communications of the ACM* in 1973, the same year as their triconnectivity algorithm and a year before their linear planarity test. Gallai, and independently Harary and Prins in 1966, had described the tree of blocks and cut vertices.

S. Rao Kosaraju found the two-pass method for strong components in 1978 without publishing it. Micha Sharir found it on his own and published it in 1981, and Aho, Hopcroft and Ullman's 1983 book made it known under Kosaraju's name. Paul Purdom in 1970 and Ian Munro in 1971 had found strong components by contracting cycles on the search path; Cheriyan and Mehlhorn in 1996 and Harold Gabow in 2000 showed that two stacks make this contraction linear. Nuutila and Soisalon-Soininen in 1994, and David Pearce in 2016, reduced the space of Tarjan's algorithm.

For all-pairs reachability, Stephen Warshall's 1962 theorem on Boolean matrices gave the triple loop, and the methods of Fischer and Meyer and of Munro reduced the closure to matrix multiplication. Aho, Garey and Ullman showed in 1972 that the transitive reduction costs as much as the closure. Measuring connectivity came with flows. Shimon Even's 1975 test needs a bounded number of flow computations, and Even and Tarjan bounded the flows on unit networks the same year. Hiroshi Nagamochi and Toshihide Ibaraki's 1992 scan gave sparse certificates and a flow-free algorithm for edge connectivity.

## Further reading

- Robert E. Tarjan, "Depth-first search and linear graph algorithms", *SIAM Journal on Computing* (1972). The source of low points and of the linear algorithms for blocks and strong components.
- Shimon Even, *Graph Algorithms*, 2nd ed. (2012). Careful chapters on depth-first search, connectivity and Menger's theorem by flows.
- Jeff Erickson, *Algorithms* (2019), Chapter 6. Depth-first search, strong components and the two linear-time algorithms side by side.
- Reinhard Diestel, *Graph Theory*. The structure of 2-connected graphs, ear decompositions, the block graph and the theorems of Menger and Whitney.
- Hiroshi Nagamochi and Toshihide Ibaraki, *Algorithmic Aspects of Graph Connectivity* (2008). Certificates, edge connectivity and minimum cuts without flows.

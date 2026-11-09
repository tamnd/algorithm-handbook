## History

Trees entered mathematics through physics and chemistry. Gustav Kirchhoff used spanning trees in 1847 to solve the equations of electrical networks, and Arthur Cayley named trees in 1857 and later counted them, a count that Heinz Prüfer reproved in 1918 with the sequence now named after him. Camille Jordan studied the center and the centroid of a tree in 1869, by removing the outermost vertices step by step, which is the leaf-peeling algorithm. The equivalent definitions of a tree were collected in Knuth's first volume of *The Art of Computer Programming* in 1968, which also fixed the names of the three traversal orders.

Lowest common ancestors became an algorithmic problem with Aho, Hopcroft and Ullman in 1973. Tarjan's 1979 paper on path compression gave the offline method with union-find. Harel and Tarjan reached $O(n)$ preprocessing and $O(1)$ queries in 1984, by a method that was correct but hard to implement, and the reduction to range minima over the Euler tour, popularized by Bender and Farach-Colton around 2000, made the bound practical. Sleator and Tarjan introduced heavy and light edges for their dynamic trees in 1983; heavy-light decomposition, centroid decomposition, DSU on tree and virtual trees are now standard in programming contests.

Dominators began in compilers. Prosser defined them in 1959 for the analysis of flow diagrams, and Lowry and Medlock used them in 1969 to find loops in IBM's FORTRAN H compiler. Lengauer and Tarjan gave the near-linear algorithm with semidominators in 1979, and it has been the reference method since.

Tree decompositions came from the graph minors project of Robertson and Seymour in the 1980s, with earlier versions by Halin and by Bertelè and Brioschi in dynamic programming. Arnborg, Corneil and Proskurowski showed in 1987 that treewidth is NP-hard to compute, and Bodlaender gave a linear-time algorithm for each fixed width in 1996. On the other branches, Tai defined tree edit distance in 1979 and Zhang and Shasha gave the keyroot algorithm in 1989; Wetherell and Shannon in 1979 and Reingold and Tilford in 1981 set the rules for drawing trees; and Bartal in 1996 and Fakcharoenphol, Rao and Talwar in 2003 showed that every metric is close, on average, to a random tree.

## Further reading

- Donald E. Knuth, *The Art of Computer Programming*, Volume 1, Section 2.3. Trees, traversals, threaded trees and the enumeration of trees.
- Michael A. Bender and Martín Farach-Colton, "The LCA problem revisited" (LATIN 2000). A short, readable path from LCA to range minima and back.
- Robert Endre Tarjan, *Data Structures and Network Algorithms* (1983). Path compression, heavy-light ideas and dynamic trees from their author.
- Marek Cygan and coauthors, *Parameterized Algorithms* (2015), Chapter 7. Treewidth, nice tree decompositions and dynamic programming over them.
- Steven S. Muchnick, *Advanced Compiler Design and Implementation* (1997). Dominators and their use in control-flow analysis.

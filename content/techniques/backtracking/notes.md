## History

R. J. Walker described it in 1960 as an enumerative technique for a class of combinatorial problems, in the proceedings of an AMS symposium on combinatorial analysis. In 1965 Solomon Golomb and Leonard Baumert gave a general account in the Journal of the ACM under the title "Backtrack programming". Their central idea is the one this chapter is built on: a test on each prefix, applied as soon as the prefix is formed, so that one failed test removes a whole subtree.

The size of that subtree is hard to know in advance, and this is the subject of Knuth's 1975 paper in Mathematics of Computation, "Estimating the efficiency of backtrack programs". The random-path estimate of [the generic backtracking algorithm](/generic-backtracking-algorithm/) comes from it. In the same year Bitner and Reingold wrote on backtrack programming techniques in the Communications of the ACM, including the choice of the next variable with the fewest choices left, which they called search rearrangement. Knuth later treated the whole subject in Section 7.2.2 of Volume 4B of *The Art of Computer Programming*.

The vocabulary of the [state space tree](/state-space-tree/), with its problem states, answer states, live nodes and E-nodes, comes from the textbook of Horowitz and Sahni, later written with Rajasekaran. The dominance tests of [search-tree pruning](/search-tree-pruning/) were studied by Ibaraki in 1977 in the setting of branch and bound.

Constraint satisfaction gave the method its other name. There the plain search is called chronological backtracking, to set it apart from backjumping, which returns to the variable that caused a failure. Haralick and Elliott studied look-ahead and the fail-first rule in Artificial Intelligence in 1980, and Brélaz published the saturation rule for graph coloring, now called DSATUR, in 1979. Freuder showed in 1982 that a tree-shaped problem that is arc consistent is solved without any backing up, the result behind Exercise 18. Prosser's 1993 paper in Computational Intelligence placed chronological backtracking, backjumping, conflict-directed backjumping and forward checking in one framework.

The two worked problems have their own history. Letter sums are older than computers: SEND + MORE = MONEY is due to Henry Dudeney, in the Strand Magazine of 1924. Eppstein proved in 1987 that deciding whether a cryptarithm has a solution is NP-complete when the base grows with the input. For the maze, Read and Tarjan gave in 1975 a backtracking method that lists the simple paths between two vertices with polynomial time per path, while Valiant's 1979 work shows that counting them is #P-complete in general graphs.

## Further reading

- Donald E. Knuth, *The Art of Computer Programming*, Volume 4B, Section 7.2.2: the fullest treatment of backtrack programming, with Algorithm B, the size estimates and many puzzles.
- Ellis Horowitz, Sartaj Sahni and Sanguthevar Rajasekaran, *Computer Algorithms*, second edition, Chapter 7: the state space tree vocabulary and the classic textbook problems, from queens to subset sum and coloring.
- Rina Dechter, *Constraint Processing*, Chapters 5 and 6: look-ahead, backjumping and variable ordering for constraint satisfaction.
- Stuart Russell and Peter Norvig, *Artificial Intelligence: A Modern Approach*, fourth edition, the chapter on constraint satisfaction problems: a short account of backtracking search with the minimum remaining values, degree and least constraining value rules.
- Solomon W. Golomb and Leonard D. Baumert, "Backtrack programming", Journal of the ACM 12(4), 1965: the paper that named the method and set out the prefix test.

## History

Query planning began with the first relational systems. In 1979 Patricia Selinger and her colleagues at IBM described the optimizer of System R in *Access Path Selection in a Relational Database Management System*. The paper set the pattern that most optimizers still follow: estimate the selectivity of each predicate from a few statistics or from fixed defaults, add up a cost in page reads and CPU work, and search the left-deep join orders by dynamic programming, keeping one plan for each set of relations and each interesting order. Rewrite rules such as pushing selections below joins were part of the algebraic optimizers of the same years.

Better statistics came next. Robert Kooi proposed histograms for selectivity estimation in his 1980 thesis, and Gregory Piatetsky-Shapiro and Charles Connell studied equi-depth histograms in 1984. Yannis Ioannidis and Stavros Christodoulakis showed in 1991 that estimation errors grow exponentially with the number of joins. Ioannidis and Viswanath Poosala introduced V-optimal histograms in 1995, and H. V. Jagadish and colleagues gave the dynamic program that builds them in 1998.

The search problem was studied in parallel. Toshihide Ibaraki and Tiko Kameda showed in 1984 that finding the best join order is NP-hard in general, and gave a polynomial algorithm for tree queries under a special cost function, which Ravi Krishnamurthy, Haran Boral and Carlo Zaniolo improved in 1986. Michael Steinbrunn, Guido Moerkotte and Alfons Kemper compared heuristic and randomized methods in 1997. Guido Moerkotte and Thomas Neumann gave DPccp in 2006, a dynamic program that visits only connected pairs of sets and so does work in proportion to the shape of the query graph. Goetz Graefe's Volcano and Cascades frameworks, from 1993 and 1995, made the rules and the search into an extensible engine.

Precomputed results became a planning problem with data warehouses. Venky Harinarayan, Anand Rajaraman and Jeffrey Ullman gave the greedy algorithm for choosing views of a data cube in 1996, with its guarantee of a constant fraction of the best benefit. In 2015 Viktor Leis and his colleagues built the Join Order Benchmark of 113 queries on real data, and measured that cardinality errors, not the cost model or the search, cause most bad plans in current systems.

## Further reading

- Patricia G. Selinger, Morton M. Astrahan, Donald D. Chamberlin, Raymond A. Lorie and Thomas G. Price, *Access Path Selection in a Relational Database Management System*, SIGMOD 1979. The source of the cost model and the dynamic program.
- Surajit Chaudhuri, *An Overview of Query Optimization in Relational Systems*, PODS 1998. A short survey of rewrites, statistics and search.
- Yannis E. Ioannidis, *The History of Histograms (abridged)*, VLDB 2003. How histograms for estimation developed.
- Venky Harinarayan, Anand Rajaraman and Jeffrey D. Ullman, *Implementing Data Cubes Efficiently*, SIGMOD 1996. The view lattice and the greedy selection.
- Viktor Leis, Andrey Gubichev, Atanas Mirchev, Peter Boncz, Alfons Kemper and Thomas Neumann, *How Good Are Query Optimizers, Really?*, PVLDB 9(3), 2015. Measurements of estimates, cost models and plans.

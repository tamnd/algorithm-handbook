A database system answers queries over data larger than memory, for many users at once, and survives crashes. Behind its query language sit algorithms from most parts of this book: external sorting and B+ trees to reach data on disk, hashing to join and group it, dynamic programming to choose a plan, cycles in a graph to check that concurrent transactions behave as if run one at a time, and logs to rebuild a consistent state after a failure.

The field has its own theory. Functional dependencies and Armstrong's axioms guide the design of schemas. Chandra and Merlin reduced the containment of conjunctive queries to finding a homomorphism. The AGM bound gives the largest possible output of a join from the sizes of its inputs, and worst-case optimal join algorithms run in time close to it, where every plan built from two-way joins can be slower by a polynomial factor.

## What the chapter will cover

The entries of this chapter are being written. They will cover:

1. **Operators.** Query plans and the iterator model; nested-loop, sort-merge and hash joins with the Grace and hybrid variants; semijoins and Bloom joins; hash aggregation.
2. **Query optimization.** Histograms, cardinality estimation, cost models, predicate pushdown, join ordering by the System R dynamic program, and multiway joins: Yannakakis's algorithm for acyclic joins, the AGM bound, generic join and leapfrog triejoin.
3. **Indexes and views.** Clustered, covering and bitmap indexes, zone maps, learned indexes, database cracking, and the incremental maintenance of materialized views.
4. **Transactions.** ACID, serializability and the conflict graph, two-phase locking, phantoms, timestamp ordering, wait-die and wound-wait, optimistic and multiversion concurrency control, and snapshot isolation.
5. **Recovery.** Write-ahead logging, steal and force policies, checkpoints, group commit, shadow paging and ARIES.
6. **Design theory and Datalog.** Attribute closure, minimal covers, normal forms with BCNF decomposition and 3NF synthesis, the chase, Datalog with semi-naive evaluation and magic sets, and query containment.
7. **Ranking queries.** Top-k queries by Fagin's algorithm and the threshold algorithm, and skyline queries.

## What to read meanwhile

The storage structures are in Volume 3: the [B+ tree](/b-plus-tree/), the [log-structured merge tree](/log-structured-merge-tree/), the [hash table](/hash-table/) and the [Bloom filter](/bloom-filter/). [External merge sort](/external-merge-sort/) in Volume 4 shows how disk-bound work is costed. Chapter 20.5 joins on many machines, by the [map-side join](/map-side-join/) and the [hypercube shares join](/hypercube-shares-join/). For size estimates, read [HyperLogLog](/hyperloglog/) and [join size estimation](/join-size-estimation-problem/) in Volume 19.

For transactions, read the [transaction](/transaction/), [undo log](/undo-log/) and [redo log](/redo-log/) entries of Chapter 22.4, the [wait-for graph](/wait-for-graph/) of Chapter 22.1, and [two-phase commit](/two-phase-commit/) in Volume 21. Datalog evaluation is forward chaining, as in [Horn-SAT](/horn-sat/), up to a least [fixed point](/fixed-point/); acyclic joins are defined on a [hypergraph](/hypergraph/), and a skyline is a [Pareto front](/pareto-front/).

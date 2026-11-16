Alice holds a string $x$ of $n$ bits and Bob holds a string $y$, and they want to know whether $x = y$. Any deterministic protocol needs $n + 1$ bits of communication in the worst case. With random choices and a small chance of error, $O(\log n)$ bits suffice. Communication complexity studies such games. It ignores how long each player computes and counts only the bits that cross between them. Query complexity does the same for one player: it counts how many bits of the input an algorithm must read, as a decision tree does.

These models matter because in them lower bounds can be proved without any hypothesis. They are also small enough to carry into larger settings. A communication bound becomes a space bound for streaming algorithms, a round bound for distributed algorithms, or a size bound for data structures and circuits. A query bound shows how far quantum algorithms can beat classical ones.

## What the chapter will cover

The entries of this chapter are being written. They will cover:

1. **Two-party models.** The communication model and matrix, deterministic, nondeterministic, randomized and one-way protocols, and quantum communication.
2. **Lower bound methods.** Fooling sets, the rank and log-rank bounds, discrepancy, corruption, sign rank, information complexity and direct sums, with the log-rank conjecture.
3. **Standard problems.** Equality and its randomized protocol, set disjointness, index, inner product, greater-than, Gap Hamming distance and pointer chasing.
4. **Many players.** Number-in-hand and number-on-forehead models, simultaneous messages, round elimination, and the Karchmer-Wigderson link to circuit depth.
5. **Query complexity.** Deterministic and randomized decision tree complexity, certificate complexity, sensitivity and block sensitivity, and the sensitivity theorem.
6. **Quantum queries.** The quantum query model, the polynomial method with approximate degree, and the quantum adversary method.

## What to read meanwhile

Volume 1 has the query side: the [decision tree model](/decision-tree-model/), the [adversary argument](/adversary-argument/) and [Yao's minimax principle](/yao-minimax-principle/), which turns a hard input distribution into a bound for randomized algorithms. [String equality testing](/string-equality-testing/) in Volume 8 proves the $n + 1$ bit bound for equality and gives the $O(\log n)$ bit protocol.

Communication bounds are used in several written entries. In Volume 19, the [index problem lower bound](/index-problem-lower-bound/) gives streaming space bounds, and the [frequency moment lower bounds](/frequency-moment-lower-bounds/) come from set disjointness. The [distributed diameter lower bound](/diameter-lower-bound-distributed/) in Volume 21 also reduces from set disjointness. For quantum queries, read [Grover optimality](/grover-optimality/) in Volume 30, which gives $\Omega(\sqrt{N})$ queries for search, and [Simon's problem](/simon-problem/) in Volume 30, where quantum algorithms need $\Theta(n)$ queries and classical ones $\Theta(2^{n/2})$.

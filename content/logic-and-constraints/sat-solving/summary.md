## What to remember

- **SAT** asks whether a CNF formula has a model. It is NP-complete, and so is [3-SAT](/3-sat/). The best proven bounds for 3-SAT are about $1.307^n$, from PPSZ, and $O^*((4/3)^n)$ from [Schöning's random walk](/schoning-algorithm/).
- **Three classes are easy.** [2-SAT](/2-sat/) is decided in $\Theta(n + m)$ time through the strongly connected components of the implication graph. [Horn-SAT](/horn-sat/) has a least model, found by forward chaining in $\Theta(n + m + s)$ time. [XOR-SAT](/xor-sat/) is a linear system over GF(2), solved in $O(m n \min(m, n))$ time.
- **Unit propagation** is the inner loop of every complete solver. A clause with one free literal and all others false forces that literal. Two watched literals per clause make it cheap.
- **Encodings decide what the solver sees.** The [Tseitin transformation](/tseitin-transformation/) gives an equisatisfiable CNF with one new variable per gate and a linear number of clauses. Plaisted-Greenbaum keeps only the clauses of one polarity. A sequential counter encodes "at most $k$" with $k(n - 1)$ new variables.
- **DPLL** is backtracking with unit propagation and the pure literal rule: $O(2^n n m k)$ in the worst case. **CDCL** adds learning. At a conflict it cuts the [implication graph](/implication-graph/) at the first UIP, learns a clause that the formula implies, and jumps back to the level where that clause becomes unit.
- **CDCL is still exponential in the worst case.** Every resolution refutation of the pigeonhole formula has $2^{\Omega(n)}$ clauses, and a CDCL run is a resolution proof. With restarts and good decisions, CDCL can simulate resolution with a polynomial loss.
- **Unsatisfiable answers come with proofs.** A [DRAT](/drat-proof/) proof lists added and deleted clauses, each one RUP or RAT. An LRAT proof adds hints, so a checker runs in time linear in the proof.
- **Local search** is incomplete but fast on many satisfiable formulas. [WalkSAT](/walksat/) picks a false clause and flips one of its variables, chosen by its break count or at random.
- **Beyond yes or no.** [MaxSAT](/max-sat/) is NP-hard even for 2-literal clauses, and a random assignment satisfies $7/8$ of the clauses of an exact 3-CNF in expectation. [Model counting](/model-counting/) is #P-complete, and [QBF](/qbf/) is PSPACE-complete.

## The main methods side by side

| Method | Problem | Time | Space |
|---|---|---|---|
| [2-SAT algorithm](/two-sat-algorithm/) | 2-SAT | $\Theta(n + m)$ | $\Theta(n + m)$ |
| [Forward chaining](/horn-sat-forward-chaining/) | Horn-SAT | $\Theta(n + m + s)$ | $\Theta(n + m + s)$ |
| [Gaussian elimination](/xor-gaussian-elimination/) | XOR-SAT | $O(m n \min(m, n))$ | $O(m n)$ |
| [Davis-Putnam elimination](/davis-putnam-elimination/) | SAT | $O(n^2 9^n)$ | $O(n 3^n)$ |
| [DPLL](/dpll/) | SAT | $O(2^n n m k)$ | $O(n m k)$ |
| [CDCL](/cdcl/) | SAT | $2^{\Omega(n)}$ | $O(n m)$ |
| [GSAT](/gsat/) | SAT, models only | $O(t f m k)$ | $O(n + m)$ |
| [WalkSAT](/walksat/) | SAT, models only | $O(t(f k d + m k))$ | $O(n + m k)$ |
| [Schöning](/schoning-algorithm/) | $k$-SAT, models only | $O((2(k-1)/k)^n n^2 m k)$ expected | $O(n + m k)$ |
| [PPSZ](/ppsz-algorithm/) | $k$-SAT, models only | $O(2^{(1-c)n + o(n)})$ expected | $O(g s)$ |
| [Core-guided MaxSAT](/core-guided-maxsat/) | partial MaxSAT | $O(c s T)$ | $O(m + c s^2)$ |

: Here $n$ is the number of variables, $m$ the number of clauses, $k$ the largest clause width and $s$ the number of literal occurrences, except in the last two rows. For local search, $t$ and $f$ are the numbers of tries and flips and $d$ the largest number of clauses on one variable. For PPSZ, $c = 2 - 2\ln 2$ when $k = 3$, and $g$ and $s$ are the number and size of the clauses after bounded resolution. For core-guided MaxSAT, $s$ is the number of soft clauses, $c$ the optimal cost and $T$ the time of one SAT call. The CDCL row is a lower bound, from the pigeonhole formulas.

## Choosing a method

- If every clause has two literals, every clause is Horn, or every constraint is an XOR, use the polynomial algorithm of its class.
- For a general formula from verification, planning or scheduling, use a CDCL solver with preprocessing. Write the problem as a circuit and apply the Tseitin transformation, or Plaisted-Greenbaum when only satisfiability matters.
- For large satisfiable random formulas, or when any good model will do, try WalkSAT or probSAT. They cannot prove unsatisfiability.
- When the answer must be trusted, ask the solver for a DRAT or LRAT proof and check it with an independent checker.
- When some clauses may be broken at a cost, use a MaxSAT solver. Core-guided methods do well when the optimal cost is small.

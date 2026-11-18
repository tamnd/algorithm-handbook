## What to remember

- **Algebra and calculus have the same power.** Relational algebra with its six operators and the domain-independent relational calculus express the same queries ([Codd's theorem](/codds-theorem/)). Domain independence itself is undecidable, so systems use the safe-range syntax instead. A fixed first-order query runs in polynomial time in the data, but with the query as input evaluation is PSPACE-complete.
- **SQL uses three truth values.** A comparison with NULL is UNKNOWN, and WHERE keeps a row only when its condition is TRUE. So NOT IN against a list with a NULL returns nothing, while set operations, GROUP BY and DISTINCT treat two NULLs as equal.
- **Closure decides functional dependencies.** $F \models X \to Y$ exactly when $Y \subseteq X^+$, and $X^+$ takes $\Theta(n + m)$ time. Armstrong's axioms are sound and complete for the same relation. Keys and minimal covers come from closures, but deciding whether an attribute is in some key is NP-complete.
- **BCNF and 3NF trade off.** [BCNF decomposition](/bcnf-decomposition/) always gives a lossless split into BCNF schemas, but it can lose dependencies, and some schemas have no dependency-preserving BCNF split. [3NF synthesis](/third-normal-form-synthesis/) always gives a split that is lossless and preserves the dependencies, at the price of some redundancy.
- **A lossless join is a chase question.** A two-part split $(R_1, R_2)$ is lossless under FDs exactly when $R_1 \cap R_2 \to R_1$ or $R_1 \cap R_2 \to R_2$ follows. For any number of parts, the [tableau test](/lossless-join-test/) chases one row per part and asks for an all-distinguished row.
- **Containment is homomorphism.** For conjunctive queries, $Q_1 \subseteq Q_2$ holds exactly when there is a homomorphism from $Q_2$ to $Q_1$ that fixes the head, so containment is NP-complete. Every conjunctive query has a unique minimal equivalent, its core, up to renaming. For unions, each member of the first must be contained in a member of the second.
- **Acyclic queries are easy.** An $\alpha$-acyclic hypergraph has a join tree, the GYO reduction finds one, and hypertree width 1 means acyclic. Conjunctive queries of bounded hypertree width or bounded fractional hypertree width are evaluated in polynomial time.
- **Datalog is recursion with a least fixed point.** Its data complexity is P-complete and its combined complexity is EXPTIME-complete. Semi-naive evaluation fires each rule instance once instead of once per round, and magic sets confine bottom-up work to the facts a query with constants needs.
- **Annotations follow a semiring.** Positive queries carry provenance polynomials in $\mathbb{N}[X]$, from which bag counts, costs and witnesses follow by substitution. On tuple-independent databases, a self-join-free conjunctive query is in polynomial time when it is hierarchical and #P-hard otherwise.

## The algorithms side by side

| Algorithm | Decides or builds | Time |
|---|---|---|
| [Attribute closure](/attribute-closure-algorithm/) | $X^+$ under $F$ | $\Theta(n + m)$ |
| [Minimal cover](/minimal-cover-problem/) | an equivalent irredundant cover | $O(m(n + m))$ |
| [BCNF decomposition](/bcnf-decomposition/) | lossless BCNF split | $O(4^n m)$ |
| [3NF synthesis](/third-normal-form-synthesis/) | lossless, dependency-preserving 3NF split | $O(n(n + m)^2)$ |
| [Tableau test](/lossless-join-test/) | lossless join of $k$ parts | $O(k^2 a (1 + m \log k))$ |
| [Chase](/chase-algorithm/) with FDs | implication, lossless join | $O(s^2 n (n + m))$ |
| [GYO reduction](/gyo-reduction/) | $\alpha$-acyclicity and a join tree | $O(m^3 v^2)$ |
| [CQ minimization](/conjunctive-query-minimization/) | the core of a query | $O(a k^{k+1})$ |
| [Semi-naive evaluation](/semi-naive-evaluation/) | least model of a Datalog program | $O(s r k^2 n^v)$ |

: The main algorithms of the chapter with the worst-case bounds of their entries. Here $n$ is the number of attributes and $m$ the size of the FDs, except in the GYO row, where $m$ counts edges and $v$ vertices. In the other rows $k$, $a$, $s$, $r$ and $v$ are defined in each entry. With JDs or MVDs the chase can take time exponential in the number of attributes.

## Choosing a method

To design a schema, find the keys with closures, compute a minimal cover, and try BCNF first. If the BCNF split loses a dependency you need to check on every update, use 3NF synthesis, or keep the BCNF split and check the lost dependency with a join. Independent multivalued facts call for 4NF.

To test a split, use the two-part condition for two parts and the tableau test for more. To compare two conjunctive queries, look for a homomorphism. Minimize a query before you evaluate it when it may contain redundant atoms, as generated queries often do. For acyclic queries, build the join tree with GYO and evaluate along it. For recursion, write Datalog and evaluate it semi-naively, with magic sets when the query binds constants.

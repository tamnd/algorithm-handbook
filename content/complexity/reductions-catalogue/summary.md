## What to remember

- A Karp reduction $A \le_m^p B$ is a polynomial-time map $f$ with $x \in A \iff f(x) \in B$. If $B \in \mathsf{P}$ in time $q$ and $f$ runs in time $p$, then $A$ is decided in time $p(n) + q(p(n))$. Also $\overline{A} \le_m^p \overline{B}$.
- Reductions compose, but the exponents multiply: a chain of $k$ reductions of degree $d$ can have degree $d^k$. So a constant number of steps is safe, and a chain whose length grows with $n$ is not.
- A [Turing reduction](/turing-reduction/) may ask many questions and use the answers freely. Every Karp reduction is a Turing reduction, and the converse fails. NP is closed under Turing reductions only if $\mathsf{NP} = \mathsf{coNP}$, so NP-completeness uses Karp reductions. For P-completeness and NL-completeness, use logspace reductions, since under polynomial-time reductions every nontrivial problem in P is complete for P.
- An [NP-completeness proof](/np-completeness-proof/) has four parts: membership in NP, a map from a known NP-complete problem *to* the new one, a bound on the time of the map, and both directions of the "if and only if". The usual errors are reducing the wrong way and proving one direction only.
- [Gadgets](/gadget-reduction/) carry the parts of a formula: a variable gadget forces a consistent choice, and a clause gadget can be completed only if the clause is satisfied. From 3-SAT, vertex cover uses $k = n + 2m$, and 3-coloring uses $3 + 2n + 6m$ vertices.
- Some boundaries are sharp, unless P = NP: 2-coloring is in P and 3-coloring is NP-complete; NAE-2SAT and one-in-two SAT are linear equations modulo 2; 0-1 equations with at most two ones per column are perfect matching; [CVP](/circuit-value-problem/) is in P, and circuit SAT is NP-complete.
- Number problems built from exact cover by digits, such as [knapsack](/knapsack-decision/) and subset sum, are only weakly NP-hard, since an $O(nW)$ dynamic program exists. [3-partition](/three-partition/) is strongly NP-complete and so has no pseudo-polynomial algorithm unless P = NP.
- For NP-complete problems, a decision procedure finds a solution with polynomially many questions; SAT needs $n$ questions after the first. A [parsimonious reduction](/parsimonious-reduction/) keeps the number of solutions, and Cook's tableau and the Tseitin encoding of circuits are parsimonious, so #SAT is #P-complete.

## The main reductions side by side

| Reduction | Size of the result | Gadget or idea | Parsimonious | Hardness it proves |
|---|---|---|---|---|
| [Circuit SAT](/circuit-sat/) to 3-SAT | $\le 3s + 1$ clauses for $s$ gates | Tseitin clauses per gate | yes | strong |
| 3-SAT to [clique](/clique-problem/) | $3m$ vertices, $k = m$ | one vertex per literal occurrence | no | strong |
| 3-SAT to vertex cover | $2n + 3m$ vertices, $k = n + 2m$ | edge per variable, triangle per clause | no | strong |
| 3-SAT to [3-coloring](/three-coloring/) | $3 + 2n + 6m$ vertices | palette triangle, OR gadgets | no | strong |
| Vertex cover to [Hamiltonian cycle](/hamiltonian-cycle-np-completeness/) | $12\lvert E \rvert + k$ vertices | 12-vertex cover-testing gadget | no | strong |
| Hamiltonian cycle to [TSP](/traveling-salesman-decision/) | complete graph on $n$ vertices | distances 1 and 2, bound $n$ | yes, on cycles | strong |
| 3-SAT to [NAE-3SAT](/not-all-equal-sat/) | $n + m + 1$ variables, $2m$ clauses | shared variable $w$, complement symmetry | no | strong |
| 3-SAT to [one-in-three SAT](/one-in-three-sat/) | $n + 4m$ variables, $3m$ clauses | chain of three clauses | no | strong |
| [0-1 equations](/zero-one-equations/) to subset sum | $n$ numbers of $m$ digits | digits in base $n + 1$ | yes | weak |
| 4-partition to [3-partition](/three-partition/) | $24m^2 - 3m$ numbers | residues modulo 4 | no | strong |

: Standard reductions of the chapter, with sizes as the entries give them, for a formula with $n$ variables and $m$ clauses. "Strong" means that the result has no large numbers, so it proves strong NP-hardness. All hardness holds unless P = NP.

## Using the chapter

- Choose the source by the shape of the target: use 3-SAT or circuit SAT for choices and logic, NAE-3SAT for problems with two symmetric sides, one-in-three SAT or exact cover for "exactly one" conditions, Hamiltonian cycle for orderings and tours, and 3-partition for packing and scheduling with small numbers.
- Try restriction first, then local replacement,, and design gadgets last.
- Test a reduction before you trust it. Build it for small satisfiable and unsatisfiable formulas and compare answers by brute force.
- If you need hardness of approximation, of counting or of parameterized versions, check what the reduction keeps. A Karp reduction keeps yes and no only; approximation needs gap-preserving maps, counting needs parsimonious maps, and parameterized hardness needs parameterized reductions.

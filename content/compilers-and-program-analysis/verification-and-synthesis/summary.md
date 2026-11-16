## What to remember

- The inputs that follow a path are the solutions of its [path condition](/path-condition/). Feasibility is NP-complete over fixed-width bit vectors and undecidable over unbounded integers with products. With $k$ tests in sequence a program can have $2^k$ paths; this [explosion](/path-explosion-problem/) is the limit of symbolic execution.
- [Concolic testing](/concolic-testing/) runs one test per feasible path and never reports a false alarm. It is complete only on a finite input domain with an exact solver, and proves nothing about paths it has not run. [Fuzzing](/coverage-guided-fuzzing/) has no completeness: every crash is real, and no crash proves nothing.
- [Delta debugging](/delta-debugging/) returns a 1-minimal failing input, not a smallest one, after at most $2\lceil \log_2 N \rceil$ tests when one element causes the failure and $(3N-2)(N-1)$ in the worst case.
- [Verification condition generation](/verification-condition-generation/) is sound, and exact on loop-free code; with loops it is only as good as its invariants.
- Whether a loop has an adequate inductive invariant is undecidable. [Houdini](/houdini-algorithm/) returns the largest inductive subset of $c$ candidates with at most $c + 1$ prover calls, and the [Farkas method](/farkas-invariant-generation/) finds a single linear inequality that is inductive over $\mathbb{Q}$, complete for the multipliers it tries.
- A single-path linear loop over $\mathbb{Q}$ has a [linear ranking function](/ranking-function-synthesis/) exactly when one linear program is feasible, so the question is in polynomial time; over $\mathbb{Z}$ it is coNP-complete. A program terminates if and only if it has a [transition invariant](/transition-invariants/) that is a finite union of well-founded relations.
- [Noninterference](/noninterference/) compares two runs. It is a 2-safety property, not a property of single traces, and [self-composition](/self-composition/) turns it into one Hoare triple over two renamed copies. Program equivalence is undecidable, so [verified compilation](/verified-compilation/) proves a compiler once, and [translation validation](/translation-validation/) checks each compilation but can reject a correct one.
- [Program synthesis](/program-synthesis/) is undecidable in general, and enumeration by size is a semi-decision procedure. [Bottom-up enumeration](/bottom-up-enumerative-synthesis/) returns a smallest program consistent with the examples. [CEGIS](/cegis/) terminates on a finite space of hole values, and whether a [sketch](/program-sketching/) has a completion is $\Sigma_2^P$-complete.
- Realizability of an LTL formula is 2EXPTIME-complete by the [Pnueli-Rosner theorem](/pnueli-rosner-theorem/), one exponential above LTL satisfiability,; GR(1) specifications are solved in time polynomial in the game graph.

| Method | Finds | Guarantee | Cost |
|---|---|---|---|
| Concolic testing (DART) | an input per feasible path | no false alarms; complete only on finite domains | $O(R(T + mC))$ |
| Generational search | the same runs in another order | as concolic testing | $O(R(T + mC + \log R))$ |
| Coverage-guided fuzzing | crashing inputs | none beyond the runs made | per run; queue at most $8E$ plus seeds |
| Delta debugging | a 1-minimal failing input | 1-minimal, not minimum | $(3N-2)(N-1)$ tests worst case |
| VC generation | formulas to prove | sound; exact without loops | $2^{O(n)}$ naive, $O(n^2)$ compact |
| Houdini | largest inductive subset of candidates | exact for the candidates | $c + 1$ prover calls |
| Farkas invariants | one linear invariant | complete over $\mathbb{Q}$ for the multiplier set $M$ | $(\lvert M\rvert + 1)^k$ linear programs |
| Linear ranking synthesis | a ranking function | decides existence over $\mathbb{Q}$ | one linear program |
| Bottom-up enumeration | smallest consistent program | complete up to the size bound | $O(k b^2)$, $O(k b^3)$ with ite |
| Sketching with CEGIS | values for the holes | terminates on finite hole spaces | $\Sigma_2^P$-complete |
| LTL reactive synthesis | a Mealy machine | decides realizability | $2^{2^{O(n)}}$ |

: Main methods. $R$ counts runs, $T$ steps of a run, $m$ conditions on a run and $C$ the cost of one solver call; $E$ counts edges for the fuzzer; $N$ is the size of the failing input; $n$ is the size of the program or formula; $c$ counts candidates, $k$ transitions (Farkas) or examples (enumeration), and $b$ kept programs.

## Choosing a method

To find bugs, start with coverage-guided fuzzing. Add concolic testing or generational search for branches on magic values, and generate from a grammar when the input has one. Shrink failing inputs with delta debugging. Test compilers with differential testing and equivalence modulo inputs.

To prove a property, write the invariants and let a verification condition generator and an SMT solver check them. Let Houdini filter guessed invariants, or solve for a linear one with Farkas' lemma. For termination, try a linear ranking function, then transition invariants. For two runs, build a product program with aligned loops.

To synthesize, give examples for small programs, a sketch when you know the shape, and types for recursion over data. For a controller, use GR(1) when you can.

## What to remember

- **Trees are easy, DAGs are hard.** Tiling a tree by dynamic programming gives a cover of least cost for the tile costs, in $\Theta(n)$ time for a fixed grammar. Maximal munch can lose: on `MEM(ADD(MUL(a,b),c))` it pays 15 where the optimum is 14. Optimal code for a DAG is NP-complete.
- **The Sethi-Ullman label.** A leaf that is a left operand has label 1, a right leaf label 0, and an inner node with child labels $\ell_1, \ell_2$ has label $\max(\ell_1, \ell_2)$ if they differ and $\ell_1 + 1$ if they are equal. The label of the root is the least number of registers that evaluates the tree without a store. Aho and Johnson extend the label to a table of least costs for each number of registers.
- **Coloring is hard, simplifying is cheap.** Deciding whether a program fits in $k$ registers, one for each name, is NP-complete for every fixed $k \ge 3$. Chaitin's simplify removes vertices of degree below $k$ and colors every $(k-1)$-degenerate graph. Briggs's optimistic coloring spills only a subset of Chaitin's spills.
- **Safe coalescing.** The Briggs test merges $u$ and $v$ when the merged node has fewer than $k$ neighbours of degree at least $k$. The George test merges $v$ into $u$ when every neighbour of $v$ already interferes with $u$ or has degree below $k$. Neither test can make a graph that simplify colors uncolorable by simplify.
- **SSA makes coloring easy.** The interference graph of a strict SSA program is chordal, so $\chi = \omega = \mathrm{MaxLive}$, and coloring the names in dominance order of their definitions uses exactly that many registers. Spilling and coalescing stay NP-hard on SSA programs.
- **Local and linear allocation.** In a block with clean values, evicting the value used furthest in the future gives the fewest loads; with dirty values the problem is NP-hard. Linear scan spills the fewest intervals, but intervals are larger than live ranges, so on programs it is a heuristic.
- **Scheduling bounds.** Scheduling a block with latencies is strongly NP-complete even with issue width 1. A modulo schedule needs $II \ge \mathrm{MII} = \max(\mathrm{ResMII}, \mathrm{RecMII})$ with $\mathrm{ResMII} = \max_r \lceil u_r / c_r \rceil$ and $\mathrm{RecMII} = \max_C \lceil \delta(C) / d(C) \rceil$, and $N$ iterations take $N + SC - 1$ passes of $II$ cycles.
- **When to compile.** Interpreting a run costs $a$, a compiled run costs $b < a$ and compiling costs $C$. The break-even rule compiles after $k = \lceil C/(a-b) \rceil$ runs and costs less than $2\,\mathrm{OPT}(n) + (a - b)$ for every number of runs $n$.

| Method | Problem | Time | Guarantee |
|---|---|---|---|
| Tree tiling by DP, BURS | instruction selection on a tree | $\Theta(n)$ for a fixed grammar | optimal for the tile costs |
| Maximal munch | instruction selection on a tree | $\Theta(n)$ for a fixed table | none, heuristic |
| Sethi-Ullman, Aho-Johnson | evaluation order and stores | $\Theta(n)$, $\Theta(nr)$ | optimal on trees in their machine model |
| Chaitin, Briggs | global register allocation | $O(n + m)$ a round after building | heuristic; Briggs spills a subset of Chaitin's |
| Briggs and George tests | coalescing | $O(\deg u + \deg v)$ a test | keeps simplify-colorability |
| Chordal coloring on SSA | allocation without spills | polynomial | exactly MaxLive registers |
| Linear scan | global register allocation | $O(n \log n)$ | optimal for its intervals, heuristic on programs |
| List scheduling | scheduling a block | polynomial | no empty cycle while work is ready; heuristic |
| Iterative modulo scheduling | software pipelining | $O(n^3)$ for the bounds, budgeted search | legal, $II \ge \mathrm{MII}$; often equal |
| Break-even rule | when to compile | $O(1)$ a run | below $2\,\mathrm{OPT} + (a - b)$ |

: The main methods of the chapter and what is proved about each.

## Choosing a method

For instruction selection, use a tree-tiling generator such as BURS. Maximal munch is simpler and does well when the large tiles are also the cheap ones.

For register allocation in an optimizing compiler, use optimistic coloring with iterated register coalescing, or allocate on SSA form, where spilling comes first and coloring needs no further spill. For a fast JIT compiler, use linear scan. Inside one block, use the furthest-next-use rule.

For scheduling, use list scheduling by height on blocks, a superblock or trace scheduler across branches, and iterative modulo scheduling for inner loops.

In a JIT compiler, interpret first and compile near the break-even point. Then specialize on the types and receivers seen at run time, and keep deoptimization ready for wrong guesses.

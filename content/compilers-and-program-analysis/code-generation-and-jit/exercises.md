1. ◦ Take the expression tree of $((a + b) \cdot (c - d)) + (e \cdot (f + g))$, with every leaf a variable in memory and no algebraic law. Compute the [Sethi-Ullman](/sethi-ullman-numbering/) label of every node. Then run GEN with $k = 2$ registers and write the code. How many instructions and stores does it emit, and how many with $k = 3$ and with $k = 1$?

2. ◦ A send site sees the receiver classes A, B, C, A, B, C, and so on, 30 sends in all. A monomorphic [inline cache](/inline-caching/) rebinds itself to the new class on each miss. A [polymorphic inline cache](/polymorphic-inline-cache/) appends a class on a miss while it has fewer than $k$ entries and turns megamorphic on a miss when it is full; a hit on its $j$-th entry costs $j$ class tests. Count the misses of the inline cache, and the misses, hits and class tests on hits of the polymorphic cache with $k = 3$. With $k = 2$, at which send does the site turn megamorphic?

3. ◦ Four objects start empty and get their properties in these orders: object 1 gets $x$, $y$, $z$; object 2 gets $x$, $z$; object 3 gets $z$, $x$; object 4 gets $x$, $y$. With [hidden classes](/hidden-classes/) that share a tree of transitions from one root shape, how many shapes exist at the end, counting the root? How many distinct shapes do the four objects have, and at which offset does each store $x$?

4. ◦ The library of [copy-and-patch compilation](/copy-and-patch-compilation/) has 69 stencils: one `const`, two `copy`, $14 \cdot 4 = 56$ `op`, two `br`, two `ret`, one `jump`, one `jump-next`, two `phi`, one `move` and one `goto`. The two operand kinds are a variable and a constant. Add a third kind, a value read from a separate parameter area, to every stencil that loads an operand. How many stencils does the library have now, and by which factor does the number of `op` stencils grow?

5. ◦ In a language with nested functions, `main` at depth 0 declares `x`, `f` at depth 1 inside `main` declares `y`, `g` at depth 2 inside `f` declares `z`, and `h` at depth 3 inside `g` reads `x`, `y` and `z` and then calls `f`. Using the static links of the [activation record](/activation-record/), how many links does each read follow? Which frame does the call put into the static link of `f`, and how many links does the caller follow to find it?

6. ◦ A function costs $a = 8$ to interpret, $b = 2$ to run compiled, and $C = 300$ to compile. Give the threshold of the break-even rule of [just-in-time compilation](/just-in-time-compilation/), and its cost, the best cost and their ratio for $n = 51$ and $n = 1000$ runs.

7. ◦ A [software pipelined](/software-pipelining/) loop has $II = 3$, and the last operation of one iteration starts at cycle 14. Run alone, one iteration takes 15 cycles. Give the stage count $SC$, the number of passes and cycles for $N = 40$ iterations, and the cycles without any overlap.

8. ◦ An [interference graph](/interference-graph/) has the vertices $a$ to $f$ and the edges $a$-$b$, $a$-$d$, $a$-$f$, $b$-$c$, $b$-$e$, $c$-$f$, $d$-$e$ and $e$-$f$. Show that two registers are enough. Then add the edge $c$-$e$ and find the least number of registers.

9. • Use the tile table of [maximal munch](/maximal-munch/), with its rule that a tie in size goes to the first pattern of the table. Tile $\mathrm{MEM}(\mathrm{ADD}(\mathrm{ADD}(\mathrm{MUL}(a, b), c), 8))$ by maximal munch and by [dynamic programming](/tree-dynamic-programming/), and give both costs. How many tilings does the tree have in all?

10. • With the tile table and the store cost $s = 3$ of [Aho-Johnson code generation](/aho-johnson-code-generation/), compute the cost vectors for $(a \cdot b + c) \cdot (d \cdot e + 4)$ with $r = 2$, $r = 3$ and $r = 4$. What does the best tiling with no limit on registers cost, and how many registers does it use?

11. • Run the bottom-up [local register allocator](/local-register-allocation/) with $k = 2$ on the block `x = a * b; y = b + c; z = x - c; w = y * a; v = z + w; ret v`, where `a`, `b` and `c` start in memory. Count the loads and the stores. Then count the loads in the clean model, and with $k = 3$.

12. • [Linear scan](/linear-scan-register-allocation/) gets the intervals $a = [0, 15]$, $b = [1, 3]$, $c = [2, 8]$, $d = [4, 10]$, $e = [5, 6]$, $f = [9, 14]$ and $g = [11, 13]$. Run it with $k = 2$, freeing intervals that end before the current start and spilling the interval with the largest end. Which intervals are spilled? Compare with the least number of spills, and repeat with $k = 3$.

13. • The cube graph has the vertices 0 to 7 and an edge between two numbers that differ in one bit. All spill costs are 1, a spill candidate has the least cost divided by its current degree, and ties go to the smallest number. Run the simplify phase of [Chaitin's allocator](/chaitin-register-allocation/) and of [optimistic coloring](/briggs-optimistic-coloring/) with $k = 2$ and with $k = 3$. Which vertices does each spill, and what is the chromatic number?

14. • An interference graph has the edges $u$-$a$, $u$-$b$, $u$-$c$, $v$-$b$, $v$-$c$, $v$-$d$, $a$-$e$, $a$-$d$, $b$-$e$, $b$-$d$, $c$-$e$ and $d$-$e$, and a copy relates $u$ and $v$. For $k = 4$ and for $k = 3$, apply the Briggs test and the George test in both directions of [conservative coalescing](/conservative-coalescing/).

15. • The program `entry: x = n; jump L` / `L: y = x * 2; z = y + x; w = y - 1; x = z + w; x = x % w; br x L E` / `E: ret x` reads the parameter `n`. Compute [liveness](/live-variable-analysis/), the interference graph, MaxLive and the chromatic number. Put the program in strict [SSA form](/static-single-assignment-form/) and repeat. Which graph is chordal?

16. • The block `a = p + 1; b = a; c = b * 2; d = a + c; e = d - b; ret e` has a copy `b = a`. Build the interference graph with the rule that a copy does not make its two ends interfere. Give MaxLive and the chromatic number. What changes if the copy is written `b = a + 0`?

17. • A machine issues one instruction per cycle. Loads have latency 3, multiplications 2 and additions 1. Schedule the block `a = load p; b = load q; c = a + b; d = c * 2; e = load r; f = e + 1; g = d + f` in program order, and by [list scheduling](/list-scheduling/) with the height of each instruction as its priority. Give both lengths, and say whether the second is optimal.

18. • A loop has the operations A (memory, latency 2), B (multiply, latency 3), C (ALU, latency 1), D (memory, latency 1) and E (ALU, latency 1), and the edges A→B, B→C, C→D, A→E and E→D within one iteration, and C→B with distance 2. The machine has one unit of each class. Find ResMII and RecMII, a legal modulo schedule at the least $II$ for [iterative modulo scheduling](/iterative-modulo-scheduling/), its stage count, and the cycles for $N = 50$ iterations.

19. • Change the loop of [tracing JIT compilation](/tracing-jit-compilation/) to `t = i % 4` and $n = 50$, with the rest as in its worked example. With threshold 5, which iteration is recorded, how many iterations complete in the trace, and how many side exits happen? Answer again with threshold 4, and give the final value of `s`.

20. ★ Let $L(r)$ be the fewest leaves of a binary tree whose Sethi-Ullman label is $r$. Prove that $L(1) = 1$ and $L(r) = 3 \cdot 2^{r-2}$ for $r \ge 2$.

21. ★ A complete binary tree has $2^h$ leaves and $1 \le k \le h$ registers. Prove that GEN emits $2^{h-k} - 1$ stores and $2^h + 2^{h-1} + 2^{h-k} - 2$ instructions.

22. ★ Prove that with $k = 2$, optimistic coloring colors every even cycle with no spill and spills exactly one vertex of every odd cycle, whatever the spill costs and the order of ties, while Chaitin's allocator spills at least one vertex of every cycle.

23. ★ Two trees share a product: $\mathrm{MEM}(\mathrm{ADD}(\mathrm{MUL}(a, b), c))$ and $\mathrm{ADD}(\mathrm{MUL}(a, b), d)$. With the tile table of maximal munch, $a$ and $b$ are loaded once and stay in registers. Compare computing the product once with recomputing it in each tree by MADD, and with tiling the two trees apart. Then make MADD cost 1 and compare again. What does this say about [DAG code generation](/dag-code-generation-np-completeness/)?

24. ★ For $a = 5$, $b = 1$ and $C = 100$, find the number of runs at which the break-even rule has its largest ratio to the best cost, and that ratio. A rule that compiles after $j$ runs is called the rule $j$. Find the $j$ that makes the largest ratio smallest, and that ratio.

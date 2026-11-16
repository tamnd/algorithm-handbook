1. ◦ A basic block reads `a = b + c`, `d = c + b`, `e = a - d`, `f = e * g`, `b = 7`, `h = b + c`, `k = b * 2`, `m = h - a`, `n = c + b`. Run [local value numbering](/local-value-numbering/) with commutative operands sorted, constant folding, and the identities $x - x \to 0$ and $x \cdot 0 \to 0$. Which instructions become copies or constants? Why do `h` and `m` stay as they are, and what happens to `n`?

2. ◦ A function reads `f(n) = 0` if `n == 0`, `f(n) = f(n - 1)` if `n` is odd, and `f(n) = 1 + f(n - 1)` if `n` is even and positive. Which of the two recursive calls is a [tail call](/tail-call-optimization/)? What does `f(10)` return, and how many frames are on the stack at the deepest point with and without tail call optimization, counting the frame of the first call?

3. ◦ A DAG has the edges A→B, A→C, A→D, B→E, C→E, C→F, D→F, E→G and F→G, with A the entry and G the exit, and the out-edges of each node taken in this order. Run the numbering of [Ball-Larus path profiling](/ball-larus-path-profiling/): give the number of paths from each node to G, the nonzero edge values, and the number of each entry-to-exit path. Which path has number 2?

4. ◦ A procedure has blocks E (the entry), A, B, C, D and X, and a profile with E→A 10, E→B 4, A→C 8, A→D 3, B→D 5, C→X 8 and D→X 7. Run the chain-building phase of [Pettis-Hansen code positioning](/pettis-hansen-code-positioning/), taking equal weights in the order listed, and give the chains, the layout with E first, and the total weight of the edges that fall through. Is any layout better?

5. ◦ A loop starts with `i = 0`, runs while `i < n`, computes `x = 12 * i + 5` and then sets `i = i + 3`. Apply [strength reduction](/strength-reduction/) to `x`: give the start value and the step of the new variable `t`. Then rewrite the loop test in terms of `t` so that `i` can be removed, and say when the new test is wrong on $w$-bit words.

6. ◦ Class `A` defines a method `m`. Class `B` extends `A` and overrides `m`, class `C` extends `A` without overriding it, and class `D` extends `B` without overriding it. The whole program creates objects of `A` and `C` only, and calls `p.m()` with `p` of static type `A`. Which targets does [class hierarchy analysis](/class-hierarchy-analysis/) give, and which does [rapid type analysis](/rapid-type-analysis/) give? When may the call become a direct call without a guard?

7. ◦ In [stochastic superoptimization](/stochastic-superoptimization/) on the toy machine with $N = 716$ instructions and $p_u = 0.2$, an instruction move fills an unused slot with an instruction. Compute its Hastings factor. If the move raises the cost by 1, with what probability is it accepted at $\beta = 4$ and at $\beta = 6$?

8. ◦ Which of these problems are decidable? (a) Find a smallest program equivalent to a given loop-free block on 4-bit words. (b) Decide whether a given instruction of a program on unbounded integers ever executes. (c) Decide whether a program with a fixed set of 8-bit variables, no memory and no input halts. Use the [full employment theorem](/full-employment-theorem/) and its tightness remarks.

9. • Run round-based [copy propagation](/copy-propagation/) on this program, then remove the dead copies. How many rounds does it take, counting the last round with no change, and what is left?

```
entry:
  b = a
  br p L R
L:
  c = b
  jump J
R:
  c = a
  jump J
J:
  d = c + b
  ret d
```

10. • Run the [Alpern-Wegman-Zadeck algorithm](/alpern-wegman-zadeck-value-numbering/) on the SSA loop below and give the congruence classes of the names in `h` and `body`. Then number the same code pessimistically by hashing, in the order written, giving a fresh number to a phi whose operand from `body` is not yet numbered. Which equalities does each method find? `k.1` always equals `p`; does either method see it?

```
entry:
  jump h
h:
  i.1 = phi [entry: 0, body: i.2]
  j.1 = phi [entry: 0, body: j.2]
  q.1 = phi [entry: 0, body: q.2]
  k.1 = phi [entry: 0, body: k.2]
  t = i.1 < n
  br t body exit
body:
  i.2 = i.1 + 1
  j.2 = j.1 + 1
  q.2 = i.1 + 1
  k.2 = k.1 + 2
  p = i.1 * 2
  jump h
exit:
  ret j.1
```

11. • In the program below, `a` and `b` are never assigned. Run [lazy code motion](/lazy-code-motion/) for `a + b` on the graph with one node per instruction and terminator. Where does busy code motion insert `t = a + b`, and where does lazy code motion insert it? Which computations become copies of `t`? Count the evaluations of `a + b` on the path B1, B2, B4, B5, B6 and on the path B1, B3, B4, B5, B6, before and after.

```
B1:
  br p B2 B3
B2:
  x = a + b
  jump B4
B3:
  jump B4
B4:
  jump B5
B5:
  y = a + b
  br q B6 B7
B6:
  z = a + b
  ret z
B7:
  ret y
```

12. • Run [aggressive dead code elimination](/aggressive-dead-code-elimination/) and liveness-based [dead code elimination](/dead-code-elimination/) on the program below, with `x` an unbounded integer parameter. What does each one remove? For which inputs does the result behave differently from the source, and why does the entry allow this?

```
entry:
  jump h
h:
  t = x != 0
  br t body done
body:
  x = x - 2
  jump h
done:
  ret 0
```

13. • A program has `main(n)` with the calls `x = f(2, n)`, `y = f(2, 5)` and `z = g(1)`; `f(p, q)` with `t = h(p, 3)` and `ret t + q`; `g(r)` with `s = r + 2` and `v = h(2, s)`; and `h(a, b)` with `m = a * b` and `ret m`. Run [interprocedural constant propagation](/interprocedural-constant-propagation/) with jump functions that are a constant, a formal or $\bot$, as in the entry. Give the value of each formal. Which formal holds the same constant on every call, yet is not found?

14. • A loop reads `B0: i = 0`, `B1: br i < n B2 B5`, `B2: br i % 2 B3 B4`, `B3: jump B4`, `B4: i = i + 1; jump B1`, `B5: ret`. Turn the back edge B4→B1 into a start edge ENTRY→B1 and a stop edge B4→EXIT, list the out-edges of each node with the original edges first, and number the paths with [Ball-Larus path profiling](/ball-larus-path-profiling/). Which path numbers does a run with $n = 3$ record, in order, and which does a run with $n = 0$ record?

15. • In the DAG of Exercise 3, a profile counts the paths ABEG 30, ACEG 5, ACFG 40 and ADFG 25 times. Compute the edge frequencies, add the edge G–A, and build a [maximum spanning tree](/maximum-spanning-tree/) with Kruskal's method, taking G–A first and equal weights in the order of the edge list. Move the increments to the chords and give their values. How many nonzero increments do the 100 runs execute with the values of Exercise 3 on their edges, and how many with the moved increments?

16. • A call graph has the call counts a–b 100, b–c 90, a–d 80, c–e 70, d–e 10 and main–a 5, in either direction. Order the procedures by the closest-is-best rule of [Pettis-Hansen code positioning](/pettis-hansen-code-positioning/). Give each merge with the weight between the two groups, and the final order. Which pair with calls ends up farthest apart?

17. • An [inliner](/function-inlining/) has a budget of 70 instructions of growth and five call sites with (growth, benefit) $s_1 = (40, 30)$, $s_2 = (30, 24)$, $s_3 = (25, 21)$, $s_4 = (20, 14)$ and $s_5 = (10, 6)$. Choose sites greedily by benefit per instruction, and then find the best choice exactly, as a [knapsack problem](/knapsack-problem/). How far is the greedy choice from the best?

18. • On the toy machine of [superoptimization](/superoptimization/), with $w = 4$, 716 instructions, inputs `r0` and `r1`, `r2 = r3 = 0`, logical shifts, and a shift by 4 or more giving 0, the target is `r0 = r0 - r1` with `r0` live-out. Which single instructions pass the tests $(r_0, r_1) = (0, 0)$, $(3, 0)$ and $(5, 5)$? For each wrong one, count the inputs among the 256 on which it fails, and give one more test that rejects all of them.

19. • The function `power(n, x)` returns 1 if `n == 0`, `x * power(n - 1, x)` if `n` is odd, and the square of `power(n / 2, x)` if `n` is even. [Partially evaluate](/partial-evaluation/) it for $n = 13$ static and $x$ dynamic, with the square written as `let y = power(n / 2, x) in y * y`. How many multiplications does the residual program do? How many if the square is written as `power(n / 2, x) * power(n / 2, x)`?

20. • The functions `upto(i, n)`, `map(sq, xs)` and `sum(xs)` build the list $[i, \ldots, n]$, square each element and add up a list. How many list cells does `sum(map(sq, upto(1, 10)))` allocate, and what does [deforestation](/deforestation/) turn it into? Why can the transformation of the entry not be applied to `let ys = map(sq, xs) in sum(ys) + length(ys)` as it stands?

21. ★ An e-graph holds the term $a_1 + (a_2 + (\cdots + a_n))$ for distinct leaves, and [equality saturation](/equality-saturation/) runs with associativity in both directions as its only rules. Show that the saturated e-graph has $n(n + 1)/2$ classes and $n + \binom{n+1}{3}$ e-nodes, and how many terms the root class represents. Check the counts for $n = 4$.

22. ★ Run the chain of [stochastic superoptimization](/stochastic-superoptimization/) with $L = 1$, so the only move replaces the single slot. There are $N = 2$ instructions with costs 1 and 3, an unused slot costs 2, $p_u = 1/2$ and $\beta = \ln 2$. Compute the target distribution $\pi$. Then show that without the Hastings factor the chain samples a distribution proportional to $q(s)\,\pi(s)$, and compute it.

23. ★ In the setting of Exercise 17, show that choosing sites by benefit per instruction can give an arbitrarily small fraction of the best benefit. Then show that the better of the greedy choice and the single best site that fits gets at least half of the best benefit, when every site fits the budget on its own.

24. ★ Show that the set of pairs (program, instruction) such that the instruction executes on some input is semi-decidable but not decidable, for programs on unbounded integers. Conclude that the set of instructions that never execute is not even semi-decidable, and say what this means for any [dead code elimination](/dead-code-elimination/).

25. ★ Homeomorphic embedding $s \trianglelefteq t$, the whistle of [supercompilation](/supercompilation/), holds if both are variables, or if $s \trianglelefteq t_i$ for some argument $t_i$ of $t$ (diving), or if $s$ and $t$ have the same function symbol and each argument of $s$ embeds in the matching argument of $t$ (coupling). A direct recursive test may visit the same pair of subterms many times. Give an algorithm that decides $s \trianglelefteq t$ in $O(|s|\,|t|)$ steps, counting each subterm pair once. Decide $f(x, g(y)) \trianglelefteq f(h(x), g(h(y)))$ and $f(a, b) \trianglelefteq f(b, a)$, with $a$ and $b$ constants.

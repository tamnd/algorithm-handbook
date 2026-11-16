1. ◦ Number the definitions of this program $d_1$ to $d_6$ in the order they appear. Which of them [reach](/reaching-definitions/) the start of B2, B3 and B4? Which variables are [live](/live-variable-analysis/) at the start of each block, with `n` a parameter?

```
B1:
  x = 0
  y = 1
  jump B2
B2:
  t = x < n
  br t B3 B4
B3:
  y = y * 2
  x = x + 1
  jump B2
B4:
  z = y + 1
  ret z
```

2. ◦ In the program below, which expressions are [available](/available-expressions/) at the start of B4? Which are [very busy](/very-busy-expressions/) at the end of B1, and what change to the code does that allow?

```
B1:
  t = a + b
  br c B2 B3
B2:
  u = a * b
  a = u - 1
  jump B4
B3:
  v = a * b
  jump B4
B4:
  w = a + b
  ret w
```

3. ◦ Facts are subsets of $\{a, b\}$. Let $f(X) = \{b\}$ if $a \in X$ and $f(X) = \emptyset$ otherwise, and let $g(X) = \{a\}$ if $X = \{a, b\}$ and $g(X) = \emptyset$ otherwise. For each function, say whether it is monotone, whether it distributes over $\cup$, whether it distributes over $\cap$, and whether it has the [gen-kill](/gen-kill-problem/) form $G \cup (X - K)$.

4. ◦ Which variables are live at the start of `head`? Which are strongly live, in the sense of the live variables entry, where a read counts only if the instruction that reads is useful? Which instructions does the difference let you delete?

```
entry:
  i = 0
  x = 0
  jump head
head:
  t = i < n
  br t body exit
body:
  x = x + 1
  i = i + 1
  jump head
exit:
  ret i
```

5. ◦ Two runs reach a join point with $(x, y) = (0, 1)$ and $(x, y) = (2, 0)$. Give the join in the [interval domain](/interval-domain/), in the [octagon domain](/octagon-domain/) and in the [polyhedra domain](/polyhedra-domain/). Does each result contain the point $(1, 1)$? The point $(2, 1)$?

6. ◦ At the start of the block `y = x; z = x - y`, interval analysis knows $x \in [-1, 1]$. What interval does it find for `z` statement by statement? What does the best transformer of the whole block, $\alpha \circ f \circ \gamma$ as on the [Galois connection](/galois-connection/) entry, give?

7. ◦ Over the facts $D = \{a, b, c\}$, represent a distributive function $f$ by edges: $0 \to 0$; $0 \to d$ for each $d \in f(\emptyset)$; and $d \to d'$ for each $d' \in f(\{d\}) - f(\emptyset)$. Draw the edges for $f(X) = \{a\} \cup (X - \{b\})$, as in the [IFDS framework](/ifds-framework/). Then read $f(\{b, c\})$ off the edges.

8. ◦ Run [constant propagation](/constant-propagation-problem/) on this loop, where `t` is an unknown parameter, once starting every block except `entry` at $\top$ (no information yet) and once starting them at $\bot$ (not a constant). What value of `x` does each run give at `exit`?

```
entry:
  x = 1
  jump head
head:
  br t body exit
body:
  x = 2 - x
  jump head
exit:
  ret x
```

9. ◦ Give the [static slice](/pdg-slicing/) of this program for `x` at line 11, by reachability in its program dependence graph. Which lines are left out?

```
1   read n
2   i = 0
3   x = 0
4   y = 0
5   while i < n:
6     if i % 2 == 0:
7       x = 1
      else:
8       x = 2
9     y = y + i
10    i = i + 1
11  write x
```

10. • Analyze `x = 100; while x > 0: x = x - 3` with intervals, using the standard [widening](/widening-operator/) at the loop head. Give the head and exit intervals after widening and after one [narrowing](/narrowing-operator/) step. The only value of `x` at the exit is $-2$; which product of domains would find it?

11. • The sign domain has the elements $\bot$, *neg*, *zero*, *pos* and $\top$, with *neg*, *zero* and *pos* meaning $x < 0$, $x = 0$ and $x > 0$. Define $\alpha$ and $\gamma$ to sets of integers and check that they form a Galois connection. Give the best transformer of `x = x - 1` on each of the five elements, and $\alpha(\{-2, 0\})$.

12. • Take the product of the sign domain of exercise 11 with parity (*even*, *odd*). After a test `x == 0` that only the sign part understands, the state is (*zero*, $\top$). Apply `x = x + 1` component by component, first without reducing the pair and then after the [reduction](/reduced-product/). Is the result of the first way already reduced?

13. • Interval analysis knows $x \in [0, 10]$ before `if x > 5: y = x else: y = 10 - x`. What interval does it find for `y` after the join when the branch condition refines `x` in each arm, and what when it does not? What is the exact set of values of `y`?

14. • An octagon over the rationals has the constraints $x \ge 0$, $y \ge 0$, $y \le 2$ and $x - y \le 1$. Give the bounds on $x$, $y$, $x - y$ and $x + y$ after closure, and for each new bound the constraints it is derived from.

15. • In the program below, block `u` has no edge into it except its own. Expressions are only `a + b`. Compute the maximal fixed point of available expressions with every block except `entry` started at $\top$, and the meet over all paths. Do they agree at `r`? What is the usual fix, and why does the [MOP-MFP coincidence theorem](/mop-mfp-coincidence-theorem/) not apply?

```
entry:
  e = a + b
  jump r
u:
  a = 0
  br c u r
r:
  f = a + b
  ret f
```

16. • Very busy expressions are a backward must problem, with the greatest fixed point as answer and $\emptyset$ at the end. Take the expressions $E = \{x + 1, y * 2\}$ of the program below. Compute the maximal fixed point at the start of `L` and at the end of `entry`, and the meet over all paths to the end of the procedure, where a meet over no paths is $E$. Which answer is safe for hoisting `x + 1` into `entry`?

```
entry:
  br c L exit
L:
  x = y * 2
  jump L
exit:
  z = x + 1
  ret z
```

17. • Run the program of exercise 9 on $n = 2$. Give its [dynamic slice](/dynamic-slicing/) for `x` at line 11. Agrawal and Horgan's first method takes the static slice in the dependence graph restricted to the lines that ran; what does it give, and which lines does it add? What is the dynamic slice for $n = 0$?

18. • In the [IDE framework](/ide-framework/) for linear constant propagation, let $f = \lambda l.\, 2l + 1$ and $g = \lambda l.\, 3l - 1$. Compute $f \circ g$, $g \circ f$ and the meet $f \sqcap g$. A procedure with parameter `a` runs `if c: x = 2 * a + 1 else: x = 3 * a - 1` and then `y = 2 * x + 1`. What does the analysis find for `y` when the procedure is called with $a = 2$, and with $a = 3$?

19. • Use [strictness analysis](/strictness-analysis/) on `g x y = if x == 0 then y else g (x - 1) (y + 1)` and `h x y = if x == 0 then 0 else h (x - 1) y`. Compute the abstract functions by iteration from the constant function 0, and say in which arguments each function is strict. Check each answer against the real functions.

20. ★ Generalize the tightness example of the [Kam-Ullman bound](/kam-ullman-iteration-bound/) to every depth $d \ge 1$. The flow graph has the edges entry→$H_1$ and $H_1$→exit; for $1 \le j < d$ the edges $H_j \to H_{j+1}$, $H_{j+1} \to L_j$ and $L_j \to H_j$; and the innermost loop $H_d \to X$, $X \to B$, $B \to H_d$. Block $X$ holds the only definition. Round robin visits entry, $H_1, \ldots, H_d$, $X$, $B$, $L_{d-1}, \ldots, L_1$, exit, which is a reverse postorder. Prove that reaching definitions needs exactly $d + 2$ passes.

21. ★ A flow graph has the edges s→a, s→b, a→b, a→c, b→c, c→a and c→b, with entry s. Show that it is not [reducible](/reducible-flow-graph/). Find two depth-first searches from s whose reverse postorders give different values of the depth $d$ of the Kam-Ullman bound, and give $d$ and the bound for each.

22. ★ Let $(\alpha, \gamma)$ be a Galois connection between sets of states and an abstract domain, and let $f$ and $g$ be monotone concrete transformers. Prove that $\alpha \circ g \circ f \circ \gamma \sqsubseteq (\alpha \circ g \circ \gamma) \circ (\alpha \circ f \circ \gamma)$, give a condition on $f$ under which equality holds, and use exercise 6 to show that the inequality can be strict.

23. ★ Prove that two Galois connections compose: from sets of integers to intervals by $(\alpha_1, \gamma_1)$, and from intervals to signs by $(\alpha_2, \gamma_2)$, the pair $(\alpha_2 \circ \alpha_1, \gamma_1 \circ \gamma_2)$ is a Galois connection. Define $\alpha_2$ and $\gamma_2$, and show that the best sign transformer of $f$ equals $\alpha_2 \circ f^\sharp \circ \gamma_2$, where $f^\sharp$ is the best interval transformer. Then analyze `x = 1; y = x - 1` once with signs and once with intervals, mapping the final interval to a sign. Do the answers agree?

24. ★ In this program, `f` returns its first argument after `m` recursive calls. Run constant propagation across procedures with [call strings](/context-sensitivity/) of length at most $k$, merging contexts that agree on their last $k$ call sites. Show that for every $k \ge 0$ it finds `r1` and `r2` not constant. Then show that the [functional approach](/functional-approach-interprocedural/), with one summary per input value, finds $r1 = 1$ and $r2 = 2$.

```
main(n):
  r1 = f(1, n)       # call site s1
  r2 = f(2, n)       # call site s2
  ret r1 + r2
f(a, m):
  if m == 0: return a
  r = f(a, m - 1)    # call site s3
  return r
```

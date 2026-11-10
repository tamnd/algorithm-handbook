## What to remember

- The **Shannon expansion** $f = \bar{x}\, f|_{x=0} \vee x\, f|_{x=1}$ is the recursion behind every BDD algorithm. A function depends on $x$ exactly when its two [cofactors](/cofactor/) differ.
- A **reduced ordered BDD** is an ordered BDD to which the two [reduction rules](/bdd-reduction-rules/) no longer apply: no node has equal children, and no two nodes have the same variable and children. For a fixed order it is **unique** ([canonicity](/bdd-canonicity/)), and it is the smallest ordered BDD of its function in that order. With a unique table, equal functions are the same node, so an equality test takes $O(1)$ time.
- **APPLY** combines $f$ and $g$ with any binary operator in $O(|f| \cdot |g|)$ expected time, and the result has at most $|f| \cdot |g|$ nodes. The bound comes from the [computed table](/computed-table/): without it the recursion follows paths, not pairs of nodes, and can take exponential time. [ITE](/ite-operator/) takes $O(|f| \cdot |g| \cdot |h|)$.
- **Counting, choosing and testing are cheap; quantifying is not.** Model counting is $O(|f|)$ arithmetic operations, finding one model is $O(n)$, and restriction is $O(|f|)$. But $\exists x\, f = f|_{x=0} \vee f|_{x=1}$ costs $O(|f|^2)$ and can square the size, and several quantified variables can make it exponential.
- **The order decides the size.** The function $x_1x_2 \vee \cdots \vee x_{2k-1}x_{2k}$ has $2k+2$ nodes in the natural order and $2^{k+1}$ when the odd variables come first. Deciding whether an order reaches a given size is NP-complete; Friedman and Supowit find the best order in $O(n^2 3^n)$ time, and [sifting](/bdd-sifting/) is the heuristic in practice.
- **Some functions are hard under every order.** The middle bit of an $n$-by-$n$ product needs at least $2^{n/8}$ nodes, and the hidden weighted bit function about $2^{n/5}$, while a [free BDD](/free-binary-decision-diagram/) computes HWB with at most $n(n+1)+2$ nodes.
- **Change the reduction rule and you get a new diagram.** The [zero-suppressed BDD](/zero-suppressed-bdd/) removes nodes whose high edge goes to the empty family, so a skipped element is absent instead of free; it is small for families of few small sets.

## Operations side by side

| Operation | Time | Size of the result |
|---|---|---|
| [Evaluate](/ordered-binary-decision-diagram/) at one input | $O(n)$ | — |
| [Reduce](/bdd-reduction-rules/) an ordered BDD | $O(p)$ expected | at most $p$ |
| Equality of two ROBDDs | $O(1)$ | — |
| [APPLY](/bdd-apply/) $f \circ g$ | $O(\lvert f\rvert \lvert g\rvert)$ expected | at most $\lvert f\rvert \lvert g\rvert$ |
| [ITE](/ite-operator/) $(f, g, h)$ | $O(\lvert f\rvert \lvert g\rvert \lvert h\rvert)$ expected | at most $\lvert f\rvert \lvert g\rvert \lvert h\rvert$ |
| [Model count](/bdd-satisfy-count/) | $O(\lvert f\rvert)$ arithmetic operations | a number of up to $n+1$ bits |
| [$\exists x\, f$](/bdd-quantification/), one variable | $O(\lvert f\rvert^2)$ expected | $O(\lvert f\rvert^2)$ |
| [Compose](/bdd-compose/) $f[x_i := g]$ | $O(\lvert f\rvert^2 \lvert g\rvert)$ expected | $O(\lvert f\rvert^2 \lvert g\rvert)$ |
| [Friedman–Supowit](/friedman-supowit-ordering/) best order | $O(n^2 3^n)$ from the truth table | the minimum |

: The main operations on reduced ordered BDDs with one variable order; $p$ is the number of nodes of an unreduced input, $n$ the number of variables. "Expected" refers to hashing in the unique and computed tables.

## Choosing a method

- To test whether two circuits or formulas are equal, build both ROBDDs in the same order and compare pointers. If the BDDs blow up, fall back on a [SAT](/sat/) check, as in [Boolean equivalence checking](/boolean-equivalence-checking/).
- Choose the first order by structure: put related inputs next to each other, such as the bits of the same position of two words, and control inputs before data inputs. Then let the package run [sifting](/bdd-sifting/) when the diagram grows.
- Use [ITE](/ite-operator/) with [complemented edges](/complemented-edges/) as the single core operation; it gives every binary operator, negation in constant time, and a diagram that can be as small as half the plain one.
- When only some inputs matter, simplify with restrict or constrain from [generalized cofactors](/generalized-cofactor/), and check that the result is in fact smaller.
- For families of sparse sets, as in combinatorics, use [ZDDs](/zero-suppressed-bdd/). For functions with numeric values, use [algebraic decision diagrams](/algebraic-decision-diagram/); for arithmetic circuits such as multipliers, word-level diagrams such as [binary moment diagrams](/binary-moment-diagram/).

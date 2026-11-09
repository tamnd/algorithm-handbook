## What to remember

- A [recurrence relation](/recurrence-relation/) together with its initial values defines a sequence completely. Solving it means finding a [closed form](/closed-form-solution/) or at least the order of growth; the base case changes only the constant factor of a divide-and-conquer solution.
- The [iteration method](/iteration-method/) and the [recursion tree](/recursion-tree-method/) turn $T(n) = aT(n/b) + f(n)$ into the sum $\sum_{j} a^j f(n/b^j)$ plus about $n^{\log_b a}$ for the leaves. Level $j$ has $a^j$ nodes, each of cost $f(n/b^j)$.
- The [substitution method](/substitution-method/) proves a guess by induction. When the guess $cn^k$ fails by a lower-order term, subtract a lower-order term from the guess, $cn^k - dn$, rather than give up the guess.
- The [master theorem](/master-theorem/) compares $f(n)$ with the [watershed function](/watershed-function/) $n^{w}$, $w = \log_b a$. If $f = O(n^{w-\varepsilon})$, $T = \Theta(n^w)$. If $f = \Theta(n^w \lg^k n)$ with $k \ge 0$, $T = \Theta(n^w \lg^{k+1} n)$. If $f = \Omega(n^{w+\varepsilon})$ and $af(n/b) \le cf(n)$ for a $c < 1$, $T = \Theta(f(n))$. Functions between the cases, such as $n^w/\lg n$, are not covered.
- A [change of variables](/change-of-variables/) such as $m = \lg n$ turns $\sqrt n$ into $m/2$, and dividing by a factor, $S = T/n$, can turn a multiplicative recurrence into an additive one.
- A [linear recurrence with constant coefficients](/linear-recurrences-with-constant-coefficients/) $a_n = c_1 a_{n-1} + \cdots + c_d a_{n-d}$ has solutions $\sum_r P_r(n)\, r^n$, one term per root $r$ of the characteristic polynomial, with $P_r$ a polynomial of degree less than the multiplicity of $r$. For Fibonacci, [Binet's formula](/binet-formula/) gives $F_n = (\varphi^n - \psi^n)/\sqrt 5$ with $\varphi = (1+\sqrt5)/2$.
- The [Akra-Bazzi theorem](/akra-bazzi-theorem/) solves $T(x) = \sum_i a_i T(b_i x) + g(x)$: find $p$ with $\sum_i a_i b_i^p = 1$, and $T(x) = \Theta\big(x^p (1 + \int_1^x g(u)/u^{p+1}\,du)\big)$.
- The [smoothness rules](/smoothness-rules/) allow you to solve for $n$ a power of 2 only, when $T$ is non-decreasing and the answer $f$ satisfies $f(2n) = O(f(n))$.

## Recurrences that recur

| Recurrence | Solution | Example |
|---|---|---|
| $T(n) = T(n/2) + 1$ | $\Theta(\log n)$ | [binary search](/binary-search/) |
| $T(n) = T(n/2) + n$ | $\Theta(n)$ | halving with a linear pass |
| $T(n) = 2T(n/2) + 1$ | $\Theta(n)$ | [tree traversal](/tree-traversal/) of a balanced tree |
| $T(n) = 2T(n/2) + n$ | $\Theta(n \log n)$ | [merge sort](/merge-sort/) |
| $T(n) = 3T(n/2) + n$ | $\Theta(n^{\lg 3}) \approx \Theta(n^{1.585})$ | [Karatsuba multiplication](/karatsuba-multiplication/) |
| $T(n) = 7T(n/2) + n^2$ | $\Theta(n^{\lg 7}) \approx \Theta(n^{2.807})$ | [Strassen's algorithm](/strassen-algorithm/) |
| $T(n) = T(n-1) + 1$ | $\Theta(n)$ | a recursive scan |
| $T(n) = T(n-1) + n$ | $\Theta(n^2)$ | [selection sort](/selection-sort/) |
| $T(n) = 2T(n-1) + 1$ | $2^n - 1$ with $T(0) = 0$ | [Tower of Hanoi](/tower-of-hanoi/) |
| $T(n) = T(n-1) + T(n-2) + 1$ | $\Theta(\varphi^n)$ | naive recursive Fibonacci |

: Recurrences met in later volumes and their solutions. The first six are divide-and-conquer recurrences that the master theorem solves. The last four shrink $n$ by subtraction, not by division, and the master theorem does not apply to them; iteration or the characteristic polynomial does.

## Solving a recurrence in practice

- Write the recurrence from the program, including the cost of the split and the merge, and check it on a small $n$ by hand.
- Try the master theorem first. If $f$ falls between the cases, or the subproblems have unequal sizes, use a recursion tree or the Akra-Bazzi theorem.
- Draw a recursion tree to guess, and look at how the level sums change: growing geometrically, the leaves dominate; shrinking geometrically, the root dominates; equal, multiply by the number of levels.
- Prove the answer by substitution when the result matters, or at least compute $T(n)$ for a few $n$ with a program and compare.
- Subtracting a constant from $n$ and dividing $n$ by a constant are different. $T(n) = 2T(n-1) + 1$ is exponential; $T(n) = 2T(n/2) + 1$ is linear.

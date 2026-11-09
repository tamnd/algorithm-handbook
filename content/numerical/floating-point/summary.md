## What to remember

- A finite float is $\pm M \beta^{e-p+1}$ with an integer $M < \beta^{p}$. In binary64, $p = 53$, the [unit roundoff](/machine-epsilon/) is $u = 2^{-53} \approx 1.11 \times 10^{-16}$, and [machine epsilon](/machine-epsilon/) $\varepsilon = 2u = 2^{-52}$ is the gap above 1. The gap $\mathrm{ulp}(x)$ doubles from one binade to the next, so the relative spacing stays between $2^{-53}$ and $2^{-52}$.
- [IEEE 754](/ieee-754/) requires $+$, $-$, $\times$, $/$, $\sqrt{\ }$ and the [FMA](/fused-multiply-add/) to be correctly rounded: the result is the exact result rounded once. Hence the [standard model](/floating-point-model/) $\mathrm{fl}(x \mathbin{op} y) = (x \mathbin{op} y)(1 + \delta)$ with $|\delta| \le u$, when there is no underflow or overflow, and $n$ such factors combine into $1 + \theta_n$ with $|\theta_n| \le \gamma_n = nu/(1 - nu)$.
- The [condition number](/condition-number/) belongs to the problem; for a scalar function it is $|x f'(x)/f(x)|$. [Backward stability](/backward-error-analysis/) belongs to the algorithm. To first order, forward error $\lesssim$ condition number $\times$ backward error.
- Subtracting close numbers is exact when $y/2 \le x \le 2y$ ([Sterbenz](/sterbenz-lemma/)), but it multiplies the relative errors the operands already carry by $(|x| + |y|)/|x - y|$. This [catastrophic cancellation](/catastrophic-cancellation/) is the usual cause of instability, and the cure is to rewrite the formula.
- The rounding error of a sum or a product of two floats is itself a float (barring overflow, and underflow for products). [TwoSum](/two-sum/) finds it in 6 operations, [Fast2Sum](/fast-two-sum/) in 3 when the exponent of $a$ is at least that of $b$, and [TwoProduct](/two-product/) in 2 with an FMA or 17 without.
- Left-to-right summation has error at most $\gamma_{n-1}\sum|x_i|$, [pairwise summation](/pairwise-summation/) $\gamma_{\lceil \log_2 n \rceil}\sum|x_i|$, and [Kahan summation](/kahan-summation/) $(2u + O(nu^2))\sum|x_i|$. Divided by $|\sum x_i|$, each bound is multiplied by the condition number $\sum|x_i|/|\sum x_i|$ of the sum.
- Seventeen significant digits always identify a binary64 value, and nine a binary32 value. The [shortest round-trip string](/shortest-round-trip-representation/) is often much shorter; [Ryu](/ryu/) finds it with fixed-width integers for every input.
- IEEE 754 only recommends correct rounding for $\exp$, $\log$, $\sin$ and the other elementary functions. The [table-maker's dilemma](/table-maker-dilemma/) is why: the exact value can lie extremely close to a rounding boundary.

## Summation methods side by side

| Method | Error bound (round to nearest, no overflow) | Cost | Notes |
|---|---|---|---|
| Recursive, left to right | $\gamma_{n-1}\sum\lvert x_i\rvert$ | $n - 1$ additions | streaming, $O(1)$ space |
| [Pairwise](/pairwise-summation/) | $\gamma_{\lceil\log_2 n\rceil}\sum\lvert x_i\rvert$ | $n - 1$ additions | $\Theta(\log n)$ stack; NumPy and Julia use a blocked form |
| [Kahan](/kahan-summation/) | $(2u + O(nu^2))\sum\lvert x_i\rvert$ | $4n$ flops | fails when a term is larger than the running sum |
| [Neumaier](/neumaier-summation/) | $u\lvert s\rvert + \gamma_{n-1}^2\sum\lvert x_i\rvert$ | about $4n$ flops and a comparison | Python's built-in `sum` since 3.12 |
| Sum2, a [TwoSum](/two-sum/) cascade | $u\lvert s\rvert + \gamma_{n-1}^2\sum\lvert x_i\rvert$ | $7n$ flops | no branches |
| [Expansions](/shewchuk-expansion-sum/), `math.fsum` | correctly rounded | $O(n)$ typical | cost grows with the spread of the exponents |
| [Long accumulator](/kulisch-accumulator/) | correctly rounded | $O(n)$ | wide fixed-point register; order independent |
| [Reproducible](/reproducible-summation/), $K$ folds | far below recursive | about $4K n$ flops | same bits for every order and every split |

: Methods for adding $n$ floats $x_1, \ldots, x_n$ with exact sum $s$. The bounds are worst-case bounds; on random data the error of recursive summation grows more like $\sqrt{n}\,u$.

## Choosing a method

- Before you blame the algorithm, estimate the condition number. If the problem is ill conditioned, no rearrangement of the same arithmetic helps; reformulate the problem or carry more precision.
- When a formula subtracts two computed values that are nearly equal, rewrite it. Use `log1p`, `expm1` and `hypot`, the stable form of the [quadratic formula](/quadratic-formula/), and the [log-sum-exp trick](/log-sum-exp-trick/) for sums of exponentials.
- For a long sum, pairwise summation is free and usually enough. Use Kahan's method when the terms are known to be smaller than the running sum, Neumaier's otherwise, and `math.fsum` or a long accumulator when the answer must be correctly rounded or must not depend on the order.
- When a few steps need more precision than binary64 gives, use [double-double arithmetic](/double-double-arithmetic/) or a compensated algorithm such as [Dot2](/dot2-compensated-dot-product/) before reaching for arbitrary precision.
- After a computation, compare floats with a tolerance in ulps or relative error, chosen from an error bound, not with `==`.
- To print a float so that it reads back exactly, use the shortest round-trip form that your language provides, or 17 significant digits for binary64.
- Do not let a compiler reassociate floating-point code that relies on the order of operations: an optimizer that treats addition as associative turns Kahan summation into a plain loop.

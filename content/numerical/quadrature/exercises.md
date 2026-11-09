1. ◦ Compute the [midpoint](/midpoint-rule/), [trapezoidal](/trapezoidal-rule/) and [Simpson](/simpsons-rule/) approximations to $\int_1^2 dx/x = \log 2$, each with two subintervals of width $\tfrac12$. Give the three errors and their signs. Then check that $\tfrac13(2M + T)$ equals Simpson's rule with four subintervals.

2. ◦ On $[-1, 1]$, find the [degree of precision](/degree-of-precision/) of the rule $Q(f) = \tfrac12 f(-1) + \tfrac32 f(\tfrac13)$. Which kind of Gauss rule is it?

3. ◦ The two-point Gauss-Legendre rule on $[-1, 1]$ is $f(-1/\sqrt3) + f(1/\sqrt3)$. Compute its error on $x^4$ and compare it with the error of Simpson's rule $\tfrac13(f(-1) + 4f(0) + f(1))$ on the same monomial.

4. ◦ The [composite](/composite-quadrature/) trapezoidal rule with $m = 10$ panels has error $4 \times 10^{-4}$ on a smooth integrand, and so does the composite Simpson rule with $m = 10$ on another one. Assuming each error follows its leading term, how many panels does each rule need for an error of $10^{-6}$?

5. ◦ [Monte Carlo integration](/monte-carlo-integration/) estimates $\int_0^1 x^2\,dx$ from $N$ uniform points. Compute $\sigma^2 = \operatorname{Var}(X^2)$, the root mean square error for $N = 100$, and the $N$ that brings it down to $10^{-3}$.

6. ◦ Give the degree of precision of the 7-point Gauss rule $G_7$, of its [Kronrod extension](/gauss-kronrod-quadrature/) $K_{15}$ and of the 15-point Gauss rule. How many evaluations does the adaptive driver spend if it performs 10 splits with the G7-K15 pair?

7. ◦ Build the [Romberg](/romberg-integration/) table $R[i, k]$ for $\int_0^1 x^4\,dx$ with $1, 2, 4$ subintervals, in exact fractions. Which entry is exact, and why?

8. ◦ The first three points of the van der Corput sequence are $0, \tfrac12, \tfrac14$. Compute their star [discrepancy](/discrepancy/), the bound that the [Koksma-Hlawka inequality](/koksma-hlawka-inequality/) gives for the error of their average on $f(x) = x^2$, and the actual error.

9. • The corrected trapezoidal rule is $T_m - \tfrac{h^2}{12}\bigl(f'(b) - f'(a)\bigr)$. Show that it integrates cubics exactly but not $x^4$, using the [Euler-Maclaurin formula](/euler-maclaurin-formula/) or a direct check on one panel. Apply it to $\int_1^2 dx/x$ with $m = 2$ and compare its error with Simpson's rule on the same three values.

10. • Use the Euler-Maclaurin formula to estimate $\sum_{k \ge 1} 1/k^2$ as $\sum_{k=1}^{9} 1/k^2$ plus the integral from 10 to infinity and two correction terms. Give the corrections, the error against $\pi^2/6$, and the next term of the series.

11. • Find the weights of the open [Newton-Cotes](/newton-cotes-formulas/) rule on $[0, 4]$ with nodes $1, 2, 3$ from the moment equations. What is its degree of precision, and what is unusual about its weights?

12. • The three-point Gauss-Legendre rule on $[0, 1]$ has nodes $\tfrac12$ and $\tfrac12 \pm \tfrac{\sqrt{15}}{10}$ with weights $\tfrac49$ and $\tfrac{5}{18}$. Apply it to $\int_0^1 dx/(1 + x^2) = \pi/4$ and compare its error with Simpson's rule on $0, \tfrac12, 1$.

13. • Construct the two-point [Gaussian quadrature](/gaussian-quadrature/) rule for the weight $w(x) = x$ on $[0, 1]$: find the monic orthogonal polynomial of degree 2, its zeros, and the weights. Check that the rule integrates $x \cdot x^3$ exactly and find its error on $x \cdot x^4$.

14. • The two-point [Gauss-Laguerre](/gauss-laguerre-quadrature/) rule has nodes $2 \mp \sqrt2$ and weights $(2 \pm \sqrt2)/4$. Show that it gives exactly $\tfrac47$ for $\int_0^\infty e^{-x}/(1 + x)\,dx = 0.5963474\ldots$. Then compute the errors for $n = 4, 8, 16, 32$ with a [Golub-Welsch](/golub-welsch-algorithm/) program, and describe how they fall with $n$.

15. • In [tanh-sinh quadrature](/tanh-sinh-quadrature/) on $[-1, 1]$, the node for parameter $t$ is $x = \tanh u$ with $u = \tfrac{\pi}{2}\sinh t$. Compute the distance $\delta = 1 - x$ for $t = 2, 3, 4$. What does the formula $1 - \tanh u$ give in binary64 at $t = 3$ and $t = 4$, and what should the program compute instead?

16. • Find the Kronrod extension of the one-point Gauss rule $2f(0)$ on $[-1, 1]$: three nodes, including $0$, with degree $3 \cdot 1 + 2 = 5$. Which known rule is it? On $\int_{-1}^1 e^x\,dx$, compare the estimate $|K - G|$ with the true error of $K$.

17. • A [sparse grid](/sparse-grid-quadrature/) built from nested [Clenshaw-Curtis](/clenshaw-curtis-quadrature/) rules with $1, 3, 5, 9, \ldots$ points adds $1, 2, 2, 4, \ldots$ new points per level. Count the distinct points of the Smolyak rule with $s = 3$ and level $\ell = 2$, and compare with the [product rule](/product-quadrature/) of the 5-point rule. Repeat for $s = 10$.

18. • Estimate the volume of the unit ball in $\mathbb{R}^{10}$ by sampling the cube $[-1, 1]^{10}$ and counting hits. What fraction of points hit, and about how many samples give a relative standard error of 1%?

19. • For $I_\omega = \int_0^1 \frac{\cos \omega x}{1 + x}\,dx$, integrate by parts twice to get the two-term asymptotic approximation used in [oscillatory integration](/oscillatory-integration/). For $\omega = 50$, give the one-term and two-term approximations and their errors.

20. ★ Prove that an $n$-point rule on $[a, b]$ with a positive weight function and the node $a$ prescribed cannot have degree $2n - 1$, and that a rule with both ends prescribed cannot have degree $2n - 2$. This shows that [Gauss-Radau](/gauss-radau-quadrature/) and [Gauss-Lobatto](/gauss-lobatto-quadrature/) rules reach the best possible degree.

21. ★ Let $Q_n$ be the Gauss rule for a weight $w$ and let $\pi_n$ be the monic orthogonal polynomial of degree $n$. Prove that $E_n(x^{2n}) = \int \pi_n^2 w$. Evaluate it for Gauss-Legendre with $n = 4$, where $\pi_4 = x^4 - \tfrac67 x^2 + \tfrac{3}{35}$.

22. ★ The function $f(x) = 1/(2 + \cos x)$ has Fourier coefficients $c_k = r^{|k|}/\sqrt3$ with $r = \sqrt3 - 2$, and $\int_0^{2\pi} f = 2\pi/\sqrt3$. Prove that the periodic trapezoidal rule with $m$ points has error $T_m - I = \frac{4\pi}{\sqrt3}\,\frac{r^m}{1 - r^m}$, and evaluate it for $m = 4, 8, 16$.

23. ★ Write the Romberg entry $R[3, 3]$ on $[0, 1]$ as a rule on the nine points $j/8$. Show that its weights are positive and find its degree of precision. Compare with the 9-point closed Newton-Cotes rule.

24. ★ Monte Carlo with importance sampling draws $X$ from a density $p$ and averages $f(X)/p(X)$. Prove that its variance is $\int f^2/p - I^2$ and that $p = |f|/\int|f|$ minimizes it. For $f(x) = e^x$ on $[0, 1]$ and $p(x) = \tfrac23(1 + x)$, compute the variance and compare it with plain sampling.

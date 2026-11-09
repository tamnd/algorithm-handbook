1. ◦ [Bisection](/bisection-method/) starts on $[1, 2]$ with $f(1) < 0 < f(2)$ and stops when the bracket is no longer than $2\delta$, then returns the midpoint. How many halvings does it make for $\delta = 10^{-6}$?

2. ◦ Run three steps of [Newton's method](/newton-raphson-method/) on $f(x) = x^2 - 3$ from $x_0 = 2$ in exact fractions. How far is the third iterate from $\sqrt 3$?

3. ◦ Compute the efficiency index $q^{1/w}$ of Newton's method, the [secant method](/secant-method/), [Halley's method](/halley-method/) and [Steffensen's method](/steffensen-method/), counting each evaluation of $f$, $f'$ or $f''$ as one. Which is largest?

4. ◦ Use the [rational root theorem](/rational-root-theorem/) to list the candidates for rational roots of $2x^3 - 3x^2 - 11x + 6$, then find all three roots.

5. ◦ What is the [multiplicity](/multiplicity-of-roots/) of the root $x = 1$ of $x^3 - 3x + 2$? At what linear rate does Newton's method converge to it?

6. ◦ For $p(x) = x^3 - 2x^2 - 5x + 6$, compute the simple bound $1 + \max_k |a_k/a_0|$ from the [Cauchy root bound](/cauchy-root-bound/), and the sharper radius $R$, the positive root of $x^3 - 2x^2 - 5x - 6$, to three decimals. The roots of $p$ are $-2$, $1$ and $3$; how close do the two bounds come to the largest modulus?

7. ◦ [Fixed-point iteration](/fixed-point-iteration/) $x \leftarrow \cos x$ converges to $x^* \approx 0.739085$. What is its linear rate, and about how many decimal digits does it gain in each step?

8. ◦ The equation $x^2 - x - 2 = 0$ has the root $2$. Which of the iterations $x \leftarrow x^2 - 2$, $x \leftarrow \sqrt{x + 2}$ and $x \leftarrow 1 + 2/x$ converge to $2$ from nearby starts, and at what rates?

9. • Run three steps of the secant method on $x^2 - 2$ from $x_0 = 1$, $x_1 = 2$ in exact fractions. Compare the third iterate with the third Newton iterate from $x_0 = 1$.

10. • Newton's method on $f(x) = 1/x - a$ gives the division-free step $x \leftarrow x(2 - ax)$. Show that the residual $r = 1 - ax$ squares in each step. For $a = 7$ and $x_0 = 0.1$, how many steps make $|r| < 10^{-16}$?

11. • Apply Newton's method to $f(x) = (x - 1)^2$ from $x_0 = 2$ and find $x_k$ in closed form. Then apply the step $x - 2f(x)/f'(x)$ instead. What happens?

12. • The polynomial $x^2 - 3x + 2$ has the simple roots $1$ and $2$, and $(x - 1)^2$ has a double root at $1$. Subtract $10^{-10}$ from the constant term of each. How far does the root near $1$ move in each case? Relate the answers to [root conditioning](/root-conditioning/).

13. • [Newton's square root](/newton-square-root/) iteration $x \leftarrow (x + a/x)/2$ runs with $a = 10^6$ from $x_0 = 1$. Explain why the error roughly halves in the first steps. After how many steps is the relative error first below $1$, and after how many is it first below $10^{-15}$?

14. • In [Wilkinson's polynomial](/wilkinson-polynomial/), the root $j$ moves at the rate $|\partial x^*/\partial a_{19}| = j^{19}/((j - 1)!\,(20 - j)!)$ when the coefficient of $x^{19}$ changes. Evaluate this rate for $j = 20$. Is the largest root more or less sensitive than the root at $16$?

15. • Use the [Budan-Fourier theorem](/budan-fourier-theorem/) on $p(x) = x^3 - 3x + 1$ with $a = 0$ and $b = 2$. How many roots can lie in $(0, 2]$? Settle the count with one more evaluation of $p$.

16. • Solve $x^3 - 6x - 9 = 0$ with [Cardano's formula](/cardano-formula/). Give $u^3$, $v^3$, the real root, and the two complex roots.

17. • Apply [Newton's method for systems](/newton-method-for-systems/) to $x^2 + y^2 = 4$, $x = y$ from $(1, 1)$. Give the first two iterates in exact fractions and explain why they match a scalar iteration you have seen.

18. • Show that Newton's method on $f(x) = x^{1/3}$, the real cube root, diverges from every $x_0 \ne 0$. Which hypothesis of the local convergence theorem fails?

19. ★ Show that [Halley's method](/halley-method/) on $f(x) = x^m$ gives $x_{k+1} = \frac{m-1}{m+1}x_k$. Compare this rate with that of Newton's method on the same function for $m = 2$ and $m = 10$.

20. ★ Bisection on $x^2 - 2$ runs in binary64 on $[1, 2]$, halving until the computed midpoint equals one of the ends. How many halvings does it make, and what are the two final ends? Explain the count from the spacing of the floats in $[1, 2)$.

21. ★ Apply the [Kantorovich theorem](/kantorovich-theorem/) to $f(x) = x^2 - 2$ on the real line. Find $\eta$ and the relative Lipschitz constant $L$ in terms of $x_0 > 0$, and find the set of $x_0 > 0$ for which $h = L\eta \le 1/2$. For $x_0 = 1$, what interval does the theorem give for the root?

22. ★ Newton's method on $x^3 - 2x + 2$ from $x_0 = 0$ cycles between $0$ and $1$. Show that the cycle attracts nearby starts: compute the derivative of the two-step map $N(N(x))$ at $x = 0$, where $N(x) = x - f(x)/f'(x)$.

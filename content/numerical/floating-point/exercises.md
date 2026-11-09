1. ◦ Write $-6.5$ in [IEEE 754](/ieee-754/) binary32: give the sign bit, the biased exponent in binary, the 23 fraction bits, and the whole word in hexadecimal.

2. ◦ What is $\mathrm{ulp}(1000)$ in binary64, as a power of 2 and in decimal? What is the relative spacing $\mathrm{ulp}(1000)/1000$, and how does it compare with [machine epsilon](/machine-epsilon/)?

3. ◦ What is the smallest positive integer that binary32 cannot represent exactly? The smallest for binary64? To which float does each one round?

4. ◦ Binary16 has 16 bits, 5 of them for the exponent. How many of its $2^{16}$ bit patterns are NaNs, how many are infinities, and how many encode finite values, counting $+0$ and $-0$ separately? See [special values](/special-floating-point-values/).

5. ◦ Round $0.5$, $1.5$, $2.5$ and $3.5$ to integers with [round to nearest, ties to even](/round-to-nearest-even/). Why does this tie rule avoid a bias in long sums of rounded values?

6. ◦ In binary64, $0.1 + 0.2$ and $0.3$ give different floats. By how much do they differ, and how many ulps of $0.3$ is that?

7. ◦ Give the [condition number](/condition-number/) $|x f'(x) / f(x)|$ of $f(x) = \sqrt{x}$ at any $x > 0$, of $f(x) = x - 1$ at $x = 1.001$, and of $f(x) = e^x$ at $x = 700$.

8. ◦ The loop `eps = 1.0; while 1.0 + eps/2 > 1.0: eps = eps/2` runs in binary64 with round to nearest. How many times does the body run, and what value of `eps` does the loop return?

9. • For $x = 10^{16}$, evaluate $\sqrt{x + 1} - \sqrt{x}$ in binary64 as written. What do you get, and what is the true value to two digits? Rewrite the expression so that it has no [cancellation](/catastrophic-cancellation/), and show that the new form is accurate.

10. • Evaluate $(1 - \cos x)/x^2$ at $x = 10^{-8}$ in binary64. Explain why the result is $0$ when the true value is close to $1/2$, and give a form built from $\sin(x/2)$ that is accurate.

11. • Sum $1, 2^{-53}, 2^{-53}$ in binary64, left to right, first by plain recursive summation and then by [Kahan summation](/kahan-summation/). Show the running sum and the compensation after each step. Which result is exact?

12. • Let $a = b = 1 + 2^{-30}$. Find $p = \mathrm{fl}(ab)$ and the error $e = ab - p$ that [TwoProduct](/two-product/) returns. Check that $e$ is a float and that $p + e$ is exact.

13. • Compute $\log(e^{1000} + e^{1001})$ in binary64. What does the formula as written return, and what does the [log-sum-exp trick](/log-sum-exp-trick/) return to 10 significant digits?

14. • The number of significant decimal digits that identifies every float of precision $p$ is $1 + \lceil p \log_{10} 2 \rceil$. Evaluate it for binary16, [bfloat16](/bfloat16/) and binary128.

15. • How many binary64 numbers lie strictly between $0$ and $1$? Count the normal and the [subnormal](/subnormal-numbers/) ones, and check your answer against the bit pattern of $1.0$ read as an integer.

16. • For which smallest positive integer $n$ is $\mathrm{fl}(n \cdot \mathrm{fl}(1/n)) \ne 1$ in binary64? Run the search, and say what value the product takes.

17. • In decimal arithmetic with three significant digits and round half to even, let $a = 5.01$ and $b = 5.02$. Compute $\mathrm{fl}(\mathrm{fl}(a + b)/2)$ and $\mathrm{fl}(a + \mathrm{fl}(b - a)/2)$. Which of the two lies in $[a, b]$?

18. • Compare the bounds $\gamma_{n-1}$ for recursive summation and $\gamma_{\lceil \log_2 n \rceil}$ for [pairwise summation](/pairwise-summation/) when $n = 2^{20}$ in binary64. By what factor do they differ?

19. ★ Show that the recursive summation bound $\gamma_{n-1}\sum|x_i|$ is sharp to first order. Sum $x_1 = 1$ and then $n - 1$ copies of $u = 2^{-53}$ in binary64, from left to right. Find the computed sum and the relative error for $n - 1 = 1000$.

20. ★ Prove that in [Fast2Sum](/fast-two-sum/), with round to nearest and the exponent of $a$ at least that of $b$, the subtraction $z = s - a$ is exact. Use the [Sterbenz lemma](/sterbenz-lemma/), and treat the cases where $a$ and $b$ have the same sign and opposite signs separately.

21. ★ A common way to round to the nearest integer is $\lfloor x + 0.5 \rfloor$. Show that in binary64 it gives $1$ for $x = 0.49999999999999994$, the float just below $0.5$, and that it gives the wrong answer for $x = 2^{52} + 1$. What is the result in that second case?

22. ★ Compute $q = \mathrm{fl}(1/3)$ in binary64 as an integer times a power of 2, and then the exact product $3q$. Show that $\mathrm{fl}(3q) = 1$, and explain which rule makes it come out exactly 1.

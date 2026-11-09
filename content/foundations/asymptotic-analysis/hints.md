1. $\lg \lg n$, $(\lg n)^3$, $\sqrt n$, $2^{\lg n} = n$, then $n \lg n$ and $\lg(n!)$, which are $\Theta$ of each other, then $n^2/\lg n$, then $4^{\lg n} = n^2$.

2. (a) true, with $c = 2$; (b) false, since $2^{2n}/2^n = 2^n$ is unbounded; (c) false; (d) true, since $\lg(n^3) = 3 \lg n$; (e) true; (f) true, with $c = 1$.

3. $c = 20$ and $n_0 = 1$ work, since $3n^2 + 10n + 7 \le 20n^2$ for $n \ge 1$. With $c = 4$ you need $n^2 \ge 10n + 7$, which first holds at $n = 11$.

4. $\sum_{i=1}^{n} (n - i + 1) = n(n+1)/2$, which is $\Theta(n^2)$.

5. Nine times: $1000, 500, 250, 125, 62, 31, 15, 7, 3, 1$. In general $\lfloor \lg n \rfloor$ times.

6. $\lg^* 16 = 3$, $\lg^* 65536 = 4$ and $\lg^* 2^{65536} = 5$. Since $A_3(1) = 2047$, $\alpha(2047) = 3$ and $\alpha(2048) = 4$.

7. $H_4 = 25/12 \approx 2.083$, and $\ln 5 \approx 1.609 \le 2.083 \le 1 + \ln 4 \approx 2.386$.

8. $O(n^2)$ and $\Omega(n)$ are true on every input. The other three each fail on some input: $\Theta(n^2)$ and $\Omega(n^2)$ on a best-case input, $O(n)$ on a worst-case input.

10. The largest $\lceil n/2 \rceil$ factors of $n!$ are each at least $n/2$, so $n! \ge (n/2)^{n/2}$ and $\lg n! \ge \tfrac{n}{2}(\lg n - 1)$, which is at least $\tfrac14 n \lg n$ for $n \ge 4$.

11. (a) $f = 2n$ and $g = n$. (b) From $f \le c\,g$ we get $\lg f \le \lg c + \lg g \le (|\lg c| + 1) \lg g$, because $\lg g \ge 1$.

13. The inner loop runs $s = 1, 2, 4, \ldots, 2^k$ times, where $k = \lfloor \lg n \rfloor$, so the total is $2^{k+1} - 1$. Since $2^k \le n < 2^{k+1}$, this is at least $n$ and at most $2n - 1$.

14. Each run of the body is one triple $k < j < i$ of numbers from $0$ to $n - 1$, so the count is $\binom{n}{3} = n(n-1)(n-2)/6 \sim n^3/6$.

15. Write $\binom{2n}{n} = (2n)!/(n!)^2$ and apply Stirling to the three factorials; the powers of $e$ cancel. For $n = 10$ the formula gives about 187079, about 1.3 percent too high.

16. Each term lies between $n/k - 1$ and $n/k$, so the sum lies between $n H_n - n$ and $n H_n$.

17. Take $\log_b$ of both sides. $3^{\lg n} = n^{\lg 3} \approx n^{1.585}$, so it grows faster than $n^{1.5}$ by the factor $n^{\lg 3 - 1.5} \approx n^{0.085}$.

18. At the end $x = 2^{2^n}$, which has $2^n + 1$ bits. The unit-cost time is $\Theta(n)$. Under the logarithmic rule the $i$-th squaring costs $\Theta(2^i)$, so the total is $\Theta(2^n)$.

20. $A_4(1) = A_3(A_3(1)) = A_3(2047)$, and $A_3(j) > A_2(j)$, so $A_4(1) > A_2(2047) = 2^{2048} \cdot 2048 - 1$.

22. Take $g = \sqrt f$. Then $g/f = 1/\sqrt f \to 0$, and $g$ is nondecreasing and unbounded.

23. Let $f(n) = (2\lfloor n/2 \rfloor)!$ and $g(n) = (2\lfloor (n-1)/2 \rfloor + 1)!$. Both are nondecreasing. At even $n$, $f(n)/g(n) = n!/(n-1)! = n$; at odd $n$, $g(n)/f(n) = n$.

24. Read $s$ positions chosen independently and uniformly, and output the fraction of 1s among them. Its mean is $p$ and its variance is $p(1-p)/s \le 1/(4s)$. By [Chebyshev's inequality](/chebyshev-inequality/) the error exceeds $\varepsilon$ with probability at most $1/(4s\varepsilon^2)$, so $s = \lceil 3/(4\varepsilon^2) \rceil$ suffices.

25. For $k \le \sqrt n$ there are at most $\sqrt n$ values of $k$; for $k > \sqrt n$ the value $\lfloor n/k \rfloor$ is less than $\sqrt n$. To sum, start at $k = 1$: with $q = \lfloor n/k \rfloor$, the last $k'$ with the same quotient is $\lfloor n/q \rfloor$, so add $q(k' - k + 1)$ and jump to $k' + 1$.

26. Let $2^m$ be the largest power of 2 that is at most $n$. Only the term $1/2^m$ has $2^m$ in its denominator. Multiply $H_n$ by $2^{m-1}$ times the product of the odd numbers up to $n$: every term becomes an integer except $1/2^m$, which becomes an odd number over 2.

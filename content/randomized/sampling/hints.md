1. The first item is taken with probability $2/5$. The scan stops after two items only if both are taken, with probability $\frac{2}{5} \cdot \frac{1}{4} = \frac{1}{10}$. The expected number looked at is $E[L] = 2 \cdot 6/3 = 4$.

3. Algorithm R keeps item 3 with probability $1/3$, and item 2 with probability $\frac12 \cdot \frac23 = \frac13$, so each item has $1/3$. The rule with probability $1/2$ gives $1/4$, $1/4$ and $1/2$: the last item is kept too often.

5. The positions are $\lfloor 2/4 \rfloor, \lfloor 12/4 \rfloor, \lfloor 22/4 \rfloor, \lfloor 32/4 \rfloor = 0, 3, 5, 8$. Only five samples occur, $\{0,2,5,7\}$, $\{0,3,5,8\}$, $\{1,3,6,8\}$, $\{1,4,6,9\}$ and $\{2,4,7,9\}$, each for two values of $r$, so each has probability $1/5$. There are $\binom{10}{4} = 210$ subsets of size 4.

6. $W = 8$ and $q = (4, 4, 8, 16)$, so *small* $= [0, 1]$ and *large* $= [2, 3]$. Column 1 gets alias 3 and $q_3$ drops to 12; column 0 gets alias 3 and $q_3$ drops to 8. So $\mathit{prob} = (4, 4, 8, 8)$ and $\mathit{alias} = (3, 3, 2, 3)$. Item 3 gets $8 + 4 + 4 = 16$ of the 32 pairs, which is $4/8$.

8. The mean number of tries is $M = 2$, and $y$ is accepted with probability $f(y)/(M g(y)) = y$. For the half-normal, $f(x)/g(x) = \sqrt{2/\pi}\, e^{x - x^2/2}$ is largest at $x = 1$, so $M = \sqrt{2e/\pi} \approx 1.3155$.

11. $\Pr[L \le \ell] = \binom{\ell}{n}/\binom{N}{n}$. Sum $\Pr[L > \ell]$ over $\ell$, or use $\sum_{\ell} \ell \binom{\ell - 1}{n - 1} = n \binom{N+1}{n+1}$. For $N = 4$ and $n = 2$ the maxima of the six subsets are $2, 3, 3, 4, 4, 4$, with mean $10/3 = 2 \cdot 5/3$.

12. Item $t > k$ is in the reservoir after step $t$ with probability $k/t$, and it can enter only at step $t$; the first $k$ items must all be written. So the expected number of writes is at least $k + \sum_{t=k+1}^{n} k/t$. For $k = 10$ and $n = 10^4$ this is about $78.59$. Algorithm R writes exactly the first $k$ items and each later item it accepts, with probability $k/t$.

14. Successive sampling gives $\Pr[i \in S] = \frac{5}{12}, \frac{11}{15}, \frac{17}{20}$, and proportional inclusion gives $\frac13, \frac23, 1$. Item 3 is certain in the second design but missing with probability $3/20$ in the first.

16. Item 1 wins if $1/u_1 > 3/u_2$, that is $u_2 > 3u_1$, with probability $1/6$. Then $\tau = 3/u_2 \ge 3$ and $\hat w_1 = \tau$. Given $\tau = s$, item 1 wins with probability $1/s$, so $E[\hat w_1] = E[s \cdot (1/s)] = 1$.

19. $a = \sup \sqrt{h} = 1$, $b_- = 0$ and $b_+ = \sup_{x \ge 0} x e^{-x/2} = 2/e$, reached at $x = 2$. The region $C_h$ has area $\frac12 \int h = \frac12$, so the acceptance probability is $\frac{1/2}{2/e} = e/4 \approx 0.680$.

21. Compare the bits of a uniform $U$, drawn one at a time, with the binary digits of $p$, and stop at the first place where they differ; output 1 if $U$ has the 0 there. Each place differs with probability $1/2$, so the number of bits is geometric with mean 2.

22. Each run that uses at most $B$ bits has probability a multiple of $2^{-B}$, so each output has such a probability, and $1/\binom{n}{k}$ must be one. That forces $\binom{n}{k}$ to be a power of 2. By the Sylvester-Schur theorem, for $2 \le k \le n - 2$ the number $\binom{n}{k}$ has a prime factor larger than 2, so only $k \in \{0, n\}$, or $k \in \{1, n - 1\}$ with $n$ a power of 2, remain.

24. Induct on the rounds. For a target sequence $s$ of $i + 1$ distinct elements of $\{0, \ldots, j\}$, find the one old sequence and the one value of $t$ that produce it: if $j$ is first in $s$ or absent, then $t$ is the first element of $s$ and the old sequence is the rest; otherwise $t$ is the element just before $j$ and the old sequence is $s$ without $j$.

25. Draw $J$ with the hypergeometric law $\Pr[J = j] = \binom{n_1}{j}\binom{n_2}{k - j}/\binom{n_1 + n_2}{k}$, then a uniform $j$-subset of $S_1$ and a uniform $(k - j)$-subset of $S_2$. A uniform $j$-subset of a uniform $k$-subset is a uniform $j$-subset of the stream.

26. $X_i = -\ln K_i = E_i/w_i$ with $E_i$ standard exponential, so $X_i$ is exponential with rate $w_i$, and the largest keys are the smallest $X_i$. The minimum of independent exponentials is item $i$ with probability $w_i/W$, and by the memoryless property the others, less the minimum, are again independent exponentials with the same rates.

27. Each $\hat p_i$ has mean $p_i$ and relative variance $(1 - p_i)/(p_i t) \le 1/t$. For independent factors, the relative variance of the product is $\prod_i (1 + v_i) - 1 \le e^{m/t} - 1$. Make it at most $\varepsilon^2/16$ and apply Chebyshev's inequality. In all $mt = O(m^2/\varepsilon^2)$ samples.

28. Write $V(y)$ for the variance as a function of the population. The expectation of any estimator is the average of $k$ terms, each depending only on the $y$ values of one residue class. Such a sum has zero mixed partial derivative $\partial^2/\partial y_a \partial y_b$ for $a$ and $b$ in different classes, but $V(y)$, which contains $-\bar Y^2$, does not.

1. The mean increase is 4, so $T_0 = -4/\ln 0.8 \approx 17.93$. The increase of 6 is accepted with probability $e^{-6/17.93} \approx 0.716$. The temperature after $j$ reductions is $17.93 \cdot 0.9^j$, which is first below $0.1$ at $j = 50$.

3. With $L = 2$ the candidates of iterations 1, 2, 4 and 5 are accepted (counting from 0). Iterations 2 and 5 accept a worse solution, from 9 to 10 and from 8 to 9, because the candidate is no worse than the cost stored two iterations earlier. At the end the list is $(8, 9)$, the current cost is 9 and the best is 8. With $L = 1$ only the candidates of cost 9 and 8 are accepted, and the run ends at 8.

5. Roulette: $0.1, 0.2, 0.3, 0.4$, so $0.4, 0.8, 1.2, 1.6$ copies. After adding 10: $0.22, 0.24, 0.26, 0.28$, and the best expects only $1.12$ copies. The best is missed in all four spins with probability $0.6^4 = 0.1296$. Binary tournament gives the member of rank $r$ (1 the worst) probability $(2r - 1)/16$, that is $1/16, 3/16, 5/16, 7/16$, and adding 10 changes nothing, since only the order counts.

7. Order 3, defining length $6 - 1 = 5$. The factor is $(1 - 0.7 \cdot 5/7)(0.99)^3 = 0.5 \cdot 0.9703 \approx 0.485$, so the bound promises growth only when $f(H, t)/\bar f(t) > 2.06$.

9. $\lambda = 0.2 \cdot 32/5 = 1.28$. The utilities are $c_e/(1 + p_e)$, so the edges of length 9, 8, 6, 5 and again 9 are penalized (in the fifth iteration the utilities are $4.5, 4, 3, 2.5, 4$). The penalties then add up to 5, and $h = 32 + 1.28 \cdot 5 = 38.4$.

12. The local minima that are not global are state 0 (depth 2) and states 2 and 6 (depth 3 each), so $d^* = 3$ and $c = 3$. Then $T_k \le 0.5$ when $\ln(k + 1) \ge 6$, first at $k = 403$. For the geometric schedule the terms $e^{-3/(T_0 \alpha^k)}$ fall faster than any geometric series, so the sum is finite.

13. From $z$ zeros, a step succeeds with probability $z/n$, so the expected wait is $n/z$, and the waits add over $z, z - 1, \ldots, 1$. For $n = 10$ this gives $10 H_{10} \approx 29.3$, against $e \cdot 10 \cdot H_{10} \approx 79.6$ for the bound.

15. The averages are $7/4$, $2$, $5/2$, $3$, $1$ and $1$. In both competitions the schema of the optimum 111 loses, to $0{*}{*}$ and to $00{*}$, so the short schemata guide the search toward 000, which is a local maximum of value 4. The function is deceptive: combining the winning blocks gives 000, not the optimum.

16. (a), (c) and (e) are closed under permutation: composing with a bijection of $X$ keeps the number of minima, the set of values and the orbit. (b) is not, since $\sigma$ can move the minimum away from 1. (d) is not: for $N = 3$ the function with values $0, 1, 2$ is unimodal, but its rearrangement $0, 2, 1$ is not.

20. Hill climbing needs 50 seconds on average and simulated annealing 60, since the run that succeeds also counts in full. In 300 seconds the failure probabilities are $0.98^{300} \approx 0.0023$ and $0.5^{10} \approx 0.0010$. Per second, simulated annealing lowers the log of the failure probability by $\ln 2/30 \approx 0.0231$ and hill climbing by $-\ln 0.98 \approx 0.0202$, so for large budgets it wins, while its long runs cost it in the mean.

22. Check detailed balance: $|N(x)| e^{-f(x)/T} \cdot \frac{1}{|N(x)|} \min(1, e^{-(f(y) - f(x))/T}) = \min(e^{-f(x)/T}, e^{-f(y)/T})$, which is symmetric in $x$ and $y$. On the path the distribution is $(1/4, 1/2, 1/4)$ instead of uniform. Accept with probability $\min\left(1, e^{-\Delta/T} |N(x)|/|N(y)|\right)$.

23. Bound $Z$ from above: the members of $S^*$ give $|S^*| e^{-f^*/T}$, and every other state gives at most $e^{-(f^* + \delta)/T}$. For the numbers given, you need $2^{20} e^{-1/T} \le 1/99$, that is $T \le 1/(\ln 99 + 20 \ln 2) \approx 0.054$.

24. The probability of making one given point at distance $m$ is $p^m (1 - p)^{n - m}$, and with $p = 1/n$ it is at least $n^{-m}(1 - 1/n)^{n-1} \ge 1/(e n^m)$. Setting the derivative of $m \ln p + (n - m) \ln(1 - p)$ to zero gives $p = m/n$. The waiting times tend to $e n^m$ and $(e n/m)^m$, so the ratio tends to $m^m/e^{m - 1}$: about $1.47$ for $m = 2$ and $3.65$ for $m = 3$.

25. The runs are independent, and the number of runs is geometric with mean $1/q$. Each run costs $\min(T, t_0)$ for its own $T$, and Wald's identity gives the total. With no restarts the mean is $0.1 + 90 = 90.1$; with $t_0 = 1$ it is $1/0.1 = 10$.

26. Ternary search keeps an interval that contains the minimizer and compares two inner points; each comparison removes a third of the interval, and the golden-section spacing lets one of the two points be reused. The set of unimodal functions is not closed under permutation, so the theorem does not apply to it: for $N = 3$, of the six orderings of three values, $0, 2, 1$ and $1, 2, 0$ are not unimodal.

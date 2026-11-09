7. A pivot of rank $r$, from 0 to $n - 1$, leaves the $r$ keys below it, and $r = 0$ ends the search. So $C(n) = (n - 1) + \frac{1}{n}\sum_{r=0}^{n-1} C(r)$ with $C(0) = C(1) = 0$. Subtract the equation for $n - 1$ after multiplying each by its size: $nC(n) - (n - 1)C(n - 1) = 2(n - 1) + C(n - 1)$, so $C(n) = C(n - 1) + 2 - 2/n$. Then $C(n) = 2n - 2H_n$, which is $20 - 2H_{10} \approx 14.14$ for $n = 10$, the value in the table of the entry.

8. One round stops within the budget with probability $1 - 2^{-j}$. Its expected cost is $\sum_{i=1}^{j} 2^{-i} 2^i + 2^{-j} 2^j = j + 1$. The number of rounds is geometric, so the expected total is $(j + 1)/(1 - 2^{-j})$: 4 for $j = 1$, 4 for $j = 2$, about 4.57 for $j = 3$, and it grows after that. The best budgets are 2 and 4 steps, with expected total 4.

9. The cost is $1 + 2 + \cdots + T = T(T + 1)/2$ for $T$ rounds. For a geometric $T$ with $p = 1/2$, $\mathbb{E}[T] = 2$ and $\mathbb{E}[T^2] = \mathrm{Var}[T] + 4 = 2 + 4 = 6$. So the expected cost is $(6 + 2)/2 = 4$, not 3: the expectation of a function of $T$ is not the function of the expectation.

12. With $p = 1/190$, the bound $(1 - p)^t \le e^{-t/190} \le 1/100$ needs $t \ge 190 \ln 100 \approx 874.98$, so 875 runs suffice. The exact condition $(189/190)^t \le 1/100$ gives $t \ge 872.68$, so 873 runs are the least.

14. Sum $1/(|j - i| + 1)$ over $j \ne i$. The keys below $i$ give $1/2 + 1/3 + \cdots + 1/i = H_i - 1$, and the keys above give $H_{n - i + 1} - 1$. For $n = 7$ and $i = 4$, both are $H_4 - 1 = 13/12$, so the answer is $13/6$.

15. If two neighbours were both kept, each would come before the other. Vertex $v$ is first among itself and its $d(v)$ neighbours with probability $1/(d(v) + 1)$, and linearity of expectation adds these. The star gives $1/6 + 5/2 = 8/3$, so some order keeps at least 3 vertices; the five leaves are the largest independent set. The path gives $1/2 + 3 \cdot 1/3 + 1/2 = 2$; its largest independent set has 3 vertices.

16. In a random colouring, an edge has one colour with probability $2 \cdot 2^{-k} = 2^{1-k}$, so the union bound gives a bad colouring with probability at most $m 2^{1-k} < 1$. When $m \le 2^{k-2}$ this is at most $1/2$: colour at random, check every edge in $O(km)$ time, and repeat on failure. The expected number of rounds is at most 2. The Fano plane has $m = 7$ and $2^{k-1} = 4$, so the condition fails and nothing is claimed.

17. Probing in random order without repeats is reading a random permutation of the cells. Each of the $n - k$ unmarked cells comes before all $k$ marked cells with probability $1/(k + 1)$, so the expected number of unmarked cells probed is $(n - k)/(k + 1)$, and one more probe finds the mark: $(n + 1)/(k + 1)$ in total. For $n = 10$ and $k = 5$ this is $11/6$; with repeats it is $n/k = 2$.

18. A pivot of rank $r$ leaves $r$ keys, so $R(n) = 1 + \frac{1}{n}\sum_{r=0}^{n-1} R(r)$ with $R(0) = 0$. As in Exercise 7, $nR(n) - (n - 1)R(n - 1) = 1 + R(n - 1)$, so $R(n) = R(n - 1) + 1/n$ and $R(n) = H_n$. Then $R(7) = 363/140$, about 2.59.

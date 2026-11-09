1. Eleven of the 36 outcomes contain a 6, and two of them, $(1,6)$ and $(6,1)$, have sum 7, so the answer is $2/11$. Without the condition it is $6/36 = 1/6$, which is smaller.

3. The number of throws is geometric with $p = 1/6$, so its mean is 6. More than 10 throws are needed exactly when the first 10 all miss: $(5/6)^{10} \approx 0.162$.

4. Each of the $n - 1$ adjacent pairs is a descent with probability $1/2$, so the mean is $(n-1)/2$. Of the three keys at positions $i - 1, i, i + 1$, each is the largest with probability $1/3$, so the mean number of peaks is $(n-2)/3$.

5. $H_{10} = 7381/2520 \approx 2.929$. Exactly one hire happens when the best candidate comes first, with probability $1/10$. All 10 are hired only when the order is increasing, with probability $1/10! \approx 2.8 \times 10^{-7}$.

6. Markov gives $10/15 = 2/3$. Chebyshev gives $\Pr[|X - 10| \ge 5] \le 4/25 = 0.16$. The program runs for time at least $4T$ with probability at most $1/4$, by Markov.

7. About $\sqrt{2 \ln 2 \cdot 2^{32}} \approx 77{,}000$ keys for 32 bits, and about $5.1 \times 10^9$ for 64 bits.

8. $6H_6 = 6 \cdot 49/20 = 14.7$.

9. A bin is empty with probability $0.99^{100}$, so the mean is $100 \cdot 0.99^{100} \approx 36.6$. A bin has exactly one ball with probability $100 \cdot 0.01 \cdot 0.99^{99}$, so the mean is $100 \cdot 0.99^{99} \approx 37.0$.

10. With 100 doors, switching wins unless your first pick was right: $99/100$. In the second game the host's door shows a goat with probability $1/3 \cdot 1 + 2/3 \cdot 1/2 = 2/3$, and your door has the car in $1/3$ of all games, all of them with a goat shown. So staying wins with probability $(1/3)/(2/3) = 1/2$, and so does switching.

13. Let $Y_j$ be the number of keys before position $j$ that are larger than the key at position $j$. In a random permutation the $Y_j$ are independent and $Y_j$ is uniform on $\{0, \ldots, j-1\}$, with variance $(j^2 - 1)/12$. Sum over $j$.

17. Chebyshev: $250/100^2 = 0.025$. Chernoff with $\mu = 500$ and $\delta = 0.2$: $e^{-20/3} \approx 1.3 \times 10^{-3}$. Hoeffding with $t = 0.1$: $e^{-2 \cdot 1000 \cdot 0.01} = e^{-20} \approx 2.1 \times 10^{-9}$. All three are far above the true value; Hoeffding is the closest.

23. Use $\mathbb{E}[M] = \sum_{k \ge 0} \Pr[M > k]$ and $\Pr[M > k] = 1 - (1 - 2^{-k})^n$. For the upper bound, bound each term by $\min(1, n2^{-k})$ and split at $k = \lceil \lg n \rceil$. For the lower bound, use $1 - (1 - 2^{-k})^n \ge 1 - e^{-n2^{-k}}$ for $k = 0, \ldots, \lfloor \lg n \rfloor$, and note that $\sum_{j \ge 0} e^{-2^j} < 0.53$.

24. Take $f(s) = (q/p)^s$: then $\mathbb{E}[f(S_{t+1}) \mid S_t] = (q/p)^{S_t}(p \cdot q/p + q \cdot p/q) = f(S_t)$. The stopped process is bounded, so optional stopping gives $\Pr[\text{reach } b] = (1 - (q/p)^a)/(1 - (q/p)^b)$, about $0.716$ for the given values.

25. Let $A_C$ be the event that a uniformly random assignment falsifies clause $C$; $\Pr[A_C] = 2^{-k}$. $A_C$ is mutually independent of the events of all clauses that share no variable with $C$, and at most $d = k(m-1)$ clauses share one. The symmetric lemma needs $e \, 2^{-k}(d+1) \le 1$, and $d + 1 \le km \le 2^k/e$.

27. The number of hires counts the left-to-right maxima of the order. Write each cycle of a permutation with its largest element first, list the cycles in increasing order of their first elements and erase the parentheses. This is a bijection from permutations to sequences, and the first elements of the cycles are exactly the left-to-right maxima of the sequence.

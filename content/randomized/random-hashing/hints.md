1. The digits are $50 = (1, 0, 1)$ and $100 = (2, 0, 2)$, so $h_a(50) = 3 + 1 = 4$ and $h_a(100) = 6 + 2 = 8 \bmod 7 = 1$. The digit vector of 100 is twice that of 50, and the family is linear. The keys collide exactly when $h_a(50) = 0$, that is $a_0 + a_2 \equiv 0$: 49 vectors, probability $1/7$.

3. $179 \cdot 2 \bmod 256 = 102 = 01100110_2$, so $h(2) = 3$. $179 \cdot 3 \bmod 256 = 25 = 00011001_2$, so $h(3) = 0$. For odd $a$, $128a \bmod 256 = 128 = 10000000_2$, so $h(128) = 100_2 = 4$.

4. At most $\alpha = 2$ for an absent key, at most $1 + 999/500 = 2.998$ for a stored key, and at most $\binom{1000}{2}/500 = 999$ colliding pairs. With multiply-shift the collision probability is at most $2/m$, so the stored-key bound is $1 + 2 \cdot 999/500 = 4.996$.

5. $a_0 = 1$, then $a_1 + a_2 = 2$ and $2a_1 + 4a_2 = 1$ in $\mathbb{Z}_7$, so $a_2 = 2$ and $a_1 = 0$: $h(x) = 1 + 2x^2$ and $h(3) = 19 \bmod 7 = 5$. Exactly one polynomial, by the Vandermonde argument.

7. For $n = 1100$ the load is $0.55 > 1/2$, so the keys cannot be stored with probability $1 - o(1)$. For $n = 800$, $q = 0.8$ and the bound is $\frac{4}{1000} \cdot \frac{0.8 \cdot 1.8}{0.2^3} = 0.72$, about 150 times the measured rate $0.00485$.

9. $E[X] = 100$ and $\operatorname{Var}[X] = 10\,000 \cdot 0.01 \cdot 0.99 = 99$. Chebyshev gives $\Pr[|X - 100| \ge 100] \le 99/10^4 = 0.0099$. The union bound gives only $0.99$ for some slot; pairwise independence is too weak for a useful bound on the fullest slot.

11. For $k = 2$ the condition is $t(t-1) \ge 2 \cdot 10^6$, so $t = 1415$. For $k = 4$ it is $t(t-1)(t-2)(t-3) \ge 2 \cdot 10^6$, so $t = 40$, since $39 \cdot 38 \cdot 37 \cdot 36 = 1\,974\,024$.

13. Let $n_\sigma$ be the multiplicity of the permutation $\sigma$. Each key comes first in exactly 2 of the 6 members. For a pair $\{y, z\}$ with third key $x$, $y$ comes before $z$ when $y$ is first or when the order is $x, y, z$; this must happen 3 times, so the order $x, y, z$ occurs exactly once. This holds for every order.

16. Put $m = n$ in part 3 of the chain length theorem: $n + n(n-1)/n = 2n - 1$. Then Markov's inequality gives $\Pr[\sum_j L_j^2 \ge 4n] \le (2n-1)/(4n) < 1/2$.

17. A placement is a matching of the keys into the cells in the bipartite graph of keys and cells. A set $K$ of keys uses the cells at the ends of its edges, and these edges form a subgraph whose components have at most one cycle, because each component of the cuckoo graph has at most one. So $|K| \le |N(K)|$. Conversely, the keys of a component with $e > v$ have only $v$ cells.

18. The keys of a component can use only its $v_C$ cells, so at least $e_C - v_C$ of them go to the stash. For the converse, in each component with $e_C > v_C$ keep the edges of a spanning tree and one more edge, and stash the other $e_C - v_C$ keys; what is left has one cycle per component, and part 1 places it.

19. Put $Y_i = 2X_i - 1$ and use the inner product $\langle f, g \rangle = \sum_\omega \Pr[\omega] f(\omega) g(\omega)$ on functions $\Omega \to \mathbb{R}$. The constant 1 and $Y_1, \ldots, Y_n$ are orthonormal, so they are $n + 1$ linearly independent vectors in a space of dimension $|\Omega|$. The parity construction has $2^k$ points and $2^k - 1$ bits.

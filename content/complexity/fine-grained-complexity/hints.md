1. There are three: $-12 + 3 + 9$, $-5 + (-2) + 7$ and $-5 + 1 + 4$.

3. The first half gives $00 \mapsto 100$, $01 \mapsto 110$, $10 \mapsto 001$, $11 \mapsto 011$, and the second half gives $00 \mapsto 110$, $01 \mapsto 101$, $10 \mapsto 010$, $11 \mapsto 001$, where $01$ means $x_1 = 0, x_2 = 1$ or $x_3 = 0, x_4 = 1$. There are 5 orthogonal pairs and 5 satisfying assignments, one for each pair.

5. The triangles $123$, $124$, $134$ and $234$ weigh $-2$, $2$, $3$ and $1$. Only $123$ is negative.

6. (a) True. (b) False; it is not known. (c) False: it would refute SETH and the orthogonal vectors hypothesis, which says nothing about $\mathsf{P}$ versus $\mathsf{NP}$. (d) False: 3-SAT has much faster algorithms, and SETH is about $k$-SAT as $k$ grows.

7. $s \approx 0.415$, $0.585$ and $0.848$. SETH says that the best exponent $s_k$ tends to 1, so no fixed saving works for every $k$.

11. $N = n (c \log_2 n)^2$, so $N^{1.9} = O(n^{1.9} \log^{3.8} n)$. This is $O(n^{2-\varepsilon})$ for any $\varepsilon < 0.1$ and every $c$, which contradicts the hypothesis.

12. Set $w_{ii} = +\infty$ and compute $C = W \star W$ with $C_{ij} = \min_k (w_{ik} + w_{kj})$. A negative triangle exists exactly when $C_{ij} + w_{ji} < 0$ for some $i$ and $j$.

13. The time is $O(n^{c} \log n)$, truly subquadratic for $c < 2$. The hypothesis claims hardness only for dimension $c \log n$ with $c$ large enough for the given $\varepsilon$, so small $c$ is no contradiction.

18. Each call costs $(n^{0.7} \log n)^{1.8} = n^{1.26} \log^{1.8} n$ up to constants, and $n^{0.5}$ calls give $O(n^{1.76} \log^{1.8} n)$, which is truly subquadratic.

19. With $M = 4n$, put $M a_i + i$ in the first two lists and $-(M a_k + k)$ in the third. A zero sum means $M(a_i + a_j - a_k) + (i + j - k) = 0$, and since $\lvert i + j - k \rvert < M$, both parts are zero, so $k = i + j$.

20. Shift each number by $U$ and form $P(x) = \sum_{a \in S} x^{a + U}$. Square it by the fast Fourier transform in $O(U \log U)$ time; the coefficient of $x^{2U - c}$ counts ordered pairs with $a + b = -c$. Subtract the pairs with $a = b$ or with $c$ itself among them, and check whether any $c$ has a pair left.

21. Split the $N$ variables into $k$ groups of $N/k$, and give each assignment of a group a vector with one coordinate per clause, 1 when the group leaves the clause unsatisfied. The $k$ vectors have zero product exactly when the assignments together satisfy every clause. With $n = 2^{N/k}$, time $n^{k-\varepsilon}$ is $2^{(1-\varepsilon/k) N}$, and sparsification keeps the dimension $O(N)$.

22. Edges with an end of degree at most $\sqrt{m}$ are checked through that end's neighbors in $O(m \sqrt{m})$ time. There are at most $2\sqrt{m}$ vertices of larger degree, so all triples of them take $O(m^{3/2})$. With threshold $\Delta$ and matrix multiplication on the at most $2m/\Delta$ high vertices, the time is $O(m \Delta + (m/\Delta)^{\omega})$, balanced at $\Delta = m^{(\omega-1)/(\omega+1)}$. For $\omega = 2$ this is $m^{4/3}$.

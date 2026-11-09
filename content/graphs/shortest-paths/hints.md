1. Finish order $s, b, a, c, d, t$. Distances $a = 3$, $b = 1$, $c = 4$, $d = 7$, $t = 8$. Parents: $a \leftarrow b$, $b \leftarrow s$, $c \leftarrow a$, $d \leftarrow c$, $t \leftarrow d$.

2. After the passes: $[0, 4, 6, 9, 9]$, $[0, 4, 6, 5, 9]$, $[0, 4, 5, 5, 7]$, $[0, 4, 5, 4, 7]$. The check pass still lowers $d(4)$ through $3 \to 4$, so a negative cycle is reachable: $2 \to 3 \to 4 \to 2$ has weight $-1 + 2 - 2 = -1$.

3. Extraction order $s, a, c, b$. When $b$ is extracted, $d(a)$ falls from 2 to 1, but $c$ is already finished with $d(c) = 3$, while the true distance is 2. The value at $a$ is right because $b \to a$ is relaxed; nothing relaxes $a \to c$ again.

4. Rows: $[0, 3, 1, 2]$, $[1, 0, -2, -1]$, $[3, 6, 0, 1]$, $[2, 5, 3, 0]$.

5. One order is $a, b, d, c, e, f$. Distances $a = 0$, $b = 2$, $d = -2$, $c = -1$, $e = -3$, $f = -2$. Tree: $b \leftarrow a$, $d \leftarrow b$, $c \leftarrow d$, $e \leftarrow c$, $f \leftarrow e$.

6. Each constraint $x_j - x_i \le c$ is an edge $x_i \to x_j$ of weight $c$. The distances give $(x_1, x_2, x_3, x_4) = (0, -2, 0, -1)$; check all five constraints.

7. Weight each edge $-\log(\text{rate})$. The cycle USD, EUR, GBP, USD has product $0.9 \cdot 0.9 \cdot 1.25 = 1.0125$, so one dollar becomes 1.0125 dollars and the cycle weight is $-\log 1.0125 < 0$.

8. $h = (0, -2, 0, -1)$. New weights: $(0, 1)$ 0, $(1, 2)$ 1, $(0, 2)$ 4, $(2, 3)$ 0, $(3, 1)$ 3, $(1, 3)$ 4. Distances from 0: $0, -2, 1, 0$.

10. Keep a count $c(v)$; when an edge gives a strictly smaller estimate, copy $c(u)$, and when it ties, add $c(u)$. With positive weights every predecessor on a shortest path is finished before $v$. A zero edge can tie two vertices at the same distance and finish one before the other has its final count.

11. With in-place updates one pass can carry a value along the whole chain, since $a$, then $b$, then $c$ are relaxed in order, giving $c$ a finite value after one pass. Relax from a copy of the previous array.

15. Take the path $0 \to 2 \to 3 \to 1$. The pair $(0, 1)$ is handled before $(0, 3)$ and $(2, 1)$ have finite values, and it is never visited again.

17. Maximize a product of probabilities by minimizing the sum of $-\log p$, which is nonnegative, so Dijkstra applies. The best path is $s \to a \to t$ with probability 0.72.

21. A shortest path with at most $n - 1$ edges splits into maximal runs of increasing and decreasing vertex numbers, and one pass relaxes one increasing run and the decreasing run after it.

23. Replace the entry $a$ by $x^{M - a}$ with $x = n + 1$, and $\infty$ by 0. The highest power in a sum of $n$ such terms identifies the minimum, because fewer than $x$ terms share a power. The numbers have $O(M \log n)$ bits.

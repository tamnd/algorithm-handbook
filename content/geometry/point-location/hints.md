1. $V = 5$ (the four corners and the center), $E = 8$ (four sides and four half-diagonals), $C = 1$, and $F = 5$: four triangles and the outer face. Then $5 - 8 + 5 = 2 = 1 + C$.

2. Two slabs, $0 < x < 1$ and $1 < x < 2$. The left one holds, from the bottom, the bottom side, the half-diagonals from $(0,0)$ and from $(0,2)$ to the center, and the top side; the right one holds the bottom side, the half-diagonals from the center to $(2,0)$ and to $(2,2)$, and the top side. At $x = 1/2$ the two half-diagonals are at heights $1/2$ and $3/2$, so $(1/2, 1)$ is in the left triangle $(0,0), (1,1), (0,2)$.

4. There are $5 + 8 + 5 = 18$ possible answers, and $3^2 < 18 \le 3^3$, so three tests are needed in the worst case.

5. Seven, by $1 + n + m = 1 + 3 + 3$: the region left of $x = 0$; above the triangle for $0 < x < 2$; inside it for $0 < x < 2$; inside it for $2 < x < 6$; above it for $2 < x < 6$; below it for $0 < x < 6$, since the wall down from $(2,5)$ stops at the bottom edge; and the region right of $x = 6$.

9. In the order $s_1, \ldots, s_n$ the trapezoid that contains the query is split by every new segment, which adds one Y-node to its path: $3 + (n - 1) = n + 2$ nodes. In the order $s_n, \ldots, s_1$ every later segment lies below $s_n$ and never touches the trapezoid above it, so the path keeps its $3$ nodes.

11. The bound allows $121$ levels and $8 \cdot 121 = 968$ triangle tests, against $\lceil \log_2 1000 \rceil = 10$. The constant in Kirkpatrick's analysis is large, and it is the reason the method is studied more than it is implemented.

13. Sweep a vertical line from left to right over the end points and the query points together, with the edges that cross the line in a balanced search tree ordered from bottom to top. At a query point, search the tree for the edge directly above it.

14. With $j$ inner vertices of degree at least $11$, the inner degree sum gives $11 j + 3(N - 3 - j) \le 6N - 18$, so $j \le 3(N - 3)/8$ and at least $5(N - 3)/8$ inner vertices have degree at most $10$. Each chosen vertex blocks itself and at most $10$ neighbors, so each round removes at least $5(N - 3)/88$ vertices, and the factor is $83/88$, slightly better than $17/18$.

15. The probability is at most $1/2$ when $(n + 1)^{\lambda \ln 1.25 - 3} \ge 4$. For $n \ge 3$ it is enough that $\lambda \ln 1.25 - 3 \ge 1$, that is $\lambda \ge 4 / \ln 1.25 \approx 17.9$, so $\lambda = 18$ works. Each build succeeds with probability at least $1/2$, so the number of builds is geometric with expectation at most $2$.

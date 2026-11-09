1. The local coefficients are $C(1) = 1$, $C(2) = C(3) = 2/3$ and $C(4) = 1/3$; vertex 5 has degree 1, so $C(5)$ is undefined. Leaving vertex 5 out gives the average $2/3$, and counting it as 0 gives $8/15$. The graph has 2 triangles and $\sum_v \binom{d(v)}{2} = 1 + 3 + 3 + 3 + 0 = 10$ connected triples, so the global coefficient is $3 \cdot 2/10 = 3/5$. The three numbers are all different.

2. Degree: $1, 2, 2, 2, 1$. Closeness $(n-1)/\sum_u d(v,u)$: $2/5, 4/7, 2/3, 4/7, 2/5$. Harmonic: $25/12, 17/6, 3, 17/6, 25/12$. Betweenness: $0, 3, 4, 3, 0$. All four put vertex 2 first and the two ends last, but degree cannot tell vertex 2 from vertices 1 and 3.

3. The arcs $(1,2), (2,1), (3,4), (4,3)$ are reciprocated, so $r = 4/7$. The density is $\bar a = 7/12$, and $\rho = (4/7 - 7/12)/(5/12) = -1/35$. The graph has slightly fewer mutual arcs than a random graph of the same density.

4. Common neighbours rank $\{u, v\}$ first, 2 against 1. Adamic-Adar gives $2/\ln 5 \approx 1.243$ against $1/\ln 2 \approx 1.443$, and resource allocation gives $2/5$ against $1/2$, so both rank $\{x, y\}$ first. A shared neighbour of low degree is stronger evidence than two shared neighbours of high degree.

5. Vertex 8 has core number 1, vertices 5, 6 and 7 have core number 2, and vertices 1 to 4 have core number 3. The 1-core is the whole graph, the 2-core is $H - 8$, and the 3-core is the $K_4$ on $\{1, 2, 3, 4\}$: once vertex 8 is gone, vertex 7 has degree 2, and peeling it leaves 5 and 6 with degree 2 as well.

6. The expected number of edges is $\binom{1000}{2} \cdot 0.01 = 4995$, the expected degree is $999 \cdot 0.01 = 9.99$, and the expected number of triangles is $\binom{1000}{3} \cdot 10^{-6} \approx 166.2$. Two neighbours of a vertex are adjacent with probability $p$, so the expected clustering is about $0.01$. The threshold is $\ln 1000/1000 \approx 0.0069$, so $p$ is above it and the graph is connected with high probability.

7. Here $m = 7$. Each triangle has 3 inside edges and degree sum 7, so $Q = 2\,(3/7 - (7/14)^2) = 5/14 \approx 0.357$. The single community has $e_C = m$ and $D_C = 2m$, so $Q = 1 - 1 = 0$.

8. The groups are $\{1, 2\}$ and $\{3, 4, 5\}$: the positive edges lie inside groups and the negative edges between them. With the negative edge $35$, the triangle $3, 4, 5$ has the signs $+, +, -$, an odd number of negative edges, so no split into two groups works.

9. The star has $k$ vertices of degree 1 and one of degree $k$, so $p_1 = k/(k+1)$ and $p_k = 1/(k+1)$. Every edge joins degree 1 to degree $k$. In the formula for $r$, the numerator is $k - (1+k)^2/4 = -(k-1)^2/4$ and the denominator is $(1+k^2)/2 - (1+k)^2/4 = (k-1)^2/4$.

10. Vertex 4 has no in-arcs, so $\pi_4 = (1 - \alpha)/n = 0.0375$. Solving $\pi = \frac{1 - \alpha}{n}\mathbf{1} + \alpha M \pi$ for the rest gives $\pi \approx (0.373, 0.196, 0.394, 0.0375)$.

11. The authority vector is the leading eigenvector of $A^{\mathsf T} A$, whose eigenvalue is $3 + \sqrt{3}$. The authorities of 3 and 4 are 1 and that of 5 is $\sqrt{3} - 1$.

13. $\sigma = 1, 1, 1, 2, 2$ for $s, a, b, c, d$. Working back from $d$: $\delta_s(d) = 0$, $\delta_s(c) = 1$, $\delta_s(a) = \delta_s(b) = 1$. The betweenness values are $1/2, 1, 1, 7/2, 0$ for $s, a, b, c, d$, which add up to 6, the same as the sum of $d(s,t) - 1$ over the ten pairs.

16. For a community of $s$ vertices of $K_n$, the inside edges are $\binom{s}{2}$ and the degree sum is $s(n-1)$. Its term in $Q$ simplifies to $s(s - n)/(n^2(n-1))$.

21. Use the live-edge view: average over the 16 sets of live arcs. For $\{a\}$, the vertex $d$ is reached with probability $1 - (3/4)^2 = 7/16$.

24. For a fixed live-edge graph, the spread of $S$ is the number of vertices reachable from $S$, which is a coverage function.

25. The expected number of cycles of length $k$ is at most $(c^k)/(2k)$, and each has $k$ vertices.

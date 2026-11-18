1. With $N = 600$ reads, FPKM is $c \cdot 10^9/(\ell N)$: 500000, 166667 and 41667, which sum to 708333. The reads per base are 0.3, 0.1 and 0.025, so TPM is 705882, 235294 and 58824. Dividing each FPKM by 708333 and multiplying by $10^6$ gives the same numbers.

3. The gene $(0, 7)$ is dropped because one of its counts is 0. The geometric means of the others are $\sqrt{200}$, $\sqrt{800}$, $\sqrt{1800}$ and $\sqrt{16000}$. The ratios of the first sample are $2^{-1/2}$ three times and $0.316$; of the second, $2^{1/2}$ three times and $3.162$. The medians of four values, the geometric means of the two middle ones, are $2^{-1/2}$ and $2^{1/2}$. The fourth gene sits at one end of each sorted list, so it does not reach the middle.

5. $P(X \ge 3) = \big(\binom{5}{3}\binom{15}{1} + \binom{5}{4}\binom{15}{0}\big)/\binom{20}{4} = 155/4845 = 31/969 \approx 0.032$. The expected overlap is $4 \cdot 5/20 = 1$.

6. Unique gives 7 and cluster gives 2: $\{$AAAA, AAAC, AAAT, AATT$\}$ and $\{$CCCC, CCCG, GCCG$\}$. The arcs are AAAA $\to$ AAAT, AAAT $\to$ AATT, CCCC $\to$ CCCG and CCCG $\to$ GCCG; there is no arc from AAAA to AAAC, since $40 < 2 \cdot 25 - 1$. So directional gives 3 groups: $\{$AAAA, AAAT, AATT$\}$, $\{$AAAC$\}$ and $\{$CCCC, CCCG, GCCG$\}$.

7. With equal lengths, $\alpha_A' = (30 + 60\,\alpha_A/(\alpha_A + \alpha_B))/100$. One round gives $\alpha = (3/5, 2/5)$. The fixed point solves $\alpha_A = (30 + 60\alpha_A)/100$, so $\alpha = (3/4, 1/4)$.

9. The missing k-mer is skipped, so the set is $\{T_1, T_2\}$. No: an error can create a k-mer that belongs to another transcript and whose color leaves out the source.

11. Three paths suffice: $1, 2, 4, 5$, then $1, 3, 4, 5$, then $1, 3, 5$. The fragments $(2,4)$, $(3,4)$ and $(3,5)$ need three paths, because no path visits both 2 and 3, and no path holds both $(3,4)$ and $(3,5)$.

19. Each class holds both transcripts or neither, and the lengths are equal, so each term of the likelihood holds $\alpha_A + \alpha_B$ only. The maximizers form a segment of the simplex. From a uniform start, each round gives A and B equal shares, so the EM returns the midpoint of the segment, which is not more likely than any other point of it.

21. Each inner sum is linear in $\alpha$, and the logarithm is concave and increasing, so each term is concave. At a fixed point with all $\alpha_t > 0$, the update says that the gradient of $\log L$ is constant on the support, which is the Lagrange condition on the simplex. For a concave function this condition is sufficient.

22. Let $p(v)$ be the number of paths from node 1 to node $v$. Then $p(1) = p(2) = 1$ and $p(v) = p(v - 1) + p(v - 2)$. The number grows as about $1.618^n$, so no method can list every candidate, while the count itself takes linear time.

23. The four paths are $s,b,t$ with 7, $s,b,c,d,t$ with 5, $s,a,b,c,t$ with 9 and $s,a,c,t$ with 7. Greedy first takes $s,b,c,t$ with 12, then $s,a,b,t$ with 7, then $s,a,c,d,t$ with 5. What remains is $sa = 4$, $ab = 2$, $ac = 2$, $bc = 2$ and $ct = 4$, which needs two more paths of value 2 in any order.

24. Up to rank $i$ the walk has taken $h_i$ steps of $1/N_H$ and $i - h_i$ steps of $1/(n - N_H)$. These are the two empirical distribution functions at $i$. Both are step functions that change only at the ranks, so the largest gap is reached at some rank.

25. Expand $1 - e^{-\lambda} - \lambda e^{-\lambda} = \lambda^2/2 - \lambda^3/3 + O(\lambda^4)$ and $1 - e^{-\lambda} = \lambda(1 - \lambda/2 + O(\lambda^2))$. Dividing gives $(\lambda/2)(1 - 2\lambda/3)(1 + \lambda/2) + O(\lambda^3) = \lambda/2 - \lambda^2/12 + O(\lambda^3)$.

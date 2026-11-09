1. $\lfloor 1000/5 \rfloor + \lfloor 1000/25 \rfloor + \lfloor 1000/125 \rfloor + \lfloor 1000/625 \rfloor = 200 + 40 + 8 + 1 = 249$ zeros. The exponent of 2 in $20!$ is $10 + 5 + 2 + 1 = 18$.

2. For $2\,5\,4\,3\,1$ the scan stops at $i = 1$, the item 2 is exchanged with 3, and the result is $3\,1\,2\,4\,5$. For $3\,1\,4\,4\,2\,1$ it stops at $i = 2$, the item 1 is exchanged with the 2, and the result is $3\,2\,1\,1\,4\,4$.

3. The Lehmer code of $3\,5\,1\,4\,2$ is $(2, 3, 0, 1, 0)$, so the rank is $2 \cdot 24 + 3 \cdot 6 + 0 \cdot 2 + 1 \cdot 1 = 67$. Since $100 = 4 \cdot 24 + 0 \cdot 6 + 2 \cdot 2 + 0 \cdot 1$, the code $(4, 0, 2, 0, 0)$ gives $5\,1\,4\,2\,3$.

5. $(1\ 4\ 3)(2\ 6)(5\ 8)(7)$. The type is $(3, 2, 2, 1)$, the sign is $(-1)^{8 - 4} = +1$, and the order is $\operatorname{lcm}(3, 2, 2, 1) = 6$.

6. Values 3, 3, 2, 3 and 3. The list ends at $2\,1\,3\,4$.

8. The step makes $1 + \lfloor L/2 \rfloor$ exchanges, so it changes the sign exactly when $\lfloor L/2 \rfloor$ is even, that is, when $L \equiv 0$ or $1 \pmod 4$. For $n = 4$ the suffix length is 1, 2 or 3, so only the 12 steps with $L = 1$ change the sign. The signs are $+, -, -, +$ repeated six times.

9. The steps that move a value smaller than $n$ are exactly the steps of the list for $n - 1$, and between two of them value $n$ crosses the other $n - 1$ values. So value $n$ moves $(n-1) \cdot (n-1)!$ times, and induction gives the rest. The sum telescopes: $(m-1)\,(m-1)! = m! - (m-1)!$.

10. The graph is a cycle of length 6, so there are $6 \cdot 2 = 12$ lists. For the multiset, each exchange of two different neighbors changes the number of inversions by one. Four arrangements have an even count ($1122$, $1221$, $2112$, $2211$) and two have an odd count ($1212$, $2121$), but a list that alternates can have at most one more of one kind than of the other.

16. Induction: $N(n) \le 1 + (3t_{n-1} - 1) + (n-1)(3t_{n-2} - 1) = 3t_n - (n-1)$, which is at most $3t_n - 1$ for $n \ge 2$, using $N(0) = 1 \le 3t_0 - 1$ as the base below $n = 2$. The recurrence gives $N(8) = 1716$, against $3t_8 - 1 = 2291$.

17. The list for $n$ is the list for $n - 1$ with value $n$ sweeping across each permutation, right to left over the permutations of even rank and left to right over those of odd rank. So the rank is $n \cdot r' + (n - 1 - p)$ when $r'$ is even and $n \cdot r' + p$ when $r'$ is odd, where $r'$ is the rank of $\pi'$. The rank of $3\,5\,1\,4\,2$ is $5 \cdot 9 + 1 = 46$, since $3\,1\,4\,2$ has rank 9. For rank 100, $r' = 20$ and the remainder is 0; the permutation of rank 20 for $n = 4$ is $4\,2\,1\,3$, and 5 goes at the right end: $4\,2\,1\,3\,5$.

18. Pair the positions as $(1, 2), (3, 4), \ldots$ and exchange the entries of the first pair whose two entries differ. This pairs the arrangements, and it changes the inversion count by exactly one. What is left over are the arrangements made of blocks $11$ and $22$, with one single item at the end when $a + b$ is odd; they all have an even number of inversions, and there are none of them when $a$ and $b$ are both odd. Each step of the list changes the parity, so the two classes can differ in size by at most one, while here $D(a, b) \ge 2$.

19. The length is $n! - 1$, and the last permutation is $n \cdots 2\,1$. By induction, $z_{n-1}$ visits every arrangement of the first $n - 1$ positions and ends with them reversed. The reversal of length $n$ that follows then brings a new item to position $n$: starting from $x_1 \cdots x_n$, the items at the end are $x_n, x_{n-1}, \ldots, x_1$ in turn.

1. The cube is `1-0-` and covers 8, 9, 12 and 13. A cube contains minterm 5, that is `0101`, when each position holds either the bit of 5 or a dash, so 16 cubes contain it, the cube `----` among them.

3. No. $f$ is positive unate in $x_2$ and in $x_3$. It is binate in $x_1$: from $(0, 0, 1)$ to $(1, 0, 1)$ it falls from 1 to 0, and from $(0, 1, 0)$ to $(1, 1, 0)$ it rises from 0 to 1.

6. The columns for $x_1 x_2 = 00, 01, 10, 11$ are the constant 0, $x_3$, $x_3$ and the constant 1, so $\mu = 3$. Since $2 < 3 \le 4$, the decomposition needs $t = 2$ functions, and there is no simple decomposition with one $h$. By symmetry the same holds for every bound set of two variables.

8. For $k = 4$: $\{o\}$, $\{e, f\}$, $\{a, b, f\}$, $\{c, d, e\}$ and $\{a, b, c, d\}$, five cuts. For $k = 3$ the last one is too large, which leaves four.

9. ASAP: $v_1, v_2, v_4, v_6$ at step 1, $v_3$ at 2, $v_5$ at 3. ALAP at $L = 4$: $v_1, v_2$ at 2, $v_3, v_4$ at 3, $v_5, v_6$ at 4. The mobilities are 1 for $v_1, v_2, v_3, v_5$, 2 for $v_4$ and 3 for $v_6$.

11. Eight primes: `010-`, `01-1`, `0-00`, `100-`, `10-1`, `1-11`, `-000` and `-111`. Each minterm lies in exactly two primes, so none is essential, and the primes form a cycle of length 8 around the minterms. A cover needs at least 4 primes, and Petrick's product has exactly two terms with 4 primes: `010-`, `10-1`, `-000`, `-111` and `01-1`, `0-00`, `100-`, `1-11`, each with 12 literals.

13. Without don't-cares the primes are $\bar{x}_1 x_3$ and $x_1 \bar{x}_3 x_4$, both essential, 5 literals. With them, $x_1 \bar{x}_3 x_4$ grows to $\bar{x}_3 x_4$, which covers 1, 5, 9 and 13, and the cover $\bar{x}_1 x_3 + \bar{x}_3 x_4$ has 4 literals.

14. The rows $(y, a)$, $(y, b)$ and $(z, c)$ all hold the kernel $d + e$. That rectangle covers six cubes with 12 literals and adds $ax$, $bx$, $cx$ and the node $x = d + e$, so its value is $12 - 6 - 2 = 4$. The rows $(y, d)$ and $(y, e)$ with the columns $a$ and $b$ have value 2. The network goes from 13 to 9 literals.

17. The least level is $\lceil \log_2(1 + 1 + 1 + 1 + 4 + 8) \rceil = 4$. The queue joins two leaves of level 0 twice, then the two nodes of level 1, then two nodes of level 2, then the two of level 3.

19. A $3$-feasible cut of $g_i$ is $g_j$ together with the inputs $x_{j+2}, \ldots, x_{i+1}$, so it reaches back at most two gates. The labels grow by 1 every two gates, and $g_8$ gets label 4. The tree of 3-input gates has depth 2: FlowMap is optimal only for the structure it is given.

21. $\mathrm{ODC}_1(y)$ is $c = 1$ and $\mathrm{ODC}_2(y)$ is $d = 0$, so $\mathrm{ODC}(y) = c\bar{d}$. The wire $a$ differs from $ab$ at $a = 1, b = 0$, and the vector $1001$ is not in $c\bar{d}$, so the change is not allowed.

23. A cokernel picks one literal from each factor of a proper subset $J$ of the factors, and its kernel is the product of the other factors. So the kernels are the products of nonempty sets of factors, $2^k - 1$ of them, and the pairs number $\sum_{j < k} \binom{k}{j} s^j = (s + 1)^k - s^k$. For $s = 3$ and $k = 3$ that is 7 kernels and 37 pairs.

24. $\mathrm{ODC}(y_1) = ac$, the vectors $101$ and $111$, and $\mathrm{ODC}(y_2) = ab$, the vectors $110$ and $111$. Setting both to 0 at $111$ gives $z = 0$ there, but $z(111) = 1$. In the order $y_1, y_2$, give $y_1$ its full set. Then $y_2$ may change only where $y_1$ is 1 whatever $y_1$ does inside its set, which leaves only the vector $110$.

25. Apply the $3! \cdot 2^3 = 48$ input transforms, and the output negation for NPN, to each of the 256 tables and count the orbits. There are 22 NP classes and 14 NPN classes.

26. The two registers split the ring into at most two register-free segments of consecutive gates. With both on one edge, one path runs through all three gates, delay 9. Otherwise the segments hold one gate and two gates, and the longer has delay 6. Each gate has delay 3, so no segment has delay 5, and 6 is the least.

27. With 3 nodes, list all graphs by computer, or argue from the possible functions of the top node. One graph of 4 nodes is $n_1 = a \wedge b$, $n_2 = \bar{a} \wedge \bar{b}$, $n_3 = c \wedge \bar{n}_2$ and the output $\overline{\bar{n}_1 \wedge \bar{n}_3}$, which is $ab + c(a + b)$. A majority-inverter graph needs one node.

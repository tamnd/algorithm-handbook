3. The quotients are $2$, $-2$ and $-7$: $(66, 29) - 2(43, 19) = (-20, -9)$, then $(43, 19) + 2(-20, -9) = (3, 1)$, then $(-20, -9) + 7(3, 1) = (1, -2)$, after which the quotient is $0$ and no vector gets shorter. The reduced basis is $(1, -2)$, $(3, 1)$, so $\lambda_1 = \sqrt 5$, $\lambda_2 = \sqrt{10}$ and $\det(L) = 7$.

4. $\mu_{21} = 2/5$, $\|b_1^*\|^2 = 25$ and $\|b_2^*\|^2 = 9 < (3/4 - 4/25) \cdot 25 = 14.75$, so the condition fails. After the swap $b_1 = (2, 3)$, $\mu_{21} = 10/13$ rounds to $1$ and $b_2 = (3, -3)$; now $\mu_{21} = -3/13$, $\|b_2^*\|^2 = 225/13 \approx 17.3$, which exceeds $(3/4 - 9/169) \cdot 13 \approx 9.06$. The basis $(2, 3)$, $(3, -3)$ is LLL-reduced.

8. $1.0219^{300} \approx 665$ and $1.0128^{300} \approx 45$, against the proved $2^{74.75} \approx 3 \cdot 10^{22}$. The worst-case bound is of no use for predicting what LLL does on such a lattice.

9. $\mu_{21} = 1/2$ and $\|b_2\| = \sqrt{10} > 2$, so the basis is reduced and $\lambda_1 = 2$, $\lambda_2 = \sqrt{10}$. The triangle $0$, $(2, 0)$, $(1, 3)$ is acute, so the covering radius is its circumradius: the center $(1, 4/3)$ is a deep hole and $\mu(L) = 5/3$. Then $6 \le 2\sqrt{10} \approx 6.32 \le 6.93$.

11. $\|b_2^*\|^2 = 9$, so $|x_2| \le 1$. For $x_2 = 0$, $|x_1| \le 1$; for $x_2 = \pm 1$, the remaining budget is $1$ and $(2 x_1 \pm 1)^2 \le 1$ gives two values of $x_1$. The six vectors are $\pm(2, 0)$, $\pm(1, 3)$ and $\pm(-1, 3)$.

12. At $k = 2$: $b_2 \leftarrow b_2 - 3 b_1 = (-1, 0, 1)$, then the Lovász test fails ($6/5 < 59/20$) and the vectors swap; $b_2 \leftarrow b_2 + b_1 = (1, 1, 1)$ and the test passes. At $k = 3$: $b_3 \leftarrow b_3 - 6 b_2 = (1, -2, 0)$, which leaves $\mu_{31} = -1/2$, and the test passes. The output is $(-1, 0, 1)$, $(1, 1, 1)$, $(1, -2, 0)$ after one swap, and $\det(L) = 5$.

14. The lattice has index $61$ in $\mathbb{Z}^2$, so $\det = 61$. The open disk of radius $\sqrt{122}$ has area $122 \pi > 4 \cdot 61$. For $(a, b)$ in the lattice, $a^2 + b^2 \equiv a^2 (1 + 121) \equiv 0 \pmod{61}$, so a nonzero vector in the disk has $a^2 + b^2 = 61$. Reduction gives $(-6, -5)$, so $61 = 6^2 + 5^2$.

18. The vectors with last coordinate $\pm 1$ are $\pm(t - w, 1)$ with $w \in L$, and $t - (5, 0) = (0, 1)$ gives length $\sqrt 2$. The second minimum is $3$, reached by $(2, 2, -1) = -(t - (7, 3), 1)$. So the closest vector is $(5, 0)$ and the gap is $3 / \sqrt 2 \approx 2.1$.

20. LLL gives $\|b_1\| \le 2^{(n-1)/2} \lambda_1 < \lambda_2$. Two independent lattice vectors shorter than $\lambda_2$ cannot exist, so $b_1$ is a real multiple of $s$, hence an integer multiple, since $s$ is primitive. A basis vector is primitive too, so the multiple is $\pm 1$.

21. The basis is size-reduced and $\|b_1\| = \sqrt 2$ is the minimum. Project onto the orthogonal complement of $b_1$: the projected lattice has basis $(1, 1, 1)$ and $(\tfrac12, -2, \tfrac12)$, with squared lengths $3$ and $9/2$ and inner product $-1$, so $(1, 1, 1)$ is its shortest vector. The minima are $\sqrt 2, \sqrt 3, \sqrt 5$, and $5 \le \sqrt{30} \approx 5.48 \le 5 \sqrt 2$.

22. Take a Lagrange-Gauss reduced basis, so $\|b_1\| = \lambda_1 \le \|b_2\|$ and $|\mu_{21}| \le 1/2$. Then $\det(L)^2 = \|b_1\|^2 (\|b_2\|^2 - \mu_{21}^2 \|b_1\|^2) \ge \tfrac34 \lambda_1^4$. Equality needs $\|b_2\| = \|b_1\|$ and $|\mu_{21}| = 1/2$, an angle of $60°$.

23. The basis rows are $(N, 0, 0)$, $(0, 8N, 0)$ and $(419719, 8 \cdot 654321, 64)$. Reduction gives the first row $(-2863, -1264, 5184)$, that is $h(x) = 81 x^2 - 158 x - 2863 = 81 f(x) - 53 N x - 34 N$, of norm about $6055 < N / \sqrt 3$. Then $h(x) = (x - 7)(81 x + 409)$, so $x_0 = 7$.

24. Use the rows $(2 e_i, C a_i)$ for $i = 1, \ldots, 8$ and $(1, \ldots, 1, C s)$ with $C = 100$. The vector $(\pm 1, \ldots, \pm 1, 0)$ with $-1$ at the chosen weights has length $\sqrt 8$. LLL finds the subset $8513 + 9112 + 6401 + 4459 = 28485$. The density is $8 / \log_2 9112 \approx 0.61$.

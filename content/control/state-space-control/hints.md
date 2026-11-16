1. $[B, AB] = \begin{bmatrix} 1 & 0 \\ 0 & 0 \end{bmatrix}$ has rank 1, so the pair is not controllable. The reachable set is $\operatorname{span}(e_1)$: the input acts only on $x_1$, and $x_2$ never changes, so from the origin it stays 0.

3. At $\lambda = -1$ the matrix $[A + I, B] = \begin{bmatrix} 0 & 0 & 1 \\ 0 & 0 & 1 \end{bmatrix}$ has rank 1, not 2. The eigenvalue $-1$ has geometric multiplicity 2, and $[A - \lambda I, B]$ can have rank 2 only if $B$ has at least 2 columns. Two inputs suffice: $B = I$ works.

4. $A = \begin{bmatrix} 0 & 1 \\ -5 & -3 \end{bmatrix}$, $B = (0, 1)^T$, $C = [1, 2]$. The last row of $A - BK$ is $[-5 - k_1, -3 - k_2]$, and it must be $[-16, -8]$ for $(s + 4)^2 = s^2 + 8s + 16$. So $K = [11, 5]$.

5. $W_c(t) = \int_0^t e^{-4s}\,ds = (1 - e^{-4t})/4$, with limit $1/4$. The least energy is $1/W_c(1) = 4/(1 - e^{-4}) \approx 4.0746$, a little more than the limit 4.

8. $\sigma_1 = |bc|/(2a) = 3/4$. The error is $\|G\|_\infty = G(0) = 3/2 = 2\sigma_1$, so the bound is attained.

10. The observability matrix $\begin{bmatrix} c & 1 \\ -2 & c - 3 \end{bmatrix}$ has determinant $c^2 - 3c + 2 = (c - 1)(c - 2)$, so $c = 1$ or $c = 2$. The transfer function is $(s + c)/((s+1)(s+2))$: for $c = 1$ it is $1/(s + 2)$, and for $c = 2$ it is $1/(s + 1)$. The zero cancels a pole, and the cancelled mode is the one the output cannot see.

15. The controller is $\dot{\hat x} = (A - BK - LC)\hat x + Ly$, $u = -K\hat x$, with $A - BK - LC = \begin{bmatrix} -4 & 1 \\ -6 & -2 \end{bmatrix}$. So $-u = \dfrac{16s + 8}{s^2 + 6s + 14}\,y$. The loop polynomial is $s^2(s^2 + 6s + 14) + 16s + 8 = s^4 + 6s^3 + 14s^2 + 16s + 8 = (s^2 + 2s + 2)(s^2 + 4s + 4)$.

16. The Hankel matrix has rank 2, since each row is the sum of the two rows above it. So the order is 2. The sequence satisfies $h_{k+2} = h_{k+1} + h_k$, so the denominator is $s^2 - s - 1$, and $G(s) = s/(s^2 - s - 1)$. One realization is $A = \begin{bmatrix} 0 & 1 \\ 1 & 1 \end{bmatrix}$, $B = (0, 1)^T$, $C = [0, 1]$; check $CB = 1$, $CAB = 1$, $CA^2B = 2$.

18. $\mathcal V_0 = \ker C = \{x_1 + x_2 = 0\}$ contains $e_3$, so $\mathcal V_0 + \operatorname{im} B = \mathcal V_0$, and $A^{-1}\mathcal V_0 = \{x_2 + x_3 = 0\}$. So $\mathcal V_1 = \operatorname{span}((1, -1, 1)^T)$. Then $\mathcal V_1 + \operatorname{im} B = \mathcal V_0$ again, $\mathcal V_2 = \mathcal V_1$, and the dimensions are $[2, 1, 1]$. Since $Av = -v$ for $v = (1, -1, 1)^T$, the line is invariant even with $K = 0$. It is the mode at $-1$ that cancels in $G(s) = (s + 1)/((s+1)(s+2)(s+3))$, so the output never sees it. The problem is solvable for $E = v$ and not for $E = e_3$.

20. $[A - bK - \lambda I, b] = [A - \lambda I, b]\begin{bmatrix} I & 0 \\ -K & 1 \end{bmatrix}$ has rank $n$, because the right factor is invertible and the PBH test holds. Deleting the last column lowers the rank by at most 1. For $A - bK = -I$ the matrix $A - bK + I$ would be 0, of rank $0 < n - 1$.

21. $A - BK = -K$, so $K$ must have trace 3 and determinant 2: $K = \begin{bmatrix} a & b \\ c & 3 - a \end{bmatrix}$ with $a(3 - a) - bc = 2$, which leaves 2 free parameters, $n(m - 1) = 2$. A Schur form gives $\|K\|_F^2 = 1^2 + 2^2 + \|N\|_F^2 \ge 5$, with equality exactly when $K$ is normal, here symmetric. So the least norm is $\sqrt 5$, attained by $K = Q\operatorname{diag}(1, 2)Q^T$ for every rotation $Q$. Their eigenvectors are orthogonal, so $\kappa_2(X) = 1$.

22. Expand the square and use the residue formula for the inner product. For fixed $\lambda$ the best $\varphi$ is $2\lambda G(\lambda)$, and then the squared error is $\|G\|_{H_2}^2 - 2\lambda G(\lambda)^2$ with $\|G\|_{H_2}^2 = 1/12$. Maximizing $\lambda G(\lambda)^2$ gives $G(\lambda) + 2\lambda G'(\lambda) = 0$, that is $3\lambda^2 + 3\lambda - 2 = 0$, whose only positive root is $\lambda = (\sqrt{33} - 3)/6 \approx 0.45743$. The error tends to $\|G\|_{H_2}$ as $\lambda \to 0$ or $\lambda \to \infty$, so this root is the minimum. Then $\varphi = 6 - \sqrt{33} \approx 0.25544$. The error is $\sqrt{(569 - 99\sqrt{33})/24} \approx 0.10960$. The choice of $\varphi$ gives $G_1(\lambda) = G(\lambda)$, and the condition on $\lambda$ gives $G_1'(\lambda) = G'(\lambda)$: these are the two conditions at the mirror image of the pole $-\lambda$.

23. The polynomial is $s^4 + 6s^3 + 14s^2 + 16ks + 8k$. The Routh array has first column $1$, $6$, $(84 - 16k)/6$, $16k - 288k/(84 - 16k)$, $8k$, so the loop is asymptotically stable exactly for $0 < k < 33/8 = 4.125$. At $k = 33/8$ the roots include $\pm i\sqrt{11}$. With full state feedback the polynomial is $s^2 + 2ks + 2k$, Hurwitz for every $k > 0$.

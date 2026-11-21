1. $r = (89, 56, 12)$ for $k = 0, 1, 2$. The z-transform is $(2 + z)(2 + 3z)$, with zeros $-2$ and $-2/3$.
Flipping $-2$ to $-1/2$ gives $(1 + 2z)(2 + 3z) = 2 + 7z + 6z^2$, so $[2, 7, 6]$ (or its reversal
$[6, 7, 2]$) has the autocorrelation $(89, 56, 12)$ too.

3. A $79 \times 59$ grid, since $2n_k - 1$ samples are needed along each axis. On $64 \times 64$,
$\sigma = 4096/1200 \approx 3.41$, which is above 2 in total although the second axis is not sampled at
$2n_k - 1$. For the cube, $\sigma = 32768/8000 \approx 4.10$.

5. $|F| = (3, \sqrt5, 1, \sqrt5)$. With $G_0 = (1, 1, 1, 1)$ the magnitude step gives
$g'_0 = (1 + \sqrt5/2,\ 1/2,\ 1 - \sqrt5/2,\ 1/2)$, and the support step gives
$g_1 = (1 + \sqrt5/2, 1/2, 0, 0) \approx (2.118, 0.5, 0, 0)$. $E_F(g_0) \approx 2.656$ and
$E_F(g_1) \approx 0.731$. The iterates tend to $(2, 1, 0, 0)$, the reversal of $f$ moved back into the
support: a trivial ambiguity of a real signal.

8. The zeros are at $|f| = \sqrt{k/(\lambda z)}$, $k = 0, 1, 2, \ldots$, so the first nonzero one is at
$1/\sqrt{\lambda z} \approx 44.7$ cycles per mm. The first maximum is at $1/\sqrt{2\lambda z} \approx 31.6$
cycles per mm.

9. Each of the three zeros can be flipped, $(c + z) \to (1 + cz)$, which gives 8 signals with the
autocorrelation $(1962, 1250, 331, 30)$: $[30, 31, 10, 1]$, $[15, 38, 17, 2]$, $[10, 37, 22, 3]$,
$[6, 35, 26, 5]$ and their reversals. That is 4 classes, equal to $2^{n-2}$ for $n = 4$.

10. When the sums are distinct, the differences of $A + B$ are the multiset
$\{(a - a') + (b - b')\}$, and those of $A - B$ are $\{(a - a') - (b - b')\}$; the multiset of differences
of $B$ is symmetric under negation. Here $A + B = \{0,1,3,4,5,7,9,10,12\}$ and, after a shift,
$A - B = \{0,1,3,5,6,8,9,10,12\}$; the reflection of $A + B$ is $\{0,2,3,5,7,8,9,11,12\}$, and both sets
span 12, so no shift can match them.

14. Expand $\mathbb E[(a^\top x)^2 a_ia_j]$ by the fourth moments of Gaussians,
$\mathbb E[a_ia_ja_ka_l] = \delta_{ij}\delta_{kl} + \delta_{ik}\delta_{jl} + \delta_{il}\delta_{jk}$. For
$x = (1, 2, 2)$ the matrix is $\begin{pmatrix}11 & 4 & 4\\ 4 & 17 & 8\\ 4 & 8 & 17\end{pmatrix}$, with
eigenvalues 27, 9, 9 and leading eigenvector $(1, 2, 2)/3$. Since $\mathbb E[y] = \lVert x \rVert^2$, the
mean of the $y_i$ estimates $\lVert x \rVert^2 = 9$.

17. The square gives $[-1, 1]^2$, area 4, four times the square. The triangle gives the hexagon with corners
$\pm(1, 0)$, $\pm(0, 1)$, $\pm(1, -1)$, area 3, six times the triangle. A support taken from the
autocorrelation is therefore much too large, which is why shrinkwrap tightens it.

19. Take $u \ne 0$ orthogonal to the span of the first set and $v \ne 0$ orthogonal to the span of the
second, and put $x = u + v$, $y = u - v$. On the first set $\langle a, x\rangle = -\langle a, y\rangle$, on the
second $\langle a, x\rangle = \langle a, y\rangle$, and $x = \pm y$ would force $u = 0$ or $v = 0$. With
$m \le 2n - 2$, split the vectors into two sets of at most $n - 1$. With $2n - 1$ vectors, one side of any
split has at least $n$ of them.

20. The 2D z-transform of $\tilde v$ is $z_1z_2\,\overline{V(1/\bar z_1, 1/\bar z_2)}$, which has the same
modulus as $V$ on the unit torus. $x = \begin{pmatrix}1&2&0\\5&6&2\\6&5&1\end{pmatrix}$ and
$x' = \begin{pmatrix}1&4&4\\3&8&4\\0&3&1\end{pmatrix}$; the turned $x$ is
$\begin{pmatrix}1&5&6\\2&6&5\\0&2&1\end{pmatrix}$. Products $u * v$ of two $2 \times 2$ images have at
most $4 + 4 - 1 = 7$ free parameters, fewer than the 9 of a $3 \times 3$ image.

21. On $S$, $P_S$ is the identity, so $T(g) = P_Mg$; off $S$ it is zero, so $T(g) = g - P_Mg$. A fixed point
has $P_S(2P_Mg - g) = P_Mg$, so $P_Mg$ is in the range of $P_S$ as well as in the magnitude set.

22. The zero-padded DFT samples the transform of the circular autocorrelation $c_k = \sum_{l \equiv k} r_l$.
With $M = 2n - 2$ the only lags that collide are $\pm(n - 1)$, and $c_{n-1} = 2\operatorname{Re} r_{n-1}$,
which gives $r_{n-1}$ for a real signal but loses its imaginary part for a complex one. The signals
$[1, i]$ and $[1, -i]$ both give $|F_0|^2 = |F_1|^2 = 2$, yet $r_1 = i$ for one and $-i$ for the other.

23. At each frequency one hologram gives one equation in two unknowns. For two holograms the determinant
of $\begin{pmatrix}\sin\alpha_1 & -\cos\alpha_1\\ \sin\alpha_2 & -\cos\alpha_2\end{pmatrix}$ is
$\sin(\alpha_2 - \alpha_1)$.

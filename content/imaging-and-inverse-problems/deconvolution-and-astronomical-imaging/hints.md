2. The error at frequency $k$ is multiplied by $1 - H_k$ in each step. $H_k = 1, 0.911, 2/3, 1/3$ for
$k = 0, 1, 2, 3$ (and $k = 11, 10, 9$), so the error shrinks there. $H_4 = H_8 = 0$, so the error stays.
$H_5 = H_7 \approx -0.244$ and $H_6 = -1/3$, so the error grows by the factors $1.244$ and $4/3$ per step.

3. The dirty image is $(0, 1, 5/2, 2, 1/2, 0)$. Step 1 picks pixel 2 and adds $5/4$, leaving the residual
$(0, 3/8, 5/4, 11/8, 1/2, 0)$. Step 2 picks pixel 3 and adds $11/16$, leaving
$(0, 3/8, 29/32, 11/16, 5/32, 0)$.

4. $u_1 = (1, 5/2, 2, 1/2)$ and $u_2 = (1/2, 45/14, 15/7, 1/7)$; both sum to 6, because the PSF is
normalized and the border is periodic.

7. $k_c \approx 5.385$ cycles per µm, a period of about 185.7 nm. With stripes at $k_c$ the cutoff becomes
$2k_c$, a period of about 92.9 nm; with stripes at $0.8\,k_c$ it is $1.8\,k_c$, about 103.2 nm.

11. $u_1 = (5/2, 3/2)$, $u_2 = (20/7, 8/7)$, $u_3 = (580/187, 168/187)$. The maximum likelihood estimate
is $A^{-1}d = (4, 0)$, which is nonnegative and fits the counts exactly. The iterates approach it slowly
(about $(3.68, 0.32)$ after 10 steps and $(3.97, 0.03)$ after 100), each step further from the truth $(2, 2)$.

12. The residual at the second frequency is $0.15 \cdot 0.9^K$, and the first is zero after one step. It
falls below $\tau\delta = 0.055$ first at $K = 10$. The second component is then
$(1 - 0.9^{10}) \cdot 1.5 \approx 0.977$, against the noisy limit $0.15/0.1 = 1.5$; the true value is 1.

15. Hudgin: $G^\top G$ is the Laplacian of the 4-cycle, whose null space is the constants (piston). Fried: two
equations in four unknowns, with the null space spanned by the constant and by the waffle pattern
$\begin{pmatrix}1 & -1\\ -1 & 1\end{pmatrix}$.

17. The constraint gives $x_1 + x_2 = 3$ or $5$. By symmetry and concavity the maximum on each line is at
$x_1 = x_2$; $S(1.5, 1.5) = 2(0.5 - 1.5\ln 1.5) \approx -0.216$ is larger than
$S(2.5, 2.5) \approx -1.58$, so the answer is $(1.5, 1.5)$.

19. $q$ has degree $2 = f_c$, equals 1 at $0$ and $1/2$ and is below 1 in modulus elsewhere, and the two
columns $e^{-2\pi ikt_j}$, $|k| \le 2$, are independent. The theorem gives sufficient conditions, not
necessary ones: positive spikes need no separation at all.

20. Orthogonality of the error to the data, $\mathbb E[(X - GY)\overline Y] = 0$, gives
$G = \overline{H}S_x/(|H|^2S_x + S_n)$. For the numbers given $G = 0.1/0.02 = 5$, half of $1/H = 10$. As
$S_n \to 0$, $G \to 1/H$ when $H \ne 0$ and $G = 0$ when $H = 0$: the pseudo-inverse.

21. $|1 - \beta H|^2 < 1$ is $\beta^2|H|^2 < 2\beta\operatorname{Re}H$, that is
$\beta < 2\operatorname{Re}H/|H|^2$. A Gaussian PSF has a positive OTF with $H \le 1$, so
$0 < \beta < 2$ works. The box of exercise 2 has negative values, so no $\beta$ works.

22. The difference of two such measures has at most $2f_c$ spikes, and its $2f_c + 1$ coefficients vanish.
The $(2f_c + 1) \times 2f_c$ Vandermonde matrix in $e^{-2\pi it_j}$ has full column rank for distinct $t_j$,
so all amplitudes are zero. The TV theorem adds a convex program that finds the spikes and is stable to
noise when they are separated.

23. The gradient commutes with convolution, and $\lVert k * g\rVert_1 \le \lVert k\rVert_1\lVert g\rVert_1 = \lVert g\rVert_1$.
At $(y, \delta)$ the data term is zero and the prior term is $\lambda\lVert\nabla y\rVert_1 \le \lambda\lVert\nabla x\rVert_1$.

24. Let $d = \psi - \psi'$. Equal bispectrum phases give $d(u + v) = d(u) + d(v)$ modulo $2\pi$ for all
$u, v$, so $d(u) = u_1d(e_1) + u_2d(e_2)$, and periodicity makes $d(e_i)$ a multiple of $2\pi/N_i$. A linear
phase is a shift of the image.

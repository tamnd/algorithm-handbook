1. ◦ Compute the autocorrelation $r_k = \sum_j x_{j+k}x_j$, $k = 0, 1, 2$, of the real signal
$x = [4, 8, 3]$. Factor its z-transform $4 + 8z + 3z^2$, and flip one zero as in
[phase retrieval](/phase-retrieval/) to find a signal with integer entries that has the same autocorrelation
but is not $\pm x$, a shift of $\pm x$ or a reversal of $\pm x$.

2. ◦ For the complex signal $x = [1, i, 2]$, compute $r_k = \sum_j x_{j+k}\overline{x_j}$ for
$k = -2, \ldots, 2$. Check that the conjugate reversal $[2, -i, 1]$ has the same autocorrelation and that the
plain reversal $[2, i, 1]$ does not, as [phase retrieval ambiguities](/phase-retrieval-ambiguities/) says.

3. ◦ An object fills a $40 \times 30$ block of pixels. What is the smallest detector grid, per axis, whose
samples of the far-field intensity give the whole autocorrelation, by the theorem in
[oversampling in phase retrieval](/oversampling-in-phase-retrieval/)? What is the oversampling ratio
$\sigma$ if the pattern is recorded on a $64 \times 64$ grid? What is $\sigma$ for a $20 \times 20 \times 20$
object recorded on a $32^3$ grid?

4. ◦ A one-dimensional periodic cell of length 12 holds three equal point atoms at the positions 0, 2 and 7.
List the positions of the non-origin peaks of the [Patterson function](/patterson-function/), with their
multiplicities, and check that their number is $N(N - 1)$.

5. ◦ Use the length-4 DFT $F_k = \sum_j f_j e^{-2\pi i jk/4}$. The object $f = (1, 2, 0, 0)$ has the support
$\{0, 1\}$. Compute the measured magnitudes $|F_k|$. Run one step of the
[error reduction algorithm](/error-reduction-algorithm/) from $g_0 = (1, 0, 0, 0)$ with the support
constraint only, and give $g_1$ and the Fourier errors $E_F(g) = \lVert |G| - |F| \rVert_2$ of $g_0$ and
$g_1$. To which signal do the iterates converge, and why is it an acceptable answer?

6. ◦ Show that the three vectors $(1, 0)$, $(0, 1)$, $(1, 1)$ in $\mathbb R^2$ have the
[complement property](/complement-property/). Then drop $(1, 1)$ and give two real vectors $x \ne \pm y$
with $|\langle a, x\rangle| = |\langle a, y\rangle|$ for both remaining vectors $a$.

7. ◦ The [angular spectrum method](/angular-spectrum-method/) is run with the wavelength
$\lambda = 0.5\ \mu$m on a square grid of spacing $d = 0.3\ \mu$m. Do all grid frequencies propagate? Find
the largest grid frequency and the fraction of the frequency square that is evanescent.

8. ◦ An in-line hologram of a weak phase object is recorded at $z = 1$ mm with $\lambda = 0.5\ \mu$m. Using
the transfer function $2\sin(\pi\lambda z|f|^2)$ of the [twin image problem](/twin-image-problem/), give the
first nonzero frequency at which the hologram carries no information about the object, the frequency of the
first maximum of the transfer, and the general formula for the zeros.

9. • The real signal $x = [30, 31, 10, 1]$ has the z-transform $(2 + z)(3 + z)(5 + z)$. List all real signals
of length 4, up to sign, with the same autocorrelation, and group them into classes under reversal. Compare
the number of classes with the bound $2^{n-2}$.

10. • Let $A$ and $B$ be finite sets of integers such that the sums $a + b$ are all distinct. Prove that
$A + B$ and $A - B$ have the same multiset of differences, so they are homometric, as in the
[crystallographic phase problem](/crystallographic-phase-problem/). Check it for $A = \{0, 1, 3\}$ and
$B = \{0, 4, 9\}$, and show that these two sets of nine points are not translates or reflections of each
other.

11. • For a complex number $G$ and $m \ge 0$, show that the point of modulus $m$ nearest to $G$ is
$mG/|G|$ when $G \ne 0$. With the unnormalized DFT of length $N$, Parseval reads
$\lVert G \rVert^2 = N\lVert g \rVert^2$. Write $g'_k$ for the image after the magnitude step and $E_0(g'_k)$
for its norm outside the support. Prove the chain
$E_F(g_{k+1}) \le \sqrt N\, E_0(g'_k) \le E_F(g_k)$ for error reduction.

12. • In $\mathbb R^2$ let $A$ be the $x$-axis and $B$ the line $y = x$. Write the Douglas-Rachford step
$T(v) = v + P_B(2P_Av - v) - P_Av$ as a matrix. Show that $\lVert T^k v \rVert = 2^{-k/2}\lVert v \rVert$, and
that the shadow $P_A T^k v$ converges to the only common point. Which algorithm of the
[RAAR](/raar/) family is this?

13. • An off-axis hologram on an axis of $n_a$ samples records $|R + O|^2$ with a tilted plane reference wave of
carrier $c_a$, and the object spectrum lies in $|f_a| \le B$. Name the four terms of the spectrum and the
interval each occupies along the axis, and derive the conditions $3B < |c_a|$ and $|c_a| + B < n_a/2$ of
[digital holography reconstruction](/digital-holography-reconstruction/). For $n_a = 1024$, give the largest
integer $B$, and the range of carriers for $B = 100$.

14. • Let $a$ be a standard Gaussian vector in $\mathbb R^n$ and $y = (a^\top x)^2$. Prove that
$\mathbb E[y\, aa^\top] = \lVert x \rVert^2 I + 2xx^\top$, as used by
[spectral initialization](/spectral-initialization/). For $x = (1, 2, 2)$, give this matrix, its eigenvalues
and its leading eigenvector, and say how the length of $x$ is estimated from the data.

15. • For real Gaussian measurements, write the Wirtinger flow loss as
$f(z) = \frac1{4m}\sum_i\big((a_i^\top z)^2 - y_i\big)^2$. Show that $z = 0$ is a stationary point, that the
Hessian there is $-Y$ with $Y = \frac1m\sum_i y_i a_ia_i^\top$, and what this says about the direction in
which a descent method leaves the origin. Relate it to [Wirtinger flow](/wirtinger-flow/) and its start.

16. • Take $x = (1, 2) \in \mathbb C^2$ and the vectors $a_1 = (1, 0)$, $a_2 = (0, 1)$, $a_3 = (1, 1)$,
$a_4 = (1, i)$, with $y_i = |a_i^* x|^2$. Compute the $y_i$. Show that the four linear equations
$y_i = \operatorname{tr}(a_ia_i^* X)$ determine every Hermitian $2 \times 2$ matrix $X$, so the feasible set
of [PhaseLift](/phaselift/) is one point, and read off $x$ up to a global phase.

17. • The support of the autocorrelation of an object with support $S$ is the difference set $S - S$, which
[shrinkwrap](/shrinkwrap/) thresholds for its first support. Compute $S - S$ and the ratio of its area to the
area of $S$ for the unit square and for the triangle with corners $(0, 0)$, $(1, 0)$, $(0, 1)$.

18. • A unit cell holds one mercury atom ($Z = 80$) and 99 carbon atoms ($Z = 6$), all treated as points. How
many non-origin [Patterson](/patterson-function/) peaks are there, how many of them join the mercury atom to
a carbon atom, and how much higher is such a peak than a carbon-carbon peak? Explain why this makes the
heavy atom easy to find.

19. ★ Prove the real half of the theorem in [complement property](/complement-property/): if the vectors
$a_1, \ldots, a_m \in \mathbb R^n$ can be split into two sets that both fail to span $\mathbb R^n$, then
some $x \ne \pm y$ have $|\langle a_i, x\rangle| = |\langle a_i, y\rangle|$ for all $i$. Deduce that
$m \ge 2n - 1$ is needed, and that $2n - 1$ vectors of which every $n$ are independent have the
complement property, so they suffice by the other half of the theorem.

20. ★ Let $u = \begin{pmatrix}1 & 2\\ 3 & 1\end{pmatrix}$ and $v = \begin{pmatrix}1 & 0\\ 2 & 1\end{pmatrix}$,
and let $\tilde v$ be $v$ turned by 180 degrees. Show that the $3 \times 3$ images $x = u * v$ and
$x' = u * \tilde v$ (2D linear convolution) have the same Fourier magnitude, compute both, and check that
$x'$ is not a shift, sign change or 180-degree turn of $x$. Then explain, by a dimension count, why such
images form a set of measure zero among $3 \times 3$ images, as the
[Bruck-Sodin theorem](/bruck-sodin-uniqueness/) says.

21. ★ Let $P_S$ be the projection onto the images that vanish outside a support $S$ and $P_M$ a projection
onto the images with the measured Fourier magnitude. Show that the Douglas-Rachford step
$T(g) = g + P_S(2P_Mg - g) - P_Mg$ is the [hybrid input-output](/hybrid-input-output/) step with $\beta = 1$.
Then show that for any fixed point $g$ of $T$, the image $P_Mg$ lies in both sets.

22. ★ A signal of length $n$ is zero padded to length $M$ and $|F_k|^2$ is measured at the $M$ DFT
frequencies. Show that for real signals $M = 2n - 2$ samples already give the full autocorrelation, while
for complex signals they do not in general: find two complex signals of length 2 that are not trivially
related and have the same samples for $M = 2$. Compare with the per-axis rule in
[oversampling in phase retrieval](/oversampling-in-phase-retrieval/).

23. ★ In the paraxial model of the [twin image problem](/twin-image-problem/), a weak object
$s = -a + i\varphi$ with real $a$ and $\varphi$ gives an in-line hologram at distance $z$ whose spectrum is, to
first order, $\delta + 2\sin(\alpha)\hat\varphi - 2\cos(\alpha)\hat a$ with $\alpha = \pi\lambda z|f|^2$. Show
that one hologram cannot separate $\hat a$ from $\hat\varphi$ at any frequency, and that two holograms at
$z_1 \ne z_2$ determine both exactly at the frequencies where $\sin(\pi\lambda(z_2 - z_1)|f|^2) \ne 0$.

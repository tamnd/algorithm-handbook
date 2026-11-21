1. ◦ A microscope objective has $\mathrm{NA} = 0.95$ and images at $\lambda = 600$ nm. Give the Rayleigh
distance $0.61\lambda/\mathrm{NA}$ of the [Rayleigh criterion](/rayleigh-criterion/), the finest period
$\lambda/(2\,\mathrm{NA})$ passed by the [Abbe diffraction limit](/abbe-diffraction-limit/), and the
incoherent cutoff frequency in cycles per µm. Then give the Rayleigh angle $1.22\lambda/D$ of a telescope of
diameter $D = 8.2$ m at $\lambda = 2.2\ \mu$m, in radians and in arcseconds.

2. ◦ A periodic signal of length 12 is blurred by the box $h = (1, 1, 1)/3$ centred at 0, whose DFT is
$H_k = (1 + 2\cos(\pi k/6))/3$. Run [van Cittert deconvolution](/van-cittert-deconvolution/) with
$\beta = 1$ on noise-free data. At which frequencies $k$ does the error grow, at which does it stay the
same, and at which does it shrink?

3. ◦ A one-dimensional dirty beam has the values $1/2, 1, 1/2$ at the offsets $-1, 0, 1$, and the sky has a
point of flux 2 at pixel 2 and a point of flux 1 at pixel 3, on pixels $0, \ldots, 5$. Compute the dirty
image, and run two steps of [Högbom CLEAN](/hogbom-clean/) with gain $g = 1/2$. Give the component and the
residual after each step.

4. ◦ Run two steps of [Richardson-Lucy deconvolution](/richardson-lucy-deconvolution/) on four periodic
pixels with the PSF $(1/4, 1/2, 1/4)$ centred at 0, the data $d = (0, 4, 2, 0)$ and the flat start
$u_0 = (3/2, 3/2, 3/2, 3/2)$. Check that the total flux stays 6.

5. ◦ An emitter gives $N = 1000$ photons, the Gaussian PSF has width $s = 100$ nm, the pixels have side
$a = 100$ nm and there is no background. Using the [localization precision formula](/localization-precision-formula/),
give the Thompson-Larson-Webb precision, the least squares precision of Mortensen and coworkers, and the
bound $s/\sqrt N$ for an ideal detector without pixels.

6. ◦ The PSF of a microscope is a Gaussian of width $\sigma = 120$ nm. Give the width of the
[SOFI](/sofi/) PSF of orders 2, 3 and 4. An emitter is on with probability $\rho$ in each frame,
independently; its fourth cumulant is $\rho(1 - \rho)(1 - 6\rho(1 - \rho))$. Evaluate it at $\rho = 1/2$.

7. ◦ For [structured illumination](/structured-illumination-microscopy/) at $\lambda = 520$ nm with
$\mathrm{NA} = 1.4$, give the incoherent cutoff $k_c = 2\,\mathrm{NA}/\lambda$ and the finest period without
stripes. What is the finest period when the stripe frequency is $k_c$, and when it is $0.8\,k_c$?

8. ◦ In [w-projection](/w-projection/) the error of ignoring the w-term at a direction of radius $\rho$
from the phase centre is bounded by $2\pi|w|\bigl(1 - \sqrt{1 - \rho^2}\bigr)S'$, where $S'$ is the total
flux. Evaluate the bound for $w = 1000$ wavelengths and $\rho = 0.01$ rad. For which $\rho$ does it fall to
$0.01\,S'$?

9. ◦ In [multi-frame super-resolution](/multiframe-super-resolution/) with the decimation factor $L = 3$,
four frames have the shifts $0, 3, 4, 8$ in fine pixels. Do they determine the fine image? Answer the same
question for the shifts $0, 3, 6, 1$.

10. • In the setting of exercise 2, replace the van Cittert step by
[Landweber iteration](/landweber-iteration/), which applies the mirrored PSF to the residual. Show that the
error at frequency $k$ is multiplied by $1 - \beta|H_k|^2$, give the range of $\beta$ for which no
frequency diverges, and compute the filter factor $1 - (1 - \beta|H_k|^2)^K$ at $H_k = -1/3$ for
$\beta = 1$ and $K = 10$.

11. • Two pixels are imaged by $A = \begin{pmatrix}3/4 & 1/4\\ 1/4 & 3/4\end{pmatrix}$, and the Poisson
counts are $d = (3, 1)$. Run three steps of Richardson-Lucy from $u_0 = (2, 2)$, which here is also the
true scene. Find the maximum likelihood estimate and show that the iterates move away from the truth
towards it.

12. • A blur has the transfer values $H = (1, 0.1)$ at two frequencies; the true spectrum is $(1, 1)$ and the
noise spectrum is $(0, 0.05)$. Run van Cittert with $\beta = 1$ and stop it by the
[discrepancy principle](/morozov-discrepancy-principle/) with $\tau = 1.1$ and noise level
$\delta = 0.05$, that is at the first $K$ with residual at most $\tau\delta$. Give $K$, the estimate of the
second component then, and the limit of that component as $K \to \infty$.

13. • In blind deconvolution, as in [Ayers-Dainty](/ayers-dainty-blind-deconvolution/), the data are
$y = h * x$ with both factors unknown. Show that for
every $c \ne 0$ and every shift $t$ the pair $c\,x(\cdot - t)$, $h(\cdot + t)/c$ gives the same data. Which
of the two ambiguities is removed by the constraints $h \ge 0$ and $\sum h = 1$?

14. • The dirty beam is $(0.3, 0.8, 1, 0.8, 0.3)$ at the offsets $-2, \ldots, 2$, and the sky is two points of
flux 1 at pixels 2 and 4. Compute the dirty image on pixels $0, \ldots, 6$ and say where
[Högbom CLEAN](/hogbom-clean/) puts its first component. What does this say about CLEAN and the true sky?

15. • A $2 \times 2$ grid of phase values is measured by slopes. In the Hudgin geometry each of the four edges
gives the difference of its two end values; in the Fried geometry the one square gives the average
difference in $x$ and in $y$. For each, find the null space of the least squares problem of
[zonal wavefront reconstruction](/zonal-wavefront-reconstruction/).

16. • In [nearest neighbour deconvolution](/nearest-neighbor-deconvolution/) each plane is estimated as
$\hat x_j = y_j - c\,(h_{+1} * y_{j-1} + h_{-1} * y_{j+1})$ with normalized defocus PSFs $h_{\pm1}$. A
focal series is constant, with the value 10 in every pixel of every plane. What is $\hat x_j$ for
$c = 0.45$ and for $c = 1/2$? Why is this a warning about the method?

17. • In the [maximum entropy method](/maximum-entropy-method-imaging/) with the entropy
$S(x) = \sum_i \bigl(x_i - m_i - x_i\ln(x_i/m_i)\bigr)$, take two pixels, the default $m = (1, 1)$, one datum
$y = x_1 + x_2 = 4$ with $\sigma = 1$, and the constraint $\chi^2 = 1$. Find the image of maximum entropy and
its entropy.

18. • The Sparrow criterion calls two equal points just resolved when the second derivative of their sum is
zero at the midpoint. Find the Sparrow distance for the Gaussian PSF $e^{-x^2/(2s^2)}$, and compare it with
the width $2s$ of the PSF at $e^{-1/2}$ of its peak.

19. • Let $f_c = 2$ and $x = \delta_0 + \delta_{1/2}$ on the circle $[0, 1)$. Show that $q(t) = \cos(4\pi t)$ is a
dual certificate for $x$ in the [Beurling LASSO](/beurling-lasso/) with exact data, and conclude that $x$ is
the unique measure of least total variation with its coefficients $|k| \le 2$. Explain why this does not
contradict the separation condition of the
[total variation theorem](/super-resolution-total-variation-theorem/).

20. ★ Let $Y = HX + V$ at one frequency, with $X$ and $V$ uncorrelated, zero mean, of power $S_x$ and $S_n$.
Derive the gain $G$ of the linear estimate $GY$ of least mean square error, and show that it is the
[Wiener filter](/wiener-filter/) gain $\overline{H}S_x/(|H|^2S_x + S_n)$. Evaluate it for $H = 0.1$,
$S_x = 1$, $S_n = 0.01$, compare with $1/H$, and give its limit as $S_n \to 0$ when $H = 0$ and when
$H \ne 0$.

21. ★ Prove that van Cittert with a fixed $\beta > 0$ converges at every frequency with $H_k \ne 0$ if and
only if $\operatorname{Re} H_k > 0$ for all such $k$, and that the admissible $\beta$ are then
$0 < \beta < \min_k 2\operatorname{Re}H_k/|H_k|^2$. Apply this to a Gaussian PSF and to the box of
exercise 2.

22. ★ Prove that a measure on the circle with at most $f_c$ spikes, with complex amplitudes, is determined
by its Fourier coefficients for $|k| \le f_c$, with no condition on the separation. Use the
[Vandermonde matrix](/vandermonde-matrix/) of the difference of two such measures. Then say what the total
variation theorem adds to this fact, in view of the [Prony method](/prony-method/).

23. ★ For a kernel $k \ge 0$ with $\sum k = 1$, show that $\lVert\nabla(k * x)\rVert_1 \le \lVert\nabla x\rVert_1$.
Deduce that for noise-free data $y = k * x$ the joint MAP cost
$\lVert y - k * x\rVert^2/(2\sigma^2) + \lambda\lVert\nabla x\rVert_1$ is at least as small at the no-blur
pair $(y, \delta)$ as at the true pair, which is why
[variational Bayes blind deconvolution](/variational-bayes-blind-deconvolution/) averages over the image.

24. ★ The bispectrum phase of an image with Fourier phase $\psi$ is
$\psi(u) + \psi(v) - \psi(u + v)$, and [speckle masking](/speckle-masking/) measures it free of turbulence.
Show that two images on a periodic grid with the same Fourier modulus and the same bispectrum phase at all
pairs $(u, v)$ differ only by a shift, so the bispectrum fixes the object up to its position.

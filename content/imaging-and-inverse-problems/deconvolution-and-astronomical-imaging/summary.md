## What to remember

- **The cutoff is a theorem, the resolution criterion a convention.** The incoherent OTF is the normalized
  autocorrelation of the pupil, with $H(0) = 1$ and $|H| \le 1$, and in the scalar model it is zero above
  $2\,\mathrm{NA}/\lambda$ (Abbe), so periods below $\lambda/(2\,\mathrm{NA})$ are lost. Rayleigh's
  $0.61\lambda/\mathrm{NA}$, with a dip of about 26%, and Sparrow's $0.47\lambda/\mathrm{NA}$ are
  agreed thresholds for two points.
- **Unregularized iterations semiconverge.** Van Cittert multiplies the error at frequency $k$ by
  $1 - \beta H_k$ and diverges where the OTF is negative; applying the mirrored PSF turns it into Landweber.
  [Richardson-Lucy](/richardson-lucy-deconvolution/) is EM for Poisson counts: its likelihood never falls,
  it keeps flux and positivity, and it tends to the noisy maximum likelihood estimate. All of them are
  stopped early, by the [discrepancy principle](/morozov-discrepancy-principle/) when the noise level is
  known.
- **Linear estimation.** Wiener deconvolution $\overline{H}S_x/(|H|^2S_x + S_n)$ is the linear MMSE
  estimator for stationary signal and noise with known spectra, and the best of all estimators only when
  both are Gaussian.
- **Blind deconvolution is ambiguous.** $(c\,x(\cdot - t),\ h(\cdot + t)/c)$ fits as well as $(x, h)$, and
  the pair (data, delta) fits perfectly. Ayers-Dainty has no convergence proof; joint MAP with a sparse gradient prior prefers the no-blur
answer, so variational Bayes averages over the image.
- **CLEAN fits the data, not the sky.** Högbom CLEAN is greedy coordinate descent on the misfit $Q$; each
  step lowers $Q$ by $(2g - g^2)R_p^2/B_0$ for $0 < g < 2$ and the residual tends to zero. Many skies fit the same visibilities, and CLEAN need not find the true one.
- **Turbulence.** Speckle interferometry recovers $|O|^2$ to the diffraction limit from
  $\langle|I|^2\rangle = |O|^2\langle|T|^2\rangle$; the bispectrum of speckle masking is unchanged by image
  motion, so the phase is found but the absolute position is lost.
- **Super-resolution has conditions.** Shifted frames determine the fine image when their shift residues
  modulo $L$ cover all residues. Linear SIM at most doubles the cutoff. Localization precision obeys
  $\sigma^2 \ge s^2/N$ for a Gaussian PSF of width $s$ and $N$ photons, and maximum likelihood reaches it only
  for large counts and a correct PSF. TV minimization recovers spikes exactly from $|k| \le f_c$ when
  $f_c \ge 128$ and the separation is at least $2/f_c$.

| Method | Data | What is proved | Time |
|---|---|---|---|
| [Van Cittert](/van-cittert-deconvolution/) | known PSF | converges iff $\lvert 1 - \beta H_k\rvert < 1$ at all $H_k \ne 0$ | $\Theta(Knm)$ |
| [Richardson-Lucy](/richardson-lucy-deconvolution/) | Poisson, known PSF | likelihood never falls; flux kept | $\Theta(Knm)$ |
| [RL with TV](/richardson-lucy-total-variation/) | Poisson, known PSF | positive for $\lambda < 1/4$ in 2D; no monotonicity | $\Theta(Knm)$ |
| [Maximum entropy](/maximum-entropy-method-imaging/) | Gaussian, known PSF | unique solution for each $\lambda$ | $\Theta(mn^2 + Kn^3)$ |
| [Ayers-Dainty](/ayers-dainty-blind-deconvolution/) | blind | no convergence proof | $\Theta(KN\log N)$ |
| [VB blind](/variational-bayes-blind-deconvolution/) | blind | free energy never falls | $\Theta(K(n^3 + 2^m m^3))$ |
| [Högbom CLEAN](/hogbom-clean/) | dirty image | $Q$ falls each step; residual $\to 0$ | $\Theta(Kn)$ |
| [Cotton-Schwab](/cotton-schwab-clean/) | visibilities | exact residual each major cycle; not monotone | $\Theta(Cmn + K(n + b))$ |
| [Multiscale CLEAN](/multiscale-clean/) | dirty image | $Q$ falls each step | $\Theta(Ksn + s^2n\log n)$ |
| [Back-projection](/iterative-back-projection-super-resolution/) | shifted frames | Landweber; converges for small steps | $\Theta(TKnm)$ |
| [Drizzle](/drizzle/) | shifted frames | linear; keeps flux; no deblurring | $\Theta(Knc + m)$ |
| [ML localization](/maximum-likelihood-localization/) | Poisson, one emitter | reaches the CRB only asymptotically | $\Theta(KP)$ |

: The main methods of the chapter. $K$ counts iterations, $n$ or $N$ pixels and $m$ PSF entries, except
that $m$ counts data for MEM, kernel entries for VB, visibilities for Cotton-Schwab and output pixels for
drizzle; the entries define the other letters.

## Choosing a method

With a known PSF and photon counts, use Richardson-Lucy and stop it early, or add a TV term when the
noise is strong and the scene has edges. With Gaussian noise and known spectra,
the Wiener filter is the linear choice. Avoid plain van Cittert when the OTF changes
sign, as defocus and motion blur do. When the PSF is unknown, fix its sum, support and positivity, or measure the wavefront by phase
diversity or a slope sensor. For radio data, run Cotton-Schwab major cycles, use multiscale components for extended emission and
w-projection for wide fields. For dithered frames, drizzle when the goal is a photometric image, and use back-projection or a
regularized inverse when the goal is detail. In fluorescence microscopy, choose SIM for live samples when a gain of two is enough, and localization
when tens of nanometres are needed and the emitters can be made sparse.

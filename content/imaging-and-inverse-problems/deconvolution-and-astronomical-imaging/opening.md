Every optical instrument blurs. A telescope, a microscope or a radio array records the scene convolved with
its [point spread function](/point-spread-function/), adds noise and samples the result. In Fourier terms
the instrument multiplies the spectrum of the scene by a transfer function that falls to zero at a cutoff
frequency, so the finest detail is not damped but absent. Deconvolution tries to undo the blur inside the
passband, where the data still carry the information. Super-resolution tries to go further: finer than the
pixels, which needs several shifted frames, or finer than the diffraction limit, which needs something
the optics does not provide, such as structured light, emitters that switch on one at a time, or the
knowledge that the scene is a few points.

The methods of this chapter come mostly from astronomy and fluorescence microscopy. A radio interferometer
measures Fourier coefficients of the sky at scattered points, and the CLEAN family removes the sidelobes
that the missing coefficients leave. Ground-based telescopes look through turbulence that changes the blur
every few milliseconds, which speckle methods, lucky imaging and wavefront sensing work around.
Microscopists localize single molecules to a few nanometres with a lens that resolves a few hundred.

Most of these algorithms are iterations without a regularization term, and many of their guarantees are
weak or conditional. [Richardson-Lucy](/richardson-lucy-deconvolution/) is EM for Poisson data and tends to
the noisy maximum likelihood estimate, so it is stopped early; van Cittert and Landweber iterations show the same
[semi-convergence](/semi-convergence/). The [Wiener filter](/wiener-filter/) is the best linear estimator
for stationary Gaussian signal and noise with known spectra. CLEAN is greedy and fits the data, but nothing
says it reaches the true sky. Blind deconvolution can never fix the scale and position of the image and the
blur separately. The resolution limits themselves hold under stated models: the Abbe limit for scalar
incoherent imaging, the exact recovery of spikes for a stated minimum separation.

## What the chapter covers

1. **What the optics passes.** The [optical transfer function](/optical-transfer-function/), the
   [Rayleigh criterion](/rayleigh-criterion/) and the [Abbe diffraction limit](/abbe-diffraction-limit/).
2. **Deconvolution with a known blur.** [Van Cittert deconvolution](/van-cittert-deconvolution/),
   [Richardson-Lucy with total variation](/richardson-lucy-total-variation/), the
   [maximum entropy method](/maximum-entropy-method-imaging/), and for widefield microscopy the
   [Gibson-Lanni model](/gibson-lanni-model/) and [nearest neighbour deconvolution](/nearest-neighbor-deconvolution/).
3. **Imaging through turbulence.** [Lucky imaging](/lucky-imaging/),
   [speckle interferometry](/speckle-interferometry/), the [Knox-Thompson method](/knox-thompson-method/)
   and [speckle masking](/speckle-masking/).
4. **Blind deconvolution and the wavefront.** [Ayers-Dainty](/ayers-dainty-blind-deconvolution/),
   [variational Bayes blind deconvolution](/variational-bayes-blind-deconvolution/),
   [phase diversity](/phase-diversity/) and [zonal wavefront reconstruction](/zonal-wavefront-reconstruction/).
5. **Radio interferometry and CLEAN.** The [Van Cittert-Zernike theorem](/van-cittert-zernike-theorem/),
   [aperture synthesis](/aperture-synthesis/), the [dirty image](/dirty-image/),
   [Högbom CLEAN](/hogbom-clean/), [Cotton-Schwab CLEAN](/cotton-schwab-clean/),
   [multiscale CLEAN](/multiscale-clean/) and [w-projection](/w-projection/).
6. **Super-resolution from many frames.** [Multi-frame super-resolution](/multiframe-super-resolution/),
   [iterative back-projection](/iterative-back-projection-super-resolution/) and [drizzle](/drizzle/).
7. **Fluorescence microscopy beyond the diffraction limit.**
   [Structured illumination](/structured-illumination-microscopy/),
   [single-molecule localization](/single-molecule-localization/), the
   [localization precision formula](/localization-precision-formula/),
   [maximum likelihood localization](/maximum-likelihood-localization/) and [SOFI](/sofi/).
8. **Sparse super-resolution theory.** The [Beurling LASSO](/beurling-lasso/) and
   [exact super-resolution by total variation minimization](/super-resolution-total-variation-theorem/).

## A first reading

Read these in order:

1. [Optical transfer function](/optical-transfer-function/)
2. [Abbe diffraction limit](/abbe-diffraction-limit/)
3. [Rayleigh criterion](/rayleigh-criterion/)
4. [Van Cittert deconvolution](/van-cittert-deconvolution/)
5. [Speckle interferometry](/speckle-interferometry/)
6. [Lucky imaging](/lucky-imaging/)
7. [Van Cittert-Zernike theorem](/van-cittert-zernike-theorem/)
8. [Aperture synthesis](/aperture-synthesis/)
9. [Dirty image](/dirty-image/)
10. [Högbom CLEAN](/hogbom-clean/)
11. [Multi-frame super-resolution](/multiframe-super-resolution/)
12. [Single-molecule localization](/single-molecule-localization/)

The microscopy models of the second group, the bispectrum and blind methods, the refinements of CLEAN and
the sparse theory of the last group can wait. The groups after the first depend little on each other, so a
reader interested in one instrument can go from the first group straight to its group.

## Before you start

From Volume 28 the chapter uses the [point spread function](/point-spread-function/),
[image deblurring](/image-deblurring/), [Richardson-Lucy deconvolution](/richardson-lucy-deconvolution/),
the [Wiener filter](/wiener-filter/), [cross-correlation](/cross-correlation/),
[aliasing](/aliasing/) and [image registration](/image-registration/). The
[discrete Fourier transform](/discrete-fourier-transform/) and the
[convolution theorem](/convolution-theorem/) come from Volume 11. From earlier in this volume it uses
[Landweber iteration](/landweber-iteration/), the
[discrepancy principle](/morozov-discrepancy-principle/), [speckle](/speckle/) and
[phase retrieval](/phase-retrieval/). The statistical entries need
[maximum likelihood estimation](/maximum-likelihood-estimation/) and
[variational inference](/variational-inference/) from Volume 25, the
[Cramér-Rao bound](/cramer-rao-bound/) from Volume 33 and the
[Poisson distribution](/poisson-distribution/) from Volume 1. Zonal reconstruction solves a
[least squares problem](/least-squares-problem/) by the
[conjugate gradient method](/conjugate-gradient-method/) (Volume 12), and the sparse theory uses
[Lagrangian duality](/lagrangian-duality/) from Volume 15.

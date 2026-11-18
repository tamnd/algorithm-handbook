Every optical instrument blurs. A microscope, a telescope or a camera records the true scene convolved with its point spread function, adds noise, and samples the result on a grid of pixels. Deconvolution tries to undo the blur, and super-resolution tries to recover detail finer than the pixels or than the diffraction limit of the optics. Both are ill-posed: the blur removes high frequencies, and any method that puts them back must also decide what to do with the noise at those frequencies. Prior knowledge, such as positivity, a few point sources or a known noise distribution, is what makes the problem solvable.

Astronomy and microscopy have driven many of the algorithms. Radio astronomers form images from interferometer data that sample the sky's Fourier transform only at scattered points, and remove the resulting artifacts with the CLEAN family. Optical astronomers fight the turbulence of the atmosphere with speckle methods and lucky imaging. Fluorescence microscopists beat the diffraction limit by localizing single molecules, one at a time, to a precision much finer than the width of the point spread function. The theory of super-resolution says when such recovery is possible: exact recovery of point sources by total variation minimization holds when the sources are separated by a stated minimum distance.

## What the chapter will cover

The entries of this chapter are being written. They will cover:

1. **Image formation and limits.** The Abbe diffraction limit, the Rayleigh criterion, the optical transfer function and the Gibson-Lanni model of a microscope point spread function.
2. **Deconvolution.** Van Cittert deconvolution, nearest neighbor deconvolution, Richardson-Lucy with total variation regularization, the maximum entropy method, and blind deconvolution by the Ayers-Dainty method, variational Bayes and phase diversity.
3. **Radio interferometry.** Aperture synthesis, the van Cittert-Zernike theorem, the dirty image, Högbom, Cotton-Schwab and multiscale CLEAN, and W-projection.
4. **Imaging through turbulence.** Speckle interferometry, the Knox-Thompson method, speckle masking, lucky imaging and zonal wavefront reconstruction.
5. **Super-resolution.** Multi-frame and iterative back-projection super-resolution, drizzle, the Beurling LASSO and exact super-resolution by total variation minimization, single-molecule localization with its precision formula and maximum likelihood localization, structured illumination microscopy and SOFI.

## What to read meanwhile

Volume 28 has the written entries closest to this chapter: the [point spread function](/point-spread-function/), [Richardson-Lucy deconvolution](/richardson-lucy-deconvolution/), the [Wiener filter](/wiener-filter/), [super-resolution](/super-resolution/), [image denoising](/image-denoising/) and [total variation denoising](/total-variation-denoising/). The [convolution theorem](/convolution-theorem/) and the [fast Fourier transform](/fast-fourier-transform/) of Volume 11 explain why blur is a product in the frequency domain, and [Tikhonov regularization](/tikhonov-regularization/) of Volume 12 is the simplest stable inverse. CLEAN is a greedy method close to [orthogonal matching pursuit](/orthogonal-matching-pursuit/) in Volume 28, and the precision of single-molecule localization is limited by the [Cramér-Rao bound](/cramer-rao-bound/) of Volume 33.

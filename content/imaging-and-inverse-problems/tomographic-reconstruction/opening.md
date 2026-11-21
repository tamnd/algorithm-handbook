A CT scanner sends X-rays through a body from many directions and counts how many get through. By the
[Beer-Lambert law](/beer-lambert-law/) the logarithm of the ratio of counts is the integral of the attenuation
along the ray. So the data are line integrals of an unknown image, and the image is a function on the plane
that has to be found from its integrals along lines. That is the inversion of the
[Radon transform](/radon-transform/). Radon gave an exact formula in 1917. A scanner has a finite number of
angles and detector cells, Poisson noise in every count, rays from a point source instead of parallel beams,
and sometimes a gap in the angles or a metal implant in the way. The chapter is about what survives of the
exact formula under each of these limits, and what replaces it when nothing does.

The central fact is the [Fourier slice theorem](/fourier-slice-theorem/): the 1D Fourier transform of a
projection is the 2D Fourier transform of the image along one line through the origin. Weight each projection
by the [ramp filter](/ramp-filter/) $|\sigma|$, smear it back over the plane, and the sum over angles is the
image. This is [filtered back-projection](/filtered-back-projection/), which costs $O(a d \log d + a n^2)$ for
$a$ angles, $d$ detector cells and an $n \times n$ image, and it is still the default in clinical CT. The ramp
amplifies high frequencies by $|\sigma|$, and that one factor is the whole ill-posedness of the problem: mild,
of degree $1/2$, much milder than deblurring.

## What the chapter covers

The chapter is in 7 groups, read in order.

1. **Projections and the data.** The [Radon transform](/radon-transform/), the [sinogram](/sinogram/), the
   [Shepp-Logan phantom](/shepp-logan-phantom/), the 3D [X-ray transform](/x-ray-transform/), the
   [back-projection operator](/back-projection-operator/) and the
   [reconstruction problem](/tomographic-reconstruction-problem/) with its sampling rules.
2. **Fourier methods and filtered back-projection.** The slice theorem, the ramp filter and its windows,
   filtered back-projection, [direct Fourier reconstruction](/direct-fourier-reconstruction/) and the
   [Radon inversion formula](/radon-inversion-formula/).
3. **Fan beams and cone beams.** [Fan-beam FBP](/fan-beam-filtered-back-projection/) with short scans,
   [rebinning](/fan-to-parallel-rebinning/), the approximate [Feldkamp-Davis-Kress](/feldkamp-davis-kress/)
   method, [Grangeat's formula](/grangeat-formula/), the [Tuy condition](/tuy-condition/) and the exact
   [Katsevich algorithm](/katsevich-algorithm/) for the helix.
4. **Discrete models and algebraic methods.** The projectors of [Siddon](/siddon-algorithm/),
   [Joseph](/joseph-projector/) and the [distance-driven](/distance-driven-projector/) kind, and the iterations
   [SIRT](/sirt/) and [SART](/sart/).
5. **Emission tomography.** The Poisson [model](/emission-tomography-model/), [MLEM](/mlem-reconstruction/),
   [OSEM](/osem/), the penalized methods [one-step-late](/one-step-late-algorithm/) and
   [SPS](/separable-paraboloidal-surrogates/), the [attenuated Radon transform](/attenuated-radon-transform/)
   and [Novikov's formula](/novikov-inversion-formula/).
6. **Incomplete data and artifacts.** [Limited angle](/limited-angle-tomography/),
   [interior](/interior-tomography/), [lambda](/lambda-tomography/) and
   [sparse-view](/sparse-view-ct-reconstruction/) tomography, [ASD-POCS](/asd-pocs/),
   [beam hardening](/beam-hardening/) and [metal artifact reduction](/metal-artifact-reduction/).
7. **Related problems.** [Discrete tomography](/discrete-tomography/),
   [single particle reconstruction](/single-particle-reconstruction/) and the
   [common lines method](/common-lines-method/) from cryo-electron microscopy, and the
   [Calderón problem](/calderon-problem/) of impedance tomography with the [D-bar method](/d-bar-method/).

## A first reading

For a short path through the chapter, read these ten entries in order:

1. [Radon transform](/radon-transform/)
2. [Sinogram](/sinogram/)
3. [Back-projection operator](/back-projection-operator/)
4. [Fourier slice theorem](/fourier-slice-theorem/)
5. [Ramp filter](/ramp-filter/)
6. [Filtered back-projection](/filtered-back-projection/)
7. [Feldkamp-Davis-Kress](/feldkamp-davis-kress/)
8. [SIRT](/sirt/)
9. [MLEM](/mlem-reconstruction/)
10. [Limited-angle tomography](/limited-angle-tomography/)

The first six give the analytic method from the data to the image. FDK shows what changes in a cone. SIRT and
MLEM are the two iterative families, one for least squares and one for Poisson counts. The limited angle entry
shows how fast things go wrong when a range of directions is missing.

## Before you start

The Fourier side needs the [discrete Fourier transform](/discrete-fourier-transform/) and the
[fast Fourier transform](/fast-fourier-transform/) (Volume 11), the [nonuniform FFT](/nonuniform-fft/) for direct
Fourier reconstruction (Volume 11), and the [sampling theorem](/sampling-theorem/) (Volume 28). The algebraic
methods use [least squares](/least-squares-problem/) and the [Kaczmarz method](/kaczmarz-method/) (Volume 12).
The emission methods use the [Poisson distribution](/poisson-distribution/) (Volume 1) and
[maximum likelihood](/maximum-likelihood-estimation/) with [EM](/expectation-maximization/) (Volume 25). From
chapter 46.1 you need the [forward operator](/forward-operator/), the
[Landweber iteration](/landweber-iteration/) and [semi-convergence](/semi-convergence/); ASD-POCS and sparse view
use [total variation](/total-variation-denoising/) and [compressed sensing](/compressed-sensing/) from
Volume 28.

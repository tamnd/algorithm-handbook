A CT scanner sends X-rays through a body from many directions and records how much each ray is weakened. By the Beer-Lambert law, the logarithm of the weakening is the integral of the attenuation along the ray, so the data are line integrals of the unknown image: its Radon transform. Tomographic reconstruction inverts that transform. The Fourier slice theorem says that the one-dimensional Fourier transform of each projection is a line through the two-dimensional Fourier transform of the image, and filtered back-projection, which follows from it, is still the workhorse of clinical scanners.

The chapter covers the exact inversion formulas for parallel, fan and cone beams, the discretized algebraic and statistical methods that handle noise and incomplete data better, and the hard cases: few views, limited angles, a region of interest inside a larger body, and emission tomography, where the data are Poisson counts. It also covers related problems that share the mathematics, such as electrical impedance tomography and the reconstruction of molecules from cryo-electron microscopy images.

## What the chapter will cover

The entries of this chapter are being written. They will cover:

1. **The transforms.** The tomographic reconstruction problem, the Beer-Lambert law, the Radon and X-ray transforms, the sinogram, the back-projection operator, the Fourier slice theorem, the Radon inversion formula, the attenuated Radon transform and the Novikov inversion formula.
2. **Analytic reconstruction.** Filtered back-projection and the ramp filter, direct Fourier reconstruction, fan-beam filtered back-projection and fan-to-parallel rebinning, the Feldkamp-Davis-Kress algorithm, the Tuy condition, Grangeat's formula and the Katsevich algorithm for helical scans.
3. **Discrete projectors and algebraic methods.** Siddon's algorithm, Joseph's projector, the distance-driven projector, SIRT, SART, adaptive steepest descent POCS and discrete tomography.
4. **Statistical methods for emission tomography.** The emission tomography model, maximum likelihood expectation maximization, ordered subsets EM, the one-step-late algorithm and separable paraboloidal surrogates.
5. **Incomplete data and artifacts.** Limited-angle, interior, lambda and sparse-view tomography, beam hardening, metal artifact reduction and the Shepp-Logan phantom used to test them.
6. **Related problems.** The Calderón problem and the D-bar method of electrical impedance tomography, the common lines method and single-particle reconstruction.

## What to read meanwhile

The algebraic methods are the [Kaczmarz method](/kaczmarz-method/) of Volume 12 applied to a projection matrix, and the [conjugate gradient method](/conjugate-gradient-method/) there solves the least squares form. The Fourier slice theorem rests on the [fast Fourier transform](/fast-fourier-transform/) and the [convolution theorem](/convolution-theorem/) of Volume 11, and direct Fourier reconstruction needs the [nonuniform FFT](/nonuniform-fft/) there. MLEM is [expectation maximization](/expectation-maximization/) of Volume 25 for Poisson data, and it has the same form as [Richardson-Lucy deconvolution](/richardson-lucy-deconvolution/) in Volume 28. Siddon's algorithm walks a ray through a grid much as the [Bresenham line algorithm](/bresenham-line-algorithm/) of Volume 28 does.

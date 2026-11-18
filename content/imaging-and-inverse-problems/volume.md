A CT scanner never sees the inside of a body. It records how much each X-ray beam is weakened on its way through, and a computer turns thousands of such numbers into a slice. An MRI scanner records samples of a Fourier transform, a radar records echoes, a seismic survey records vibrations at the surface, and an X-ray diffraction camera records only the brightness of a pattern whose phase is lost. In each case the image is not measured; it is computed, by inverting a model of how the data were made. That inversion is unstable, because the measuring process smooths away detail that noise then swamps, and the algorithms of this volume are the ways to make it stable, fast and honest about what the data can tell.

The volume has eight chapters. In this edition one entry is written, [phase retrieval](/phase-retrieval/) in Chapter 46.7. The other chapters have no written entries yet; their pages say what they will cover and point to the written entries elsewhere in the handbook, mostly in Volumes 12, 15 and 28, that a reader can use now.

## Why imaging gets a volume of its own

A few ideas run through the whole subject:

- **Ill-posedness.** A problem is well posed when its solution exists, is unique and depends continuously on the data. Most inverse problems fail the last condition: small noise in the data gives large errors in the naive inverse. The singular value decomposition shows why, and every method in the volume is a way of damping the small singular values.
- **Prior knowledge.** What the data cannot fix must come from what is known about the object: smoothness, sparsity in some basis, positivity, a support, or a probability distribution. The choice of prior, and of how strongly to weight it, decides the result as much as the data do.
- **Physics in the forward model.** Each modality has its own forward operator, the Radon transform for CT, a Fourier transform for MRI, the wave equation for ultrasound and seismic imaging. Fast algorithms come from the structure of that operator, most often from the fast Fourier transform.
- **Proved for a model, measured on images.** Exact recovery theorems, such as those of compressed sensing, hold under stated conditions on the measurements. Iterative methods for nonconvex problems, including the phase retrieval iterations, often have no convergence guarantee, and learned reconstructions are judged by benchmark measurements.

## The chapters

**Chapter 46.1, Regularization of inverse problems**, will cover ill-posedness, truncated SVD and Tikhonov regularization, iterative regularization by early stopping, rules for choosing the regularization parameter, convergence rates and the Bayesian formulation. Meanwhile read the [singular value decomposition](/singular-value-decomposition/) and [Tikhonov regularization](/tikhonov-regularization/) in Volume 12.

**Chapter 46.2, Variational, sparse and learned reconstruction**, will cover variational regularization, primal-dual and Bregman algorithms, sparse recovery theory, dictionary learning and learned priors. Meanwhile read [compressed sensing](/compressed-sensing/) in Volume 28 and the [proximal gradient method](/proximal-gradient-method/) in Volume 15.

**Chapter 46.3, Tomographic reconstruction**, will cover the Radon transform and the Fourier slice theorem, filtered back-projection and cone-beam formulas, algebraic and statistical methods, and reconstruction from incomplete data. Meanwhile read the [Kaczmarz method](/kaczmarz-method/) in Volume 12 and [expectation maximization](/expectation-maximization/) in Volume 25.

**Chapter 46.4, MRI reconstruction**, will cover k-space, non-Cartesian sampling, parallel imaging with several coils, compressed sensing MRI and low-rank dynamic imaging. Meanwhile read the [nonuniform FFT](/nonuniform-fft/) in Volume 11 and the [conjugate gradient method](/conjugate-gradient-method/) in Volume 12.

**Chapter 46.5, Ultrasound and radar imaging**, will cover pulse-echo image formation, adaptive beamforming, synthetic aperture radar algorithms, interferometry with phase unwrapping, and speckle. Meanwhile read [delay-and-sum beamforming](/delay-and-sum-beamforming/) and the [matched filter](/matched-filter/) in Volume 28.

**Chapter 46.6, Seismic imaging**, will cover seismic processing and velocity analysis, migration from Kirchhoff to reverse time migration, traveltime tomography and full waveform inversion. Meanwhile read the [wave equation](/wave-equation/) and the [eikonal equation](/eikonal-equation/) in Volume 12.

**Chapter 46.7, Phase retrieval and coherent imaging**, has one written entry, [phase retrieval](/phase-retrieval/): recovering a signal from the magnitude of its Fourier transform. The entry shows that the magnitude carries exactly the autocorrelation, counts the ambiguities in one dimension, states the uniqueness result for two and more dimensions, and compares spectral factorization, the iterations of Gerchberg, Saxton and Fienup, and the methods with guarantees for random measurements. The separate entries on the iterations, on crystallography and on ptychography and holography are still to be written.

**Chapter 46.8, Deconvolution, super-resolution and astronomical imaging**, will cover the diffraction limit, deconvolution and blind deconvolution, radio interferometry and CLEAN, imaging through turbulence, and super-resolution by localization and by sparse recovery. Meanwhile read [Richardson-Lucy deconvolution](/richardson-lucy-deconvolution/) and the [Wiener filter](/wiener-filter/) in Volume 28.

## How to read this volume

For now, read [phase retrieval](/phase-retrieval/) as the one complete entry, and use the opening pages of the other chapters as reading lists. A reader new to inverse problems should start from the meanwhile list of Chapter 46.1, since the singular value decomposition and Tikhonov regularization explain the instability that every later chapter has to deal with. Chapters 46.3 to 46.6 are about particular modalities and can be read in any order once 46.1 and 46.2 are familiar. Each entry stands on its own; its facts box lists what it needs, by entry number.

## What you need first

Linear algebra at the level of the [singular value decomposition](/singular-value-decomposition/) and the [least squares problem](/least-squares-problem/) of Volume 12, and the [discrete Fourier transform](/discrete-fourier-transform/) and [fast Fourier transform](/fast-fourier-transform/) of Volume 11. For phase retrieval you also need the [autocorrelation](/autocorrelation/) and the [z-transform](/z-transform/) of Volume 28. The later chapters use convex optimization from Volume 15, such as [gradient descent](/gradient-descent/) and the [proximal operator](/proximal-operator/), and basic probability for the noise models.

## The exercises

Chapter 46.7 ends with exercises in three bands. Exercises marked ◦ check that you read the entries closely; you should be able to do them in a few minutes. Exercises marked • ask you to use an idea in a new place; each takes some thought, and some need a short program. Exercises marked ★ are harder; some are results from research papers. Hints for many exercises are in the appendix *Hints to the exercises* at the end of the volume.

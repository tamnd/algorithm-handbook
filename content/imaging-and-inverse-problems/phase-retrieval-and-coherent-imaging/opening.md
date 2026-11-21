An X-ray detector, an electron camera and the sensor behind a microscope objective count photons. They
record the intensity of the wave that reaches them, and the intensity is the squared magnitude of the
complex field. The phase, which carries much of the information about the object, is lost. When the
detector sits in the far field of the object, the field there is the Fourier transform of the object, and
the task is to recover a signal from the magnitude of its Fourier transform. This is phase retrieval. It
decides how protein structures are solved from crystal diffraction, how a nanocrystal is imaged with X-rays
without any lens, how a hologram is turned back into an image, and how a microscope can image transparent
cells.

The magnitude fixes the [autocorrelation](/autocorrelation/) of the signal and nothing else. The signals of length $n$
that share one autocorrelation fall into as many as $2^{n-2}$ classes that no trivial change connects, so in
one dimension the problem is badly posed. In two or more dimensions a generic image is
unique up to a global phase, a shift and the conjugate reversal, provided the magnitude is sampled finely
enough. Uniqueness is not an algorithm, though. The algorithms used in practice alternate between two
constraint sets, one of which is not convex. Some never increase their error and stagnate; the better ones
escape stagnation but have no general convergence proof. Methods with proofs exist only for random
measurement models.

## What the chapter covers

1. **The problem and its ambiguities.** [Phase retrieval](/phase-retrieval/) itself, with the
   one-dimensional zero-flipping argument, and the [ambiguities](/phase-retrieval-ambiguities/) that no data
   of this kind can remove.
2. **When the magnitude determines the signal.** [Oversampling](/oversampling-in-phase-retrieval/), the
   [Bruck-Sodin uniqueness theorem](/bruck-sodin-uniqueness/) for images of two or more dimensions, and the
   [complement property](/complement-property/) for general linear measurements.
3. **Iterative projection methods.** The [Gerchberg-Saxton algorithm](/gerchberg-saxton-algorithm/),
   [error reduction](/error-reduction-algorithm/), [hybrid input-output](/hybrid-input-output/), the
   [difference map](/difference-map/), [RAAR](/raar/) and [shrinkwrap](/shrinkwrap/).
4. **The crystallographic phase problem.** The [phase problem of crystals](/crystallographic-phase-problem/),
   the [Patterson function](/patterson-function/), [direct methods](/direct-methods-crystallography/) and
   [charge flipping](/charge-flipping/).
5. **Propagation and holography.** The [angular spectrum method](/angular-spectrum-method/),
   [digital holography](/digital-holography-reconstruction/), the [twin image problem](/twin-image-problem/)
   and the [transport of intensity equation](/transport-of-intensity-equation/).
6. **Coherent diffraction imaging and ptychography.** [Coherent diffraction imaging](/coherent-diffraction-imaging/),
   [ptychography](/ptychography/), [ePIE](/epie/) and [Fourier ptychography](/fourier-ptychography/).
7. **Methods with guarantees.** [PhaseLift](/phaselift/), [spectral initialization](/spectral-initialization/)
   and [Wirtinger flow](/wirtinger-flow/), which are proved to work for Gaussian measurement vectors.

## A first reading

Read these in order:

1. [Phase retrieval](/phase-retrieval/)
2. [Phase retrieval ambiguities](/phase-retrieval-ambiguities/)
3. [Oversampling in phase retrieval](/oversampling-in-phase-retrieval/)
4. [Gerchberg-Saxton algorithm](/gerchberg-saxton-algorithm/)
5. [Error reduction algorithm](/error-reduction-algorithm/)
6. [Hybrid input-output](/hybrid-input-output/)
7. [Crystallographic phase problem](/crystallographic-phase-problem/)
8. [Patterson function](/patterson-function/)
9. [Angular spectrum method](/angular-spectrum-method/)
10. [Coherent diffraction imaging](/coherent-diffraction-imaging/)
11. [Ptychography](/ptychography/)

The uniqueness theorems of the second group, the refinements of HIO (the difference map, RAAR and
shrinkwrap), direct methods and charge flipping, and the last group can wait. Read the last group when the
measurements are designed rather than given by physics, as in coded illumination.

## Before you start

The chapter uses the [discrete Fourier transform](/discrete-fourier-transform/), the
[fast Fourier transform](/fast-fourier-transform/) and the [convolution theorem](/convolution-theorem/)
from Volume 11, and the [z-transform](/z-transform/), [autocorrelation](/autocorrelation/) and the
[Nyquist rate](/nyquist-rate/) from Volume 28. The uniqueness group needs
[irreducible polynomials](/irreducible-polynomial/) (Volume 11). The methods with guarantees use
[semidefinite programming](/semidefinite-programming/) and [gradient descent](/gradient-descent/) from
Volume 15 and [power iteration](/power-iteration/) from Volume 12. The propagation group needs the
[wave equation](/wave-equation/) (Volume 12) at the level of plane waves. Some feeling for complex numbers
and for Fourier optics helps throughout; the [optical transfer function](/optical-transfer-function/) and the
[Abbe diffraction limit](/abbe-diffraction-limit/), from the chapter on deconvolution and astronomical
imaging, are used by Fourier ptychography.

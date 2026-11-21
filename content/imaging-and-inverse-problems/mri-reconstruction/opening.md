An MRI scanner does not take a picture. It puts the body in a strong field, tips the magnetization of the
hydrogen nuclei with a radio pulse, and listens to the weak signal they send back while gradient fields make the
precession frequency depend on position. The [signal equation](/mri-signal-equation/) shows that each sample is
the Fourier transform of the image at one point of [k-space](/k-space/), the point set by the integral of the
gradients up to that time. Reconstruction is therefore the inversion of a Fourier transform. With a full
Cartesian grid it is one inverse FFT. Each sample costs scan time, though, and the patient has to hold still.
So most of this chapter is about getting the image from fewer samples than the grid asks for.

There are three ways to need fewer samples, and the chapter treats each. The image may be nearly real, so its
k-space is nearly Hermitian and a little more than half of it is enough. The scanner may have several receive
coils, each seeing the body through a different sensitivity, so the coils together supply the information that
skipped lines would have carried. Or the image may be sparse in some transform, or a series of frames may be of
low rank, so that random undersampling can be undone by an optimization. Each way comes with a price, and the
entries state it: the [g-factor](/g-factor/) of parallel imaging is at least 1 and divides the SNR on top of the
$\sqrt R$ loss, while the guarantees of compressed sensing hold for models of the sampling, not for a given scan.

## What the chapter covers

The chapter is in 8 groups, read in order.

1. **Physics and the forward model.** The [Bloch equations](/bloch-equations/), the signal equation, k-space,
   [trajectories](/k-space-trajectory/) and the [reconstruction problem](/mri-reconstruction-problem/).
2. **Non-Cartesian scans.** [Density compensation](/density-compensation/),
   [conjugate phase reconstruction](/conjugate-phase-reconstruction/) and [PROPELLER](/propeller-mri/).
3. **Partial Fourier.** The [theory](/partial-fourier-reconstruction/), the
   [homodyne method](/homodyne-reconstruction/) and [POCS](/pocs-partial-fourier/).
4. **Coil maps and image-domain parallel imaging.** [Coil sensitivity maps](/coil-sensitivity-map/),
   [root sum of squares](/root-sum-of-squares-coil-combination/), [SENSE](/sense/), the g-factor and
   [CG-SENSE](/cg-sense/).
5. **Parallel imaging in k-space.** [GRAPPA](/grappa/), [SPIRiT](/spirit/), [ESPIRiT](/espirit/) and
   [slice-GRAPPA](/slice-grappa/).
6. **Sparsity and low rank.** [Compressed sensing MRI](/compressed-sensing-mri/),
   [variable density sampling](/variable-density-sampling/) and [LORAKS](/loraks/).
7. **Dynamic imaging.** [k-t BLAST](/k-t-blast/), the [partial separability model](/partial-separability-model/)
   and [low rank plus sparse](/low-rank-plus-sparse-mri/).
8. **Quantitative and learned methods.**
   [Quantitative susceptibility mapping](/quantitative-susceptibility-mapping/),
   [MR fingerprinting](/mr-fingerprinting/) and the [variational network](/variational-network-mri/).

## A first reading

For a short path, read these ten entries in order:

1. [Bloch equations](/bloch-equations/)
2. [MRI signal equation](/mri-signal-equation/)
3. [k-space](/k-space/)
4. [MRI reconstruction problem](/mri-reconstruction-problem/)
5. [Partial Fourier reconstruction](/partial-fourier-reconstruction/)
6. [Coil sensitivity map](/coil-sensitivity-map/)
7. [SENSE](/sense/)
8. [g-factor](/g-factor/)
9. [GRAPPA](/grappa/)
10. [Compressed sensing MRI](/compressed-sensing-mri/)

The first four set up the Fourier model and its sampling rules. Partial Fourier is the simplest use of prior
knowledge. SENSE, the g-factor and GRAPPA are the two views of parallel imaging and its noise cost, and
compressed sensing is the third way of saving samples.

## Before you start

The chapter uses the [discrete Fourier transform](/discrete-fourier-transform/), the
[fast Fourier transform](/fast-fourier-transform/) and the [nonuniform FFT](/nonuniform-fft/) (Volume 11), and
the [sampling theorem](/sampling-theorem/) and [aliasing](/aliasing/) (Volume 28). The Bloch equations are an
[initial value problem](/ode-initial-value-problem/) (Volume 12). Parallel imaging is
[least squares](/least-squares-problem/) solved directly or by the
[conjugate gradient method](/conjugate-gradient-method/) (Volume 12), and ESPIRiT and the low-rank models use the
[singular value decomposition](/singular-value-decomposition/) (Volume 12). The sparse methods need
[compressed sensing](/compressed-sensing/) (Volume 28) and the [proximal operator](/proximal-operator/) with
[FISTA](/fista/) (Volume 15). From chapter 46.1 you need the [inverse problem](/inverse-problem/) and its
[forward operator](/forward-operator/). The [Fourier slice theorem](/fourier-slice-theorem/) of chapter 46.3 explains radial sampling.

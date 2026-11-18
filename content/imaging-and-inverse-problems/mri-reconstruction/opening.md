A magnetic resonance scanner does not take a picture. It measures, one line at a time, samples of the spatial Fourier transform of the magnetization in the body, a space the field calls k-space. When k-space is sampled fully on a Cartesian grid, the image is one inverse FFT away. The difficulty is time: each line takes milliseconds, a full scan takes minutes, and patients move and breathe. Almost every reconstruction method in this chapter exists to make an image from fewer samples than the Nyquist rate asks for, or from samples off the grid.

Three ideas do most of the work. Parallel imaging uses several receiver coils, each with its own spatial sensitivity, so that the coils together supply information the skipped lines would have given; SENSE solves for the image in image space and GRAPPA fills in the missing k-space lines. Compressed sensing MRI samples k-space at random, more densely near the centre, and recovers a sparse image by convex optimization. Low-rank and model-based methods exploit the structure of dynamic and quantitative scans. The theory guarantees recovery only under conditions the scanner can approximate, so image quality is in the end judged by measurement.

## What the chapter will cover

The entries of this chapter are being written. They will cover:

1. **The measurement.** The Bloch equations, the MRI signal equation, k-space, k-space trajectories and the MRI reconstruction problem.
2. **Non-Cartesian and partial data.** Density compensation, conjugate phase reconstruction, PROPELLER, partial Fourier reconstruction, homodyne reconstruction and POCS partial Fourier reconstruction.
3. **Parallel imaging.** Coil sensitivity maps, root sum of squares coil combination, SENSE and the geometry factor, CG-SENSE, GRAPPA, slice-GRAPPA, SPIRiT and ESPIRiT.
4. **Sparsity and low rank.** Compressed sensing MRI, variable density sampling, k-t BLAST, the partial separability model, low-rank plus sparse dynamic MRI and LORAKS.
5. **Quantitative and learned methods.** MR fingerprinting, quantitative susceptibility mapping and variational networks.

## What to read meanwhile

The [fast Fourier transform](/fast-fourier-transform/) and, for spiral and radial trajectories, the [nonuniform FFT](/nonuniform-fft/) are in Volume 11. CG-SENSE is the [conjugate gradient method](/conjugate-gradient-method/) of Volume 12 applied to the normal equations of the coil model. Compressed sensing MRI rests on [compressed sensing](/compressed-sensing/), the [restricted isometry property](/restricted-isometry-property/), the [discrete wavelet transform](/discrete-wavelet-transform/) and [total variation denoising](/total-variation-denoising/) in Volume 28, solved by [FISTA](/fista/) or [ADMM](/admm/) from Volume 15. Low-rank dynamic imaging uses the [singular value decomposition](/singular-value-decomposition/) of Volume 12 and the ideas of [matrix completion](/matrix-completion/) in Volume 35.

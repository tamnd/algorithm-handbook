## What to remember

- **The data are Fourier samples.** The [signal equation](/mri-signal-equation/) makes each sample the transform of the image at $k(t) = \bar\gamma \int_0^t G$. The sample spacing sets the field of view, $1/\Delta k$, and the extent sets the pixel size, $1/(2k_{\max})$. Skipping lines by a factor $R$ folds the image $R$ times.
- **Non-Cartesian data need weights.** A radial scan needs about $\pi n/2$ spokes for an $n$-sample diameter. [Density compensation](/density-compensation/) by the iteration $w \leftarrow w/(Cw)$ works well in practice but has no convergence guarantee, and the weighted adjoint is [conjugate phase reconstruction](/conjugate-phase-reconstruction/).
- **Partial Fourier saves at most a little under half.** With a known phase, $n/2 + 1$ samples of a line are the least that can work. The least squares variance is $\sigma^2 (n - k_0 - 1)/n$ per pixel. [Homodyne](/homodyne-reconstruction/) is exact for $\rho \ge 0$ with a constant phase, and the [POCS](/pocs-partial-fourier/) error halves at each step in that case. For a general smooth phase the error is measured, not bounded.
- **Parallel imaging pays a g-factor.** [SENSE](/sense/) needs $R \le c$ coils and divides the SNR by $g\sqrt R$ with $g \ge 1$. The g-factor depends on the coil geometry and grows fast as $R$ nears $c$: for four ring coils the entry measured a mean of 1.34 at $R = 2$ and 67.3 at $R = 4$.
- **CG-SENSE is conjugate gradients on the normal equations.** Its error in the energy norm does not increase, and in exact arithmetic it stops after at most as many steps as there are unknowns. In practice a few dozen steps are used.
- **GRAPPA and SPIRiT work in k-space.** [GRAPPA](/grappa/) is exact when the maps have a small k-space support that the kernel spans, and an approximation for real coils. [ESPIRiT](/espirit/) turns the calibration kernel into maps, with the true map an eigenvector of eigenvalue 1 under its model.
- **Sparse and low-rank models need incoherent sampling.** [Compressed sensing MRI](/compressed-sensing-mri/) samples at random with a [variable density](/variable-density-sampling/), and $p_k \propto \mu_k^2$ minimizes the bound $K^2 = \max_k \mu_k^2/p_k$. The guarantees are for random models of the sampling. The [partial separability model](/partial-separability-model/) of rank $L$ has $L(N + T - L)$ degrees of freedom instead of $NT$.
- **Quantitative maps are inverse problems too.** The dipole kernel of [QSM](/quantitative-susceptibility-mapping/) is zero on a cone at $54.7°$, so a single orientation needs regularization; Tikhonov gains at most $1/(2\sqrt\alpha)$ on the noise. [MR fingerprinting](/mr-fingerprinting/) matching is maximum likelihood on the dictionary grid. The [variational network](/variational-network-mri/) has measured results and no theorem for the trained network.

## The methods

| method | data | what is proved |
|---|---|---|
| inverse FFT | full Cartesian grid | exact |
| homodyne, POCS | a little over half of each line | exact for a real image with constant phase |
| SENSE | Cartesian, $R \le c$, known maps | least squares unfolding; noise $g\sqrt R$ times the full scan, $g \ge 1$ |
| CG-SENSE | any trajectory, known maps | energy-norm error does not increase |
| GRAPPA | Cartesian with a calibration block | exact for maps with small k-space support |
| SPIRiT | any sampling with a calibration block | consistency residual does not increase |
| compressed sensing | random variable density | recovery bounds for random sampling models |
| L+S | dynamic, undersampled | convergence to a minimizer of the cost for small steps; no recovery theorem |
| variational network | training pairs | none; quality is measured |

: What the entries prove for each method. The bounds for compressed sensing are about models of the sampling, not about one scan.

## Choosing a method

On a Cartesian scan with a fully sampled center, GRAPPA is the usual default because it needs no maps; use
SENSE when good maps are at hand, for example from ESPIRiT or a prescan, and keep $R$ well below the number of
coils in the direction of undersampling. Add partial Fourier when the phase is smooth and a little more time
must be saved. For radial and spiral scans, grid with density compensation for a quick image, and use CG-SENSE
or SPIRiT for an accurate one. When the image or the series has structure, compressed sensing, LORAKS or a
low-rank model can go further than parallel imaging alone, at the price of parameters that are tuned by hand and
results that must be checked on known data. Learned methods need training data from the same kind of scan.

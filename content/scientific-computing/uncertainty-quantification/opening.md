A model of groundwater flow needs the permeability of the rock at every point, and nobody knows it: a few boreholes give samples, and the rest is a guess with error bars. So the predicted path of a contaminant is uncertain too, and a single run, however accurate, does not say how uncertain. Uncertainty quantification treats the unknown inputs as random, propagates them through the model, and reports the distribution of the output: its mean, its spread, the probability of failure, and which inputs matter.

Plain Monte Carlo does this with an error that falls like $1/\sqrt{N}$ in the number of runs, whatever the dimension, but each run may be an hour of computing. The methods of this chapter need fewer or cheaper runs. Multilevel Monte Carlo takes most samples on coarse grids and few on fine ones, and under conditions on how fast the level variances decay its cost for accuracy $\varepsilon$ is of the order of $\varepsilon^{-2}$. Polynomial chaos expands the output in orthogonal polynomials of the inputs and converges fast for smooth dependence on few inputs. Reduced-order models replace the full simulation by a small one fitted to a few full runs.

## What the chapter will cover

The entries of this chapter are being written. They will cover:

1. **Forward propagation.** Forward uncertainty propagation and random fields, multilevel Monte Carlo and its complexity theorem, multifidelity Monte Carlo, the first-order reliability method and subset simulation for rare failures.
2. **Polynomial chaos and collocation.** Polynomial chaos expansions and generalized polynomial chaos, the stochastic Galerkin and stochastic collocation methods, non-intrusive spectral projection, regression-based and sparse polynomial chaos.
3. **Sensitivity analysis.** The Hoeffding-Sobol decomposition and Sobol indices, the Saltelli sampling scheme, the Morris method, the Fourier amplitude sensitivity test and active subspaces.
4. **Calibration and inverse problems.** The well-posedness of Bayesian inverse problems and the Kennedy-O'Hagan calibration model.
5. **Reduced-order models.** POD-Galerkin models, the reduced basis method with the weak greedy algorithm, empirical and discrete empirical interpolation, proper generalized decomposition and operator inference.

## What to read meanwhile

The sampling methods are written: [Monte Carlo integration](/monte-carlo-integration/), [quasi-Monte Carlo integration](/quasi-monte-carlo-integration/) with the [Sobol sequence](/sobol-sequence/) and [Gaussian quadrature](/gaussian-quadrature/) in Volume 12, and [Latin hypercube sampling](/latin-hypercube-sampling/), [importance sampling](/importance-sampling/) and [Metropolis-Hastings](/metropolis-hastings/) in Volume 17. Surrogate models are [Gaussian processes](/gaussian-process/) in Volume 25 and [kriging](/kriging/) in Volume 12.

For model reduction, [principal component analysis](/principal-component-analysis/) (Volume 25) is the proper orthogonal decomposition under another name, and [dynamic mode decomposition](/dynamic-mode-decomposition/) is in Volume 36. Gradients of outputs with respect to many inputs come from [adjoint sensitivity analysis](/adjoint-sensitivity-analysis/) in Volume 32, and [approximate Bayesian computation](/approximate-bayesian-computation/) in Volume 33 handles inverse problems whose likelihood cannot be evaluated.

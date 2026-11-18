Differential privacy is a promise about an algorithm, not about a data set. A randomized algorithm is ε-differentially private if adding or removing one person's record changes the probability of any output by at most a factor of e^ε. Whatever an attacker knows beforehand, the output tells them about the same about any one person whether or not that person took part. The definition was given by Dwork, McSherry, Nissim and Smith in 2006, after Dinur and Nissim showed that answering too many counting queries too accurately lets anyone rebuild the data. It is now used by census bureaus and in the software of large companies.

The basic tool is noise scaled to sensitivity: if one record can change a count by at most 1, adding Laplace noise of scale 1/ε makes the count ε-private. The harder questions are about many queries. Privacy loss adds up under composition, and much of the subject is careful accounting of that loss, and the design of mechanisms that answer many queries with less noise than answering each one alone.

## What the chapter will cover

The entries of this chapter are being written. They will cover:

1. **The definition.** Pure and approximate differential privacy, sensitivity, group privacy, closure under post-processing and the privacy loss random variable.
2. **Basic mechanisms.** Randomized response, the Laplace, geometric, Gaussian and discrete Gaussian mechanisms, the exponential mechanism, report noisy max and the sparse vector technique.
3. **Composition and accounting.** Basic, advanced, optimal and parallel composition, Rényi differential privacy, zero-concentrated and Gaussian differential privacy, the moments accountant, numerical accounting and amplification by subsampling and by shuffling.
4. **Beyond global sensitivity.** Smooth sensitivity, propose-test-release and subsample-and-aggregate.
5. **Query release and learning.** The binary tree mechanism for counters, the matrix mechanism, MWEM, SmallDB, output and objective perturbation, DP-SGD and PATE.
6. **Local privacy and lower bounds.** RAPPOR, optimized local hashing, geo-indistinguishability, the Dinur-Nissim reconstruction attack and the packing and fingerprinting lower bounds.

## What to read meanwhile

The accuracy of every mechanism is a tail bound: read the [Chernoff bound](/chernoff-bound/) and [Hoeffding's inequality](/hoeffding-inequality/) in Volume 1. MWEM is the [multiplicative weights update](/multiplicative-weights-update/) method of Volume 19 run against a private choice of query, and DP-SGD is [stochastic gradient descent](/stochastic-gradient-descent/) of Volume 15 with clipped gradients and added noise. Local frequency estimation uses the same hashing as the [count-min sketch](/count-min-sketch/) of Volume 19. Rényi and approximate privacy are divergences between output distributions, close to the [Kullback-Leibler divergence](/kullback-leibler-divergence/) of Volume 33. The discrete Gaussian is sampled as in [Gaussian sampling over lattices](/gaussian-sampling-over-lattices/) in Volume 23, and the cryptographic route to privacy is [secure multiparty computation](/secure-multiparty-computation/), also in Volume 23.

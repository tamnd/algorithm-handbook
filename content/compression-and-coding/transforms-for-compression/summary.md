## What to remember

- Delta encoding, run-length encoding and the Burrows-Wheeler transform are exact and take $\Theta(n)$ time each way. A string $L$ with one end marker is a Burrows-Wheeler transform if and only if its LF mapping is a single cycle. For geometric run lengths, $P(\ell) = (1-\theta)\theta^{\ell}$, the best prefix code is Golomb with the smallest $m$ such that $\theta^m + \theta^{m+1} \le 1$.
- After a Burrows-Wheeler transform, [move-to-front](/move-to-front-transform/) outputs small numbers because the rank of a symbol is less than the distance to its last occurrence.
- For a Gaussian source of variance $\sigma^2$ under squared error, $R(D) = \frac12 \log_2(\sigma^2/D)$, so each bit is worth $6.02$ dB. At high rate a uniform [scalar quantizer](/scalar-quantization/) with step $\Delta$ has error about $\Delta^2/12$, and with an ideal entropy coder it is $\frac12 \log_2(\pi e/6) \approx 0.254$ bit, or $1.53$ dB, above $R(D)$. [Vector quantization](/vector-quantization/) can gain at most these $1.53$ dB in space filling.
- An [orthogonal transform](/orthogonal-transform/) keeps the energy, $\|Tx\| = \|x\|$, so the squared error of the coefficients is that of the signal. Under the high-rate model the [coding gain](/transform-coding/) is $G = \frac{\frac1N \sum_k \sigma_k^2}{(\prod_k \sigma_k^2)^{1/N}}$. By Hadamard's inequality the [Karhunen-Loève transform](/karhunen-loeve-transform/) has the largest gain of all orthogonal transforms, $(\frac1N \operatorname{tr} R) / (\det R)^{1/N}$. For some non-Gaussian sources other transforms do better.
- The optimal rates are $b_k = b + \frac12 \log_2 \bigl(\sigma_k^2 / (\prod_j \sigma_j^2)^{1/N}\bigr)$. When some $b_k$ would be negative, reverse water-filling gives the coefficients with $\sigma_k^2 < \theta$ no bits and the others the error $\theta$.
- The orthonormal [DCT-II](/discrete-cosine-transform/) is close to the KLT of a first-order autoregressive source with high $\rho$. Lee's algorithm needs 12 multiplications and 29 additions for $N = 8$.
- A two-channel bank with the alias-cancelling synthesis has [perfect reconstruction](/perfect-reconstruction/) if and only if its product filter satisfies $P(z) - P(-z) = 2c\,z^{-l}$, with $l$ odd. With real symmetric FIR filters, only the Haar bank is orthogonal. The [MDCT](/modified-discrete-cosine-transform/) maps $2N$ samples to $N$ coefficients and is exact with a symmetric window with $w[n]^2 + w[n+N]^2 = 1$.
- Stopping a [bit-plane](/bit-plane-coding/) stream after plane $p$ is a dead-zone quantizer with step $2^p$, and the midpoint decoder errs by at most $2^{p-1}$ on each significant value. [SPIHT](/spiht/) and [JPEG 2000](/jpeg-2000/) rely on this.

| Method | What it does | Exact or lossy | Time |
|---|---|---|---|
| [Delta encoding](/delta-encoding/) | differences of neighbours | exact | $\Theta(n)$ |
| [Run-length encoding](/run-length-encoding/) | symbol and run length | exact | $\Theta(n)$ |
| [Burrows-Wheeler transform](/burrows-wheeler-transform/) and [inverse](/inverse-burrows-wheeler-transform/) | sorts rotations; LF walk | exact | $\Theta(n)$ each way |
| Move-to-front | ranks in a recency list | exact | $\Theta(n\sigma)$ worst, $O(n + S)$ for output sum $S$ |
| [Bijective BWT](/bijective-burrows-wheeler-transform/) | sorts rotations of Lyndon factors | exact | $O(n^2 \log n)$ simple, $\Theta(n)$ linear method |
| KLT | eigenvectors of the covariance | exact transform | $\Theta(MN^2 + rN^2)$ design, $\Theta(N^2)$ per block |
| DCT-II | fixed cosine basis | exact transform | $\Theta(N \log N)$ |
| MDCT | lapped, $2N \to N$ | exact after overlap-add | $\Theta((L + N)\log N)$ |
| Baseline [JPEG](/jpeg-compression/) | $8 \times 8$ DCT, table quantizer, Huffman | lossy | $\Theta(n)$ |
| SPIHT | wavelet, significance trees | lossy, embedded | $\Theta(np)$ |
| JPEG 2000 transform stages | RCT, 5/3 or 9/7 lifting, dead zone | lossless with 5/3, lossy with 9/7 | $\Theta(np)$ |

: Transforms of the chapter. An image has $n$ pixels and $p$ bit planes; the KLT design uses $M$ training blocks and $r$ Jacobi rotations. For the first-order autoregressive source with $\rho = 0.95$ and $N = 8$, the coding gains are 7.667 (8.846 dB) for the KLT, 7.631 (8.826 dB) for the DCT, 6.232 for the Walsh-Hadamard transform and 5.738 for the unitary DFT.

## Choosing a method

For slowly changing integers, such as timestamps, use delta encoding with zigzag and a variable-length integer code. For a binary source with long runs, use a Golomb or Rice code on the run lengths. For text, use the Burrows-Wheeler transform, move-to-front and an entropy coder, as bzip2 does.

Use the DCT on blocks of smooth images and video residuals: it needs no training, and on a highly correlated source it is within a few hundredths of a decibel of the KLT. Use the KLT only for a known, stable covariance far from that model. Use the MDCT for audio, where block edges would be heard. Use wavelets with bit-plane coding, as in JPEG 2000, when the stream must be cut at any rate or decode losslessly. Use vector quantization for small blocks at low rates, where a scalar quantizer cannot spend a fraction of a bit per value.

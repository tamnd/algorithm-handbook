1. ◦ A log stores the timestamps $1000, 1003, 1001, 1001, 1130$. Apply [delta encoding](/delta-encoding/) with the first value kept as it is, map each value with zigzag ($v \mapsto 2v$ for $v \ge 0$ and $v \mapsto -2v - 1$ for $v < 0$), and write the results as LEB128 bytes, seven bits per byte with the low group first. Give the bytes in hexadecimal and compare the total with five 16-bit integers.

2. ◦ The first stage of bzip2 replaces each run of 4 to 255 equal bytes by four copies of the byte and one count byte from 0 to 251 for the rest of the run. Apply it to `aaaaaaaaaabbbbc`. How many bytes come out, and why does the run `bbbb` cost one byte more than it would without this stage?

3. ◦ The runs of a binary source have the geometric law $P(\ell) = (1-\theta)\theta^\ell$ with $\theta = 0.8$. Find the Golomb parameter $m$ of [run-length compression](/run-length-compression/), the smallest $m$ with $\theta^m + \theta^{m+1} \le 1$. With a unary quotient ended by a 0 and a truncated binary remainder, how many bits do the runs $0, 4, 7$ cost in all?

4. ◦ Compute the [Burrows-Wheeler transform](/burrows-wheeler-transform/) of `mississippi$`, where `$` is the smallest symbol. Then apply [move-to-front](/move-to-front-transform/) with the initial list $(\$, i, m, p, s)$ and ranks from 0.

5. ◦ Compute the orthonormal 4-point [DCT-II](/discrete-cosine-transform/) of $x = (1, 2, 3, 4)$ to four digits. Check that the energy is kept, and give the share of the energy in the first coefficient and in the first two.

6. ◦ Code $v = (-6, 0, 3, 9)$ with [bit-plane coding](/bit-plane-coding/), four magnitude planes and one sign bit for each nonzero value. How many bits does the full stream have? The decoder puts each significant value at the midpoint of its interval and each insignificant one at 0. Give the decoded vector and the squared error after planes 3, 2, 1 and 0.

7. ◦ In a baseline [JPEG](/jpeg-compression/) block, the 63 AC coefficients in [zigzag](/zigzag-scan/) order are $5, 0, 0, -3$, then eighteen zeros, then $1$, then zeros to the end. List the run/size symbols of the block. The DC values of four blocks in a row are $50, 47, 47, 60$, with the predictor starting at 0. Give the differences and their size categories.

8. ◦ Apply one level of the reversible 5/3 lifting of [JPEG 2000](/jpeg-2000/), with symmetric extension at the ends, to $x = (4, 6, 9, 9, 8, 2)$: $d[n] = x[2n+1] - \lfloor (x[2n] + x[2n+2])/2 \rfloor$ and $s[n] = x[2n] + \lfloor (d[n-1] + d[n] + 2)/4 \rfloor$. Then apply the reversible color transform to the 8-bit pixel $(R, G, B) = (200, 100, 50)$ after the level shift, and recover $G$ from the result.

9. ◦ [SPIHT](/spiht/) codes a $64 \times 64$ image after three levels of a wavelet transform. How many descendants does a coefficient of a detail band at the coarsest level have? How many does a root in the low band have, if it has offspring? Check that the trees, together with the low band, account for all 4096 coefficients.

10. ◦ An [MDCT](/modified-discrete-cosine-transform/) with $N = 256$ codes $L = 1000$ samples, with frames that start before the signal and end after it. How many frames and coefficients are there? Write the sine window $w[n] = \sin(\pi(n + \frac12)/(2N))$ for $N = 2$ and check the Princen-Bradley condition.

11. • A fair binary source is coded in blocks of three bits: the encoder sends one bit, the majority of the block, and the decoder repeats it three times. Find the rate and the Hamming distortion per source bit. Compare with time-sharing between sending a bit exactly and guessing it, at the same rate, and with the [rate-distortion](/lossy-compression/) bound $R(D) = 1 - h(D)$.

12. • A Gaussian source with variance 1 is quantized by a uniform [scalar quantizer](/scalar-quantization/) with step $\Delta = 0.1$, followed by an ideal entropy coder. Use the high-rate approximations to give the rate and the mean squared error. How far above $R(D)$ is the rate, in bits and in decibels?

13. • Run the generalized Lloyd algorithm of [vector quantization](/vector-quantization/) in one dimension on the training set $\{0, 2, 3, 10\}$, for two codewords, starting from a split of the one-codeword solution. Give the final codewords and the mean squared error per value. Is it the best 2-level quantizer for this set?

14. • Four coefficients have variances $16, 4, 1, \frac14$. Under the high-rate model of [transform coding](/transform-coding/), give the optimal allocation at a mean rate of 2 bits and the coding gain in decibels. What goes wrong with the same formula at a mean rate of 1 bit? Find the reverse water-filling allocation and the mean distortion at that rate.

15. • Find the [Karhunen-Loève transform](/karhunen-loeve-transform/) of a source with covariance
$$R = \begin{pmatrix} 2 & 1 & 0 \\ 1 & 2 & 1 \\ 0 & 1 & 2 \end{pmatrix}.$$
Give the share of the energy in the first coefficient and the coding gain in decibels.

16. • Show that the Golomb parameter of exercise 3 is $m = \lceil \log(1 + \theta) / (-\log \theta) \rceil$, and find $m$ for $\theta = 0.95$.

17. • Let $w$ be a primitive word, one that is not a power of a shorter word, and use the transform that sorts all rotations of a word, with no end marker. Show that the transform of $w^k$ repeats each symbol of the transform of $w$ $k$ times in place. Check it on $ababab$ and $abcabc$.

18. • Apply the three [locality recodings](/locality-recoding/) to `mississippi` with the order $A = (i, m, p, s)$ and the virtual prefix: the intervals, the recency ranks and the inversion frequencies. Check that each rank plus one is at most the matching interval.

19. • Compute the [bijective Burrows-Wheeler transform](/bijective-burrows-wheeler-transform/) of each of the eight words of length 3 over $\{a, b\}$. Which words does it fix, and which does it swap?

20. • Check that the Daubechies 4-tap filter $h_0 = (1 + \sqrt3, 3 + \sqrt3, 3 - \sqrt3, 1 - \sqrt3)/(4\sqrt2)$ has unit norm, is orthogonal to its shift by two, and has $\sum_n h_0[n] = \sqrt2$. For its highpass filter $h_1[n] = (-1)^n h_0[3 - n]$, show that $\sum_n h_1[n] = 0$ and $\sum_n n\,h_1[n] = 0$.

21. • Use the error bound of baseline JPEG, mean squared error at most $(B + 4)^2/64$ with $B = \frac12 \sqrt{\sum Q^2}$, to give the guaranteed PSNR for 8-bit samples when all 64 steps are 2. What is the largest equal integer step that guarantees at least 40 dB?

22. • Two JPEG 2000 code blocks have the truncation points (rate, distortion) $A$: $(0, 100), (10, 40), (20, 30), (30, 5), (40, 4)$ and $B$: $(0, 50), (10, 20), (20, 10), (30, 8)$. Which point is not on the lower convex hull? With post-compression rate-distortion optimization, choose the truncation points for a total budget of 50, and then of 40, and give the total distortion.

23. ★ Sample a Brownian motion at times $1, 2, \ldots, N$, so that $R_{ij} = \min(i, j)$. Show that the eigenvalues are $\lambda_k = 1 / \bigl(4 \sin^2 \frac{(2k-1)\pi}{2(2N+1)}\bigr)$ for $k = 1, \ldots, N$, and that the coding gain of the KLT is exactly $(N + 1)/2$. Check both for $N = 3$.

24. ★ For the first-order autoregressive source with unit variance and correlation $\rho$, show that the errors of the best linear prediction of each sample from the samples before it, in the same block, are uncorrelated, with variances $1, 1 - \rho^2, \ldots, 1 - \rho^2$. Deduce that the KLT coding gain is $(1 - \rho^2)^{-(N-1)/N}$ and evaluate it for $N = 8$ and $\rho = 0.9$.

25. ★ Let $v[n] = x[2n]$ and $v[N - 1 - n] = x[2n + 1]$ for $0 \le n < N/2$, and let $V$ be the DFT of $v$. Prove that the unnormalized DCT-II, $X[k] = \sum_n x[n] \cos \frac{\pi (2n+1) k}{2N}$, satisfies $X[k] = \operatorname{Re}\bigl(e^{-i\pi k/(2N)} V[k]\bigr)$.

26. ★ A real FIR filter $h$ of even length $L$, with $h[0] \ne 0$, is symmetric, $h[n] = h[L - 1 - n]$, and orthonormal to its even shifts, $\sum_n h[n] h[n + 2k] = \delta_k$. Prove that $h$ has exactly two nonzero taps, $h[0] = h[L - 1] = \pm 1/\sqrt2$, so that a [perfect reconstruction](/perfect-reconstruction/) bank that is orthogonal and has symmetric FIR filters is the Haar bank, up to delays.

27. ★ Prove that a string $L$ over $\Sigma \cup \{\$\}$ with exactly one $\$$ is the transform of some text ending in $\$$ if and only if its LF mapping is a single cycle, the condition used by the [inverse transform](/inverse-burrows-wheeler-transform/). Which of the six orderings of $a, b, \$$ are valid?

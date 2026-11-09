## What to remember

- The $n$-th **roots of unity** $\omega_n^k$, with $\omega_n = e^{-2\pi i/n}$, satisfy three lemmas. Cancellation: $\omega_{dn}^{dk} = \omega_n^k$. Halving: the squares of the $n$-th roots are the $(n/2)$-th roots, each twice. Summation: $\sum_{j=0}^{n-1} \omega_n^{jk} = 0$ unless $n$ divides $k$. The FFT uses the first two; the inverse uses the third.
- The **DFT** $X_k = \sum_j x_j \omega_n^{jk}$ evaluates the polynomial with coefficients $x_j$ at the $n$-th roots of unity. Its matrix $F_n$ satisfies $F_n^{-1} = \frac{1}{n}\overline{F_n}$, so the inverse is a DFT with $\omega_n^{-1}$ and a factor $1/n$. [Parseval's theorem](/parseval-theorem/) reads $\sum |X_k|^2 = n \sum |x_j|^2$.
- The **radix-2 FFT** splits by even and odd index and joins the halves with $n/2$ butterflies $(a, b) \mapsto (a + \omega b,\ a - \omega b)$. It uses $\frac{n}{2}\lg n$ multiplications and $n \lg n$ additions, against $n(n-1)$ of each for the direct sum. The [iterative FFT](/iterative-fft/) does the same work in place after a [bit-reversal permutation](/bit-reversal-permutation/).
- The **convolution theorem**: the DFT of a cyclic convolution is the pointwise product of the DFTs. To multiply polynomials with $m$ and $\ell$ coefficients, pad to a power of two $N \ge m + \ell - 1$ and use three FFTs, for $O(N \log N)$ operations.
- The **number-theoretic transform** runs the same algorithm in $\mathbb{Z}/p$ when $2^k \mid p - 1$. It is exact, but each result must be smaller than $p$, or several primes are used and joined by the Chinese remainder theorem.
- **Any length** has an $O(n \log n)$ algorithm: mixed radix for smooth $n$, [Rader's algorithm](/rader-fft/) for prime $n$ (a cyclic convolution of length $n - 1$), and [Bluestein's algorithm](/bluestein-fft/) for every $n$ (a convolution of power-of-two length $M \ge 2n - 1$).
- The **Walsh-Hadamard transform** is the Fourier transform of the group $(\mathbb{Z}/2)^k$. Its fast form uses $n \lg n$ additions and no multiplications, and it turns XOR convolution into a pointwise product.

## Fast transforms side by side

| Algorithm | Length | Cost | Arithmetic |
|---|---|---|---|
| Direct [DFT](/discrete-fourier-transform/) | any $n$ | $n(n-1)$ multiplications, $n(n-1)$ additions | complex |
| [Radix-2 FFT](/fast-fourier-transform/) | $2^k$ | $\frac{n}{2}\lg n$ multiplications, $n \lg n$ additions | complex, error $O(u \log n)$ |
| [Split-radix FFT](/split-radix-fft/) | $2^k$ | $4n \lg n - 6n + 8$ real operations | complex |
| [Mixed-radix FFT](/mixed-radix-fft/) | $n = r_1 \cdots r_t$ | $\Theta(n \sum r_i)$ | complex |
| [Bluestein's algorithm](/bluestein-fft/) | any $n$ | three FFTs of length $M < 4n$ | complex |
| [Number-theoretic transform](/number-theoretic-transform/) | $2^k \mid p - 1$ | $\frac{n}{2}\lg n$ multiplications mod $p$ | exact, mod $p$ |
| [Goertzel algorithm](/goertzel-algorithm/) | any $n$ | $n + 1$ multiplications, $2n + 1$ additions per coefficient | real multiplier in the loop |
| [Fast Walsh-Hadamard transform](/fast-walsh-hadamard-transform/) | $2^k$ | $n \lg n$ additions | exact on integers |
| [Haar wavelet transform](/haar-wavelet-transform/) | $2^k$ | $2n - 2$ additions, $2n - 2$ multiplications | real |

: The main fast transforms. Counts are for complex data where the transform is complex; $u$ is the unit roundoff. The Goertzel algorithm wins over a full FFT only when fewer than about $\lg n$ coefficients are wanted.

## Choosing a method

- To multiply polynomials or big integers with integer coefficients, use the NTT with one prime if the results fit, or two or three primes and the Chinese remainder theorem if not. Use a floating-point FFT when the coefficients are small and some rounding is acceptable.
- For a power-of-two length, use an iterative radix-2 or split-radix FFT. For other lengths, use mixed radix when $n$ has small factors, and Bluestein's algorithm otherwise.
- For real input, use the [real-valued FFT](/real-valued-fft/), which costs one complex FFT of length $n/2$.
- For one or two frequencies, as in tone detection, use the Goertzel algorithm.
- For XOR, AND or OR convolution over bit masks, use the fast Walsh-Hadamard transform or the [sum over subsets](/sum-over-subsets/) transform, not the FFT.
- For samples that are not equally spaced, use the [nonuniform FFT](/nonuniform-fft/), not an exact algorithm.

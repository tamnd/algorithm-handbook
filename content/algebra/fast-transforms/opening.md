Multiply two polynomials of degree $n$ the schoolbook way and you do about $n^2$ multiplications. Evaluate both at $2n$ points, multiply the values, and interpolate, and the product needs only $2n$ multiplications in the middle; the cost moves into the evaluation and the interpolation. If the points are the complex roots of unity, both steps are a discrete Fourier transform, and the fast Fourier transform does each one in $O(n \log n)$ operations. That one idea speeds up polynomial and integer multiplication, signal filtering, image compression and string matching.

This chapter is about that transform and its relatives. The core is short: a few lemmas about roots of unity, the radix-2 FFT, and the convolution theorem. The rest of the chapter extends it to every length, to real data, to finite fields, to a few coefficients at a time, and to transforms with other kernels.

## What the chapter covers

The chapter is in eight groups, read in order.

1. **Roots of unity and the DFT.** The [roots of unity](/roots-of-unity/), the cancellation, halving and summation lemmas, the [discrete Fourier transform](/discrete-fourier-transform/) as a matrix and as polynomial evaluation, its inverse, and [Parseval's theorem](/parseval-theorem/).
2. **The fast Fourier transform.** The [butterfly](/butterfly-operation/), the [radix-2 FFT](/fast-fourier-transform/), and its [iterative](/iterative-fft/) form, which works in place after a [bit-reversal permutation](/bit-reversal-permutation/). It uses exactly $\frac{n}{2}\lg n$ multiplications and $n \lg n$ additions.
3. **Convolution.** The [convolution theorem](/convolution-theorem/), the algorithm that multiplies polynomials by three FFTs, and the [number-theoretic transform](/number-theoretic-transform/), which does the same modulo a prime such as $998244353 = 119 \cdot 2^{23} + 1$, with no rounding.
4. **FFTs for every length.** [Mixed radix](/mixed-radix-fft/), the prime-factor algorithm, [Rader's algorithm](/rader-fft/) for prime $n$, and [Bluestein's algorithm](/bluestein-fft/), which handles any $n$ with a convolution of power-of-two length.
5. **Fewer operations, more dimensions.** [Split radix](/split-radix-fft/), which needs $4n\lg n - 6n + 8$ real operations, the [FFT of real data](/real-valued-fft/) at half the cost, and the [multidimensional FFT](/multidimensional-fft/).
6. **A few coefficients, or points off the grid.** The [Goertzel algorithm](/goertzel-algorithm/), the [sparse Fourier transform](/sparse-fourier-transform/), and the [nonuniform FFT](/nonuniform-fft/).
7. **Real transforms.** The [discrete sine transform](/discrete-sine-transform/), the [fast DCT](/fast-dct/), and the Hartley transform with its fast algorithm.
8. **Walsh-Hadamard and wavelets.** The [fast Walsh-Hadamard transform](/fast-walsh-hadamard-transform/), which needs only additions, and the [Haar](/haar-wavelet-transform/) and [fast wavelet](/fast-wavelet-transform/) transforms, which run in linear time.

## A first reading

For a first reading, take these eleven entries in order: [roots of unity](/roots-of-unity/), [the summation lemma](/fft-summation-lemma/), [the discrete Fourier transform](/discrete-fourier-transform/), [the halving lemma](/fft-halving-lemma/), [the butterfly](/butterfly-operation/), [the fast Fourier transform](/fast-fourier-transform/), [the inverse FFT](/inverse-fft/), [convolution](/convolution/), [the convolution theorem](/convolution-theorem/), [convolution via the FFT](/convolution-via-fft/) and [the number-theoretic transform](/number-theoretic-transform/). Add the [fast Walsh-Hadamard transform](/fast-walsh-hadamard-transform/) if you meet XOR convolutions in contest problems. After these, the iterative FFT and the bit-reversal permutation are what you need to write a fast implementation; the other groups can be read in any order.

One warning on signs. This book writes $\omega_n = e^{-2\pi i/n}$, so the DFT is $X_k = \sum_j x_j \omega_n^{jk}$ and the inverse carries $\omega_n^{-1}$ and a factor $1/n$. Some textbooks, among them the one by Cormen, Leiserson, Rivest and Stein, use $e^{+2\pi i/n}$ in the forward transform. Every theorem holds with either sign, but formulas taken from two sources must not be mixed.

## Before you start

You need [asymptotic notation](/asymptotic-notation/), the [geometric series](/geometric-series/), and the [divide-and-conquer paradigm](/divide-and-conquer-paradigm/) with the [master theorem](/master-theorem/) from the early volumes. Complex numbers in polar form are assumed. For the finite-field transforms you need the [primitive root](/primitive-root/), [modular exponentiation](/modular-exponentiation/) and the [Chinese remainder theorem](/chinese-remainder-theorem/) from Volume 10. [Polynomial multiplication](/polynomial-multiplication/) from Chapter 11.2 is the main application, and the [Kronecker product](/kronecker-product/) from Chapter 11.4 describes the Walsh-Hadamard matrix and the multidimensional transform. The roadmap below lists every entry of the chapter with its kind and level, and the figure after it shows which entries lean on which.

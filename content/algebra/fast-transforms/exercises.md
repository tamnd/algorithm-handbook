1. ◦ Compute the [DFT](/discrete-fourier-transform/) of $(1, 0, -1, 0)$ with $\omega_4 = -i$. Check [Parseval's theorem](/parseval-theorem/) on the result.

2. ◦ Write out the [bit-reversal permutation](/bit-reversal-permutation/) for $n = 16$. How many indices are fixed, and how many swaps does an in-place reordering make?

3. ◦ Compute the linear [convolution](/convolution/) of $(1, 1, 1)$ and $(1, 2, 3)$, and their cyclic convolution of length 3. What is the smallest power-of-two FFT length that gives the linear convolution with no wraparound?

4. ◦ Multiply $314$ by $27$ by convolving the digit sequences, lowest digit first, and then carrying. Show the sequence before the carries.

5. ◦ The prime $257$ has $256 = 2^8$ as $p - 1$. What is the longest power-of-two length of a [number-theoretic transform](/number-theoretic-transform/) modulo 257? Show that $2$ has order 16 modulo 257. Why is an NTT of length 16 with $\omega = 2$ cheap to compute?

6. ◦ Run the [fast Walsh-Hadamard transform](/fast-walsh-hadamard-transform/) on $(1, 0, 1, 0, 0, 0, 0, 1)$. Show the vector after each of the three stages and count the additions and subtractions.

7. ◦ Run the [Haar wavelet transform](/haar-wavelet-transform/) with scale $c = 1/2$ on $(2, 4, 8, 6)$. Then run it with $c = 1/\sqrt 2$ and check that the sum of squares does not change.

8. ◦ For $n = 1024$, how many complex multiplications and additions does the radix-2 [fast Fourier transform](/fast-fourier-transform/) make? How many does the direct sum make? How many of the butterflies have twiddle factor 1?

9. • Show that for real input $x$ the DFT satisfies $X_{n-k} = \overline{X_k}$, and that $X_0$ and, for even $n$, $X_{n/2}$ are real. How many real numbers does $X$ hold, counted this way?

10. • Let $x$ and $y$ be real sequences of length $n$ and let $Z$ be the DFT of $z = x + iy$. Show that $X_k = (Z_k + \overline{Z_{n-k}})/2$ and $Y_k = (Z_k - \overline{Z_{n-k}})/(2i)$, with indices modulo $n$. So one complex FFT gives two real ones.

11. • Let $y_j = x_{(j - 1) \bmod n}$, a cyclic shift. Show that $Y_k = \omega_n^k X_k$. What does the DFT do to a cyclic shift by $s$ places?

12. • Prove that exactly $n - 1$ of the $\frac{n}{2}\lg n$ butterflies of the radix-2 FFT have [twiddle factor](/twiddle-factor/) $1$. How many nontrivial complex multiplications are left?

13. • Show that $F_n^2 = nP$, where $F_n$ is the [DFT matrix](/dft-matrix/) and $P$ is the permutation $j \mapsto -j \bmod n$. Deduce $F_n^4 = n^2 I$, and that every eigenvalue of $F_n$ is one of $\sqrt n$, $-\sqrt n$, $i\sqrt n$, $-i\sqrt n$.

14. • Given sets $A, B \subseteq \{0, \ldots, m\}$, show how to count, for every $s$, the pairs $(a, b) \in A \times B$ with $a + b = s$, in $O(m \log m)$ time. Do it by hand for $A = \{1, 2, 5\}$ and $B = \{0, 3, 4\}$.

15. • The XOR convolution of $a$ and $b$, of length $n = 2^k$, is $c_t = \sum_{i \oplus j = t} a_i b_j$. Show that the [Walsh-Hadamard transform](/walsh-hadamard-transform/) maps it to the pointwise product of the transforms, and give an $O(n \log n)$ algorithm for it.

16. • Prove that the Walsh-Hadamard matrix $H_n = H_2^{\otimes k}$ satisfies $H_n^2 = nI$, using the mixed-product rule of the [Kronecker product](/kronecker-product/).

17. • You must multiply two polynomials of degree less than $10^5$ whose coefficients are integers in $[0, 1000)$, exactly, with NTTs. Is the prime $998244353$ enough on its own? If not, how many primes of about that size do you need, and what transform length?

18. • Check the identity $2jk = j^2 + k^2 - (k - j)^2$ and use it to write a DFT of length $n$ as a convolution, as [Bluestein's algorithm](/bluestein-fft/) does. What power-of-two length does it use for $n = 1000$? For $n = 1025$? Show that the length is always less than $4n$.

19. • [Rader's algorithm](/rader-fft/) for $n = 7$ uses the primitive root $g = 3$. In what order does it read $x_1, \ldots, x_6$, and in what order does it produce $X_1, \ldots, X_6$? What convolution is left, and how long is it?

20. • Show that any circuit of fan-in-2 gates that computes the DFT of length $n$ has depth at least $\lg n$. Conclude that the [parallel FFT circuit](/parallel-fft-circuit/) has optimal depth.

21. ★ *Matching with wildcards.* A text $t$ of length $n$ and a pattern $p$ of length $m$ use letters coded as positive integers, and $0$ for a wildcard that matches anything. Find every position where the pattern matches in $O(n \log n)$ time.

22. ★ Let $V$ be a subspace of $(\mathbb{Z}/2)^k$ and $f$ its indicator vector. Show that the Walsh-Hadamard transform of $f$ is $|V|$ times the indicator of the orthogonal complement $V^\perp$.

23. ★ Let $n = n_1 n_2$ with $\gcd(n_1, n_2) = 1$. Show that $j = (n_2 j_1 + n_1 j_2) \bmod n$ is a bijection from pairs $(j_1, j_2)$ to $\{0, \ldots, n - 1\}$, and that with the output index $k$ given by $k \equiv k_1 \pmod{n_1}$, $k \equiv k_2 \pmod{n_2}$, the DFT of length $n$ becomes a two-dimensional DFT of size $n_1 \times n_2$ with no twiddle factors. This is the [prime-factor algorithm](/chinese-remainder-theorem-fft/).

24. ★ A filter of length $\ell$ is applied to a signal of length $m \gg \ell$. A single FFT convolution costs $O(m \log m)$. Show how to cut the signal into blocks and get $O(m \log \ell)$ instead.

25. ★ *The chirp z-transform.* Given a polynomial $f$ of degree less than $n$ and nonzero $a$ and $z$, evaluate $f$ at the $m$ points $a z^k$, $0 \le k < m$, in $O((n + m)\log(n + m))$ operations. Use $jk = \binom{j+k}{2} - \binom{j}{2} - \binom{k}{2}$, which avoids the square root of $z$ that Bluestein's identity needs.

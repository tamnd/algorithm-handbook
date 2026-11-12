1. The deltas are $1000, 3, -2, 0, 129$ and the zigzag values $2000, 6, 3, 0, 258$. The bytes are `D0 0F 06 03 00 82 02`: two for 2000, one each for 6, 3 and 0, and two for 258. That is 7 bytes against 10.

3. $m = 2$ gives $0.64 + 0.512 > 1$ and $m = 3$ gives $0.512 + 0.4096 \le 1$, so $m = 3$. The remainder 0 takes 1 bit and the remainders 1 and 2 take 2 bits. The runs cost $1 + 1$, $2 + 2$ and $3 + 2$ bits, 11 in all. The mean code length is about 3.639 bits per run, against an entropy of $h(0.8)/0.2 \approx 3.610$.

4. The transform is `ipssm$pissii`. The ranks are $1, 3, 4, 0, 4, 4, 3, 4, 4, 0, 1, 0$.

6. The stream has $4 \cdot 4 + 3 = 19$ bits. After plane 3: $(0, 0, 0, 12)$, error 54. After plane 2: $(-6, 0, 0, 10)$, error 10. After plane 1: $(-7, 0, 3, 9)$, error 1. After plane 0 the vector is exact.

8. The low band is $(4, 9, 7)$ and the high band $(0, 1, -6)$; the last low value uses $\lfloor -3/4 \rfloor = -1$. The shifted pixel is $(72, -28, -78)$, which gives $Y = \lfloor -62/4 \rfloor = -16$, $U = B - G = -50$ and $V = R - G = 100$. Then $G = Y - \lfloor (U + V)/4 \rfloor = -16 - 12 = -28$, which is $100$ after the shift back.

11. The rate is $1/3$ bit per source bit. A block is decoded wrongly in one bit with probability $6/8$, so $D = 1/4$. Time-sharing at rate $1/3$ gives $D = \frac23 \cdot \frac12 = 1/3$. The bound needs only $1 - h(1/4) \approx 0.189$ bit for $D = 1/4$, and at rate $1/3$ it allows $D \approx 0.174$, where $h(D) = 2/3$.

12. The rate is about $h(X) - \log_2 \Delta = \frac12 \log_2(2\pi e) + \log_2 10 \approx 5.369$ bits and $D = \Delta^2/12 \approx 8.33 \cdot 10^{-4}$. Then $R(D) = \frac12 \log_2(1/D) \approx 5.114$, so the gap is $\frac12 \log_2(\pi e/6) \approx 0.254$ bit, or $1.53$ dB, at any small step.

14. The geometric mean is 2 and the arithmetic mean $5.3125$, so the gain is $2.656$, or $4.24$ dB, and at 2 bits $b = (3.5, 2.5, 1.5, 0.5)$. At 1 bit the formula gives $-0.5$ for the last coefficient. Drop it and share 4 bits among the first three: $\theta^3 = 16 \cdot 4 \cdot 1 / 2^8$, so $\theta = 2^{-2/3} \approx 0.630$, $b \approx (2.333, 1.333, 0.333, 0)$ and $D = (3\theta + \frac14)/4 \approx 0.535$.

18. The intervals are $2, 2, 6, 1, 3, 2, 1, 3, 11, 1, 3$ and the ranks $1, 1, 3, 0, 1, 1, 0, 1, 3, 0, 1$. The inversion frequencies are $i$: $1, 2, 2, 2$; $m$: $0$; $p$: $4, 0$; $s$: $0, 0, 0, 0$.

22. On block $A$ the slopes are $6, 1, 2.5, 0.1$; they must fall, so $(20, 30)$ is off the hull, and the hull slopes are $6, 1.75, 0.1$. Block $B$ has $3, 1, 0.2$. Take the steps in order of slope: at budget 50, $A$ stops at 30 and $B$ at 20, with $D = 5 + 10 = 15$. At budget 40, $A$ stops at 30 and $B$ at 10, with $D = 25$.

23. $R = LL^{\mathsf T}$ with $L$ the lower triangular matrix of ones, so $\det R = 1$, and $R^{-1}$ is tridiagonal with $2$ on the diagonal, $-1$ next to it, and $1$ in the last diagonal place. Try eigenvectors $\sin(n\phi)$ and use the last row to fix $\phi = (2k-1)\pi/(2N+1)$. The gain is $\operatorname{tr}(R)/N = (N+1)/2$ over $(\det R)^{1/N} = 1$. For $N = 3$: $\lambda \approx 5.0489, 0.6431, 0.3080$, product 1 and gain 2.

24. The best predictor of $x_t$ from the past is $\rho x_{t-1}$, and its error is uncorrelated with all earlier samples, so with each other. This is the factorization $R = L D L^{\mathsf T}$ with $L$ unit lower triangular and $D = \operatorname{diag}(1, 1-\rho^2, \ldots)$, so $\det R = (1-\rho^2)^{N-1}$, the product of the KLT eigenvalues. The arithmetic mean of the variances is 1. For $N = 8$ and $\rho = 0.9$ the gain is $0.19^{-7/8} \approx 4.2765$.

25. Write $\cos \frac{\pi(2n+1)k}{2N} = \operatorname{Re} e^{-i\pi(2n+1)k/(2N)}$ and split the sum into even and odd $n$. The odd samples $x[2n+1]$ sit at $v[N-1-n]$, and with $m = N - 1 - n$ the angle $\pi(4n+3)k/(2N)$ becomes $2\pi k - \pi(4m+1)k/(2N)$, so its cosine equals that of the even case at index $m$. Both halves then sum $v[m] \cos \frac{\pi(4m+1)k}{2N} = \operatorname{Re}\bigl(e^{-i\pi k/(2N)} v[m] e^{-2\pi i mk/N}\bigr)$.

26. By symmetry the autocorrelation at shift $s$ equals $(h * h)[L - 1 - s]$, so $h * h$ is zero at every odd index except $L - 1$, where it is 1. Split $H(z) = E(z^2) + z^{-1} O(z^2)$. The odd part of $H(z)^2$ is $2z^{-1} E(z^2) O(z^2)$, so $E O$ is a single monomial, and then both $E$ and $O$ are monomials. Symmetry pairs the even tap with the odd one at $L - 1 - n$, and $h[0] \ne 0$ places them at $0$ and $L - 1$.

27. If $L$ is a transform of $T$, LF steps from the row of each rotation to the row of the rotation one place earlier, so it walks through all $n$ rotations in one cycle. Conversely, if LF is one cycle, the walk from the row of `$` reads a text $T$ backwards; show that the sorted rotations of $T$ have last column $L$, using the fact that LF keeps the order of equal symbols. Only `ab$`, the transform of `ba$`, and `b$a`, the transform of `ab$`, are valid. There are only two texts, and distinct texts have distinct transforms.

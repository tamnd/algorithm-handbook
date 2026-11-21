1. ◦ A direct-sequence link spreads 15 kbit/s over a chip rate of 3.84 Mchip/s. Give the
[processing gain](/processing-gain/) as a ratio and in dB. The receiver needs $E_b/J_0 = 7$ dB and has
2 dB of implementation loss. What jamming margin is left?

2. ◦ An [FDMA](/frequency-division-multiple-access/) system has 1.25 MHz of spectrum, a guard band of 25 kHz
at each edge and channels of 30 kHz. How many channels fit?

3. ◦ A [TDMA](/time-division-multiple-access/) frame has 16 slots of 625 µs on a channel of 1 Mbit/s. Each
slot loses 30 µs of guard time and 40 µs of preamble. Give the slot efficiency and the net rate of a user
who owns one slot per frame.

4. ◦ A [frequency-hopping](/frequency-hopping-spread-spectrum/) network has $q = 50$ channels, and each user
hops independently and uniformly. Give the probability that a given hop of one user collides with at
least one other user when $K = 4$ users are active. What is the largest $K$ that keeps this probability at
or below 10%?

5. ◦ How many distinct [m-sequences](/maximal-length-sequence/) are there of degree $n = 5$, 6, 7 and 10?

6. ◦ Users ask for [OVSF codes](/ovsf-codes/) with spreading factors 2, 4, 8 and 8. Show that the request
can be met, and give one assignment with the index $k$ of each code $C_{SF,k}$ (indices from 0, with
$C_{2N,2k} = (C_{N,k}, C_{N,k})$ and $C_{2N,2k+1} = (C_{N,k}, -C_{N,k})$). Which codes of spreading factor 8
are blocked by the code $C_{4,1}$?

7. ◦ Write the phase exponents $u\,n(n+1)/2 \bmod 7$ of the [Zadoff-Chu sequence](/zadoff-chu-sequence/)
of length $N = 7$ with root $u = 3$, for $n = 0, \ldots, 6$. What is the magnitude of its periodic
cross-correlation with the root $u = 1$ sequence, at any lag?

8. ◦ Two synchronous users have the correlation $\rho = 0.6$. Give the asymptotic efficiency of the
[decorrelating detector](/decorrelating-detector/) and the loss in dB against a single user.

9. ◦ A multipath channel has three resolvable paths with energies 0.49, 0.25 and 0.25. How much energy, in
dB, does a [rake receiver](/rake-receiver/) with one finger lose against one with three? With two?

10. • Generate one period of the m-sequence of $x^5 + x^2 + 1$, with the recurrence
$s_{k+5} = s_{k+2} \oplus s_k$ and the start $10000$. Check the balance property, count the runs of each
length (cyclically), and check that the periodic autocorrelation of the $\pm 1$ form is $-1$ at every
nonzero shift.

11. • Give the size of the [Gold](/gold-sequences/) family of degree $n = 7$, its largest correlation
$t(7)$ and the three correlation values. Compare $t(7)$ with the sequence form of the
[Welch bound](/welch-bound/), $\theta_{\max} \ge N\sqrt{(M - 1)/(MN - 1)}$.

12. • For $n = 10$ ($N = 1023$), compare the small [Kasami](/kasami-sequences/) set, the Gold family and the
large Kasami set: the number of sequences, $\theta_{\max}$, and the ratio of $\theta_{\max}$ to the Welch
bound for that number of sequences.

13. • Two users have the correlation $\rho = 0.2$ and the matched filter is used. At what ratio
$A_2/A_1$, in dB, does the efficiency of user 1 fall to zero? At what ratio is it one half? Use the formula
of the [near-far problem](/near-far-problem/).

14. • Three synchronous users have equal correlations $R_{kj} = \rho$ for $k \ne j$. Find $(R^{-1})_{kk}$
and the near-far resistance of the decorrelator as functions of $\rho$, and evaluate them at
$\rho = 1/4$. For what range of $\rho$ is $R$ positive definite?

15. • Two users have $\rho = 0.5$, equal amplitudes $A_1 = A_2 = 1$ and noise variance $\sigma^2 = 0.25$ at
the matched filter outputs (noise covariance $\sigma^2 R$). Compute the output SINR of user 1 for the
matched filter, the [decorrelator](/decorrelating-detector/) and the
[MMSE detector](/mmse-multiuser-detector/), and compare them with the single-user SNR.

16. • Three users have $A = (3, 1, 1.5)$ and all correlations $\rho = 0.3$. In which order does
[SIC](/successive-interference-cancellation/) decide them, and does the noiseless condition for correct
decisions hold at each step? Repeat with $A = (1, 1, 1)$ and $\rho = 0.6$, and find a bit vector for which
the first decision is wrong without noise.

17. • A [serial search](/serial-search-code-acquisition/) has $q = 2046$ cells (half-chip steps over a
code of 1023 chips), $P_d = 0.95$, $P_{fa} = 0.001$ and a false alarm penalty of $K = 1000$ dwells. Compute
the mean acquisition time in dwells, and compare it with the case without false alarms.

18. • A software GPS receiver searches $F = 21$ Doppler bins with blocks of $N = 2048$ samples. Count the
complex multiply-adds of the direct correlations and of the
[parallel code phase search](/parallel-code-phase-search/), with radix-2 FFTs of $(N/2)\log_2 N$
multiplications and the code transform computed once.

19. • Two users share a Gaussian [MAC](/mac-capacity-region/) with $\mathrm{SNR}_1 = 20$ and
$\mathrm{SNR}_2 = 5$. Give the three bounds of the region and its two corner points, with the decoding
order of each. Is the symmetric rate pair on the sum-rate face achievable?

20. • In a downlink, the strong user has $\gamma_1 = 50$ and the weak user $\gamma_2 = 5$. With
[NOMA](/non-orthogonal-multiple-access/), the strong user gets the power fraction $a = 0.1$ and cancels the
weak user's signal first. Compute both rates. Then find the time-sharing split that gives the weak user the
same rate, and the rate of the strong user under it.

21. • In a frame of [coded slotted ALOHA](/coded-slotted-aloha/) with four slots, user A sends copies in
slots 1 and 2, user B in slots 2 and 3, user C in slot 3, and user D in slots 1 and 4. Run the peeling
decoder and give the order in which users are resolved. What would plain slotted ALOHA have decoded from
the same slots, if each user had sent only its first copy?

22. ★ The six diagonals of a regular icosahedron are the lines through the vertices
$(0, \pm 1, \pm\varphi)$, $(\pm 1, \pm\varphi, 0)$, $(\pm\varphi, 0, \pm 1)$ with $\varphi = (1 + \sqrt5)/2$.
Show that their unit vectors meet the [Welch bound](/welch-bound/) for $K = 6$ and $N = 3$ with equality,
and check that they form a tight frame.

23. ★ Let $s_1, \ldots, s_K$ be unit vectors in $\mathbb R^N$ with Gram matrix $R$. Prove that the total
squared correlation $\sum_{k,j}(s_k^\top s_j)^2$ is at least $K^2/N$, and that equality holds exactly when
$SS^\top = (K/N)I$. Derive the Welch bound from this inequality.

24. ★ Apply the reduction of the [NP-hardness proof](/multiuser-detection-np-hardness/) to the cycle on
four vertices with unit weights: build $R$, check that it is positive definite, and find the value of
$b^\top Rb$ for cuts of size 0, 2 and 4. Which bit vectors minimize it?

25. ★ The Jacobi form of [parallel interference cancellation](/parallel-interference-cancellation/)
converges if and only if all eigenvalues of $R$ lie in $(0, 2)$. For $K$ users with equal correlations
$\rho \ge 0$, find the eigenvalues of $R$ and the range of $\rho$ for which the iteration converges. Evaluate
the limit for $K = 5$.

26. ★ Coded slotted ALOHA with degree distribution $\Lambda(x) = \sum_d \Lambda_d x^d$ is analysed by the
recursion $p \leftarrow 1 - \exp(-G\,\Lambda'(p))$, with $\Lambda_1 = 0$. Show that decoding cannot start to converge near
$p = 0$ unless $G < 1/(2\Lambda_2)$, and that for $\Lambda(x) = x^2$ this gives the exact threshold
$G^* = 1/2$.

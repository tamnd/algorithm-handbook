1. ◦ Run [von Neumann debiasing](/von-neumann-debiasing/) on the 14 flips $x = 01100011101001$, with the pair $01$ giving 0 and $10$ giving 1. What is the output? For a coin with $\Pr[1] = 0.2$, how many output bits do 100 flips give in expectation, and how many flips does one output bit cost on average?

2. ◦ A source on $\{0,1\}^3$ gives one string with probability $1/2$, two strings with probability $1/8$ each and the other four with probability $1/16$ each. Compute its [min-entropy](/min-entropy/) $H_\infty$, its collision entropy $H_2$ and its Shannon entropy $H$, and check that $H_\infty \le H_2 \le H$.

3. ◦ Apply the [method of conditional expectations](/method-of-conditional-expectations/) to MAX-CUT on the graph with vertices 0 to 5 and the nine edges 03, 04, 05, 12, 14, 23, 25, 35, 45. Fix the vertices in the order 0 to 5, put each one on the side opposite to most of its fixed neighbours, and break ties toward side 0. Which cut do you get? Compare its size with $m/2$ and with the maximum cut.

4. ◦ Write out the Hadamard sample space for $m = 2$: the seed is $y \in \{0,1\}^2$, and $X_a = \langle a, y \rangle \bmod 2$ for $a = 01, 10, 11$. List its four points, check that the three bits are unbiased and pairwise independent, and give a test on the three bits that shows they are not 3-wise independent. Compare the size of the space with the lower bound for [$k$-wise independence](/k-wise-independence/) with $k = 2$.

5. ◦ Run the powering construction of the [small-bias generator](/small-bias-generator/) with $m = 3$, the modulus $t^3 + t + 1$, the seed $x = 011$ (that is, $t + 1$) and $y = 101$, for the $n = 7$ output bits $\langle x^i, y \rangle$, $i = 0, \ldots, 6$. What bound does the construction give on the bias of a nonempty parity of these bits?

6. ◦ A source of $n = 256$ bits has min-entropy $k = 128$. By the [leftover hash lemma](/leftover-hash-lemma/), how many bits within statistical distance $2^{-40}$ of uniform can a universal hash function extract? How many seed bits does the Toeplitz construction need for this output length?

7. ◦ An algorithm with one-sided error uses 100 random bits and errs with probability at most $1/2$. Take a 16-regular graph on $2^{100}$ vertices with $\lambda \le 1/2$. Using the bound $\mu(\mu + \lambda(1 - \mu))^{t-1}$ of the [expander walk sampler](/expander-walk-sampler/), find the smallest number $t$ of walk vertices that brings the error to at most $2^{-10}$, and count the random bits. How many random bits do independent runs need for the same error?

8. ◦ A [Santha-Vazirani source](/santha-vazirani-source/) with $\delta = 1/3$ gives each bit the value 1 with conditional probability between $1/3$ and $2/3$, whatever the earlier bits. Give a lower bound on the min-entropy of 10 such bits. What bias can the source force on any fixed function $f : \{0,1\}^{10} \to \{0,1\}$? If two independent such sources are combined by XOR bit by bit, what is the parameter $\delta'$ of the result?

9. • Show that a uniformly random assignment satisfies $3m/4$ of $m$ clauses with two distinct literals in expectation. Then run the method of conditional expectations on the six clauses $(x_1 \lor x_2)$, $(\lnot x_1 \lor x_3)$, $(\lnot x_2 \lor \lnot x_3)$, $(x_1 \lor \lnot x_3)$, $(\lnot x_1 \lor \lnot x_2)$, $(x_2 \lor x_3)$, fixing $x_1, x_2, x_3$ in this order and breaking ties toward true. Give each conditional expectation. How many clauses does the result satisfy?

10. • An algorithm with one-sided error uses 64 random bits and accepts each yes-input with probability at least $1/2$. Its runs use the pairwise independent strings $r_i = a + \alpha_i b$ over $\mathrm{GF}(2^{64})$, where $a, b$ are random and $\alpha_1, \ldots, \alpha_t$ are distinct field elements. Use Chebyshev's inequality, as in [limited independence](/limited-independence/), to bound the probability that all $t$ runs reject a yes-input. How many runs bring this to at most $0.001$, and how many random bits do they use? Compare with independent runs.

11. • Let $G(a, b) = (a, b, a \oplus b)$ and let the test $D(y)$ accept when $y_3 = y_1 \oplus y_2$. Compute the advantage of $D$ against $G$ and the acceptance probabilities $p_0, p_1, p_2, p_3$ of the hybrids of [computational indistinguishability](/computational-indistinguishability/), where hybrid $i$ takes its first $i$ bits from $G$ and the rest uniformly. Which bit position does the predictor of [Yao's theorem](/yao-next-bit-unpredictability/) use, and how often is it right?

12. • Take the source $X$ uniform on $\{001, 010, 100, 111\}$ and the [seeded extractor](/seeded-extractor/) $\mathrm{Ext}(x, y) = \langle x, y \rangle \bmod 2$ with a uniform seed $y \in \{0,1\}^3$. Compute the strong distance $\Delta((Y, \mathrm{Ext}(X, Y)), (Y, U_1))$ exactly and compare it with the bound $\frac12\sqrt{2^{m-k}}$ of the leftover hash lemma.

13. • Let $\mathrm{Disp}(x, y)$ be the $y$-th neighbour of $x$ in the cycle on the 8 vertices $0, \ldots, 7$, with one seed bit. Find the smallest number of neighbours of a set of 4 vertices, and the least $\varepsilon$ for which this is a $(2, \varepsilon)$-[disperser](/disperser/). Explain why the spectral bound $\varepsilon \le \lambda^2 N/K$ says nothing here.

14. • A coin with $\Pr[1] = 0.2$ is flipped 100 times. Compute the min-entropy and the Shannon entropy of the 100 flips. How many bits within distance $2^{-10}$ of uniform does the leftover hash lemma extract? Compare with the expected output of von Neumann debiasing and with the number of bits that Peres's iteration approaches.

15. • Let $X_1, \ldots, X_{100}$ be 4-wise independent and uniform on $\{-1, +1\}$, and $S = \sum_i X_i$, so that $\mathrm{E}[S^4] = 3n^2 - 2n$. Bound $\Pr[|S| \ge 50]$ with the fourth moment, and compare with Chebyshev's inequality, which uses only pairwise independence.

16. • Any $k$ bits of an $\varepsilon$-biased space are within $\frac{\varepsilon}{2}\sqrt{2^k - 1}$ of uniform. Find the largest $\varepsilon$ that makes every 10 of $n = 1000$ bits within $0.01$ of uniform, and the seed length of the powering generator, $2\lceil \log_2((n-1)/\varepsilon) \rceil$, for this $\varepsilon$.

17. • The polynomial design of the [Nisan-Wigderson generator](/nisan-wigderson-generator/) over $\mathrm{GF}(q)$ uses the graphs of the polynomials of degree less than $r$. For $q = 5$ and $r = 2$, and again for $r = 3$, give the number of sets $m$, the set size, the seed length $d$ and the largest overlap $a$. How much larger than the tests must the circuits be that the hard function defeats, that is, what is $(m-1)(a+1)2^a + 2$?

18. • In the complete graph $K_4$ the walk matrix has eigenvalues $1$ and $-1/3$, so $\lambda = 1/3$. Let $B$ be a set of two vertices. Compute exactly the probability that a walk with $t$ vertices, started at a uniform vertex, stays in $B$, and compare it with the bound of the expander walk sampler. Give both values for $t = 5$.

19. • Run [Nisan's generator](/nisan-prg/) over $\mathrm{GF}(4)$ built with $t^2 + t + 1$, with the elements written $0, 1, 2 = t, 3 = t + 1$, on the seed $x = 2$, $h_1(y) = y + 1$, $h_2(y) = 2y$, $h_3(y) = 3y + 1$. List the eight blocks. How many bits are the seed and the output?

20. ★ Show that no $G : \{0,1\}^d \to \{0,1\}^m$ with $m > d$ fools every test: give a test with advantage at least $1 - 2^{d-m}$. In the same way, show that a function $\{0,1\}^n \times \{0,1\}^d \to \{0,1\}^m$ with $m > k + d$ has error at least $1 - 2^{k+d-m}$ on some flat source of min-entropy $k$, so it is not a [randomness extractor](/randomness-extractor/) with small error. Evaluate the second bound for $k = 10$, $d = 5$, $m = 20$, and say why the first does not contradict the existence of pseudorandom generators.

21. ★ A family of $N$ tests on $\{0,1\}^m$ each accept at least half of the strings. Show that $T$ independent uniform strings hit every test with probability at least $1 - N 2^{-T}$, so that a set of $\lceil \log_2 N \rceil + 1$ strings hitting all of them exists; give $T$ for $N = 2^{1000}$. Then show that a set that hits every test accepting at least half of the strings, with no limit on the tests, needs more than $2^{m-1}$ strings. Relate both facts to the [hitting set generator](/hitting-set-generator/).

22. ★ Prove that a sample space of $n$ unbiased pairwise independent bits has at least $n + 1$ points, and that a sample space of $n$ unbiased 4-wise independent bits has at least $1 + n + \binom{n}{2}$ points. Give both numbers for $n = 8$.

23. ★ Prove that a space of $n$ bits whose every nonempty parity has bias less than 1 has at least $n + 1$ points. Use this to show that the space of Exercise 4 is not $\varepsilon$-biased for any $\varepsilon < 1$, although it is pairwise independent.

24. ★ Peres's procedure outputs the von Neumann bits of $x$, then applies itself to the sequence $u$ that marks the unequal pairs and to the sequence $v$ of values of the equal pairs. Derive a recurrence for the rate $r_\nu(p)$, in output bits per input flip, at recursion depth $\nu$, with $r_1(p) = p(1 - p)$. Compute $r_2(1/3)$ exactly and compare it with $r_1(1/3)$ and with the entropy $H(1/3)$.

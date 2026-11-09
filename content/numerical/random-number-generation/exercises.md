1. ◦ Use the [Hull-Dobell theorem](/hull-dobell-theorem/) to decide which of these generators $s \leftarrow (as + c) \bmod m$ have full period: $(m, a, c) = (100, 21, 3)$, $(100, 11, 7)$, $(64, 13, 7)$ and $(64, 13, 8)$. For each one that fails, name the condition it breaks and find its period from the seed 0.

2. ◦ A 16-bit random word $W$ is reduced to $W \bmod 1000$. Which values have the larger probability, and what are the two probabilities? Compute the total variation distance from uniform with the formula of [modulo bias](/modulo-bias/), and the expected number of words that the rejection fix uses.

3. ◦ Run the four-digit [middle-square method](/middle-square-method/) from the seed 1234 until a value repeats. Give the first three successors, the tail length $\mu$, the period $\rho$, and the value the sequence ends in.

4. ◦ A four-bit [linear feedback shift register](/linear-feedback-shift-register/) follows $s_{i+4} = s_{i+2} \oplus s_i$, with characteristic polynomial $x^4 + x^2 + 1$. Split the 15 nonzero states into cycles and give their lengths. Why is the maximal length 15 not reached?

5. ◦ Apply von Neumann's method from [unbiased bits from a biased coin](/unbiased-bits-from-biased-coin/) to the flips 0 1 1 1 1 0 0 1 0 0 1 0 1 1. Which bits come out? For a coin with $p = 0.9$, how many flips does one output bit cost on average, and what is the entropy bound $h(0.9)$ on the rate?

6. ◦ Compute the point with index 23 of the [Halton sequence](/halton-sequence/) in the bases 2, 3 and 5, as exact fractions.

7. ◦ Evaluate the bound $(d!\,m)^{1/d}$ of [Marsaglia's theorem](/marsaglia-hyperplane-theorem/) for $m = 2^{16}$ and $d = 2, 3, 4$. At most how many planes hold the triples of any [LCG](/linear-congruential-generator/) with this modulus?

8. ◦ Run [Blum Blum Shub](/blum-blum-shub/) with $p = 7$, $q = 11$ and the seed 3, so that $x_0 = 9$. List the states until they repeat, the output bits, and the period.

9. ◦ For the multiplicative generator $s \leftarrow 5s \bmod 32$, find the period from the seeds 1, 2, 4 and 8. Which seeds give the largest period, and how does it compare with $m = 32$?

10. • Run [Lemire's method](/lemire-bounded-integers/) with $w = 8$ and range $s = 10$ over all 256 words. Which words are rejected, how many words need the division that computes the threshold, and how many accepted words give each output?

11. • Count the pairs $(a, c)$ with $0 \le a, c < 200$ for which $s \leftarrow (as + c) \bmod 200$ has full period. Check your count by a program that runs every pair.

12. • The multiplier $a = 2^{16} + 5$ with $m = 2^{31}$ and $c = 0$ is a near relative of [RANDU](/randu/). Show that $a^2 \equiv 10a - 25 \pmod{2^{31}}$, deduce a linear relation between three consecutive outputs $u_i, u_{i+1}, u_{i+2}$, and bound the number of planes that hold all triples. How many of these planes does a run of $3 \times 10^5$ outputs from the seed 1 actually use?

13. • For $s \leftarrow (5s + 3) \bmod 16$, the leapfrog subsequence $s_0, s_k, s_{2k}, \ldots$ is again an LCG. Find its multiplier and increment for $k = 2$ and $k = 4$, and its period from $s_0 = 7$. What does $k = 4$ show about the generator?

14. • Write a [jump-ahead](/jump-ahead/) routine for the LCG with $m = 2^{32}$, $a = 1664525$ and $c = 1013904223$ that composes affine maps by repeated squaring. Give the affine map $(A, C)$ for a jump of $10^6$ steps and the state $s_{10^6}$ from the seed 0, and check it against a direct loop.

15. • You need a uniform integer in $\{0, \ldots, 4\}$ from fair coin flips by rejection. One plan reads 3 flips and rejects 5, 6 and 7; another reads 4 flips, rejects 15 and returns the value mod 5. Find the expected number of flips of each, and compare with the entropy bound $\log_2 5$ of [uniform random integer generation](/uniform-random-integer-generation/).

16. • A [Fisher-Yates shuffle](/fisher-yates-shuffle/) of three items draws its first swap index as $W \bmod 3$ and its second as $W \bmod 2$, with each $W$ a uniform 3-bit word. Find the probability of each of the six permutations.

17. • A cluster starts $10^4$ jobs, each with an independent uniform 32-bit [seed](/seed/). Estimate the probability that two jobs share a seed. With 64-bit seeds, about how many jobs bring that probability to 1 percent?

18. • The tempering of the [Mersenne Twister](/mersenne-twister/) contains the step $y \leftarrow y \oplus (y \gg 18)$ on 32-bit words. Show that this step is its own inverse, and that $y \oplus (y \gg 11)$ is undone by $z \mapsto z \oplus (z \gg 11) \oplus (z \gg 22)$. Why does this make the generator predictable?

19. • A die is rolled 6000 times by a generator and the faces come up 1020, 950, 1010, 1060, 980 and 980 times. Compute Pearson's chi-square statistic, and decide at the 5 percent level, where the critical value on 5 degrees of freedom is about 11.07, whether the test of [statistical tests for randomness](/statistical-tests-for-randomness/) rejects the generator.

20. • A toy [multiply-with-carry](/multiply-with-carry/) generator has base $b = 10$ and $a = 6$, so $m = ab - 1 = 59$, a safe prime. Run it from $(x, c) = (1, 0)$ for a few steps, find its period, and explain why it is $m - 1$ and not $(m - 1)/2$. Which of the 60 pairs $(x, c)$ with $0 \le x < 10$, $0 \le c < 6$ are fixed points?

21. ★ Show that $a^{2^{w-2}} \equiv 1 \pmod{2^w}$ for every odd $a$ and $w \ge 3$, so that a multiplicative LCG modulo $2^w$ has period at most $2^{w-2}$. For $w \ge 4$, show that the period from an odd seed equals $2^{w-2}$ exactly when $a \equiv 3$ or $5 \pmod 8$. What goes wrong at $w = 3$?

22. ★ Carry out the three-dimensional [spectral test](/spectral-test/) for the generator of exercise 12: find the shortest nonzero vector of the lattice $\{k \in \mathbb{Z}^3 : k_1 + k_2 a + k_3 a^2 \equiv 0 \pmod{2^{31}}\}$, prove that nothing shorter exists, and give the largest distance between adjacent planes. Compare it with RANDU's.

23. ★ A 16-bit [xorshift](/xorshift/) generator applies $x \leftarrow x \oplus (x \ll a)$, $x \leftarrow x \oplus (x \gg b)$, $x \leftarrow x \oplus (x \ll c)$ with masking to 16 bits. Write a program that decides, by computing powers of the $16 \times 16$ matrix over $\mathrm{GF}(2)$, which of the $15^3$ triples with $1 \le a, b, c \le 15$ give period $2^{16} - 1$. How many do, and what test on the matrix order do you use?

24. ★ Let $n = pq$ with primes $p \equiv q \equiv 3 \pmod 4$. Show that squaring is a permutation of the quadratic residues modulo $n$ that are coprime to $n$. Deduce that every Blum Blum Shub state sequence is purely periodic, and that the generator can run backwards when $p$ and $q$ are known.

25. ★ Elias's method cuts the flips of a biased coin into blocks of 4. Within a block with $j$ ones, the $\binom{4}{j}$ strings are equally likely; their index is turned into fair bits by splitting $\binom{4}{j}$ into powers of two. Find the expected number of fair bits per block for $p = 1/2$ and $p = 0.7$, and compare the rates per flip with von Neumann's.

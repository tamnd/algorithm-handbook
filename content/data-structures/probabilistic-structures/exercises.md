1. ◦ A [Bloom filter](/bloom-filter/) has $m = 1200$ bits and $k = 5$ hash functions, and holds $n = 100$ keys. Estimate its false positive rate with $(1 - e^{-kn/m})^k$.

2. ◦ You need a false positive rate of $\varepsilon = 0.001$. How many bits per key does a Bloom filter with the best $k$ use? How many does the [lower bound](/bloom-filter-lower-bound/) require? Give both in megabytes for $10^6$ keys.

3. ◦ A Bloom filter has $m = 12$ bits and $k = 2$. The keys a, b and c have the positions $(1, 5)$, $(5, 9)$ and $(2, 11)$. Which bits are set after the three inserts? What do the queries for x, at $(1, 9)$, and y, at $(3, 5)$, return? Which answer is wrong?

4. ◦ A [counting Bloom filter](/counting-bloom-filter/) with the same positions as in exercise 3 holds a and b. A program deletes x, at $(1, 9)$, which was never inserted. What does the filter now answer for a?

5. ◦ A count-min sketch should overestimate each count by at most $0.001 N$ with probability at least $0.99$. What width $w$ and depth $d$ does the [error bound](/count-min-error-bound/) give? How many counters is that, and how many bytes with 4-byte counters?

6. ◦ A [quotient filter](/quotient-filter/) has $2^{20}$ slots, each with a remainder of $r = 7$ bits and 3 bits of metadata. How many bits does it use? At a load of $0.75$, how many keys does it hold, how many bits per key does it use, and what is its bound $\alpha 2^{-r}$ on the false positive rate?

7. ◦ An [xor filter](/xor-filter/) with 8-bit fingerprints holds $n = 10^6$ keys in $3\lceil (\lfloor 1.23 n \rfloor + 32)/3 \rceil$ cells. How many bits does it use, and what is its false positive rate? How many bits per key would an optimal Bloom filter need for the same rate?

8. ◦ One bitmap of a [Flajolet–Martin sketch](/flajolet-martin-sketch/) has bits 0 to 7 equal to $1, 1, 1, 1, 0, 1, 0, 0$. What is $R$, and what does the single-bitmap estimate $2^R/\varphi$ give, with $\varphi = 0.77351$? How many bitmaps does PCSA need for a standard error of 5 percent?

9. • For the filter of exercise 1, find the integer $k$ that gives the smallest rate, and that rate. Compare $k$ with $(m/n) \ln 2$.

10. • Show that, with the best $k$, each extra $1.44$ bits per key halves the false positive rate of a Bloom filter.

11. • A [scalable Bloom filter](/scalable-bloom-filter/) has a first slice for 1000 keys and growth factor $s = 2$, so slice $i$ holds $1000 \cdot 2^i$ keys. Slice $i$ has rate $\varepsilon_0 r^i$ with $\varepsilon_0 = 0.0005$ and $r = 1/2$. How many slices does it have after $10^6$ inserts? What bound on the total rate does it guarantee? How many bits per key does the last slice use, against the first, at the best $k$?

12. • A filter must hold $10^9$ keys with $\varepsilon = 2^{-10}$. How many gigabytes does the lower bound require? How many does a Bloom filter use, an xor filter at $1.23$ times the bound, and a [binary fuse filter](/binary-fuse-filter/) at $1.125$ times the bound?

13. • A count-min sketch has $d = 2$ rows of $w = 4$ counters. Row 1 sends a, b, c, d to columns 0, 1, 0, 2, and row 2 sends them to columns 3, 3, 1, 2. The stream is a, a, a, a, a, b, b, b, c, c, d. Give the counters and the estimate of each item. Which estimates are wrong?

14. • Run the same stream through the sketch of exercise 13 with the *minimal increase* rule of the [spectral Bloom filter](/spectral-bloom-filter/): each arrival raises only the counters that equal the current estimate. Give the counters and the estimates.

15. • A counting Bloom filter has $m = 10^6$ counters and the best $k$. The bound on the probability that some counter reaches $i$ is $m (e \ln 2 / i)^i$. Evaluate it for 3-bit counters, which overflow at $i = 8$, and for 4-bit counters, at $i = 16$. Are 3-bit counters safe?

16. • A [cuckoo filter](/cuckoo-filter/) has buckets of $b = 4$ slots and runs at 95 percent load. Its rate is at most $(2b + 1)/(2^f - 1)$. Find the smallest fingerprint size $f$ for a rate of at most $10^{-5}$, and the bits per key. Compare with a Bloom filter.

17. • An xor filter has 9 cells in three blocks, $\{0, 1, 2\}$, $\{3, 4, 5\}$ and $\{6, 7, 8\}$. Set A has keys at the cells $(0, 3, 6)$, $(0, 4, 7)$, $(1, 4, 8)$, $(2, 5, 7)$; set B has keys at $(0, 3, 6)$, $(0, 3, 7)$, $(1, 4, 6)$, $(1, 4, 7)$. Which set can be peeled? For the other set, when does the system of equations still have a solution?

18. • A [learned Bloom filter](/learned-bloom-filter/) for $10^6$ keys should have an overall rate of $0.001$, which is $F_p + (1 - F_p)\varepsilon_b$. Its classifier has $F_p = 0.0005$ and misses 40 percent of the keys. What rate $\varepsilon_b$ must the backup filter have? How many bits do the backup filter and an ordinary Bloom filter for the whole set use? How large may the classifier be for the learned filter to save space?

19. • A Bloom filter has $m = 4$ bits and $k = 2$ independent uniform hash functions, which may choose the same bit twice. It holds one key. Find the exact false positive rate, and compare it with $(1 - (1 - 1/m)^{kn})^k$ and with $(1 - e^{-kn/m})^k$.

20. • You have $10^7$ bits for a Bloom filter with a target rate of $0.01$. How many keys can it hold at the best $k$, and what is that $k$?

21. ★ A Bloom filter with $m$ bits and $k$ hash functions has $X$ bits set, and you do not know $n$. Using the expected number of zero bits, derive an estimate of $n$ from $X$. Evaluate it for $m = 1000$, $k = 4$, $X = 400$.

22. ★ A count-min sketch can use width $w = \lceil c/\varepsilon \rceil$ and depth $d = \lceil \ln(1/\delta)/\ln c \rceil$ for any $c > 1$, since by Markov's inequality each row fails with probability at most $1/c$. Ignoring the rounding, show that the number of counters is smallest at $c = e$. For $\varepsilon = \delta = 0.001$, compare the counters for $c = e$ and $c = 2$.

23. ★ A *partitioned* Bloom filter splits its $m$ bits into $k$ parts of $m/k$ bits, and hash function $i$ sets a bit of part $i$. Show that after $n$ inserts its expected fraction of zero bits, $(1 - k/m)^n$, is at most that of the standard filter, $(1 - 1/m)^{kn}$. Evaluate the rates $(1 - \text{zero fraction})^k$ of both for $m = 1200$, $k = 5$, $n = 100$.

24. ★ Take a quotient filter at load $\alpha = 0.75$, with $r = \lceil \log_2(\alpha/\varepsilon) \rceil$ and $(r + 3)/\alpha$ bits per key, and an optimal Bloom filter with $\log_2(1/\varepsilon)/\ln 2$ bits per key. For targets $\varepsilon = 2^{-L}$ with $L$ an integer, find the smallest $L$ at which the quotient filter uses fewer bits per key.

25. ★ To answer the total count of a range $[l, r]$ of items, a sketch can be kept for each level of the dyadic intervals of $\{0, \ldots, 2^h - 1\}$, and the range split into dyadic intervals. Show that for $h \ge 2$ every range needs at most $2h - 2$ intervals and that some range needs exactly that many. For $h = 16$, how many point queries does a range query make at most?

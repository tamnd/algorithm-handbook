1. $kn/m = 5/12$, so the rate is about $(1 - e^{-5/12})^5 \approx 0.0046$.

3. Bits 1, 2, 5, 9 and 11 are set. The query for x finds bits 1 and 9 set and answers "maybe present"; that is a false positive. The query for y finds bit 3 clear and answers "absent", which is right.

5. $w = \lceil e/0.001 \rceil = 2719$ and $d = \lceil \ln 100 \rceil = 5$, so 13 595 counters, or 54 380 bytes.

7. There are $3 \cdot 410\,011 = 1\,230\,033$ cells, so 9 840 264 bits, about $9.84$ bits per key. The rate is $2^{-8} \approx 0.0039$, and a Bloom filter needs $8/\ln 2 \approx 11.54$ bits per key for it.

9. Here $(m/n)\ln 2 \approx 8.32$. Try the integers near it.

11. After $t$ slices the capacity is $1000(2^t - 1)$. The rates form a geometric series.

13. Count each item into its two counters. Only one item shares a counter with another item in both rows.

17. Look for a cell that belongs to exactly one key. In set B, add the equations of the first two keys, and then those of the last two.

18. Solve $0.0005 + 0.9995\,\varepsilon_b = 0.001$. A Bloom filter for $n$ keys at rate $\varepsilon$ uses $n \log_2(1/\varepsilon)/\ln 2$ bits.

21. After $n$ inserts the expected number of zero bits is $m(1 - 1/m)^{kn} \approx m e^{-kn/m}$. Set it equal to $m - X$ and solve for $n$.

22. The number of counters is about $\frac{c}{\ln c} \cdot \frac{1}{\varepsilon} \ln \frac{1}{\delta}$. Differentiate $c/\ln c$.

23. Compare $(1 - 1/m)^k$ with $1 - k/m$; the first is at least the second by Bernoulli's inequality.

24. For an integer $L$, $\log_2(0.75 \cdot 2^L) = L - 0.415$, so $r = L$.

25. Work from the two ends of the range toward the top of the tree. At each level, at most one interval is taken on the left side and at most one on the right side.

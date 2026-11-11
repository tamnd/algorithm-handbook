1. ◦ Write down the [frequency vector](/frequency-vector/) of the stream b, c, b, a, b, d, c, b over the items a, b, c, d. Give $F_0$, $F_1$, $F_2$ and $\|f\|_\infty$. Which items are $\ell_1$ heavy hitters for $\phi = 0.3$, and which are $\ell_2$ heavy hitters for the same $\phi$?

2. ◦ Run the [Boyer-Moore majority vote](/boyer-moore-majority/) on c, a, c, b, c, a, a, c, c. Give the candidate and the counter after each item, and say what the second pass reports.

3. ◦ Run the [Misra-Gries summary](/misra-gries-summary/) with $k = 3$, so with two counters, on a, b, c, a, b, a, d, a, c, b, a. Give the final counters and the number of decrement steps, and check the error bound $m/k$ for every item.

4. ◦ A [count-min sketch](/count-min-sketch/) has $w = 5$ and $d = 2$, with $h_1(x) = x \bmod 5$ and $h_2(x) = ((3x + 1) \bmod 31) \bmod 5$. Apply the updates $(2, 4)$, $(4, 1)$, $(6, 2)$, $(9, 3)$, $(13, 5)$. Give the two rows and the estimates for the items 2, 4, 6, 9, 13 and for the absent item 11.

5. ◦ With $U = 32$, split the range $[5, 26]$ into the fewest [dyadic intervals](/dyadic-intervals/), and do the same for the prefix $[0, 22]$. Which range in $[0, 31]$ needs the most intervals, and how many?

6. ◦ The stream is 2, 2, 2, 7, 7, 9, 9, 9, 9, 4, so $n = 10$. With $\varepsilon = 0.1$, list every value that is an $\varepsilon$-approximate $\phi$-quantile in the sense of the [quantile summary problem](/quantile-summary-problem/), for $\phi = 0.5$, $\phi = 0.9$ and $\phi = 0.3$.

7. ◦ Find the empirical entropy of a, b, a, c, a, b, a, d. Then compute the sampling estimator $X = g(R) - g(R - 1)$ of the [entropy estimation problem](/entropy-estimation-problem/) for each of the eight start positions, with $g(r) = r\log_2(m/r)$, and check that the mean of the eight values is the entropy.

8. ◦ A [linear counting](/linear-counting/) bitmap has $m = 16$ bits. Give the estimate when 6 bits are set and when 7 bits are set. Then find the number of [HyperLogLog](/hyperloglog/) registers, as a power of 2, for a relative standard error of at most 1%, and the size in bytes with 5-bit registers.

9. ◦ Size three sketches. (a) Count-min with $\varepsilon = 0.001$ and $\delta = 10^{-4}$. (b) The [count sketch](/count-sketch/) with $\varepsilon = \delta = 0.01$, with $w = \lceil 3/\varepsilon^2 \rceil$ and $d = \lceil 18\ln(1/\delta) \rceil$. (c) The number of copies the [median trick](/median-trick/) needs for $\delta = 10^{-6}$ when each copy fails with probability $p = 1/4$, and when $p = 1/3$.

10. ◦ The [mergeable summary](/mergeable-summaries/) for the variance keeps $(n, \mu, M)$, with $M$ the sum of squared deviations from the mean. Build it for the parts 2, 4, 9 and 1, 7, merge the two, and check the result against the five values directly.

11. • A [Morris counter](/morris-counter/) must count up to $n = 10^{12}$. (a) How many bits does an exact counter need? (b) Bound the chance that the register reaches 50, and give a register size. (c) How many copies does Morris+ need for a relative standard deviation of 5%? (d) Morris(a) with $\varepsilon = 0.1$ and $\delta = 0.05$ uses $a = 2\varepsilon^2\delta$; about how large is its register at $n = 10^9$? (e) Give the distribution of the base-2 register after 5 events, and check the mean and variance of the estimate.

12. • Run Misra-Gries with $k = 3$ on $s_1$ = a, a, b, a, a, b, c, a and on $s_2$ = b, c, b, c, d, b, c. Merge the two summaries with MG-MERGE. Check the error of every item against the bound for the merged summary, and compare with Misra-Gries run on $s_1$ followed by $s_2$.

13. • Run [Space-Saving](/space-saving/) with $k = 3$ on $s_1$ and on $s_2$ of the previous exercise. Give the counters and $\mu$, and check that subtracting $\mu$ from each counter gives the Misra-Gries summaries of the previous exercise.

14. • Run [lossy counting](/lossy-counting/) with $w = 4$ on a, b, c, a, d, b, a, e, b, c, a, f, a, b ($N = 14$). Give the entries after each bucket boundary and at the end. Which item has the largest error, and is the bound $\lfloor N/w \rfloor$ reached?

15. • For support $s = 0.01$, $\varepsilon = 0.001$ and $\delta = 10^{-4}$, compare the expected number of entries of [sticky sampling](/sticky-sampling/), the worst-case number of entries of lossy counting after $N = 10^9$ items, and the counters of Misra-Gries and Space-Saving for error $\varepsilon N$.

16. • [Sample and hold](/sample-and-hold/) samples each packet of an untracked flow with probability $p$. (a) With $p = 0.1$, how likely is it that a flow of 30 packets is missed? (b) With oversampling $O = 20$ and threshold $T = 1000$, give $p$, the chance of missing a flow of size $T$, and the bound on the standard deviation of its estimate. (c) Bound the expected number of entries for a stream of $10^6$ packets.

17. • Run the [Flajolet-Martin algorithm](/flajolet-martin-algorithm/) on the 8-bit hash values 10011000, 01110101, 00100110, 11010100, 01011010, 10000001, 00111100 of seven distinct items. Give the bitmap, $R$ and the estimate. Then give the estimate of the AMS version, which keeps only $Z$.

18. • A [KMV sketch](/kmv-sketch/) with $k = 4$ is built on set $A$ with hash values a .42, b .07, c .33, d .91, e .15, f .58, g .26, and on set $B$ with c .33, e .15, h .04, i .71, j .19, k .48. Estimate $|A|$, $|B|$ and $|A \cup B|$. Then estimate $|A \cap B|$ and the Jaccard similarity, and compare with the true values.

19. • A HyperLogLog with $m = 16$ has registers 0, 2, 1, 0, 3, 1, 0, 2, 4, 1, 0, 2, 1, 1, 0, 2, and $\alpha_{16} = 0.673$. Compute the raw estimate, decide whether the small-range correction applies, and give the final estimate. Compare with the [LogLog](/loglog-counting/) estimate from the same registers, with $\alpha_{16} = 0.376$. Repeat for the registers 3, 5, 2, 4, 6, 3, 2, 4, 5, 3, 4, 2, 7, 3, 4, 5.

20. • For $f = (3, 1, 1)$, list $Z^2$ for all eight sign vectors of the [AMS sketch](/ams-sketch/). Check that the mean is $F_2$ and find the variance. With the mean of 24 copies, what does Chebyshev's inequality give for an error of $0.5F_2$?

21. • For $f = (1, 2, 0, 3)$ and $g = (2, 1, 4, 1)$, find the join size $J$, the self-join sizes, and the variance of the tug-of-war estimate $Z_f Z_g$ of the [join size estimation problem](/join-size-estimation-problem/). Give the additive error for $\varepsilon = 0.1$ and the number of copies for $\delta = 0.01$.

22. • One level of an [L0 sampler](/l0-sampler/) holds $x_3 = 2$ and $x_5 = -1$. Compute $A$ and $B$ and the coordinate they suggest. With $q = 11$ and $z = 2$, compute $C$ and run the fingerprint test. How many copies $R$ are needed for $\delta = 0.01$ and for $\delta = 1/2$?

23. • In the [AGM sketch](/agm-graph-sketch/) on 4 vertices, insert the edges {1, 2}, {2, 3}, {1, 4}, {3, 4} and then delete {2, 3}. Write the four signed incidence vectors. Add them over $S = \{1, 2\}$, over $S = \{1, 2, 4\}$ and over all four vertices, and say what each sum tells you.

24. • Use the reduction from INDEX on the [INDEX lower bound](/index-problem-lower-bound/) page with $x = 1011$ and $i = 2$, indexed from 0. Write the stream of Alice and Bob, find its median, and read off $x_2$.

25. ★ A count-min sketch with $w = 4$ and $d = 3$ uses $h_1(x) = x \bmod 4$, $h_2(x) = (5x \bmod 13) \bmod 4$ and $h_3(x) = ((7x + 3) \bmod 13) \bmod 4$. Apply $(1, 5)$, $(2, 3)$, $(6, -4)$, $(7, 2)$ in the general [turnstile model](/turnstile-model/). Estimate the items 1, 2, 6, 7 and the absent item 3, once with the minimum and once with the median of the rows. Which rule is right here, and why does the minimum fail?

26. ★ Merge the two Space-Saving summaries of Exercise 13 through the Misra-Gries merge, and put back $D = \lfloor (m - \sum C)/k \rfloor$. Give the merged estimates and check that each is an overestimate by at most $m/k$.

27. ★ Run the [KLL sketch](/kll-sketch/) with $k = 6$ and $c = 2/3$ on 6, 13, 2, 9, 15, 4, 11, 1, 8, 14, 3, 12, 7, 10, 5, 16, with the random bits 1, 0, 1, 1 in order. Give each compaction, the final levels, the estimated rank of every value from 1 to 16, the largest rank error, and the answer to the query for rank 8.

28. ★ The edges of $K_4$ arrive as {1, 2}, {1, 3}, {3, 4}, {2, 3}, {1, 4}, {2, 4}. Find the distribution of one neighbourhood sampling estimate of [streaming triangle counting](/streaming-triangle-counting/), with its mean and variance. How many copies does Chebyshev's inequality ask for with $\varepsilon = \delta = 0.1$, and with $\varepsilon = 0.2$, $\delta = 0.1$?

29. ★ Follow the reduction on the [frequency moment lower bounds](/frequency-moment-lower-bounds/) page for $n = 10^6$ and $k = 3$. Give $t$, the largest $F_3$ of a NO instance, the smallest $F_3$ of a YES instance, and the decision threshold for $\varepsilon = 1/3$. If one-way promise disjointness needed exactly $n/t$ bits, what space would a one-pass algorithm need, and how does that compare with $n^{1 - 2/k}$?

30. ★ Answer rank queries over integers in $[0, 2^{16})$ with count-min sketches on dyadic intervals, one sketch per level. A rank query by binary search makes 16 prefix queries of at most 16 point queries each. For $\varepsilon = \delta = 0.01$ with the error measured against $n$, choose the per-sketch $\varepsilon'$ and $\delta'$ and give the total number of counters. Compare with the size bound of the [q-digest](/q-digest/).

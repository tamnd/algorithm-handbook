1. ◦ List the [k-mers](/kmer/) of ACGTTGCAAC for $k = 3$. How many are there, how many are distinct, and how many distinct canonical k-mers remain when each k-mer is replaced by the smaller of itself and its reverse complement? How many canonical 3-mers and canonical 4-mers exist in all?

2. ◦ A bacterial genome has $G = 5$ Mbp and is sequenced with reads of length $L = 150$. How many reads give [coverage](/sequencing-coverage/) $c = 40$? At $c = 5$, about how many bases are unread and about how many gaps are there, under the Poisson model?

3. ◦ An assembly has contigs of lengths 50, 45, 30, 25, 20, 15, 10 and 5 kbp. Find its [N50](/n50/), L50 and N90. The genome is known to be 300 kbp long; find NG50. Then the contigs of 45 and 30 kbp are wrongly joined into one contig of 75 kbp. What are the new N50, L50 and NG50?

4. ◦ Build the [de Bruijn graph](/de-bruijn-graph/) of the 3-mers of ATGGCGTGCA, with the 2-mers as vertices. Which vertices are not simple, and what are the [unitigs](/unitig/)?

5. ◦ A [paired-end](/paired-end-reads/) library has mean insert size $\mu = 500$ and standard deviation $\sigma = 40$. Four pairs link contig A to contig B, with distances from the read ends to the contig ends $(d_A, d_B) = (180, 120)$, $(150, 120)$, $(210, 120)$ and $(160, 130)$. Estimate the gap from each pair with $g = \mu - d_A - d_B$, then give the mean and the standard deviation of the mean.

6. ◦ Merqury finds that a fraction $K_a/K = 0.001$ of the 21-mers of an assembly are absent from the reads. Estimate the base error rate and the QV, using $e = 1 - (1 - K_a/K)^{1/k}$ from [quality assessment](/assembly-quality-assessment/). What QV does an assembly of 5 Mbp with 50 errors have?

7. ◦ A [k-mer spectrum](/kmer-spectrum/) for $k = 21$ has $M = 1.5 \cdot 10^9$ k-mers in total, of which $M_s = 1.2 \cdot 10^9$ lie in the main peak, and the peak is at $\lambda = 24$. Estimate the genome size and the per-base error rate.

8. ◦ Two reads of length 100 overlap along their whole length and differ in $e$ positions. Seeds have length 21. For which $e$ does the pigeonhole argument of [overlap detection](/overlap-detection/) guarantee a shared exact seed? If the two reads differ independently at each position with probability 0.02, what is the chance that a fixed 21-mer of the overlap is error-free?

9. ◦ In the [Lander-Waterman model](/lander-waterman-model/), take $G = 2$ Mbp, $L = 1000$, $c = 8$ and a minimum detectable overlap $T = 250$, so $\sigma = 0.75$. Find the number of reads, the expected number of islands, the expected number of true gaps $N e^{-c}$, the mean number of reads per island and the mean island length.

10. • A circular genome has two repeats X, of length 300, and Y, of length 500, whose copies interleave, a repeat Z of length 200 with three copies, and a repeat W of length 2000 with two copies that do not interleave with any other repeat. Using the [repeat](/genome-repeat/) analysis, what read length does Ukkonen's condition require, and is that length enough when all the $L$-mers of the genome are known? Explain why W does not count.

11. • [Greedy merging](/greedy-shortest-common-superstring/) is run on a genome of $G = 4 \cdot 10^6$ with reads of length $L = 800$ and longest repeat $R = 200$. Using the expected number of breaks $N e^{-c(L - R - 1)/L}$, compare $c = 10$ with $c = 20$.

12. • The genome TGACCATGCTTAGCATCG is read error-free by six reads of length 8 starting at positions 0, 2, 4, 6, 8 and 10. Build the overlap graph with minimum overlap $\ell = 3$ and the [string graph](/string-graph/). Count the edges before and after transitive reduction. Then do the same for $\ell = 4$.

13. • In [consensus calling](/consensus-sequence-calling/) with weights $w = \log_{10}(3(1-p)/p)$, a column has three reads with A at Q20 and two reads with G at Q30. Which base is called? Which base is called if the three A reads are at Q15 instead?

14. • Reads have length $L = 100$ and $k = 31$. A single substitution sits at position $i$ of a read, counting from 0, and the other k-mers of the read are true. For which $i$ does it make a source tip, a sink tip or a bubble, and how many edges does each tip have? Does the default length bound $2k$ of [tip removal](/tip-removal/) catch every tip? How many false k-mers does one error create on average, over a uniform position?

15. • A genome of $G = 5 \cdot 10^6$ is read at $c = 15$ with reads of length 100, and $k = 31$. About how many true k-mers are lost when [graph simplification](/assembly-graph-simplification/) drops k-mers seen fewer than $t = 2$ times? Fewer than $t = 3$ times? Use a Poisson model for the k-mer depth.

16. • A [gap-filling](/gap-filling/) graph has edges $s \to a$ of length 4, $s \to b$ 6, $a \to b$ 3, $a \to c$ 5, $b \to c$ 2, $c \to b$ 2, $c \to t$ 3 and $b \to t$ 7. Walks may repeat vertices. Which walk lengths from $s$ to $t$ are possible up to 20? List the walks of length $15 \pm 1$, and say whether the gap has a unique fill when the length must be exactly 15.

17. • Four contigs A, B, C, D are linked by pairs that say whether two contigs have the same or opposite orientation: AB opposite with weight 6, BC same 3, CD opposite 4, DA same 5, AC same 2 and BD same 1. Find the orientation that satisfies the largest total weight in [scaffolding](/scaffolding/), and the cycles that cannot all be satisfied.

18. • In the Lander-Waterman model with $c = 6$ and $\theta = 0.1$, find the probability that an ocean is at least one read length long. Then find the probability that an apparent gap between islands is a true gap in the coverage.

19. • A [hybrid assembly](/hybrid-assembly/) uses long reads of $L = 20$ kb at $c = 15$, and a read bridges a repeat when it covers it plus 1 kb on each side. Using a Poisson count of bridging reads, find the probability that a repeat of 12 kb is not bridged, and the same for 5 kb. What do short reads of 150 bp contribute to bridging?

20. • For a genome of $G = 5 \cdot 10^6$ and reads of $L = 150$, what coverage makes the expected number of gaps $N e^{-c}$ equal to 1? Solve $c = \ln(cG/L)$ by iteration and give the number of reads.

21. • In a set of $m = 10^6$ reads of uniform random sequence, bound the expected number of chance overlaps of length $\ell$ by $m^2 \cdot \frac{4}{3} 4^{-\ell}$. Compare $\ell = 15$ and $\ell = 20$ with the number of true overlaps for reads of 10 kb at $c = 20$, about $Nc$ arcs.

22. ★ Prove that joining two contigs into one never lowers N50, and that adding a contig shorter than the current N50 never raises it. Use the form $N50 = \max\{x : \text{the contigs of length} \ge x \text{ have total length} \ge T/2\}$, where $T$ is the total assembly length, and first prove that it agrees with the sorted definition.

23. ★ In the Lander-Waterman model the expected number of contigs of at least two reads is $N(e^{-c\sigma} - e^{-2c\sigma})$. For fixed $G$, $L$ and $\sigma$, find the coverage that maximizes it and the maximum value. Compare with the coverage at which the number of islands peaks.

24. ★ Find every string whose set of 3-mers equals that of AAACAAGGACC, each 3-mer used once, as in [sequencing by hybridization](/sequencing-by-hybridization/). Check the count with the BEST theorem after adding one arc that closes the Eulerian path into a circuit.

25. ★ Reads are error-free substrings of one strand of a genome, all of length $L$, with distinct start positions, no repeat of length $\ge \ell$, and each read overlapping the next one along the genome by at least $\ell$ letters. Prove that the string graph with minimum overlap $\ell$ is a single chain from the first read to the last, with $N - 1$ edges.

26. ★ For $k \ge 1$, run greedy merging on the three strings $c(ab)^k$, $(ba)^k$ and $(ab)^k c$. Show that greedy outputs a superstring of length $4k + 2$, while a superstring of length $2k + 4$ exists. What does this say about the ratio of greedy, compared with the proved bound and the conjecture of Tarhio and Ukkonen?

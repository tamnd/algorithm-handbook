1. ◦ On the forward strand of `CATGAAATGGCCTAGATGTTTTAAGG`, list every [open reading frame](/open-reading-frame/) that starts at ATG and ends at the first stop codon in the same frame, with its 1-based start and end positions. Which ATG has no stop in its frame before the end of the sequence?

2. ◦ Apply the window rule of [CpG island detection](/cpg-island-detection/) with $w = 200$, $g = 0.5$ and $r = 0.6$ to two windows. The first has 60 C, 50 G and 20 CG pairs. The second has 40 C, 40 G and 4 CG pairs. Compute $(C + G)/w$ and the observed over expected ratio for each, and say which window is marked.

3. ◦ With a uniform background, give the [information content](/motif-information-content/) in bits of motif columns with probabilities $(0.5, 0.5, 0, 0)$, $(1, 0, 0, 0)$ and $(0.7, 0.1, 0.1, 0.1)$ for A, C, G, T. Then give it for the column $(1, 0, 0, 0)$ against the background $(0.3, 0.2, 0.2, 0.3)$.

4. ◦ Solve [exon chaining](/exon-chaining/) for the candidate exons $[1, 5]$ of weight 4, $[3, 9]$ of weight 7, $[6, 8]$ of weight 3, $[9, 12]$ of weight 4, $[10, 15]$ of weight 5, $[13, 18]$ of weight 4 and $[16, 20]$ of weight 2. Two exons that share a position overlap. Give the best chain and its weight.

5. ◦ A reference set gives the [codon adaptation](/codon-adaptation-index/) weights $w(\text{GAA}) = 1$, $w(\text{GAG}) = 0.25$, $w(\text{AAA}) = 1/3$ and $w(\text{AAG}) = 1$. Compute the CAI of the gene fragment GAA GAG AAG AAA.

6. ◦ For the sequences `TACGTTAC`, `GGACGCAT` and `CCTTACGA` and $L = 3$, compute the total distance of `ACG` and of `TAC` in the sense of the [median string problem](/median-string-problem/). Which of them is a median string?

7. ◦ A weight matrix of two columns has the scores A 2, C −1, G 0, T −1 in the first column and A −1, C 1, G 2, T −2 in the second. Under a uniform background, list the 2-mers with score at least 3 and give the [p-value](/pwm-score-p-value/) of the score 3.

8. ◦ In the [planted motif problem](/planted-motif-problem/) with $L = 15$ and $d = 4$, how many 15-mers are within Hamming distance 4 of a fixed motif $M$? What is the probability that a random 15-mer is one of them, and how many such windows do 20 random sequences of length 600 hold by chance?

9. • Show that choosing exons by decreasing weight, skipping any that overlaps one already chosen, gives weight 14 on the exons of exercise 4. Then build, for each $k$, a set of exons on which this greedy rule gets less than $1/k$ of the best weight.

10. • In a random DNA sequence with equal base frequencies, a codon is a stop with probability $3/64$. Give the expected number of stop codons, and so of stop-to-stop open frames, in one million bases read in all six frames. What fraction of these frames have at least 100 sense codons, and how many is that?

11. • A two-state CpG model emits bases independently: the island state emits A and T with probability 0.2 and C and G with 0.3, the background state the reverse. Both states start with probability 1/2, and each stays in itself with probability $a$. For the sequence `AAAACGCGCGCAAAA`, compare the log probability of the all-background path with the path that marks `CGCGCGC` as an island, for $a = 0.9$ and $a = 0.8$. How long must a run of C and G be before the Viterbi path marks it, for each $a$?

12. • In the [Gibbs motif sampler](/gibbs-motif-sampler/) with $L = 3$, pseudocount $b = 1$ and uniform background, the sites of the other three sequences are `ACG`, `ACG` and `ATG`. Give the sampling probability of each window of the left-out sequence `TACGATG`.

13. • A [MEME](/meme-algorithm/) model has $\lambda = 0.01$, motif columns $(0.7, 0.1, 0.1, 0.1)$, $(0.1, 0.1, 0.7, 0.1)$ and $(0.1, 0.1, 0.1, 0.7)$ for A, C, G, T, and a uniform background. Compute the E-step weight $z$ of the windows `AGT`, `AGA` and `CCC`.

14. • Add a third column with scores A 1, C 0, G −1, T 1 to the matrix of exercise 7. Compute the distribution of the score under a uniform background by the dynamic program over partial scores, and give the p-values of the scores 4 and 5.

15. • Run one step of [randomized motif search](/randomized-motif-search/) with pseudocount 1 on the sequences `TACGCC`, `CACGGT` and `GAACGG`, $L = 3$, from the windows `ACG`, `GGT` and `CGG`, breaking ties by the first window. Give the new windows and scores, check that the next step does not improve, and compare with the best possible score.

16. • In [maximal dependence decomposition](/maximal-dependence-decomposition/), 60 sites have the consensus base at position $i$ and 40 do not. At position $j$, the first group has A 40, C 5, G 10, T 5 and the second A 10, C 10, G 10, T 10. Compute the chi-squared statistic of the $2 \times 4$ table and decide whether the pair passes the cutoff 16.3.

17. • Apply the analysis of [random projection](/random-projection-motif-finding/) to the $(18, 5)$ problem with $n = 20$ sequences of length 600, $k = 7$ projected positions and bucket threshold $s = 4$. Compute the probability $p$ that an instance with exactly 5 changes hashes to the bucket of the motif, the probability $P$ that a trial puts 4 or more instances there, the number of trials for 95 percent success, and the expected number of random windows in one bucket.

18. • [Branch-and-bound motif search](/branch-and-bound-motif-search/) over strings prunes a prefix $u$ when the sum over sequences of the smallest distance between $u$ and a window prefix of length $|u|$ exceeds the best total distance found so far. Prove that this bound never removes a better string. For the sequences of exercise 6, compute the bound for the prefix `TT`.

19. • [Tandem repeat finding](/tandem-repeat-finding/) looks for $k$-tuples that match at distance $p$. Show that two adjacent copies of length $p$ that differ only by $e$ substitutions share at least $p - k + 1 - ke$ matching $k$-tuples at distance $p$. Evaluate the bound for $p = 30$, $k = 5$ and $e = 3$.

20. • In an HMM, a state with self-transition probability $a$ has runs of length $\ell$ with probability $a^{\ell - 1}(1 - a)$. Give the mean run length for $a = 0.999$ and the probability that a run is shorter than 50 bases. Explain why this shape is a poor model of exon lengths, and what the [generalized HMM](/generalized-hmm-gene-finder/) pays to replace it.

21. ★ For the $(15, 4)$ problem with 20 sequences of length 600, estimate the expected number of 15-mers other than the motif that lie within distance 4 of some window in every sequence. Then compute the expected number of pairs of windows from different sequences at distance at most 8, the edges that [WINNOWER](/winnower-algorithm/) must start from. Explain how the two numbers together make the problem hard.

22. ★ Prove that the information content of a column with probabilities $p$ against a background $q$ is at least 0, with equality only when $p = q$, and at most $\log_2(1/\min_a q(a))$. When is the upper bound reached?

23. ★ Score each window $x$ by the log-odds $S(x) = \sum_j \log_2(p_j(x_j)/q(x_j))$ of a motif with columns $p_j$ against a background $q$. Show that the expected score of a site drawn from the motif equals the information content of the motif, and that the expected score of a background window is $-\sum_j D(q \Vert p_j)$, which is at most 0.

24. ★ Show that the Gibbs motif sampler with pseudocount $b > 0$ and $q(a) > 0$ is an irreducible and aperiodic [Markov chain](/markov-chain/) on the starts $(t_1, \ldots, t_n)$. Give a small input and a start from which the sampler without pseudocounts can never reach some states.

25. ★ Prove that the smallest total distance of a string of length $L$ in the median string problem equals the smallest score $\sum_j (n - \max_a c_j(a))$ over choices of one window per sequence in the [motif finding problem](/motif-finding-problem/). Explain how an optimal solution of either problem gives one of the other.

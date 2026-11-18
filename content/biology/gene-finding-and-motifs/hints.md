1. The ATGs are at positions 2, 7 and 16. The ORFs are 7 to 15 (ATG GCC TAG) and 16 to 24 (ATG TTT TAA), both in the frame that starts at position 1. The ATG at position 2 reads ATG AAA TGG CCT AGA TGT TTT AAG and meets no stop.

3. $1$ bit, $2$ bits and $0.7 \log_2 2.8 + 0.3 \log_2 0.4 \approx 0.643$ bits. Against the second background the column gives $\log_2(1/0.3) \approx 1.737$ bits, less than 2 because A is already common.

4. Sort by right end and keep the best weight of a chain that ends at or before each exon. The best chain is $[1, 5]$, $[6, 8]$, $[9, 12]$, $[13, 18]$ with weight 15. The chain that starts with the heaviest exon, $[3, 9]$, $[10, 15]$, $[16, 20]$, reaches only 14.

8. $V = \sum_{i=0}^{4} \binom{15}{i} 3^i = 123{,}841$, so the probability is $123{,}841/4^{15} \approx 1.15 \times 10^{-4}$. Each sequence has 586 windows, so the 20 sequences hold about $20 \cdot 586 \cdot 1.15 \times 10^{-4} \approx 1.35$ such windows by chance, besides the planted ones.

10. Each frame of a million bases has about $333{,}333$ codons, so the six frames have about $2 \cdot 10^6 \cdot 3/64 = 93{,}750$ stops. A frame has at least 100 sense codons before its stop with probability $(61/64)^{100} \approx 0.0082$, so about 770 open frames that long arise by chance in every million bases.

11. Only the emissions of the seven C and G bases and the two state changes differ. Each C or G gains $\ln 1.5 \approx 0.405$ in the island state, and the two changes cost $2 \ln((1 - a)/a)$. For $a = 0.9$ the island path loses $4.394 - 2.838 = 1.556$, and for $a = 0.8$ it wins by $2.838 - 2.773 = 0.065$. A run of $k$ bases is marked when $k \ln 1.5 > 2 \ln(a/(1 - a))$: $k \ge 11$ for $a = 0.9$ and $k \ge 7$ for $a = 0.8$.

12. The profile of the other sites is $(c + 1)/7$ in each column. The windows `TAC`, `ACG`, `CGA`, `GAT` and `ATG` get the products $1$, $48$, $1$, $1$ and $32$ over $7^3$, and the background is the same for all, so the probabilities are $1/83$, $48/83$, $1/83$, $1/83$ and $32/83$.

15. The first step gives `ACG`, `CGG`, `CGG` and lowers the score from 4 to 2. The next profile picks the same windows, so the search stops at 2, although `ACG` occurs in all three sequences and gives score 0. A restart from another random start is needed to find it.

17. $p = \binom{13}{7}/\binom{18}{7} = 1716/31824 \approx 0.0539$ and $P = \Pr[\mathrm{Bin}(20, p) \ge 4] \approx 0.0204$, so $m = \lceil \ln 0.05 / \ln(1 - P) \rceil = 146$ trials. A bucket gets $20 \cdot 583 / 4^7 \approx 0.71$ random windows on average.

21. With $p = 123{,}841/4^{15}$, a fixed 15-mer is within 4 of some window of one sequence with probability $1 - (1 - p)^{586} \approx 0.065$, and of all 20 with probability $0.065^{20}$. Over all $4^{15}$ strings this gives about $2 \times 10^{-15}$, so the motif is the only answer. But the 190 pairs of sequences give $65{,}245{,}240$ pairs of windows, and a fraction $\sum_{i \le 8} \binom{15}{i} 3^i / 4^{15} \approx 0.057$ of them, about 3.7 million, are within 8. The 190 edges of the true clique hide among them.

22. The lower bound is Gibbs' inequality, from $\ln x \le x - 1$ applied to $q(a)/p(a)$. For the upper bound, $\sum_a p(a) \log_2(1/q(a)) \le \log_2(1/\min_a q(a))$ and the entropy of $p$ is at least 0. Both steps are tight when $p$ puts all its mass on one letter of smallest background probability.

23. Take expectations column by column. Under $p_j$ the expected term is $\sum_a p_j(a) \log_2(p_j(a)/q(a)) = D(p_j \Vert q)$, and under $q$ it is $-D(q \Vert p_j)$. Exercise 22 shows that each $D$ is at least 0.

24. With $b > 0$ every window has a positive sampling probability whatever the other sites are, so one sweep can reach any state, and the chance of keeping the current site makes the chain aperiodic. Without pseudocounts, take two copies of `ACGT` with $L = 2$ and start at (`AC`, `AC`). The profile of the other site is a point mass on `AC`, so the sampler never leaves this state and never reaches (`CG`, `CG`).

25. For fixed windows, the best string takes the most common letter of each column, and its total distance to the windows is the score. For a fixed string, each sequence contributes the distance to its closest window. Minimizing over both in either order gives the same value.

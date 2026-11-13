1. ◦ Score the alignment below with $s(a, a) = +2$ and $s(a, b) = -1$ for $a \ne b$, first with the [linear gap penalty](/linear-gap-penalty/) $d = 2$ per gap symbol, then with the [affine gap penalty](/affine-gap-penalty/) $g(L) = 3 + (L - 1) \cdot 1$.

   ```
   A C G G T A - C
   A - - G T A T C
   ```

2. ◦ The [BLOSUM62](/blosum-matrix/) matrix is in half-bit units. A pair of amino acids has score 4 and another has score $-2$. By what factor is each pair more or less frequent in related proteins than by chance, under the log-odds reading of a [substitution matrix](/substitution-matrix/)?

3. ◦ [Needleman-Wunsch](/needleman-wunsch/) aligns a sequence of 1000 letters with one of 500. How many cells does it fill? How many table entries does it keep if only the score is wanted, and about how many cells does [Hirschberg's algorithm](/hirschberg-algorithm/) compute to return the alignment?

4. ◦ A [banded alignment](/banded-alignment/) of two sequences of length 1000 keeps the cells $(i, j)$ with $|i - j| \le 10$, counting row and column 0. How many cells is that, and what fraction of the full table?

5. ◦ Find the best [local alignment](/local-alignment/) of ATTAGCG and AAGCGT with [Smith-Waterman](/smith-waterman/), using $+2$ for a match, $-1$ for a mismatch and $d = 2$. Give its score and the two substrings.

6. ◦ For DNA with uniform letters and the $\pm 1$ scheme, the [Karlin-Altschul statistics](/karlin-altschul-statistics/) give $\lambda = \ln 3$ and $K = 1/3$. A query of 1000 bases is compared with a database of $10^6$ bases. Compute the [E-value](/e-value/) and the P-value of an ungapped segment pair of score 20.

7. ◦ The database of a search doubles in size. What happens to the E-value of a hit with the same raw score? By how many [bits](/bit-score/) must the score rise to keep the E-value, and by how many raw points under the gapped BLOSUM62 parameters $\lambda = 0.267$, $K = 0.041$?

8. ◦ Compute the [sum-of-pairs score](/sum-of-pairs-score/) of the alignment below with match $+1$, mismatch $-1$, a letter against a gap $-2$ and a gap against a gap 0.

   ```
   A C G - T
   A - G C T
   A C G C -
   ```

9. ◦ A column of a DNA alignment of eight sequences holds A four times, C twice, G once and T once. Ignoring the small-sample correction, find the height of its stack in a [sequence logo](/sequence-logo/) and the height of each letter.

10. • Show that for uniform DNA and the $\pm 1$ scheme the equation $\sum_{a, b} p_a p_b e^{\lambda s(a, b)} = 1$ has the positive root $\lambda = \ln 3$. Then solve it for the scheme $+1/-2$, and find in both cases the fraction of identities $\sum_a q_{aa}$ in the target frequencies $q_{ab} = p_a p_b e^{\lambda s(a, b)}$ for which the scheme is the log-odds score.

11. • Under the $\pm 1$ DNA scheme of Exercise 6, a query of 1000 bases is searched against $10^9$ bases. What is the least integer score $S$ whose E-value is below 0.01?

12. • Find the best overlap of GATTACA and TACAGGT, a suffix of the first against a prefix of the second, with $+1$, $-1$ and $d = 1$. Fill the [semi-global table](/semi-global-dp/) with the zero border on the side of the first sequence, and read the answer in the last row.

13. • Run the first split of Hirschberg's algorithm on $x = $ ACGTC and $y = $ AGTAC with $+2$, $-1$ and $d = 2$. Compute the forward scores of $x_1 x_2$ against every prefix of $y$ and the backward scores of $x_3 x_4 x_5$ against every suffix of $y$, and find the column where the optimal path crosses the middle.

14. • Align AGGTCA with AGCA globally with $+2$ and $-1$, once with the linear penalty $d = 2$ and once with the affine penalty $g(L) = 4 + (L - 1)$ of [Gotoh's algorithm](/gotoh-algorithm/). Give the optimal scores and all optimal alignments in each case.

15. • Show that the number of global alignments of sequences of lengths $m$ and $n$ satisfies $D(m, n) = D(m - 1, n) + D(m, n - 1) + D(m - 1, n - 1)$ with $D(m, 0) = D(0, n) = 1$, where an alignment is a path in the [alignment graph](/alignment-graph/). Compute $D(3, 3)$.

16. • In a region of 10 aligned columns, each column is a match with probability $1/2$, independently. Find the probability that the contiguous seed 111 hits the region, and the same for the [spaced seed](/spaced-seed/) 1101 of the same weight. Do the same for 8 columns.

17. • List the $(w, k) = (3, 2)$ [minimizers](/minimizer/) of GATTACAGA under the lexicographic order $A < C < G < T$, with ties to the leftmost k-mer. What fraction of the k-mer positions does the sketch keep, compared with $2/(w + 1)$?

18. • Six fragments are given by their intervals in $x$ and $y$ and their weights: A $= ([1, 4], [2, 5], 4)$, B $= ([3, 8], [10, 15], 6)$, C $= ([6, 9], [6, 9], 4)$, D $= ([10, 14], [11, 15], 5)$, E $= ([12, 16], [1, 5], 5)$, F $= ([15, 18], [17, 20], 4)$. A fragment may follow another if it starts after the other ends in both sequences. Find the heaviest [colinear chain](/colinear-chaining/).

19. • Apply the [center-star method](/center-star-method/) to GATTACA, GATACA, GTTACA and GATTAC with unit edit costs. Which sequence is the center? Use the [bound](/center-star-approximation-bound/) to show that the star alignment costs at most 9, and use pairwise distances to show that every alignment costs at least 8.

20. • Build a [position-specific scoring matrix](/position-specific-scoring-matrix/) from ACG, ACT, AGG and TCG with one pseudocount per letter and background $1/4$, in bits. Score ACG, TGT and CCA.

21. ★ Let $s$ be a scoring matrix with $\sum_{a, b} p_a p_b s(a, b) < 0$ and $s(a, b) > 0$ for some pair with $p_a p_b > 0$. Prove that $\sum_{a, b} p_a p_b e^{\lambda s(a, b)} = 1$ has exactly one root $\lambda > 0$.

22. ★ Find an optimal local alignment, not only its score, in $O(mn)$ time and $O(m + n)$ space.

23. ★ Show that the optimal sum-of-pairs cost of A, C and AC under unit edit costs is 4, while the sum of the three pairwise edit distances is 3. So the lower bound $\mathrm{OPT} \ge \sum_{i < j} D(i, j)$ used to prune the exact [multiple alignment](/multiple-sequence-alignment/) program can be strict.

24. ★ Take a local alignment scheme with $s(a, a) = 1$, any mismatch scores, and gap penalty $d = 0$. Show that the best local score of two random uniform DNA sequences of length $n$ grows linearly in $n$, with a constant of at least $1/4$. Why does this rule out a logarithmic law like that of the Karlin-Altschul statistics for this scheme?

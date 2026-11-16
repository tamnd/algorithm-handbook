1. ◦ A query has four relevant documents: b and g of grade 2, c and k of grade 1. A run returns a, b, c, d, e, f, g, h, i, j in this order and does not return k. With binary relevance (grade at least 1), compute [precision at k](/precision-at-k/) for $k = 1, 3, 5, 10$, the [R-precision](/r-precision/) and the [recall](/precision-and-recall/) at rank 10.

2. ◦ For the run of exercise 1 with binary relevance, compute the [average precision](/mean-average-precision/) as an exact fraction and as a decimal.

3. ◦ For the run of exercise 1, compute the [interpolated precision](/interpolated-precision-recall-curve/) at the 11 recall levels $0, 0.1, \ldots, 1$ and their mean, using the exact recall levels (not trec_eval's rounding).

4. ◦ For the run of exercise 1, compute [nDCG](/normalized-discounted-cumulative-gain/) at 5 with the discount $1/\log_2(i + 1)$, once with the gain $g$ and once with the gain $2^g - 1$. Build the ideal ordering from all four relevant documents.

5. ◦ For the run of exercise 1, compute [ERR](/expected-reciprocal-rank/) on the scale with $g_{\max} = 2$, so that a document of grade $g$ satisfies with probability $(2^g - 1)/4$. Give the full ERR and ERR at 3 as fractions.

6. ◦ For the run of exercise 1 with binary gains, compute [rank-biased precision](/rank-biased-precision/) with $p = 0.8$. Nothing below rank 10 is judged. Give the residual and the interval that contains the RBP of every completion of the judgments.

7. ◦ Four queries each have at least one relevant document. A run puts its first relevant document at rank 1, 4 and 2 for the first three, and retrieves no relevant document for the fourth. Compute the [mean reciprocal rank](/mean-reciprocal-rank/).

8. ◦ For the query of exercise 1, only some documents are judged: b, c, g and k relevant, and a, e and h not relevant. The other documents are unjudged. Compute the [bpref](/bpref/) of the run in the form of the paper, which divides by $R$, and in the trec_eval form, which divides by $\min(N, R)$.

9. ◦ Run [balanced interleaving](/balanced-interleaving/) on $A = (p, q, r, s)$ and $B = (q, s, p, t)$. Give the shown list when $A$ moves first and when $B$ moves first. Then give the credit, for either list, when the user clicks only $s$, and when the user clicks $q$ and $r$.

10. • Show that if every query has a relevant document in the run, then $\mathrm{MRR} \ge 1/\bar r$, where $\bar r$ is the mean of the first relevant ranks, with equality only when all the ranks are equal. Then find two systems, each over two queries, that MRR and the mean first rank put in opposite orders. Use [Jensen's inequality](/jensens-inequality/).

11. • A run gives the scores u 3.0, v 2.0, w 2.0, x 2.0 and y 1.0, and only x and y are relevant. Compute the AP when ties are broken by id ascending, as in this area, when they are broken in reverse lexical order, as in trec_eval, and the tie-aware AP, the mean over the six orders of the tied group.

12. • On a scale from 0 to 3, the judged documents are a of grade 3, b and c of grade 2. Run X shows b, c and run Y shows a, e, where e is not relevant. Compute [nDCG](/normalized-discounted-cumulative-gain/) at 2 for both runs with the gain $g$ and with the gain $2^g - 1$. Which run wins under each gain?

13. • A ranking of six documents reads, from rank 1: relevant, unjudged, not relevant, relevant, unjudged, not relevant. Nothing below rank 6 is judged. With binary gains and $p = 1/2$, compute the [rank-biased precision](/rank-biased-precision/) of the judged documents, the residual and the interval.

14. • The relevant documents are a, b, c and d. Runs $A = (a, x, b, y, c)$ and $B = (b, a, y, z, d)$ build a [pool](/pooling/) of depth 2. Run $C = (c, w, d, a, b)$ is scored later. Compute the AP of each run on the pool judgments, with unjudged documents not relevant, and on the full judgments. How does the order of the three runs change?

15. • A query has $R = 3$ relevant documents $r_1, r_2, r_3$. Run $X = (r_1, n_1, n_2, n_3, r_2, r_3)$ and run $Y = (n_1, r_1, r_2, n_2, n_3, n_4)$, where the $n_i$ are not relevant. Compute the [average precision](/mean-average-precision/) and the [R-precision](/r-precision/) of both runs, and say which run each metric prefers.

16. • In the [C/W/L framework](/cwl-framework/), take the binary gains $1, 0, 1, 0, 0, \ldots$ with $R = 2$. For precision at 3 ($C(i) = 1$ for $i < 3$, else 0), RBP with $p = 1/2$, reciprocal rank ($C(i) = 1 - g_i$) and average precision ($C(i) = \sum_{j > i} g_j/j \,/ \sum_{j \ge i} g_j/j$), compute $C(1), C(2), C(3)$, the weights $W(1), W(2), W(3)$, the expected utility EU and the expected depth ED.

17. • Run [team-draft interleaving](/team-draft-interleaving/) on $A = (a, b, c, d)$ and $B = (b, a, c, d)$. List the shown list and the two teams for each of the four results of the two round coins. Compute the expected outcome when the user clicks only c, and when the user clicks a and c.

18. • Interleaving on 25 queries gives 16 wins for A, 5 for B and 4 ties. Compute the exact two-sided p-value of the [sign test](/sign-test/), with the ties left out. Is the difference significant at level 0.05?

19. • On a scale from 0 to 3, document a has grade 3 and b, c and d have grade 2. Run X shows a and two documents that are not relevant; run Y shows b, c, d. Compute [ERR](/expected-reciprocal-rank/) with $g_{\max} = 3$ and nDCG at 3 with both gains, and say which run each metric prefers.

20. • With $\alpha = 1/2$, documents x, y, z and w contain the nuggets $\{t_1, t_2\}$, $\{t_1\}$, $\{t_2, t_3\}$ and none. Compute the [alpha-nDCG](/alpha-ndcg/) gains of the ranking y, x, w, z, the greedy ideal ranking, and alpha-nDCG at 2 and at 4.

21. ★ Run the [minimal test collection](/minimal-test-collection/) algorithm on $A = (a, b, c)$ and $B = (c, a, b)$ with $p = 1/2$. Give the coefficients $c_{ij}$, the first bounds on $D = R(\mathrm{AP}(A) - \mathrm{AP}(B))$, and the scores that choose the first document. If only a is relevant, which documents are judged, and what are the final bounds?

22. ★ Take [alpha-nDCG](/alpha-ndcg/) with $\alpha = 1$, so that a nugget counts only the first time. Documents A, B and C contain the nuggets $\{2, 3, 4, 5\}$, $\{1, 2, 3\}$ and $\{4, 5, 6\}$. Compute the greedy ideal at depth 2 and its alpha-DCG, the best alpha-DCG at depth 2, and the alpha-nDCG at 2 of the ranking B, C with the greedy normalizer. Relate the ideal at depth $j$ to [maximum coverage](/max-coverage/).

23. ★ A run ranks a, b, c, the pool is $\{a, b, c\}$, and b and c are relevant. A sample of 2 pool documents is drawn uniformly. Compute [inferred AP](/inferred-average-precision/) for each of the three samples with $\varepsilon \to 0$, the mean over the samples and the true AP. What is the bias?

24. ★ In [probabilistic interleaving](/probabilistic-interleaving/) with $\tau = 3$ (weight $1/r^3$ for rank $r$), take $A = (a, b, c)$, $B = (b, a, c)$ and the shown list $L = (a, b, c)$. Compute the posterior probabilities $q_1, q_2, q_3$ that each position was drawn from $A$, and the marginalized outcome for clicks on positions 1 and 2, and for a click on position 2 only.

25. ★ Choose the persistence of [rank-biased precision](/rank-biased-precision/) so that the expected number of documents read is $n$. Show that the share of the total weight on ranks 1 to $n$ is $1 - (1 - 1/n)^n$, compute it for $n = 2, 5, 10$, and prove that it is larger than $1 - 1/e$ for every $n$ and tends to $1 - 1/e$. The [geometric distribution](/geometric-distribution/) gives the expected depth.

Several exercises use the toy collection of the entries. Its eight documents are $d_1$ = "binary search finds a key in a sorted array", $d_2$ = "merge sort merges two sorted runs into one sorted array", $d_3$ = "an inverted index maps each term to a posting list", $d_4$ = "a posting list is a sorted list of document ids", $d_5$ = "skip pointers speed up the merge of two posting lists", $d_6$ = "a hash table finds a key in constant expected time", $d_7$ = "search engines rank documents by a score for the query" and $d_8$ = "the sorted array of ids is compressed with gap encoding". They have 79 tokens in all; $d_1$ has 9 and the others 10, so avgdl $= 9.875$.

1. ◦ In the [Boolean model](/boolean-retrieval-model/), evaluate "sorted AND array AND NOT search" on the toy collection. Give the posting lists of the three terms and say in which order a query processor should intersect them.

2. ◦ With the [tf-idf](/tf-idf/) scheme ntn (raw term count times $\log_{10}(N/\mathrm{df})$, no normalization), compute the scores of $d_1$ and $d_2$ for the query "sorted array search". Document 2 holds "sorted" twice. Why does $d_1$ still score higher?

3. ◦ A query vector is $u = (1, 1)$ and two item vectors are $a = (3, 0)$ and $b = (1, 1)$. Rank the items by inner product and by cosine. Which of the two orders does a [dual encoder](/dual-encoder-retrieval/) trained with the inner product use at search time, and what does the norm of an item vector act as?

4. ◦ For the term "search" in $d_1$, compute the unsmoothed maximum likelihood estimate of $p(\text{search} \mid d_1)$, the [Jelinek-Mercer](/jelinek-mercer-smoothing/) estimate with $\lambda = 0.5$ on the collection model, and the [Dirichlet](/dirichlet-prior-smoothing/) estimate with $\mu = 10$. Then say what score the unsmoothed [query likelihood model](/query-likelihood-model/) gives $d_4$ for "sorted array search".

5. ◦ In the cost model of the [probability ranking principle](/probability-ranking-principle/), retrieving a non-relevant document costs $C_0 = 1$ and missing a relevant one costs $C_1 = 3$. Four documents have calibrated probabilities of relevance 0.6, 0.3, 0.2 and 0.1. How many should the system return?

6. ◦ With [reciprocal rank fusion](/reciprocal-rank-fusion/) and $k = 60$, document $x$ is at ranks 1 and 3 of two lists and document $y$ is at rank 2 in both. Which one is fused first? Answer the same question for $k = 0$.

7. ◦ One query has four documents with labels 2, 1, 1 and 0. How many preferred pairs do the [Ranking SVM](/ranking-svm/) and [RankNet](/ranknet/) use for it? What is the RankNet cost of this query with $\sigma = 1$ when all scores are 0?

8. ◦ In [unbiased learning to rank](/unbiased-learning-to-rank/), the examination propensity at rank $r$ is $1/r$. A logged ranking of five documents got clicks at ranks 1 and 4 only. Give the weight of each click and the inverse-propensity estimate of the number of relevant documents in the list. What does the estimate become if the propensity at rank 4 is wrongly taken as $1/2$?

9. ◦ A first stage returns 100 candidates per query, and a relevant document is among them for 70% of the queries. A [cross-encoder](/cross-encoder-reranking/) reranks the 100. What is the largest MRR@10 the reranked lists can reach, and how does their recall at depth 100 compare with that of the first stage?

10. • Compute the [BM25](/bm25/) scores for the query "key table" on the toy collection, with $k_1 = 1.2$, $b = 0.75$ and the idf $\ln(1 + (N - \mathrm{df} + 0.5)/(\mathrm{df} + 0.5))$. Which documents get a nonzero score, and in what order?

11. • In a collection with avgdl $= 10$, take BM25 with $k_1 = 1.2$ and $b = 0.75$. Compute the length factor $B(d) = 1 - b + b\,|d|/\mathrm{avgdl}$ for documents of 5 and 20 tokens, and the term frequency part $\mathrm{tf}(k_1 + 1)/(\mathrm{tf} + k_1 B(d))$ for $\mathrm{tf} = 2$ in each. What value does this part approach as tf grows? Relate $B(d)$ to [pivoted length normalization](/pivoted-length-normalization/).

12. • A collection has $N = 20$ documents, and a term occurs in $n = 5$ of them. Four documents are judged relevant, and three of those contain the term. Compute the Robertson-Sparck Jones weight of the [binary independence model](/binary-independence-model/), with the 0.5 corrections, and the weight the same formula gives with no judgments.

13. • In the [Rocchio algorithm](/rocchio-algorithm/) with $\alpha = 1$, $\beta = 0.75$ and $\gamma = 0.15$, the query is $q = (1, 0, 0, 0)$ over four terms, the judged relevant documents are $(0.6, 0.8, 0, 0)$ and $(0.6, 0, 0.8, 0)$, and the judged non-relevant document is $(0, 0.6, 0, 0.8)$. Compute the new query, with negative weights set to 0.

14. • Three voters rank four items as $(a, b, c, d)$, $(b, a, d, c)$ and $(c, b, a, d)$. Compute the [Borda count](/borda-count/) ranking, the [Kemeny](/kemeny-rank-aggregation/) ranking with its total [Kendall tau distance](/kendall-tau-distance/) to the three lists, and the total distance of each input list. Is there a Condorcet winner?

15. • Two lists rank three items as $(a, b, c)$ and $(c, b, a)$. Find every Kemeny-optimal ranking and its cost. Then show that for any two lists, either input list is a Kemeny-optimal ranking.

16. • Run MC4 of [Markov chain rank aggregation](/markov-chain-rank-aggregation/) on the three lists of Exercise 14: from item $P$, pick an item $Q$ uniformly among the four, and move to $Q$ if a majority of the lists rank $Q$ above $P$. What is the stationary distribution with no teleport? With the teleport $\varepsilon = 0.15$, what order does the stationary distribution give?

17. • Three documents are ranked in the order of their labels 0, 2, 1 (rank 1 holds label 0). With gain $2^y - 1$ and discount $1/\log_2(r + 1)$ and no cutoff, compute the nDCG of the ranking and the swap weight $|\Delta Z_{ij}|$ of [LambdaRank](/lambdarank/) for each of the three pairs with different labels. Which pair gets the largest push?

18. • A query has three documents with scores $(0, \ln 2, \ln 3)$ and labels $(0, 1, 2)$. Compute the [ListNet](/listnet/) top-one distributions $P_s$ and $P_y$ (softmax of the scores and of the labels), the gradient of the loss with respect to the scores, the loss, and its smallest possible value for these labels.

19. • A query has two token vectors $(1, 0)$ and $(0.6, 0.8)$. Document $D$ has the token vectors $(0.8, 0.6)$ and $(0, 1)$; document $E$ has the single token vector $(1, 0)$. Score both documents by the late interaction of [ColBERT](/colbert/), and by the inner product of the mean token vectors, as a single-vector dual encoder with mean pooling would. Do the two orders agree?

20. • In [retrieval-augmented generation](/retrieval-augmented-generation/), two passages have retriever probabilities $(0.5, 0.5)$, and the generator gives the target output the probabilities 0.2 and 0.6 given each passage. Compute $p_{\text{seq}}(y \mid x)$, the posterior over the two passages, and the gradient of $\log p_{\text{seq}}$ with respect to each retriever score.

21. ★ Show that as $k_1 \to \infty$, BM25 ranks documents by $\sum_t \mathrm{idf}(t)\, \mathrm{tf}(t, d) / B(d)$, and that as $k_1 \to 0$ it ranks them by the sum of the idf values of the query terms they contain. Name the earlier model that each limit gives.

22. ★ Suppose the relevance of the documents is independent and document $d$ is relevant with probability $p_d$. Prove that sorting by $p_d$ maximizes the expected reciprocal rank of the first relevant document. Then let $A$ and $B$ be copies, relevant together with probability 0.5, and let $C$ be independent and relevant with probability 0.4. Compute the expected reciprocal rank of the orders $A, B, C$ and $A, C, B$.

23. ★ For the three lists of Exercise 14, find every ranking that minimizes the total [Spearman footrule](/spearman-footrule/) distance to the lists, with positions counted from 1. Give the Kendall cost of each, and compare it with the Kemeny cost and with the factor-2 bound for footrule aggregation.

24. ★ [RankBoost](/rankboost/) starts from the uniform distribution over $P = 1000$ preferred pairs, and every round has $r_t \ge 0.2$. Using $\mathrm{rloss} \le \exp(-\frac{1}{2} \sum_t r_t^2)$, find the number of rounds after which no training pair can be misordered.

25. ★ A dual encoder of dimension 2 has the four item vectors $a = (1, 0)$, $b = (2, 0)$, $c = (0, 1)$ and $d = (0, 2)$. Count the strict orders of the four items that some query vector produces, and compare the count with the bound $N(N - 1)$ for $N$ items in dimension 2.

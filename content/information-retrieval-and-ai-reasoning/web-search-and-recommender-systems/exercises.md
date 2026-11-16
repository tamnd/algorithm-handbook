1. ◦ A crawl must fetch 5 pages of host a, with a gap of 2 seconds between the starts of fetches to a, and 3 pages of host b, with a gap of 5 seconds. Each fetch takes 0.5 seconds. Give the lower bound of the [web crawling](/web-crawling/) entry on the time from the first fetch to the end of the last one. How many machines do you need to reach it?

2. ◦ A directed graph has the nodes 0 to 9 and the edges 0→1, 1→2, 2→3, 3→1, 2→4, 5→1, 5→6, 5→9, 9→4 and 7→4. Split it into the parts of the [bow-tie](/bow-tie-web-structure/): CORE, IN, OUT, TENDRILS (with tubes) and DISCONNECTED. Which pages does a crawl from seed 0 find, and which does a crawl from seed 5 miss?

3. ◦ A page changes as a Poisson process with rate 2 per day and is refetched every half day, in a fixed order. Using the [crawl revisit policy](/crawl-revisit-policy/) entry, give its expected freshness, its freshness if it were refetched at random times at the same average rate, and its mean age.

4. ◦ In the optimal [link farm](/link-spam/) with damping $\alpha = 0.85$, no links from outside, and scores multiplied by the number of pages $n$, how many boosting pages does the target need to reach 10 times the average score?

5. ◦ A query log holds "car" 50 times, "cart" 30, "card games" 25, "care" 10 and "cat" 40. What does [most popular completion](/most-popular-completion/) return for the prefix "car" with $k = 3$? If each completion of "car" is meant with probability proportional to its count, what are the success rate and the expected reciprocal rank of that list?

6. ◦ Four candidates have relevance 0.9, 0.85, 0.6 and 0.5, and the similarities $s(d_1, d_2) = 0.95$, $s(d_1, d_3) = 0.1$, $s(d_1, d_4) = 0.2$, $s(d_2, d_3) = 0.2$, $s(d_2, d_4) = 0.1$ and $s(d_3, d_4) = 0.3$. Run [maximal marginal relevance](/maximal-marginal-relevance/) for $k = 3$ with $\lambda = 0.5$ and with $\lambda = 0.7$. Above which $\lambda$ does $d_2$ come second?

7. ◦ A query has two intents, car with probability 0.6 and animal with 0.4. Document $d_1$ satisfies car with probability 0.9, $d_2$ satisfies car with 0.8, and $d_3$ satisfies animal with 0.9; no document satisfies the other intent. Run [IA-Select](/ia-select/) for $k = 3$ and give the objective after each pick. Is the greedy pair optimal for $k = 2$?

8. ◦ In the [cascade model](/cascade-click-model/), a list shows documents with attractiveness 0.3, 0.6 and 0.5, in that order. Give the probability of a click at each rank, the probability of no click, and the expected number of results the user examines.

9. ◦ Under the [position-based model](/position-based-click-model/) with $\gamma_1 = 1$ and $\gamma_3 = 0.3$, a document was shown 1000 times at rank 1 and clicked 250 times, and shown 1000 times at rank 3 and clicked 75 times. Give its raw click rate and its estimate weighted by inverse propensity. Why does the second need the documents to have moved between ranks?

10. ◦ On the toy matrix of the [recommendation problem](/recommendation-problem/) entry, predict the rating of $u_4$ for $i_1$ with [Slope One](/slope-one/) and with weighted Slope One.

11. • Two documents read "the cat sat on the mat" and "the cat sat on a mat". Give the Jaccard resemblance of their sets of 2-word shingles and of their sets of words. With 200 independent [MinHash](/minhash/) values, what is the standard deviation of the estimate of the first? Two documents whose feature vectors have cosine 0.9 get 64-bit [SimHash](/simhash/) fingerprints; how many bits do they differ in, on average? Would they pass the threshold of 3 bits used for web pages in the [near-duplicate detection](/near-duplicate-document-detection/) entry?

12. • A query graph has the links 0→3, 0→4, 1→3, 2→4, 2→5, 6→7 and 8→7. Compute the [SALSA](/salsa-algorithm/) authority and hub scores from its closed form, and the [HITS](/hits-algorithm/) authority scores scaled to sum 1. Explain why page 7, with two in-links, gets a positive SALSA score but HITS score 0.

13. • Run [TrustRank](/trustrank/) on the links 0→1, 1→0, 1→2, 2→0, 2→3, 3→4 and 4→3 with the single seed 0 and $\alpha = 17/20$. Find the fixed point exactly. Pages 3 and 4 form a spam farm: check that their trust meets the bound $\frac{\alpha}{1 - \alpha} X$ of the entry with equality, and say why.

14. • The [noisy channel spelling corrector](/noisy-channel-spelling-correction/) sees "possting". Its error log has the insertion counts ins[o, s] = 1 and ins[s, s] = 2, the corpus has count[o] = 25 and count[s] = 35, and "posting" occurs 3 times among 79 tokens. Give $P(\text{possting} \mid \text{posting})$ and the score of "posting". Why are there two terms?

15. • In the example of the [xQuAD](/xquad/) entry, find the exact value of $\lambda$ above which d3 rather than d2 is placed second. What does the tie rule do at that value?

16. • The cascade model is fitted to six sessions on the documents a, b and c: (a, b, c) with a click on a; (a, b, c) with a click on b; (a, b, c) with no click; (b, a, c) with a click on b; (b, a, c) with a click on a; (b, a, c) with a click on c. Give the maximum likelihood estimates of the three attractiveness values and the raw click rates. Why do they differ?

17. • In the example of the [SLIM](/sparse-linear-method/) entry, keep $\beta = 0.5$ and compute column $i_2$ of $W$ as a function of $\lambda$. For which $\lambda$ is the column all zero? Check the KKT condition for $w_{42}$.

18. • Take [matrix factorization](/matrix-factorization-recommendation/) without biases, with $r = 1$, a known rating 4, $p_u = 1$, $q_i = 2$, step $\gamma = 0.1$ and $\lambda = 0.5$. Do one SGD step, updating $p_u$ and $q_i$ at the same time, and give the new prediction. Then do one [ALS](/alternating-least-squares/) user step with $r = 2$ for a user who rated items with factors $(1, 0)$ and $(1, 1)$ as 3 and 5, with $\lambda = 1$ and the plain penalty.

19. • A [factorization machine](/factorization-machine/) has $k = 2$, input $x = (1, 1, 0, 2)$ and factor vectors $v_1 = (1, 0)$, $v_2 = (0, 1)$, $v_3 = (5, 5)$, $v_4 = (1, 2)$. Compute its pairwise term directly and by the linear-time identity. Which vector plays no part, and why?

20. • For $n = 4$, compute the coherence of the column space spanned by $(1, 1, 1, 1)$ and of the one spanned by $e_1$. The matrix $e_1 e_1^\top$ is observed in every entry except $(1, 1)$. What does nuclear-norm minimization return, and which hypothesis of the [exact completion theorem](/exact-matrix-completion-theorem/) fails?

21. • Do one [BPR](/bayesian-personalized-ranking/) step without regularization on the triple $(u, i, j)$ with $w_u = (1, 0)$, $h_i = (0, 1)$, $h_j = (1, 0)$ and step 0.1. Give the margin and the loss $-\ln \sigma(x_{uij})$ before and after.

22. • For one user step of [weighted ALS](/implicit-feedback-als/) over all users, count the operations to build the matrices $Y^\top C^u Y$ directly and with the identity $Y^\top C^u Y = Y^\top Y + Y^\top (C^u - I) Y$. Evaluate both for $10^6$ users, $10^5$ items, $10^8$ nonzero counts and $r = 100$, including the $r^3$ solves.

23. • In [SASRec](/sasrec/), how many pairs $(t, u)$ does the causal mask allow in one sequence of length $n$, and how many does it block? For $n = 200$ and $d = 50$, which of the two terms $n^2 d$ and $n d^2$ of the cost is larger, and by what factor?

24. ★ Under purely random refreshing, a page with change rate $\lambda$ refetched at rate $f$ is fresh with probability $f/(f + \lambda)$. Prove that uniform allocation of a total rate $F$ beats proportional allocation. Then find the optimal allocation, and evaluate it for change rates 9 and 1 with $F = 2$.

25. ★ Give an instance of IA-Select with $k = 2$ on which the greedy list is strictly worse than the optimum, whatever the tie rule, with a ratio that tends to $3/4$. Which bound does this show to be tight?

26. ★ In the [DBN click model](/dbn-click-model/) with attractiveness $a_d$, satisfaction $s_d$ and perseverance $\gamma$, prove that $P(E_{i+1} = 1) = \gamma (1 - a_{d_i} s_{d_i}) P(E_i = 1)$. Deduce the click probability at each rank, and show that $\gamma = 1$ and $s \equiv 1$ give the cascade formula. Evaluate for $a = (0.6, 0.5, 0.4)$, $s = (0.5, 0.2, 0.3)$ and $\gamma = 0.8$.

27. ★ Sample each entry of the $n \times n$ all-ones matrix independently with probability $p$. Show that if some row has no sampled entry, the rank-1 completion is not unique. Show that the probability that no row is empty is at most $\exp(-n (1 - p)^n)$, and conclude that about $n \ln n$ samples are needed for [matrix completion](/matrix-completion/). Evaluate for $n = 1000$ and $p = (\ln n - 2)/n$.

28. ★ The weighted ALS objective sums $c_{ui}(p_{ui} - x_u^\top y_i)^2$ over all $m n$ cells, plus the penalty. Show how to compute it exactly in $O(s r + (m + n) r^2)$ time, where $s$ is the number of nonzero counts.

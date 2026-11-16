## What to remember

- **A crawl is a polite graph search.** With a gap $\delta(h)$ between fetches to host $h$, a crawl of $n_h$ pages per host takes at least $\max_h (n_h - 1)\,\delta(h)$ time, whatever the number of machines. The [URL frontier](/url-frontier/) hands out each URL once and provably keeps every gap.
- **Freshness has a formula.** A page that changes as a Poisson process with rate $\lambda$ and is refetched at frequency $f$ is fresh a fraction $(1 - e^{-r})/r$ of the time, with $r = \lambda / f$. Refreshing all pages equally often provably beats refreshing in proportion to their change rates.
- **Link scores can be forged, and some defences are proved.** An optimal [link farm](/link-spam/) with $k$ boosting pages gives its target $x/(1 - \alpha^2) + (1 + \alpha k)/((1 + \alpha) n)$. [TrustRank](/trustrank/) is personalized PageRank from hand-checked good seeds. A set of pages without a seed holds at most $\alpha/(1 - \alpha)$ times the trust that links carry into it; that good pages seldom link to spam is an observation, not a theorem.
- **Diversification is NP-hard, and greedy is the method.** [IA-Select](/ia-select/) maximizes a monotone submodular objective, so its greedy list reaches at least $1 - (1 - 1/k)^k > 1 - 1/e$ of the best value under its model of intents. [MMR](/maximal-marginal-relevance/) has no such guarantee, and all their gains are measured.
- **A click needs examination and attraction.** In the [cascade model](/cascade-click-model/), $P(C_i = 1) = \alpha_{d_i} \prod_{j < i} (1 - \alpha_{d_j})$, and the maximum likelihood estimate is clicks over sessions in which the document was examined. The [position-based model](/position-based-click-model/) has $P(C_r = 1) = \gamma_r \alpha_d$, identified only up to scale and only if documents move between ranks. Click models are fitted models, judged on held-out logs.
- **Neighborhood predictions differ in what they keep.** [User-based](/user-based-collaborative-filtering/) prediction $\mu_u + \sum_v w_{uv}(r_{vi} - \mu_v) / \sum_v |w_{uv}|$ can leave the rating scale. [Item-based](/item-based-collaborative-filtering/) prediction with positive weights is a convex combination and cannot.
- **Matrix factorization is nonconvex.** Fitting even a rank-one matrix to a partly known matrix is NP-hard. Each [ALS](/alternating-least-squares/) half step is an exact ridge solve, so the objective never increases, but only stationarity of limit points is proved. Exact recovery by nuclear-norm minimization needs incoherence and about $32 \max\{\mu_1^2, \mu_0\}\, r (n_1 + n_2) \log^2 n_2$ uniformly random entries; real ratings are not missing at random.
- **Implicit feedback changes the loss, not the factor model.** Weighted ALS counts every blank cell as a weak zero and still costs $O(s r^2 + (m + n) r^3)$ per sweep, thanks to $Y^\top C^u Y = Y^\top Y + Y^\top (C^u - I) Y$. [BPR](/bayesian-personalized-ranking/) maximizes a smooth lower bound on each user's AUC. Careful reruns found tuned simple baselines competitive with the neural models.

## The main methods side by side

| Method | Time | What is guaranteed |
|---|---|---|
| [URL frontier](/url-frontier/) | $O(F)$ per add, $O(\log B)$ per next, amortized | each URL once; politeness gaps kept |
| [TrustRank](/trustrank/) | $O(M (n + m) + n \log n)$ | unique fixed point; error $\le 2 \alpha^M$ after $M$ rounds |
| [Most popular completion](/most-popular-completion/) | $O(m + kL \log(kL))$ per prefix | exact top $k$ by log frequency |
| [MMR](/maximal-marginal-relevance/) | $O(n \log n + nk)$ | none |
| [IA-Select](/ia-select/) | $O(n \log n + nkm)$ | $1 - 1/e$ of the optimum under its model |
| [User-based filtering](/user-based-collaborative-filtering/) | $O(mn)$ per prediction | none; may leave the scale |
| [Item-based filtering](/item-based-collaborative-filtering/) | build $O(ns + n^2 \log n)$, predict $O(k)$ | prediction inside the scale |
| [Matrix factorization](/matrix-factorization-recommendation/), SGD | $O(Esr)$ | expected step is a gradient step |
| [ALS](/alternating-least-squares/), [weighted ALS](/implicit-feedback-als/) | $O(T(sr^2 + (m + n) r^3))$ | objective never increases |
| [BPR](/bayesian-personalized-ranking/) | $O(Tr + (m + n) r)$ | unbiased stochastic gradient steps |

: The main methods of the chapter, with the letters of each entry: for TrustRank, $n$ pages and $m$ links; for the recommenders, $m$ users, $n$ items, $s$ known ratings and $r$ factors. Gains in quality are all measured; the last column lists only what the entries prove.

## Choosing a method

- For a first recommender, fit the bias model $\mu + b_u + b_i$, then item-based filtering, then matrix factorization by ALS or SGD. Compare them on a held-out split: RMSE for ratings, a ranking measure for lists.
- With clicks, plays or purchases, use weighted ALS or BPR, not an explicit-rating method on zero-filled data.
- For new users and items, add content features through a hybrid or a factorization machine. Before adopting a neural model, tune a simple baseline on the same split; offline gains may differ from online results.

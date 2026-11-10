## What to remember

- A **sampling design** is a law on subsets. Uniform $k$-subsets, Bernoulli, systematic, stratified and PPS designs differ in which subsets they can produce, but the Horvitz-Thompson estimator is unbiased for each of them once the inclusion probabilities are known and positive.
- **To choose $k$ of $n$ items**, scan with probability (still needed)/(still left) when $n$ is known and the order must be kept; use [Floyd's algorithm](/floyd-sampling/) with $k$ draws when $n$ is huge and items have indices; use a [reservoir](/reservoir-sampling/) when $n$ is unknown. Algorithm R makes $k(H_n - H_k)$ replacements in expectation.
- **Skipping** draws how many items will be passed over, instead of one decision per item. It turns Bernoulli sampling into $\Theta(1 + np)$ expected time, and reservoir sampling into $O(k(1 + \log(n/k)))$ with [Algorithm L](/algorithm-l/) or Vitter's Algorithm Z.
- **Inversion** returns $F^{-1}(U)$ and works for every law on the line, with one uniform per variate. **Rejection** keeps a proposal $Y$ from $g$ when $U\,M g(Y) \le f(Y)$; the output is exact and the number of tries is geometric with mean $M$.
- **Normal variates** come from two uniforms by [Box-Muller](/box-muller-transform/), from a point in the unit disk by the [polar method](/marsaglia-polar-method/), which accepts with probability $\pi/4$, or from the [ziggurat](/ziggurat-method/), where about 97% of tries with 128 layers need no $\ln$, $\exp$ or square root.
- **Weighted sampling** with replacement takes $O(1)$ per draw with the [alias method](/alias-method/). Without replacement, successive sampling and proportional inclusion are different laws. Random keys $u^{1/w}$, or Gumbel noise on $\ln w$, give successive sampling by keeping the largest keys.
- **Samples estimate.** Importance weights $p/q$ correct for drawing from the wrong law; the [Karp-Luby estimator](/karp-luby-estimator/) needs $O(m \log(1/\delta)/\varepsilon^2)$ samples for a union of $m$ sets; and for self-reducible problems almost uniform sampling and approximate counting are polynomially equivalent.

## The main methods side by side

| Method | Problem | Setup | Cost | Random numbers |
|---|---|---|---|---|
| [Selection sampling](/selection-sampling/) | $k$ of $n$, $n$ known, in order | none | $\Theta(n)$ worst | one per item looked at |
| [Floyd's algorithm](/floyd-sampling/) | $k$ of $n$, by index | none | $\Theta(k)$ expected | exactly $k$ |
| [Algorithm R](/reservoir-sampling/) | $k$ of a stream | none | $\Theta(n)$ | $n - k$ |
| [Algorithm L](/algorithm-l/) | $k$ of a stream | none | $O(k(1 + \log(n/k)))$ expected | $2 + 3k(H_n - H_k)$ expected |
| [Bernoulli sampling](/bernoulli-sampling/), skips | each item with probability $p$ | none | $\Theta(1 + np)$ expected | one per kept item, plus one |
| [Inversion](/inverse-transform-sampling/), discrete | one index by weight | $\Theta(n)$ prefix sums | $O(\log n)$ by binary search | one |
| [Alias method](/alias-method/) | one index by weight | $\Theta(n)$ | $\Theta(1)$ | two |
| [Weighted reservoir](/weighted-reservoir-sampling/), A-Res | $k$ by weight, one pass | none | $O(n \log k)$ | one per item |
| [Box-Muller](/box-muller-transform/) | two normals | none | $\Theta(1)$ | two |
| [Polar method](/marsaglia-polar-method/) | two normals | none | $\Theta(1)$ expected | $8/\pi \approx 2.55$ expected |

: Methods of the chapter by problem. "Cost" is the time per sample, or per stream of $n$ items for the stream methods, with a skip counted as $O(1)$.

## Choosing a method

To pick a fixed number of items, the deciding questions are whether $n$ is known and whether the items can be reached by index. A known list that must stay in order calls for selection sampling; a huge range of indices calls for Floyd's algorithm; a stream calls for a reservoir, with Algorithm L when random numbers are costly or skipping is cheap. If the sample size may vary, Bernoulli sampling with skips is the simplest and merges trivially.

For draws by weight, build an alias table when the weights are fixed and many draws are needed. Use prefix sums and binary search when the weights change rarely and the table must be simple, and keys with a heap when the weights arrive as a stream. When weights come as logarithms, the Gumbel-max trick avoids overflow.

For a continuous law, use inversion when $F^{-1}$ has a closed form or the output must be a monotone function of $U$, as in stratified, Latin hypercube or quasi-Monte Carlo designs. Otherwise use rejection with a tight envelope; for very many normal or exponential variates, the ziggurat repays its table setup. When only an estimate is needed and no good envelope exists, weight the samples with importance sampling instead.

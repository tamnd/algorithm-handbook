## What to remember

- **A causal effect is a contrast of potential outcomes**, and only one outcome per unit is seen. The average effect can be identified; the law of the unit effects, and so their median or variance, in general cannot.
- **Randomization identifies the average effect with no model.** The difference in means is exactly unbiased for the ATE in finite samples. Neyman's variance estimate is conservative, by $S_\tau^2/n$ in expectation. A Fisher randomization test is exact, but only for the sharp null of no effect for any unit.
- **Design reduces variance before the analysis starts.** Blocks, Latin squares and a pre-period covariate (as in CUPED) remove nuisance variation. Factorial designs estimate every effect with all the runs, and fractions trade high-order interactions for runs, as their resolution records.
- **Simultaneous inference needs its own multiplier.** Tukey's method is exact for all pairs in balanced normal data and conservative for unequal sizes. Scheffé's is exact for all contrasts, including those picked after seeing the data.
- **Without randomization every method rests on an assumption the data cannot fully check:** ignorability with overlap for weighting, matching and AIPW; parallel trends for difference in differences; relevance, exclusion and monotonicity for instruments; continuity at the cutoff for regression discontinuity. Overlap, pre-trends and the first stage can be inspected; the core assumption cannot.
- **Identification comes before estimation.** Doubly robust estimators, double machine learning and TMLE estimate an identified effect well. They do not make an effect identified, and their guarantees are asymptotic, under product-rate conditions on the nuisance errors.
- **An instrument estimates the effect for compliers**, not for everyone, and a weak instrument makes the usual intervals wrong. The Anderson-Rubin set stays valid however weak the instrument is: exactly so under normal errors, approximately otherwise.
- **Causal discovery returns a class of graphs** under the causal Markov and faithfulness assumptions. PC and GES return the Markov equivalence class and assume no hidden common causes; FCI allows them and returns a partial ancestral graph. LiNGAM identifies the whole DAG by assuming linear structure and non-normal errors.

## Methods side by side

| Method | Main assumption | What it estimates | Guarantee |
|---|---|---|---|
| [Randomized experiment](/randomized-experiment/) | random assignment, SUTVA | ATE | exactly unbiased |
| [Inverse probability weighting](/inverse-probability-weighting/) | ignorability, overlap, right $e(x)$ | ATE | unbiased with known $e$; consistent with fitted $e$ |
| [Propensity score matching](/propensity-score-matching/) | ignorability, overlap | usually ATT | consistent; standard errors must allow for the estimated score, and the plain bootstrap fails with replacement |
| [AIPW](/augmented-inverse-probability-weighting/), [DML](/double-machine-learning/), [TMLE](/targeted-maximum-likelihood-estimation/) | ignorability, overlap | ATE | consistent if either model is right; asymptotically normal under rate conditions |
| [Difference in differences](/difference-in-differences/) | parallel trends, no anticipation | ATT | unbiased in the 2-by-2 case; staggered two-way fixed effects can mislead |
| [Synthetic control](/synthetic-control-method/) | good pre-period fit, no spillover | effect on one treated unit | placebo p-value valid only under exchangeability |
| [IV](/instrumental-variables-estimation/) and [2SLS](/two-stage-least-squares/) | relevance, exclusion, monotonicity | LATE | consistent; biased toward OLS with weak instruments |
| [Regression discontinuity](/regression-discontinuity-design/) | continuity at the cutoff | effect at the cutoff | local linear bias of order $h^2$ |
| [Front-door criterion](/front-door-criterion/) | graph conditions on a mediator | ATE | exact identification |
| [PC](/pc-algorithm/) and [GES](/greedy-equivalence-search/) | Markov, faithfulness, no hidden causes | equivalence class | correct with a perfect oracle or in the limit |

: The main causal methods of the chapter. "Consistent" and "asymptotically normal" are statements about large samples; only the randomized experiment and Horvitz-Thompson weighting with known propensities are unbiased in finite samples.

## Choosing a method

Randomize when you can. Then use the difference in means, adjust for a pre-treatment covariate to cut the variance, and block on what you know affects the outcome.

- To screen many factors in few runs, use a [fractional factorial](/fractional-factorial-design/) or a [Plackett-Burman design](/plackett-burman-design/); to find an optimum, follow with [response surface methodology](/response-surface-methodology/). For an irregular region or model, search for a D-optimal design with the [Fedorov exchange algorithm](/fedorov-exchange-algorithm/) and check it with the [Kiefer-Wolfowitz theorem](/kiefer-wolfowitz-equivalence-theorem/).
- With observational data and rich covariates, check overlap first, then use AIPW with cross-fitting, and report a [sensitivity analysis](/rosenbaum-sensitivity-analysis/).
- With a policy change and untreated comparison units observed over time, use difference in differences, or synthetic control when there is one treated unit.
- With a variable that shifts treatment but plausibly not the outcome, use instrumental variables and report the first-stage F and an Anderson-Rubin set.
- With treatment set by a threshold on a score, use regression discontinuity and check the density of the score at the cutoff.

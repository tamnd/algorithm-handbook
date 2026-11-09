Sort a million distinct keys with [quicksort](/quicksort/) that picks each pivot at random. The number of comparisons is not fixed: run the program twice on the same input and the counts differ. Yet the count stays close to its mean, about 24.8 million, on nearly every run, and the chance that one run needs twice as many is far below one in a million. Nothing about the input causes this. A sorted array, a reversed one and a random one get the same guarantee, because the randomness is in the algorithm's choices, not in the data.

Statements of this kind need two things. The first is an expected value: the [expected running time](/quicksort-expected-running-time/) of randomized quicksort is $2(n+1)H_n - 4n$ comparisons, where $H_n$ is the $n$-th harmonic number. The second is a tail bound, which says how unlikely a run much slower than the mean is. This chapter gives the probability needed for both. It starts from the definition of a probability space and ends with the inequalities that research papers on randomized algorithms use: the Chernoff bound, martingales and the Lovász local lemma.

The same tools serve a second purpose. An algorithm without random choices can be analyzed on random inputs, and the result is its average-case cost. [Insertion sort](/insertion-sort/) does about $n^2/4$ swaps on a random permutation, and a [hash table](/hash-table/) with a random hash function has a short chain at every key in expectation. The chapter treats both uses together, since the mathematics is the same.

## What the chapter covers

The chapter is in eight groups, read in order.

1. **Probability spaces and events.** The [probability space](/probability-space/), [conditional probability](/conditional-probability/), [independent events](/independent-events/), and distributions on finite and countable sets. The [Monty Hall problem](/monty-hall-problem/) tests the definitions.
2. **Random variables and distributions.** [Random variables](/random-variable/), [Bernoulli trials](/bernoulli-trials/), and the [binomial](/binomial-distribution/), [geometric](/geometric-distribution/), [Poisson](/poisson-distribution/) and [uniform](/uniform-distribution/) distributions.
3. **Expectation.** The [expected value](/expected-value/), [indicator random variables](/indicator-random-variable/), [linearity of expectation](/linearity-of-expectation/), [variance](/variance/), [Jensen's inequality](/jensens-inequality/) and [conditional expectation](/conditional-expectation/).
4. **The expected cost of an algorithm.** [Average-case analysis](/average-case-analysis/), the [hiring problem](/hiring-problem/), the expected cost of randomized quicksort, and [smoothed analysis](/smoothed-analysis/).
5. **Tail bounds.** [Markov's](/markov-inequality/) and [Chebyshev's](/chebyshev-inequality/) inequalities, the [union bound](/union-bound/), the [law of large numbers](/law-of-large-numbers/) and the [central limit theorem](/central-limit-theorem/).
6. **Four random processes.** The [coupon collector](/coupon-collector-problem/), the [birthday paradox](/birthday-paradox/), [balls into bins](/balls-into-bins/) and the [longest streak](/streaks/) of heads.
7. **Exponential tail bounds.** The [moment generating function](/moment-generating-function/), the [Chernoff bound](/chernoff-bound/), [Hoeffding's inequality](/hoeffding-inequality/) and the meaning of [with high probability](/high-probability-bounds/).
8. **Martingales and dependent events.** [Martingales](/martingale/), the [optional stopping theorem](/optional-stopping-theorem/), [Wald's equation](/walds-equation/), the [Azuma-Hoeffding inequality](/azuma-inequality/) and the [Lovász local lemma](/lovasz-local-lemma/).

## A first reading

For a first reading, take these entries in order: [probability space](/probability-space/), [conditional probability](/conditional-probability/), [independent events](/independent-events/), [random variable](/random-variable/), [geometric distribution](/geometric-distribution/), [expected value](/expected-value/), [indicator random variable](/indicator-random-variable/), [linearity of expectation](/linearity-of-expectation/), [hiring problem](/hiring-problem/), [expected running time of randomized quicksort](/quicksort-expected-running-time/), [Markov's inequality](/markov-inequality/), [union bound](/union-bound/), [birthday paradox](/birthday-paradox/) and [Chernoff bound](/chernoff-bound/). These are enough for most of the randomized algorithms in the handbook. The continuous distributions, the central limit theorem and the last group can wait until an entry needs them.

## Before you start

The chapter assumes counting with [binomial coefficients](/binomial-coefficient/), sums such as the [geometric series](/geometric-series/) and the [harmonic series](/harmonic-series/) from Chapter 1.2, and the limit $(1 - 1/n)^n \to e^{-1}$. A few entries use integrals for continuous distributions, and the proofs of the exponential bounds use the inequality $1 + x \le e^x$. No earlier course in probability is needed: the first group starts from the definitions.

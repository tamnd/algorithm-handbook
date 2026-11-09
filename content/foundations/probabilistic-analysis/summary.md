## What to remember

- [Conditional probability](/conditional-probability/) is $\Pr[A \mid B] = \Pr[A \cap B]/\Pr[B]$. Events are [independent](/independent-events/) when $\Pr[A \cap B] = \Pr[A]\Pr[B]$; for more than two events, pairwise independence does not imply mutual independence.
- [Linearity of expectation](/linearity-of-expectation/), $\mathbb{E}[X + Y] = \mathbb{E}[X] + \mathbb{E}[Y]$, needs no independence. Write a count as a sum of [indicators](/indicator-random-variable/) and add the probabilities: $H_n$ hires in the [hiring problem](/hiring-problem/), $2(n+1)H_n - 4n$ comparisons in [randomized quicksort](/quicksort-expected-running-time/), where the keys of ranks $i < j$ are compared with probability $2/(j - i + 1)$.
- A [geometric](/geometric-distribution/) variable with success probability $p$ has mean $1/p$. The [coupon collector](/coupon-collector-problem/) needs $nH_n \approx n \ln n$ draws on average, a sum of $n$ geometric waits.
- [Markov](/markov-inequality/): $\Pr[X \ge a] \le \mathbb{E}[X]/a$ for $X \ge 0$. [Chebyshev](/chebyshev-inequality/): $\Pr[|X - \mu| \ge a] \le \mathrm{Var}(X)/a^2$. Variances add for independent, and even for pairwise independent, variables.
- The [union bound](/union-bound/), $\Pr[\bigcup A_i] \le \sum \Pr[A_i]$, holds for any events. A bound that fails with probability $n^{-c}$ survives a union over $n^{c-1}$ events: this is why results hold [with high probability](/high-probability-bounds/).
- About $\sqrt{2n \ln 2} \approx 1.18\sqrt n$ random draws from $n$ values give a repeat with probability $1/2$ (the [birthday paradox](/birthday-paradox/)). With $n$ [balls in $n$ bins](/balls-into-bins/), a fraction about $1/e$ of the bins stays empty and the fullest bin has $\Theta(\log n / \log\log n)$ balls with high probability.
- [Chernoff](/chernoff-bound/): a sum of independent 0/1 variables with mean $\mu$ satisfies $\Pr[X \ge (1+\delta)\mu] \le e^{-\delta^2\mu/3}$ for $0 < \delta \le 1$. [Hoeffding](/hoeffding-inequality/): for $n$ independent variables in $[0,1]$, the mean exceeds its expectation by $t$ with probability at most $e^{-2nt^2}$.
- A [martingale](/martingale/) keeps its mean at a stopping time under the conditions of the [optional stopping theorem](/optional-stopping-theorem/). [Azuma-Hoeffding](/azuma-inequality/): with steps bounded by $c_k$, $\Pr[|X_n - X_0| \ge t] \le 2e^{-t^2/(2\sum c_k^2)}$.

## Which bound to use

| What you know about $X$ | Bound | Decay of $\Pr[X - \mu \ge t]$ |
|---|---|---|
| $X \ge 0$ and its mean | [Markov](/markov-inequality/) | $\mu/(\mu + t)$ |
| Mean and variance $\sigma^2$ | [Chebyshev](/chebyshev-inequality/) | $\sigma^2/t^2$ |
| Probabilities of the bad events, any dependence | [Union bound](/union-bound/) | sum of the probabilities |
| Sum of $n$ independent 0/1 variables | [Chernoff](/chernoff-bound/) | $e^{-t^2/(3\mu)}$ for $t \le \mu$ |
| Sum of $n$ independent variables in $[0, 1]$ | [Hoeffding](/hoeffding-inequality/) | $e^{-2t^2/n}$ |
| Martingale with steps at most $c_k$ | [Azuma-Hoeffding](/azuma-inequality/) | $e^{-t^2/(2\sum c_k^2)}$ |
| Rare bad events, each depending on at most $d$ others | [Lovász local lemma](/lovasz-local-lemma/) | none fail if $e\,p\,(d+1) \le 1$ |

: The tail bounds of the chapter, from the weakest assumption to the strongest. Here $\mu = \mathbb{E}[X]$ and $p$ bounds the probability of each bad event. The more you know about $X$, the faster the bound falls.

## Doing a probabilistic analysis

- Say where the randomness is: in the input, as in average-case analysis, or in the algorithm's choices. A bound over random choices holds for every input.
- To find an expectation, look for indicators first. Linearity works even when the indicators depend on each other.
- To bound a tail, start with Markov or Chebyshev; move to Chernoff or Hoeffding only when the variable is a sum of independent parts and you need a probability below $1/\mathrm{poly}(n)$.
- When there are many bad events, bound each one by $n^{-c}$ and add them with the union bound.
- Check every claim of independence. A common error is to multiply the probabilities of events that are not independent.

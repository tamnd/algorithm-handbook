## What to remember

- **Diversity has several numbers.** The [Shannon index](/shannon-diversity-index/) $H = -\sum p_i \ln p_i$ and the [Simpson index](/simpson-diversity-index/) $\lambda = \sum p_i^2$ weight rare species differently. Their effective numbers satisfy $1/\lambda \le e^H \le S$. The plug-in $H$ is biased low and depends on the sample size, which [rarefaction](/rarefaction/) corrects; [Chao1](/chao1-estimator/) adds $f_1^2/(2f_2)$ for the species that the sample missed.
- **Logistic growth is the base model.** $\dot N = rN(1 - N/K)$ rises along an S-curve to $K$, fastest at $K/2$. Written for separate generations as the [logistic map](/logistic-map/) or the [Ricker model](/ricker-model/), it has a stable fixed point only for small $r$, then cycles of period 2, 4, 8 and chaos.
- **Interactions are read from the Jacobian.** The [Lotka-Volterra predator-prey model](/lotka-volterra-predator-prey/) has neutral cycles; a [Holling type II](/holling-functional-response/) response can make them a limit cycle. In [Lotka-Volterra competition](/lotka-volterra-competition/) the two species coexist stably when each limits itself more than it limits the other.
- **$R_0$ is the threshold.** An epidemic grows when the [basic reproduction number](/basic-reproduction-number/) exceeds 1. With homogeneous mixing, immunity in a share $1 - 1/R_0$ stops spread, and the [final size](/final-size-relation/) $z$ solves $1 - z = e^{-R_0 z}$. For $R_0 = 2$, $z = 0.797$, well above the threshold $0.5$, because the epidemic overshoots.
- **Structure enters through a matrix.** With several types of host, $R_0$ is the spectral radius of the [next-generation matrix](/next-generation-matrix/). On a network with degree distribution $P(k)$, the SIS threshold is $\langle k \rangle / \langle k^2 \rangle$, which goes to 0 when the degree variance is unbounded.
- **Early chance can end an outbreak.** For a [branching process](/galton-watson-process/) with offspring generating function $f$, the extinction probability is the smallest root of $f(s) = s$ in $[0, 1]$, and it is less than 1 exactly when the mean exceeds 1 (with $p_1 < 1$).
- **Growth rate and $R$ are linked by the generation interval.** $R = 1/M(-r)$, where $M$ is the moment generating function of the [generation interval](/generation-interval/). The same growth rate gives a larger $R$ when the interval is longer or less variable.
- **$R_t$ is estimated from the renewal equation.** [Cori estimation](/cori-rt-estimation/) gives a gamma posterior with shape $a + \sum I_u$ and rate $1/b + \sum \Lambda_u$ over a window; its coefficient of variation is $1/\sqrt{\text{shape}}$.

## The main methods side by side

| Method | Input | Output | Cost |
|---|---|---|---|
| [Chao1](/chao1-estimator/) | one sample of $n$ individuals | lower estimate of species richness | $\Theta(n)$ expected |
| [Lincoln-Petersen](/lincoln-petersen-estimator/) | marked, caught, recaptured | population size $MC/R$ | $\Theta(M + C)$ expected |
| [Leslie matrix](/leslie-matrix/) projection | $k$ age classes, $T$ steps | numbers by age, growth rate | $\Theta(kT)$ |
| [Final size](/final-size-relation/) iteration | $R_0$ | attack rate $z$ | linear convergence |
| [Reed-Frost](/reed-frost-model/) simulation | $S_0$, $I_0$, $p$ | one epidemic by generation | $O(S_0)$ binomial draws |
| [Stochastic SIR](/stochastic-sir-model/) | $N$, $\beta$, $\gamma$ | one exact sample path | $O(N)$ events |
| [Cori estimation](/cori-rt-estimation/) | $T$ daily counts, interval of length $s$ | posterior of $R_t$ per window | $\Theta(Ts)$ |
| [Data augmentation MCMC](/epidemic-data-augmentation-mcmc/) | $n$ removal times | joint posterior of $\beta$, $\gamma$ | $\Theta(n^2 \log n)$ per iteration |

: Main computational methods of the chapter. The costs are those stated in the entries; the final size iteration is the fixed-point iteration from $z_0 = 1$.

## Choosing a method

- For diversity, report an effective number ($e^H$ or $1/\lambda$) and compare samples only at a common size, by rarefaction. Use Chao1 when the sample has many singletons.
- For a population with separate generations, use a map; for overlapping generations and age-dependent rates, use the Leslie matrix; for occupancy of patches, use the Levins model.
- For a quick answer about an epidemic, compute $R_0$, the threshold $1 - 1/R_0$ and the final size. Add an exposed class when the latent period is long, and use the next-generation matrix when hosts differ.
- When cases are few, use a stochastic model: the branching process for the chance of a major outbreak, the stochastic SIR model for whole paths.
- To track transmission during an outbreak, use Cori estimation with a stated generation interval. To estimate rates from removal times alone, use data augmentation MCMC.

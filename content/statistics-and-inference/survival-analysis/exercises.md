1. ◦ A lifetime has [survival function](/survival-function/) $S(t) = \exp(-(t/10)^2)$ for $t \ge 0$, a Weibull law with shape 2. Compute $S(5)$, the [hazard](/hazard-function/) $h(5)$, the cumulative hazard $H(5)$ and the median. Is the hazard increasing or decreasing?

2. ◦ Name the kind of incomplete observation in each case, using the terms of [censoring](/censoring/). (a) Twenty bulbs go on test and the test stops at the fifth failure; the other fifteen are still lit. (b) A patient tests negative for an infection at the visit in year 2 and positive at the visit in year 3. (c) A study of the age at which children learn to read tests each child first at age 4, and some can already read. (d) A study of the residents of a retirement home records the age at death, and only people who have reached age 70 alive can enter the home.

3. ◦ Eight subjects have the observed times $3,\ 4^+,\ 4,\ 6,\ 8^+,\ 9,\ 9,\ 12^+$, where $+$ marks a censored time. Compute the [Kaplan-Meier estimate](/kaplan-meier-estimator/) $\hat S(t)$ at each event time and the estimated median. At $t = 4$, is the subject censored at 4 in the risk set?

4. ◦ For the eight times of exercise 3, compute the [Nelson-Aalen estimate](/nelson-aalen-estimator/) $\hat H(t)$ at each event time as an exact fraction. Compare $\exp(-\hat H(9))$ with $\hat S(9)$, and say why the first is larger for every data set.

5. ◦ For the eight times of exercise 3, use [Greenwood's formula](/greenwood-formula/) to estimate the variance and the standard error of $\hat S(6)$. Give the plain 95% interval $\hat S \pm 1.96\,\widehat{\mathrm{se}}$ and the log-log interval.

6. ◦ At one event time of a [log-rank test](/log-rank-test/), group A has 10 subjects at risk and group B has 6. Three events happen, two of them in group A. Compute the expected number $E_A$ of events in group A and the hypergeometric variance $V$ of this table.

7. ◦ Five subjects have observed times $2, 4^+, 5, 6, 9^+$ and risk scores $0.7, 0.2, 0.8, 0.4, 0.1$, where a larger score predicts an earlier event. List the comparable pairs and compute [Harrell's C](/harrell-c-index/).

8. ◦ In a [Cox model](/cox-proportional-hazards-model/) with one binary covariate, $\beta = \log 2$, and the group with $x = 0$ has $S_0(t) = 0.8$ at a time $t$. Find $S_1(t)$, the two event probabilities by $t$ and their ratio. What is $\log(-\log S_1(t)) - \log(-\log S_0(t))$?

9. ◦ In a shared gamma [frailty model](/frailty-model/) with frailty variance $\theta = 0.5$, the conditional hazard ratio of a binary covariate is $r = 3$. Compute the marginal hazard ratio at a time where $H_0(t) = 2$, and Kendall's $\tau$ between two event times in the same cluster.

10. • A discrete lifetime has $P(T = k) = p(1 - p)^{k-1}$ for $k = 1, 2, \ldots$, the [geometric law](/geometric-distribution/). Find its discrete hazard $h_k$, its survival function $S(k)$ and $H(k) = \sum_{j \le k} h_j$. For $p = 1/2$ compare $S(2)$ with $\exp(-H(2))$. Then prove that $\prod_j (1 - h_j) \le \exp(-\sum_j h_j)$ for any discrete hazards, with equality only when all the $h_j$ in the product are $0$.

11. • Five components are tested for 10 hours. Three fail, at hours 2, 5 and 7, and two are still working at hour 10. Under an exponential model, write the likelihood with the censored times and find the maximum likelihood estimate $\hat\lambda$ and its standard error from the observed information. Compare $\hat\lambda$ with the estimate that drops the two censored components and with the one that treats them as failures at hour 10, and say in which direction each one is biased.

12. • Run Efron's redistribute-to-the-right construction on the eight times of exercise 3: start with mass $1/8$ on each time, and move the mass of each censored time, from left to right, equally to all later times. Check that the mass left on each event time equals the jump of $\hat S$ there. Where does the mass of $12^+$ go?

13. • Group A has times $2, 4, 5^+, 7, 9$ and group B has times $1, 3, 3, 6^+, 8$. Build the table of the [log-rank test](/log-rank-test/) and compute $O_A$, $E_A$, $V$, the statistic $X^2 = (O_A - E_A)^2/V$ and its approximate p-value from $\chi^2_1$. What does the p-value say about the hypothesis of equal hazards, and what does it not say?

14. • Under proportional hazards with a fraction $p$ of the subjects in group 1, the log-rank $U/\sqrt V$ is approximately $N(\sqrt{Dp(1-p)}\,\log\theta, 1)$, where $D$ is the number of events. Derive the number of events needed for a two-sided test at level $\alpha$ with power $1 - \beta$. Evaluate it for $\theta = 0.7$, $\alpha = 0.05$ and power $0.8$, with equal allocation and with allocation $2:1$. With equal allocation, how many subjects are needed if 60% of them are expected to have the event during the trial? (See [sample size determination](/sample-size-determination/).)

15. • Five subjects have times and binary covariates $(1, 0), (3, 1), (4^+, 1), (6, 0), (8, 1)$. For the [Cox partial likelihood](/cox-partial-likelihood/), compute the score $U(0)$ and the information $I(0)$ exactly, take one [Newton](/newton-raphson-method/) step from $\beta = 0$, and iterate to $\hat\beta$. What is $U(0)^2/I(0)$, and why is it the log-rank statistic for these data?

16. • For the data of exercise 15, fix $\beta = \log 2$, so that the weights $e^{\beta x}$ are 1 and 2. Compute the [Breslow estimate](/breslow-estimator/) $\hat H_0$ at each event time as a fraction, and the predicted survival $\hat S(6 \mid x)$ for $x = 0$ and $x = 1$. Compute the [Schoenfeld residuals](/schoenfeld-residuals/) at $\beta = \log 2$ and check that they sum to the score $U(\log 2)$. What does the sign of the sum say about $\hat\beta$?

17. • In the [accelerated failure time model](/accelerated-failure-time-model/) $\log T = \mu + \gamma x + \sigma W$ with $W$ standard minimum extreme value, take $\gamma = -0.3$ and $\sigma = 0.5$. Give the time ratio, the ratio of the medians and the hazard ratio between $x = 1$ and $x = 0$. Is the hazard increasing or decreasing in $t$?

18. • Eight subjects have times $1, 2, 3, 3, 5, 6, 7, 8$ and causes $1, 0, 2, 1, 2, 0, 1, 0$, where 0 means censored. Compute the [Aalen-Johansen](/aalen-johansen-estimator/) cumulative incidences $\hat F_1$ and $\hat F_2$ and the all-cause $\hat S$ at each event time, and check that they sum to 1. Compute one minus the Kaplan-Meier estimate for cause 1 with cause 2 treated as censored. At which time do the two estimates of the cause-1 risk first differ, and why not earlier?

19. • Two causes have constant cause-specific hazards $h_1 = h_2 = 1$. Find $F_1(t)$, the all-cause $S(t)$ and the subdistribution hazard $\tilde h_1(t) = h_1(t)S(t)/(1 - F_1(t))$ of the [Fine-Gray model](/fine-gray-model/). Find $\tilde h_1(0)$ and the limit of $\tilde h_1(t)$ as $t \to \infty$, and explain why $\tilde h_1$ falls while $h_1$ is constant.

20. • Four interval-censored observations are $(0, 3]$, $(2, 5]$, $(4, 7]$ and $(6, 9]$. Find the innermost intervals of the [Turnbull estimator](/turnbull-estimator/), write the likelihood as a function of their masses, and find the NPMLE and its likelihood. Check the Kuhn-Tucker conditions at your answer.

21. • At an event time, 10 subjects are at risk and 3 events are recorded at the same time. Show that the Kaplan-Meier factor does not change if the three events are taken to happen at three distinct times just apart, while the Nelson-Aalen increment does. Give both Nelson-Aalen increments, and prove the statement for $d$ tied events among $n$ at risk.

22. • Every member of a population has a constant hazard $\lambda Z$, where $\lambda = 1$ and the frailty $Z$ is gamma with mean 1 and variance $\theta = 0.5$. Find the population survival function and hazard. At what time is the population hazard half its initial value, and what is the population survival at that time, compared with $e^{-2}$ for a population in which every $Z = 1$?

23. ★ With no censoring and no tied times, order the $n$ subjects by time and let $a_i = 1 - \sum_{k=1}^{i} 1/(n - k + 1)$ be the score of rank $i$. Prove that the log-rank numerator $U = O_1 - E_1$ equals $\sum_{i \in G_1} a_i$, the sum of the scores of the subjects in group 1, so that the log-rank test is a linear rank test.

24. ★ Let $(T, C)$ have a joint density on $(0, \infty)^2$, possibly with $T$ and $C$ dependent, and observe $Y = \min(T, C)$ and $\delta = 1\{T \le C\}$. Define the crude hazards $g_1(t) = \lim_{\Delta \to 0} P(t \le Y < t + \Delta, \delta = 1 \mid Y \ge t)/\Delta$ and $g_0(t)$ in the same way with $\delta = 0$. Construct independent times $T^\ast$ and $C^\ast$ for which $(\min(T^\ast, C^\ast), 1\{T^\ast \le C^\ast\})$ has the same distribution as $(Y, \delta)$, and prove it. What does this say about testing independent [censoring](/censoring/)?

25. ★ Design an algorithm that computes [Harrell's C](/harrell-c-index/) for $n$ subjects with right censoring, tied times and tied scores in $O(n \log n)$ time, using a [Fenwick tree](/fenwick-tree/) over the ranks of the scores. Use the conventions of the entry: a pair is comparable when the earlier time is an event, a censored time tied with an event time outlasts it, two events at the same time are not comparable, and tied scores count $1/2$.

26. ★ Two groups share the cause-specific hazard $h_1 = 1$ for cause 1. The cause-2 hazard is $h_2 = 1$ for $x = 0$ and $h_2 = 2$ for $x = 1$. Find $F_1(t \mid x)$ for both groups and the ratio of the subdistribution hazards $\tilde h_1(t \mid 1)/\tilde h_1(t \mid 0)$ as a function of $t$. Show that it equals 1 at $t = 0$ and tends to 0, so that the [Fine-Gray model](/fine-gray-model/) does not hold although the covariate does not act on the cause-1 hazard at all. What are $F_1(\infty \mid 0)$ and $F_1(\infty \mid 1)$?

27. ★ Run the self-consistency (EM) iteration of the [Turnbull estimator](/turnbull-estimator/) on the data of exercise 20, starting from equal masses $1/3$ on the three innermost intervals. Prove that after $k$ iterations the middle mass is exactly $1/(k + 3)$, so that the iteration converges to the NPMLE but the error falls only like $1/k$.

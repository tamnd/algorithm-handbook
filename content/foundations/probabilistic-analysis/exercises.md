1. ◦ Two fair dice are thrown. What is the probability that the sum is 7, given that at least one die shows a 6? Compare it with the probability that the sum is 7 with no condition.

2. ◦ Two fair coins are tossed. Let $A$ be the event that the first coin shows heads, $B$ that the second shows heads, and $C$ that the two coins agree. Show that each two of the events are [independent](/independent-events/) but the three are not mutually independent.

3. ◦ A fair die is thrown until it shows a 6. What is the expected number of throws? What is the probability that more than 10 throws are needed?

4. ◦ A position $i$ with $1 \le i < n$ is a descent of a sequence $a_1, \ldots, a_n$ if $a_i > a_{i+1}$, and a position $1 < i < n$ is a peak if $a_{i-1} < a_i > a_{i+1}$. Use [indicators](/indicator-random-variable/) to find the expected number of descents and of peaks in a uniformly random permutation of $n$ distinct keys.

5. ◦ [HIRE-ASSISTANT](/hire-assistant/) is run on 10 candidates in uniformly random order. What is the expected number of hires, to three decimal places? What is the probability that exactly one candidate is hired, and that all 10 are hired?

6. ◦ A random variable $X \ge 0$ has mean 10 and variance 4. What upper bounds on $\Pr[X \ge 15]$ do [Markov's](/markov-inequality/) and [Chebyshev's](/chebyshev-inequality/) inequalities give? A program whose expected running time is $T$ is stopped after time $4T$; bound the probability that it is stopped before it finishes.

7. ◦ A program hashes keys to uniformly random 32-bit values. About how many keys give a repeated hash value with probability $1/2$? About how many for 64-bit values?

8. ◦ A fair die is thrown until every face has appeared. What is the expected number of throws?

9. ◦ 100 balls are thrown independently and uniformly into 100 bins. Find, to one decimal place, the expected number of empty bins and the expected number of bins with exactly one ball.

10. ◦ In a [Monty Hall](/monty-hall-problem/) game with 100 doors, you pick one door and the host, who knows where the car is, opens 98 of the others, all with goats. What is the probability of winning if you switch? Now change the game: there are 3 doors, and the host opens one of the two doors you did not pick uniformly at random, without knowing where the car is. It happens to show a goat. What is the probability of winning if you switch?

11. • [Randomized quicksort](/randomized-quicksort/) sorts $n$ distinct keys. What is the probability that the smallest and the largest key are compared? What is the expected number of comparisons in which the smallest key takes part?

12. • In [HIRE-ASSISTANT](/hire-assistant/) on a random order, let $X_i$ be the indicator that candidate $i$ is better than candidates $1, \ldots, i-1$. Show that $X_1, \ldots, X_n$ are independent, and find the [variance](/variance/) of the number of hires. Evaluate it for $n = 10$.

13. • Show that the variance of the number of inversions of a uniformly random permutation of $n$ keys is $n(n-1)(2n+5)/72$. The mean, $n(n-1)/4$, is the average number of shifts of [insertion sort](/insertion-sort/).

14. • Let $T$ be the number of draws in the [coupon collector's problem](/coupon-collector-problem/) with $n$ coupons. Show that $\mathrm{Var}(T) < \pi^2 n^2/6$ and that $\Pr[T \ge 2nH_n] \le \pi^2/(6H_n^2)$.

15. • A fair coin is flipped $n$ times. Use the [union bound](/union-bound/) to show that the probability of a run of at least $k$ heads is at most $n 2^{-k}$, and deduce that a run of $\lceil 2 \lg n \rceil$ heads appears with probability at most $1/n$.

16. • Let $X$ be [geometric](/geometric-distribution/) with success probability $p$, counting the trials up to and including the first success. Find $\mathbb{E}[X^2]$, $\mathrm{Var}(X)$ and $\mathbb{E}[1/X]$, and check that the last one agrees with [Jensen's inequality](/jensens-inequality/).

17. • A fair coin is flipped 1000 times. Bound the probability of at least 600 heads with Chebyshev's inequality, with the [Chernoff bound](/chernoff-bound/) in the form $e^{-\delta^2\mu/3}$, and with [Hoeffding's inequality](/hoeffding-inequality/). Compare the three bounds with the exact value, about $1.4 \times 10^{-10}$.

18. • An unknown probability $p$ is estimated by the fraction of successes in $n$ independent trials. How large must $n$ be for Hoeffding's inequality to guarantee that the estimate is within $0.01$ of $p$ with probability at least $0.99$?

19. • A randomized algorithm for a yes-or-no question answers correctly with probability $2/3$ on every input. It is run $k$ times independently and the majority answer is returned. Show that the majority is wrong with probability at most $e^{-k/18}$, and find $k$ such that the error is at most $n^{-2}$, so that the answer is correct [with high probability](/high-probability-bounds/).

20. • A fair die is thrown until it shows a 6. What is the expected sum of all the throws, the 6 included? Find it with [Wald's equation](/walds-equation/), and check the answer by another argument.

21. • From $k$ independent fair bits $b_1, \ldots, b_k$, form for each nonempty set $S \subseteq \{1, \ldots, k\}$ the bit $Y_S = \bigoplus_{i \in S} b_i$. Show that the $2^k - 1$ bits $Y_S$ are each fair and pairwise independent, but for $k \ge 2$ not three-wise independent.

22. • A gambler bets 1 on each toss of a fair coin and stops at the first time $T$ at which he is 1 ahead. His fortune $S_t$ is a [martingale](/martingale/) with $S_0 = 0$, $T$ is finite with probability 1, and $S_T = 1$. Which conditions of the [optional stopping theorem](/optional-stopping-theorem/) fail?

23. ★ Let $M$ be the maximum of $n$ independent geometric variables with $p = 1/2$; it is the number of levels of a [skip list](/skip-list/) with $n$ keys. Show that $\lg n - 1 < \mathbb{E}[M] \le \lg n + 3$.

24. ★ A walk starts at $a$ and moves $+1$ with probability $p$ and $-1$ with probability $q = 1 - p$, with $p \ne 1/2$, until it reaches $0$ or $b > a$. Find a function $f$ for which $f(S_t)$ is a martingale, and use it to find the probability that the walk reaches $b$. Evaluate it for $p = 0.6$, $a = 3$, $b = 10$.

25. ★ A formula in conjunctive normal form has clauses of exactly $k$ literals on distinct variables, and each variable appears in at most $m$ clauses. Use the [Lovász local lemma](/lovasz-local-lemma/) to show that the formula is satisfiable when $m \le 2^k/(ek)$.

26. ★ $m$ balls are thrown independently and uniformly into $n$ bins, and $Z$ is the number of empty bins. Use the [Azuma-Hoeffding inequality](/azuma-inequality/) to show that $\Pr[|Z - \mathbb{E}[Z]| \ge t] \le 2e^{-t^2/(2m)}$. For $m = n$, what deviation $t$ makes the bound $2/n^2$?

27. ★ Show that the number of cycles of a uniformly random permutation of $n$ elements has the same distribution as the number of hires of [HIRE-ASSISTANT](/hire-assistant/) on $n$ candidates in random order. Deduce that the expected number of cycles is $H_n$.

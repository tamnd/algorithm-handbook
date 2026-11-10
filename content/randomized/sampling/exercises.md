1. ◦ Run [selection sampling](/selection-sampling/) with $N = 5$ and $n = 2$. What is the probability that the first item is selected? That the scan stops after looking at exactly two items? What is the expected number of items it looks at?

2. ◦ Run [Floyd's algorithm](/floyd-sampling/) with $n = 5$ and $k = 2$, so that $j$ takes the values 3 and 4. List the pairs of draws $(t_3, t_4)$ that produce the set $\{3, 4\}$, and check that the set has probability $1/\binom{5}{2}$.

3. ◦ A [reservoir](/reservoir-sampling/) of size $k = 1$ reads a stream of three items. With Algorithm R, what is the probability that each item is the one kept at the end? Now replace the kept item by each new item with probability $1/2$ instead. What are the three probabilities?

4. ◦ [Bernoulli sampling](/bernoulli-sampling/) with $p = 0.01$ runs on $n = 1000$ items. Give the mean and the variance of the sample size, and the probability that the sample is empty. With $p = 1/4$, the skip method draws $U = 1/2$ first. What skip $G$ does line L8 return, and which position is kept first?

5. ◦ Run [systematic sampling](/systematic-sampling/) with $N = 10$, $n = 4$ and $r = 2$. Which positions are taken? As $r$ runs over $\{0, \ldots, 9\}$, how many different samples can the method produce, and with what probabilities? Compare with the number of 4-subsets of 10 items.

6. ◦ Build the [alias table](/alias-method/) for the weights $w = (1, 1, 2, 4)$ with ALIAS-BUILD, using *small* and *large* as stacks. Give $\mathit{prob}$, $\mathit{alias}$ and $W$, and count the pairs $(i, t)$ that return item 3.

7. ◦ Apply the [Box-Muller transform](/box-muller-transform/) to $U_1 = e^{-2}$ and $U_2 = 1/8$. How many uniforms does the [polar method](/marsaglia-polar-method/) use on average to make one pair of normals?

8. ◦ Use [rejection sampling](/rejection-sampling/) for the density $f(x) = 2x$ on $[0, 1]$, with the uniform proposal and $M = 2$. What is the mean number of tries, and with what probability is a proposal $y$ accepted? For the half-normal density $f(x) = \sqrt{2/\pi}\, e^{-x^2/2}$ on $x \ge 0$ with the proposal $g(x) = e^{-x}$, find the smallest $M$.

9. ◦ Four [importance sampling](/importance-sampling/) draws have weights $1, 1, 1, 5$. What is Kong's effective sample size? What is it when all four weights are equal?

10. ◦ The [Karp-Luby estimator](/karp-luby-estimator/) is run on a union of $m = 10$ sets with $\varepsilon = 0.1$ and $\delta = 0.01$. How many samples does the bound $N = \lceil 3m \ln(2/\delta)/\varepsilon^2 \rceil$ ask for?

11. • Show that the largest element $L$ of a uniform $n$-subset of $\{1, \ldots, N\}$ has $E[L] = n(N + 1)/(n + 1)$, which is the expected number of items that selection sampling looks at. Check the formula for $N = 4$ and $n = 2$ by listing the six subsets.

12. • Show that every reservoir algorithm writes at least $k(1 + H_n - H_k)$ items into its reservoir in expectation, using only the fact that after item $t$ the reservoir is a uniform sample of the first $t$ items. Evaluate the bound for $k = 10$ and $n = 10^4$, and show that Algorithm R meets it exactly.

13. • How many random numbers does [Algorithm L](/algorithm-l/) use in expectation for $k = 100$ and $n = 10^6$? How many does Algorithm R use?

14. • Take the weights $w = (1, 2, 3)$ and $k = 2$. Compute the probability that each item is in the sample under successive sampling, and under proportional inclusion $\pi_i = k w_i / W$, as defined in [weighted sampling](/weighted-sampling/). Which item shows the difference most?

15. • Item $i$ of [weighted reservoir sampling](/weighted-reservoir-sampling/) has the key $K_i = u_i^{1/w_i}$. Show that $\Pr[K_1 > K_2] = w_1/(w_1 + w_2)$. Then show that, for the same uniform $u_i$, the [Gumbel-max](/gumbel-max-trick/) key $\ln w_i - \ln(-\ln u_i)$ orders the items exactly as $K_i$ does.

16. • Run [priority sampling](/priority-sampling/) with $k = 1$ on two items of weights 1 and 3. What is the probability that item 1 is the one sampled? Show that its estimate $\hat w_1$ still has mean exactly 1.

17. • A population has two strata of 500 units each, with standard deviations $S_1 = 1$ and $S_2 = 9$. A [stratified sample](/stratified-sampling/) of $n = 100$ is taken. Ignoring the finite population correction, compare the variance of the stratified mean under proportional allocation and under Neyman allocation $n_h \propto N_h S_h$.

18. • Let $d = 1$ and $f(x) = x$. Show that [Latin hypercube sampling](/latin-hypercube-sampling/) with $n$ points estimates $\int_0^1 x\,dx$ with variance $1/(12 n^3)$, against $1/(12 n)$ for $n$ independent points.

19. • Apply [ratio-of-uniforms](/ratio-of-uniforms/) to the exponential density, with $h(x) = e^{-x}$ for $x \ge 0$. Find the box $(0, a] \times [b_-, b_+]$ and the acceptance probability.

20. • To get a uniform point in the unit ball of $\mathbb{R}^d$, draw uniform points in the cube $[-1, 1]^d$ and keep the first one inside the ball. Give the acceptance probability for $d = 2$ and for $d = 10$, and the mean number of tries for $d = 10$. What does this say about rejection sampling in high dimension?

21. • Give a method that returns 1 with probability $p$, for any real $p \in (0, 1)$ whose binary digits can be computed one at a time, using fair bits only. Show that it uses 2 bits on average, whatever $p$ is.

22. • Show that no algorithm that uses at most $B$ fair bits, for a fixed $B$, can output a uniform 2-subset of $\{1, 2, 3, 4\}$. For which $n$ and $k$ does such an algorithm exist? Compare with the [uniform random subset](/uniform-random-subset/) entry.

23. • In the Karp-Luby estimator, let $Z_1 = W \cdot [\text{$i$ is the first set that holds $x$}]$ and $Z_2 = W / c(x)$ for a uniform pair $(i, x)$. Show that both have mean $|U|$, that $E[Z_1^2]/|U|^2 = W/|U| \le m$, and that $Z_2$ never has a larger variance than $Z_1$.

24. ★ In the permutation variant of Floyd's algorithm, $S$ is a sequence: if $t \notin S$, put $t$ at the front, and otherwise insert $j$ right after $t$. Prove that the output is a uniformly random ordered $k$-sample, each of the $n(n-1)\cdots(n-k+1)$ sequences of distinct elements having the same probability.

25. ★ Two machines hold uniform $k$-samples $S_1$ and $S_2$ of disjoint streams of lengths $n_1, n_2 \ge k$, kept by Algorithm R with no keys. Give a way to combine them into a uniform $k$-sample of the union of the streams, and prove that it is uniform.

26. ★ Prove that the $k$ items with the largest keys $u_i^{1/w_i}$, read in decreasing order of key, have the law of successive sampling: each item in turn is chosen among those left with probability proportional to its weight.

27. ★ In part 2 of the [Jerrum-Valiant-Vazirani theorem](/jerrum-valiant-vazirani-theorem/), suppose the path $x = x^{(0)}, x^{(1)}, \ldots, x^{(m)}$ is fixed in advance, each step goes to a part with ratio $p_i = N(x^{(i+1)})/N(x^{(i)}) \ge 1/2$, $N(x^{(m)}) = 1$, and the sampler is exactly uniform. With $t$ samples per level, show that $t = \lceil 32 m / \varepsilon^2 \rceil$ makes $\prod_i \hat p_i$ lie within a factor $1 \pm \varepsilon/2$ of $1/N(x)$ with probability at least $3/4$. How many samples is that in all?

28. ★ Systematic sampling with $n \mid N$ and step $k = N/n \ge 2$ gives two items in the same residue class mod $k$ the joint inclusion probability $1/k$, and two items in different classes probability 0. Prove that no function of the one systematic sample is an unbiased estimator of the variance of the sample mean for every population $y$.

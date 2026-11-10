1. ◦ Run the randomized algorithm for [nuts and bolts](/nuts-and-bolts/) on the nuts $[2, 4, 1, 3]$ and the bolts $[3, 1, 4, 2]$, where equal numbers fit. Instead of a random pivot, always take the first bolt of the current range, and keep the input order inside each pile. A single nut and bolt cost one comparison. Count the comparisons and compare the count with the expected value $4(n+1)H_n - 7n$ and the worst case $n^2$ for $n = 4$.

2. ◦ Let $A = \begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix}$, $B = \begin{pmatrix} 1 & 0 \\ 1 & 1 \end{pmatrix}$ and the claimed product $C = \begin{pmatrix} 3 & 2 \\ 1 & 1 \end{pmatrix}$. Run one round of [Freivalds' algorithm](/freivalds-algorithm/) for each of the four vectors $r \in \{0, 1\}^2$. What is the error of one round on this instance? How many rounds bring the error on this instance below $10^{-3}$, and how many does the general bound $2^{-k}$ ask for?

3. ◦ Let $n = 341 = 11 \cdot 31$ and take the base $2$. Run the [Fermat test](/fermat-primality-test/), one round of the [Miller-Rabin test](/miller-rabin-primality-test/) and one round of the [Solovay-Strassen test](/solovay-strassen-primality-test/). Which tests are fooled? If Miller-Rabin finds a [nontrivial square root of 1](/nontrivial-square-root-of-one/), use it to split $341$.

4. ◦ Let $n = 45$ and take the base $19$. Show that $19$ is a witness for Miller-Rabin and an Euler liar for Solovay-Strassen. Then split $45$ with the square root that Miller-Rabin finds.

5. ◦ Count the zeros of $x^2 - y^2$ in $\mathbb{F}_7^2$ and compare the count with the bound of the [Schwartz-Zippel lemma](/schwartz-zippel-lemma/) for $S = \mathbb{F}_7$.

6. ◦ A Monte Carlo algorithm with [two-sided error](/two-sided-error/) is wrong with probability $1/3$. Find the exact error of the majority of $3$ independent runs and of $5$ runs.

7. ◦ A [Las Vegas algorithm](/las-vegas-algorithm/) has expected running time $10$ ms on every input. You need a Monte Carlo algorithm that fails with probability at most $10^{-4}$. Give the total time of the [conversion](/las-vegas-to-monte-carlo-conversion/) with cut-off $2t$, with cut-off $et$, and with a single run cut off by Markov's inequality.

8. ◦ A program calls Freivalds' algorithm $1000$ times and must be wrong in any call with probability at most $10^{-6}$ in all. By the [union bound](/union-bound/), how many rounds does each call need?

9. ◦ Two strings of length $1000$ over the alphabet $\{0, \ldots, 255\}$ are compared by reading each as the coefficients of a polynomial over $\mathbb{F}_p$, $p = 10^9 + 7$, and evaluating both at one uniform point. Bound the probability that two different strings give the same value.

10. • A test has [one-sided error](/one-sided-error/) $1/4$. How many runs bring the error below $10^{-3}$? Now suppose instead that the error $1/4$ is two-sided. Give the number of runs that the bound $e^{-2\gamma^2 k}$ asks for, and check that the exact majority error is about $0.0013$ for $k = 31$ and $0.00095$ for $k = 33$.

11. • A test with two-sided error is right with probability $0.55$. Using the bound $e^{-2\gamma^2 k}$, find the least odd number of runs whose majority errs with probability at most $10^{-6}$. Compare it with the $249$ runs that the same bound asks for at success probability $2/3$, and explain the ratio.

12. • In the nuts and bolts problem, you only want the smallest nut and its bolt. Pick a random bolt, compare it with every nut, compare its nut with every other bolt, and recurse only on the piles of smaller nuts and bolts. Let $C(m)$ be the expected number of comparisons for $m$ pairs, with $C(1) = 1$. Write the recurrence and show that $C(n) = 4n - 3H_n$.

13. • Run the contraction algorithm of [Karger](/karger-min-cut/) on the complete graph $K_4$. Find the exact probability that it returns a given singleton cut and the probability that it returns a given cut into two pairs. Compare the first with the bound $1/\binom{4}{2}$ of the [minimum cut count bound](/minimum-cut-count-bound/), and show that $K_n$ has exactly $n$ minimum cuts for $n \ge 3$.

14. • On the cycle $C_n$, show that the contraction algorithm returns each of the $\binom{n}{2}$ minimum cuts with probability exactly $1/\binom{n}{2}$.

15. • Write the [Tutte matrix](/tutte-matrix/) of the path $1 - 2 - 3 - 4$ and of the star with centre $1$ and leaves $2, 3, 4$, and compute both determinants. If the variables are drawn uniformly from $\mathbb{F}_7$, what is the exact probability that the random test reports "no perfect matching" for the path? Compare it with the Schwartz-Zippel bound.

16. • Let $n \equiv 3 \pmod 4$ be an odd composite. Show that every Euler liar of $n$ is a strong liar, so the two tests accept exactly the same bases. Check the claim on $n = 91$, which has $18$ strong liars.

17. • Over $\mathbb{F}_5$ let $f = x + 1$ and $g = x + 2$, and let the claimed product be $h = x^2 + 2$. A test draws a uniform $r \in \mathbb{F}_5$ and checks $f(r)g(r) = h(r)$. Find its exact error on this instance and the Schwartz-Zippel bound. How long does one round take for polynomials of degree $n$?

18. • A Monte Carlo algorithm returns a correct solution with probability $1/4$ in $3$ ms, and a verifier checks a solution in $1$ ms. Turn it into a Las Vegas algorithm. Give its expected running time and the probability that it is still running after $40$ ms.

19. • Run one round of Miller-Rabin and one of Solovay-Strassen on the [Carmichael number](/carmichael-number/) $1729 = 7 \cdot 13 \cdot 19$ with the base $2$. Show that only Miller-Rabin detects that $1729$ is composite, and find the factor that its chain gives.

20. ★ Let $E_k$ be the exact error of the majority of $k$ independent runs, each wrong with probability $q < 1/2$, for odd $k = 2j + 1$. Show that $E_{k+2} - E_k = \binom{2j+1}{j} \bigl(q(1-q)\bigr)^{j+1} (2q - 1)$, so the error falls with every two more runs.

21. ★ Let $G$ be a connected multigraph on $n \ge 3$ vertices with minimum cut $\lambda$. Show that $G$ has at most $n(n-1)(n-2)/2$ cuts of size at most $3\lambda/2$.

22. ★ Let $n = p^2$ for an odd prime $p$. Show that $n$ has exactly $p - 1$ strong liars, and list them for $n = 25$. What is the probability that a random base in $\{2, \ldots, 23\}$ fools one round on $25$?

23. ★ A deterministic checker of $AB = C$ fixes vectors $r_1, \ldots, r_k$ in advance and accepts when $A(Br_i) = Cr_i$ for all $i$. Show that for $k < n$ there is a wrong $C$ that it accepts. For $n = 3$, $r_1 = (1, 0, 1)$ and $r_2 = (0, 1, 1)$, give an explicit nonzero error $D = C - AB$.

24. ★ An array of $n$ cells holds a single $1$, and an algorithm stops only when it reads that cell. Show that probing in a uniformly random order takes $(n+1)/2$ expected probes on every input, and use the [Yao minimax principle](/yao-minimax-principle/) to show that no Las Vegas algorithm does better on its worst input.

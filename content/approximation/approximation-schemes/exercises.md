1. ◦ Classify each running time of a family of $(1 + \varepsilon)$-approximation algorithms as an FPTAS, an EPTAS that is not an FPTAS, a PTAS that is not an EPTAS, or no scheme at all: (a) $O(n^3/\varepsilon^2)$; (b) $O(n \log n + (1/\varepsilon)^{1/\varepsilon})$; (c) $O(n^{2/\varepsilon})$; (d) $O(2^{1/\varepsilon^2} n^4)$; (e) $O(n^2 (1/\varepsilon)^{20})$; (f) $O(n^{\log_2(1/\varepsilon)})$; (g) $O(2^n/\varepsilon)$. Use the definitions on the [PTAS](/ptas/), [FPTAS](/fptas/) and [EPTAS](/eptas/) pages.

2. ◦ A maximization scheme can be stated as $\mathrm{ALG} \ge (1 - \varepsilon)\,\mathrm{OPT}$ or as $\mathrm{ALG} \ge \mathrm{OPT}/(1 + \varepsilon)$. Which $\varepsilon$ must you pass in each form to be sure of $\mathrm{ALG} \ge 0.95\,\mathrm{OPT}$? A minimization scheme is stated as $\mathrm{ALG} \le \mathrm{OPT}/(1 - \varepsilon)$; which $\varepsilon$ gives ratio at most $1.05$?

3. ◦ Run the [knapsack FPTAS](/knapsack-fptas/) on five items with profits $60, 48, 38, 33, 32$, weights $9, 8, 9, 5, 5$ and $W = 10$. Give $K$, the scaled profits, $q^*$ and the returned set for $\varepsilon = 1/2$ and for $\varepsilon = 1/4$, and compare each result with $\mathrm{OPT}$ and with the bound $(1 - \varepsilon)\,\mathrm{OPT}$.

4. ◦ Apply TRIM from the [subset sum FPTAS](/subset-sum-fptas/) with $\delta = 0.2$ to the list $\langle 5, 6, 7, 8, 9, 11, 13, 14, 17, 20, 24, 30 \rangle$. Then say how many values remain when the list $\langle 1, 2, \ldots, 1000 \rangle$ is trimmed with $\delta = 0.1$, and compare this with the bound $\log_{1+\delta} t + 2$ for $t = 1000$.

5. ◦ Run APPROX-SUBSET-SUM on $x = \langle 14, 18, 46, 58 \rangle$ with $t = 76$ and $\varepsilon = 0.8$. Give the merged list, the sums removed by TRIM, the sums removed for exceeding $t$, and the list kept at each step. Compare the result with $\mathrm{OPT}$ and with $\mathrm{OPT}/(1 + \varepsilon)$.

6. ◦ A knapsack instance has $n = 40$ items with integer profits of at most 25 each. To make the knapsack FPTAS exact, the argument of Garey and Johnson uses $\varepsilon = 1/(B + 1)$ for a bound $B \ge \mathrm{OPT}$. Count the steps $n^3/\varepsilon$ with $B = n \cdot 25$, then with the choice $\varepsilon = 1/P$ of the knapsack FPTAS page, where $P$ is the largest profit. Compare both with the $O(nV)$ steps of the exact [profit-indexed dynamic program](/profit-indexed-dynamic-programming/), where $V$ is the sum of the profits.

7. ◦ In the [Hochbaum-Shmoys PTAS](/hochbaum-shmoys-makespan-ptas/) take $\varepsilon = 0.3$, so $k = \lceil 1/\varepsilon \rceil$, and the guess $T = 80$. Give $k$, the unit $u$, the threshold for large jobs, the set of possible rounded sizes and its size $d$, and the most large jobs a machine can hold. Round jobs of length 47, 21 and 20. If the test accepts, what makespan is guaranteed?

8. ◦ Run the first steps of the [Fernandez de la Vega-Lueker APTAS](/fernandez-de-la-vega-lueker-aptas/) with $\varepsilon = 1/2$ on an instance with $n' = 1000$ large items. Is the grouping used? Give $K$, the number of groups, the number of items in $J$ and the most distinct sizes they can have, and the number of bins for $G_1$. Show that these bins are at most $\delta \cdot \mathrm{OPT}$.

9. ◦ The [shifting technique](/shifting-technique/) gives ratio $(1 + 1/\ell)^d$ in $d$ dimensions. Find the least $\ell$ with ratio at most $1.5$ for $d = 2$ and for $d = 3$.

10. ◦ You can afford $10^{10}$ steps on an instance with $n = 10^4$. For each scheme, find the smallest $\varepsilon$ of the form $1/j$, with $j$ a positive integer, that fits: an EPTAS with $2^{1/\varepsilon} n^2$ steps, a PTAS with $n^{1/\varepsilon}$ steps, an FPTAS with $n^2/\varepsilon^3$ steps, and an FPTAS with $n/\varepsilon^2$ steps.

11. • Write the knapsack FPTAS as a program, with exact rational arithmetic for $K$. Run it on profits $10, 69, 48, 92, 19, 53, 54, 34, 72, 19$, weights $40, 28, 32, 9, 38, 18, 20, 27, 8, 26$ and $W = 75$, for $\varepsilon = 1, 1/2, 1/4, 1/8, 1/16$. Find $\mathrm{OPT}$ by brute force, and the largest $\varepsilon$ of the form $2^{-i}$ for which the scheme is exact.

12. • Run HS-PTAS with $k = 2$ on the jobs $9, 9, 7, 6, 4, 4, 2$ and $m = 3$. Give the guesses tested by the binary search, the schedule returned and its makespan, and compare it with $\mathrm{OPT}$. What small change to HS-PTAS gives a better answer here, and does it change the guarantee?

13. • For the knapsack scheme by partial enumeration on the [PTAS](/ptas/) page, show that the result is at least $\frac{k}{k+1}\,\mathrm{OPT}$, not only $(1 - 1/k)\,\mathrm{OPT}$. Which $k$ then suffices for a given $\varepsilon$?

14. • Give a polynomial-time algorithm that colours the vertices of a [planar graph](/planar-graph/) with at most $\mathrm{OPT} + 1$ colours. You may use that a planar graph can be 4-coloured in polynomial time. Then show that no polynomial-time algorithm has ratio below $4/3$ for this problem unless P = NP.

15. • For [makespan minimization](/makespan-minimization/) on identical machines with integer job lengths: (a) show that no polynomial-time algorithm has $\mathrm{ALG} \le \mathrm{OPT} + c$ for a constant $c$ unless P = NP; (b) apply the scaling lemma of the [asymptotic PTAS](/asymptotic-ptas/) page. What is the instance $I^{(k)}$, and why do $k$ disjoint copies of the instance not work?

16. • Show that a running time of $n^{1/\varepsilon}$ cannot be written as $O(f(1/\varepsilon) \cdot n^c)$ for any function $f$ and constant $c$.

17. • Baker's scheme for maximum independent set in planar graphs gives $(1 - 1/k)\,\mathrm{OPT}$ in $2^{O(k)} n$ time. With $k = n + 1$ the result is exact. Why does this not show P = NP? Show that an FPTAS for this problem would.

18. • Use [Baker's PTAS](/baker-planar-ptas/) for vertex cover in planar graphs to decide whether a planar graph has a vertex cover of size at most $k$ in $2^{O(k)} n$ time.

19. • An algorithm for a minimization problem always returns at most $\mathrm{OPT} + \sqrt{\mathrm{OPT}}$. Show that it is an asymptotic PTAS: give $c(\varepsilon)$ with $\mathrm{ALG} \le (1 + \varepsilon)\,\mathrm{OPT} + c(\varepsilon)$ for every $\varepsilon > 0$. What is its asymptotic ratio?

20. • In the unbounded knapsack problem each item may be taken any number of times. Reduce it to the 0/1 problem with few copies of each item, and give the time of the resulting FPTAS in terms of $n$, $W$ and $\varepsilon$.

21. • A bin packing algorithm uses at most $(1 + \varepsilon)\,\mathrm{OPT} + 1$ bins. Combine it with one simple test so that, for a fixed $\varepsilon$, the result has absolute ratio $3/2$, the best possible unless P = NP. Which $\varepsilon$ works?

22. • In a [bin packing](/bin-packing/) instance every item is larger than $1/3$. Give an exact $O(n \log n)$ algorithm and prove that it is optimal.

23. ★ Show that max cut stays NP-hard on graphs with $n$ vertices and at least $n^2/10$ edges. Conclude that the [dense max cut PTAS](/dense-max-cut-ptas/) cannot be turned into an FPTAS unless P = NP.

24. ★ The two-dimensional knapsack problem gives each item a profit and two weights, and two capacities. Show that it has no FPTAS unless P = NP, although it has a pseudo-polynomial algorithm. Reduce from the equipartition problem: given $n$ numbers with sum $2A$, $n$ even, is there a set of exactly $n/2$ of them with sum $A$?

25. ★ In the restricted shortest path problem on a directed acyclic graph, each edge has an integer cost and a delay, and the task is a path from $s$ to $t$ of least cost with delay at most $D$. Give an FPTAS. Find bounds $B \le \mathrm{OPT} \le (n - 1) B$ in polynomial time, and give the time of the scheme.

26. ★ Jobs with lengths $p_j$, due dates $d_j$ and integer weights $w_j$ are scheduled on one machine. Give an FPTAS for the largest total weight of jobs that finish by their due dates, with time $O(n^3/\varepsilon)$.

27. ★ For makespan on $m$ identical machines, schedule the $k$ longest jobs optimally by trying every assignment, then add the others by [list scheduling](/list-scheduling/). Show that the makespan is at most $\bigl(1 + \frac{1 - 1/m}{1 + \lfloor k/m \rfloor}\bigr)\mathrm{OPT}$. Conclude that this is a scheme for each fixed $m$, with time $O(k m^k + n \log n)$, and say why it is not a PTAS when $m$ is part of the input.

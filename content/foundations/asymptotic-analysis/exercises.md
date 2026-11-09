1. ◦ Put these functions in increasing order of growth, and mark the pairs that are $\Theta$ of each other: $n \lg n$, $\sqrt{n}$, $4^{\lg n}$, $\lg \lg n$, $2^{\lg n}$, $\lg(n!)$, $n^2 / \lg n$, $(\lg n)^3$.

2. ◦ True or false? (a) $2^{n+1} = O(2^n)$. (b) $2^{2n} = O(2^n)$. (c) $n^2 = o(n^2)$. (d) $\lg(n^3) = \Theta(\lg n)$. (e) $(\lg n)^3 = O(n^{0.1})$. (f) $n! = O(n^n)$.

3. ◦ Find constants $c$ and $n_0$ that prove $3n^2 + 10n + 7 = O(n^2)$ from the definition in [asymptotic notation](/asymptotic-notation/). If you insist on $c = 4$, what is the least $n_0$ that works?

4. ◦ How many times does the body of `for i ← 1 to n: for j ← i to n: body` run? Give the exact count and its order of growth.

5. ◦ The loop `i ← n; while i > 1: i ← ⌊i/2⌋` runs on $n = 1000$. How many times does the body run? Give the count for general $n \ge 1$.

6. ◦ Compute $\lg^* 16$, $\lg^* 65536$ and $\lg^* 2^{65536}$, using the definition of the [iterated logarithm](/iterated-logarithm/). Then use the values $A_0(1) = 2$, $A_1(1) = 3$, $A_2(1) = 7$, $A_3(1) = 2047$ to find $\alpha(2047)$ and $\alpha(2048)$ for the [inverse Ackermann function](/inverse-ackermann-function/).

7. ◦ Compute $H_4$ as a fraction and check the bounds $\ln(n+1) \le H_n \le 1 + \ln n$ of the [harmonic series](/harmonic-series/) for $n = 4$.

8. ◦ An algorithm has worst-case time $\Theta(n^2)$ and best-case time $\Theta(n)$. Which of these statements about its running time are true on every input of size $n$: $O(n^2)$, $\Omega(n)$, $\Theta(n^2)$, $\Omega(n^2)$, $O(n)$?

9. ◦ Linear search scans an array of $n$ distinct keys from the left for a key that is present. How many comparisons does it make in the best case and in the worst case? If the key is equally likely to be at each position, what is the average?

10. • Prove that $\lg(n!) = \Theta(n \lg n)$ without [Stirling's approximation](/stirling-approximation/): bound $n!$ above by $n^n$ and below by the product of its largest $\lceil n/2 \rceil$ factors.

11. • Let $f$ and $g$ be functions with $f(n) \ge 1$ and $g(n) \ge 2$ for all large $n$. (a) Show by an example that $f = O(g)$ does not imply $2^{f} = O(2^{g})$. (b) Prove that $f = O(g)$ does imply $\lg f = O(\lg g)$.

12. • Prove that $\sum_{k=1}^{n} k^d = \Theta(n^{d+1})$ for each fixed integer $d \ge 0$. Use only two estimates: every term is at most $n^d$, and the largest $\lceil n/2 \rceil$ terms are each at least $(n/2)^d$.

13. • Count the exact number of times the body runs in `s ← 1; while s ≤ n: (for j ← 1 to s: body); s ← 2s`, for $n \ge 1$. Show that the count lies between $n$ and $2n - 1$.

14. • How many times does the body of `for i ← 0 to n−1: for j ← 0 to i−1: for k ← 0 to j−1: body` run? Give the exact count and its [tilde approximation](/tilde-notation/).

15. • Use Stirling's approximation to show that $\binom{2n}{n} \sim 4^n / \sqrt{\pi n}$. How close is the approximation for $n = 10$, where $\binom{20}{10} = 184756$?

16. • Prove that $\sum_{k=1}^{n} \lfloor n/k \rfloor = \Theta(n \log n)$. (This sum counts the pairs $(k, m)$ with $km \le n$, and it is the number of steps of a sieve that visits each multiple of each $k$.)

17. • Show that $a^{\log_b n} = n^{\log_b a}$ for constants $a, b > 1$. Use this to decide which of $3^{\lg n}$ and $n^{1.5}$ grows faster, and by what factor.

18. • A program starts with $x = 2$ and runs $x \leftarrow x \cdot x$ $n$ times. How many bits does $x$ have at the end? What is the running time under the [unit-cost model](/unit-cost-model/), and what is it under the [logarithmic-cost model](/logarithmic-cost-model/) when a multiplication costs the number of bits of its operands?

19. • Give functions $f \sim g$ for which $2^f \sim 2^g$ fails. Then prove that $f \sim g$ implies $f = \Theta(g)$, and show that the converse is false.

20. • Using $A_k(j) = A_{k-1}^{(j+1)}(j)$ and $A_2(j) = 2^{j+1}(j+1) - 1$, show that $A_4(1) > 2^{2048}$. Conclude that $\alpha(n) \le 4$ for all $n \le 2^{2048}$.

21. • Show that $e^n \ge n^n / n!$ from the power series of $e^x$, and conclude that $n! \ge (n/e)^n$ and $\lg n! \ge n \lg n - n \lg e$ for all $n \ge 1$.

22. • Show that there is no slowest-growing unbounded function: for each nondecreasing unbounded $f$ with positive values, give a nondecreasing unbounded $g$ with $g = o(f)$.

23. ★ Find two nondecreasing functions $f, g$ from the positive integers to the positive integers such that neither $f = O(g)$ nor $g = O(f)$. (So $O$ does not order all functions, not even monotone ones.)

24. ★ An array holds $n$ bits, and a fraction $p$ of them are 1. Give an algorithm that reads only $s$ random positions and outputs an estimate within $\varepsilon$ of $p$ with probability at least $2/3$, where $s$ depends on $\varepsilon$ but not on $n$. How large must $s$ be? This is a [sublinear-time](/sublinear-time/) algorithm.

25. ★ Show that the numbers $\lfloor n/k \rfloor$ for $1 \le k \le n$ take at most $2\sqrt{n}$ distinct values. Use this to compute $\sum_{k=1}^{n} \lfloor n/k \rfloor$ with $O(\sqrt n)$ arithmetic operations.

26. ★ Prove that $H_n$ is not an integer for any $n \ge 2$.

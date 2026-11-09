1. ◦ Use the [master theorem](/master-theorem/) to solve each recurrence, or say why it does not apply: (a) $T(n) = 8T(n/2) + n^2$; (b) $T(n) = T(n/3) + 1$; (c) $T(n) = 3T(n/2) + n^2$; (d) $T(n) = 4T(n/2) + n^2 \lg n$; (e) $T(n) = 3T(n/9) + \sqrt n$.

2. ◦ Give the [watershed function](/watershed-function/) of the recurrences of binary search ($a = 1$, $b = 2$), merge sort ($a = 2$, $b = 2$), Karatsuba multiplication ($a = 3$, $b = 2$) and Strassen's algorithm ($a = 7$, $b = 2$), with the exponent to three decimal places.

3. ◦ The naive recursive program `fib(n) = n if n < 2 else fib(n−1) + fib(n−2)` makes $C(n)$ calls in all, counting the first one. Write the recurrence for $C(n)$, show that $C(n) = 2F_{n+1} - 1$, and compute $C(10)$.

4. ◦ Solve $T(n) = 3T(n/3) + n$ with $T(1) = 1$ exactly for $n = 3^k$, by the [iteration method](/iteration-method/).

5. ◦ Solve $a_n = a_{n-1} + 6a_{n-2}$ with $a_0 = 1$ and $a_1 = 8$ by the characteristic polynomial, and check your formula at $n = 2$.

6. ◦ Solve $a_n = 4a_{n-1} - 4a_{n-2}$ with $a_0 = 1$ and $a_1 = 4$. The characteristic polynomial has a repeated root; say how that changes the form of the solution.

7. ◦ Check [Cassini's identity](/cassini-identity/) for $n = 10$. Then use [Binet's formula](/binet-formula/) to explain why $F_n$ is the integer nearest to $\varphi^n/\sqrt 5$, and find the number of decimal digits of $F_{100}$ without computing it.

8. ◦ Which of these functions are smooth in the sense of the [smoothness rules](/smoothness-rules/), that is, eventually non-decreasing with $f(2n) = O(f(n))$: $n^2$, $n \lg n$, $2^n$, $n^{\lg n}$, $n!$?

9. • Show that the master theorem does not apply to $T(n) = 2T(n/2) + n/\lg n$. Solve it exactly for $n = 2^k$ with $T(1) = 0$, and give its order of growth.

10. • Use the [Akra-Bazzi theorem](/akra-bazzi-theorem/) to solve (a) $T(x) = T(x/2) + T(x/3) + T(x/6) + x$ and (b) $T(x) = T(x/2) + T(x/4) + x$. In (b), find $p$ in closed form.

11. • Solve $T(n) = 3T(n/2) + n$ with $T(1) = 1$ exactly for $n = 2^k$, and write the answer in terms of $n$.

12. • Solve $T(n) = \sqrt n\, T(\sqrt n) + n$ for $n = 2^{2^k}$, with $T(2) = 2$, by a [change of variables](/change-of-variables/). What is its order of growth?

13. • A recursive procedure on an array of $n \ge 2$ items makes one call on the first $\lfloor n/2 \rfloor$ items, one on the remaining $\lceil n/2 \rceil$, and does one unit of work; on one item it does one unit. Prove by strong induction that its cost is exactly $2n - 1$ for every $n \ge 1$.

14. • Let $s_n$ be the number of strings of length $n$ over the alphabet $\{a, b, c\}$ with no two consecutive $a$'s. Find a recurrence for $s_n$, solve it in closed form, and check it for $n = 3$.

15. • The selection algorithm [median of medians](/median-of-medians/) satisfies $T(n) \le T(n/5) + T(7n/10) + cn$. Use a recursion tree to prove $T(n) \le 10cn$, ignoring floors. Why does the algorithm use groups of five and not of three, for which the recurrence becomes $T(n) \le T(n/3) + T(2n/3) + cn$?

16. • A new algorithm multiplies $n \times n$ matrices by splitting them into blocks of size $n/3$, making $a$ recursive products of blocks and spending $\Theta(n^2)$ on additions. What is the largest integer $a$ for which it is asymptotically faster than Strassen's $\Theta(n^{\lg 7})$?

17. • Solve $a_n = a_{n-1}\, a_{n-2}$ with $a_0 = a_1 = 2$ by taking logarithms.

18. • Solve $T(n) = T(\lceil \lg n \rceil) + 1$ with $T(n) = 0$ for $n \le 1$, and compare the answer with the [iterated logarithm](/iterated-logarithm/).

19. • [Stooge sort](/stooge-sort/) sorts the first two thirds of an array, then the last two thirds, then the first two thirds again. Write its recurrence and give its running time as $\Theta(n^c)$ with $c$ to three decimal places. Is it faster or slower than insertion sort?

20. ★ Extend case 2 of the master theorem to negative powers of the logarithm. For $T(n) = aT(n/b) + n^w \lg^k n$ with $w = \log_b a$, show that $T(n) = \Theta(n^w \lg\lg n)$ when $k = -1$ and $T(n) = \Theta(n^w)$ when $k < -1$. Work on powers of $b$.

21. ★ Solve $F_n = n + \frac1n \sum_{k=0}^{n-1} F_k$ with $F_0 = 0$ exactly, by multiplying by $n$ and subtracting the equation for $n - 1$. Then check the leading term against the [continuous master theorem](/continuous-master-theorem/). What algorithm has this recurrence?

22. ★ From the identity $F_{m+n} = F_m F_{n+1} + F_{m-1} F_n$, derive formulas for $F_{2n}$ and $F_{2n+1}$ in terms of $F_n$ and $F_{n+1}$. Write a recursive algorithm that computes $F_n$ with $O(\log n)$ arithmetic operations. Why is its running time not $O(\log n)$ in the [logarithmic-cost model](/logarithmic-cost-model/)?

23. ★ An AVL tree of height $h$ with the fewest nodes has a root, one subtree of height $h - 1$ and one of height $h - 2$, both of the fewest nodes. Taking a single node to have height 0, show that the least number of nodes is $N_h = F_{h+3} - 1$, and deduce that an [AVL tree](/avl-tree/) with $n$ nodes has height less than $\log_\varphi(n + 1) \approx 1.44 \lg(n + 1)$.

24. ★ Prove that if the Euclidean algorithm on $a > b \ge 1$ makes $k$ division steps, then $a \ge F_{k+2}$ and $b \ge F_{k+1}$. Deduce that $k \le 1 + \log_\varphi b$, and give, for each $k$, a pair that needs exactly $k$ steps with the smallest possible $a$.

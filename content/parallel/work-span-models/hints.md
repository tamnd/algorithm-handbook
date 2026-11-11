1. Common: the step is not allowed, since the values differ. Arbitrary: any one of 5, 3 and 7. Priority: 5. Combining with addition: 15.

2. Ten steps and 1023 additions. On 128 processors the steps take $4, 2, 1, 1, 1, 1, 1, 1, 1, 1$ rounds, 14 in all; the bound gives $\lfloor 1023/128 \rfloor + 10 = 17$.

5. Lower bounds 100, 40, 40, 40; upper bounds 136, 78.4, 59.2, 49.6. The parallelism is 25, so past $p = 25$ the span law holds the time at 40 or more.

8. Without locks: 2, 3, 4 or 6. The values 2 and 3 come from both updates reading $x = 1$. With locks only 4 and 6 remain, and the race is still there: the two updates are logically parallel and both write $x$.

10. The work is 8, the span is 5, and $1, 4, 6, 7, 8$ is the critical path. The first scheduler runs $\{1\}, \{2, 3\}, \{4, 5\}, \{6\}, \{7\}, \{8\}$, which is 6 steps. The second puts strand 4 first and finishes in 5. The greedy bound is $(8 - 5)/2 + 5 = 6.5$, and 5 is optimal by the span law.

12. For the fork-join program, $S(n) = 3S(n/2) + O(1)$, since the top-left, the anti-diagonal pair and the bottom-right run one after another. For $n = 1024$ this is $3^{10} = 59{,}049$ against 2047. The sync makes all of the top-right and bottom-left quadrants wait for each other, although a cell needs only its two neighbours.

14. The work law rules out a win while $p \le T_1/(n-1)$. For Hillis–Steele that means $p \le 15$, and the greedy bound wins from $p = 16$. For Blelloch, $p \le 2$ cannot win and $p = 3$ does.

15. $n = 20$: $T_1 = 32{,}836$, $T_\infty = 39$ and slackness about 13.2. At $n = 19$ it is about 8.6. The guarantee $ps/(s+1)$ gives a speedup of about 59.5, an efficiency of about 0.93.

16. Put $f/p = 1 - f$ into the formula. For $f = 0.99$ that is $p = 99$, with speedup 50 and efficiency about 0.505. A chain of $a$ strands followed by $b$ independent strands takes exactly $a + b/p$ steps when $p$ divides $b$.

18. The efficiency is $(n - 1)/(n - p + p \lg p)$. Setting it to at least 0.9 gives $n \ge 9(p \lg p - p) + 10 = 82{,}954$.

21. $T(n) = T(\sqrt{n}) + O(1)$, so $T(n) = O(\log \log n)$. The combining step uses $(\sqrt{n})^2 = n$ processors, and each of the $\log \log n$ levels does $O(n)$ work. The total is $O(n \log \log n)$, so the algorithm is not work-efficient.

22. Take a chain of $k$ strands and $(p - 1)k$ independent strands. One schedule runs the chain on one processor and the independent strands on the others, and takes $k$ steps. A greedy schedule that always chooses independent strands first finishes them in $(p-1)k/p$ steps, then runs the chain alone.

23. Sort the write requests by (address, processor number). A request wins if it is first in the sorted order or its address differs from the request before it, and only winners write. For reads, sort the requests by address and let the first request of each run read. Then copy the value along the run by doubling, in $O(\log p)$ steps. With a bitonic sort each phase costs $O(\log^2 p)$.

24. Use induction on the serial execution, and handle the three events (spawn or call, return, sync) one at a time. The key fact is that a spawned child that has returned stays logically parallel with the parent's continuation until the next sync. After the sync it precedes everything that follows.

25. The probability that some iteration is long is $1 - (1 - 1/n)^n \ge 1 - 1/e$, and then the span is at least $n$. The expected work is $n(1 + (n-1)/n) < 2n$, by linearity of expectation. The span is a maximum, and the expectation of a maximum can far exceed the maximum of the expectations.

26. $S(n) = (2b - 1) S(n/b) + O(b \log b)$, and the master theorem gives the exponent $\log_b(2b-1)$. The values are about 1.585, 1.465, 1.404 and 1.302, which fall towards 1. With $b = n$ the program is the plain wavefront: $2n - 1$ antidiagonals, each costing $O(\log n)$ in spawn overhead, for span $\Theta(n \log n)$.

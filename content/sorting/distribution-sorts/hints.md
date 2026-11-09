1. After counting, $C = [1, 2, 1, 3]$; after the prefix sums, $C = [0, 1, 3, 4]$. The output is $B = [0, 1, 1, 2, 3, 3, 3]$, and the first 3 of the input goes to $B[4]$, ahead of the other two.

2. After the passes: $\langle 140, 81, 312, 263, 205, 47, 7 \rangle$, then $\langle 205, 7, 312, 140, 47, 263, 81 \rangle$, then $\langle 7, 47, 81, 140, 205, 263, 312 \rangle$. In the second pass, 205 and 7 tie on tens digit 0, and 140 and 47 tie on 4; the first pass, on the ones digits, has already put them in the right order.

3. The inclusive sums are $C = [1, 3]$. Then $x$ goes to index 2, $y$ to index 0 and $z$ to index 1, so the output is $\langle y, z, x \rangle$. It is sorted but not stable: $z$ now comes before $x$.

4. The sizes are $n_0 = 3$, $n_2 = 1$, $n_4 = 3$, $n_7 = 1$ and 0 for the other buckets, so $\sum_j n_j^2 = 20$. Bucket 0 receives $0.07, 0.12, 0.04$ and bucket 4 receives $0.61, 0.55, 0.58$; each needs two shifts, four in all.

5. The scans swap 5 with 1 and then 7 with 3, and stop with $i = 4$. The array is $\langle 1, 2, 3, 0, 6, 7, 5 \rangle$.

6. The costs are $8\,388\,736$, $4\,195\,328$, $3\,151\,872$, $2\,228\,224$ and $4\,296\,015\,872$. The best is $r = 16$. With $r = 32$ there is one pass, but the count array has $2^{32}$ entries, four thousand times more than there are keys.

7. The distinguishing prefixes are app, apr, bana, band, banda and c. The string band has no prefix of its own that is not a prefix of bandana, so its whole length counts. $D = 3 + 3 + 4 + 4 + 5 + 1 = 20$ and $N = 35$.

8. The two strings stay together in one task at each depth $0, 1, \ldots, L$, so there are $L + 1$ tasks with two strings, each with $R + 1$ counters: $(L + 1)(R + 1)$ in all. Insertion sort makes one comparison, which reads $L + 1$ characters of each string.

10. After pass 0 the claim of the correctness proof only needs the keys sorted by digit 0, which any sort gives. From pass 1 on, the proof needs ties on the new digit to keep the order of the earlier passes. The whole sort is then no longer stable: if pass 0 swaps two items with equal keys, every later pass sees equal digits and keeps them swapped.

11. Count the keys and form inclusive prefix sums, so that $P[v]$ is the number of keys at most $v$. The answer is $P[b] - P[a - 1]$, with $P[-1] = 0$.

12. Sort stably by $y$ first, then by $x$: in LSD order the less significant field goes first. The keys $xn + y$ are less than $10^{12} < 2^{40}$, so 8-bit digits need five passes.

13. Each $n_j$ is binomial with parameters $n$ and $1/m$, so $\mathbb{E}[n_j^2] = \frac{n}{m}\big(1 - \frac{1}{m}\big) + \frac{n^2}{m^2}$; multiply by $m$. With $m = \sqrt{n}$ the expected time is $\Theta(n^{3/2})$. With $m = n/10$ the sum is $11n - 10$, and the time is $\Theta(n)$.

14. Bucket $j$ gets each key with probability $p_j = \int_{j/n}^{(j+1)/n} f \le c/n$. Then $\mathbb{E}[n_j^2] = np_j(1 - p_j) + n^2 p_j^2 \le c + c^2$, and the sum over the $n$ buckets is at most $(c + c^2)n$.

15. All $n!$ orders of $\{0, \ldots, n-1\}$ are possible inputs, so the decision tree still needs $n!$ leaves. Radix sort uses a digit of a key as an array index, which is not a comparison.

16. Take $\langle \mathtt{b}_1, \mathtt{a}_1, \mathtt{a}_2, \mathtt{b}_2 \rangle$. The first step swaps $\mathtt{b}_1$ into the first free place of bucket b, which holds $\mathtt{a}_2$, and the output is $\langle \mathtt{a}_2, \mathtt{a}_1, \mathtt{b}_1, \mathtt{b}_2 \rangle$.

17. Among non-negative floats the order of the bit patterns, exponent first, is the numeric order. A negative float stores its magnitude the same way, so a larger pattern means a more negative number: flipping all its bits reverses that order and clears the sign bit, which puts all negatives below all non-negatives. $-0.0$ becomes the largest pattern of the negatives and $+0.0$ the smallest of the others, so they end up next to each other, $-0.0$ first.

18. If $r \le \lg n$, the term $\lceil w/r \rceil n$ is at least $wn/\lg n$. If $r > \lg n$, use that $2^r/r$ grows with $r$, so $\lceil w/r \rceil 2^r \ge w \cdot 2^{\lg n}/\lg n$. For $r = \lfloor \lg n \rfloor$, both $\lceil w/r \rceil \le 2w/r$ and $n + 2^r \le 2n$ hold.

19. Day (31 buckets), then month (12), then year (200), each pass stable.

20. The lists after the passes are $\langle \text{bab} \rangle$, then $\langle \text{ba}, \text{bab}, \text{ab} \rangle$, then $\langle \text{a}, \text{ab}, \text{b}, \text{ba}, \text{bab} \rangle$. Each string is read once per pass it takes part in, so $3 + 1 + 2 + 2 + 1 = 9 = N$ characters.

21. $\Pr[X < t] = t^{1/4}$, so bucket 0 gets each key with probability $n^{-1/4}$ and holds about $n^{3/4}$ keys in random order: insertion sort there alone costs $\Theta(n^{3/2})$ expected. For the upper bound, $p_j \le \frac{1}{4} n^{-1/4} j^{-3/4}$ for $j \ge 1$, and $\sum_j j^{-3/2}$ converges. The map $\lfloor n x^{1/4} \rfloor$ makes the bucket of each key uniform.

22. A fixed bucket gets at least $k$ keys with probability at most $\binom{n}{k} n^{-k} \le 1/k!$. Take a union bound over the $n$ buckets, and check that $k! \ge (k/e)^k \ge n^2$ for $k = 3 \ln n / \ln \ln n$ and $n$ large.

23. A key is in a task of at least two keys at depth $d$ only if some other key agrees with it on the first $d$ bits, which has probability at most $\min(1, (n-1)2^{-d})$. Sum over $d \ge 0$: the first $\lceil \lg n \rceil$ terms are at most 1 each, and the rest form a geometric series with sum at most 2.

24. Set all test bits of $X$ to 1 and all test bits of $Y$ to 0, subtract $Y$ from $X$, and AND the result with a mask of the test bits. Field $i$ of the difference is $2^k + x_i - y_i$, which lies between 1 and $2^{k+1} - 1$, so no borrow crosses into the next field, and its top bit is 1 exactly when $x_i \ge y_i$.

25. Induction on $j$ from the longest length down. Pass $j$ adds the strings of length exactly $j$ at the front; their suffix from position $j + 1$ is empty, the smallest of all, so the list is still in order of the suffixes from position $j + 1$. A stable sort by character $j$ then orders by the suffixes from position $j$.

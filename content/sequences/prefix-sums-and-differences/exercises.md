1. ◦ Build the [prefix sums](/prefix-sums/) $P[0 \ldots 7]$ of $a = \langle 2, -1, 3, 0, 4, -2, 5 \rangle$ (indices from 0). Use them to find the sum of $a[2 \ldots 5]$ and of $a[1 \ldots 3]$, inclusive. Which two entries of $P$ does each query read?

2. ◦ Start from six zeros and apply, with the [difference array](/difference-array/) and half-open ranges, $+2$ to $[0, 3)$, $+5$ to $[2, 6)$ and $-1$ to $[1, 2)$. Write the array $d[0 \ldots 6]$ after the three updates and the final array.

3. ◦ Evaluate $\sum_{k=1}^{99} \dfrac{1}{\sqrt{k} + \sqrt{k+1}}$ exactly. (Multiply each term by $\sqrt{k+1} - \sqrt{k}$ over itself.)

4. ◦ Build the table $S$ of [two-dimensional prefix sums](/two-dimensional-prefix-sums/), with its border of zeros, for the grid with rows $\langle 1, 2, 3 \rangle$, $\langle 4, 5, 6 \rangle$, $\langle 7, 8, 9 \rangle$. Compute the sum of the lower-right $2 \times 2$ block from four entries of $S$, and name the four entries.

5. ◦ Compute the prefix XORs of $\langle 5, 3, 6, 1 \rangle$, and from them the XOR of the items at positions 1 and 2. Why is no subtraction needed?

6. ◦ On a $3 \times 3$ grid of zeros, add $1$ to the rectangle $[0, 2) \times [0, 2)$ and $1$ to the rectangle $[1, 3) \times [1, 3)$ with a [two-dimensional difference array](/two-dimensional-difference-array/). Write the $4 \times 4$ grid $D$ and the final grid.

7. ◦ For which of these operations does a prefix table answer every range query with one table operation: addition of integers; XOR; maximum; gcd; multiplication modulo 7; multiplication modulo 8? Where the answer depends on the data, say on what.

8. ◦ In three dimensions, how many entries of the prefix table does the sum of a box $[x_1, x_2) \times [y_1, y_2) \times [z_1, z_2)$ read? Which of them get a minus sign?

9. • Give an $O(n)$ preprocessing after which the weighted sum $\sum_{i=l}^{r-1} (i - l + 1)\, a[i]$ of any range comes out in $O(1)$ time.

10. • Give an $O(n)$ preprocessing after which the mean and the variance of the items of any range $a[l \ldots r-1]$ come out in $O(1)$ time.

11. • First $m$ range adds are applied to an array of $n$ items, and then $q$ queries ask for range sums of the final array. Answer all the queries in $O(n + m + q)$ time.

12. • Use a telescoping sum to show that $\sum_{k=1}^{n} \dfrac{k}{(k+1)!} = 1 - \dfrac{1}{(n+1)!}$.

13. • Use the [Abel summation formula](/abel-summation/) to find a closed form for $\sum_{k=0}^{n-1} k\, c^k$ for any $c \ne 1$. Check it against the value 258 for $c = 2$ and $n = 6$.

14. • A row of $n$ lamps starts off. Each of $m$ operations toggles every lamp in a range $[l, r)$. Find the final state of every lamp in $O(n + m)$ time. Then answer "is lamp $i$ on?" between the toggles, each operation in $O(\log n)$ time.

15. • An $R \times C$ grid holds zeros and ones. Count, in $O(RC)$ time, the $k \times k$ squares of the grid that hold at least $t$ ones.

16. • The *select* query asks for the least $k$ with $P[k] \ge s$. Show that a binary search on a static prefix table answers it in $O(\log n)$ time when all items are non-negative. Give an array with a negative item on which the binary search returns a wrong index.

17. • Point updates and range-sum queries arrive mixed, $q$ operations in all, and you have no tree structure at hand. Keep a prefix table and a list of the updates made since it was last rebuilt, and rebuild it when the list reaches $B$ updates. What does each operation cost? Choose $B$ to make the total time $O(n + q\sqrt{n})$.

18. • Start from the array $\langle 1, 0, 0, \ldots \rangle$ and take prefix sums $k$ times. Prove that the item at position $i$ is then $\binom{i + k - 1}{k - 1}$.

19. ★ Many updates each add $(i - l + 1)^2$ to $a[i]$ for $l \le i < l + m$, with $m \ge 2$, and the final array is read once. Work on the third difference of $a$, which three prefix-sum passes turn back into $a$. Which entries does one update change, and by how much?

20. ★ The falling power is extended to negative exponents by $k^{\underline{-m}} = 1/\big((k+1)(k+2) \cdots (k+m)\big)$. Prove that $\Delta k^{\underline{-m}} = -m\, k^{\underline{-m-1}}$, and use it to show that $\sum_{k=0}^{n-1} \dfrac{1}{(k+1)(k+2)(k+3)(k+4)} = \dfrac{1}{18} - \dfrac{1}{3(n+1)(n+2)(n+3)}$.

21. ★ Count the pairs $l < r$ for which the sum of $a[l \ldots r-1]$ lies between two given bounds $L$ and $U$, in $O(n \log n)$ time. The items may be negative.

22. ★ A tree of fan-out $B$ over the array stores, at each node, the prefix sums of the totals of its children. Show that it solves the [partial sums problem](/partial-sums-problem/) with queries in $O(\log_B n)$ and updates in $O(B \log_B n)$. Choose $B$ so that queries take $O(\log n / \log \log n)$ time and updates $O(\log^{1+\varepsilon} n)$ for a constant $\varepsilon > 0$, and check that this does not contradict the [Fredman-Saks lower bound](/fredman-saks-partial-sums-lower-bound/).

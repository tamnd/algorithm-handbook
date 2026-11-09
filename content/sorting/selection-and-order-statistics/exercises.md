1. ◦ Let $A = \langle 12, 5, 17, 9, 3, 14, 8, 11 \rangle$. Give the [order statistics](/order-statistic/) $a_{(1)}$, $a_{(4)}$ and $a_{(8)}$, the lower and upper [median](/median/), and the quartiles $Q(1/4)$, $Q(1/2)$ and $Q(3/4)$ under the rule $Q(p) = a_{(\lceil pn \rceil)}$. What median does the interpolating rule of R and NumPy give?

2. ◦ Find the minimum and the maximum of $\langle 7, 2, 9, 4, 1, 8, 3, 6 \rangle$ by the pairs method of [minimum and maximum finding](/minimum-and-maximum-finding/). Count the comparisons, and compare the count with that of two separate scans.

3. ◦ Use a knockout [tournament](/tournament-method/) to find the smallest and the second smallest of $\langle 14, 6, 11, 3, 9, 15, 2, 8 \rangle$, pairing neighbours in each round. List the items that lost to the winner, and count all comparisons.

4. ◦ Run [quickselect](/quickselect/) with the [Lomuto partition](/lomuto-partition/), taking the last item of the range as the pivot, to find the third smallest item of $\langle 6, 1, 9, 4, 7, 2, 8, 5 \rangle$. Give the pivot and the array after each partition, and count the comparisons.

5. ◦ Split $\langle 22, 7, 35, 14, 3, 41, 19, 28, 10, 33, 5, 26, 17, 39, 12 \rangle$ into groups of five in the given order. Find the median of each group and the [median of medians](/median-of-medians/) $x$. How many items are sure to be at most $x$, and how many at least $x$, from the group medians alone? Finish the selection of the median of all fifteen items.

6. ◦ By the [selection lower bound](/selection-lower-bound/), at least how many comparisons does any method need, in the worst case, to find the median of 9 items? The second smallest of 9 items? The tournament finds the second smallest of 9 items with how many comparisons, and which of the two numbers is the exact answer?

7. ◦ Find the three smallest items of the stream $\langle 50, 20, 70, 10, 60, 30, 40, 80, 5 \rangle$ with [heap select](/heap-select/), keeping a max-heap of three candidates. Give the set of candidates after each item, and count how many times the top of the heap is replaced.

8. ◦ The keys $\langle 58, 127, 49, 60, 162, 53, 123, 8 \rangle$ are 8-bit numbers. Find the fourth smallest by [radix select](/radix-select/) with digits of $r = 4$ bits, starting from the high digit. Give the counts of the high digits and the bucket that the search enters.

9. ◦ The items $2, 5, 6, 9, 12$ have weights $0.25, 0.1, 0.2, 0.3, 0.15$. Find the lower and upper [weighted median](/weighted-median/), and the value of $f(x) = \sum_i w_i |x - x_i|$ at $x = 5$, $6$ and $9$.

10. • Quickselect with a random pivot looks for the minimum, $k = 1$, and each partition of $m$ items makes $m - 1$ comparisons. Write the recurrence for the expected number of comparisons $C(n)$ and solve it exactly. Check your answer against the general formula in [the expected cost of quickselect](/quickselect-expected-linear/), and evaluate it for $n = 1000$.

11. • Median of medians with groups of an odd size $g$ guarantees about $n(g + 1)/(4g)$ items on each side of the pivot. Write the recurrence for the running time with this group size, and find all odd $g$ for which the two recursive fractions sum to less than 1. What is the sum for $g = 3$, and what running time does the recurrence give then?

12. • Heap select keeps a max-heap of $k$ candidates. Give an order of the input on which the top is replaced at every item after the first $k$, and one on which it is never replaced. For $n$ items, how many comparisons does each order cost, up to lower-order terms?

13. • An algorithm has found, by comparisons, the set of the $k$ smallest items, in no particular order. Give an example with $n = 3$ and $k = 2$ in which the comparisons made so far do not determine the second smallest item. Show that $k - 1$ more comparisons always suffice to find the $k$-th smallest.

14. • Keep two [binary heaps](/binary-heap/), a max-heap for the lower half of the items seen so far and a min-heap for the upper half, so that the lower median is always at the top of the max-heap. For the stream $\langle 5, 15, 1, 3, 8, 7, 9, 10 \rangle$, give the lower median after each item. Show that each new item costs $O(\log n)$ time.

15. • The matrix with rows $\langle 2, 6, 9, 15 \rangle$, $\langle 4, 8, 12, 18 \rangle$, $\langle 7, 11, 16, 21 \rangle$ and $\langle 10, 14, 19, 25 \rangle$ has sorted rows and columns. Count the entries at most 9 and at most 10 with a staircase walk that starts in the bottom-left corner, and use the counts to find the seventh smallest entry. How many cells can the walk visit in an $m \times n$ [sorted matrix](/sorted-matrix-selection/)?

16. • Give an $O(n)$ algorithm that finds the $k$ items closest in value to a given number $t$, which need not be in the array. Run it on $\langle 14, 3, 22, 9, 17, 30, 11, 6 \rangle$ with $t = 12$ and $k = 3$. Say how to handle two items at the same distance from $t$, and compare with [the k nearest to the median](/k-nearest-to-median/).

17. • Four towns lie at $(1, 7)$, $(4, 2)$, $(6, 5)$ and $(9, 1)$, with weights $2$, $1$, $3$ and $2$. Find the point $p$ that minimizes the weighted sum of the Manhattan distances $|p_x - x_i| + |p_y - y_i|$ to the towns, and the minimum sum. Explain why the problem splits into one weighted median for each coordinate, as in the [post office problem](/weighted-median-post-office-location/).

18. • Find the tertiles of $\langle 27, 4, 19, 33, 8, 15, 41, 2, 23, 11, 36, 30 \rangle$, the items of ranks $\lceil jn/3 \rceil$ for $j = 1, 2$, and the three blocks of four items they cut the array into. If [multiple selection](/multiple-selection/) selects rank 8 first and partitions, how many items does the second selection look at? Show that cutting $n$ items into $q$ blocks this way takes $O(n \log q)$ time.

19. • Show that if some value occurs more than $n/2$ times among $n$ items, it is the lower median. Use this to decide in $O(n)$ worst-case time whether an array has a majority value. Run the test on $\langle 4, 7, 4, 2, 4, 4, 9 \rangle$ and on $\langle 3, 8, 3, 5, 8, 8 \rangle$.

20. • Quickselect uses a three-way partition, which puts all items equal to the pivot in the middle and stops if the rank falls there. Show that if the input has only $d$ distinct values, quickselect makes at most $d$ partitions, whatever pivots it picks, and so runs in $O(dn)$ time. How many partitions does it make at most when $d = 2$?

21. ★ The selection lower bound says that the median of five items needs at least six comparisons. Give a method that always finds the median of five items with six comparisons.

22. ★ Prove that any comparison method that finds the smallest and the second smallest of $n$ items needs $n + \lceil \lg n \rceil - 2$ comparisons in the worst case, for every $n \ge 2$, and that the tournament makes no more than that. See [the second-largest lower bound](/second-largest-lower-bound/) for the mirror case.

23. ★ Let $q \ge 2$. Show that every value that occurs more than $n/q$ times among $n$ items appears at one of the ranks $\lceil jn/q \rceil$, $j = 1, \ldots, q$. Use this to find all such values in $O(n \log q)$ time by comparisons. For $n = 12$ and $q = 4$, which ranks must you select?

24. ★ The array is read-only, and you may keep only $O(1)$ words of extra memory besides it. Give a randomized algorithm that finds the item of rank $k$ in $O(n \log n)$ expected time. (You may not move items, so quickselect does not apply as it stands.)

25. ★ Given a function that finds the unweighted median of $n$ items in $O(n)$ worst-case time, find the weighted $p$-quantile of $n$ distinct weighted items, for any $0 < p < 1$, in $O(n)$ worst-case time. This is the smallest item $x$ such that the items at most $x$ weigh at least $pW$, where $W$ is the total weight.

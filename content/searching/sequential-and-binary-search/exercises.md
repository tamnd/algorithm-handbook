1. ◦ Run [binary search](/binary-search/), with the half-open range $[lo, hi)$ of its entry, on $A = \langle 3, 9, 14, 20, 27, 31, 40, 52 \rangle$ for $x = 20$ and for $x = 28$. Give $lo$, $hi$ and $mid$ at each step. Where would 28 be inserted to keep the array sorted?

2. ◦ For $A = \langle 1, 2, 2, 2, 5, 7, 7, 9 \rangle$, give the [lower bound](/lower-bound-query/) $\ell$ and the [upper bound](/upper-bound-query/) $u$ of each key $x = 2, 7, 6, 0, 10$. For which keys is $u - \ell$ the number of copies, and what is it?

3. ◦ For which $n$ does binary search make exactly 10 comparisons in the worst case? How many does it make for $n = 1000$ and for $n = 1024$?

4. ◦ Run [exponential search](/exponential-search/) on a sorted array of $10^6$ distinct items for a key whose lower bound is 37. Which indices does the doubling phase read? What range $[lo, hi]$ does the binary search phase get, and how many comparisons does the search make in all?

5. ◦ Run [interpolation search](/interpolation-search/) on $A = \langle 1, 2, 4, 8, \ldots, 512 \rangle$ (the ten powers of 2) for $x = 8$. List the probed indices. Then run it on $A = \langle 10, 20, 30, \ldots, 1000 \rangle$ for $x = 470$.

6. ◦ Run the search of [minimum of a rotated sorted array](/rotated-sorted-array-minimum/), which compares the middle item with the last item of the range, on $\langle 40, 45, 50, 5, 10, 20, 30 \rangle$. How many comparisons does it make, and what index does it return?

7. ◦ List every peak of $A = \langle 1, 3, 4, 3, 5, 1, 2, 6, 5 \rangle$. Which one does the slope search of [peak finding](/peak-finding/) return, and after which probes?

8. ◦ The matrix below has sorted rows and sorted columns. Run [staircase search](/staircase-search/) from the top-right corner for $x = 13$ and for $x = 15$, and list the cells it reads.
$$\begin{pmatrix} 1 & 4 & 7 & 11 \\ 2 & 5 & 8 & 12 \\ 3 & 6 & 9 & 16 \\ 10 & 13 & 14 & 17 \end{pmatrix}$$

9. ◦ Write the [Eytzinger layout](/eytzinger-layout/) of the sorted items $10, 20, \ldots, 100$ in slots 1 to 10. Then search it for the lower bound of $x = 65$: which slots are read, at which slot $k > n$ does the walk stop, and which slot holds the answer?

10. ◦ A list holds $a, b, c$ in this order. Requests come for $c, c, b, c, a$, and each costs the position of the item (1 for the front). What is the total cost under [move to front](/self-organizing-list-search/)? What is the cost of the best fixed order for this sequence?

11. ◦ Run the cut search of [median of two sorted arrays](/median-of-two-sorted-arrays/) on $A = \langle 1, 3, 8, 9, 15 \rangle$ and $B = \langle 7, 11, 18, 19, 21, 25 \rangle$ with $k = 6$. How many of the six smallest items come from $A$, and what is the median?

12. • Prove that $\lfloor \lg n \rfloor + 1 = \lceil \lg(n+1) \rceil$ for every integer $n \ge 1$.

13. • A sorted array holds $n$ distinct integers. Find an index $i$ with $A[i] = i$, if there is one, in $O(\log n)$ time. Why does your method need the items to be distinct?

14. • *Ternary search* on a sorted array compares $x$ with the items at one third and two thirds of the range and keeps one of the three parts. Show that it makes about $2 \log_3 n \approx 1.26 \lg n$ comparisons in the worst case, more than binary search.

15. • In an array of distinct keys, each item is at most one place away from where it would be in sorted order. Find a key in $O(\log n)$ time.

16. • The scan of [finding the maximum](/find-maximum/) changes its "largest so far" each time it meets an item larger than all before it. Show that on a uniform random order of $n$ distinct items, the expected number of such items, counting the first, is the harmonic number $H_n$. What is it for $n = 4$?

17. • A sorted array can be read only through a function $get(i)$, which returns $+\infty$ for $i \ge n$, and $n$ is not known. Find $n$ with $2\lfloor \lg n \rfloor + O(1)$ calls.

18. • Show that the greedy walk "move to the largest neighbour while it is larger than the current cell" can take $\Theta(n^2)$ steps on an $n \times n$ grid before it stops at a local maximum.

19. • Given a rotated sorted array of $n$ distinct items, return the $k$-th smallest item in $O(\log n)$ time.

20. • For sorted arrays $a$ of length $m$ and $b$ of length $n$, count the pairs $(i, j)$ with $a[i] + b[j] \le x$ in $O(m + n)$ time, without building the matrix of sums.

21. • Interpolation search takes $\Theta(n)$ probes on some inputs. Change it so that the worst case is $O(\log n)$ probes while every interpolation probe is kept, and give the bound.

22. • An array of distinct keys first increases and then decreases. Find a key $x$ in it with at most about $3 \lg n$ comparisons.

23. • Find the $k$-th smallest item of the union of two sorted arrays of lengths $m$ and $n$ in $O(\log \min(m, n, k))$ time.

24. ★ A key occurs exactly once in an unordered array of $n$ items. Show that every randomized algorithm that always finds it reads, on some input, at least $(n+1)/2$ items on average. Give an algorithm that reads exactly $(n+1)/2$ on average for every input.

25. ★ Give an algorithm that finds a local maximum of an $n \times n$ grid (a cell at least as large as its four neighbours) by reading $O(n)$ cells.

26. ★ In the [unbounded search](/unbounded-search/) problem, a test $P(i)$ is false for $i < N$ and true from $N$ on. Find $N$ with $\lg N + 2\lg \lg N + O(1)$ tests.

27. ★ *Interpolation-sequential search* makes one interpolation probe and then scans from it, left or right, to the key. Show that on $n$ keys drawn independently from the uniform distribution on $[0, 1]$, and a fixed key $x$, it reads $O(\sqrt{n})$ items on average.

28. ★ Prove that for every request sequence of length $m$ to a list of $n$ items, [move to front](/self-organizing-list-search/) costs at most $2C - m$, where $C$ is the cost of serving the same requests with any fixed order of the items, if both start in that fixed order.

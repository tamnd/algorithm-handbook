1. ◦ Run [odd-even transposition sort](/odd-even-transposition-sort/) on $\langle 5, 1, 4, 2, 3 \rangle$, starting with the round that compares positions $(0, 1)$ and $(2, 3)$. Show the keys after each round. After which round are they sorted, and how many compare-exchanges do the five rounds make in all?

2. ◦ Merge $A = \langle 3, 5, 8 \rangle$ and $B = \langle 1, 5, 6, 9 \rangle$ by ranking, as in the [parallel merging problem](/parallel-merging-problem/): each $A[i]$ goes to position $i$ plus the number of keys of $B$ less than $A[i]$, and each $B[j]$ to position $j$ plus the number of keys of $A$ at most $B[j]$. Give all seven positions. What goes wrong if both lists count the keys less than themselves?

3. ◦ A parallel sort has work $n \lg n$ and span $\lg^3 n$, for $n = 2^{20}$. What is its parallelism, the work divided by the span? Use [Brent's theorem](/brent-theorem/) to bound its time on $p = 1024$ processors, and say which of the two terms is larger.

4. ◦ Run [shearsort](/shearsort/) on the $4 \times 4$ matrix with rows $\langle 3, 11, 6, 16 \rangle$, $\langle 8, 1, 14, 9 \rangle$, $\langle 12, 15, 2, 5 \rangle$, $\langle 7, 4, 13, 10 \rangle$. Show the matrix after every row phase and every column phase. If each row or column sort is an odd-even transposition sort, how many steps does the whole sort take, and how does that compare with the lower bound of the [mesh sorting problem](/mesh-sorting-problem/)?

5. ◦ Sort the 16 keys $52, 17, 88, 5, 63, 29, 94, 41, 70, 12, 36, 81, 23, 58, 9, 47$ by [sample sort](/sample-sort/) with $p = 4$ and $s = 2$. The draws are $52, 5, 70, 29, 88, 41, 12, 63$, and a key equal to a splitter goes to the lower bucket. Give the splitters and the four buckets. Is any bucket larger than $2n/p$?

6. ◦ One pass of [parallel radix sort](/parallel-radix-sort/) sorts the digits $\langle 3, 1, 2, 0, 3, 2, 1, 1 \rangle$ with $R = 4$ digit values on $p = 2$ processors; processor 0 holds the first four keys and processor 1 the last four. Give each processor's digit counts, the prefix sums that give the starting slot for each pair of digit and processor, and the slot that processor 1's key $2$ is written to.

7. ◦ Merge $A = \langle 2, 5, 7, 8 \rangle$ and $B = \langle 1, 3, 4, 6, 9, 10 \rangle$ with [merge path](/merge-path/) on $p = 3$ processors that take $3$, $3$ and $4$ output items. Give the co-ranks of diagonals $3$ and $6$, and the part of $A$ and of $B$ that each processor merges.

8. ◦ Run [hyperquicksort](/hyperquicksort/) on $p = 4$ processors holding $\{0, 1, 2, 3\}$, $\{4, 5, 6, 7\}$, $\{8, 9, 10, 11\}$ and $\{12, 13, 14, 15\}$. Each pivot is the lower median of the list of the lowest-numbered processor of its subcube. Give the lists after each round and the final loads.

9. ◦ For $n = 16$, compute three lower bounds from the [parallel sorting depth lower bound](/parallel-sorting-depth-lower-bound/): the fan-in bound for a comparator network, the counting bound for a network whose layers have at most $8$ comparators, and the counting bound for the parallel comparison model with $16$ processors. Use $\lceil \lg 16! \rceil = 45$. Compare them with the depth $10$ of bitonic sort.

10. • Show that for every even $n \ge 4$, odd-even transposition sort started with the round that compares $(0, 1)$ needs all $n$ rounds on the input $\langle 2, 3, \ldots, n - 1, 0, 1 \rangle$. So $n - 1$ rounds are not enough.

11. • Odd-even transposition sort with $p$ processors and $n/p$ keys each first sorts each block, then runs $p$ rounds in which neighbours merge their blocks and split them into a lower and an upper half. Give its time, and the largest $p$ for which it is work-efficient.

12. • A line of $p$ processors holds $n/p$ keys each, and each link carries one key per step in each direction. Show that some input needs at least about $n/2$ steps. For which $p$ is the block sort of Exercise 11 within a constant factor of this bound?

13. • Split an array stably by one bit, the keys whose bit is $0$ first, with one prefix sum. If $s[i]$ is the number of zero bits before position $i$ and $Z$ is the total number of zero bits, show that key $i$ goes to $s[i]$ if its bit is $0$ and to $Z + i - s[i]$ if it is $1$. Apply this to bit $0$ of $\langle 5, 2, 7, 4, 1, 6 \rangle$. This is one pass of a radix sort with $1$-bit digits.

14. • Rank sort uses $n^2$ processors on the [CREW PRAM](/crew-pram/): one processor for each pair $(i, j)$ compares the keys $i$ and $j$, and the rank of key $i$ is the sum of its row. Give the time and the work, and say why it is not work-efficient. Can any sort run in constant time on a CRCW PRAM with polynomially many processors?

15. • Find the largest of $n$ keys in $O(1)$ time on a common [CRCW PRAM](/crcw-pram/) with $n^2$ processors. Then show that on the CREW PRAM no number of processors finds the largest key in $o(\log n)$ time.

16. • In [regular sampling](/parallel-sorting-by-regular-sampling/), let each processor take $ps$ evenly spaced samples instead of $p$, and take every $ps$-th of the $p^2 s$ sorted samples as a splitter. For distinct keys, show that no processor receives more than $(1 + 1/s) n/p - p$ keys.

17. • Run [parallel merge sort](/parallel-merge-sort/) on the CREW PRAM with $p$ processors, using [Shiloach-Vishkin merging](/shiloach-vishkin-merge/) at every level, with the processors shared among the merges of a level in proportion to their lengths. Show that the time is $O((n/p) \log n + \log^2 n)$, and find the $p$ for which the speedup is linear.

18. • In the parallel comparison model with $n$ processors, use [Valiant's merge](/valiant-parallel-merge/) at every level of a merge sort. How many rounds does the sort take? Compare with the bound of [Cole's merge sort](/cole-merge-sort/).

19. • The zero-one principle holds only for oblivious sorts. On three positions, do a compare-exchange on $(0, 1)$, then on $(1, 2)$, then one more on $(0, 1)$, but only if the keys at positions $0$ and $2$ are equal. Show that this sorts every input of zeros and ones but not $\langle 3, 2, 1 \rangle$.

20. • Radix sort sorts $n = 2^{24}$ keys of $w = 32$ bits on $p = 2^8$ processors, and one pass with $b$-bit digits costs $n/p + 2^b + \lg p$ steps. Find the total cost for $b = 4, 8, 11$ and $16$, and the best $b$.

21. • Show that every comparator of [bitonic sort](/bitonic-sort/) on $n = 2^d$ wires joins two wires $i$ and $i \oplus 2^j$ whose numbers differ in one bit. Conclude that a hypercube of $n$ processors, one key each, runs bitonic sort in $d(d + 1)/2$ steps.

22. ★ Run sample sort with $s = 1$, so that the $p - 1$ splitters come from a random sample of $p$ keys. Show that with probability at least $1 - n^{-2}$, every bucket has at most $3 (n/p) \ln n$ keys. Compare with the bound for $s = \Theta(\log n)$.

23. ★ A primitive sorting network has comparators only between neighbouring wires $k$ and $k + 1$. Show that it has at least $n(n-1)/2$ comparators and, for $n \ge 3$, depth at least $n$. Conclude that odd-even transposition sort is optimal among primitive networks in both size and depth.

24. ★ In the parallel comparison model with $n$ processors, find the largest of $n$ keys in $O(\log \log n)$ rounds. Why does this not contradict the $\lg n$ fan-in bound for networks?

25. ★ In shearsort on an $r \times r$ mesh, show that column phase $k$ needs only $r / 2^{k-1}$ rounds of odd-even transposition. Show that the whole sort then takes $\sqrt n (\tfrac12 \lg n + 3) - 2$ steps, and check it on Exercise 4.

26. ★ [Columnsort](/columnsort/) on an $r \times s$ matrix needs $s$ to divide $r$. For $s = 3$, find the smallest $r$ for which it sorts every input, and give an input of zeros and ones on which it fails for $r = 6$. Do the same search for $s = 4$, and compare the results with the condition $r \ge 2(s-1)^2$.

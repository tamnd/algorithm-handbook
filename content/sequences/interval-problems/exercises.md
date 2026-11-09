1. ◦ Run [interval merging by sorting](/interval-merging-sort/) on the closed intervals $[5, 7], [1, 2], [2, 4], [8, 9], [6, 6], [3, 5]$. Show the sorted order and the output. What is the output if the intervals are sets of integers, so that $[1, 3]$ and $[4, 5]$ count as joined?

2. ◦ Run the [sweep for union length](/sweep-union-length/) on $[0, 6], [2, 4], [3, 8], [7, 10]$. What is the length of the union? What is the length of the part covered by at least two intervals, and what is the largest coverage at any point?

3. ◦ Intersect the closed lists $A = [1, 4], [6, 8], [10, 15]$ and $B = [0, 2], [3, 7], [8, 11], [14, 20]$ with the [two-pointer scan](/interval-list-intersection-two-pointers/). List the output and the number of steps of the loop. Which pieces disappear if all the intervals are half-open?

4. ◦ Run [interval containment by sorting](/interval-containment-sort/) on the closed intervals $[2, 5], [1, 6], [2, 7], [3, 4], [6, 9], [7, 9]$. Give the order after the sort and the intervals that are kept as maximal.

5. ◦ Take the intervals with end points $(1, 4), (2, 3), (4, 6), (5, 8), (3, 5)$. Find the depth and the first point where the [sweep](/sweep-maximum-overlap/) reaches it, once for closed and once for half-open intervals. Then run the [partitioning greedy](/interval-partitioning-greedy/) on the closed intervals and give the resources it opens.

6. ◦ Cover the closed target $[0, 10]$ with the closed intervals $[0, 3], [1, 5], [2, 4], [4, 8], [5, 10], [7, 9]$ using the [covering greedy](/interval-covering-greedy/). Then cover $(0, 10)$ with the open intervals of the same end points. How many intervals does each cover use, and why do they differ?

7. ◦ Run the [piercing greedy](/interval-piercing-greedy/) on the closed intervals $[1, 3], [2, 5], [4, 6], [6, 9], [7, 8], [10, 11]$. Give the points, and a set of pairwise disjoint intervals that proves no smaller set of points exists.

8. ◦ Store the intervals with end points $(1, 4), (2, 6), (5, 9), (6, 7), (8, 10)$. Use the counting formula of [interval stabbing queries](/interval-stabbing-query/), with two binary searches, to count the intervals that contain $p = 6$, once for closed, once for half-open and once for open intervals. Check each count by listing the intervals.

9. ◦ Name the relation of [Allen's interval algebra](/allens-interval-algebra/) that holds from $X$ to $Y$ for each pair, written as end point pairs: $X = (2, 5)$, $Y = (5, 9)$; $X = (3, 6)$, $Y = (1, 6)$; $X = (1, 4)$, $Y = (1, 8)$; $X = (2, 7)$, $Y = (4, 9)$; $X = (4, 5)$, $Y = (1, 9)$; $X = (6, 8)$, $Y = (2, 4)$. Which of these pairs share a point as closed sets but not as half-open sets?

10. • Run the [weighted interval dynamic program](/weighted-interval-dp/) on the half-open intervals $a = [0, 4)$, $b = [1, 3)$, $c = [3, 6)$, $d = [4, 7)$, $e = [6, 9)$, $f = [7, 8)$ with weights $3, 2, 4, 4, 3, 2$. Give $p[j]$ and $M[j]$ for each $j$ in the sorted order and the optimal weight. Then change the recurrence so that it also counts the optimal sets, and use it to find how many optimal sets this input has.

11. • Each greedy rule below is wrong. Give a small input on which it fails, and the correct answer. (a) To cover a target, take the longest interval first, then cover what is left. (b) To pierce intervals, sort by left end and put a point at the right end of the first interval not yet hit. (c) To choose disjoint weighted intervals, use [earliest finish time first](/earliest-finish-time-first/).

12. • Find the fewest intervals to remove from the half-open intervals $[0, 5), [1, 2), [2, 4), [3, 6), [5, 7), [6, 8)$ so that the rest are pairwise disjoint. Prove that for any family the answer is $n - \nu$, where $\nu$ is the largest number of pairwise disjoint intervals, and say which algorithm of the chapter computes it in $O(n \log n)$ time.

13. • Two people are busy at the half-open times $[9, 10), [12, 13), [16, 17)$ and $[10, 11), [13, 14), [15, 16)$, each list sorted. Find the times in $[9, 17)$ when both are free. Give an algorithm that does this for two sorted lists of lengths $m$ and $n$ in $O(m + n)$ time.

14. • A *nested chain* is a sequence of intervals, each properly containing the next. Sort distinct closed intervals by left end ascending and, at equal left ends, by right end descending. Show that the nested chains are exactly the subsequences whose right ends do not increase. Use this to find a longest nested chain of $[1, 10], [2, 9], [3, 4], [2, 5], [5, 8], [6, 7], [3, 9]$, with a [longest increasing subsequence](/longest-increasing-subsequence/) method.

15. • Count the pairs of overlapping closed intervals among $n$ intervals in $O(n \log n)$ time, even when there are $\Theta(n^2)$ such pairs. Check your method on $[1, 3], [2, 5], [4, 6], [7, 8]$.

16. • Compute these compositions in Allen's algebra and justify each from the end point conditions: starts $\circ$ during, meets $\circ$ overlaps, and finishes $\circ$ finished by.

17. • In the unit-weight problem on [$k$ machines](/k-machine-interval-scheduling/), the jobs are taken in order of right end, and each job goes to a free machine or is rejected. Show that for $k = 2$ the choice of the free machine matters: give four half-open jobs on which giving each job to the free machine whose last job ends *latest* accepts all four, but giving it to the one whose last job ends *earliest* accepts only three.

18. • A family of arcs of a circle is to be pierced by the fewest points. Fix any point $q$ of the circle, put a point at $q$, cut the circle at $q$, and run the line greedy on the arcs that do not contain $q$. Show that this uses at most one point more than the optimum.

19. • The end points of $n$ half-open intervals $[l_j, r_j)$ are integers in $\{0, 1, \ldots, U\}$. Find the depth in $O(n + U)$ time with a [difference array](/difference-array/). What changes for closed intervals of integers?

20. • Start from the [PQ-tree](/pq-tree/) UNIVERSAL$(\{1, 2, 3, 4, 5\})$ and reduce it by $\{1, 2\}$, then by $\{2, 3\}$, then by $\{3, 4\}$. Draw the tree after each step and count the orders it stores. What happens if you then reduce by $\{1, 4\}$?

21. ★ Let a family of closed intervals cover the closed target $[s, t]$. Prove that the fewest intervals of the family that cover $[s, t]$ equals the largest number of points of $[s, t]$ no two of which lie in a common interval of the family. Use the run of the [covering greedy](/interval-covering-greedy/) to find the points.

22. ★ Each closed interval $I_j$ has a cost $w_j \ge 0$. Give an $O(n \log n)$ algorithm for a cover of the target $[s, t]$ of least total cost, and prove it correct.

23. ★ Each closed interval $[l_j, r_j]$ of integers asks for at least $k_j$ chosen integers inside it, with $k_j \le r_j - l_j + 1$. Show that this greedy chooses the fewest integers: take the intervals by right end, and when an interval still lacks $c$ points, add the $c$ largest integers of it not yet chosen. Run it on $[0, 4], [2, 6], [5, 8], [7, 9]$ with $k_j = 2$ for all $j$.

24. ★ For closed intervals write $I \prec J$ when $r_I < l_J$. Show that $\prec$ is a strict partial order, that its chains are the sets of pairwise disjoint intervals, and that its antichains are the sets of pairwise meeting intervals. Then use [Dilworth's theorem](/dilworth-theorem/) and the [Helly property](/helly-property-intervals/) to give a second proof of the [depth theorem](/interval-coloring-depth-theorem/). Finally show that $\prec$ has no four intervals with $A \prec B$ and $C \prec D$ while $A, D$ meet and $C, B$ meet.

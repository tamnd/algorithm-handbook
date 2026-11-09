1. ◦ Run the [pair search](/two-pointer-pair-search/) on $A = [2, 5, 7, 9, 12, 15, 20]$, once with $t = 21$ and once with $t = 30$. For each run list the pairs $(A[lo], A[hi])$ that the loop tests, and say what it returns and after how many iterations.

2. ◦ Run [Dijkstra's three-way partition](/dutch-national-flag-algorithm/) on $A = [2, 0, 1, 2, 1, 0]$ with pivot $p = 1$. Give the array and the values of $lo$, $mid$ and $hi$ after each iteration, the number of swaps, the number of those swaps that exchange an item with itself, and the pair that the procedure returns.

3. ◦ Compact the sorted array $[1, 1, 1, 2, 2, 3, 3, 3, 3, 4]$ in place so that each value appears at most twice, with a read index $r$ and a write index $w$ and the test "$w < 2$ or $A[r] \ne A[w - 2]$" of [removing duplicates](/remove-duplicates-from-sorted-array/). Give the final value of $w$ and the prefix $A[0 \ldots w-1]$.

4. ◦ Compute the multiset [intersection](/sorted-array-intersection/) of $A = [1, 3, 4, 4, 7, 9, 12]$ and $B = [2, 3, 4, 4, 4, 9, 10, 12, 15]$ with the merge-like scan. How many three-way comparisons does the scan make, and how far is this from the bound $m + n - 1$?

5. ◦ A function $f$ has $f(7) = 5$, $f(5) = 8$, $f(8) = 1$, $f(1) = 4$, $f(4) = 9$, $f(9) = 2$ and $f(2) = 4$. Start at $x_0 = 7$ and run the method of [fast and slow pointers](/fast-and-slow-pointers/). Find the tail length $\mu$, the cycle length $\lambda$, the number $\nu$ of steps until the two pointers meet, the item where they meet, and the total number of evaluations of $f$.

6. ◦ For the string $s = $ abccbadb, give the left end $L(r)$ of the window after each step $r = 0, \ldots, 7$ of the [sliding window for the longest distinct substring](/sliding-window-longest-substring/), and the answer. Then run the faulty version that sets the left end to $p(r) + 1$, where $p(r)$ is the last earlier position of $s_r$, without taking the maximum with the old left end. What length does it report, and for which window?

7. ◦ Run the [monotonic deque](/sliding-window-maximum-deque/) on $A = [4, 2, 12, 3, 8, 7, 1, 6]$ with $k = 3$. Give the output $M$, the deque of indices after step $r = 5$, the step at which line L5 removes an index from the front, and the number of value comparisons in line L3.

8. ◦ Find the water held by the bars $h = [3, 0, 2, 0, 4, 0, 1, 3]$ in [trapping rain water](/trapping-rain-water/). Give the water above each bar and the total.

9. • In the scan of the [container with most water](/container-with-most-water/), the code moves the left index when $h_i \le h_j$. Prove that when $h_i = h_j$ the scan may move both indices at once and still return the optimum.

10. • Count the pairs $i < j$ with $A[i] + A[j] = 6$ in the sorted array $A = [1, 2, 2, 3, 3, 3, 4, 5]$. Then change the pair search so that it counts all such pairs in $O(n)$ time when values repeat, and say what it adds when $A[lo] + A[hi] = t$.

11. • Change the [3SUM scan](/three-sum-two-pointer-scan/) so that it returns a triple whose sum is closest to a target $t$. Run it on $A = [-8, -3, 1, 5, 6, 12]$ with $t = 7$ and give the triple and its sum. What is the running time?

12. • The array $[2, 2, 0, 1, 0, 1, 2, 0]$ is to be sorted into its three blocks. How many swaps does [Dijkstra's three-way partition](/dutch-national-flag-algorithm/) with $p = 1$ make, and how many of them exchange two different positions? What is the smallest number of swaps that sorts this array, by the formula of the [Dutch national flag problem](/dutch-national-flag/)?

13. • A window of a string is *good* if at most $k$ of its characters must be changed to make all its characters equal, that is, if its length minus the largest count of one character is at most $k$. Prove that this property is down-closed, so the [sliding window](/sliding-window/) template applies. Find the longest good window of ABBACBBAB for $k = 2$ and for $k = 1$.

14. • Run the template LONGEST-WINDOW of the [sliding window](/sliding-window/) with the test "the sum of the window is even" on $A = [1, 2, 1]$. What does it return, and what is the right answer? Which condition of the [monotone window property](/monotone-window-property/) fails?

15. • Find the [minimum window substring](/minimum-window-substring/) of BACDAEBA for the pattern ABA, in which A must appear twice. Give the window and its length, and show that no shorter window works.

16. • The array $A[0 \ldots 6] = [4, 6, 1, 5, 3, 2, 4]$ holds values in $1, \ldots, 6$, so some value repeats. Follow $x_0 = 0$ and $x_{i+1} = A[x_i]$ as in the duplicate search of [fast and slow pointers](/fast-and-slow-pointers/). Give $\mu$, $\lambda$ and $\nu$, and the repeated value that the method returns.

17. • Prove that a row of bars traps no water if and only if its heights first do not decrease and then do not increase. Use the formula $w_i = \min(\max_{j \le i} h_j, \max_{j \ge i} h_j) - h_i$ of [trapping rain water](/trapping-rain-water/).

18. • In the keep-at-most-$c$ compaction of exercise 3, a programmer tests $A[r] \ne A[r - c]$ in place of $A[r] \ne A[w - c]$. Show that with $c = 2$ this gives a wrong answer on $[0, 0, 0, 1, 1]$, and explain why the test that reads the original array at $r - c$ fails when it runs in place.

19. ★ Find the 7th smallest of the $15$ differences $A[j] - A[i]$, $i < j$, of the sorted array $A = [1, 3, 4, 7, 8, 12]$. Give a method that finds the $k$-th smallest pair difference of a sorted array of $n$ integers in $O(n \log D)$ time, where $D$ is the largest difference, and prove that its count step is correct.

20. ★ Three sorted lists are $[1, 5, 9]$, $[4, 11, 14]$ and $[6, 8, 15]$. Find the shortest range $[a, b]$ that contains at least one item of each list. Give a method for $k$ lists with $N$ items in total in $O(N \log k)$ time, which keeps one pointer in each list, and prove that it does not skip the optimum.

21. ★ The items of $A$ may be negative, so the sliding window fails for "the sum is at most $s$". Give an $O(n \log n)$ method for the longest subarray with sum at most $s$, using the [prefix sums](/prefix-sums/) and their running maxima. Apply it to $A = [2, -3, 4, -1, 3, -5, 2]$ with $s = 1$.

22. ★ Count the triples $i < j < k$ with $A[i] + A[j] + A[k] < 3$ in the sorted array $A = [-3, -1, 0, 2, 4, 5]$. Give an $O(n^2)$ method for any sorted $A$ and target $t$, based on the [3SUM scan](/three-sum-two-pointer-scan/), and prove that it counts each triple once.

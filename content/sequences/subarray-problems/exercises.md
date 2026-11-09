1. ◦ Run [Kadane's algorithm](/kadane-algorithm/) on $A = [3, -4, 2, -1, 3, -5, 4]$. Give $cur$ and $best$ after each step. Two subarrays reach the largest sum; which one does the algorithm report, and why?

2. ◦ An array has 6 items. How many non-empty [subarrays](/subarray/) does it have, and how many of them have length 3? How many non-empty subsequences does it have?

3. ◦ Find the [maximum circular subarray sum](/maximum-circular-subarray-sum/) of the ring $[2, -6, 3, -1, 4, -7, 5]$. Give the largest plain sum, the smallest plain sum and the total, and say which run is the answer.

4. ◦ Run the [max-product scan](/kadane-max-product/) on $A = [2, -5, -2, -4, 3]$. Give $hi$ and $lo$ after each step, and the answer.

5. ◦ Run the [histogram stack algorithm](/histogram-stack-algorithm/) on $h = [3, 1, 3, 2, 2]$. List the pops in order, with the width and area of each. Which pop gives the answer? Which bar gets a width that is too short, and why is the answer still right?

6. ◦ For $A = [1, -1, 1, -1, 1]$, how many subarrays have sum $0$? How long is the [longest zero-sum subarray](/longest-zero-sum-subarray/)? Answer both from the prefix sums.

7. ◦ Find the window of length $3$ with the largest sum in $A = [4, -2, 7, 1, -3, 6, 5]$. How many additions and subtractions does the rolling sum of [maximum sum subarray of fixed length](/maximum-sum-subarray-of-fixed-length/) make on it?

8. ◦ Run the [sliding window for positive sums](/sliding-window-positive-sum/) on $A = [3, -2, 4]$ with $s = 4$, ignoring that the items must not be negative. What length does it return, and what is the right answer? Say which step goes wrong.

9. ◦ Compute the prefix XORs of $A = [5, 1, 6, 2]$ and find its [maximum XOR subarray](/maximum-xor-subarray/).

10. • Kadane's algorithm can be written with the prefix sums: keep the running prefix sum $P$ and the smallest earlier prefix sum $m$, and take $\max(best, P - m)$ at each step. Prove that after step $j$ the value $P_j - \min_{a < j} P_a$ equals $cur$ of the algorithm as its entry gives it.

11. • Change Kadane's algorithm so that among all maximum subarrays it reports one of least length. Prove your change correct.

12. • The [divide-and-conquer algorithm](/maximum-subarray-divide-and-conquer/) becomes linear if each call returns four values: the total, the best prefix sum, the best suffix sum and the best subarray sum. Prove that the combine rules of its entry are correct. Then compute the four values for $[3, -4, 2, -1]$ and $[3, -5, 4]$ and join them.

13. • Count the subarrays of $A = [3, 1, 4, 1, 5]$ whose sum is divisible by $5$. Then give a method that counts the subarrays with sum divisible by $m$ in $O(n + m)$ worst-case time, for items of any sign.

14. • Use [two pointers with distinct counts](/distinct-count-two-pointers/) to count the subarrays with at most $k$ distinct values. Then count the subarrays of $A = [1, 2, 1, 3, 2]$ with exactly two distinct values.

15. • For $A$ with distinct items, the sum of the minimums of all its subarrays can be found in $\Theta(n)$ time with a monotonic stack. Give the method, and check it on $A = [3, 1, 2, 4]$. How must ties be broken when items repeat?

16. • Count the submatrices of an $m \times n$ matrix, $m \le n$, whose sum is exactly $t$, in $O(m^2 n)$ expected time.

17. • Find the largest sum of a subarray whose length is between $L = 2$ and $U = 3$ in $A = [2, -1, 3, -4, 5, -1, 2]$. Then give an $O(n)$ method for any $L \le U$.

18. • Find the largest sum of a non-empty subarray from which at most one item may be deleted, with the result still non-empty, in $O(n)$ time. Apply it to $A = [2, -5, 3, -1, 4, -6, 1]$.

19. • Find the longest subarray of the binary array $[0, 1, 1, 0, 1, 1, 1, 0]$ with as many $0$s as $1$s, by reduction to the longest zero-sum subarray.

20. • Prove that if every item is a non-zero integer and $n \ge 2$, some [maximum product subarray](/maximum-product-subarray/) is a prefix or a suffix of the array. Say which one, in terms of the negative items.

21. ★ Count the subarrays whose sum lies in a range $[lo, hi]$ in $O(n \log n)$ time, for items of any sign. Check your method on $A = [1, -3, 2, 4]$ with $lo = 0$ and $hi = 3$.

22. ★ Count the rectangles of a binary matrix that contain only ones, in $O(rc)$ time for an $r \times c$ matrix. Check your method on the matrix with rows $[1, 0, 1]$ and $[1, 1, 1]$.

23. ★ In the [maximum density segment](/maximum-density-segment/) problem with unit widths and a minimum length $L$, prove that some optimal segment has length less than $2L$. Use this to give an $O(nL)$ algorithm.

24. ★ Give an $O(nk)$ dynamic program for the [k-maximum subarray problem](/k-maximum-subarray-problem/), with at most $k$ disjoint subarrays. Compute $g(1)$, $g(2)$ and $g(3)$ for $A = [3, -2, 6, -5, 7]$, and check that the greedy merging of runs in the entry gives the same increments.

25. ★ For a modulus $m$ and non-negative items, find the largest value of $(A[i] + \dots + A[j]) \bmod m$ over all subarrays in $O(n \log n)$ time. Apply your method to $A = [5, 8, 2, 7, 4]$ with $m = 10$.

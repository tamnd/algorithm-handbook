1. Each run of line L5 removes one inversion and changes no other pair. The input has 9 inversions, so line L5 runs 9 times.

3. Insertion sort makes $n - 1$ comparisons: each new item stops at once. Selection sort makes $n(n-1)/2$ whatever the input. The Lomuto partition sends every item that is not larger than the pivot to the left, so each partition peels off only the pivot, and quicksort makes $n(n-1)/2$ comparisons.

5. The first comparison is $a_1 : a_2$. Then $a_3$ is compared with the larger of the two, and, if it is smaller, with the other one. The tree has 6 leaves and height 3, and $\lceil \lg 6 \rceil = 3$, so no comparison sort does better on three items.

6. Six comparisons. Four suffice for $\langle 1, 2, 3, 4 \rangle$ and $\langle 5, 6, 7, 8 \rangle$: once one list is used up, the rest of the other is copied with no comparison.

7. The array becomes $\langle 2, 1, 3, 4, 7, 5, 6, 8 \rangle$ and the partition returns index 3 (counting from 0).

8. $\langle 16, 14, 10, 8, 7, 9, 3, 2, 4, 1 \rangle$.

9. For stability, insert the new item after every item with an equal key: search for the first item that is strictly larger. On input in reverse order, item $i$ still moves $i$ places.

11. Cycle sort writes each item at most once.

12. Solve $W(n) = 2W(n/2) + n - 1$ with $W(1) = 0$. An input that needs every comparison interleaves the halves at every level, such as $\langle 1, 5, 3, 7, 2, 6, 4, 8 \rangle$.

14. In both cases the pivot is the smallest or the largest item of its range at every step. Check that this stays true after each partition, so the sizes of the ranges go $n, n-1, n-2, \ldots$

15. Both scans stop at every item equal to the pivot, so the two indices swap and step towards each other and meet near the middle. The splits are nearly even, and the recurrence is $T(n) = 2T(n/2) + \Theta(n)$.

16. The smaller side has at most half of the items, so each nested recursive call works on at most half the size of the call above it.

17. If $A[i] > A[j]$ with $i < j$, then $j - i < 2k$, so there are fewer than $2nk$ inversions. For $O(n \log k)$, keep a min-heap of the next $k + 1$ items: the smallest item still unplaced is always among them.

18. Compare the pairs $(key, i)$, where $i$ is the item's position in the input. This needs $\Theta(n)$ extra space for the positions, or $O(\log n)$ more bits per key.

19. After sorting, equal items are neighbours. For the sum, scan with one index from each end and move the one that makes the sum closer to $x$.

20. When the merge takes an item from the right half while $r$ items remain in the left half, the item forms an inversion with each of those $r$ items.

21. After the first partition, one of the parts "less than" and "greater than" is empty and the other holds only equal keys, so the next call finishes in one pass.

22. Merge runs of width 1, 2, 4, … by relinking nodes, with a constant number of pointers. Heapsort needs to jump to the item at position $2i + 1$, which costs $\Theta(i)$ steps in a list.

23. The average is the external path length of the decision tree divided by its number of leaves $L \ge n!$. Show that a binary tree with $L$ leaves has external path length at least $L \lg L$, for example by induction using that $x \lg x$ is convex.

24. Use this lemma: if $x_i \le y_i$ for each $i$, and you sort the $x$'s and the $y$'s separately, then the $i$-th smallest $x$ is still at most the $i$-th smallest $y$, for each $i$.

25. Take the input $a_1 < b_1 < a_2 < b_2 < \cdots < a_n < b_n$. If some pair of neighbours in this chain, such as $a_i$ and $b_i$, is never compared, swap their values: the answers of all comparisons stay the same, but the merged output must change. There are $2n - 1$ such pairs.

26. $\lg 5! = \lg 120 \approx 6.9$, so six comparisons cannot tell 120 orders apart. For seven: compare $a : b$ and $c : d$, then the two larger ones, to get a chain $a < b < d$ with $c < d$. Insert $e$ into the chain of three with two comparisons. Then $c$ is below $d$, so it goes into a chain of at most three items: two more comparisons.

27. The items of ranks $i < j$ are compared exactly when one of them is the first pivot chosen among the ranks $i, \ldots, j$. This happens with probability $2/(j - i + 1)$. Sum over all pairs.

28. Take the middle item of the longer run, find its place in the other run by binary search, and rotate the block between them. This leaves two smaller independent merges. The recursion has depth $O(\log n)$, and the rotations on each level move $O(n)$ items in all.

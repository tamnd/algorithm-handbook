1. ◦ Run [insertion sort](/insertion-sort/) on $\langle 5, 2, 4, 6, 1, 3 \rangle$. Show the array after each pass of the outer loop. How many times does line L5 run in all?

2. ◦ Which of these sorts are stable as their entries give them: insertion sort, selection sort, merge sort, quicksort with the Lomuto partition, heapsort? For each one that is not, give an input of at most four items on which two equal keys change their order.

3. ◦ An array holds $n$ items that are all equal. How many comparisons does insertion sort make on it? Selection sort? Quicksort with the [Lomuto partition](/lomuto-partition/)?

4. ◦ What does it mean for a sort to be [in place](/in-place-algorithm/)? Is merge sort in place? Is quicksort? Say what part the recursion stack plays in your answer.

5. ◦ Draw the decision tree of insertion sort on three items $a_1, a_2, a_3$. How many leaves does it have, and what is its height? Compare the height with $\lceil \lg 3! \rceil$.

6. ◦ Merge $\langle 1, 4, 7, 8 \rangle$ with $\langle 2, 3, 5, 6 \rangle$. How many comparisons does the merge of [merging sorted lists](/merging-sorted-lists/) make? Give two sorted lists of four items each on which it makes only four.

7. ◦ Run the Lomuto partition, with the last item as the pivot, on $\langle 2, 8, 7, 1, 3, 5, 6, 4 \rangle$. Show the array after the partition and the index it returns.

8. ◦ Build a max-heap from $\langle 4, 1, 3, 2, 16, 9, 10, 14, 8, 7 \rangle$ as the first phase of [heapsort](/heapsort/) does. Show the array after the build.

9. • *Binary insertion sort* finds the place of each new item by [binary search](/binary-search/) and then shifts the larger items right. Show that it makes $O(n \log n)$ comparisons but still $\Theta(n^2)$ moves in the worst case. Which form of binary search keeps the sort stable?

10. • Prove that [bubble sort](/bubble-sort/) makes exactly as many exchanges as the input has [inversions](/inversion/). Prove the same for the number of times line L5 of insertion sort runs.

11. • Show that [selection sort](/selection-sort/) makes $\Theta(n^2)$ comparisons on every input but at most $n - 1$ exchanges. Why does this make it a fair choice when writing an item costs far more than comparing two? Which sort in this chapter writes even less?

12. • Show that merge sort makes at most $n \lg n - n + 1$ comparisons when $n$ is a power of 2. Give an input that needs exactly this many when $n = 8$.

13. • Write *bottom-up* merge sort, with no recursion: merge runs of width 1, then 2, then 4, and so on. When $n$ is a power of 2, does it do the same merges as top-down merge sort? When $n$ is not?

14. • Show that [quicksort](/quicksort/) with the Lomuto partition and the last item as the pivot takes $\Theta(n^2)$ time on an array that is already sorted, and also on an array sorted in reverse order.

15. • What does the [Hoare partition](/hoare-partition/) do when all keys are equal? Explain why quicksort with the Hoare partition takes $\Theta(n \log n)$ time on such input, when with the Lomuto partition it takes $\Theta(n^2)$.

16. • Show that plain quicksort can reach recursion depth $\Theta(n)$. Then show that if it recurses on the smaller side and loops on the larger one, the stack never holds more than $O(\log n)$ frames, whatever the pivots.

17. • An array is *$k$-sorted* if each item is at most $k$ places from its position in sorted order. Show that insertion sort sorts such an array in $O(nk)$ time. Then give an $O(n \log k)$ algorithm.

18. • Give a small input on which heapsort changes the order of equal keys. Then show how to make any comparison sort stable by changing what it compares. What does this cost in time and in space?

19. • Use sorting to decide, in $O(n \log n)$ time, (a) whether an array of $n$ numbers has two equal items, and (b) whether it has two items whose sum is a given number $x$.

20. • Change merge sort so that it also counts the inversions of its input, still in $O(n \log n)$ time.

21. • An array holds only two distinct key values, in any order. Explain why [three-way quicksort](/three-way-quicksort/) sorts it in linear time, whichever item it picks as the pivot.

22. • Sort a singly linked list with merge sort in $O(n \log n)$ time and $O(1)$ extra space besides the list, using the bottom-up form. Why is heapsort a poor fit for a linked list?

23. ★ Prove that every comparison sort makes at least $\lg n!$ comparisons *on average* over the $n!$ orders of $n$ distinct keys, and not only in the worst case.

24. ★ Prove that if an array is $h$-sorted and you then $k$-sort it, it is still $h$-sorted. (This fact is why each pass of [Shellsort](/shell-sort/) keeps the work of the passes before it.)

25. ★ Prove that merging two sorted lists of $n$ items each needs $2n - 1$ comparisons in the worst case, for any merging algorithm. Compare with the [merging lower bound](/merging-lower-bound/).

26. ★ Sort five items with seven comparisons in the worst case. Explain why no method can use only six.

27. ★ Show that randomized quicksort makes $2(n+1)H_n - 4n$ comparisons on average on $n$ distinct keys, where $H_n$ is the $n$-th harmonic number and each partition of $m$ items makes $m - 1$ comparisons.

28. ★ Give a stable merge of two adjacent sorted runs $A[lo..mid)$ and $A[mid..hi)$ that uses $O(1)$ extra space besides the recursion stack and $O(n \log n)$ time, using [binary search](/binary-search/) and rotations. Conclude that there is a stable in-place sort that runs in $O(n \log^2 n)$ time.

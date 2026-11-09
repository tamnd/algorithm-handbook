1. ◦ A [binary counter](/binary-counter-increment/) of 16 bits starts at 0 and is incremented 1000 times. How many bit flips are there in all? Compare with $2n$.

2. ◦ A sequence of $n$ operations is performed, and the $i$-th costs $i$ if $i$ is a power of 2 and 1 otherwise. Use the [aggregate method](/aggregate-method/) to show that the total is less than $3n$.

3. ◦ A dynamic array starts with capacity 1 and no items. Writing an item costs 1, and when the array is full the next append first copies all items into an array of twice the capacity, at a cost of 1 per item. What is the total cost of 17 appends? For which numbers $n$ of appends is the total largest compared with $n$, and what is it then?

4. ◦ A binary counter starts at a value whose binary form has $b$ ones. Use the potential $\Phi = $ number of 1 bits to show that $n$ increments flip at most $2n + b$ bits. Why does the bound $2n$ fail here?

5. ◦ For each bound, say whether it is a worst-case bound on each operation, an amortized bound, an expected bound, or an expected amortized bound: (a) $O(1)$ per append to a [dynamic array](/dynamic-array/); (b) $O(n \log n)$ for quicksort with random pivots; (c) $O(1)$ per insertion into a [hash table](/hash-table/) with chaining that doubles its size when full; (d) $O(\log n)$ per access in a [splay tree](/splay-tree/); (e) $O(\log n)$ per insertion into a binary heap.

6. ◦ A dynamic array of 8-byte items doubles when full. At $2^{20}$ items it is full and receives one more append. How many items does that append copy, and how much memory is allocated to the array, old and new together, during the copy?

7. ◦ For the [stack with multipop](/stack-with-multipop/) and $\Phi$ the size of the stack, compute the actual and the amortized cost of each operation in the sequence push, push, push, multipop(2), push, multipop(5), where multipop($k$) pops $\min(k, s)$ items from a stack of $s$ items. Check that the totals differ by $\Phi_{\text{end}} - \Phi_{\text{start}}$.

8. • A $k$-bit counter supports both INCREMENT and DECREMENT. Show a sequence of $n$ operations that flips $\Theta(nk)$ bits, so that no $O(1)$ amortized bound holds.

9. • A dynamic array grows by a constant number $k$ of cells when it is full, instead of doubling. Show that $n$ appends from an empty array cost $\Theta(n^2/k)$ in all.

10. • In a binary counter, flipping bit $i$ costs $2^i$. Show that $n$ increments from 0 cost $\Theta(n \log n)$ in all.

11. • A static structure supports search in a sorted array. To add insertions, keep sorted arrays of sizes $2^i$, at most one of each size, like the bits of a binary counter. An insertion makes an array of size 1 and merges equal sizes as long as there are two. Show that $n$ insertions cost $O(n \log n)$ in all, and that a search costs $O(\log^2 n)$.

12. • The [sliding window maximum](/sliding-window-maximum/) of an array of $n$ numbers, with window size $w$, can be computed with a deque of indices whose values decrease from front to back. Show that the whole computation takes $O(n)$ time, though one step may remove $w - 1$ indices from the deque.

13. • The [prefix function](/prefix-function/) of a pattern $P$ of length $m$ is computed by `k ← 0; for q ← 1 to m−1: (while k > 0 and P[k] ≠ P[q]: k ← π[k−1]); if P[k] = P[q] then k ← k + 1; π[q] ← k`. Use $k$ as a potential to show that the inner loop runs fewer than $m$ times in all.

14. • A binary counter gains an UNDO operation that restores the value before the last increment, at a cost of the number of bits it changes. Show a sequence of $n$ operations on a $k$-bit counter that costs $\Theta(nk)$. What does this say about amortized bounds for [persistent](/persistent-data-structure/) structures?

15. • In [linked-list disjoint sets](/linked-list-disjoint-sets/) with union by size, the union of two sets updates the representative pointer of each item of the smaller set. Show that any sequence of unions on $n$ items costs $O(n \log n)$ for the updates in all, and give a sequence of $n - 1$ unions, for $n$ a power of 2, that costs $\frac n2 \lg n$.

16. ★ A list of $n$ items serves accesses; accessing the item at position $k$, counted from 1, costs $k$. The [move-to-front heuristic](/move-to-front-heuristic/) then moves the item to the front at no cost. Compare it with any fixed order $L$ that starts equal to the list. Use the potential $\Phi = $ the number of pairs of items in different relative orders in the two lists to show that each access costs move-to-front at most $2i - 1$ amortized, where $i$ is the item's position in $L$, and so that move-to-front costs less than twice as much as $L$ on any sequence.

17. ★ A counter stores an integer as digits $d_i \in \{-1, 0, 1\}$ with value $\sum_i d_i 2^i$. INCREMENT adds 1 at position 0; a digit that would become 2 becomes 0 and carries 1 to the next position. DECREMENT is symmetric, with a digit that would become $-2$. Show that from 0 any sequence of $n$ increments and decrements changes $O(n)$ digits, and compare with Exercise 8.

18. ★ Turn array doubling into a structure with $O(1)$ worst-case time per append, assuming that allocating an array without initializing it takes $O(1)$ time. When the array of capacity $c$ is full, allocate one of capacity $2c$, and let each later append copy two old items. Show that the copying is complete before the new array is full, and explain how to read the item at index $i$ in the meantime. What is the most memory in use at one time?

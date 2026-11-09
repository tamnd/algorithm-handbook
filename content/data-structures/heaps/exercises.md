1. ◦ Which of these arrays, read as binary min-heaps in positions $1$ to $n$, have the [heap property](/heap-property/)? (a) $\langle 1, 4, 2, 7, 5, 3, 9, 8 \rangle$; (b) $\langle 1, 3, 6, 5, 2, 8, 9 \rangle$; (c) $\langle 2, 2, 5, 3, 2, 6 \rangle$. For each one that fails, name a parent and child in the wrong order.

2. ◦ A [binary heap](/binary-heap/) holds $n = 100$ keys in positions 1 to 100. Give the parent and the children of position 37, the height of the tree, and the positions of the leaves. How many nodes have height at least 3?

3. ◦ Insert 4 into the min-heap $\langle 3, 8, 5, 12, 10, 7, 9, 15, 14 \rangle$ (positions 1 to 9) with [sift-up](/sift-up/), and give the array and the number of swaps. Then call extract-min on the result and give the array again.

4. ◦ Build a min-heap from $\langle 9, 7, 8, 3, 6, 5, 1, 2, 4 \rangle$ with [Floyd's method](/floyd-heap-construction/). Give the array after the build and the number of swaps, and compare the count with the bound $n - s_2(n)$. Then build a heap from the same keys by inserting them one at a time in the given order. Is the result the same array?

5. ◦ In the min-heap $\langle 1, 10, 2, 11, 12, 3, 4 \rangle$, delete the key at position 5 as [heap delete](/heap-delete/) does. Which of the two moves, sift-up or sift-down, does the work here? Give the final array.

6. ◦ In a [d-ary heap](/d-ary-heap/) with $d = 3$ stored from index 0, give the parent of index 20 and the children of index 6. What is the height of a 4-ary heap with 1000 keys?

7. ◦ Solve the [top M](/top-m-problem/) problem with $M = 3$ for the stream $12, 7, 25, 3, 18, 30, 9, 22, 41, 15$. Give the contents of the heap after each item and the number of times the heap changes.

8. ◦ A [binomial heap](/binomial-heap/) holds 13 keys. Which binomial trees does it have? How many links does the next insert make, and the one after it? How many links does the insert into a heap of 15 keys make?

9. ◦ A [radix heap](/radix-heap/) starts with $last = 0$. Insert 9, 2, 12 and 3, and give the buckets. Then call extract-min three times. Give the value of $last$ and the buckets after each call, and the total number of item moves made by the refills.

10. • Insert three items with the same key 5, named $a$, $b$ and $c$ in that order, into an empty binary min-heap whose sift-up and sift-down swap only on a strict "less than". In what order do three extract-mins return them? Show how to make the heap return equal keys in the order they came in, and what it costs.

11. • A heap on the distinct keys $1, \ldots, n$ can be arranged in $n! / \prod_v s(v)$ ways, where $s(v)$ is the size of the subtree of $v$. Count the heaps for $n = 6$ and $n = 7$. What lower bound on the number of comparisons needed to build a heap does each count give? Compare it with the worst case of Floyd's method for these $n$, which its entry gives as 7 and 8.

12. • An [indexed priority queue](/indexed-priority-queue/) with room for items $0$ to $5$ starts empty. Run insert$(3, 50)$, insert$(0, 20)$, insert$(5, 40)$, insert$(1, 10)$, insert$(4, 30)$. Give the arrays $pq$ and $qp$. Then run decrease-key$(5, 5)$ and extract-min, and give both arrays after each.

13. • The array $\langle 2, 40, 30, 10, 12, 6, 8, 25, 35, 15 \rangle$, from index 0, is a [min-max heap](/min-max-heap/). Insert 50, then insert 1, then call delete-max. Give the array after each step.

14. • Write a tree as key(left, right), with "-" for an empty subtree. Meld the [leftist heaps](/leftist-heap/) 3(6(9, -), 8) and 4(5(11, -), 7). Give the result, the number of key comparisons, and the rank of the new root.

15. • The root 1 of a [pairing heap](/pairing-heap/) has the children 6, 4[9], 8, 3 and 7, from left to right, where 4[9] is a node 4 with one child 9. Call delete-min with two-pass pairing, putting a new child first in the list of children, as the entry does. Give the tree and the number of links.

16. • Insert $n$ keys one at a time into an empty binomial heap. Prove that the total number of links is exactly $n - s_2(n)$, and give it for $n = 1000$. Now let $n = 2^k - 1$ and alternate insert and extract-min, where each new key is the smallest. How many links does each pair of operations make? Explain why this does not contradict the $O(1)$ amortized bound for insert.

17. • Insert the keys $1, 2, \ldots, 9$ into an empty [Fibonacci heap](/fibonacci-heap/) and call extract-min. How many links does the consolidation make, and what trees are left? What is the largest degree a node can have in a Fibonacci heap of 100 nodes? Compare with $\lfloor \log_\phi 100 \rfloor$.

18. • Keep the median of a stream with two heaps: a max-heap for the lower half and a min-heap for the upper half. State the rule that keeps their sizes balanced, and give the lower median after each item of the stream $5, 15, 1, 3, 8, 7, 9, 10$. What does each new item cost?

19. • [Dijkstra's algorithm](/dijkstra/) runs on a graph with integer edge weights from 0 to $W$, using a [bucket queue](/bucket-queue/). Show that $W + 1$ buckets, used in a circle with bucket $k \bmod (W + 1)$ for key $k$, are enough, however large the distances grow. What is the running time with $n$ vertices and $m$ edges?

20. • Insert the keys $n, n - 1, \ldots, 1$, in that order, into an empty binary min-heap. Show that this makes exactly $\sum_{i=1}^{n} \lfloor \lg i \rfloor$ swaps, that no order of the keys makes more, and give the count for $n = 10$.

21. ★ Give an algorithm that lists the $k$ smallest keys of a binary min-heap of $n$ keys in $O(k \log k)$ time, without changing the heap. Prove that it is correct.

22. ★ Insert $3, 4, 5, 2, 6, 1, 7$ into an empty [skew heap](/skew-heap/) and give the tree. Then, for each $k \ge 1$, give $2k + 1$ inserts after which one more insert, of a key larger than all the others, makes $k + 1$ comparisons. Why does this not contradict the $O(\log n)$ amortized bound?

23. ★ Suppose a Fibonacci heap cuts a node from its parent on decrease-key but never makes cascading cuts. Show that a node of degree $k$ may then have a subtree of only $k + 1$ nodes, and give a sequence of operations that produces one. Which part of the analysis of extract-min fails?

24. ★ Insert $n$ distinct keys into a [soft heap](/soft-heap/) with error rate $\varepsilon = 1/3$, then call extract-min $\lceil n/3 \rceil$ times, and let $x$ be the largest original key among the items it returned. Prove that the rank of $x$ among all $n$ keys is at least $n/3$ and at most $2n/3 + 1$. Use this to select the $k$-th smallest of $n$ keys in $O(n)$ time.

25. ★ Find an input of 8 distinct keys on which Floyd's method, building a min-heap, makes 11 comparisons, counting one comparison for a node with one child and two for a node with two. Count them sift-down by sift-down, and check the total against $2n - 2s_2(n) - e_2(n)$, where $e_2(n)$ is the exponent of 2 in $n$.

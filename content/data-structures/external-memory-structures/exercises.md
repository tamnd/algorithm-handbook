1. ◦ An [external stack](/external-stack/) has $B = 3$, so its buffer holds up to 6 items. Push $1, \ldots, 10$, pop 5 times, push 11 and 12, then pop until the stack is empty. Give the disk and the buffer after the first five pops, the order of all the popped items, and the number of I/Os. Compare it with the bound $\lfloor n/B \rfloor$.

2. ◦ An [external queue](/external-queue/) has $B = 4$. Enqueue $1, \ldots, 10$, dequeue 3 times, enqueue 11, 12, 13, then dequeue until the queue is empty. Give the head, the disk part and the tail after the enqueue of 13, and the number of I/Os in all. Compare it with the bound $2\lfloor n/B \rfloor$.

3. ◦ Insert $50, 20, 80, 10, 30, 60, 90, 40, 70, 25$ into an empty [B-tree](/b-tree/) with $t = 2$, splitting full nodes on the way down. Give the final tree and the number of splits. One split is made although no node on the path would overflow. Which one, and why does the algorithm make it?

4. ◦ A B-tree has minimum degree $t = 100$. What is the smallest number of keys in a tree of height 3, and the largest number a tree of height 2 can hold? What is the largest possible height of a tree with $10^6$ keys?

5. ◦ Disk blocks have 4096 bytes, keys and pointers have 8 bytes, and each record has 120 bytes besides its key. A [B-tree](/b-tree/) stores the records in its nodes; a [B+ tree](/b-plus-tree/) stores them in its leaves only. How many keys and children fit in an internal node of each? How many levels of internal nodes does a B+ tree with $10^6$ leaves need if all its internal nodes are full?

6. ◦ Give the [van Emde Boas layout](/van-emde-boas-layout/) of the complete binary search tree on the keys $1, \ldots, 31$, as the list of keys in memory order, with a top tree of 2 levels and bottom trees of 3 levels. Which positions does a search for 21 visit? With blocks of $B = 4$ cells starting at position 0, how many blocks does it touch, and how many in the breadth-first layout?

7. ◦ A [packed memory array](/packed-memory-array/) has $H = 4$, $\tau_0 = 1$ and $\tau_H = 1/2$, with the upper thresholds evenly spaced. Give $\tau_0, \ldots, \tau_4$. Segments have 4 cells. An insert, counted in, makes the windows that contain its segment hold 5 keys in 4 cells, 8 in 8, 13 in 16 and 19 in 32. Which window is spread?

8. ◦ A leveled [LSM tree](/log-structured-merge-tree/) has a memtable of $C_0 = 10^6$ entries and size ratio $T = 10$. Give the capacity of the first four levels. How many levels on disk does it need to hold $5 \cdot 10^9$ distinct keys?

9. • Insert $1, 2, \ldots, 20$ in this order into an empty B-tree with $t = 2$. Give the final tree, its height, the number of nodes and the number of splits. What fraction of the key slots of the leaves is used? Then prove that $n$ inserts into an empty B-tree make at most $(n - 1)/(t - 1) - h$ splits, where $h$ is the final height.

10. • A [B+ tree](/b-plus-tree/) of order $d = 100$ holds $10^6$ keys, and its root is kept in memory. Show that its height is at most 2. A range query returns $Z = 5000$ keys. Give the bound on the number of nodes it reads.

11. • A [B*-tree](/b-star-tree/) has leaf capacity $C = 10$. Give $f$ and the largest root size $R$. A leaf with 10 keys gets one more key, and its neighbour has 8 keys: what are the sizes of the two leaves after SHARE? If instead both are full, what are the sizes after the split into three? Compare the smallest fill of a leaf with that of a B+ tree whose leaves hold up to 10 keys.

12. • A [B^ε-tree](/b-epsilon-tree/) has nodes of $B = 4096$ items, $\varepsilon = 1/2$, and holds $N = 2^{36}$ keys. Using the leading terms of the bounds, give its fan-out, its height, the I/Os per insert and per search, and compare them with a B-tree on the same blocks.

13. • Sort $N = 2^{40}$ items with $M = 2^{30}$ and $B = 2^{10}$ in two ways: insert them one by one into a B-tree and read the leaves in order, or use external merge sort. Estimate the I/Os of each with the leading terms, and the ratio between them.

14. • A leveled and a tiered LSM tree both have $C_0 = 10^6$, $T = 10$ and blocks of $B = 100$ entries, and hold $N = 10^{10}$ entries. Using the leading terms of the bounds, give for each the I/Os per insert and the number of runs a lookup may read without Bloom filters.

15. • In the van Emde Boas layout of Exercise 6, with $B = 4$ and blocks starting at position 0, count the blocks touched by the search for each of the 16 leaves. Give the largest count and the average, and the same for the breadth-first layout.

16. • $N$ records fill $N/B$ blocks. Show how to reverse their order with $2N/B$ I/Os and memory $B$, and how to shift them cyclically by $s$ places, where $B$ does not divide $s$, with $2N/B + 1$ I/Os and memory $2B$. Why does this not contradict the [permuting lower bound](/permuting-lower-bound/)?

17. • Change the external stack so that its buffer holds only $B$ items: a push into a full buffer writes it as a block, and a pop from an empty buffer reads the last block. Give a sequence of $n$ operations that makes $n/2$ I/Os.

18. • Build a B+ tree of order $d = 100$ from $10^6$ sorted keys from the bottom up: fill the leaves with $2d$ keys each, from left to right, then build each level of internal nodes, with up to $2d + 1$ children, from the level below. Give the number of nodes on each level and check the invariants. About how many leaves does the tree have if the keys are inserted one by one in increasing order instead?

19. ★ Design an external deque: push and pop at both ends, with $O(1/B)$ I/Os amortized per operation and memory $O(B)$. Prove the bound with a potential function.

20. ★ Show that a search in the van Emde Boas layout touches at most about $4\log_B N$ blocks. Stop the recursion at the first level where the pieces have at most $B$ nodes, and count the pieces on a search path and the blocks each can touch.

21. ★ A $p \times p$ matrix with $N = p^2$ entries is stored in row-major order, $B$ divides $p$, and $M \ge B^2$. Transpose it in $2N/B$ I/Os. Explain why this does not contradict the permuting lower bound.

22. ★ Prove that every comparison-based [external memory priority queue](/external-memory-priority-queue/) has a sequence of $N$ inserts and $N$ delete-mins that costs $\Omega\big(\frac{N}{B}\log_{M/B}\frac{N}{B}\big)$ I/Os, for $N$ large compared with $M$. What does this say about using a B-tree as a priority queue?

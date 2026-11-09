1. After the pushes the disk holds $[1\ 2\ 3]\ [4\ 5\ 6]$ and the buffer $[7\ 8\ 9\ 10]$, after 2 writes. The fifth pop finds the buffer empty and reads $[4\ 5\ 6]$, so the disk holds $[1\ 2\ 3]$ and the buffer $[4\ 5]$. The pops return $10, 9, 8, 7, 6, 12, 11, 5, 4, 3, 2, 1$, and there are 4 I/Os in all: 2 writes and 2 reads. The bound for the 24 operations is $\lfloor 24/3 \rfloor = 8$.

2. The head is $[4]$, the disk part $[5\ 6\ 7\ 8]\ [9\ 10\ 11\ 12]$ and the tail $[13]$. There are 3 writes and 3 reads, 6 I/Os, and the last dequeue takes 13 from the tail with no I/O. The bound for the 26 operations is $2\lfloor 26/4 \rfloor = 12$.

3. The tree is $[50]([20]([10]\ [25\ 30\ 40])\ [80]([60\ 70]\ [90]))$, after 4 splits: the root at 10, the leaf $[10\ 20\ 30]$ at 40, the leaf $[60\ 80\ 90]$ at 70, and the root $[20\ 50\ 80]$ at 25. The last one is not needed, since 25 goes into $[30\ 40]$, which has room. The algorithm splits every full node it passes, so that a split lower down always finds room in its parent and the insert never has to go back up.

6. The layout is $16, 8, 24, 4, 2, 1, 3, 6, 5, 7, 12, 10, 9, 11, 14, 13, 15, 20, 18, 17, 19, 22, 21, 23, 28, 26, 25, 27, 30, 29, 31$. The search visits 16, 24, 20, 22, 21 at positions 0, 2, 17, 21, 22, which lie in the blocks 0, 4 and 5, so 3 blocks. In breadth-first order the same keys are at positions 0, 2, 5, 12, 25, in 4 blocks.

7. $1, 7/8, 3/4, 5/8, 1/2$. The densities are $5/4 > 1$, $8/8 > 7/8$, $13/16 > 3/4$ and $19/32 \le 5/8$, so the window of height 3, with 32 cells, is spread.

9. The tree is $[8]([4]([2]([1]\ [3])\ [6]([5]\ [7]))\ [12]([10]([9]\ [11])\ [14\ 16\ 18]([13]\ [15]\ [17]\ [19\ 20])))$, of height 3, with 17 nodes, after 13 splits. Its 10 leaves hold 11 keys in 30 slots, so $11/30$ of them are used. For the bound, count nodes in two ways. Every node but the root holds at least $t - 1$ keys, so a tree of $m$ nodes has $n \ge 1 + (m - 1)(t - 1)$. Each split adds one node, except a root split, which adds two, and there are exactly $h$ root splits; so $m = 1 + s + h$.

11. $f = \lfloor 21/3 \rfloor = 7$ and $R = 13$. SHARE leaves 9 and 10 keys, and the split leaves 7, 7 and 7. Every leaf but the root is at least $7/10$ full, against $5/10$ in the B+ tree.

13. With the leading terms, the B-tree pays $\log_B N = 4$ I/Os per insert, $2^{42}$ in all, and merge sort pays $\frac{N}{B}\log_{M/B}\frac{N}{B} = 2^{30} \cdot \frac{30}{20} = 1.5 \cdot 2^{30}$. The ratio is $2^{12}/1.5 \approx 2731$.

15. For the leaves $1, 3, \ldots, 31$ the vEB counts are $2, 2, 3, 3, 3, 3, 3, 4, 2, 3, 3, 3, 2, 2, 3, 3$: at most 4, for the leaf 15, and $44/16 = 2.75$ on average. The breadth-first counts are 3 for the first four leaves and 4 for the others: at most 4, and $60/16 = 3.75$ on average.

19. Keep a front buffer $F$ and a back buffer $R$ in memory, each of at most $2B$ items, and between them a sequence of full blocks on disk, linked in both directions. A push into a full $F$ writes the $B$ items of $F$ farthest from the front as a new first block; a pop from an empty $F$ reads the first block, or, if the disk part is empty, splits $R$ into two halves with no I/O. The back is the mirror image. Use $\Phi = \big(\,\big||F| - B\big| + \big||R| - B\big|\,\big)/B$: an operation without I/O raises it by at most $1/B$, a transfer lowers it by about 1, and the split of $R$ does not raise it.

20. A piece where the recursion stops came from a tree with more than $B$ nodes, and it has about half its height, so every piece on the path but perhaps the first has height at least about $\frac{1}{2}\lg B$. A path of $\lg N$ levels then meets at most about $2\lg N / \lg B$ pieces. Each piece is a contiguous range of at most $B$ cells, so it lies in at most 2 blocks.

21. Cut the matrix into $B \times B$ tiles. A tile is $B$ pieces of rows, each one aligned block, so it can be read with $B$ I/Os into memory, which holds $B^2$ entries. Transpose it there, and write it as the tile in the mirror position with $B$ more I/Os. There are $N/B^2$ tiles. The lower bound holds for the worst permutation, and the counting argument shows that most permutations are hard, not that each one is.

22. Insert the $N$ items, then call delete-min $N$ times: the items come out in sorted order, so the queue sorts by comparisons with the same I/Os. The [external sorting lower bound](/external-sorting-lower-bound/) of Volume 1 says that this needs $\Omega\big(\frac{N}{B}\log_{M/B}\frac{N}{B}\big)$ I/Os. A B-tree used this way pays $\Theta(\log_B N)$ I/Os per operation, roughly $B$ times the bound.

1. The shortest solution takes $2^{10} - 1 = 1023$ moves. Disc $d$ moves $2^{10-d}$ times, so the smallest disc moves 512 times and the largest moves once.

2. Write $12 = 2^3 + 4$. For $k = 2$, $J(2^m + l, 2) = 2l + 1$, so the survivor is person 9. The removal order is 2, 4, 6, 8, 10, 12, 3, 7, 11, 5, 1.

3. Without a reference coin, $(3^4 - 3)/2 = 39$ coins. With one genuine coin, $(3^4 - 1)/2 = 40$.

5. The tiles in reading order are 1 2 3 4 5 6 8 7, with one inversion, the pair 8 and 7. The width 3 is odd, so a solvable position needs an even number of inversions, and this one is not solvable.

7. The twists of the corners sum to 0 modulo 3, a factor 3. The flips of the edges sum to 0 modulo 2, a factor 2. The permutation of the corners and the permutation of the edges have the same parity, a factor 2. So $3 \cdot 2 \cdot 2 = 12$.

8. A knight always moves to a square of the other colour, so a closed tour alternates colours and needs an even number of squares; 25 is odd. The argument rules out every $m \times n$ board with $m$ and $n$ both odd.

11. Tabulate $S(k, 4)$ for $k \le 7$ first: 1, 3, 5, 9, 13, 17, 25. Then compare $2S(k, 4) + 2^{8-k} - 1$ for $k = 1, \ldots, 7$. Two values of $k$ tie.

13. Run a breadth-first search from $(0, 0)$ over pairs $(x, y)$ with six successors each, and stop at the first pair with a 6. Since $\gcd(4, 9) = 1$, every reachable state lies on the boundary of the $4 \times 9$ rectangle.

16. A blank in a $2 \times 2$ grid has only two moves, and one of them undoes the last move, so the reachable positions form a single cycle. Half of the $4! = 24$ arrangements are reachable.

17. The solvable patterns are the column space of the press matrix, of size $2^{\text{rank}}$. Two press sets clear the same pattern exactly when their difference is in the null space, of size $2^{16 - \text{rank}}$.

20. Push both blocks as far left as they go, then as far right. A cell that lies under the same block in both placements is filled in every filling. Here the first block covers cells 1 to 3 at the left and 3 to 5 at the right.

22. A short certificate needs a solution of polynomial length. Every solvable position of the $(n^2 - 1)$-puzzle has a solution of $O(n^3)$ moves, while PSPACE-completeness rules out short certificates for a problem unless NP = PSPACE.

23. Show that the differences $S(n, 4) - S(n - 1, 4)$ are 1, then 2 twice, then 4 three times, and in general $2^j$ exactly $j + 1$ times. Then $S(t(t+1)/2, 4) = \sum_{j=0}^{t-1} (j + 1) 2^j$, and this sum is $(t - 1) 2^t + 1$ by induction on $t$.

25. The press matrix is symmetric, so a pattern can be turned off exactly when it is orthogonal over GF(2) to the null space, which two quiet patterns span. Take the dot product of each pattern with both of them.

27. Put $k$ coins on each pan. If the pans balance, the other $13 - 2k$ coins give $2(13 - 2k)$ cases for the 9 outcomes of two more weighings. If they do not, the $2k$ coins on the pans give $2k$ cases. No $k$ satisfies both bounds.

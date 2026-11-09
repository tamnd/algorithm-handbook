1. ◦ For six queens on a $6 \times 6$ board, find the size of three [search spaces](/search-space/): all sets of 6 cells, one queen in each row, and one queen in each row and each column. There are 4 solutions. What fraction of the third space do they form?

2. ◦ A program that tries all $2^n$ subsets of an $n$-set handles $n = 40$ in one hour. Another program takes $\Theta(n^3)$ steps and handles $n = 10\,000$ in one hour. By the rule of [combinatorial explosion](/combinatorial-explosion/), what is the largest $n$ each one handles in one hour on a machine 1000 times faster?

3. ◦ A machine does $10^9$ steps per second. In one day, what is the largest number of cities $n$ for which it can run a [brute-force search](/brute-force-search/) over all $(n-1)!/2$ tours at one step per tour? And for the [Held-Karp algorithm](/held-karp-algorithm/) at $n^2 2^n$ steps?

4. ◦ Run one step of the bitwise program of the [n-queens problem](/n-queens-problem/) for $n = 4$, with bit $i$ standing for column $i$. Before row 0, $cols = ld = rd = 0$, and the queen of row 0 goes to column 1. Give $cols$, $ld$ and $rd$ for row 1 as 4-bit words, and the word of free cells.

5. ◦ Write out the rule "the queen of row $r$ goes to column $2r \bmod n$" for $n = 7$, and check that the values $r + c$ and $r - c$ are distinct modulo 7. What goes wrong with the same rule for $n = 6$?

6. ◦ In the [exact cover](/exact-cover/) form of the pentomino problem on the $6 \times 10$ board, each option places one piece on five cells. How many options belong to the X pentomino, the plus sign, and how many to the I pentomino, the straight line of five cells?

7. ◦ Write a $4 \times 4$ Sudoku, with four $2 \times 2$ boxes and the digits 1 to 4, as an exact cover problem in the way of the $9 \times 9$ case. How many items and how many options are there? Give the general counts for an $n^2 \times n^2$ Sudoku.

8. ◦ An exact cover instance has items $A$ to $F$ and the eight options $AB$, $ACE$, $BD$, $CDF$, $EF$, $BC$, $DE$, $AF$, so every item lies in three options. With [dancing links](/dancing-links/), cover item $A$. Which options leave the lists, and what are the lengths of the lists of $B$ to $F$ afterwards?

9. ◦ The largest number $g(n)$ of maximal independent sets in a graph on $n$ vertices is given by the Moon-Moser formula in [maximal independent set enumeration](/maximal-independent-set-enumeration/). Find $g(7)$, $g(8)$ and $g(12)$, and for each give a graph that reaches it.

10. ◦ Over the variables $a, b, c$, let $f$ have the single term $abc$ and let $g$ have the terms $a$ and $b$. Run the checks L2 to L5 of the [Fredman-Khachiyan algorithm](/fredman-khachiyan-algorithm/) in order. Which check fails first, what witness does it return, and why is it a witness? What is the dual of $f$?

11. • Apply the explicit construction of the n-queens problem for $n = 9$ and for $n = 14$. Give both lists of columns, and check for $n = 9$ that the sums of row and column are distinct.

12. • A 6-mark [Golomb ruler](/golomb-ruler-problem/) of length 17 has marks $0 < a_2 < a_3 < a_4 < a_5 < 17$. How many candidates does a brute-force search over these rulers test? Find all the Golomb rulers among them, and say how many there are up to reflection.

13. • A branching algorithm for maximum independent set solves a graph with no vertex of degree 2 or more directly, and otherwise picks a vertex $v$ of degree at least 2 and tries two cases: $v$ is out, or $v$ is in and its neighbors are out. Write the recurrence for the number of leaves, find the base $\lambda$ of its solution $O^*(\lambda^n)$ as in [exact exponential-time algorithms](/exact-exponential-algorithms/), and compare it with the rule that waits for degree 3.

14. • Run [Algorithm X](/algorithm-x/) on the instance of exercise 8, choosing the item with the fewest options and breaking ties by the alphabet. Draw the search tree, count its nodes with one node per call as in the entry, and give every solution.

15. • Write Langford pairs for $n = 4$ as an exact cover problem. How many items and options are there? Find all the solutions.

16. • Tiling a $2 \times n$ board with dominoes is an exact cover problem with one item per cell. How many options are there? Show that the number of tilings $t(n)$ satisfies $t(n) = t(n-1) + t(n-2)$, and find $t(10)$.

17. • Use [reverse search](/reverse-search/) on the triangulations of a convex hexagon with vertices 1 to 6. The parent of a triangulation that is not the fan at vertex 1 flips one diagonal not at vertex 1 into a diagonal at vertex 1. Show that such a flip always exists, that the depth of a triangulation is the number of its diagonals not at vertex 1, and count the triangulations at each depth.

18. • There are 63 fixed pentominoes. Find how many of them each of the 8 symmetries of the square maps to itself, and use the [Burnside lemma](/burnside-lemma/) to count the free and the one-sided pentominoes, as in [polyomino enumeration](/polyomino-enumeration/).

19. • How many 5-step self-avoiding walks from the origin end at a neighbor of the origin? Answer by turning each such walk into a closed polygon, and check the method on 3-step walks, as in [self-avoiding walk enumeration](/self-avoiding-walk-enumeration/).

20. • Let $p(n)$ be the number of maximal independent sets of the path with $n$ vertices. Show that $p(n) = p(n-2) + p(n-3)$ for $n \ge 3$, with $p(0) = 1$, $p(1) = 1$, $p(2) = 2$, and find $p(8)$.

21. • For a graph $G$, consider its edges as a [hypergraph](/hypergraph/). Show that the minimal transversals of this hypergraph are the complements of the maximal independent sets of $G$. How many minimal transversals does the edge set of the cycle $C_7$ have, and how large are they?

22. • List the minimal transversals of $H = \{ab, bc, cd, de\}$, the edges of a path on five vertices, as in [minimal transversal enumeration](/minimal-transversal-enumeration/). Then check that the minimal transversals of your list give back $H$.

23. ★ Prove that the toroidal $n$-queens problem has no solution when $n$ is even. Use the sums $\sum_r c_r$ and $\sum_r (r + c_r)$ modulo $n$.

24. ★ Prove that Langford pairs for $n$ exist only if $n \equiv 0$ or $3 \pmod 4$. What does this say about the searches for $n = 5$ and $n = 6$?

25. ★ Call the *first* cell of a fixed polyomino the lowest cell of its leftmost column, and its *last* cell the highest cell of its rightmost column. Join a polyomino $P$ with $m$ cells and a polyomino $Q$ with $n$ cells by placing $Q$ so that its first cell lies just to the right of the last cell of $P$. Prove that this gives a one-to-one map into the polyominoes with $m + n$ cells, so that $a(m)\,a(n) \le a(m + n)$. Deduce a lower bound on the growth constant $\lambda$ from $a(10) = 36\,446$.

26. ★ Let $v$ be a vertex of least degree $d$ in a graph $G$. Show that the number of maximal independent sets of $G$ is at most $\sum_{u} \mu(G - N[u])$ over the $d + 1$ vertices $u$ of the closed neighborhood $N[v]$, where $\mu$ counts maximal independent sets. Deduce the Moon-Moser bound $\mu(G) \le 3^{n/3}$.

27. ★ Lawler's algorithm for the chromatic number uses $\chi(G[S]) = 1 + \min_I \chi(G[S \setminus I])$ for every nonempty $S \subseteq V$, with $I$ ranging over the maximal independent sets of $G[S]$. Bound the total number of pairs $(S, I)$ by the Moon-Moser bound, sum over $S$, and find the base $c$ of the running time $O^*(c^n)$.

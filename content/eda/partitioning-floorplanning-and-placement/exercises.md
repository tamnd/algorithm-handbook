1. ◦ A net has four pins with $x$ coordinates $0, 2, 3, 7$. Find its [half-perimeter wirelength](/half-perimeter-wirelength/) in $x$, the range $R$. Then compute $\sum_{i<j} |x_i - x_j|$ and check that it lies between $(p - 1)R$ and $\lfloor p^2/4 \rfloor R$. What does the linear [clique net model](/clique-net-model/) give with edge weight $1/(p - 1)$, and with edge weight $2/p$?

2. ◦ Two pins lie at $x = 0$ and $x = 2$. Compute the $x$ part of the [log-sum-exp wirelength](/log-sum-exp-wirelength/), $\gamma \ln \sum_i e^{x_i/\gamma} + \gamma \ln \sum_i e^{-x_i/\gamma}$, for $\gamma = 1$ and $\gamma = \tfrac12$. Compare the excess over the range with the bound $2\gamma \ln p$.

3. ◦ A logic family follows [Rent's rule](/rents-rule/) $T = t g^p$ with $t = 3$ and $p = 0.6$. How many terminals does a block of 1024 gates have? By what factor does $T$ grow when the block has 32 times as many gates, and what is the new $T$?

4. ◦ Find the least [ratio cut](/ratio-cut/) $\mathrm{cut}(A, B) / (|A|\,|B|)$ of the cycle $C_8$. The second eigenvalue of the [Laplacian](/laplacian-matrix/) of $C_n$ is $2 - 2\cos(2\pi/n)$. Compute the lower bound $\lambda_2/n$ for $C_8$ and compare.

5. ◦ The blocks are 1: $2 \times 3$, 2: $4 \times 1$, 3: $2 \times 2$ and 4: $1 \times 3$, written width by height, with no rotation. In the expression $1\,2\,3\,H\,V\,4\,V$, $V$ puts its two operands side by side and $H$ puts the second above the first. Find the width, height and area of the [slicing floorplan](/slicing-floorplan/) and its empty area. Is the word a [normalized Polish expression](/normalized-polish-expression/)? Of the words $1\,2\,V\,3\,V$ and $1\,2\,3\,V\,V$, which is normalized, and do they give the same floorplan?

6. ◦ The [shape functions](/shape-function/) of two subtrees have the corners $A = \{(2, 6), (3, 4), (6, 2)\}$ and $B = \{(1, 5), (4, 3), (5, 1)\}$, as (width, height). Find the corners of the shape function of an $H$ node with children $A$ and $B$, which stacks one above the other. Check that it has at most $|A| + |B| - 1$ corners, and find the least area.

7. ◦ Take the [sequence pair](/sequence-pair/) $\Gamma_+ = (3, 1, 4, 2)$, $\Gamma_- = (1, 3, 2, 4)$ and the blocks 1: $2 \times 1$, 2: $1 \times 2$, 3: $2 \times 2$, 4: $1 \times 1$. List the relation of every pair of blocks, pack the blocks to the left and down, and give the corners and the size of the packing.

8. ◦ For $n = 5$ labelled blocks, count the [B*-trees](/b-star-tree-floorplan/) ($n!$ times the [Catalan number](/catalan-numbers/) $C_n$), the normalized Polish expressions ($n!$ times the large Schröder number 90), the labelled [mosaic floorplans](/mosaic-floorplan/) ($n!$ times the Baxter number 92) and the sequence pairs. Order the four search spaces by size.

9. ◦ In [force-directed placement](/force-directed-placement/) a free cell has springs to fixed points at $0$ with weight 1, at $4$ with weight 2 and at $10$ with weight 1. Find the position of zero force. Give the net force on the cell when it sits at $x = 4$, and its direction.

10. ◦ In [simulated annealing placement](/simulated-annealing-placement/) a move raises the wire length by $\Delta = 4$. Find its probability of acceptance at $T = 10$ and at $T = 2$. With the geometric schedule $T \leftarrow 0.95\,T$, how many temperatures does it take for $T$ to fall by a factor of 1000?

11. • A row has sites $0, 1, \ldots, 9$. Three cells of widths 2, 2 and 1 have the global left edges $x' = 3, 3, 4$, in this order. Run PlaceRow of [Abacus legalization](/abacus-legalization/) with the squared displacement: give the clusters, the real positions and their cost. Round with $\lfloor x + \tfrac12 \rfloor$, check that the result is legal, and compare its cost with the best integer placement. Then run [Tetris legalization](/tetris-legalization/) in the same order and compare the squared and the total displacement.

12. • In one dimension, pads $P = 0$ and $Q = 12$ are fixed, and the free cells $a, b, c$ have the nets $Pa$, $ab$, $bc$, $cQ$ of weight 1 and the net $ac$ of weight 2. Write the system of [quadratic placement](/quadratic-placement/) and solve it. Give the quadratic cost and the weighted wire length of the solution. Then find the least weighted linear wire length and a placement that reaches it.

13. • A row has five sites at $x = 0, \ldots, 4$, and pads $P = -1$ and $Q = 5$ are fixed. The cells $a, b, c, d, e$ have the nets $\{P, a, b\}$, $\{b, c\}$, $\{c, d, e\}$, $\{e, Q\}$ and $\{a, c\}$, each of length equal to its span. For each of the six unit gaps between $-1$ and $5$, find the least number of nets that must cross it over all orders, and add these numbers into a lower bound. Find an order that meets the bound. This is the kind of window that [detailed placement](/detailed-placement/) solves exactly.

14. • A region of [min-cut placement](/min-cut-placement/) has four sites, two at $x = 0$ and two at $x = 1$, and is cut by the line $x = \tfrac12$ into two halves of two cells each. The cells are $a, b, c, d$. Outside the region are pins $P$ at $(-1, 0)$, $u$ at $(3, \tfrac12)$ and $v$ at $(\tfrac12, 3)$. The nets are $ab$, $bc$, $cd$, $ad$, $\{P, a\}$, $\{u, c\}$, $\{v, b, d\}$ and $\{P, u, b\}$. Apply [terminal propagation](/terminal-propagation/): build the reduced netlist with fixed terminals $T_0$ and $T_1$, and say which net is dropped and why. For each of the six balanced splits, give the plain cut of the cells, the cut with terminals and the number of crossing nets in total. Which splits does each objective choose?

15. • [Independent set matching](/independent-set-matching/) works on three unit cells in slots with left edges $x = 0, 3, 6$; a cell in a slot has its pin at the center, $x + \tfrac12$. Cell $a$ has a net to a pad at 8, cell $b$ a three-pin net with pads at 0 and 2, and cell $c$ a net to a pad at 3. The cells now sit in the order $a, b, c$. Build the $3 \times 3$ cost table, solve the [assignment problem](/assignment-problem/), and compare the result with the best single swap.

16. • In [Wong-Liu floorplanning](/wong-liu-floorplanning/) the move M3 swaps an adjacent operand and operator. List every such swap in $1\,2\,V\,3\,H\,4\,V$ and say which results are normalized Polish expressions. For the others, name the rule that fails.

17. • A cell $c$ lies between a fixed pin $P = 0$ and three fixed pins $Q_1, Q_2, Q_3$ at 12, with a two-pin net to each. A timing constraint asks for $x_c \le 3$. With quadratic wire length and weight $w$ on the net $\{P, c\}$, find $x_c$ as a function of $w$. Which $w$ meets the constraint with equality? Compare the half-perimeter wire length at $w = 1$ and at that $w$ with the optimum of the half-perimeter wire length under the constraint. This is the net weighting of [timing-driven placement](/timing-driven-placement/).

18. • For two pins at distance $d$ and $\gamma = 1$, show that the log-sum-exp $x$ part equals $d + 2\ln(1 + e^{-d})$. For which $d$ is the excess below $0.01$?

19. • In a row of $2n$ unit sites, $n$ unit cells all have the global left edge $x' = n$. Find the total displacement of Tetris and of the best legal placement. Show that their ratio tends to 2.

20. • The barbell graph is two copies of $K_4$ joined by one edge, with $n = 8$. Its second Laplacian eigenvalue is $3 - \sqrt7$. Use the bound $n\lambda_2/4$ to show that the bisection found by [spectral partitioning](/spectral-partitioning/) is optimal. Find the least ratio cut and compare it with $\lambda_2/n$.

21. • A B*-tree has the root $A$ ($2 \times 2$), $A$'s left child $B$ ($1 \times 3$), $B$'s right child $C$ ($3 \times 1$) and $A$'s right child $D$ ($2 \times 1$). The left child is placed just to the right of its parent and the right child above it at the same $x$, and every block drops onto the contour. Pack the blocks in preorder and give their corners, the size of the packing and its empty area.

22. ★ Show that every mosaic floorplan with at most four rooms has a segment from one side of the chip to the other, so that every such floorplan is slicing. Use the [constraint graphs](/floorplan-constraint-graphs/) or the segments directly.

23. ★ In quadratic placement, suppose that swapping two free cells $u$ and $v$ maps the weighted netlist to itself and fixes every pad. Show that $u$ and $v$ get the same position whenever every connected group of free cells has a net to a pad. Explain why this forces a spreading step after the solve.

24. ★ Unit squares sit at $A = (0, 0)$, $D = (0, 1)$ and $E = (1, 0)$. Find two different B*-trees whose packing is this placement. What does this say about a search over B*-trees?

25. ★ For the path $P_n$, show that the least ratio cut is $1/(\lfloor n/2 \rfloor \lceil n/2 \rceil)$. With $\lambda_2 = 2 - 2\cos(\pi/n)$, show that the ratio of the optimum to the bound $\lambda_2/n$ is about $4n/\pi^2$, so it grows without bound.

26. ★ Unit-width cells must go on distinct integer sites of one row, and the cost is $\sum_i f(x_i - x'_i)$ for a convex $f$. Show that some optimal legal placement keeps the order of the $x'_i$. This is why Tetris and Abacus place the cells in order of $x'$.

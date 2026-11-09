1. (a) 154. (b) $15 \cdot 12 = 180$. (c) Items 1, 2 and 3 fill weight 12 with value 114, and half of item 4 adds 15, so 129. (d) Items 1, 2 and 3 fit, items 4 and 5 do not, so 114. The first three are upper bounds; the greedy value is the value of a feasible packing, a lower bound, and the optimum is 116. The tightest upper bound is 129.

4. The row minima are 5, 4, 3 and 6, which sum to 18. After the rows are reduced, column 2 has minimum 3 and the other columns have a zero, so the bound is 21. The tour costs $8 + 4 + 3 + 6 = 21$, equal to the bound, so no tour is cheaper.

8. The root is $(34/11, 64/11)$ with value $62$, where both constraints are tight. The child $x_1 \le 3$ has its optimum at $(3, 35/6)$ with value $185/3 \approx 61.67$. The child $x_1 \ge 4$ has its optimum at $(4, 4)$ with value 52, an integer point, so 52 is the first incumbent and the optimum lies in $[52, 61]$.

9. Twelve nodes are visited and seven expanded: the root, then taking items 1, 2 and 3 (incumbents 36, 86, 114), then skipping items 4 and 5; back at items 1 and 2 taken, skip 3 (bound 118) and take 4 (incumbent 116, bound 118). The nodes "items 1 and 2, skip 3 and 4" (bound 96), "item 1, skip 2" (bound 98) and "skip 1" (bound 108) are dropped. The optimum is items 1, 2 and 4, weight 14 and value 116.

10. Both depth-first and best-first expand 7 nodes; breadth-first expands 8. The extra node is "skip item 1", with bound 108: breadth-first takes it out when the incumbent is only 86. The seven nodes have bounds 129, 129, 129, 129, 120, 118 and 118, all above 116 along their whole path, so every search with this bound must expand them.

13. The surviving pairs number 2, 4, 6, 7 and 7 at levels 1 to 5, so 27 nodes with the root, against 55 feasible nodes. Two kept pairs cannot have the same weight, since one would dominate the other, and the weights lie in $\{0, \ldots, W\}$.

15. Put a complete binary tree of depth $k$ under the first child of the root, with bound 4 at every node and value 0 at every leaf, and a path of length $k$ under the second child, with bound 6 and a leaf of value 5. Depth-first search has no incumbent above 0 while it is in the first subtree, so it expands all of it; best-first search follows the path, finds 5, and drops the first child.

16. At A the first row can reach at most 1, from $x_3$, which is less than 2. At B the second row has 2 from $x_5$ and needs one more, which only $x_4 = 1$ gives, and then $x_1$ and $x_3$ must be 0. With these values the first row is $2 - 1 = 1 < 2$.

19. For $t > z^*$ no solution has value at least $t$, so the run fails. For $t = z^*$ every node on the path to an optimal leaf has bound at least $z^*$, so the run reaches it. Each run expands only nodes whose path bounds are all at least $t \ge z^*$, so at most $K$ nodes, and the total is at most $(U - z^* + 1) K$. Set the next threshold to the largest bound among the nodes cut off in the last run; then each run expands a node that the previous one did not.

20. A row and column reduction subtracts $u_i$ from row $i$ and $v_j$ from column $j$ and leaves every entry nonnegative, so every assignment costs $\sum u_i + \sum v_j$ plus a nonnegative amount. For the example the reduction gives $9 + 3 = 12$ and the assignment problem 14. With three cities a permutation without fixed points is a cyclic shift, which is a tour.

21. $X^2 = [(1-r)^2, (1+r)^2]$ and $2X = [2 - 2r, 2 + 2r]$, so the extension is $[r^2 - 4r - 1, r^2 + 4r - 1]$, of width $8r$. The true range is $[-1, r^2 - 1]$. The lower bound is within $0.01$ when $4r - r^2 \le 0.01$, so $r \le 2 - \sqrt{3.99} \approx 0.0025$. Boxes near the minimizer cannot be dropped until they are this small, so they pile up there.

22. Compare the two runs node by node in the fixed depth-first order. A leaf that the run with the small incumbent sees, but the other run skips, lies under a node that the other run dropped, so its value is at most the other run's incumbent at that time. By induction the run with the larger start always has an incumbent at least as large, so every node it expands passes the test in the other run too. The seven nodes of Exercise 10 have bounds above 116, so no incumbent can drop them.

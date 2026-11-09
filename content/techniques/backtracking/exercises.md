1. ◦ Draw the [state space tree](/state-space-tree/) for arranging 1, 2, 3 in all orders, first as a fixed-tuple tree in which each of the three positions may take any of the three values, then as a permutation tree in which a value used once cannot be used again. Count the nodes of each.

2. ◦ The numbers are 2, 4, 5, 9 and the target is 11. Each level of the tree decides whether one number, in this order, is taken (left child) or left out (right child). Count the nodes of the tree pruned by the test "the numbers taken sum to at most 11", level by level, and list the solutions.

3. ◦ For 6 queens, written one column per row, say for each of the prefixes $(2, 4, 6, 1)$, $(1, 3, 5)$, $(3, 6, 2)$ and $(3, 1, 2)$ whether it is an alive [partial solution](/partial-solution/), and whether it extends to a solution. Give the solution when it does.

4. ◦ Run the [generic backtracking algorithm](/generic-backtracking-algorithm/) on 5 queens, trying the columns in increasing order. What is the first solution found, and how many prefixes, counting the empty one, are visited up to and including it? How many dead ends does the search meet on the way?

5. ◦ A 4 by 4 maze has the rows 1100, 0111, 1101 and 1001 from top to bottom, where 1 is an open cell and 0 a wall. The rat starts at the top left and must reach the bottom right, trying the moves down, right, up and left in that order, without entering a cell twice. Run the backtracking of [rat in a maze](/rat-in-a-maze/). How many calls are made, up to and including the call at the goal? Which cells are entered and then left because they lead nowhere? Write the path as a string of moves.

6. ◦ On a random path down a search tree, the root has 4 children, the chosen child has 2, the next has 1, the next has 1, and the node after that is a leaf. What is Knuth's estimate $X$ of the number of nodes? A second path meets 4 children at the root, then 3, then a leaf. What is the average of the two estimates?

7. ◦ A Golomb ruler is a set of integer marks, starting at 0, whose pairwise differences are all distinct. Check that 0, 1, 4, 6 is a Golomb ruler of length 6, and show that no Golomb ruler with 4 marks has length 5.

8. • In subset sum with negative numbers, the test "the numbers taken sum to at most the target" is not sound. Give a sound test that uses the sum $s$ of the numbers taken and the sums $P$ of the positive and $N$ of the negative numbers not yet decided, and prove that it is sound.

9. • Show that the permutation tree for $n$ items has $\sum_{k=0}^{n} n!/(n-k)!$ nodes, and that this number equals $\lfloor e \cdot n! \rfloor$ for $n \ge 1$. Check it for $n = 3$ and $n = 4$.

10. • The 10 solutions of 5 queens are to be counted with the symmetry of [search-tree pruning](/search-tree-pruning/): restrict the queen of the first row to the left half of the board and count each solution found twice, once for itself and once for its mirror image. Explain what must be done with the middle column when $n$ is odd, and check that the method gives 10 for $n = 5$.

11. • The wheel $W_5$ is a cycle $v_1 v_2 v_3 v_4 v_5$ with a hub $h$ joined to all five. Show that it has no proper coloring with 3 colors. With colors tried in the order 1, 2, 3, count the consistent assignments made by [chronological backtracking](/chronological-backtracking/) with the order $h, v_1, \ldots, v_5$, and with the order $v_1, \ldots, v_5, h$. Which rule of [variable-ordering heuristics](/variable-ordering-heuristics/) picks the better order?

12. • The rat-in-a-maze search marks a cell when it enters it. Suppose it never unmarks a cell on the way back. Show that it still finds a path whenever one exists, in time linear in the number of cells, and show on the open $2 \times 2$ grid that it no longer lists all simple paths.

13. • Solve TO + GO = OUT by hand with the column equations of [cryptarithmetic puzzle](/cryptarithmetic-puzzle/), where letters stand for distinct digits and no number starts with 0. Show that the solution is unique.

14. • Variables $X_1, \ldots, X_m$ have domains $\{1, 2\}$, except $D_m = \{1\}$, and the one constraint is $X_m \ne X_1$. Count the values tried, successful or not, by chronological backtracking with the order $X_1, \ldots, X_m$ and values in increasing order. Count them again for a search that, when $X_m$ fails, jumps straight back to $X_1$.

15. • Use backtracking to find the Golomb rulers with 5 marks and length 11. Break the mirror symmetry by asking that the first difference be smaller than the last. How many rulers are there, and how many before the symmetry is broken?

16. • Two tests $P$ and $P'$ for the same problem are both sound, and every prefix that passes $P'$ also passes $P$. Show that the tree pruned by $P'$ is a subtree of the tree pruned by $P$ and that both searches report the same solutions.

17. ★ Show that no Golomb ruler with 5 marks has length 10. Such a ruler would have each difference from 1 to 10 exactly once; count the odd differences in two ways.

18. ★ A binary constraint satisfaction problem has a constraint graph that is a tree, every domain is nonempty, and the problem is arc consistent: for every constraint between $X$ and $Y$, every value of $X$ has a value of $Y$ that it allows, and the other way round. Order the variables so that each variable after the first comes after its parent in a rooted version of the tree. Prove that chronological backtracking in this order finds a solution without ever backing up.

19. ★ In Knuth's estimate each child is chosen with probability $1/c$. Suppose instead that the child $v$ of a node $u$ is chosen with any probability $p(v) > 0$, the probabilities of the children of $u$ summing to 1. Show that $X = 1 + \sum_{k \ge 1} 1/(p(v_1) \cdots p(v_k))$, summed over the nodes $v_1, v_2, \ldots$ of the path, is still an unbiased estimate of the number of nodes. When does it have zero variance?

20. ★ Suppose the test of a backtracking search is exact at every depth: a prefix passes if and only if it extends to a solution. Show that a search listing all $S$ solutions of length $n$ visits at most $1 + nS$ prefixes, and that the first solution is reached after exactly $n + 1$ prefixes.

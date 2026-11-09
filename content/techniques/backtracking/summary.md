## What to remember

- **A partial solution** fixes the first $k$ decisions $x_1, \ldots, x_k$, or the values of some variables of a constraint satisfaction problem. Its test must be sound, never rejecting a prefix of a solution; closed under prefixes; and exact on complete candidates. An alive prefix may still be a dead end, as $(1, 3)$ is for 4 queens.
- **The state space tree** has the partial solutions as nodes. A fixed-tuple tree over $n$ yes-or-no decisions has $2^{n+1} - 1$ nodes; the permutation tree has $\sum_{k=0}^{n} n!/(n-k)!$. The running time of backtracking is the size of the pruned tree times the cost of a test, and the size is hard to predict.
- **The generic algorithm** extends the prefix by each candidate, tests it, recurses on the ones that pass and undoes the choice on return. It uses $O(n)$ space, the depth of the tree, and visits each node of the pruned tree once.
- **Knuth's estimate.** Follow one random path from the root, choosing each child with equal probability, and let $c_0, c_1, \ldots$ be the numbers of children met. Then $X = 1 + c_0 + c_0 c_1 + c_0 c_1 c_2 + \cdots$ satisfies $\mathbb{E}[X] = T$, the number of nodes. The average over many paths predicts the cost of a run.
- **Pruning** comes in five kinds: by feasibility, by a bound on the value, by symmetry, by dominance and by the alpha-beta rule. Each must be sound for the question asked. A rule that only feels plausible, such as skipping knapsack items whose value per unit of weight is below the average, is a heuristic and can lose the optimum.
- **Chronological backtracking** returns to the most recent variable after every failure. On a failure caused by an early variable it repeats the same failure for every combination of the variables in between, which is thrashing; backjumping returns to the variable that caused the failure.
- **Order matters.** Choosing the variable with the fewest remaining values first, with the degree rule to break ties, finds failures near the root, where they cut the most. Choosing the least constraining value first helps when one solution is wanted; when all solutions are wanted, or there are none, the value order does not change the number of nodes.

## Pruning and ordering at work

| Instance | What changes | Nodes before | Nodes after |
|---|---|---|---|
| 8 queens | rows with an attack test, against all prefixes | 19,173,961 | 2057 |
| 8 queens | first queen in columns 1 to 4, then reflect | 2057 | 1029 |
| Subset sum of 3, 5, 6, 7 with target 15 | sum test, then a remaining-sum test | 31 | 28, then 11 |
| SEND + MORE = MONEY | column search with carries, against all maps | 1,814,400 maps | 7236 choices |
| Four variables, $X_2 \ne X_3$ and $X_4 < X_1$ | conflict-directed backjumping | 14 assignments | 7 |
| 20 queens with forward checking | fewest remaining values first | 145,151 | 145 |
| Path of 10 vertices joined to $K_4$, 3 colors | DSATUR order, against the static order | 55,290 | 48 |

: Node counts from the entries of the chapter. The first two lines and the subset-sum line count nodes of the pruned tree; the backjumping line counts assignments, and the last two count search nodes.

## Choosing a method

- Write the test before the search, and check that it is sound. A test that only checks constraints whose variables are all assigned is always sound; a bound that depends on signs, as a partial sum does with negative numbers, may not be.
- Make the test as strong as its cost allows. A test that looks at the remaining items, as the remaining-sum test does for subset sum, often cuts more than the cheaper test on the chosen items alone.
- Before running a long search, estimate the tree with Knuth's random paths. If the estimate is far beyond what you can afford, change the order, the test or the method.
- Break symmetry at the root when the problem has it: fix the first decision to one half of its values and count the reflections.
- For constraint problems, use a dynamic variable order with fewest remaining values first and forward checking. If the run still thrashes, add backjumping or nogood learning.
- When the goal is an optimum rather than all solutions, add a bound on the best value a subtree can reach, and the method becomes [branch and bound](/depth-first-branch-and-bound/).

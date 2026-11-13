## What to remember

- In a finite two-player zero-sum game of perfect information without chance, every position has a value, and [minimax](/minimax/) computes it from the leaves up: $V(n) = \max_c V(c)$ where MAX moves and $\min_c V(c)$ where MIN moves. [Negamax](/negamax/) writes it as $N(n) = \max_c(-N(c))$ for the player to move.
- [Alpha-beta](/alpha-beta-pruning/) returns the minimax value and skips subtrees outside the window $(\alpha, \beta)$. On a uniform tree it reads all $b^d$ leaves in the worst case and exactly $b^{\lceil d/2 \rceil} + b^{\lfloor d/2 \rfloor} - 1$ with the best move first everywhere, the least any algorithm can read ([Knuth-Moore](/knuth-moore-theorem/)). On random trees with distinct leaf values the expected count grows like $R_b^d$ with $R_b = \Theta(b / \ln b)$.
- [Move ordering](/move-ordering/) and the [transposition table](/transposition-table/) bring alpha-beta near its best case; they change the size of the search, not its value. Null-window searches ([PVS](/principal-variation-search/), [MTD(f)](/mtdf/)) and [SSS*](/sss-star/) return the same value as alpha-beta in another order of work. Forward pruning ([null move](/null-move-pruning/), [futility](/futility-pruning/), [late move reductions](/late-move-reductions/)) and the [evaluation function](/evaluation-function/) are judged by measured play; forward pruning can change the result.
- [Proof-number search](/proof-number-search/) expands a most-proving node, with $\mathrm{pn} = \min$ and $\mathrm{dn} = \sum$ over the children of an OR node and the reverse at an AND node. [Retrograde analysis](/retrograde-analysis/) labels every position of an explicit game graph in $O(v + e)$ time, and the positions left unlabelled are draws.
- [Monte Carlo tree search](/monte-carlo-tree-search/) with [UCT](/uct/) picks the child that maximizes $\bar X_j + C\sqrt{\ln n / n_j}$. On a finite tree it finds the minimax move only in the limit of many playouts.
- With simultaneous moves or hidden information the value needs mixed strategies: $\max_x \min_y x^{\mathsf T} A y = \min_y \max_x x^{\mathsf T} A y$ ([minimax theorem](/minimax-theorem/)), found by one linear program. For two-player general-sum games, finding a [Nash equilibrium](/nash-equilibrium/) is PPAD-complete. [CFR](/counterfactual-regret-minimization/)'s average strategy has exploitability $O(1/\sqrt T)$ after $T$ iterations.
- Under normal play an impartial game is equivalent to a Nim heap of size $g(p) = \mathrm{mex}\{g(q)\}$ over its options, and a sum has value $g_1 \oplus \cdots \oplus g_k$ ([Sprague-Grundy](/sprague-grundy-theorem/)). The player to move loses exactly when the XOR is 0 ([Nim](/nim/)).
- Generalized geography and Hex on $n \times n$ boards are PSPACE-complete. Strategy stealing shows that the first player wins Hex, without a strategy.

| Method | Model | Cost | Guarantee |
|---|---|---|---|
| [Minimax](/minimax/) | perfect information, zero sum | $\Theta(b^d)$ leaves | exact |
| [Alpha-beta](/alpha-beta-pruning/) | same | $b^{\lceil d/2 \rceil} + b^{\lfloor d/2 \rfloor} - 1$ to $b^d$ leaves | exact |
| [PVS](/principal-variation-search/) | same | as alpha-beta with perfect ordering, re-searches otherwise | exact |
| [MTD(f)](/mtdf/) | same, with a transposition table | several null-window passes | exact |
| [SSS*](/sss-star/) | same | no leaf alpha-beta skips; large open list | exact |
| [Null move](/null-move-pruning/), [LMR](/late-move-reductions/), [futility](/futility-pruning/) | depth-limited search | measured | can change the result |
| [Proof-number search](/proof-number-search/) | AND-OR tree | memory for the whole tree | exact on trees |
| [Retrograde analysis](/retrograde-analysis/) | explicit graph, cycles allowed | $O(v + e)$ | exact, every position |
| [Expectiminimax](/expectiminimax/) | perfect information with chance | $\Theta((bn)^d)$ | exact expected value |
| [MCTS with UCT](/uct/) | perfect information | $n$ playouts | in the limit |
| [CFR](/counterfactual-regret-minimization/) | imperfect information, two-player zero sum, perfect recall | $T$ passes over the tree | average strategy, $O(1/\sqrt T)$ |
| [Sprague-Grundy](/sprague-grundy-theorem/) | impartial, normal play | $O(v + e)$ for the values | exact |

: The main methods. $b$ is the branching factor, $d$ the depth, $n$ the chance outcomes per node (expectiminimax) or the playouts (UCT), $v$ and $e$ the positions and moves.

## Choosing a method

If every position fits in memory, solve the game: retrograde analysis for a game graph, Grundy values for an impartial game. To prove the value of one position in a large game, use proof-number search, or df-pn when memory is short.

To play a large game with a good evaluation function, run alpha-beta with iterative deepening, a transposition table, killer and history moves, and principal variation search. Add quiescence search and forward pruning, and keep each change only if it wins more games. Without a good evaluation function, as in Go, use Monte Carlo tree search with UCT, and add RAVE or a learned policy.

With dice, use expectiminimax, and keep in mind that its choice depends on the scale of the leaf values, not only on their order. With simultaneous moves, solve the matrix game by linear programming. With hidden cards in a two-player zero-sum game too large for a linear program, use counterfactual regret minimization and play its average strategy.

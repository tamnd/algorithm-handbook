1. ◦ A MAX root has three MIN children, and the leaves below them, left to right, are $(5, 9, 2)$, $(7, 8, 6)$ and $(1, 10, 4)$. Find the [minimax](/minimax/) value. Run [alpha-beta](/alpha-beta-pruning/) left to right and say which leaves it reads. Then reorder the children and the leaves inside them so that alpha-beta reads as few leaves as possible, and check that the number is the one the [Knuth-Moore theorem](/knuth-moore-theorem/) gives for $b = 3$, $d = 2$.

2. ◦ A program can evaluate $10^6$ leaves per move in a game with [branching factor](/branching-factor/) $b = 10$. How deep can plain minimax search? How deep can alpha-beta search with the best move always first? How deep in its worst case?

3. ◦ In [Nim](/nim/) with heaps $(2, 9, 12)$, is the player to move winning? List every winning move.

4. ◦ Compute $\mathrm{mex}\{0, 1, 3\}$, $\mathrm{mex}\{1, 2\}$, $\mathrm{mex}\,\emptyset$ and $\mathrm{mex}\{0, 1, 2, 4, 5\}$ ([mex function](/mex-function/)). Then compute the [Grundy numbers](/grundy-number/) $g(0), \ldots, g(13)$ of the subtraction game in which a move removes 2 or 5 tokens from a heap, and list the heap sizes up to 13 at which the player to move loses.

5. ◦ Solve the zero-sum matrix game with payoffs to the row player

   $$A = \begin{pmatrix} 4 & -2 \\ -3 & 1 \end{pmatrix}.$$

   Check first that there is no saddle point, then find both optimal mixed strategies and the value ([minimax theorem](/minimax-theorem/)).

6. ◦ MAX chooses between two moves. Move A leads to a chance node that gives 6 with probability $1/3$ and 3 with probability $2/3$. Move B leads to a chance node that gives 0 or 9, each with probability $1/2$. Which move does [expectiminimax](/expectiminimax/) choose, and with what value?

7. ◦ A node of a [UCT](/uct/) search has been visited $N = 100$ times. Its three children have (wins, visits) $(3, 10)$, $(36, 50)$ and $(26, 40)$. Using the UCB1 score $\bar X_j + \sqrt{2 \ln N / n_j}$, which child does the next playout go through? Which child would the program play if the search stopped now?

8. ◦ In a [proof-number search](/proof-number-search/) tree the root is an OR node with three AND children $a$, $b$, $c$, which have 2, 3 and 4 unexpanded children. Compute the proof and disproof numbers of every node and find the most-proving node. Then the leftmost child of $a$ is expanded and found to be a win. Give the new numbers at $a$ and at the root.

9. ◦ A game graph has the moves $a \to b$, $a \to c$, $b \to d$, $c \to e$, $c \to g$, $d \to f$, $e \to a$, $e \to f$, $g \to h$, $h \to g$. A player with no move loses, and a play that never ends is a draw. Use [retrograde analysis](/retrograde-analysis/) to label every position as a win, loss or draw for the player to move.

10. • Give eight distinct leaf values for a binary tree of depth 3 with a MAX root such that alpha-beta, searching left to right, reads all eight leaves. Check your example by tracing the windows.

11. • The leaves of a MAX root with two MIN children, each with two leaves, are four distinct numbers in random order, all orders equally likely. Show that alpha-beta reads $11/3$ leaves on average.

12. • A position is the sum of three games: a heap of 9 in the subtraction game with moves $\{2, 5\}$, a heap of 7 in the subtraction game with moves $\{1, 2\}$, and a Nim heap of 3. Use the [Sprague-Grundy theorem](/sprague-grundy-theorem/) to decide who wins, and find every winning move.

13. • In misère Nim the player who takes the last token loses. With heaps $(1, 1, 4)$, find the winning move, and compare it with the winning move of normal Nim ([Bouton's theorem](/boutons-theorem/)).

14. • Chomp is played on an $m \times n$ bar whose bottom-left square is poisoned; a move eats a square and every square above and to the right of it, and whoever eats the poisoned square loses. Give an explicit winning strategy for the first player on an $n \times n$ bar with $n \ge 2$. For $2 \times n$ bars, find a winning first move. Why does the [strategy-stealing argument](/strategy-stealing-argument/) give no strategy for general $m \times n$?

15. • In directed vertex [geography](/generalized-geography/), the token starts on $s$, the players move it in turn along an edge to a vertex not yet visited, and a player who cannot move loses. The edges are $s \to a$, $s \to c$, $s \to e$, $a \to c$, $c \to b$, $b \to d$, $d \to a$, $e \to b$, $e \to d$. Who wins, and with which first move?

16. • Solve the $2 \times 3$ zero-sum game $A = \begin{pmatrix} 4 & 1 & 3 \\ 2 & 3 & 0 \end{pmatrix}$ by the graphical method: plot the column player's three payoff lines against the row player's mixed strategy, find the value, and find both optimal strategies.

17. • In a variant of rock-paper-scissors, a win with rock against scissors scores 2, the other wins score 1, and ties score 0. Write the payoff matrix and find the optimal mixed strategies and the value.

18. • In the stag hunt, each of two hunters chooses stag or hare. Two stag hunters get 4 each; a hare hunter gets 3 whatever the other does; a lone stag hunter gets 0. Find all [Nash equilibria](/nash-equilibrium/), pure and mixed, and their payoffs.

19. • A rock-paper-scissors player uses regret matching, the rule inside [counterfactual regret minimization](/counterfactual-regret-minimization/). Its cumulative regrets for rock, paper and scissors are $(4, -2, 1)$. Give its current strategy. The opponent then plays paper; update the regrets and give the next strategy.

20. • Redo exercise 6 after replacing every leaf value $x$ by $\sqrt{x}$, an increasing map. Which move is chosen now? Explain why the choice of minimax without chance nodes could not change under such a map.

21. • A [transposition table](/transposition-table/) search of a position $p$ to depth 6 with the window $(10, 20)$ returns 25 in one run, 4 in another and 13 in a third. Give the flag stored in each case. Later $p$ is probed again. Can the entry decide the result, without a search, for: the bound 25 at depth 6 with window $(22, 30)$; the bound 25 at depth 6 with window $(5, 24)$; the bound 4 at depth 6 with window $(0, 8)$; the exact value 13 when the probe wants depth 8?

22. ★ In undirected vertex geography, the token starts on $s$ and moves along edges to unvisited vertices; a player who cannot move loses. Prove that the first player wins exactly when every maximum matching of the graph covers $s$. Use it on the graph with edges $s a$, $a b$, $b c$, $c d$, $d s$, $b e$: who wins, and which first move wins? What changes if the vertex $e$ is removed?

23. ★ Prove that for every $b \ge 2$ and $d \ge 1$ there are leaf values on which alpha-beta, searching left to right, reads all $b^d$ leaves of the uniform tree.

24. ★ Prove that [principal variation search](/principal-variation-search/) on a uniform tree in which the first child of every node is its best reads exactly $b^{\lceil d/2 \rceil} + b^{\lfloor d/2 \rfloor} - 1$ leaves and never re-searches.

25. ★ In a two-player [zero-sum game](/zero-sum-game/) with mixed strategies, let $(x, y)$ and $(x', y')$ be two equilibria. Prove that $(x, y')$ is also an equilibrium and that all four pairs give the same payoff. Show by an example that this fails for general-sum games.

26. ★ Write a program that computes the expected number of leaves alpha-beta reads, left to right, on a binary tree of depth 3 with a MAX root whose eight leaves are distinct and in random order. Compare the answer with the $11/3$ of exercise 11 and with the best case of 5 and the worst case of 8.

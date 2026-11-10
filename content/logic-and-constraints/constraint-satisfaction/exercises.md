1. ◦ Write the direct SAT encoding of 3-colouring the Petersen graph, with one variable for each pair of a vertex and a colour, at-least-one and at-most-one clauses for each vertex, and one clause for each edge and colour. Count the variables and the clauses of each kind. Is the formula satisfiable?

2. ◦ Make the constraint $X < Y$ [arc consistent](/arc-consistency/) when $X \in \{2, 3, 4, 5\}$ and $Y \in \{1, 2, 3, 4\}$. Give the new domains and list all solutions.

3. ◦ Count the proper colourings with 3 colours of a path on 5 vertices and of a cycle on 5 vertices. Explain the difference with the [constraint graph](/constraint-graph/) in mind.

4. ◦ Let $R = \{01, 10\}$ be the relation $x \neq y$ on $\{0, 1\}$. Check whether $R$ is closed under the binary operations min and max, the ternary majority operation and the ternary operation $x \oplus y \oplus z$, and whether it is 0-valid or 1-valid. Which of Schaefer's classes contain $R$?

5. ◦ Show that the relation $\{100, 010, 001\}$, "exactly one of three", lies in none of the six classes of [Schaefer's theorem](/schaefer-dichotomy-theorem/). What does the theorem then say about CSPs over this relation?

6. ◦ The constraint graph has vertices $A, B, C, D$ and edges $AB$, $BC$, $CD$, $DA$ and $AC$. Compute the width of the orderings $(A, B, C, D)$ and $(D, C, B, A)$, and the width of the graph. What level of strong consistency does [Freuder's theorem](/freuder-theorem/) need for a backtrack-free search?

7. ◦ Take $x_1, x_2, x_3 \in \{1, 2\}$. Show that the three pairwise constraints $x_i \neq x_j$ are arc consistent, and that the single constraint all-different$(x_1, x_2, x_3)$ is not generalized arc consistent. What is left after [all-different filtering](/regin-all-different-filtering/)?

8. • Variables $X, Y, Z$ have the domain $\{1, \ldots, 5\}$, with the constraints $X = 2Y$, $Y < Z$ and $Z + X \le 7$. Run [AC-3](/ac-3/) to the fixpoint and give the domains. Then list all solutions. Does every value left in the domains belong to some solution?

9. • In 5-queens, with one queen per column, the queen in column 1 is in row 1 and the queen in column 2 is in row 3. Give the domains of columns 3 to 5 after [forward checking](/forward-checking/), and then after [maintaining arc consistency](/maintaining-arc-consistency/). How much search is left?

10. • A [simple temporal problem](/simple-temporal-problem/) has $10 \le x_1 - x_0 \le 20$, $30 \le x_2 - x_1 \le 40$ and $0 \le x_2 - x_0 \le 45$. Compute the minimal network and the earliest time of each event when $x_0 = 0$. Then add $x_2 - x_0 \le 39$ and find the negative cycle.

11. • Run [Régin's filtering](/regin-all-different-filtering/) on all-different with $x_1 \in \{1, 2\}$, $x_2 \in \{2, 3\}$, $x_3 \in \{1, 3\}$, $x_4 \in \{1, 2, 3, 4\}$ and $x_5 \in \{3, 4, 5\}$. Which values go, and which Hall set explains it? Count the solutions.

12. • The constraints $A < B$, $A < C$ and $A \neq D$ on the domain $\{1, 2, 3\}$ form a star with centre $A$. Apply the [tree-structured CSP](/tree-structured-csp/) algorithm with $A$ as the root: give the values that directional arc consistency removes and the first solution found by the backtrack-free pass, trying values in increasing order. How many solutions are there?

13. • Use [cutset conditioning](/cutset-conditioning/) with the cutset $\{v_1\}$ to count the proper 3-colourings of the cycle $v_1 v_2 v_3 v_4 v_5$. How many tree problems are solved, and what does each one count?

14. • Let $x, y \in \{1, 3\}$, $z \in \{2, 3, 4, 5, 6\}$ and $z = x + y$. Compare the domain of $z$ after [bounds consistency](/bounds-consistency/) with its domain after generalized arc consistency.

15. • In [graph-based backjumping](/graph-based-backjumping/) on the order $x_1, \ldots, x_6$, the earlier neighbours are $P(6) = \{x_2, x_4\}$, $P(5) = \{x_1\}$ and $P(4) = \{x_1, x_3\}$. A dead end occurs at $x_6$. Where does the search jump, and what is the induced ancestor set of that variable? If that variable then has no values left, where does the search go next? Why is it safe to skip $x_5$?

16. • Real variables have $x, y \in [0, 10]$ and $z \in [12, 15]$, with $z = x + y$ and $y \ge 2x$. Run [interval constraint propagation](/interval-constraint-propagation/) to the fixpoint. Is each bound of the result reached by some solution?

17. ★ The constraint language has two Boolean relations: $x \neq y$ and the clause $x \vee y \vee z$. Find the Schaefer classes of each relation, and show that each relation alone gives a polynomial problem but the language is NP-complete. Give a direct reduction from 3-SAT.

18. ★ The $2 \times 3$ grid has the vertices $a_1, a_2, a_3$ in the top row and $b_1, b_2, b_3$ in the bottom row, with edges between horizontal and vertical neighbours. Compute the induced width of the row order $(a_1, a_2, a_3, b_1, b_2, b_3)$ and the column order $(a_1, b_1, a_2, b_2, a_3, b_3)$. What do the two orders cost in [bucket elimination](/bucket-elimination/), and how do they compare with the [treewidth](/treewidth/) of the grid?

19. ★ The 8-queens problem has 92 solutions. The 8 symmetries of the board, 4 rotations and 4 reflections, map solutions to solutions. Show that the solutions fall into 12 classes, and find how many classes have 8 members and how many have 4. What does a [symmetry breaking](/symmetry-breaking/) constraint that keeps one solution per class gain?

20. ★ Colour the cycle on 5 vertices with 2 colours, as a binary CSP with $\neq$ on each edge. Show that [path consistency](/path-consistency/) detects that there is no solution, by following the derived relations on $(v_1, v_3)$ and $(v_1, v_4)$. What does path consistency do on an even cycle?

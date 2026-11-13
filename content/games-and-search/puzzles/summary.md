## What to remember

- A puzzle is a graph of positions with an edge for each legal move. When the reachable part fits in memory, [breadth-first search](/breadth-first-search/) from the goal gives every shortest distance at once, as for the 181,440 positions of the 8-puzzle. Larger puzzles need [IDA*](/iterative-deepening-a-star/) with an admissible heuristic such as a [pattern database](/pattern-database/).
- Some puzzles have exact answers. The [Tower of Hanoi](/tower-of-hanoi/) takes $2^n - 1$ moves, and the solution is unique. The [Frame-Stewart](/frame-stewart-algorithm/) count is optimal for four pegs (Bousch 2014) and only conjectured optimal for five or more. A jug of capacity $a$ or $b$ can hold exactly $c$ litres when $\gcd(a, b)$ divides $c$ and $c \le \max(a, b)$.
- Each weighing or question with $r$ outcomes multiplies the cases that can be told apart by at most $r$. This gives $\lceil \log_2 n \rceil$ yes or no questions and at most $(3^w - 3)/2$ coins in $w$ weighings, so 12 coins need 3. For the average number of questions, Huffman's code is optimal and lies within one question of the entropy.
- Test an invariant before you search. Half of the arrangements of the 15-puzzle cannot be solved, and the inversion count with the row of the blank says which half. Lights Out is a linear system over GF(2); on the $5 \times 5$ board the matrix has rank 23, so exactly one pattern in four can be cleared.
- Kociemba's two-phase algorithm returns a first cube solution of at most 30 moves and then improves it. God's number is 20 in the half-turn metric (2010) and 26 in the quarter-turn metric (2014), both proved by computer.
- A heuristic is not a proof. [Warnsdorff's rule](/warnsdorff-rule/) usually finds a knight's tour and fails on some boards and starting squares, depending on how it breaks ties. [Schwenk's theorem](/knights-tour-problem/) settles which boards have a closed tour.
- Every hardness result is about a generalized family, and the class matters. Sudoku on $n^2 \times n^2$ grids, Latin square completion, polyomino tiling, the pencil puzzles, Minesweeper consistency, offline Tetris and the decision form of the shortest $(n^2 - 1)$-puzzle solution are NP-complete. Sokoban, Rush Hour and sliding-block puzzles are PSPACE-complete. A puzzle of fixed size is a finite problem.

| Puzzle | Main method | Result | Generalized form |
|---|---|---|---|
| Tower of Hanoi, 3 pegs | recursion | $2^n - 1$ moves, unique | formula |
| Hanoi, 4 pegs | Frame-Stewart recurrence | optimal (Bousch 2014) | 5 or more pegs open |
| Josephus | recurrence | $J(n, 2)$ by a bit rotation | $O(n)$ time for every $k$ |
| Water jugs | gcd, BFS | $2(a + b)/g$ reachable states | pseudo-polynomial BFS |
| Counterfeit coin | ternary decision tree | $(3^w - 3)/2$ coins in $w$ weighings | formula |
| Sliding tiles | parity test, IDA* | 15-puzzle diameter 80 | shortest solution NP-complete |
| Lights Out | GF(2) elimination | $5 \times 5$ matrix has rank 23 | polynomial |
| Rubik's cube | two-phase search | God's number 20 (HTM) | $n \times n \times n$ optimal solving NP-complete |
| Knight's tour | Schwenk, divide and conquer | tours in linear time | polynomial |
| Domino tiling | matching, Kasteleyn | $8 \times 8$ has 12,988,816 tilings | polynomial on planar regions |
| Sudoku, pencil puzzles | propagation and backtracking | 17 clues needed for $9 \times 9$ | NP-complete |
| Sokoban, Rush Hour | BFS over states | Rush Hour $6 \times 6$ hardest start 93 moves | PSPACE-complete |

: The puzzles by method. The last column is the complexity of the family on boards of unbounded size.

## Choosing a method

Look for a recurrence first. Hanoi, Frame-Stewart and Josephus reduce to smaller instances of themselves. Check the first few values against a breadth-first search before trusting a closed form.

Before searching for a solution, decide whether one exists. A parity count, a position class or a rank over GF(2) answers in polynomial time.

When the state space fits in memory, search it breadth-first from the goal and store the distances; one table then answers every query. When it does not, use IDA* with the strongest admissible heuristic you can afford: Manhattan distance with linear conflicts for small tile puzzles, pattern databases for the 15- and 24-puzzles.

For pencil puzzles, write the board as a [constraint satisfaction problem](/constraint-satisfaction-problem/), an [exact cover](/exact-cover/) instance or a [SAT](/sat/) formula, propagate forced cells and [backtrack](/generic-backtracking-algorithm/) on the cell with the fewest candidates. Propagation alone solves most published puzzles, but not all. For motion puzzles, use breadth-first search or IDA* with duplicate detection and deadlock tests.

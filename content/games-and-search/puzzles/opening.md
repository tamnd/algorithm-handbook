A tower of eight discs sits on one of three pegs and must move to another peg, one disc at a time, never a larger disc on a smaller one. The shortest solution takes 255 moves, and a short induction proves that no solution is shorter. The 15-puzzle looks like the same kind of task, but no formula gives its answer. Half of all arrangements of the tiles cannot be solved at all, which a parity count shows in a few lines, and the shortest solution of a solvable position comes from a search in a space of about $10^{13}$ positions. Sudoku needs a third kind of answer. One grid falls to backtracking in milliseconds, but Sudoku on $n^2 \times n^2$ grids is [NP-complete](/np-complete/), so no method is known that is fast on every grid of every size.

Each puzzle in the chapter is a [state space](/state-space-search/): the positions are vertices of an [implicit graph](/implicit-graph/), the legal moves are its edges, and a solution is a path to a goal. The cost of a solution is its number of moves in a stated metric, and for the cube the metric matters: a half turn counts as one move in the half-turn metric and as two in the quarter-turn metric. Three kinds of result recur. Some puzzles have an exact count or formula, proved by induction or read off a recurrence. Some have an [invariant](/invariant/) that splits the positions into classes that no move can join, so solvability is a polynomial test and only the shortest solution needs search. The rest are hard: the chapter states each hardness result for the generalized family, on $n \times n$ boards or with $n$ pieces, because a puzzle of fixed size has a finite state space and is in principle solved by one table. The class is named each time. Puzzles whose solutions are short certificates, such as Sudoku, Minesweeper consistency and offline Tetris, are NP-complete. Motion puzzles such as Sokoban and Rush Hour are [PSPACE](/pspace/)-complete, so unless NP = PSPACE their solutions are not short certificates.

## What the chapter covers

1. **Puzzles with a formula.** The [Tower of Hanoi](/tower-of-hanoi/) and its four-peg form, the [Frame-Stewart algorithm](/frame-stewart-algorithm/), optimal for four pegs and only conjectured optimal for five or more. The [Josephus problem](/josephus-problem/) by a recurrence, the [water jugs](/water-jug-problem/) by a gcd test, and [missionaries and cannibals](/missionaries-and-cannibals/) by breadth-first search.
2. **Weighing and asking.** The [twenty questions problem](/twenty-questions-problem/), the [counterfeit coin problem](/counterfeit-coin-problem/) and [Mastermind](/mastermind-problem/): the information bound and the decision trees that meet it.
3. **Parity and permutation puzzles.** The [sliding tile puzzle](/sliding-tile-puzzle/) and its [solvability test](/sliding-puzzle-solvability/), the [burnt pancake problem](/burnt-pancake-problem/), [peg solitaire](/peg-solitaire/) and [Lights Out](/lights-out-puzzle/) over GF(2).
4. **Rubik's cube.** The [cube group](/rubiks-cube-problem/), [Kociemba's two-phase algorithm](/kociemba-algorithm/) and [God's number](/gods-number/), which is 20 in the half-turn metric.
5. **Tours, tilings and squares.** The [knight's tour](/knights-tour-problem/) and [Warnsdorff's rule](/warnsdorff-rule/), [domino tilings](/domino-tiling-problem/), [polyomino tilings](/polyomino-tiling-problem/), [jigsaw puzzles](/jigsaw-puzzle-problem/), [magic squares](/magic-square-problem/) and [Latin square completion](/latin-square-completion/).
6. **Pencil puzzles.** [Sudoku](/sudoku/), [Kakuro](/kakuro-problem/), [Nonograms](/nonogram-problem/), [Slitherlink](/slitherlink-problem/), [Nurikabe](/nurikabe-problem/), [Hashiwokakero](/hashiwokakero-problem/), [Numberlink](/numberlink-problem/), [Minesweeper consistency](/minesweeper-consistency/) and [crossword filling](/crossword-filling-problem/), all NP-complete in their generalized forms.
7. **Motion puzzles and Tetris.** Offline [Tetris](/tetris-problem/), NP-complete, and [Sokoban](/sokoban-problem/) and [Rush Hour](/rush-hour-problem/), PSPACE-complete.

## A first reading

Read these in order:

1. [Tower of Hanoi](/tower-of-hanoi/)
2. [Josephus problem](/josephus-problem/)
3. [Water jug problem](/water-jug-problem/)
4. [Twenty questions problem](/twenty-questions-problem/)
5. [Counterfeit coin problem](/counterfeit-coin-problem/)
6. [Sliding tile puzzle](/sliding-tile-puzzle/)
7. [Sliding puzzle solvability](/sliding-puzzle-solvability/)
8. [Lights Out](/lights-out-puzzle/)
9. [Rubik's cube](/rubiks-cube-problem/)
10. [Knight's tour](/knights-tour-problem/)
11. [Warnsdorff's rule](/warnsdorff-rule/)
12. [Domino tiling](/domino-tiling-problem/)
13. [Sudoku](/sudoku/)
14. [Sokoban](/sokoban-problem/)

Skip at first the Frame-Stewart proof, Kociemba's pruning tables, the coset search behind God's number and the hardness reductions of the pencil puzzles. They are easier once the models are familiar.

## Before you start

The formula puzzles need [recursion](/recursion/), [induction](/induction/) and [recurrence relations](/recurrence-relation/), and the water jugs need the [greatest common divisor](/greatest-common-divisor/) and [Bézout's identity](/bezouts-identity/). The search entries use [breadth-first search](/breadth-first-search/) and [depth-first search](/depth-first-search/) from the graphs volume, and [IDA*](/iterative-deepening-a-star/) and [pattern databases](/pattern-database/) from the heuristic search chapter of this volume. The weighing puzzles rest on the [information-theoretic bound](/information-theoretic-bound/), the [decision tree model](/decision-tree-model/) and [Huffman coding](/huffman-coding/). Parity arguments use [permutation parity](/permutation-parity/) and [inversions](/inversion/); Lights Out uses [Gaussian elimination](/gaussian-elimination/). Tilings and Latin squares use [bipartite matching](/bipartite-matching/) and [Hall's theorem](/hall-theorem/). The pencil puzzles are solved with the tools of the techniques volume, chiefly [backtracking](/generic-backtracking-algorithm/); of the combinatorics volume, [exhaustive search](/brute-force-search/), [exact cover](/exact-cover/) and [dancing links](/dancing-links/); and of the logic volume, [constraint satisfaction](/constraint-satisfaction-problem/) and [SAT](/sat/). The chapter does not repeat them.

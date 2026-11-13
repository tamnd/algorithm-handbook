The Handbook of Algorithms, edition 0.28.0: the written areas of [algorithm.tamnd.com](https://algorithm.tamnd.com)
as books, one volume per area, in PDF (7 × 10 in, with bookmarks and links), EPUB 3 and LaTeX source. Built from
[`tamnd/algorithm` v0.28.0](https://github.com/tamnd/algorithm/releases/tag/v0.28.0)
(`1fc5f181e694632deff85616227773b6055a61db`); the edition number follows the release of the site.

| | Volume | Entries | Pages |
|---|---|---:|---:|
| 0 | Guide and Index | the whole set | 1,497 |
| 1 | Foundations | 204 | 1,000 |
| 2 | Techniques | 208 | 1,123 |
| 3 | Data structures | 427 | 3,140 |
| 4 | Sorting | 156 | 910 |
| 5 | Searching | 115 | 646 |
| 6 | Sequences | 120 | 594 |
| 7 | Graphs | 685 | 3,693 |
| 8 | Strings | 216 | 1,256 |
| 9 | Automata and parsing | 270 | 1,604 |
| 10 | Number theory | 238 | 1,438 |
| 11 | Algebra | 328 | 2,122 |
| 12 | Numerical | 465 | 3,024 |
| 13 | Geometry | 280 | 1,794 |
| 14 | Combinatorics | 174 | 877 |
| 15 | Optimization | 301 | 1,764 |
| 16 | Logic and constraints | 325 | 2,106 |
| 17 | Randomized | 141 | 840 |
| 18 | Approximation | 213 | 1,309 |
| 19 | Online and streaming | 195 | 1,135 |
| 20 | Parallel | 128 | 897 |
| 21 | Distributed | 281 | 2,060 |
| 22 | Concurrency | 155 | 2,240 |
| 23 | Cryptography | 390 | 3,136 |
| 24 | Compression and coding | 220 | 1,741 |
| 25 | Machine learning | 419 | 2,982 |
| 26 | Systems | 442 | 3,209 |
| 27 | Biology | 254 | 1,611 |
| 28 | Graphics and signals | 401 | 2,745 |
| 29 | Games and search | 209 | 1,610 |
| | **All** | **7,960** | **54,103** |

- **New in this edition: Volume 29, Games and search**, in four chapters: *Game tree search* (62 entries: game
  trees, minimax and negamax, alpha-beta pruning and the Knuth-Moore analysis, move ordering, transposition tables,
  the killer and history heuristics, aspiration windows, principal variation search, Scout, MTD(f) and SSS*,
  quiescence search and the selective methods of game engines, proof-number search and df-pn, retrograde analysis
  and endgame tablebases, solved games, Monte Carlo tree search and UCT, games of chance and of imperfect
  information, the minimax theorem, Nash equilibria and counterfactual regret minimization, and combinatorial games:
  Nim, Bouton's theorem, the Sprague-Grundy theorem, strategy stealing and Hex), *Heuristic search* (38 entries: state
  spaces, best-first search, A* and its optimality, admissible and consistent heuristics, pattern databases,
  IDA*, RBFS and SMA*, weighted and anytime A*, beam search, LPA*, D* Lite and real-time search, jump point search
  and Theta* on grids, bidirectional search and multi-agent pathfinding by conflict-based search), *Planning* (74
  entries: STRIPS, PDDL and SAS+, the complexity of plan existence, forward and backward search, the delete
  relaxation and the heuristics of HSP and FF, landmarks, Graphplan and SATplan, partial-order planning, HTN
  planning, temporal planning, planning under uncertainty with MDPs, RTDP and POMDPs, replanning, and motion
  planning by configuration spaces, cell decomposition, potential fields, probabilistic roadmaps, RRT and RRT*) and
  *Puzzles* (35 entries: the Tower of Hanoi and the Frame-Stewart algorithm, the Josephus problem, sliding-tile
  puzzles and their solvability, the burnt pancake problem, Lights Out, the Rubik's cube, Kociemba's algorithm and God's
  number, knight's tours, tilings, magic and Latin squares, and the hardness of Sudoku, Minesweeper, Tetris,
  Sokoban, Rush Hour and other generalized puzzles). Each page says which results are proved, under which model,
  and which are only measured in play.
- **Volume 0, Guide and Index**, covers the whole set of 7,960 entries and has a new learning path,
  *Games and search*.
- **Volumes 1 to 28** have the same entries under the same numbers as in 0.27.0; their cross-references to entries
  of Volume 29 (A* search, the minimax theorem, zero-sum games, Nash equilibria, Monte Carlo tree search and
  others) now give entry numbers.
- Volumes 30 and 31 are forthcoming; Volume 0 lists their chapters.

**Files.** For each volume `NN-area`: `handbook-of-algorithms-0.28.0-NN-area.pdf`, `.epub`, and `-tex.tar.gz`
(`main.tex`, `body.tex`, `handbook.sty` and the figures; compile `main.tex` with XeLaTeX or tectonic).
`…-all-pdf.zip` and `…-all-epub.zip` hold every volume; `SHA256SUMS` lists the checksums.

Entry and statement numbers (such as 4.1.12 and Lemma 4.1.12.2) belong to this edition. The entries are the text of
the site; the learner pages were drafted by AI agents and checked as described in `content/PROVENANCE.md`. Text
CC BY-SA 4.0, code MIT. Report errors in an entry at https://github.com/tamnd/algorithm/issues and errors in the
books at https://github.com/tamnd/algorithm-handbook/issues.

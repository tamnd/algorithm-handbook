1. ◦ The [Tower of Hanoi](/tower-of-hanoi/) has 10 discs on peg 0 and must move them to peg 2. How many moves does the shortest solution take? How many of them move the smallest disc, and how many move the largest?

2. ◦ In the [Josephus problem](/josephus-problem/) with $n = 12$ people and $k = 2$, every second person still in the circle is removed, starting with person 2. Who is left at the end?

3. ◦ In the [counterfeit coin problem](/counterfeit-coin-problem/) one coin is heavier or lighter, and you must find it and say which. What is the largest number of coins that 4 weighings can handle without a reference coin, and with one extra coin known to be genuine?

4. ◦ In the [twenty questions problem](/twenty-questions-problem/), how many yes or no questions are needed in the worst case to find one of 1000 objects? One of $10^6$ objects?

5. ◦ The 8-puzzle shows 1 2 3 / 4 5 6 / 8 7 _, where _ is the blank. Is it solvable? Use the [solvability test](/sliding-puzzle-solvability/).

6. ◦ The English board of [peg solitaire](/peg-solitaire/) has 33 holes and starts full except for the centre. How many pegs are on the board at the start, and how many jumps does a game take that ends with one peg?

7. ◦ The [Rubik's cube](/rubiks-cube-problem/) group has $8! \cdot 3^8 \cdot 12! \cdot 2^{12} / 12$ elements. Which three conditions on legal positions account for the factor 12, and how much does each contribute?

8. ◦ Explain in one line why the $5 \times 5$ board has no closed [knight's tour](/knights-tour-problem/). Which other boards does the same argument rule out?

9. ◦ Give the magic constant of a [magic square](/magic-square-problem/) of orders 4, 5 and 6.

10. ◦ A $16 \times 16$ [Sudoku](/sudoku/) has $4 \times 4$ boxes. In the exact cover model with items for cells, rows, columns and boxes, how many items and how many options does it have?

11. • Compute the four-peg [Frame-Stewart](/frame-stewart-algorithm/) number $S(8, 4)$ from the recurrence $S(n, 4) = \min_{1 \le k < n} \big(2 S(k, 4) + 2^{n-k} - 1\big)$, and give every $k$ that attains the minimum.

12. • Find the order in which people are removed in the Josephus problem with $n = 10$ and $k = 3$, and the survivor.

13. • Two [water jugs](/water-jug-problem/) hold 4 and 9 litres. Steps fill a jug, empty a jug, or pour one into the other until the first is empty or the second is full. What is the fewest steps after which one jug holds exactly 6 litres? How many states can be reached from $(0, 0)$?

14. • In [missionaries and cannibals](/missionaries-and-cannibals/) with 4 missionaries, 4 cannibals and a boat for 3, cannibals may never outnumber missionaries on a bank or in the boat when missionaries are present. What is the fewest number of crossings?

15. • Five objects have probabilities 0.4, 0.2, 0.2, 0.1 and 0.1. What is the least average number of yes or no questions to find the object, and how far is it above the entropy?

16. • A $2 \times 2$ sliding puzzle has three tiles and a blank. How many positions are reachable from the goal 1 2 / 3 _, and what is the largest distance?

17. • On the $4 \times 4$ board of [Lights Out](/lights-out-puzzle/), the press matrix over GF(2) has rank 12. How many of the $2^{16}$ light patterns can be turned off, and how many press sets turn off each of them?

18. • In the [burnt pancake problem](/burnt-pancake-problem/) with two pancakes, which stack needs the most flips, and how many?

19. • Count the [domino tilings](/domino-tiling-problem/) of the $2 \times 12$ and $3 \times 10$ rectangles.

20. • A [Nonogram](/nonogram-problem/) row has 10 cells and the clue 3 4. Which cells are filled in every filling of the row, and which are empty in every filling?

21. • In [Kakuro](/kakuro-problem/), list the digit sets that a run of 3 cells with sum 7, a run of 3 cells with sum 23 and a run of 2 cells with sum 10 can hold.

22. • For each generalized puzzle, name its class: Sokoban, Rush Hour, offline Tetris, Minesweeper consistency, Latin square completion, and the decision form of the shortest solution of the $(n^2 - 1)$-puzzle. Which of them have solutions that are known to be short certificates?

23. ★ Prove that $S(t(t+1)/2, 4) = (t - 1) 2^t + 1$ for $t \ge 1$, and compute $S(21, 4)$.

24. ★ The state graph of the Tower of Hanoi with 4 discs has one vertex per legal position and one edge per move. How many vertices and edges does it have, and what is its diameter?

25. ★ On the $5 \times 5$ Lights Out board, can a pattern with only one corner lit be turned off? Can a pattern with only the centre lit?

26. ★ In the half-turn metric each move turns one of 6 faces in one of 3 ways. Bound the number of move sequences of length $d$ by $18 \cdot 15^{d-1}$, since a sequence never turns the same face twice in a row, and find the smallest $d$ for which the sequences of length at most $d$ could reach all 43,252,003,274,489,856,000 positions. How does the bound change if two turns of opposite faces are taken in only one order?

27. ★ Prove that 13 coins cannot be done in 3 weighings without a reference coin, by looking at the first weighing.

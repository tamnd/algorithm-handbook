1. ◦ [Support enumeration](/support-enumeration/) on a $3 \times 4$ bimatrix game tries every pair of nonempty supports $I$, $J$ with $|I| = |J|$. How many pairs is that? Check that the number equals $\binom{7}{3} - 1$.

2. ◦ A game has 3 players with 4 pure strategies each. How many variables, incentive inequalities and equations does the [linear program for correlated equilibria](/correlated-equilibrium-linear-program/) have? How many payoff numbers does the normal form of the game have?

3. ◦ Solve the [linear complementarity problem](/linear-complementarity-problem/) with $M = \begin{pmatrix} 2 & 1 \\ 1 & 2 \end{pmatrix}$ and $q = (-5, -6)$ by trying the four complementary patterns, and show that only one of them gives a solution.

4. ◦ In a game tree with perfect recall, a player has a first information set with actions a and b. After a the player reaches an information set with 3 actions, and after b one with 2 actions. How many sequences does the player have, and how many equations define its strategies in the [sequence form](/sequence-form/)? How many pure strategies does the player have in the normal form, and how many in the reduced normal form?

5. ◦ In one round of the [Blum-Mansour reduction](/blum-mansour-reduction/) with $k = 2$ actions, the copy for action 1 recommends $(3/4, 1/4)$ and the copy for action 2 recommends $(1/2, 1/2)$. Which distribution does the reduction play?

6. ◦ A segment $[0, 1]$ is cut into 7 pieces by 8 points, coloured in order $0, 0, 1, 0, 1, 1, 0, 1$. Count the pieces whose endpoints have different colours, and check the parity that [Sperner's lemma](/sperner-lemma/) predicts in dimension 1.

7. ◦ An instance of [END OF THE LINE](/end-of-the-line-problem/) on the 3-bit strings has the edges $000 \to 001 \to 011$ and $100 \to 110 \to 111$, and the pair $010 \to 101 \to 010$. The string $000$ is the given source. List all solutions.

8. ◦ Run the [DMP algorithm](/dmp-half-approximate-nash/) on the game with payoffs

$$A = \frac14 \begin{pmatrix} 1 & 4 & 0 \\ 3 & 0 & 2 \\ 2 & 1 & 4 \end{pmatrix}, \qquad B = \frac14 \begin{pmatrix} 2 & 3 & 0 \\ 1 & 0 & 4 \\ 4 & 2 & 1 \end{pmatrix}$$

from each of the three rows. For each start, give the output and the largest gain of each player from a deviation.

9. ◦ A player with 4 actions has cumulative external regrets $(3, 0, 1, -2)$. In the unconditional form of [regret matching](/regret-matching/), each action is played with probability proportional to the positive part of its regret. What does the player play next?

10. • Use [the linear program for zero-sum games](/zero-sum-game-linear-programming/) or a direct argument to find the value and the optimal strategies of the zero-sum game

$$M = \begin{pmatrix} 0 & -2 & 1 \\ 2 & 0 & -3 \\ -1 & 3 & 0 \end{pmatrix}.$$

11. • Find all Nash equilibria of the nondegenerate game below by support enumeration. Each cell gives the row payoff first.

| | L | C | R |
|---|---|---|---|
| T | 0, 2 | 4, 5 | 2, 1 |
| M | 2, 0 | 0, 4 | 5, 5 |
| B | 1, 5 | 5, 1 | 1, 2 |

12. • A game of chicken has payoffs $(0, 0)$ at (D, D), $(4, 1)$ at (D, C), $(1, 4)$ at (C, D) and $(3, 3)$ at (C, C). Write the correlated equilibrium LP in the four weights. Find the correlated equilibria of largest and smallest total payoff, and compare them with the total payoffs of the three Nash equilibria.

13. • In a bimatrix game with $A = B$, show that [best-response dynamics](/best-response-dynamics/), in which one player at a time switches to a strictly better pure strategy, stops after at most $mn - 1$ switches.

14. • In a [security game](/security-game/) with two targets and one resource, the defender covers target $t$ with probability $c_t$, where $c_1 + c_2 = 1$. At target 1 the defender gets 1 if covered and $-3$ if not, and the attacker gets $-1$ if covered and 2 if not. At target 2 the values are 0 and $-2$ for the defender and $-1$ and 1 for the attacker. Find the optimal coverage, the target attacked and the defender's payoff, with ties broken in the defender's favour. Does the answer change if $c_1 + c_2 \le 1$ is allowed?

15. • Deciding whether a bimatrix game has a Nash equilibrium in which player 1 gets at least $k$ is NP-complete ([hardness of optimal Nash equilibria](/hardness-of-optimal-nash-equilibria/)). Show that the same question takes polynomial time for zero-sum games, and that the question for correlated equilibria takes polynomial time in every bimatrix game.

16. • Run fictitious play on the zero-sum game $M = \begin{pmatrix} 2 & -1 \\ -1 & 1 \end{pmatrix}$ for 6 rounds, starting with row 1 and column 1 and breaking ties toward the lower index. Give the empirical frequencies after 6 rounds, the bounds on the value that they certify, and the value itself. [Robinson's theorem](/robinson-fictitious-play-theorem/) says that these bounds close in.

17. • In dimension 1, a Sperner colouring of $N + 1$ points has colour 0 at the left end and colour 1 at the right end. Give a method that finds a bichromatic piece with $\lceil \log_2 N \rceil$ colour queries, and say how many queries it needs for $N = 1000$.

18. • Show that a correlated equilibrium gives probability 0 to every strictly dominated strategy. Conclude that in a game where every player has a strictly dominant strategy the CE LP has exactly one feasible point.

19. ★ A bimatrix game $(A, B)$ satisfies $A_{ij} + B_{ij} = a_j + b_i$ for some vectors $a$ and $b$. Show that its Nash equilibria are those of a zero-sum game, and so are found by one linear program.

20. ★ Let $y$ be an optimal strategy of the column player in an $n \times n$ zero-sum game with payoffs in $[0, 1]$ and value $v$. Draw $k$ columns independently from $y$ and let $\hat y$ be their uniform mixture. Show that, when $k > \ln n / (2\varepsilon^2)$, with positive probability every row gets at most $v + \varepsilon$ against $\hat y$. How large must $k$ be for $n = 1000$ and $\varepsilon = 0.1$? This is the sampling idea behind the [Lipton-Markakis-Mehta algorithm](/lipton-markakis-mehta-algorithm/).

21. ★ Prove that the marginals of every coarse correlated equilibrium of a two-player zero-sum game are optimal strategies, and that its expected payoff is the value. Derive the [no-regret theorem for zero-sum games](/no-regret-zero-sum-theorem/) from this and the [coarse correlated theorem](/no-regret-coarse-correlated-theorem/).

22. ★ Prove that in every bimatrix game the leader's payoff in the strong Stackelberg equilibrium, as computed by the [Stackelberg commitment algorithm](/stackelberg-commitment-algorithm/), is at least the row player's payoff in every correlated equilibrium.

23. ★ Show that the unconditional regret matching of exercise 9 satisfies the condition of [Blackwell approachability](/blackwell-approachability/) for the nonpositive orthant: if $R$ is the vector of cumulative regrets and $p$ is proportional to $R^+$, then the expected regret vector of the next round is orthogonal to $R^+$, whatever the opponent does.

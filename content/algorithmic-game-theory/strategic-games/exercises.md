1. ◦ In the [bimatrix game](/bimatrix-game/) below, the row player chooses T, M or B and the column player L, C or R; each cell gives the row payoff first. Mark the best responses of each player and list all the [pure Nash equilibria](/pure-nash-equilibrium/).

| | L | C | R |
|---|---|---|---|
| T | 3, 2 | 0, 0 | 1, 1 |
| M | 1, 1 | 2, 3 | 0, 1 |
| B | 0, 2 | 1, 0 | 2, 1 |

2. ◦ A row player has three strategies with payoffs $(5, 0)$ for T, $(1, 1)$ for M and $(0, 2)$ for B against the columns L and R. Show that no pure strategy [dominates](/dominant-strategy/) M. For which $p$ does the mixed strategy $p\,\mathrm{T} + (1 - p)\,\mathrm{B}$ strictly dominate M?

3. ◦ A worker chooses Work or Shirk and an inspector chooses Inspect or Not. The payoffs (worker, inspector) are $(1, -1)$ for (Work, Inspect), $(1, 0)$ for (Work, Not), $(-1, 1)$ for (Shirk, Inspect) and $(2, -2)$ for (Shirk, Not). Show that the game has no pure equilibrium, and find the mixed equilibrium and the payoffs of both players in it.

4. ◦ In the battle of the sexes of [Nash equilibrium](/nash-equilibrium/), with payoffs $(2, 1)$ at (O, O), $(1, 2)$ at (F, F) and $(0, 0)$ otherwise, take the uniform distribution on the four cells. Is it a [correlated equilibrium](/correlated-equilibrium/)? Is it a [coarse correlated equilibrium](/coarse-correlated-equilibrium/)?

5. ◦ In an [extensive-form game](/extensive-form-game/), player 1 has three [information sets](/information-set/), with 3, 2 and 2 actions. How many pure strategies does player 1 have? How many numbers describe a mixed strategy, and how many a behaviour strategy?

6. ◦ In matching pennies with payoffs in $[0, 1]$, the row player gets 1 when the coins match and 0 otherwise, and the column player gets the opposite. The row player plays heads with probability $0.6$ and the column player with probability $0.5$. What is the smallest $\varepsilon$ for which this profile is an [$\varepsilon$-Nash equilibrium](/epsilon-nash-equilibrium/)?

7. ◦ Twenty players sit on a cycle and each chooses one of two actions. Each player's payoff depends on its own action and those of its two neighbours. How many payoff numbers does the [graphical game](/graphical-game/) need, and how many does the normal form need?

8. ◦ A [prisoner's dilemma](/prisoners-dilemma/) has $T = 6$, $R = 4$, $P = 1$ and $S = 0$, and it is repeated with discount factor $\delta$. For which $\delta$ is mutual grim trigger an equilibrium? For which $\delta$ is tit for tat a best reply to tit for tat?

9. ◦ In the hawk-dove game with prize $V = 4$ and cost $C = 6$, two hawks get $(V - C)/2$ each, a hawk against a dove gets $V$ and the dove 0, and two doves get $V/2$ each. Write the payoff matrix, find the mixed [evolutionarily stable strategy](/evolutionarily-stable-strategy/), and check that hawks and doves earn the same against it.

10. • In a [Bayesian game](/bayesian-game/) the column player has type 1 with probability $q$ and type 2 with probability $1 - q$, and knows its type. Type 1 gets 1 from L and 0 from R, type 2 gets 0 from L and 1 from R, whatever the row player does. The row player gets 3 at (U, L), 0 at (U, R), 1 at (D, L) and 2 at (D, R). Find the [Bayes-Nash equilibria](/bayes-nash-equilibrium/) for every $q$.

11. • A leader chooses U or D and a follower L or R, with payoffs (leader, follower) $(3, 1)$ at (U, L), $(5, 0)$ at (U, R), $(1, 0)$ at (D, L) and $(2, 2)$ at (D, R). Find the Nash equilibrium of the simultaneous game. Then find the leader's best mixed commitment in the strong [Stackelberg equilibrium](/stackelberg-equilibrium/) and its payoff.

12. • Player 1 chooses L or R. After L, player 2 chooses a, with payoffs $(2, 1)$, or b, with $(0, 0)$. After R, player 2 chooses c, with $(1, 2)$, or d, with $(3, 1)$. Find the [subgame perfect equilibrium](/subgame-perfect-equilibrium/) by backward induction. Then list all pure Nash equilibria of the game and say which one rests on a threat that player 2 would not carry out.

13. • For the hawk-dove game of exercise 9, write the [replicator equation](/replicator-dynamics/) for the share $x$ of hawks. Find its rest points and say which of them attract the starts $0 < x(0) < 1$.

14. • Find the value and the optimal strategies of the zero-sum game in which the row player gets

$$M = \begin{pmatrix} 4 & -2 & 3 \\ -1 & 2 & 5 \end{pmatrix}.$$

Remove a dominated column first, then use the [minimax theorem](/minimax-theorem/).

15. • Show that if every player of a finite game has a strictly dominant strategy, then the profile of these strategies is the only Nash equilibrium, also among mixed profiles.

16. • A profile is an $\varepsilon$-well-supported Nash equilibrium if every pure strategy in the support of each $\sigma_i$ earns at least the best payoff minus $\varepsilon$. Give a game and a profile that is a $0.1$-Nash equilibrium but not a $0.1$-well-supported one.

17. • Apply [iterated elimination of strictly dominated strategies](/iterated-elimination-of-dominated-strategies/) to the game below. Show that no strategy is dominated by a pure strategy at the start, and reduce the game to one profile.

| | L | C | R |
|---|---|---|---|
| T | 0, 1 | 2, 1 | 3, 2 |
| M | 2, 3 | 0, 4 | 2, 2 |
| B | 0, 1 | 0, 2 | 2, 3 |

18. • In the game with row payoffs $A = \begin{pmatrix} 1 & 1 \\ 0 & 0 \end{pmatrix}$ and column payoffs $B = \begin{pmatrix} 2 & 0 \\ 0 & 2 \end{pmatrix}$, find the logit [quantal response equilibrium](/quantal-response-equilibrium/) for $\lambda = \ln 3$, where each action is played with probability proportional to $e^{\lambda \cdot \text{expected payoff}}$. What is its limit as $\lambda \to \infty$?

19. • For each of these maps, say which hypothesis of the [Brouwer fixed-point theorem](/brouwer-fixed-point-theorem/) fails, and show that the map has no fixed point: $x \mapsto x^2$ on the open interval $(0, 1)$; a rotation of the circle by a quarter turn; the map on $[0, 1]$ that sends $x < 1/2$ to 1 and $x \ge 1/2$ to 0.

20. • A symmetric two-player game has payoff matrix $A$ for the row player and $A^{\mathsf T}$ for the column player. Show that a strategy $s$ with $A_{ss} > A_{ts}$ for every $t \ne s$ is an evolutionarily stable strategy. Then show that for $A = \begin{pmatrix} 1 & 1 \\ 1 & 0 \end{pmatrix}$ the first strategy is evolutionarily stable although this strict condition fails.

21. ★ In a two-player zero-sum game, let $X^*$ and $Y^*$ be the sets of optimal strategies of the two players. Prove that the Nash equilibria are exactly the pairs in $X^* \times Y^*$, that $X^*$ and $Y^*$ are convex polytopes, and that all equilibria give the same payoff.

22. ★ In rock-paper-scissors, let a win pay 1, a loss $-1$ and a tie $c$. For which values of $c$ is the uniform strategy an evolutionarily stable strategy?

23. ★ Let $(A, B)$ be a $2 \times 2$ game with no pure Nash equilibrium. Prove that it has exactly one correlated equilibrium, the product distribution of its unique mixed Nash equilibrium.

24. ★ In a graphical game on a path $1 - 2 - \cdots - n$, each player has $k$ actions and its payoff depends on its own action and those of its neighbours. Give a dynamic program that decides in $O(n k^3)$ time whether the game has a pure Nash equilibrium, and finds one if it does.

25. ★ In a finite game of perfect information, suppose that no player gets the same payoff at two different leaves. Prove that the game has exactly one subgame perfect equilibrium, even when behaviour strategies are allowed, and that it is pure.

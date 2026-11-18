1. ◦ In a bimatrix game the row player chooses T, M or B and the column player chooses L, C or R. The row player's payoffs are $A = \begin{pmatrix} 4 & 0 & 1 \\ 2 & 3 & 2 \\ 1 & 1 & 5 \end{pmatrix}$ and the column player's are $B = \begin{pmatrix} 3 & 1 & 0 \\ 0 & 2 & 1 \\ 2 & 0 & 1 \end{pmatrix}$, rows in the order T, M, B. Find every pure [Nash equilibrium](/nash-equilibrium/). For the cell (B, R), say which player wants to deviate.

2. ◦ The zero-sum game $M = \begin{pmatrix} 4 & -1 \\ -2 & 3 \end{pmatrix}$ pays the row player. What can each player guarantee with pure strategies alone? Find the value and an optimal mixed strategy for each player, and check the certificate of the [minimax theorem](/minimax-theorem/): $\min_j (x^{\mathsf T} M)_j = v = \max_i (M y)_i$.

3. ◦ In matching pennies the row player wins 1 when the coins match and loses 1 otherwise. Find the smallest $\varepsilon$ for which each profile is an $\varepsilon$-equilibrium: (a) the row player shows heads with probability $3/5$ and the column player with probability $1/2$; (b) the row player shows heads with probability $3/5$ and the column player with probability $2/5$.

4. ◦ Take the battle of the sexes, $A = \begin{pmatrix} 2 & 0 \\ 0 & 1 \end{pmatrix}$ and $B = \begin{pmatrix} 1 & 0 \\ 0 & 2 \end{pmatrix}$, and apply the map $T$ from the proof of the [Nash existence theorem](/nash-existence-theorem/) once to the profile in which both players mix fifty-fifty. Then apply it once to the profile in which the row player plays row 1 and the column player plays column 2. Is either profile a fixed point?

5. • Find all Nash equilibria, pure and mixed, of the game $A = \begin{pmatrix} 3 & 0 \\ 0 & 2 \end{pmatrix}$, $B = \begin{pmatrix} 1 & 0 \\ 0 & 4 \end{pmatrix}$, with the payoffs of each. Compare the mixed equilibrium with the two pure ones from the point of view of each player.

6. • A pure strategy is strictly dominated if another pure strategy pays strictly more against every strategy of the others. Show that a strictly dominated strategy has probability 0 in every Nash equilibrium. Then remove strictly dominated strategies one at a time from the game with rows T, M, B, columns L, C, R, $A = \begin{pmatrix} 1 & 1 & 5 \\ 1 & 0 & 4 \\ 2 & 4 & 3 \end{pmatrix}$ and $B = \begin{pmatrix} 2 & 5 & 3 \\ 2 & 4 & 0 \\ 0 & 4 & 3 \end{pmatrix}$, until none is left, and conclude that the game has exactly one Nash equilibrium.

7. • Each of two players names 1, 2 or 3. Equal numbers pay nothing. If one number is one more than the other, the higher number wins 1 from the other player; if it is two more, the lower number wins 2. Write the payoff matrix of the row player, and find the value of this zero-sum game and every optimal strategy of the row player.

8. • In a game of common interest both players get the same payoff, given by one matrix $C$. Show that a cell with the largest entry of $C$ is a pure Nash equilibrium, so every such game has one. Give a $2 \times 2$ example with a second pure equilibrium whose payoff is smaller than the largest entry.

9. ★ Call a $2 \times 2$ bimatrix game generic if $a_{11} \ne a_{21}$, $a_{12} \ne a_{22}$, $b_{11} \ne b_{12}$ and $b_{21} \ne b_{22}$. Prove that a generic $2 \times 2$ game has either exactly one or exactly three Nash equilibria. Say, in terms of the signs of $a_{1j} - a_{2j}$ and $b_{i1} - b_{i2}$, which case occurs.

10. ★ Prove that every finite two-player game with rational payoffs has a Nash equilibrium in which all probabilities are rational. You may use the existence theorem.

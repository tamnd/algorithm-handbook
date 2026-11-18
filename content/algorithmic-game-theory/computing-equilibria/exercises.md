1. ◦ Support enumeration tries every pair of nonempty supports of equal size. How many pairs does it try for a $4 \times 4$ game? For a $3 \times 5$ game? Check both numbers against $\binom{m+n}{m} - 1$.

2. ◦ In the battle of the sexes, $A = \begin{pmatrix} 2 & 0 \\ 0 & 1 \end{pmatrix}$ and $B = \begin{pmatrix} 1 & 0 \\ 0 & 2 \end{pmatrix}$, a referee draws (1, 1) or (2, 2) with probability $1/2$ each and tells each player only their own part. Check that this is a correlated equilibrium. What does each player get, and how does it compare with the mixed Nash equilibrium?

3. ◦ A $k$-uniform strategy is the uniform distribution on a multiset of $k$ pure strategies. How many $k$-uniform strategies does a player with 20 pure strategies have for $k = 3$, and how many pairs must a search over $k$-uniform profiles of a $20 \times 20$ game test?

4. ◦ In the game $A = \begin{pmatrix} 4 & 2 & 6 \\ 0 & 5 & 0 \\ 8 & 0 & 1 \end{pmatrix}$, $B = \begin{pmatrix} 8 & 4 & 9 \\ 8 & 0 & 4 \\ 2 & 5 & 3 \end{pmatrix}$, use the exact deviation test to check that $x = (0, 3/11, 8/11)$, $y = (5/13, 8/13, 0)$ is a Nash equilibrium. What are the two payoffs?

5. • Write support enumeration with exact fractions and run it on the game of Exercise 4. How many equilibria does it find, and what are their supports? Is the number consistent with the theory of nondegenerate games?

6. • Add 1 to every payoff of the battle of the sexes of Exercise 2 to get positive payoffs, and form the symmetric $4 \times 4$ game $S = \begin{pmatrix} 0 & A \\ B^{\mathsf T} & 0 \end{pmatrix}$. Find its symmetric equilibria $(z, z)$, and turn each $z = (x', y')$ into a profile $(x'/\lVert x' \rVert_1, y'/\lVert y' \rVert_1)$ of the original game. Why must both blocks of $z$ have positive weight when the payoffs are positive?

7. • In chicken, with payoffs $(0, 0)$ for (D, D), $(7, 2)$ for (D, C), $(2, 7)$ for (C, D) and $(6, 6)$ for (C, C), write the linear program for the correlated equilibrium with the largest total payoff and solve it. Compare with the correlated equilibrium of the [Nash equilibrium](/nash-equilibrium/) entry, which gives each player 5.

8. • Here is a simple method for a bimatrix game with payoffs in $[0, 1]$. Pick any row $i$. Let $j$ be a best reply of the column player to $i$, and $k$ a best reply of the row player to $j$. The row player mixes $i$ and $k$ with probability $1/2$ each, and the column player plays $j$. Run it with $i = 1$ (ties broken toward the lower index) on $A = \frac{1}{10}\begin{pmatrix} 9 & 2 & 5 \\ 3 & 8 & 1 \\ 6 & 4 & 7 \end{pmatrix}$, $B = \frac{1}{10}\begin{pmatrix} 1 & 6 & 3 \\ 7 & 2 & 9 \\ 4 & 5 & 0 \end{pmatrix}$, and find the smallest $\varepsilon$ for which the output is an $\varepsilon$-equilibrium.

9. ★ Prove that the method of Exercise 8 always returns a $1/2$-equilibrium. It is due to Daskalakis, Mehta and Papadimitriou.

10. ★ A bimatrix game is nondegenerate if no mixed strategy with a support of size $k$ has more than $k$ pure best replies. Prove that in every equilibrium of a nondegenerate game the two supports have the same size, so support enumeration over supports of equal size finds every equilibrium.

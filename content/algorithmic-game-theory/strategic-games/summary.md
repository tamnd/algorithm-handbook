## What to remember

- A **mixed strategy** is a probability distribution over a player's pure strategies, judged by its expected payoff. A profile $\sigma$ is a **Nash equilibrium** if $u_i(s_i, \sigma_{-i}) \le u_i(\sigma)$ for every player $i$ and every pure strategy $s_i$. Testing pure deviations is enough, and in an equilibrium every strategy in the support of $\sigma_i$ is a best response.
- An **$\varepsilon$-equilibrium** allows each player a gain of at most $\varepsilon$ from a deviation. A profile can be an $\varepsilon$-equilibrium for small $\varepsilon$ and still be far from every exact equilibrium.
- Equilibria need not be good for the players. In the prisoner's dilemma the only equilibrium is worse for both than mutual cooperation, and in chicken a correlated equilibrium gives the two players a total of 10, more than any Nash equilibrium or mixture of Nash equilibria.
- **Minimax theorem.** For every real $m \times n$ matrix $M$, $\max_x \min_y x^{\mathsf T} M y = \min_y \max_x x^{\mathsf T} M y$, the value $v$ of the zero-sum game. The proof writes the row player's problem as a linear program and takes its dual; one linear program gives the value and both optimal strategies.
- The theorem needs mixed strategies, finitely many pure strategies (or compactness and continuity), and the zero-sum form. Sion's theorem extends it to quasi-concave, quasi-convex and semicontinuous functions on convex sets, one of them compact.
- **Nash's theorem.** Every finite game has a Nash equilibrium in mixed strategies. The 1951 proof applies Brouwer's fixed point theorem to a continuous map that moves weight toward better pure strategies; its fixed points are exactly the equilibria. A symmetric game has a symmetric equilibrium.
- The proof is not an algorithm. Iterating Nash's map need not converge, and with three or more players some games with rational payoffs have only irrational equilibria. Two-player games with rational payoffs always have an equilibrium with rational probabilities.

## Reading the results together

The minimax theorem and Nash's theorem answer the same question for different games. For zero-sum games the answer is a single number, every pair of optimal strategies is an equilibrium, and linear programming finds one in polynomial time. For general games there may be many equilibria with different payoffs, and nothing in the existence proof says how to find one. Chapter 42.2 takes up that question in [Nash equilibrium computation](/nash-equilibrium-computation/).

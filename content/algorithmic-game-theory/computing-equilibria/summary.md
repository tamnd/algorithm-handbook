## What to remember

- **Zero sum is easy.** A two-player zero-sum game is solved by one linear program, which gives the value and optimal strategies for both players in polynomial time.
- **Correlated equilibria are easy.** The incentive constraints are linear in the probabilities of the profiles, so one linear program in the size of the payoff table finds a correlated equilibrium, also one that maximizes a linear objective.
- **2-NASH is PPAD-complete** (Chen, Deng and Teng 2009), and so is finding a $1/n^{\Theta(1)}$-approximate equilibrium. So there is no fully polynomial approximation scheme unless every PPAD problem is in P.
- **Three or more players.** Finding an $\varepsilon$-equilibrium is PPAD-complete (Daskalakis, Goldberg and Papadimitriou 2009); exact equilibria can be irrational, and finding one, or a point near one, is FIXP-complete (Etessami and Yannakakis 2010).
- **Not NP-hard, probably.** Every game has an equilibrium that is easy to check, so NP-hardness of 2-NASH under the usual reductions would give NP = coNP. Questions about equilibria with a property (a payoff of at least $k$, uniqueness, a strategy in the support) are NP-complete.
- **Support enumeration** tries $\binom{m+n}{m} - 1$ pairs of supports of equal size in an $m \times n$ game and solves a linear system for each. It lists all equilibria of a nondegenerate game, which always has an odd number of them.
- **Approximation.** Lipton, Markakis and Mehta showed that an $\varepsilon$-equilibrium with supports of size $O(\log n / \varepsilon^2)$ exists, which gives time $n^{O(\log n / \varepsilon^2)}$. Under an exponential time hypothesis for PPAD, Rubinstein (2016) showed that constant $\varepsilon$ needs quasi-polynomial time.

## Methods side by side

| Method | Game | Output | Worst-case time |
|---|---|---|---|
| One linear program | two-player zero-sum | value and optimal strategies | polynomial |
| One linear program | any finite game | a correlated equilibrium | polynomial in the table size |
| Support enumeration | bimatrix | all equilibria if nondegenerate | exponential |
| Lemke-Howson | bimatrix | one equilibrium | exponential (Savani and von Stengel 2006) |
| Small supports (Lipton, Markakis, Mehta) | bimatrix | an $\varepsilon$-equilibrium | $n^{O(\log n / \varepsilon^2)}$ |

: Methods of [Nash equilibrium computation](/nash-equilibrium-computation/) for games given as payoff tables.

## Choosing a method

For a zero-sum game, write the linear program. For a small bimatrix game, support enumeration is short to write and lists every equilibrium when the game is nondegenerate; test every profile it returns with the exact deviation test, and for degenerate games use vertex enumeration instead. For one equilibrium of a larger bimatrix game, Lemke-Howson is the standard method, though some games make every one of its paths exponentially long. If a correlated equilibrium is an acceptable answer, solve its linear program. Regret-minimizing dynamics are the method for very large zero-sum games, such as poker, where their average strategies converge to an equilibrium; in general-sum games they reach only coarse correlated equilibria.

Nash's theorem guarantees that every finite game has an equilibrium, but its proof is a fixed point argument and gives no recipe. This chapter asks how to compute one. The question matters wherever an equilibrium is used as a prediction or as a plan: a poker program needs the equilibrium strategy of a huge zero-sum game, a security agency needs the patrol schedule of a game against an attacker, and an economist who says that the players of a market model will reach an equilibrium is claiming that they can find one.

The answers split sharply. A two-player zero-sum game is one linear program, solved in polynomial time. A correlated equilibrium of any game is also found by one linear program in the size of the payoff table, even one that maximizes a linear objective. A Nash equilibrium of a general two-player game is a different matter: it always exists, it can be checked quickly, and yet finding one is PPAD-complete, so no polynomial algorithm is known and there is evidence that none exists. Asking for an equilibrium with a given property, such as a payoff of at least $k$ for one player, is NP-complete.

## What the chapter covers

The chapter has one group.

1. **Finding an equilibrium.** [Nash equilibrium computation](/nash-equilibrium-computation/) defines the problem for two and for more players, with exact and approximate outputs. It describes support enumeration, the Lemke-Howson algorithm and its exponentially long paths, the quasi-polynomial method of Lipton, Markakis and Mehta for approximate equilibria, and the linear program for correlated equilibria. It then gives the bounds: PPAD-completeness for two players, also for approximations within $1/n^{\Theta(1)}$; PPAD-completeness of $\varepsilon$-equilibria and FIXP-completeness of exact equilibria for three or more players; NP-completeness of many questions about equilibria with properties; and the reason why finding some equilibrium is unlikely to be NP-hard.

## A first reading

Read [Nash equilibrium computation](/nash-equilibrium-computation/) from the start through its examples: the battle of the sexes solved by support enumeration, the random $3 \times 3$ games whose numbers of equilibria are always odd, and the degenerate game where support enumeration misses most equilibria. Then read the list of known algorithms and the bounds. The reductions can wait until you have read about PPAD.

## Before you start

You need the [Nash equilibrium](/nash-equilibrium/) and the [Nash existence theorem](/nash-existence-theorem/) from Chapter 42.1, and the [minimax theorem](/minimax-theorem/) there for the zero-sum case. The [linear programming problem](/linear-programming-problem/) and the [simplex method](/simplex-method/) are in Volume 15. The complexity classes are in Volume 39: [TFNP](/tfnp/), the class of total search problems, and its subclass [PPAD](/ppad/), defined by the end-of-the-line problem, together with [NP-hard](/np-hard/) problems for comparison.

Most of the chapter is not written yet. The planned entries cover support enumeration, the indifference principle, best-response polytopes, the Lemke-Howson algorithm and the linear complementarity problem with Lemke's algorithm, Scarf's algorithm and Sperner's lemma, the PPAD-completeness proof through the end-of-the-line problem, the approximation algorithms of Lipton, Markakis and Mehta and of Daskalakis, Mehta and Papadimitriou with Rubinstein's lower bound, zero-sum and sequence-form linear programs, correlated equilibria by linear programming and the ellipsoid against hope, learning dynamics (best-response dynamics, fictitious play, regret matching, optimistic hedge, swap regret and Blackwell approachability), and Stackelberg commitment with security games.

A game, in the sense of this chapter, is a table. Each player picks a strategy, and the table gives every player a payoff for every combination of picks. The prisoner's dilemma, two firms setting prices, two drivers approaching a narrow bridge and a security team choosing where to patrol are all games of this kind. The question is what the players will do, or should do, when each of them cares only about their own payoff and knows that the others think the same way.

The answer that the rest of the volume builds on is the Nash equilibrium: a profile of strategies, possibly random, from which no player gains by changing their own strategy alone. Pure strategies are not enough. In matching pennies every pure profile leaves one player wanting to switch, and only the fifty-fifty mix is stable. With mixed strategies an equilibrium always exists. For two-player zero-sum games something stronger holds: each player has a strategy that guarantees the value of the game, whatever the other does, and the two guarantees meet.

## What the chapter covers

The chapter has one group, read in order.

1. **Equilibria and their existence.** The [Nash equilibrium](/nash-equilibrium/) gives the definition, three equivalent tests, and the standard examples: the prisoner's dilemma, matching pennies, the battle of the sexes and chicken, where a correlated equilibrium does better than every Nash equilibrium. The [minimax theorem](/minimax-theorem/) proves, by linear programming duality, that every finite zero-sum game has a value, and shows by examples which hypotheses it needs. The [Nash existence theorem](/nash-existence-theorem/) proves that every finite game has an equilibrium in mixed strategies, with Nash's 1951 proof from Brouwer's fixed point theorem and his 1950 proof from Kakutani's.

## A first reading

Read the three entries in order: [Nash equilibrium](/nash-equilibrium/), then the [minimax theorem](/minimax-theorem/), then the [Nash existence theorem](/nash-existence-theorem/). The first is short and concrete. In the second, the proof by duality is the part to learn; the alternative proofs and the history can wait. In the third, follow the Brouwer proof and the matching pennies example, and skip the Kakutani proof at first.

The computational side comes next. [Nash equilibrium computation](/nash-equilibrium-computation/), the first entry of Chapter 42.2, shows that the existence proof gives no fast algorithm: a zero-sum game takes one linear program, but finding an equilibrium of a general two-player game is PPAD-complete.

## Before you start

You need the [zero-sum game](/zero-sum-game/) of Volume 29 and [expected value](/expected-value/) from Volume 1, since a mixed strategy is judged by its expected payoff. The proof of the minimax theorem uses [linear programming duality](/lp-duality/) and [strong duality](/strong-duality/) from Volume 15. The existence theorem uses [convex sets](/convex-set/) from Volume 13 and the statement of Brouwer's fixed point theorem, which the entry states but does not prove.

Most of the chapter is not written yet. The planned entries cover normal-form and bimatrix games, best responses, dominant strategies and iterated elimination of dominated strategies, pure, approximate, correlated and coarse correlated equilibria, the refinements (subgame perfect, trembling-hand perfect, evolutionarily stable and quantal response equilibria), extensive-form and Bayesian games with information sets, perfect recall and Kuhn's theorem, Stackelberg equilibria, replicator dynamics, and the fixed point theorems of Brouwer and Kakutani.

## What to remember

- A **finite game in normal form** has players $1, \ldots, n$, strategy sets $S_i$ and payoffs $u_i : S_1 \times \cdots \times S_n \to \mathbb{R}$. A mixed strategy $\sigma_i$ is a distribution on $S_i$, and payoffs of mixed profiles are expectations over independent draws.
- A profile is a **Nash equilibrium** when no player gains by a change of their own strategy. It is enough to test pure deviations: $u_i(s_i, \sigma_{-i}) \le u_i(\sigma)$ for every $i$ and $s_i$. Equivalently, every pure strategy in the support of $\sigma_i$ is a best response, so the player is indifferent among them.
- **Nash's theorem.** Every finite game has a mixed equilibrium. The proofs use the [Brouwer](/brouwer-fixed-point-theorem/) or [Kakutani](/kakutani-fixed-point-theorem/) fixed-point theorem and give no efficient method. A pure equilibrium may not exist, as in matching pennies, and with three or more players all equilibria can be irrational.
- **Zero-sum games** are the exception. By the [minimax theorem](/minimax-theorem/), $\max_x \min_y x^{\mathsf T} M y = \min_y \max_x x^{\mathsf T} M y$, the equilibria are the pairs of optimal strategies, and they all give the same value, which a linear program computes.
- **Dominance.** A strictly dominated strategy is never used in a Nash equilibrium. Iterated removal of strictly dominated strategies, also by mixed strategies, gives the same result in every order. Weak dominance depends on the order and can remove equilibria.
- **The hierarchy.** Pure Nash $\subseteq$ mixed Nash $\subseteq$ [correlated](/correlated-equilibrium/) $\subseteq$ [coarse correlated](/coarse-correlated-equilibrium/) equilibria, where a mixed profile counts as the product distribution it defines. The last two sets are polytopes given by linear inequalities in the probabilities $p(s)$ of the profiles, and they can contain outcomes better for everyone than every Nash equilibrium.
- **Private information** turns a game into a [Bayesian game](/bayesian-game/), where a strategy maps types to actions; every finite Bayesian game has a Bayes-Nash equilibrium, by Nash's theorem on its agent form.
- **Order and information** need the extensive form. In a finite game of perfect information, backward induction finds a pure [subgame perfect equilibrium](/subgame-perfect-equilibrium/) in $O(|T|)$ time for a tree with $|T|$ nodes. With [perfect recall](/perfect-recall/), behaviour strategies give the same outcomes as mixed strategies ([Kuhn's theorem](/kuhn-theorem-behavioral-strategies/)), with one number per action instead of one per plan.

## The solution concepts side by side

| Concept | Exists in every finite game | Two-player normal form: finding one | Where it is used |
|---|---|---|---|
| [Dominant strategy equilibrium](/dominant-strategy/) | no | compare strategies directly | [prisoner's dilemma](/prisoners-dilemma/), truthful auctions |
| [Pure Nash equilibrium](/pure-nash-equilibrium/) | no | scan the $mn$ cells | congestion and potential games |
| [Nash equilibrium](/nash-equilibrium/) | yes | PPAD-complete; zero-sum by LP | the standard prediction |
| [$\varepsilon$-Nash equilibrium](/epsilon-nash-equilibrium/) | yes | quasi-polynomial for constant $\varepsilon$ | what algorithms output |
| [Correlated equilibrium](/correlated-equilibrium/) | yes | one LP | mediators, swap-regret learning |
| [Coarse correlated equilibrium](/coarse-correlated-equilibrium/) | yes | one LP | no-regret learning, price of anarchy |
| [Subgame perfect equilibrium](/subgame-perfect-equilibrium/) | yes, with perfect recall | backward induction with perfect information | sequential games, credible threats |
| [Stackelberg equilibrium](/stackelberg-equilibrium/), strong form | yes | one LP per follower strategy | commitment, security |
| [Evolutionarily stable strategy](/evolutionarily-stable-strategy/) | no | checking one is coNP-complete | populations |
| [Quantal response equilibrium](/quantal-response-equilibrium/) | yes | fixed point of a continuous map | experiments |

: The solution concepts of the chapter. "Exists" is for finite games; the subgame perfect equilibrium exists in behaviour strategies for finite extensive games with perfect recall. The computational results are those of Chapter 42.2 and of the entries: PPAD-completeness is evidence that no polynomial method exists, not a proof.

## Choosing a solution concept

- Start with dominance. If a player has a dominant strategy, that is the prediction for that player, and strict elimination can shrink a game before any other method.
- In a two-player zero-sum game, compute the value and the optimal strategies; every equilibrium is a pair of them.
- For a general game, the Nash equilibrium is the standard prediction, but expect several equilibria and no fast general method. Use the correlated or coarse correlated equilibrium when a mediator or a learning process is plausible, or when you need an answer that a linear program gives.
- When moves happen in sequence, use the extensive form and ask for subgame perfection, so that threats a player would not carry out are excluded.
- When one side commits first and the other observes, the Stackelberg equilibrium is the right model, and in its strong form the leader gets at least as much as in any Nash equilibrium of the simultaneous game.

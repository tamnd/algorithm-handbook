Two cars reach a narrow bridge from opposite ends. If both drive on, they crash; if both wait, they lose time; if one drives and the other waits, the driver gains and the one who waits loses a little. Game theory models this as a table of payoffs, one for each pair of choices, and asks for an equilibrium: choices from which neither driver gains by changing alone. This game, chicken, has three. Two are pure, one driver goes and the other waits, and the third is a mixture in which each driver flips a biased coin. A signal that tells each driver privately what to do, sometimes telling both to wait, can give them a larger total than any of the three; it is an equilibrium of another kind, a correlated one. This volume asks which equilibria exist, how to compute them, what they cost compared with a central plan, and how to design rules, such as auctions and elections, whose equilibria are good.

The volume has nine chapters. In this edition three of them are partly written: Chapter 42.1, on strategic games, with 3 entries; Chapter 42.2, on computing equilibria, with 1 entry; and Chapter 42.6, on social choice and voting, with 2 entries. The other six chapters are not written yet; each has an opening page that says what it will cover and what to read meanwhile.

## Why algorithmic game theory gets a volume of its own

Game theory and economics study what self-interested agents do. Computer science adds questions that change the answers.

- **Can the solution be computed?** Every finite game has a Nash equilibrium in mixed strategies, but finding one is PPAD-complete, even for two players, so no polynomial algorithm is known. A two-player zero-sum game, by contrast, is solved by one linear program, and so is the search for a correlated equilibrium.
- **Do the incentives survive the algorithm?** A mechanism that asks agents for private information must make honesty pay. When the best outcome is NP-hard to compute, an approximation may give agents a reason to lie, and the design must account for both.
- **How bad can selfish behaviour be?** The price of anarchy compares the equilibrium with the optimum in the worst case over a class of games, a bound in the style of an approximation ratio.
- **Some results are impossibility theorems.** Arrow's theorem and the Gibbard-Satterthwaite theorem are theorems: no rule for three or more candidates has all of a short list of reasonable properties, and the question becomes which property to give up.

## The chapters

**Chapter 42.1, Strategic games**, is written in part. The [Nash equilibrium](/nash-equilibrium/) gives the definition, mixed strategies and the standard small games; the [minimax theorem](/minimax-theorem/) proves that every finite zero-sum game has a value, by [LP duality](/lp-duality/); and the [Nash existence theorem](/nash-existence-theorem/) proves that every finite game has an equilibrium, from Brouwer's fixed point theorem.

**Chapter 42.2, Computing equilibria**, is written in part. [Nash equilibrium computation](/nash-equilibrium-computation/) covers support enumeration, the Lemke-Howson algorithm, the PPAD-completeness of two-player games, approximate equilibria, and the linear programs for zero-sum games and correlated equilibria.

**Chapter 42.3, Price of anarchy and selfish routing**, is not written yet. It will cover selfish routing and Wardrop equilibria, Pigou's example and Braess's paradox, bounds on the price of anarchy and stability, congestion and potential games, and network design games. Meanwhile, read [PLS](/pls/) in Volume 39 and the [min-cost flow problem](/min-cost-flow-problem/) in Volume 7.

**Chapter 42.4, Mechanism design**, is not written yet. It will cover the revelation principle, incentive compatibility, the Vickrey-Clarke-Groves mechanism, Myerson's lemma, the Myerson-Satterthwaite theorem and truthful approximation algorithms. Meanwhile, read [makespan scheduling on unrelated machines](/unrelated-machine-scheduling-makespan/) in Volume 18, the problem of the Nisan-Ronen conjecture on truthful scheduling.

**Chapter 42.5, Auctions**, is not written yet. It will cover the standard single-item auctions and revenue equivalence, Myerson's optimal auction, combinatorial auctions and winner determination, and the position auctions of online advertising. Meanwhile, read the [prophet inequality](/prophet-inequality/) in Volume 19 and the [set packing problem](/set-packing/) in Volume 18.

**Chapter 42.6, Social choice and voting**, is written in part. The [Borda count](/borda-count/) scores candidates by position and is open to manipulation by strategic lists; [Kemeny rank aggregation](/kemeny-rank-aggregation/) finds the ranking closest to the voters' in [Kendall tau distance](/kendall-tau-distance/), which is NP-hard, with exact methods for small instances and approximations.

**Chapter 42.7, Fair division**, is not written yet. It will cover cake cutting, envy-free protocols, the fair allocation of indivisible goods with relaxations of envy-freeness and the maximin share, maximum Nash welfare, and rent division. Meanwhile, read [max-min fairness](/max-min-fairness/) and [dominant resource fairness](/dominant-resource-fairness/) in Volume 26.

**Chapter 42.8, Matching markets and market equilibria**, is not written yet. It will cover two-sided matching beyond the basic algorithm, house allocation and top trading cycles, school choice and kidney exchange, and market equilibria in Fisher and Arrow-Debreu markets. Meanwhile, read [stable matching](/stable-matching/), the [Gale-Shapley algorithm](/gale-shapley/) and the [assignment problem](/assignment-problem/) in Volume 7.

**Chapter 42.9, Cooperative games and cost sharing**, is not written yet. It will cover the core and the nucleolus, the Shapley value, power indices of weighted voting games, cost sharing and bargaining. Meanwhile, read [LP duality](/lp-duality/) in Volume 15 and the [minimum spanning tree](/minimum-spanning-tree/) in Volume 7.

## How to read this volume

There is no course through the volume yet. Read Chapter 42.1 in the order its opening page gives, then Chapter 42.2, and do the exercises marked ◦ at the end of each. For each other chapter, its opening page lists written entries elsewhere that cover part of its ground.

Each entry stands on its own; its facts box lists what it needs, by entry number.

## What you need first

You need [expected value](/expected-value/) from Volume 1, since mixed strategies are judged by their expected payoff, and [linear programming](/linear-programming-problem/) with [LP duality](/lp-duality/) from Volume 15. The [zero-sum game](/zero-sum-game/) of Volume 29 is the starting point of Chapter 42.1, and Chapter 42.2 uses the classes [PPAD](/ppad/) and [TFNP](/tfnp/) of Volume 39. Chapter 42.6 uses the [Kendall tau distance](/kendall-tau-distance/) of Volume 6.

## The exercises

Chapters 42.1, 42.2 and 42.6 end with exercises in three bands. Exercises marked ◦ check that you read the entries closely; you should be able to do them in a few minutes. Exercises marked • ask you to use an idea in a new place; each takes some thought, and some need a short program. Exercises marked ★ are harder; some are results from research papers. Hints for many exercises are in the appendix *Hints to the exercises* at the end of the volume.

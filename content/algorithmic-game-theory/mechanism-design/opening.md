A town wants to know whether to build a bridge that costs 90. Three residents would value it at 40, 50 and 10, but only they know these numbers. If the town asks them and splits the cost by the answers, each one has a reason to say less than the truth. If it builds whenever the answers add up to 90, each one has a reason to say more. A seller of one item meets the same problem: the bidders know their values and the seller does not. Mechanism design asks how to pick the outcome and the payments so that the agents' own interests lead them to reveal what the designer needs.

The answers come in two kinds. Some are mechanisms: the Vickrey auction and its general form, the VCG mechanism, make truth telling the best plan for every agent whatever the others do, and choose the outcome of largest total value. Others are limits: no Bayesian truthful mechanism that buyers and sellers are willing to join trades efficiently between them in general without outside money, and when the residents' values can be any numbers, no dominant-strategy truthful mechanism that always makes the efficient choice for the bridge balances its budget. The algorithmic part of the subject adds a third kind: when the best outcome is hard to compute, it looks for truthful mechanisms that run in polynomial time and measures how far from optimal they must be.

## What the chapter covers

The chapter is in seven groups, read in order.

1. **The model.** [Quasilinear utility](/quasilinear-utility/), [direct mechanisms](/direct-revelation-mechanism/), and the two meanings of truthful: [dominant-strategy incentive compatibility](/dominant-strategy-incentive-compatibility/) (DSIC) and [Bayesian incentive compatibility](/bayesian-incentive-compatibility/) (BIC). Then [individual rationality](/individual-rationality/), [budget balance](/budget-balance/) and the [revelation principle](/revelation-principle/).
2. **Payments that align incentives with welfare.** [Groves mechanisms](/groves-mechanisms/), the [Clarke pivot rule](/clarke-pivot-rule/), the [VCG mechanism](/vcg-mechanism/), [affine maximizers](/affine-maximizer/) and the [AGV mechanism](/agv-mechanism/), which is BIC and budget balanced.
3. **One private number per agent.** In a [single-parameter environment](/single-parameter-environment/), a rule is truthful exactly when it is a [monotone allocation rule](/monotone-allocation-rule/), and [Myerson's lemma](/myerson-lemma/) gives the payments. [Truthful in expectation](/truthful-in-expectation/) is the randomized version.
4. **Characterizations of truthful rules.** [Cycle monotonicity](/cycle-monotonicity/) for many private numbers, [Roberts' theorem](/roberts-theorem/) for unrestricted domains, [Border's theorem](/border-theorem/) for interim allocation rules and [Maskin monotonicity](/maskin-monotonicity/) for Nash implementation.
5. **What cannot be had together.** The [Myerson-Satterthwaite theorem](/myerson-satterthwaite-theorem/), the [Green-Laffont theorem](/green-laffont-theorem/), and the [Cremer-McLean theorem](/cremer-mclean-theorem/) on correlated types.
6. **Truthful approximation.** [Maximal-in-range mechanisms](/maximal-in-range-mechanism/), [facility location](/facility-location-mechanism/) without money, [truthful scheduling on unrelated machines](/truthful-scheduling-unrelated-machines/) and the [Nisan-Ronen theorem](/nisan-ronen-conjecture/).
7. **Designing by computation.** [Automated mechanism design](/automated-mechanism-design/) by linear programming, [learned auctions](/differentiable-economics/) and [Bayesian persuasion](/bayesian-persuasion/).

## A first reading

For a first pass, read these ten entries in this order:

1. [Quasilinear utility](/quasilinear-utility/)
2. [Dominant-strategy incentive compatibility](/dominant-strategy-incentive-compatibility/)
3. [Revelation principle](/revelation-principle/)
4. [Groves mechanisms](/groves-mechanisms/)
5. [VCG mechanism](/vcg-mechanism/)
6. [Single-parameter environment](/single-parameter-environment/)
7. [Myerson's lemma](/myerson-lemma/)
8. [Bayesian incentive compatibility](/bayesian-incentive-compatibility/)
9. [Myerson-Satterthwaite theorem](/myerson-satterthwaite-theorem/)
10. [Truthful scheduling on unrelated machines](/truthful-scheduling-unrelated-machines/)

The first seven give the main positive results, VCG and Myerson's lemma. The last three show where they stop: Bayesian truthfulness is weaker than dominant strategies, even it cannot give efficient trade without a subsidy, and truthfulness can cost a factor that grows with the number of agents.

## Before you start

The solution concepts come from chapter 42.1: [dominant strategies](/dominant-strategy/), [Nash equilibrium](/nash-equilibrium/) and [Bayes-Nash equilibrium](/bayes-nash-equilibrium/). The [Vickrey auction](/vickrey-auction/) of chapter 42.5 is the first example everywhere, and its entry is short enough to read first. Several proofs and algorithms use other volumes. [Linear programming](/linear-programming-problem/) and [Farkas' lemma](/farkas-lemma/) are in Volume 15. The [max-flow min-cut theorem](/max-flow-min-cut-theorem/), used for Border's theorem, and the [Bellman-Ford algorithm](/bellman-ford/), used to compute payments from cycle monotonicity, are in Volume 7. The [approximation ratio](/approximation-ratio/) and [unrelated machine scheduling](/unrelated-machine-scheduling/) are in Volume 18. [Bayes' theorem](/bayes-theorem/), for Bayesian persuasion, is in Volume 25. You also need basic probability: expectations, independence and conditional distributions.

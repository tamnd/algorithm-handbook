Two heirs share an estate, three housemates share a rent, a court splits the goods of a divorcing couple, a
cluster shares its machines among users. In each case several parties must share something, they value its
parts differently, and there is no price that settles the matter. Fair division asks what "fair" can mean
when each party judges by its own measure, which fair outcomes always exist, and how to find them with few
questions or little computation. The simplest answer is divide and choose: one agent cuts, the other picks,
and neither has reason to complain.

The chapter has two halves. The first is about a divisible resource, modelled as the interval $[0, 1]$ in
the [cake cutting problem](/cake-cutting-problem/). There, proportional divisions are cheap, with
$\Theta(n \log n)$ queries, while envy-free divisions exist but are very expensive to find: the best
bounded protocol for $n$ agents uses a tower of exponentials, and with connected pieces no finite protocol
works for three or more agents. The second half is about indivisible goods, where envy-free allocations may
not exist at all. The research there is about relaxed goals, such as envy-freeness up to one good and the
maximin share, and about which of them can be reached together with efficiency.

## What the chapter covers

1. **The cake and the fairness goals.** The [cake cutting problem](/cake-cutting-problem/),
   [proportional division](/proportional-division/) and [envy-freeness](/envy-freeness/), and the
   [Robertson-Webb query model](/robertson-webb-query-model/), in which protocols ask eval and cut queries
   and the cost is their number.
2. **Proportional protocols.** [Divide and choose](/divide-and-choose/), the
   [Dubins-Spanier moving knife](/dubins-spanier-moving-knife/), the [last diminisher](/last-diminisher/)
   and the [Even-Paz algorithm](/even-paz-algorithm/), with the
   [Edmonds-Pruhs lower bound](/edmonds-pruhs-lower-bound/) showing that $O(n \log n)$ queries is optimal.
3. **Envy-free cake cutting.** The [Selfridge-Conway procedure](/selfridge-conway-procedure/) for three
   agents, the [Stromquist moving knife](/stromquist-moving-knife/) and
   [Stromquist's impossibility theorem](/stromquist-impossibility-theorem/) for connected pieces, and the
   [Brams-Taylor procedure](/brams-taylor-procedure/) and [Aziz-Mackenzie protocol](/aziz-mackenzie-protocol/)
   for any number of agents.
4. **Goods instead of cake.** The [adjusted winner procedure](/adjusted-winner/) for two parties, the
   [fair allocation of indivisible goods](/indivisible-goods-allocation/),
   [envy-freeness up to one good](/envy-freeness-up-to-one-good/) (EF1), and the two simple algorithms that
   reach it, [round-robin allocation](/round-robin-allocation/) and
   [envy-cycle elimination](/envy-cycle-elimination/).
5. **Maximin shares.** The [maximin share](/maximin-share/), the
   [instances where no allocation gives every agent its share](/mms-nonexistence-theorem/), and the
   [algorithms that give a fixed fraction of it](/approximate-mms-allocation/).
6. **Nash welfare and efficiency.** The [maximum Nash welfare allocation](/maximum-nash-welfare/), the
   theorem that it is EF1 and Pareto optimal ([the unreasonable fairness of MNW](/unreasonable-fairness-of-mnw/)),
   and the [Barman-Krishnamurthy-Vaish algorithm](/ef1-and-pareto-optimal-algorithm/), which reaches both
   properties in pseudo-polynomial time.
7. **Envy-freeness up to any good.** The stronger relaxation [EFX](/envy-freeness-up-to-any-good/) and the
   proof of [EFX existence for three agents](/efx-existence-for-three-agents/).
8. **Chores and rent.** [Chore division](/chore-division/), [rental harmony](/rental-harmony/) and
   [Su's algorithm](/su-rental-harmony-algorithm/), which finds an approximate rent division by a walk
   through a triangulated simplex of prices.
9. **Splitting so that everyone agrees.** [Consensus halving](/consensus-halving/), which is PPA-complete,
   and the [necklace splitting theorem](/necklace-splitting-theorem/).

## A first reading

Read these in order:

1. [Cake cutting problem](/cake-cutting-problem/)
2. [Proportional division](/proportional-division/)
3. [Envy-freeness](/envy-freeness/)
4. [Divide and choose](/divide-and-choose/)
5. [Robertson-Webb query model](/robertson-webb-query-model/)
6. [Last diminisher](/last-diminisher/)
7. [Even-Paz algorithm](/even-paz-algorithm/)
8. [Selfridge-Conway procedure](/selfridge-conway-procedure/)
9. [Fair allocation of indivisible goods](/indivisible-goods-allocation/)
10. [Envy-freeness up to one good](/envy-freeness-up-to-one-good/)
11. [Round-robin allocation](/round-robin-allocation/)
12. [Maximin share](/maximin-share/)
13. [Maximum Nash welfare allocation](/maximum-nash-welfare/)
14. [Rental harmony](/rental-harmony/)

They give the two goals, the query model, the main proportional protocols, the first envy-free protocol
and the basic notions for goods. On a first pass, skip the lower bounds, the protocols for $n$ agents
with envy-free pieces, the research entries on maximin shares and EFX, and the last group; each of them
builds on the entries above.

## Before you start

The chapter needs little beyond discrete mathematics and some comfort with proofs.
[Pareto optimality](/pareto-optimality/) (Volume 15) is used from the fourth group on. The query counts
rest on the [query model](/query-model/) of Volume 39, and the lower bound uses an
[adversary argument](/adversary-argument/) (Volume 1). Envy-cycle elimination uses
[cycle detection](/cycle-detection/) (Volume 7), the maximin share algorithms use the
[approximation ratio](/approximation-ratio/) (Volume 18), and the Barman-Krishnamurthy-Vaish algorithm runs
in [pseudo-polynomial time](/pseudo-polynomial-time/) (Volume 39). Su's algorithm follows the proof of
[Sperner's lemma](/sperner-lemma/) earlier in this volume, and the necklace theorem uses the class
[TFNP](/tfnp/) of Volume 39.

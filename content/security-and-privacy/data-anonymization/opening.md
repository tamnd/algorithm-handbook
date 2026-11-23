Removing names from a data set does not make it anonymous. Sweeney's estimate from the 1990 United States census was that about 87 percent of the population was likely unique on the 5-digit ZIP code, sex and full date of birth, and she described how a release of state employees' medical records without names was joined with a voter list on exactly those three attributes. Later work did the same for other kinds of data. Narayanan and Shmatikov showed that eight ratings with dates known to within two weeks, two of them allowed to be wrong, single out 99 percent of the records of the Netflix Prize data, and the shape of a person's links in a social network turned out to be an identifier too. Each such set of ordinary attributes is a quasi-identifier, and the join is a linkage attack.

Anonymization is the problem of changing a data set so that such joins fail while the data stay useful. The classical answer is k-anonymity: coarsen or delete values until every record shares its quasi-identifier values with at least $k - 1$ others. It raises algorithmic questions that the chapter answers in detail: how to search the lattice of generalizations, how hard the cheapest k-anonymization is (NP-hard for each fixed $k \ge 3$), and how close an approximation can come. k-anonymity also has known holes. A group of five records that all carry the same diagnosis tells the diagnosis, which led to l-diversity and t-closeness, and these have weaknesses of their own. Statistical agencies have a separate tradition, statistical disclosure control, which perturbs records by aggregation, swapping or randomization and protects published tables by hiding or adjusting cells.

All of these are syntactic conditions on the released data. None of them gives a guarantee against an attacker with arbitrary background knowledge; that kind of guarantee is what [differential privacy](/differential-privacy-definition/) was designed to give, and Chapter 45.8 treats it. The re-identification rates in the entries are measurements on stated data sets.

## What the chapter covers

1. **Re-identification.** The [quasi-identifier](/quasi-identifier/) and the [linkage attack](/linkage-attack/) are the basic threat. [Pseudonymization](/pseudonymization/) keeps records linkable and is still personal data under the GDPR, and [sparse dataset de-anonymization](/sparse-dataset-deanonymization/) shows why long sparse records cannot be anonymized by removing identifiers.
2. **k-anonymity by generalization.** [k-anonymity](/k-anonymity/) and [generalization and suppression](/generalization-and-suppression/) define the lattice of full-domain generalizations. [Datafly](/datafly/) climbs it greedily, [Samarati's algorithm](/samarati-algorithm/) binary searches its heights, [Incognito](/incognito/) finds every minimal vector, and [Mondrian](/mondrian-anonymization/) cuts the data space at medians.
3. **The complexity of optimal k-anonymity.** [NP-hardness of optimal k-anonymity](/k-anonymity-np-hardness/) reduces perfect matching in $k$-uniform hypergraphs to cell suppression, and the [$O(k)$ approximation](/k-anonymity-approximation/) builds a forest of small trees.
4. **Protecting the sensitive values.** [l-diversity](/l-diversity/), [t-closeness](/t-closeness/), [anatomy](/anatomy-bucketization/), [m-invariance](/m-invariance/) for republication and [km-anonymity](/km-anonymity/) for sets of items.
5. **Statistical disclosure control of microdata.** [Microaggregation](/microaggregation/) and its heuristic [MDAV](/mdav/), [data swapping](/data-swapping/) and the [post-randomization method](/post-randomization-method/).
6. **Tables with totals.** The [cell suppression problem](/cell-suppression-problem/) and [controlled tabular adjustment](/controlled-tabular-adjustment/), both built on linear programs.
7. **Graphs, locations and linkage.** The [active attack on social graphs](/active-attack-on-social-graphs/), [social network de-anonymization](/social-network-deanonymization/), [k-degree anonymization](/k-degree-anonymization/), [spatial cloaking](/spatial-cloaking/) and [privacy-preserving record linkage](/privacy-preserving-record-linkage/).

## A first reading

Read these in order:

1. [Quasi-identifier](/quasi-identifier/)
2. [Linkage attack](/linkage-attack/)
3. [k-anonymity](/k-anonymity/)
4. [Generalization and suppression](/generalization-and-suppression/)
5. [Datafly](/datafly/)
6. [Mondrian](/mondrian-anonymization/)
7. [NP-hardness of optimal k-anonymity](/k-anonymity-np-hardness/)
8. [l-diversity](/l-diversity/)
9. [t-closeness](/t-closeness/)
10. [Microaggregation](/microaggregation/)
11. [Cell suppression problem](/cell-suppression-problem/)
12. [Sparse dataset de-anonymization](/sparse-dataset-deanonymization/)

Samarati's algorithm and Incognito can wait until you need an exact search of the lattice. The approximation algorithm, m-invariance, km-anonymity, controlled tabular adjustment and the graph entries build on the first reading and can be read in any order after it.

## Before you start

The search algorithms use a [greedy algorithm](/greedy-algorithm/), [binary search](/binary-search/), [breadth-first search](/breadth-first-search/), the [kd-tree](/kd-tree/) and [median finding](/median-finding/). The hardness results assume [NP-completeness](/np-complete/), [polynomial-time reductions](/polynomial-time-reduction/), [three-dimensional matching](/three-dimensional-matching/) and the [approximation ratio](/approximation-ratio/). l-diversity uses [Shannon entropy](/shannon-entropy/), and t-closeness the [total variation distance](/total-variation-distance/). Table protection needs [linear programming](/linear-programming-problem/) and [LP duality](/lp-duality/); microaggregation needs the [clustering problem](/clustering-problem/); the post-randomization method needs a [Markov chain](/markov-chain/) matrix and [Gaussian elimination](/gaussian-elimination/). Pseudonymization uses [HMAC](/hmac/), record linkage the [Bloom filter](/bloom-filter/), spatial cloaking the [quadtree](/quadtree/), and the graph entries the [degree](/degree/) of a vertex in a [simple graph](/simple-graph/).

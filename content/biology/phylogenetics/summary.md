## What to remember

- **The space of trees is huge.** There are $(2n-5)!!$ unrooted and $(2n-3)!!$ rooted binary trees on $n$ taxa. An unrooted binary tree has $n-3$ nontrivial [splits](/splits-of-a-tree/), and they determine it.
- **Scoring a fixed tree is exact; finding the best tree is not.** On a fixed tree, [Fitch's algorithm](/fitch-algorithm/) takes $\Theta(mnk)$ time, [Sankoff's](/sankoff-algorithm/) $\Theta(mnk^2)$ for any cost table, and [pruning](/felsenstein-pruning/) $\Theta(mnk^2)$ for the likelihood. Over all trees, [maximum parsimony](/maximum-parsimony-np-hard/) and [maximum likelihood](/ml-tree-np-hard/) are NP-hard, so programs search locally with [NNI](/nearest-neighbor-interchange/), SPR and TBR moves ($2(n-3)$, $2(n-3)(2n-7)$ and $O(n^3)$ neighbors).
- **A matrix is a tree metric exactly when, for every four taxa, the two largest of the three pair sums are equal.** [Neighbor-joining](/neighbor-joining/) is exact on every tree metric and returns the right topology when every entry is off by less than half the shortest edge. [UPGMA](/upgma/) is exact only when the matrix is an ultrametric, that is, when the data follow a clock.
- **Distances need a model.** Under [Jukes-Cantor](/jukes-cantor-model/), a proportion $p$ of differing sites gives $d = -\tfrac34 \ln(1 - \tfrac43 p)$, undefined for $p \ge 3/4$. Corrected distances add along paths; raw proportions do not.
- **Consistency depends on the model.** Parsimony can converge to the wrong tree: in the four-taxon model of [long-branch attraction](/long-branch-attraction/) it does so when $p^2 > q(1-q)$. Maximum likelihood under the true model, and neighbor-joining on consistently corrected distances, are statistically consistent.
- **Bayesian answers converge only in the limit.** The chain visits each tree with its posterior frequency as the run grows, with no useful general bound on the mixing time. Bootstrap support is not the probability that a split is true.
- **Trees are compared by splits and by moves.** The [Robinson-Foulds distance](/robinson-foulds-distance/) is at most $2(n-3)$ and takes $O(n)$ time. The NNI, SPR and TBR distances are NP-hard, and the rooted SPR distance is the size of a maximum agreement forest minus one.
- **Gene trees are not species trees.** For three species with an inner branch of $T$ coalescent units, a gene tree matches the species tree with probability $1 - \tfrac23 e^{-T}$. In the anomaly zone the most likely gene tree differs from the species tree. Concatenating all loci can be inconsistent under the [multispecies coalescent](/multispecies-coalescent/), while [ASTRAL](/astral/) on true gene trees is consistent.

## The main methods side by side

| Method | Input and model | Guarantee | Time |
|---|---|---|---|
| [UPGMA](/upgma/) | distances, clock | exact on ultrametrics | $O(n^3)$ |
| [Neighbor-joining](/neighbor-joining/) | distances, no clock | exact on tree metrics; correct within half the shortest edge | $O(n^3)$ |
| [Four-point method](/four-point-method/) | exact tree metric | exact on tree metrics; none on other input | $O(n^2)$ |
| [Fitch](/fitch-algorithm/) | characters, unit cost, fixed rooted binary tree | exact score | $\Theta(mnk)$ |
| [Sankoff](/sankoff-algorithm/) | characters, any cost table, fixed tree | exact score | $\Theta(mnk^2)$ |
| [Gusfield](/gusfield-perfect-phylogeny/) | binary characters | decides perfect phylogeny exactly | $\Theta(nm)$ |
| [Pruning](/felsenstein-pruning/) | sequences, substitution model, fixed tree | exact likelihood | $\Theta(mnk^2)$ |
| [Maximum parsimony](/maximum-parsimony/) | characters, over all trees | NP-hard; can be inconsistent | heuristic search |
| [Maximum likelihood](/maximum-likelihood-phylogeny/) | sequences, over all trees | NP-hard; consistent under the model | heuristic search |
| [Day's algorithm](/day-algorithm/) | two trees | exact Robinson-Foulds distance | $\Theta(n)$ |
| [ASTRAL](/astral/) | $k$ gene trees, multispecies coalescent | exact within the allowed bipartitions; consistent | $O(nkx^2)$ |

: Main methods of the chapter. For Fitch, Sankoff and pruning, $n$ is the number of nodes of the tree, $m$ the number of sites (distinct site patterns for pruning) and $k$ the number of states. For Gusfield, $n$ is the number of taxa and $m$ the number of characters. For ASTRAL, $n$ is the number of species and $x$ the number of allowed bipartitions.

## Choosing a method

- For a quick tree of many taxa, run neighbor-joining on distances corrected under a [substitution model](/substitution-model/). Use UPGMA only when a [molecular clock](/molecular-clock/) is plausible.
- For an accurate tree from one alignment, use maximum likelihood under a model such as [GTR](/gtr-model/) with [rate variation](/rate-heterogeneity/), searched by SPR or NNI moves. Report [bootstrap](/phylogenetic-bootstrap/) support.
- Parsimony needs no model and suits closely related taxa with few changes. Distrust it when some branches are much longer than others.
- Use [Bayesian inference](/bayesian-phylogenetic-inference/) when priors matter, as in [divergence time estimation](/divergence-time-estimation/) with a relaxed clock. Run several chains and check that they agree, since a finite run carries no guarantee.
- For many loci that disagree, estimate one gene tree per locus and combine them with ASTRAL rather than concatenating the loci.
- When the data conflict in ways no tree can show, draw a split network with [NeighborNet](/neighbor-net/).

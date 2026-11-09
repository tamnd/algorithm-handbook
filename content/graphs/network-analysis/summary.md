## What to remember

- **Measures, algorithms and models work together.** A measure such as [clustering](/clustering-coefficient/) or [modularity](/modularity/) says what to compute, an algorithm computes it at scale, and a random model says whether the value is surprising. A number from a real network means little until it is compared with a [null model](/configuration-model/) that has the same degrees.

- **Each centrality answers a different question.** [Degree](/degree-centrality/) counts contacts, [closeness](/closeness-centrality/) and [harmonic](/harmonic-centrality/) centrality measure distance to everyone, [betweenness](/betweenness-centrality/) counts the shortest paths through a vertex, and [eigenvector](/eigenvector-centrality/), [Katz](/katz-centrality/) and [PageRank](/pagerank/) reward links from central vertices. They can rank the same vertices differently.

- **Betweenness costs one search per source.** [Brandes' algorithm](/brandes-algorithm/) counts shortest paths forward and accumulates dependencies backward, in $O(nm)$ time without weights, where the older method summed over all triples in $\Theta(n^3)$ time.

- **PageRank is a random walk with restarts.** The damping factor makes the walk ergodic, so the stationary vector exists, is unique, and is reached by power iteration at the rate $\alpha^k$. [HITS](/hits-algorithm/) instead computes two eigenvectors, of $A^{\mathsf T}A$ and $AA^{\mathsf T}$.

- **Degree ordering tames triangles and cores.** Orienting edges toward higher degree gives [triangle listing](/triangle-listing-by-degree/) in $O(m^{3/2})$ time, and peeling vertices of minimum degree gives all [core numbers](/batagelj-zaversnik-algorithm/) in linear time.

- **Random graphs have sharp thresholds.** In $G(n, c/n)$ a [giant component](/erdos-renyi-giant-component-theorem/) appears at $c = 1$, and $G(n, p)$ becomes [connected](/erdos-renyi-connectivity-threshold/) at $p = \ln n/n$. Real networks differ from this model in two ways: they cluster, which the [Watts-Strogatz model](/watts-strogatz-model/) captures, and they have heavy-tailed degrees, which [preferential attachment](/preferential-attachment/) explains.

- **Communities are found by heuristics.** Maximizing modularity is NP-hard, and the [Louvain](/louvain-method/) and [Leiden](/leiden-algorithm/) methods are greedy local search with aggregation. Modularity has a resolution limit and cannot see small communities in a large network.

- **Spreading is percolation.** An [SIR](/sir-epidemic-model/) outbreak and an [independent cascade](/independent-cascade-model/) both reach the cluster of their seeds in a random subgraph. Because the expected spread is submodular, the [greedy seed choice](/greedy-influence-maximization/) is within a factor $1 - 1/e$ of the best.

## The algorithms side by side

| Algorithm | Computes | Time | Notes |
|---|---|---|---|
| [Brandes](/brandes-algorithm/) | betweenness of all vertices | $O(nm)$ | $O(nm + n^2 \log n)$ with weights |
| [PageRank](/pagerank/) | stationary vector | $\Theta(k(n+m))$ | $k$ rounds of power iteration |
| [HITS](/hits-algorithm/) | hub and authority scores | $\Theta(k(n+m))$ | alternating updates |
| [SimRank](/simrank/) | similarity of all pairs | $\Theta(K(n^2 + m^2))$ | $\Theta(n^2)$ memory |
| [Triangle listing](/triangle-listing-by-degree/) | all triangles | $O(n + m^{3/2})$ | [compact-forward](/compact-forward-algorithm/) merges sorted lists |
| [Batagelj-Zaversnik](/batagelj-zaversnik-algorithm/) | all core numbers | $\Theta(n + m)$ | bucket queue of degrees |
| [ANF](/anf-algorithm/) | neighbourhood function | $\Theta(h\,r\,(n+m))$ | Flajolet-Martin sketches |
| [ESU](/esu-algorithm/) | connected $k$-vertex subgraphs | $O(n + m + k(k + \Delta)s)$ | each subgraph exactly once |
| [Girvan-Newman](/girvan-newman-algorithm/) | community hierarchy | $O(m^2 n)$ | recomputes betweenness after each removal |
| [Louvain](/louvain-method/) | communities | $O(n + m)$ per sweep | local moves and aggregation |
| [Leiden](/leiden-algorithm/) | connected communities | $O(n + m)$ per phase | adds a refinement phase |
| [Label propagation](/label-propagation-algorithm/) | communities | $O(n + m)$ per round | a few rounds suffice in practice |
| [Greedy influence](/greedy-influence-maximization/) | $k$ seeds | $\Theta(k\,n\,r\,(n+m))$ | $r$ Monte Carlo runs per estimate |

: The main algorithms of the chapter. $n$ is the number of vertices and $m$ the number of edges; the other parameters are the number of rounds $k$, $K$ or $h$, the number of sketches or samples $r$, the maximum degree $\Delta$ and the number $s$ of connected vertex sets of at most $k$ vertices.

## Choosing an algorithm

- To rank vertices of an undirected network by how much traffic passes through them, use betweenness with [Brandes' algorithm](/brandes-algorithm/), sampling sources on very large graphs.
- To rank pages or papers by links, use [PageRank](/pagerank/); to rank them relative to a few seeds, use [personalized PageRank](/personalized-pagerank/).
- To count triangles or compute clustering on a large graph, use [compact-forward](/compact-forward-algorithm/) triangle listing.
- To find the dense centre of a network, compute [core numbers](/batagelj-zaversnik-algorithm/).
- To estimate distances and the [effective diameter](/effective-diameter/) of a graph with billions of edges, use [ANF](/anf-algorithm/) sketches rather than all-pairs searches.
- To find communities in a large graph, use [Leiden](/leiden-algorithm/), which fixes the disconnected communities that [Louvain](/louvain-method/) can return. Use [clique percolation](/clique-percolation-method/) when communities overlap.
- To predict links, start with [common neighbours](/common-neighbors/) and the [Adamic-Adar index](/adamic-adar-index/); turn to [node embeddings](/node-embedding/) when features for a learned model are needed.
- To test whether a pattern is significant, compare it with the [configuration model](/configuration-model/), not with the [Erdős-Rényi model](/erdos-renyi-model/).

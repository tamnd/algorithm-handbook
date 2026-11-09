## What to remember

- **Augmenting paths decide everything.** A matching is maximum exactly when no [augmenting path](/augmenting-path/) exists ([Berge](/berge-lemma/)). The symmetric difference of two matchings is a union of alternating paths and even cycles, and with $M$ and a maximum $M^*$ it holds $|M^*| - |M|$ vertex-disjoint augmenting paths.
- **Greedy is half right.** A [maximal matching](/maximal-matching/) has at least half the edges of a maximum one, and its $2|M|$ ends form a vertex cover at most twice the smallest.
- **Bipartite min-max theorems.** One side can be matched completely exactly when $|N(S)| \ge |S|$ for every set $S$ on that side ([Hall](/hall-theorem/)), and the largest matching equals the smallest vertex cover ([Kőnig](/konig-theorem/)). In every graph without isolated vertices, a maximum matching and a minimum edge cover have sizes that add up to $n$ ([Gallai](/gallai-identity/)).
- **Bipartite algorithms:** [Kuhn](/kuhn-algorithm/) in $O(nm)$, one search per vertex; [Hopcroft-Karp](/hopcroft-karp/) in $O(m \sqrt{n})$, because $O(\sqrt{n})$ phases of shortest augmenting paths suffice.
- **The assignment problem** is solved in $O(n^3)$ by the [Hungarian algorithm](/hungarian-algorithm/). Prices on the vertices with $u_i + v_j \le c_{ij}$, tight on the matching, prove optimality, which is linear programming duality in combinatorial form.
- **Stable matchings always exist** for two sides. [Gale-Shapley](/gale-shapley/) finds one in time linear in the preference lists, and it is the best stable matching for every proposer and the worst for every receiver. With one side ranking itself, a stable matching may not exist, and [Irving's algorithm](/irving-stable-roommates/) decides it.
- **General graphs:** a perfect matching exists exactly when, for every $S$, the graph minus $S$ has at most $|S|$ odd components ([Tutte](/tutte-theorem/)). [Edmonds' algorithm](/edmonds-blossom/) contracts odd cycles to find augmenting paths in $O(n^3)$, and [Micali-Vazirani](/micali-vazirani-algorithm/) reaches $O(m \sqrt{n})$.
- **Algebra:** a graph has a perfect matching exactly when the [Tutte matrix](/tutte-matrix/) is nonsingular as a matrix of polynomials. Random values test it with one determinant.

## The algorithms side by side

| Algorithm | Problem | Time | Extra space |
|---|---|---|---|
| Greedy | maximal matching | $\Theta(n + m)$ | $\Theta(n)$ |
| [Kuhn](/kuhn-algorithm/) | bipartite maximum matching | $O(nm)$ | $\Theta(n)$ |
| [Hopcroft-Karp](/hopcroft-karp/) | bipartite maximum matching | $O((n + m) \sqrt{n})$ | $\Theta(n + m)$ |
| [Hungarian](/hungarian-algorithm/) | assignment, $n \times n$ | $O(n^3)$ | $\Theta(n + m)$ |
| [Jonker-Volgenant](/jonker-volgenant-algorithm/) | assignment | $O(n^3)$ | $\Theta(n)$ |
| [Auction](/auction-algorithm/) | assignment | $O(n^3 C + n^2)$ | $\Theta(n^2)$ |
| [Gale-Shapley](/gale-shapley/) | stable marriage | $O(n + m)$ | $\Theta(n + m)$ |
| [Edmonds](/edmonds-blossom/) | general maximum matching | $O(n^3)$ | $\Theta(n + m)$ |
| [Micali-Vazirani](/micali-vazirani-algorithm/) | general maximum matching | $O(m \sqrt{n})$ | $\Theta(n + m)$ |
| [Weighted blossom](/maximum-weight-matching/) | general maximum-weight matching | $O(nm + n^2 \log n)$ | $O(n + m)$ |

: Bounds from the entries. For Gale-Shapley $m$ is the total length of the preference lists; for the auction algorithm $C$ is the largest difference between two benefits.

## Choosing an algorithm

- Unweighted and bipartite: Hopcroft-Karp, or Kuhn's shorter code when $n$ is small; a maximum flow solver also works.
- Costs on a dense square matrix: the Hungarian algorithm, or Jonker-Volgenant in practice. For sparse or very large instances, auction or min-cost flow codes.
- Preferences instead of weights: Gale-Shapley, with the side that should be favoured proposing; with capacities, the hospitals-residents version.
- General graphs: Edmonds' blossom algorithm from a library; implement it only with care. For a quick randomized test of a perfect matching, a determinant of the Tutte matrix with random values.
- A fast approximation: a maximal matching, in linear time, is within a factor 2.

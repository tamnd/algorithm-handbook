1. ◦ The graph $G$ has the vertices $1, \ldots, 5$ and the edges $12, 13, 23, 24, 34, 45$. Compute the local [clustering coefficient](/clustering-coefficient/) of every vertex, the average local clustering under both conventions for vertices of degree 1, and the global clustering coefficient. Are the three numbers equal?

2. ◦ For the path $0, 1, 2, 3, 4$, compute the [degree](/degree-centrality/), [closeness](/closeness-centrality/), [harmonic](/harmonic-centrality/) and [betweenness](/betweenness-centrality/) centrality of every vertex. Do the four measures rank the vertices in the same order?

3. ◦ A directed graph on the vertices $1, 2, 3, 4$ has the arcs $(1,2), (2,1), (2,3), (3,4), (4,3), (4,1), (1,3)$. Compute its [reciprocity](/reciprocity/) $r$, its density $\bar a$ and the corrected coefficient $\rho = (r - \bar a)/(1 - \bar a)$. Does the graph have more or fewer mutual arcs than chance?

4. ◦ The pair $\{u, v\}$ has two [common neighbours](/common-neighbors/), each of degree 5. The pair $\{x, y\}$ has one common neighbour, of degree 2. Rank the two pairs by the number of common neighbours, by the [Adamic-Adar index](/adamic-adar-index/) and by the resource allocation index $\sum_w 1/d(w)$.

5. ◦ The graph $H$ has the vertices $1, \ldots, 8$ and the edges $12, 13, 14, 23, 24, 34, 36, 45, 56, 57, 67, 78$. Find the [core number](/k-core/) of every vertex, and give the 1-core, the 2-core and the 3-core.

6. ◦ In the [Erdős-Rényi model](/erdos-renyi-model/) $G(n, p)$ with $n = 1000$ and $p = 0.01$, find the expected number of edges, the expected degree of a vertex, the expected number of triangles and the expected clustering coefficient. Is $p$ above the [connectivity threshold](/erdos-renyi-connectivity-threshold/)?

7. ◦ Two triangles $\{1, 2, 3\}$ and $\{4, 5, 6\}$ are joined by the edge $34$. Compute the [modularity](/modularity/) of the partition into the two triangles and of the partition with a single community.

8. ◦ A signed graph has the positive edges $12, 34, 45$ and the negative edges $13, 15, 24$. Show that it is balanced in the sense of the [structural balance theorem](/structural-balance-theorem/) by giving the two groups. Then add the negative edge $35$ and find a cycle that shows the new graph is not balanced.

9. ◦ Find the degree distribution of the star $K_{1,k}$ for $k \ge 2$, and show that its degree [assortativity](/assortativity/) is $-1$.

10. • A directed graph on the vertices $1, 2, 3, 4$ has the arcs $(1,2), (1,3), (2,3), (3,1), (4,3)$. Compute its [PageRank](/pagerank/) with damping factor $\alpha = 0.85$. Which value can be found without solving any equations?

11. • A directed graph on the vertices $1, \ldots, 6$ has the arcs $(1,3), (1,4), (2,3), (2,4), (2,5), (6,5)$. Compute the [HITS](/hits-algorithm/) authority and hub scores, each scaled so that its largest entry is 1.

12. • For which values of $\alpha$ is [Katz centrality](/katz-centrality/) defined on the star $K_{1,3}$? Compute it for $\alpha = 1/2$, using $x = ((I - \alpha A^{\mathsf T})^{-1} - I)\mathbf{1}$.

13. • The graph has the vertices $s, a, b, c, d$ and the edges $sa, sb, ac, bc, cd$. Run one phase of [Brandes' algorithm](/brandes-algorithm/) from $s$: give the number $\sigma_{sv}$ of shortest paths to each vertex and the dependency $\delta_s(v)$ of each vertex. Then give the betweenness of every vertex, and check that the total equals $\sum_{\{s,t\}} (d(s,t) - 1)$.

14. • Orient each edge of the graph $H$ of Exercise 5 from the endpoint of smaller degree to the endpoint of larger degree, breaking ties by label, as in [triangle listing by degree](/triangle-listing-by-degree/). Give the out-neighbour lists, list the triangles, and compare the largest out-degree with $\sqrt{2m}$.

15. • Count the connected sets of 3 vertices in $H$, split into triangles and induced paths, as a [motif enumeration](/network-motif-enumeration/) would. Check the counts against $\sum_v \binom{d(v)}{2}$.

16. • Show that every partition of the complete graph $K_n$ has modularity at most 0, so the best partition of $K_n$ is the single community.

17. • In the ring lattice of the [Watts-Strogatz model](/watts-strogatz-model/), each vertex is joined to its $k$ nearest vertices on each side. Show that the clustering coefficient of every vertex is $\frac{3(k-1)}{2(2k-1)}$, and find its limit as $k$ grows.

18. • In $G(n, c/n)$ the fraction $S$ of vertices in the [giant component](/giant-component/) solves $S = 1 - e^{-cS}$. Solve this numerically for $c = 1.5$, $2$ and $3$.

19. • In the [configuration model](/configuration-model/) with every degree equal to 3, find the exact expected number of self-loops and its limit as $n$ grows.

20. • In the [Barabási-Albert model](/barabasi-albert-model/), a vertex born at time $i$ has degree about $m\sqrt{t/i}$ at time $t$. At what time does a vertex born at time 100 reach degree $10m$? How old must the network be for the first vertex to have degree $1000m$?

21. • In the [independent cascade model](/independent-cascade-model/), the arcs $(a,b), (a,c), (b,d), (c,d)$ each have probability $1/2$. Compute the expected spread of each single seed, and run the [greedy method](/greedy-influence-maximization/) for two seeds with exact spreads. Is its answer optimal?

22. • By the [percolation](/percolation/) formula $\phi_c = \langle k \rangle / (\langle k^2 \rangle - \langle k \rangle)$, find the threshold for a random 3-regular graph and for a configuration model in which half the vertices have degree 1 and half have degree 5. Which network is more fragile under random removal of edges?

23. ★ Prove the dependency recurrence of Brandes' algorithm: $\delta_s(v) = \sum_{w : v \in P_s(w)} \frac{\sigma_{sv}}{\sigma_{sw}} (1 + \delta_s(w))$, where $P_s(w)$ is the set of predecessors of $w$ on shortest paths from $s$.

24. ★ Show that the expected spread in the independent cascade model is a monotone submodular function of the seed set, using the live-edge view. Explain why this gives the greedy method its factor $1 - 1/e$.

25. ★ In $G(n, c/n)$ with $c < 1$ fixed, show that the expected number of vertices that lie on cycles is at most $\frac{c^3}{2(1-c)}$, so almost all vertices are in tree components.

26. ★ Show that one step of PageRank power iteration with damping factor $\alpha$ reduces the $L_1$ distance to the PageRank vector by a factor of at least $\alpha$. How many steps are enough to reduce the distance by a factor of $10^8$ when $\alpha = 0.85$?

## What to remember

- A graph is $G = (V, E)$ with $n = |V|$ vertices and $m = |E|$ edges. A directed edge is an ordered pair $(u, v)$, an undirected edge an unordered pair $\{u, v\}$. In this volume an undirected graph is simple unless a page says otherwise, so $m \le \binom{n}{2}$.
- **The handshake lemma.** $\sum_v d(v) = 2m$ in an undirected graph, and $\sum_v d^+(v) = \sum_v d^-(v) = m$ in a directed one. So the number of vertices of odd degree is even, the average degree is $2m/n$, and the adjacency lists of an undirected graph hold $2m$ entries.
- **Dense and sparse** describe families of graphs, not one graph: dense means $m = \Theta(n^2)$, sparse usually means $m = O(n)$. Trees, planar graphs, road networks and most real networks are sparse.
- **The adjacency list** uses $\Theta(n + m)$ space and lists the neighbours of $u$ in $\Theta(d(u))$ time. Any algorithm that reads each neighbourhood once, such as breadth-first or depth-first search, then runs in $\Theta(n + m)$ time.
- **The adjacency matrix** uses $\Theta(n^2)$ space and answers "is $(u, v)$ an edge?" in $O(1)$ time, but a scan of all neighbourhoods costs $\Theta(n^2)$. It suits dense graphs and algorithms that are matrix computations.
- **The cost of a problem can depend on the representation by more than a constant.** Deciding whether a graph has any edge needs all $\binom{n}{2}$ pair queries when only pair queries are allowed, and $O(n)$ time with neighbour lists. Yet the [universal sink](/universal-sink/) is found from a matrix with at most $3(n - 1)$ probes.
- **Static graphs are packed.** [Compressed sparse row](/compressed-sparse-row/) stores all lists in $n + 1 + m$ words, is built from an edge list by one counting sort in $\Theta(n + m)$ time, and reads each neighbourhood from consecutive memory. Transposing it is another counting sort.
- **The space lower bound** for graphs with $n$ vertices and $m$ edges is $\log_2 \binom{\binom{n}{2}}{m}$ bits for undirected graphs, about $m \log_2(n^2/m)$. Succinct structures come within $O(m)$ bits of it, and web graph compressors go below it on real data, to a few bits per edge.

## The representations side by side

| Structure | Space | Adjacent$(u, v)$ | Neighbors$(u)$ | Add edge | Remove edge |
|---|---|---|---|---|---|
| [Adjacency matrix](/adjacency-matrix/) | $\Theta(n^2)$ | $O(1)$ | $\Theta(n)$ | $O(1)$ | $O(1)$ |
| [Bitset matrix](/bitset-adjacency-matrix/) | $n \lceil n/w \rceil$ words | $O(1)$ | $O(n/w + d)$ | $O(1)$ | $O(1)$ |
| [Adjacency list](/adjacency-list/) | $\Theta(n + m)$ | $O(d)$ | $\Theta(d)$ | $O(1)$ amortized | $O(d)$ |
| [Hash-based adjacency](/hash-based-adjacency/) | $\Theta(n + m)$ | $O(1)$ expected | $\Theta(d)$ | $O(1)$ expected amortized | $O(1)$ expected |
| [Edge list](/edge-list/) | $\Theta(m)$ | $O(m)$ | $\Theta(m)$ | $O(1)$ amortized | $O(m)$ |
| [Compressed sparse row](/compressed-sparse-row/) | $n + 1 + m$ words | $O(\log d)$ | $\Theta(d)$ | $\Theta(n + m)$ rebuild | $\Theta(n + m)$ rebuild |

: Worst-case costs for a directed graph, where $d$ is the out-degree of $u$ and $w$ is the word length. The adjacency list and the edge list add an edge without testing whether it is already there. The $O(\log d)$ query of compressed sparse row assumes sorted rows.

## Choosing a representation

- For a sparse graph and any algorithm that walks from vertices to their neighbours, use adjacency lists. This is the default.
- For a dense graph, or an algorithm that asks about arbitrary pairs in its inner loop, use an adjacency matrix; for more than a few thousand vertices, pack it into bits.
- When you need fast pair queries and linear space, or the vertices are strings, use hash sets, or a [symbol graph](/symbol-graph/) in front of integer lists.
- When the graph is built once and read many times, convert it to compressed sparse row, and keep the compressed sparse column form as well if the algorithm reads in-neighbours.
- When edges are records with identities of their own, as in flow networks and multigraphs, use an [incidence list](/incidence-list/) or a [forward star](/forward-star/).
- When the graph is a rule, such as the positions of a puzzle, do not store it at all: compute neighbours on demand, as an [implicit graph](/implicit-graph/).

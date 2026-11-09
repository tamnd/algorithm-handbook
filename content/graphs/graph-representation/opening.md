A graph is a set of vertices and a set of edges, each edge joining two vertices. That is the whole definition, and it fits a road map, a social network, the links of the web, the calls between the functions of a program and the moves of a puzzle. Every later chapter of this volume runs an algorithm on such a thing. Before it can run, two questions need answers. What exactly is a graph: may an edge have a direction, a weight, a twin, or the same vertex at both ends? And how is it stored, so that the questions an algorithm asks of it are cheap?

The second question matters more than it seems. On an [adjacency list](/adjacency-list/), [breadth-first search](/breadth-first-search/) runs in $\Theta(n + m)$ time for $n$ vertices and $m$ edges. On an [adjacency matrix](/adjacency-matrix/), the same search takes $\Theta(n^2)$, which for a road network of a million crossings is the difference between a fraction of a second and many minutes, even before asking where $10^{12}$ matrix cells would be kept. The choice changes the bound, not only the constant factor.

## What the chapter covers

The chapter is in nine groups, read in order.

1. **Vertices and edges.** The [graph](/graph/) as an abstract type, [directed](/directed-graph/) and [undirected](/undirected-graph/) edges, and the conventions of the volume: an undirected graph is [simple](/simple-graph/) unless a page says otherwise, while [multigraphs](/multigraph/) and [self-loops](/self-loop/) appear where an algorithm needs them.
2. **Neighbours and degrees.** The [neighborhood](/neighborhood/) of a vertex, its [degree](/degree/), and the [handshake lemma](/handshake-lemma/) $\sum_v d(v) = 2m$, which gives the size of every adjacency list.
3. **Parts and kinds of graphs.** [Subgraphs](/subgraph/) and [induced subgraphs](/induced-subgraph/), [complete](/complete-graph/), [dense](/dense-graph/) and [sparse](/sparse-graph/) graphs, [acyclic graphs](/acyclic-graph/), [trees](/tree/) and [bipartite graphs](/bipartite-graph/).
4. **Three ways to store a graph.** The [adjacency matrix](/adjacency-matrix/), the [adjacency list](/adjacency-list/) and the [edge list](/edge-list/), with the [incidence matrix](/incidence-matrix/) and the [symbol graph](/symbol-graph/) for vertices with names.
5. **Basic questions on a stored graph.** The [adjacency query](/adjacency-query/), [neighbourhood enumeration](/neighborhood-enumeration/), [transposition](/transpose-graph/), the [universal sink](/universal-sink/) and the [square of a graph](/graph-square/), each priced on each representation.
6. **Storing trees.** The [parent-pointer tree](/parent-pointer-tree/), the [left-child right-sibling](/left-child-right-sibling/) form and the [Prüfer sequence](/prufer-sequence/).
7. **Representations for special needs.** Bit-packed matrices, hash sets, incidence lists, and the packed static forms: [compressed sparse row](/compressed-sparse-row/), its column twin and the [forward star](/forward-star/).
8. **Graphs built from other objects.** [Line graphs](/line-graph/), [hypergraphs](/hypergraph/), [functional graphs](/functional-graph/), [implicit graphs](/implicit-graph/) and the [Laplacian matrix](/laplacian-matrix/).
9. **Graphs in few bits.** [Graph compression](/graph-compression/), [succinct representations](/succinct-graph-representation/) and the [WebGraph](/webgraph-compression/) method.

## A first reading

For a first reading, take these entries in order: [graph](/graph/), [directed and undirected graphs](/directed-and-undirected-graphs/), [simple graph](/simple-graph/), [degree](/degree/), [handshake lemma](/handshake-lemma/), [subgraph](/subgraph/), [tree](/tree/), [bipartite graph](/bipartite-graph/), [adjacency matrix](/adjacency-matrix/), [adjacency list](/adjacency-list/), [edge list](/edge-list/), [adjacency query](/adjacency-query/), [graph transposition](/transpose-graph/) and [compressed sparse row](/compressed-sparse-row/). Most of the short definitions of the first three groups can be read when a later page links to them. The groups on special representations, on graphs built from other objects and on compression can wait until a problem calls for them; the last group is research material.

Several entries overlap. The [handshake lemma](/handshake-lemma/) and the [handshaking lemma](/handshaking-lemma/) are the degree sum formula and its parity corollary, and [graph transposition](/transpose-graph/) is the algorithmic side of the [graph transpose](/graph-transpose/) defined in Chapter 7.5. Read the first of each pair and skim the second.

## Before you start

You need [asymptotic notation](/asymptotic-notation/) and the [word RAM](/word-ram/) from Volume 1, since the costs here are counted in words and word operations. From Volume 3 you need the [dynamic array](/dynamic-array/), the [linked list](/linked-list/) and the [hash table](/hash-table/); the bitset and succinct forms also use [bit vectors](/bit-vector/). From Volume 4 you need [counting sort](/counting-sort/), and from Volume 6 [prefix sums](/prefix-sums/), which together build the packed forms in linear time. The [Laplacian matrix](/laplacian-matrix/) assumes [eigenvalues](/eigenvalue/) from Volume 12. No graph theory is assumed.

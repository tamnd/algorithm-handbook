## History

The oldest traversal in this chapter is a rule for mazes. Charles Pierre Trémaux, a French engineer of the nineteenth century, marked each corridor of a maze on entering and on leaving it, and never walked a corridor with two marks. Édouard Lucas published the rule in the first volume of his *Récréations mathématiques* in 1882, and Gaston Tarry gave a second rule in 1895. Shimon Even's book *Graph Algorithms* later presented Trémaux's walk as the first form of [depth-first search](/depth-first-search/).

Breadth-first search entered computing as a maze method too. Edward F. Moore described it in 1959 to find a shortest path through a maze, and C. Y. Lee found it again in 1961 to route wires on circuit boards. Arthur Kahn's 1962 paper on the topological sorting of large networks gave the method of removing vertices with no predecessors, which Knuth later presented as Algorithm T in the first volume of *The Art of Computer Programming*.

The decisive step was Robert Tarjan's 1972 paper "Depth-first search and linear graph algorithms". It showed that the tree, the timestamps and the classes of edges of a depth-first search on adjacency lists give linear-time algorithms for strong components and biconnected components, and, with John Hopcroft, for planarity. The names "parenthesis theorem" and "white-path theorem" come later, from the textbook of Cormen, Leiserson, Rivest and Stein.

Special search orders followed from sparse matrix computation. Donald Rose, Robert Tarjan and George Lueker introduced [lexicographic BFS](/lexicographic-bfs/) in 1976, to find elimination orderings that create no fill-in, which exist exactly for chordal graphs. Tarjan and Mihalis Yannakakis replaced it in 1984 by the simpler [maximum cardinality search](/maximum-cardinality-search/), and Michel Habib, Ross McConnell, Christophe Paul and Laurent Viennot recast LexBFS in 2000 as partition refinement. On trees, Joseph Morris showed in 1979 how to walk a binary tree in order with no stack, by threading it for a while.

Two later lines changed the questions. The online [exploration](/graph-exploration/) of an unknown graph, by an agent that sees only where it stands, was studied by Xiaotie Deng and Christos Papadimitriou, by Susanne Albers and Monika Henzinger, and by Petrişor Panaite and Andrzej Pelc in the late 1990s. And the space needed for reachability became a question of complexity theory: Omer Reingold proved in 2008 that undirected reachability can be decided in logarithmic space.

## Further reading

- Thomas H. Cormen, Charles E. Leiserson, Ronald L. Rivest and Clifford Stein, *Introduction to Algorithms*, fourth edition (2022). Chapter 20 proves the properties of breadth-first and depth-first search with the timestamps and colours used in this chapter.
- Jeff Erickson, *Algorithms* (2019). The chapters on graph search present whatever-first search and derive both basic searches from it, with many exercises.
- Sanjoy Dasgupta, Christos Papadimitriou and Umesh Vazirani, *Algorithms* (2008). A short and clear account of depth-first search with pre and post numbers, and of topological order.
- Shimon Even, *Graph Algorithms*, second edition, edited by Guy Even (2012). Starts depth-first search from Trémaux's maze rule and proves its properties with care.
- Martin Charles Golumbic, *Algorithmic Graph Theory and Perfect Graphs*, second edition (2004). The standard account of chordal graphs and of lexicographic BFS.

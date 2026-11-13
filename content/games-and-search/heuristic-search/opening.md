The 15-puzzle has about $10^{13}$ positions that can reach the goal, and an optimal solution of a random instance takes about 53 moves. [Breadth-first search](/breadth-first-search/) cannot store a level of that search, and [Dijkstra's algorithm](/dijkstra/) is no better, because it knows nothing about where the goal lies. A program that counts, for each tile, how many rows and columns it is away from its square knows a lot: the sum never exceeds the number of moves left. With that number as a guide, and a search whose memory grows only with the depth of the path, Korf solved random instances of the 15-puzzle optimally in 1985. Heuristic search is the study of such guides and of the searches that use them: what they guarantee, how much work they save, and what to do when memory, time or the map runs short.

Every guarantee in this chapter names its conditions, and the pages keep them apart. A heuristic $h$ is [admissible](/admissible-heuristic/) if it never overestimates the cost to a goal, [consistent](/consistent-heuristic/) if it also never drops by more than the cost of an action, or neither. [A*](/a-star-search/) as a tree search is optimal with an admissible $h$; as a graph search that never reopens a closed state, it needs a consistent one. Both results also need finite branching and action costs bounded below by a positive constant, or a finite graph. The work is counted in states expanded, not in time, and the measured counts on the pages hold for their instances only.

## What the chapter covers

1. **State spaces and heuristics.** The [state space](/state-space/) as an implicit graph, [state-space search](/state-space-search/), the [heuristic function](/heuristic-function/), and the two conditions, admissible and consistent, that the rest of the chapter depends on.
2. **A* and its theory.** The [open list](/open-list/), A*, [duplicate detection](/duplicate-detection/), the conditions of [A* optimality](/a-star-optimality/), the [optimal efficiency](/optimal-efficiency-of-a-star/) of A* in the sense of Dechter and Pearl, [heuristic dominance](/heuristic-dominance/), the [effective branching factor](/effective-branching-factor/) and [pathmax](/pathmax/).
3. **Building heuristics.** [Relaxation](/relaxation-heuristic/), which gives the misplaced tiles, the Manhattan distance and Gaschnig's heuristic, and [pattern databases](/pattern-database/), with the rule for when two tables may be added.
4. **Memory-bounded search.** The [overview](/memory-bounded-heuristic-search/), [IDA*](/iterative-deepening-a-star/), [RBFS](/recursive-best-first-search/), [SMA*](/simplified-memory-bounded-a-star/), [fringe search](/fringe-search/) and [partial expansion A*](/partial-expansion-a-star/).
5. **Suboptimal and anytime search.** [Greedy best-first search](/greedy-best-first-search/), [weighted A*](/weighted-a-star/) and its bound $w C^*$, [ARA*](/anytime-repairing-a-star/), [beam search](/beam-search/), [beam-stack search](/beam-stack-search/) and [limited discrepancy search](/limited-discrepancy-search/).
6. **Bidirectional and grid pathfinding.** [Bidirectional heuristic search](/bidirectional-heuristic-search/) by MM, [jump point search](/jump-point-search/), [HPA*](/hierarchical-pathfinding-a-star/) and [Theta*](/theta-star/).
7. **Incremental and real-time search.** [LPA*](/lifelong-planning-a-star/), [D*](/d-star/), [D* Lite](/d-star-lite/), [RTA*](/real-time-a-star/) and [LRTA*](/learning-real-time-a-star/).
8. **Multi-agent pathfinding.** The [problem](/multi-agent-pathfinding/) and [conflict-based search](/conflict-based-search/).

The kinds of result differ from group to group. A*, IDA*, RBFS, fringe search, partial expansion A*, MM and conflict-based search are optimal under stated conditions. Weighted A* and ARA* are bounded: the cost is at most a known factor times $C^*$. Greedy search, beam search and limited discrepancy search have no bound on the cost. Jump point search is optimal only on 8-connected grids with uniform costs; HPA* and Theta* return valid paths that need not be shortest. LPA*, D* and D* Lite are exact on the current map, and their savings over search from scratch are measured, not proved. RTA* reaches the goal under stated conditions with no bound on the walk, and LRTA* converges to optimal walks only over repeated trials.

## A first reading

Read these in order:

1. [State space](/state-space/)
2. [Heuristic function](/heuristic-function/)
3. [Admissible heuristic](/admissible-heuristic/) and [consistent heuristic](/consistent-heuristic/)
4. [A* search](/a-star-search/)
5. [A* optimality](/a-star-optimality/)
6. [Heuristic dominance](/heuristic-dominance/)
7. [Effective branching factor](/effective-branching-factor/)
8. [Relaxation heuristic](/relaxation-heuristic/)
9. [Pattern database](/pattern-database/)
10. [Iterative deepening A*](/iterative-deepening-a-star/)
11. [Weighted A*](/weighted-a-star/)
12. [Greedy best-first search](/greedy-best-first-search/)
13. [D* Lite](/d-star-lite/)
14. [Jump point search](/jump-point-search/)
15. [Conflict-based search](/conflict-based-search/)

Skip at first the optimal efficiency theorem, pathmax, SMA*, fringe search, partial expansion, beam-stack search, D* and the bidirectional search. They refine the core and are easier after it.

## Before you start

The chapter assumes the graph searches of the graphs volume: breadth-first search, [depth-first search](/depth-first-search/) and Dijkstra's algorithm, which is A* with $h = 0$. The techniques volume gives the general frame: [best-first search](/best-first-search/), [uniform-cost search](/uniform-cost-search/), [iterative deepening search](/iterative-deepening-search/), [bidirectional search](/bidirectional-search/) and the difference between [graph search and tree search](/graph-search-vs-tree-search/). The open list is a [priority queue](/priority-queue/), usually a [binary heap](/binary-heap/), together with a [hash table](/hash-table/) for the closed states, from the data structures volume. The [sliding tile puzzle](/sliding-tile-puzzle/) of the puzzles chapter is the running example of many pages, and Dijkstra's algorithm is the point of comparison for the incremental methods.

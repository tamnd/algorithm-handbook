## What to remember

- A heuristic is [admissible](/admissible-heuristic/) if $h \le h^*$, and [consistent](/consistent-heuristic/) if $h(u) \le c(u, v) + h(v)$ for every action and $h = 0$ at goals. Consistent implies admissible, not the converse. The exact cost of a [relaxed problem](/relaxation-heuristic/) is consistent, and so is the maximum of consistent heuristics.
- With finite branching and a finite graph or costs at least $\delta > 0$, [A*](/a-star-search/) is optimal as a tree search with an admissible $h$, as a graph search with an admissible $h$ and reopening, and as a graph search without reopening with a consistent $h$, which then expands each state at most once.
- With a consistent $h$, A* expands every state with $g^* + h < C^*$ and none with $g^* + h > C^*$. By [Dechter and Pearl](/optimal-efficiency-of-a-star/), every deterministic algorithm that sees only the start, the successors, the goal test and $h$, and is optimal on all instances with a consistent $h$, must expand every state with $g^* + h < C^*$ too.
- A larger consistent heuristic expands fewer states: with strict [dominance](/heuristic-dominance/) a subset, and otherwise the sets differ only on the contour $f = C^*$. The [effective branching factor](/effective-branching-factor/) $b^*$ solves $\sum_{i=1}^{d} b^i = N$.
- Disjoint [pattern databases](/pattern-database/) that count only the moves of their own tiles can be added; tables that count every move can only be combined by the maximum.
- [IDA*](/iterative-deepening-a-star/) and [RBFS](/recursive-best-first-search/) are optimal with an admissible $h$ in space linear in the depth, and they repeat work.
- [Weighted A*](/weighted-a-star/) costs at most $w C^*$, with an admissible $h$ and reopening or a consistent $h$ without. [ARA*](/anytime-repairing-a-star/) proves a bound $\varepsilon'$ after each call. [Greedy search](/greedy-best-first-search/), [beam search](/beam-search/) and [limited discrepancy search](/limited-discrepancy-search/) have no bound.
- [LPA*](/lifelong-planning-a-star/) and [D* Lite](/d-star-lite/) are exact on the current map after each call; their gain over search from scratch is measured, not proved. [LRTA*](/learning-real-time-a-star/) converges to optimal walks only over repeated trials.
- [Conflict-based search](/conflict-based-search/) is optimal for the sum of costs of [multi-agent pathfinding](/multi-agent-pathfinding/), which is NP-hard to solve optimally.

| Method | Heuristic | Guarantee | Memory |
|---|---|---|---|
| A*, no reopening | consistent | optimal | all states |
| IDA*, RBFS | admissible | optimal | linear |
| SMA* | admissible | optimal if an optimal path has $\le M - 1$ actions | $M$ nodes |
| Weighted A* | see above | cost $\le w C^*$ | all states |
| ARA* | consistent | $\le \varepsilon' C^*$ per call, optimal at the end | all states |
| Greedy, beam | any | none | all states, $k$ per layer |
| MM | admissible, both ways | optimal | both frontiers |
| JPS | octile | optimal on uniform 8-connected grids | all states |
| HPA* | Manhattan | $\le C^* + 2 \cdot \mathrm{gap} \cdot X$ | abstract graph |
| Theta* | Euclidean | no longer than the grid path | all corners |
| D* Lite | consistent | exact on the known map | all values |
| LRTA* | admissible | an optimal trial after finitely many trials | visited states |
| CBS | consistent | optimal sum of costs if solvable | constraint tree |

: The main methods. "Optimal" assumes finite branching and a finite graph or costs at least $\delta > 0$. $M$ is the memory of SMA*, $k$ the beam width, $X$ the number of border crossings of a shortest path.

## Choosing a method

If memory holds the reachable states and $h$ is consistent, use A* with duplicate detection and no reopening. If $h$ is only admissible, keep the reopening or use IDA*. On puzzles with few duplicates and a strong heuristic, IDA* with a pattern database is the standard choice; on graphs with many short cycles it repeats too much.

If an optimal path costs too much, choose by the promise you need: a factor $w$ from weighted A*, a path soon and a tighter bound later from ARA*, or no promise from greedy or beam search. On uniform grids JPS is optimal and faster than A*; HPA* is faster on large maps after preprocessing; Theta* gives any-angle paths. A robot in unknown terrain uses D* Lite, an agent with a time limit per move RTA* or LRTA*, and a team of agents CBS.

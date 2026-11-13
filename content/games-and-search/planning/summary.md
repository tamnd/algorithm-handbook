## What to remember

- A [STRIPS](/strips/) action maps a state $s$ to $(s \setminus \mathit{del}) \cup \mathit{add}$. For propositional STRIPS, deciding whether a plan exists is [PSPACE-complete](/strips-plan-existence-pspace-complete/), and some tasks need $2^n - 1$ actions. Deciding whether a plan of at most $k$ actions exists is [NP-complete](/bounded-plan-existence-np-complete/) when $k$ is written in unary, and PSPACE-complete when $k$ is in binary.
- [Forward search](/forward-state-space-search/) visits reachable states; [backward search](/backward-state-space-search/) visits goal descriptions made by [goal regression](/goal-regression/), some of which match no reachable state. Breadth-first search either way is complete and optimal in the number of actions.
- The [delete relaxation](/delete-relaxation/) gives $h^{\max} \le h^{+} \le h^{\mathrm{add}}$ and $h^{+} \le h^{\mathrm{FF}}$. [h-max](/h-max-heuristic/) and $h^{+}$ are admissible and consistent, but $h^{+}$ is NP-hard to compute; [h-add](/h-add-heuristic/), the [relaxed plan heuristic](/relaxed-plan-heuristic/), the [landmark](/landmark-heuristic/) count and the [causal graph heuristic](/causal-graph-heuristic/) are not admissible. A cost partition over landmarks is admissible.
- [FF](/fast-forward-planner/) runs [enforced hill climbing](/enforced-hill-climbing/) with helpful actions and, if that fails, a complete greedy best-first search, so it finds a plan exactly when one exists, but not a shortest one.
- [Graphplan](/graphplan/) is optimal in the number of parallel steps, not of actions, and it reports that no plan exists only when none does. [Mutexes](/mutex-relation/) are sound but not complete. [SATPLAN](/satplan/) is step-optimal in the same sense with a complete SAT solver.
- [Partial-order planning](/pop-partial-order-planning/) searches plans, not states, and repairs open preconditions and threats to [causal links](/causal-link/); POP, [SNLP](/snlp/) and [UCPOP](/ucpop/) are sound and complete for their action languages. [HTN planning](/htn-planning/) with partial order and recursion is undecidable. Temporal plan existence with integer time is EXPSPACE-complete.
- An [SSP](/stochastic-shortest-path/) in which a proper policy exists and every improper policy has infinite cost from some state has a unique solution of the [Bellman equation](/bellman-equation/), and value iteration converges to it from any start. [RTDP](/real-time-dynamic-programming/) from an admissible start converges on the relevant states only. [Conformant](/conformant-planning/) plan existence is EXPSPACE-complete, [contingent](/contingent-planning/) plan existence with partial observation 2-EXPTIME-complete, and [POMDP planning](/pomdp-planning/) PSPACE-complete for a polynomial horizon.
- The generalized movers' problem is PSPACE-hard; exact [cell decomposition](/cell-decomposition/) is complete but practical only in low dimension. [Potential fields](/potential-field-method/) can stop at a local minimum.
- The [PRM](/probabilistic-roadmap/), the [RRT](/rapidly-exploring-random-tree/) and [RRT-Connect](/rrt-connect/) are probabilistically complete: for a path with positive clearance the chance of failure falls exponentially in the number of samples. None of them is asymptotically optimal. [RRT*](/rrt-star/) is asymptotically optimal with probability one; the [proof](/rrt-star-asymptotic-optimality/) that stands uses the radius $\gamma(\log n/n)^{1/(d+1)}$.

| Method | Searches | Guidance | Complete | Optimal for |
|---|---|---|---|---|
| BFS or uniform-cost search | states | none | yes | actions, or cost |
| A* with h-max or LM-cut | states | admissible $h$ | yes | cost |
| [HSP](/hsp-planner/) | states, weighted A* | h-add | yes | none |
| FF | states, EHC then greedy search | $h^{\mathrm{FF}}$, helpful actions | yes, by the fallback | none |
| Graphplan | planning graph, backward | mutexes, memos | yes | parallel steps |
| SATPLAN | horizons $k = 0, 1, \dots$ | SAT solver | up to the largest horizon tried | parallel steps |
| POP, SNLP, UCPOP | partial plans | flaw selection | yes | none |
| HTN decomposition | task networks | methods | up to a depth bound | none |
| Value iteration, RTDP | values of states | Bellman backups | converges under the SSP assumptions | expected cost |
| PRM, RRT, RRT-Connect | random samples | nearest neighbors | probabilistically | none |
| RRT* | random samples | rewiring in a shrinking radius | probabilistically | cost, asymptotically, with probability one |

: The main planners. "Complete" means that the method finds a plan whenever one exists; optimality is for the measure named. HTN completeness is for decompositions up to the bound, and SATPLAN decides plan existence only with a horizon of $2^n - 1$.

## Choosing a method

For a classical task where any plan will do, use FF, or greedy best-first search with $h^{\mathrm{FF}}$ and landmarks, as in LAMA. For a cheapest plan, run A* with an admissible heuristic such as LM-cut. When the plan should be short in parallel steps, use Graphplan or a SAT encoding. Use HTN methods when experts know how tasks break down.

When actions have random outcomes and the state is observed, solve an SSP by value iteration on small models or by RTDP from an admissible heuristic on large ones. With partial observations, plan in the belief space, for instance with PBVI, whose values are lower bounds. In continuous space with few dimensions, decompose the free space; in many dimensions, use the PRM for many queries, RRT-Connect for one query, and RRT* when the cost of the path matters.

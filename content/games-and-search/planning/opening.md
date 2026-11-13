A planner is given a model of a world and a goal, and it must find the actions that reach the goal. A robot must restack crates so that the one wanted is on top; trucks must carry parcels to their towns; an arm with seven joints must reach into a shelf without touching it. The first two are planning over facts, where an action changes a few of them. The last is motion planning: the world is a continuous space, and the plan is a path through it.

The core model is [classical planning](/classical-planning/) in the [STRIPS](/strips/) representation. A state is a set of true facts, an action has a precondition, an add list and a delete list, and applying action $a$ to state $s$ gives $(s \setminus \mathit{del}(a)) \cup \mathit{add}(a)$. A plan is a path from the initial state to a goal state in a graph with up to $2^{|F|}$ states, where $|F|$ is the number of facts. The description is small and the graph is huge. Deciding whether a propositional STRIPS task has a plan at all is [PSPACE-complete](/strips-plan-existence-pspace-complete/), and some tasks need plans of $2^n - 1$ actions. Asking for a plan of at most $k$ actions, with $k$ written in unary, is [NP-complete](/bounded-plan-existence-np-complete/). The methods differ in what they search and how they guide the search.

The entries keep several kinds of guarantee apart. A planner is sound when every plan it returns is a plan, complete when it finds a plan whenever one exists, and optimal when the plan it returns is cheapest, and optimality is always for a stated cost: the number of actions, the sum of action costs, or the number of parallel steps. A heuristic is admissible when it never overestimates the cost to the goal: [h-max](/h-max-heuristic/) is, while [h-add](/h-add-heuristic/) and the [relaxed plan heuristic](/relaxed-plan-heuristic/) of FF are not and serve planners that do not promise optimal plans. Under uncertainty the cost becomes an expected cost, and a plan becomes a policy. In continuous space the sampling planners are only probabilistically complete: the chance that they miss a path, when one exists with some clearance, goes to zero as they draw more samples. [RRT*](/rrt-star/) is asymptotically optimal with probability one: the cost of its best path tends to the optimum as the samples grow, and nothing is promised after a fixed number of them.

## What the chapter covers

The chapter is in ten groups, read in order.

1. **Planning tasks.** Classical planning, the [closed-world assumption](/closed-world-assumption/), STRIPS and the [blocks world](/blocks-world/), and the three problems of describing actions in logic: the [frame](/frame-problem/), [qualification](/qualification-problem/) and [ramification](/ramification-problem/) problems.
2. **Languages and grounding.** [Action schemas](/action-schema/), [grounding](/grounding/), [PDDL](/pddl/), [conditional effects](/conditional-effects/), the finite-domain [SAS+](/sas-plus/) representation and the [International Planning Competition](/international-planning-competition/).
3. **Searching the state space.** [Forward search](/forward-state-space-search/), [goal regression](/goal-regression/) and [backward search](/backward-state-space-search/), [means-ends analysis](/means-ends-analysis/), the [Sussman anomaly](/sussman-anomaly/) and [macro-operators](/macro-operators/).
4. **How hard planning is.** The two complexity theorems and [optimal planning](/optimal-planning/).
5. **Planning graphs and SAT.** The [planning graph](/planning-graph/), [mutex relations](/mutex-relation/), [Graphplan](/graphplan/) and [SATPLAN](/satplan/).
6. **Heuristics from relaxations.** The [delete relaxation](/delete-relaxation/), h-max and h-add, the [HSP planner](/hsp-planner/), the [relaxed planning graph](/relaxed-planning-graph/), [enforced hill climbing](/enforced-hill-climbing/) and the [FF planner](/fast-forward-planner/), and the [landmark](/landmark-heuristic/) and [causal graph](/causal-graph-heuristic/) heuristics.
7. **Plan-space planning.** [Partial-order plans](/partial-order-plan/), [causal links](/causal-link/) and threats, [POP](/pop-partial-order-planning/), [SNLP](/snlp/), [TWEAK](/tweak/) and [UCPOP](/ucpop/).
8. **Hierarchies and time.** [Task networks](/task-network/), [HTN planning](/htn-planning/) and its [decomposition planner](/htn-decomposition/), and [temporal planning](/temporal-planning/).
9. **Execution and uncertainty.** [Execution monitoring](/execution-monitoring/) and [replanning](/replanning/); nondeterministic plans by [model checking](/planning-as-model-checking/); the [Bellman equation](/bellman-equation/), [stochastic shortest paths](/stochastic-shortest-path/) and [RTDP](/real-time-dynamic-programming/); the [belief space](/belief-space/), [conformant](/conformant-planning/) and [contingent](/contingent-planning/) planning, [POMDP planning](/pomdp-planning/) and [point-based value iteration](/point-based-value-iteration/); and [plan recognition](/plan-recognition/).
10. **Motion planning.** [Configuration space](/configuration-space/), the [motion planning problem](/motion-planning/) and the [piano movers problem](/piano-movers-problem/), [cell decomposition](/cell-decomposition/), [potential fields](/potential-field-method/), [bug algorithms](/bug-algorithms/), the [probabilistic roadmap](/probabilistic-roadmap/), the [RRT](/rapidly-exploring-random-tree/), [RRT-Connect](/rrt-connect/), RRT* and [kinodynamic planning](/kinodynamic-planning/).

## A first reading

Read these in order:

1. [Classical planning](/classical-planning/)
2. [STRIPS representation](/strips/)
3. [Blocks world](/blocks-world/)
4. [PDDL](/pddl/)
5. [Forward state-space search](/forward-state-space-search/)
6. [Goal regression](/goal-regression/)
7. [Sussman anomaly](/sussman-anomaly/)
8. [Delete relaxation](/delete-relaxation/)
9. [h-max heuristic](/h-max-heuristic/)
10. [FF planner](/fast-forward-planner/)
11. [Graphplan](/graphplan/)
12. [Partial-order plan](/partial-order-plan/)
13. [Stochastic shortest path problem](/stochastic-shortest-path/)
14. [Configuration space](/configuration-space/)
15. [Rapidly-exploring random tree](/rapidly-exploring-random-tree/)

Skip at first the two complexity proofs, SAS+ and the causal graph heuristic, TWEAK and UCPOP, the HTN complexity results, POMDPs and point-based value iteration, the proof of the asymptotic optimality of RRT*, and kinodynamic planning. They are easier once the core is in place.

## Before you start

Planning is search, and the chapter uses the previous chapter, on heuristic search, throughout: the [state space](/state-space/), [state-space search](/state-space-search/), [heuristic functions](/heuristic-function/), [admissible](/admissible-heuristic/) and [consistent](/consistent-heuristic/) heuristics, [A*](/a-star-search/), [weighted A*](/weighted-a-star/) and [greedy best-first search](/greedy-best-first-search/). From Volume 7 it needs [breadth-first search](/breadth-first-search/), [Dijkstra's algorithm](/dijkstra/), [shortest paths](/shortest-path/) and [topological sort](/topological-sort/). From Volume 16 it needs [SAT](/sat/) solvers for SATPLAN, the [simple temporal problem](/simple-temporal-problem/) for temporal planning, and [CTL model checking](/ctl-model-checking/) and [binary decision diagrams](/binary-decision-diagram/) for planning as model checking. The planning under uncertainty builds on the [Markov decision process](/markov-decision-process/), [value iteration](/value-iteration/) and the [POMDP](/pomdp/) of Volume 25, which is the source for MDPs and reinforcement learning, and on the [principle of optimality](/principle-of-optimality/) of Volume 2. Motion planning uses the [Minkowski sum](/minkowski-sum/) and the [trapezoidal map](/trapezoidal-map/) of Volume 13, [nearest-neighbor search](/nearest-neighbor-search/), and [random geometric graphs](/random-geometric-graph/) for the theory of RRT*. The complexity results assume the classes P, NP and PSPACE and polynomial-time reductions.

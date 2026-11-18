## What to remember

- The team is a graph. Most distributed laws in the chapter use only the neighbors of each robot, and their guarantees are conditions on this graph, which changes as the robots move.
- Consensus $\dot x = -Lx$ keeps the sum $\mathbf 1^\top x$ on an undirected graph and reaches the average when the graph is connected, with $\lVert e(t)\rVert \le e^{-\lambda_2 t}\lVert e(0)\rVert$. The sampled form needs $0 < \varepsilon < 1/\Delta$. On switching graphs, agreement needs the union over bounded intervals to be connected.
- Rendezvous laws move each robot into the convex hull of the robots it sees, so the diameter never grows. Ando's rule also keeps every link it starts with, which is what makes the limited range safe.
- Distance-based formations need a rigid target, with at least $2r - 3$ edges in the plane. The gradient law $\dot p = -R(p)^\top e$ converges only near an infinitesimally rigid target, and it has wrong equilibria such as collinear ones.
- Coverage cost $H = \sum_i \int_{V_i} \lVert q - p_i\rVert^2 \phi(q)\,dq$ has the gradient $2M_i(p_i - C_i)$. Moving to the centroids never raises $H$ and reaches a centroidal Voronoi configuration, which can be a saddle or a local minimum.
- The assignment class ST-SR-IA is solved exactly by the Hungarian algorithm. Greedy on utilities gets at least half the optimum, greedy on costs has no constant bound, and CBBA matches sequential greedy under diminishing marginal gain.
- Coupled planning in the joint space is complete but exponential in $r$. Prioritized planning is sound and fast but incomplete for every order.
- ORCA is collision-free for the next $\tau$ seconds when every linear program is feasible and every robot senses its possible partners. It has no liveness guarantee, and symmetric scenes can deadlock.

## The main algorithms side by side

| Method | Information per robot | Guarantee | Cost per step or round |
|---|---|---|---|
| [Laplacian consensus](/laplacian-consensus-protocol/) | values of neighbors | average, rate $e^{-\lambda_2 t}$, if connected and undirected | $O(r + m)$ |
| [Ando's circumcenter](/ando-circumcenter-algorithm/) | relative positions within $V$ | links kept; one point in the limit | $O(r + m)$ expected |
| [Distance-based formation](/distance-based-formation-control/) | relative positions, local frames | local, near a rigid target | $O(r + m)$ |
| [Distributed Lloyd](/cortes-coverage-algorithm/) | Voronoi neighbors | $H$ nonincreasing; critical point | $O(r(n + r))$ per robot |
| [Contract net](/contract-net-protocol/) | own costs | none on the total cost | $O(rt)$ messages |
| [CBBA](/consensus-based-bundle-algorithm/) | winning bids of neighbors | conflict-free, at least $1/2$, under DMG | $O(rLt + m(t + r))$ |
| [Prioritized planning](/prioritized-multi-robot-planning/) | paths of higher priority | sound, incomplete | $O(gH \log(gH))$ per robot |
| [ORCA](/optimal-reciprocal-collision-avoidance/) | positions and velocities of neighbors | no collision when feasible | $O(k)$ expected |

: Distributed laws and planners of the chapter. Here $r$ is the number of robots, $m$ the number of edges, $n$ the number of vertices of the region, $t$ the number of tasks, $L$ the bundle size, $g$ the number of grid cells, $H$ the time horizon and $k$ the number of sensed neighbors.

## Choosing a method

- To agree on a value or to meet on a fixed graph, use consensus. With a limited sensing range and no identifiers, use Ando's rule, and keep the links with [connectivity maintenance](/connectivity-maintenance/) if the task law could break them.
- For a formation with a common compass, displacement consensus converges from every start. Without one, use distances on a rigid graph and start near the target shape. Leader-follower pairs suit unicycles that drive in a column.
- To spread sensors over an area, run Lloyd steps. Try several starts if the cost matters, since the limit depends on the start.
- For a few robots and tasks with one computer, solve the assignment exactly with the Hungarian algorithm. With many robots and poor links, use auctions or CBBA, and check the bound that the entry states for the class.
- For a few robots on a graph that must not fail, plan in the joint space or with [conflict-based search](/conflict-based-search/). For many robots and loose spaces, plan by priority and be ready to change the order.
- For crowds that move continuously, use ORCA each step, and expect deadlocks in symmetric scenes. A small random change of the preferred velocity broke them in the measurements of the entry, but this is not a guarantee.

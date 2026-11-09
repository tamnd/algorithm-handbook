## What to remember

- **A strategy is the order of the frontier.** A first-in first-out queue gives breadth-first search, a stack gives depth-first search, and a priority queue on $f$ gives best-first search: $f = g$ is uniform-cost search, $f = h$ greedy search and $f = g + h$ A*.
- **The search tree is larger than the space.** A tree of branching factor $b$ has $(b^{d+1} - 1)/(b - 1)$ nodes down to depth $d$, while a grid has only $O(d^2)$ cells within distance $d$, and a cycle makes the tree infinite. Graph search keeps a hash table of reached states and expands each one once.
- **Completeness and optimality need conditions.** Breadth-first search is complete when $b$ is finite, and returns a cheapest path only when all actions cost the same. Uniform-cost search is complete and optimal when every action costs at least some $\varepsilon > 0$. Depth-first search can run forever on an infinite branch. No strategy can detect, on every problem given by programs, that no goal exists.
- **Iterative deepening gets both.** It runs depth-limited search with limits $0, 1, 2, \ldots$, uses $O(bd)$ memory, finds a shallowest goal, and generates fewer than $b/(b-1)$ times the nodes of one search to depth $d$. Depth-limited search must report *cutoff* apart from *failure*, or the loop cannot stop when no goal exists.
- **Test for the goal when a node is selected, not when it is made**, in any search ordered by cost. Uniform-cost search then expands nodes in order of $g$, and returns a cheapest path after $O(b^{1 + \lfloor C^*/\varepsilon \rfloor})$ nodes.
- **A heuristic changes the order, not the method.** A* with an admissible $h$ returns a cheapest path; with a consistent $h$ graph search never has to reopen a state. Greedy search can return an expensive path.
- **Two half searches beat one full search.** Bidirectional breadth-first search meets in the middle after about $2b^{d/2}$ nodes instead of $b^d$, if each side expands a complete layer before the meeting test.
- **Not all search is systematic.** A local search problem asks for a state that no neighbor improves; weighted Max-Cut with single flips is complete for the class PLS of such problems. Simulation steps a process forward and, once a state repeats after $\mu + \lambda$ steps, jumps over whole cycles of length $\lambda$.

## The strategies side by side

| Strategy | Complete | Cheapest path | Time | Space |
|---|---|---|---|---|
| [Breadth-first search](/breadth-first-search/) | if $b$ is finite | unit costs | $O(b^d)$ | $O(b^d)$ |
| [Depth-first search](/depth-first-search/), tree-like | finite trees only | no | $O(b^m)$ | $O(bm)$ |
| [Depth-limited search](/depth-limited-search/) | if $d \le \ell$ | no | $O(b^\ell)$ | $O(b\ell)$ |
| [Iterative deepening](/iterative-deepening-search/) | if $b$ is finite | unit costs | $O(b^d)$ | $O(bd)$ |
| [Iterative broadening](/iterative-broadening/) | finite trees | no | $O((1 + b/d)\, b^d)$ | $O(d)$ |
| [Uniform-cost search](/uniform-cost-search/) | if costs $\ge \varepsilon > 0$ | yes | $O(b^{1 + \lfloor C^*/\varepsilon \rfloor})$ nodes | $O(b^{1 + \lfloor C^*/\varepsilon \rfloor})$ |
| [Best-first search](/best-first-search/) | depends on $f$ | depends on $f$ | $O(N \log N)$ | $O(N + V)$ |
| [Bidirectional search](/bidirectional-search/) | if $b$ is finite | unit costs | $O(b^{d/2})$ | $O(b^{d/2})$ |

: Here $b$ is the branching factor, $d$ the depth of a shallowest goal, $m$ the largest depth, $\ell$ the depth limit, $C^*$ the cost of a cheapest solution, $\varepsilon$ the least action cost, $N$ the number of nodes generated and $V$ the number of reachable states. The bounds are worst case and count nodes of the search tree; a priority queue adds a factor $\log$ of its size.

## Choosing a method

- If all actions cost the same, use breadth-first graph search, or iterative deepening when memory is short.
- If actions have different costs, use uniform-cost search, or A* when you have an admissible heuristic. Test for the goal when a node is taken from the frontier.
- Use graph search whenever the space has cycles or many paths to the same state and the reached states fit in memory. Otherwise use tree search with a check on the current path.
- When the goal is one known state and the actions can be reversed, search from both ends.
- When the first choices at each node are likely to be right and any goal will do, try iterative broadening.
- When you need a good state, not a path, and a state that no move improves is good enough, use local search.
- When a problem describes a process, simulate it, and watch for a repeated state.

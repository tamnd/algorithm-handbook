## What to remember

- Some minimum [sum of products](/sum-of-products/) uses only [prime implicants](/prime-implicant/) (Quine). So exact [two-level minimization](/two-level-logic-minimization/) lists the primes and then solves a [set cover](/set-cover/) problem. The largest number of primes of an $n$-variable function lies between orders $3^n/n$ and $3^n/\sqrt{n}$, and the decision version is NP-complete from a truth table.
- A cube may cover [don't-care](/dont-care-condition/) points, but only on-set points must be covered. The full [observability don't-care](/observability-dont-care/) sets of two nodes cannot in general be used at the same time.
- [Espresso](/espresso/) repeats EXPAND, IRREDUNDANT and REDUCE, built on the [unate recursive paradigm](/unate-recursive-paradigm/). Its cover is prime and irredundant, not proved minimum.
- Algebraic synthesis treats a cover as a polynomial. Two expressions share a divisor of two or more cubes only if some of their [kernels](/algebraic-kernel/) share two cubes, so [kernel extraction](/kernel-extraction/) searches a kernel-cube matrix. Each step keeps every function and saves literals, with no optimality bound, and Boolean divisors such as $a + b$ in $a + bc$ are missed.
- [Tree covering](/tree-covering-technology-mapping/) is optimal for each tree of the given subject graph, not for the whole DAG, where copying logic can be cheaper.
- [FlowMap](/flowmap/) finds a $K$-LUT mapping of least depth in $O(Kmn)$ time for a $K$-bounded network of fixed structure. Finding the fewest LUTs is NP-hard. [Priority cuts](/priority-cuts/) keep $C$ cuts per node and are exact for depth only with $C$ unlimited.
- On an [and-inverter graph](/and-inverter-graph/), [balancing](/aig-balancing/) never raises depth or size, [rewriting](/aig-rewriting/) never raises size, and [SAT sweeping](/sat-sweeping/) merges only pairs proved equal. None reaches a proved optimum.
- [Retiming](/retiming/) finds the least clock period over all legal retimings in $O(V^3 \log V)$ time, and [minimum-area retiming](/minimum-area-retiming/) the fewest registers, as the dual of a min-cost flow. Both are exact.
- [ASAP and ALAP](/asap-alap-scheduling/) schedules give exact time frames in $O(V + E)$ time with no limit on units. Scheduling with a limit on units is NP-hard when the number of units is part of the input, and [force-directed scheduling](/force-directed-scheduling/) is a heuristic for it.

| Method | Task | Time | Guarantee |
|---|---|---|---|
| [Quine-McCluskey](/quine-mccluskey/) | exact two-level cover | $O(n^2 3^n)$ for the primes, then a covering search exponential in the worst case | exact |
| [Petrick's method](/petricks-method/) | prime implicant table | $O(m p^2 T^2)$, with $T \le 2^p$ | exact |
| Espresso | two-level cover | exponential in the worst case | primes, irredundant |
| Kernel extraction | shared divisors | $O(E P^4 K n)$ | keeps functions, saves literals each step |
| Tree covering | cell library mapping | $O(N L s 2^s)$ | least area among tree covers |
| FlowMap | $K$-LUT mapping | $O(Kmn)$ | least depth for the given structure |
| Priority cuts | LUT mapping | $O(NkC^4 + N^2C^2)$ | depth never grows in area passes |
| AIG balancing | lower depth | $O(N \log k)$ expected | depth and size never grow |
| AIG rewriting | lower size | $O(N^2 C^2)$ | size never grows, local optimum |
| SAT sweeping | merge equal nodes | $O(N^2(NW + T))$ | merges proved by SAT |
| Retiming | least clock period | $O(V^3 \log V)$ | exact |
| Minimum-area retiming | fewest registers | $O(EVM)$ | exact |
| ASAP and ALAP | time frames | $O(V + E)$ | exact, no unit limit |
| Force-directed scheduling | schedule within latency $L$ | $O(V^2 L (E + VL))$ | meets $L$, no bound on units |

: Worst-case bounds as given on the entries, whose variables differ from row to row. "Exact" means optimal for the stated model.

## Choosing a method

By hand, up to four variables, use a [Karnaugh map](/karnaugh-map/). For an exact cover of a small function, list the primes with Quine-McCluskey and solve the table with Petrick's method or branch and bound. For anything larger, run Espresso.

For networks of sums of products, use kernel extraction, then don't-cares on each node. In a modern flow, convert to an and-inverter graph and alternate rewriting and balancing, and use SAT sweeping to merge equal nodes or to check equivalence.

For a cell library, use tree covering, or cuts with [Boolean matching](/boolean-matching/) when the graph has much sharing. For an FPGA, FlowMap gives the least depth; for $K = 6$ and large designs, priority cuts are faster.

Retime for the clock period first, then for registers under that period. For [state assignment](/state-assignment/) and [ISFSM minimization](/incompletely-specified-fsm-minimization/), exact methods fit only small machines. For a data flow graph, compute the frames by ASAP and ALAP, then place operations with force-directed scheduling.

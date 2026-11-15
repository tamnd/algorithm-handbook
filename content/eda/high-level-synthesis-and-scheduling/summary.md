## What to remember

- [Resource-constrained scheduling](/resource-constrained-scheduling/) and [latency-constrained scheduling](/latency-constrained-scheduling/) are NP-hard. The latency is at least $\max(\mathrm{CP}, \lceil W_k / a_k \rceil)$, and a window of steps $j_1$ to $j_2$ forces $a_k \ge \lceil W_k[j_1, j_2] / (j_2 - j_1) \rceil$ units. List scheduling is a heuristic with latency at most $(|K| + 1)\lambda^*$ for $|K|$ unit types.
- The [ILP formulation](/ilp-scheduling-formulation/) is exact, with variables only in the ASAP to ALAP window of each operation, but can take exponential time. [SDC scheduling](/sdc-scheduling/) writes timing, chaining and latency as difference constraints, whose matrix is totally unimodular, so the LP optimum is an integer schedule; its resource rows are a heuristic ordering.
- Binding is clique partitioning of a [compatibility graph](/resource-compatibility-graph/). For straight-line code the fewest registers equals the largest number of live values $L$, which the [left-edge algorithm](/left-edge-algorithm/) reaches; with values that cross loop iterations it lies between $L$ and $2L$ and is NP-complete ([register binding](/register-binding/)). [Tseng-Siewiorek](/tseng-siewiorek-clique-partitioning/) and [weighted bipartite matching](/weighted-bipartite-matching-binding/) are heuristics; the second uses $L$ registers on straight-line code, with no wiring guarantee.
- A two-port unit fed by $n$ registers needs exactly $n + \mathrm{oct}(G)$ connections, with $\mathrm{oct}(G)$ the fewest registers whose removal leaves the operand graph bipartite; this is NP-complete ([interconnect binding](/interconnect-binding/)).
- A connected [synchronous dataflow](/synchronous-dataflow/) graph with $n$ actors has a periodic schedule only if its topology matrix has rank $n - 1$; the [static scheduler](/sdf-static-scheduling/) decides existence exactly but does not minimize buffers. [Kahn process networks](/kahn-process-network/) are determinate, but termination and bounded memory are undecidable.
- A recursive loop has sample period at least the [iteration bound](/iteration-bound/) $T_\infty = \max_C t(C)/w(C)$. Retiming cannot go below it; [unfolding](/dsp-unfolding/) by $J$ multiplies it by $J$ and, with retiming, can reach it per sample. A pipelined loop has $\mathrm{II} \ge \max(\mathrm{ResMII}, \mathrm{RecMII})$, and [SDC modulo scheduling](/sdc-modulo-scheduling/) does not always find the least II.
- A state machine splits serially if and only if it has a nontrivial partition with the substitution property, and in parallel when two such partitions meet in the zero partition ([FSM decomposition](/fsm-decomposition/)). [KISS](/kiss-symbolic-minimization/), [NOVA](/nova-state-encoding/) and [MUSTANG](/mustang-state-assignment/) have no optimality proof.
- [Hardware-software partitioning](/hardware-software-partitioning/) with an area budget $A$ is weakly NP-hard, like knapsack, and solved in $O(nA)$ time; with communication costs and no budget it is a minimum cut. [Bitwidth analysis](/bitwidth-analysis/) is sound but not exact.

| Method | Problem | Time | Guarantee |
|---|---|---|---|
| ASAP, ALAP (Chapter 32.2) | unlimited units | $O(V + E)$ | least latency, exact |
| List scheduling | fixed units | polynomial | heuristic, at most $(\lvert K\rvert+1)\lambda^*$ |
| Force-directed (Chapter 32.2) | fixed latency | $O(V^2 L(E + VL))$ | heuristic |
| ILP | either form | exponential worst | exact |
| SDC | timing and latency | $O(V(V+E) + VC)$ | exact for difference rows; heuristic for units |
| Path-based (AFAP) | branchy code | $O(PV^2 \log V + R(RV + E \log E))$ | exact per path; heuristic merge |
| SDC modulo | loop pipelining | $O(IPV^2(V+E))$ | valid II; not always least |
| Left-edge (Chapter 32.6) | registers, straight-line | sort, one pass per register | exact, $L$ registers |
| Tseng-Siewiorek | clique partition | $O(n^2 m)$ | heuristic |
| Weighted bipartite matching | registers and wiring | $O(n \log n + nL^2 + nLD)$ | $L$ registers; wiring heuristic |
| SDF static scheduler | periodic schedule | $O(n + E + (n + QD)D)$ | exact for existence |
| KISS, NOVA, MUSTANG | state encoding | see entries | heuristic |

: Main methods. $V$ and $E$ count operations and edges, $C$ difference constraints and $L$ the steps (force-directed) or the live values (binding); for the path scheduler $P$ counts paths and $R$ constraints, for modulo scheduling $I$ counts the intervals tried and $P$ is the largest; $n$ counts values or vertices, $m$ edges, $D$ unit ports and $Q$ firings per period.

## Choosing a method

For a small block, solve the ILP: the answer is optimal, and window bounds show how far a heuristic falls short. For larger blocks, list scheduling under unit limits and force-directed scheduling under a latency limit are the classic choices. SDC scheduling solves period, chaining and latency rows exactly in one linear program. Branchy code calls for path-based scheduling or speculative code motion, loops for SDC modulo scheduling, and memory partitioning when array ports limit the interval.

Bind registers of straight-line code by left-edge when only the count matters, and by weighted bipartite matching when wiring matters too. For filters, compute the iteration bound, then retime, unfold or fold. For a controller, try decomposition when the machine has partitions with the substitution property, then encode with NOVA or KISS for two-level logic or MUSTANG for multi-level logic, and compare after synthesis.

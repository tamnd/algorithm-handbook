## What to remember

- The [Elmore delay](/elmore-delay/) of a node of an [RC tree](/rc-tree/) is $\sum_k R_k C^{\downarrow}_k$ over the resistors on its path, with $C^{\downarrow}_k$ the capacitance below resistor $k$. Two passes give it at all nodes in $O(n)$ time. It is the first moment of the impulse response and an upper bound on the 50 percent delay of an RC tree, a model and not the exact delay.
- [Static timing analysis](/static-timing-analysis/) propagates arrival times forward and required times backward on the [timing graph](/timing-graph/) in $\Theta(V + E)$ time. It is exact for the graph and pessimistic for the circuit, because it counts [false paths](/false-path/).
- Setup bounds the longest path, $c_{\text{launch}} + d_{\max} + t_{\text{setup}} \le c_{\text{capture}} + T$, and hold the shortest, $c_{\text{launch}} + d_{\min} \ge c_{\text{capture}} + t_{\text{hold}}$, which does not involve $T$. [Clock skew scheduling](/clock-skew-scheduling/) chooses the $c_i$; the least period is a maximum cycle ratio.
- For a given topology, [Tsay's merge](/tsay-zero-skew/) gives exact zero Elmore skew in $\Theta(n)$ time, and [DME](/deferred-merge-embedding/) the least wire under linear delay. Choosing the topology is NP-hard.
- [Van Ginneken's algorithm](/van-ginneken-buffer-insertion/) keeps only non-dominated (load, required time) pairs and finds the best source slack over the given positions in $O(n^2)$ time. [Logical effort](/logical-effort/) gives the least path delay $N F^{1/N} + P$, best near a stage effort of 4.
- [Gate sizing](/gate-sizing/) is NP-hard with discrete sizes and a geometric program with continuous sizes under the Elmore delay.
- [Layout versus schematic](/layout-versus-schematic/) is GI-complete; [Gemini](/gemini-netlist-comparison/) is exponential in the worst case and near-linear on real circuits, which is measured. Double patterning is a bipartiteness test; triple patterning is NP-complete.
- Detecting a [stuck-at fault](/stuck-at-fault-model/) is NP-complete; [PODEM](/podem/) and [SAT-based ATPG](/sat-based-atpg/) are complete searches. A $k$-bit signature aliases with probability below $2^{-k}$ when all error streams are equally likely ([built-in self-test](/built-in-self-test/)).

| Method | Problem | Cost | Guarantee |
|---|---|---|---|
| [Elmore delay](/elmore-delay/) | RC tree delay | $O(n)$ | upper bound on the 50% delay; a model |
| [AWE](/asymptotic-waveform-evaluation/) | $q$-pole model | moment solves | $2q$ moments; poles can be unstable |
| [PRIMA](/prima/) | reduced RLC model | $\Theta(n^3 + k n^2 + k^2 n)$ | passive when $L = B$ |
| [STA](/static-timing-analysis/) | slacks | $\Theta(V + E)$ | exact on the graph; conservative |
| [SSTA](/statistical-static-timing-analysis/) | delay distributions | $\Theta((V + E) m)$ | approximate max |
| [Tsay merge](/tsay-zero-skew/) | zero skew, given topology | $\Theta(n)$ | exact zero Elmore skew |
| [DME](/deferred-merge-embedding/) | zero skew, least wire | $\Theta(n)$ | optimal under linear delay only |
| [Van Ginneken](/van-ginneken-buffer-insertion/) | buffers on a tree | $O(n^2)$ | best slack for the given positions |
| [TILOS](/tilos/) | gate sizes | $O(K(n + m))$ | heuristic; measured |
| [LR sizing](/lagrangian-relaxation-gate-sizing/) | continuous sizes | $O(S(n + m))$ per round | exact at optimal multipliers |
| [Gemini](/gemini-netlist-comparison/) | LVS | exponential worst case | exact; speed measured |
| [PODEM](/podem/) | test for one fault | $\le 2^{n+1} - 1$ search nodes | complete |

: The main methods. $n$ counts tree nodes, sinks or primary inputs, $m$ sources of variation (SSTA) or connections (sizing), $K$ size steps and $S$ sweeps, as in each entry.

## Choosing a method

Run static timing analysis with table-based cell delays and Elmore or reduced wire models, and read its slack as safe but pessimistic. Declare a false path only when you can show that no vector sensitizes it. Use the Elmore delay to rank choices inside an optimizer, and a reduced model with more poles for sign-off; prefer PRIMA when the model will be simulated.

Use an H-tree for sinks on a regular grid, and otherwise a topology from means and medians with DME embedding. For test, collapse the faults, run pseudorandom vectors with fault simulation and dropping, and send the faults that are left to PODEM or a SAT-based generator with a time limit.

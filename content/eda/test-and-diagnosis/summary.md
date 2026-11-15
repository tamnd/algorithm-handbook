## What to remember

- [Fault coverage](/fault-coverage/) counts detected faults of one model over the fault list. It says nothing about defects outside the model, and collapsed and uncollapsed coverage of the same tests can differ. A [redundant fault](/redundant-fault/) can never be detected, and a proof of redundancy shows logic that can be removed.
- The [Williams-Brown defect level](/williams-brown-defect-level/) $1 - Y^{1-T}$ is exact in a model where every fault is equally likely and faults occur independently.
- A complete stuck-at test set can miss a [bridge](/bridging-fault-model/), a slow node of the [transition model](/transition-fault-model/) or a defect inside a cell; [cell-aware test](/cell-aware-test/) and [N-detect tests](/n-detect-test/) answer this. A [robust test](/robust-path-delay-test/) detects a slow path whatever the other delays; a non-robust test does not.
- [Static](/static-learning/) and [recursive learning](/recursive-learning/) are sound: every learned implication holds. Static learning is not complete. Recursive learning with depth $L$, the number of lines, and two calls per line finds every necessary value, at a cost exponential in the depth.
- [Parallel fault simulation](/parallel-fault-simulation/), [PPSFP](/ppsfp/), [deductive fault simulation](/deductive-fault-simulation/) and [critical path tracing](/critical-path-tracing/) are exact for single stuck-at faults. Critical path tracing needs an explicit check at each fanout stem, since a stem's criticality is not a function of its branches.
- A [MISR](/multiple-input-signature-register/) signature is the response polynomial modulo $q(x)$. An error aliases exactly when its polynomial is a multiple of $q$. The rate $2^{-k}$ is an upper bound when all error streams are equally likely and only a limit under independent bit errors, per the [aliasing entry](/signature-aliasing-probability/).
- [LFSR reseeding](/lfsr-reseeding/) and [embedded deterministic test](/embedded-deterministic-test/) encode a test cube exactly when a linear system over GF(2) is consistent. A cube with fewer care bits than the register length can still fail.
- [March C−](/march-test/) uses $10N$ operations and detects every stuck-at, transition and unlinked [coupling fault](/memory-coupling-fault/) of van de Goor's model. MATS+ uses $5N$ and misses some.
- [Fault dictionaries](/fault-dictionary/) and [effect-cause diagnosis](/effect-cause-diagnosis/) return the modelled faults that match a failure. Equivalent faults always tie, so the answer can be ambiguous, and a real defect may match no single stuck-at fault at all.

| Method | Problem | Cost | Guarantee |
|---|---|---|---|
| [FAN](/fan-algorithm/) | test for one fault | $O(L(L+P) + 2^h(L+P))$ | complete for the fault model |
| [Static learning](/static-learning/) | indirect implications | $O(L(L+P+E))$ per pass | sound, not complete |
| [Recursive learning](/recursive-learning/) | necessary values | exponential in the depth | all necessary values at depth $\ge L$ |
| [Static compaction](/static-test-compaction/) | fewer patterns | merging and fault simulation | minimum is NP-hard; heuristics |
| [Parallel fault simulation](/parallel-fault-simulation/) | detected faults | $O(T(F/(w-1)+1)(L+P))$ | exact |
| [PPSFP](/ppsfp/) | detected faults | $O((T/w+1)(1+F)(L+P))$ | exact, combinational |
| [Critical path tracing](/critical-path-tracing/) | detected faults | $O(T(L+P)(1+S))$ | exact with stem checks |
| [COP](/cop-testability-measure/) | detection probabilities | $O(L+P)$ | exact on fanout-free circuits; an estimate otherwise |
| [MISR](/multiple-input-signature-register/) | response compaction | $O(m(k/w+1))$ | aliasing near $2^{-k}$ in a model |
| [LFSR reseeding](/lfsr-reseeding/) | seed for a cube | GF(2) elimination | exact: a seed exists or not |
| [Scan chain ordering](/scan-chain-ordering/) | short scan wiring | $O(2^n n^2)$ exact | NP-hard; heuristics measured |
| [March C−](/march-test/) | memory test | $10N$ operations | complete for the unlinked fault list |
| [Effect-cause diagnosis](/effect-cause-diagnosis/) | candidate faults | $O((T+K+CT)(L+P))$ | exact for single stuck-at faults |

: The main methods. $L$ counts lines, $P$ gate input pins, $T$ tests, $F$ faults, $w$ the word size, $S$ fanout stems, $h$ head lines, $E$ learned implications, $C$ candidates and $K$ failing outputs, as in each entry.

## Choosing a method

Start from the fault model. After the stuck-at tests of chapter 32.7, add [transition](/transition-fault-model/) tests for at-speed defects, applied by [launch-on-capture or launch-on-shift](/launch-on-capture-and-launch-on-shift/), and [path delay](/path-delay-fault-model/) tests for the few critical paths that [static timing analysis](/static-timing-analysis/) reports. Add [IDDQ](/iddq-testing/) or bridging tests for shorts, and cell-aware tests once the library is characterized.

For generation, use a complete search with learning, and let [dynamic compaction](/dynamic-test-compaction/) fill the free inputs. Use [time-frame expansion](/time-frame-expansion/) only when full scan is not available. For large scan designs, simulate with PPSFP.

For built-in self-test, measure random-pattern testability with COP first. Then add [test points](/test-point-insertion/) or [weighted patterns](/weighted-random-pattern-testing/) for the hard faults. For tester patterns, [broadcast scan](/broadcast-scan/) is the simplest compression, reseeding and EDT encode more care bits per tester bit, and [X-Compact](/x-compact/) compacts outputs that may be unknown.

Use [boundary scan](/boundary-scan/) on a board and a [wrapper and TAM](/soc-test-wrapper-and-tam-design/) on a system on chip. Test memories with a march test chosen for the fault list. For a failing chip, use a dictionary when the fault list is small and many chips share the tests, and effect-cause diagnosis otherwise.

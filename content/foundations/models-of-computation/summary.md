## What to remember

- A cost is a count of steps in a stated model. The same problem can have different costs in different models: sorting $n$ integers takes $\Theta(n \log n)$ comparisons in the [comparison model](/comparison-model/) but $O(n)$ time on a [word RAM](/word-ram/) when the keys are below $n^2$.
- The [random access machine](/random-access-machine/) reads and writes any memory cell in one step. Under the [unit-cost model](/unit-cost-model/) every operation costs 1; under the [logarithmic-cost model](/logarithmic-cost-model/) an operation on an integer $x$ costs about $\lg |x|$. Unit cost is safe only when the numbers stay small; repeated squaring builds $2^{2^n}$ in $n$ steps.
- The [word RAM](/word-ram/) is the default model of the handbook: words of $w$ bits with $w \ge \lg n$, so that a word can hold an index into the input, and constant-time arithmetic, comparison and bitwise operations on words.
- A [decision tree](/decision-tree-model/) with $L$ leaves has height at least $\lceil \lg L \rceil$. Any problem with $N$ possible answers that the algorithm must tell apart needs at least $\lceil \lg N \rceil$ yes-no queries in the worst case; for sorting, $N = n!$.
- The [external memory model](/external-memory-model/) has a memory of $M$ items, a disk moved in blocks of $B$ items, and counts only block transfers: scanning costs $\Theta(N/B)$, sorting $\Theta(\frac{N}{B} \log_{M/B} \frac{N}{B})$ and searching $\Theta(\log_B N)$. A [cache-oblivious](/cache-oblivious-model/) algorithm meets such bounds without knowing $M$ or $B$.
- A [Turing machine](/turing-machine/) and a log-cost RAM simulate each other with polynomial overhead, as the entry on [RAM and Turing machine equivalence](/ram-turing-equivalence/) shows, so polynomial time means the same thing on both. One tape costs more: recognizing palindromes on a one-tape machine takes $\Omega(n^2)$ steps.
- A [nondeterministic](/nondeterministic-turing-machine/) machine accepts if some sequence of choices accepts; a [probabilistic](/probabilistic-turing-machine/) one accepts with a probability, and repeating it $k$ times cuts a one-sided error of $1/2$ to $2^{-k}$.
- A [Boolean circuit](/boolean-circuit/) family has one circuit for each input length. Circuits of polynomial size can decide some undecidable languages, which is why [non-uniform computation](/non-uniform-computation/) is a different notion from an algorithm.

## The models side by side

| Model | Memory | What a step costs | Used for |
|---|---|---|---|
| [RAM](/random-access-machine/), unit cost | unbounded integers | 1 per instruction | quick analysis, small numbers |
| [Word RAM](/word-ram/) | words of $w \ge \lg n$ bits | 1 per word operation | almost every upper bound |
| [Real RAM](/real-ram/) | exact real numbers | 1 per arithmetic operation | computational geometry |
| [Pointer machine](/pointer-machine/) | records linked by pointers | 1 per pointer step | lower bounds for linked structures |
| [Comparison model](/comparison-model/) | the input, seen only through comparisons | 1 per comparison | sorting and searching lower bounds |
| [Cell-probe model](/cell-probe-model/) | cells of $w$ bits | 1 per cell read or written | data-structure lower bounds |
| [External memory](/external-memory-model/) | memory $M$, blocks of $B$ | 1 per block transfer | data on disk |
| [Cache-oblivious](/cache-oblivious-model/) | as above, $M$ and $B$ unknown | 1 per block transfer | caches at all levels at once |
| [Turing machine](/turing-machine/) | tapes of symbols | 1 per head move | complexity classes |
| [Boolean circuit](/boolean-circuit/) | none; one circuit per length | size and depth | non-uniform and parallel lower bounds |

: The main models of the chapter. Each row says what the model can store and what it counts. Free computation between counted steps is what makes the comparison, cell-probe and external-memory models good for lower bounds: a bound that holds with free computation holds on any real machine.

## Choosing a model

- Use the word RAM unless there is a reason not to, and state $w$ when the algorithm uses bit tricks or packs several keys into one word.
- When an algorithm multiplies or squares large numbers, check that the numbers fit in a word; if they do not, charge for their length with the logarithmic-cost model or with a bound on the bit length.
- When the data do not fit in memory, count block transfers. An algorithm with fewer operations can lose to one with fewer transfers by orders of magnitude.
- A lower bound is only as strong as its model. A comparison lower bound says nothing about an algorithm that uses keys as addresses, and the $\Omega(n \log n)$ bound for element distinctness in algebraic decision trees does not cover hashing.
- For questions of what is computable, or of polynomial versus exponential time, the choice among reasonable sequential models does not matter. For exact running times it does.

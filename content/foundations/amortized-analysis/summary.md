## What to remember

- Amortized costs $\hat c_i$ are valid when $\sum_{i=1}^{m} c_i \le \sum_{i=1}^{m} \hat c_i$ for every sequence of operations from the start state, where $c_i$ are the actual costs. The bound is about every sequence, not about a random or typical one, and it says nothing about a single operation.
- The [aggregate method](/aggregate-method/) bounds the total directly. In $n$ increments of a [binary counter](/binary-counter-increment/) from 0, bit $i$ flips $\lfloor n/2^i \rfloor$ times, so the total is less than $2n$.
- The [accounting method](/accounting-method/) charges a fixed amount per operation and stores the surplus as credit on objects. The credit must never become negative. For the [stack with multipop](/stack-with-multipop/), a push pays 2: one for itself and one stored on the item for its later pop.
- The [potential method](/potential-method/) sets $\hat c_i = c_i + \Phi(D_i) - \Phi(D_{i-1})$. The sum telescopes to $\sum c_i + \Phi(D_m) - \Phi(D_0)$, so the amortized costs are valid whenever $\Phi(D_m) \ge \Phi(D_0)$ for all reachable states, in particular when $\Phi \ge 0$ and $\Phi(D_0) = 0$.
- A good potential is large in the states that come before an expensive operation, and the expensive operation lowers it by about its own cost.
- [Array doubling](/array-doubling/) gives $O(1)$ amortized appends with $\Phi = 2n - c$. Growth by any constant factor works; growth by a constant number of cells costs $\Theta(n^2)$ for $n$ appends.
- A table that [shrinks](/dynamic-table-contraction/) must not halve as soon as it is half full: a sequence that alternates around the threshold then pays a resize on every step. Halving at a quarter full keeps every operation $O(1)$ amortized.
- An amortized bound is not an [expected](/amortized-vs-expected-cost/) bound, and it fails when old states can be revisited: if a structure can be copied or an operation undone, a costly operation can be repeated without paying again. [Global rebuilding](/global-rebuilding/) spreads a rebuild over many operations to bound each one.

## Amortized bounds in this handbook

| Structure | Operation | Worst single cost | Amortized cost | Potential |
|---|---|---|---|---|
| [Binary counter](/binary-counter-increment/) | increment | $k$ bit flips | 2 | number of 1 bits |
| [Stack with multipop](/stack-with-multipop/) | multipop | $n$ | push 2, pop and multipop 0 | stack size |
| [Dynamic array](/array-doubling/) | append | $n$ | 3 | $2n - c$ |
| [Table with contraction](/dynamic-table-contraction/) | insert, delete | $n$ | 3 and 2 | $2n - c$ or $c/2 - n$ |
| [Splay tree](/splay-tree/) | access | $n$ | $O(\log n)$ | sum of $\lg$ of subtree sizes |
| [Fibonacci heap](/fibonacci-heap/) | extract-min | $n$ | $O(\log n)$ | trees plus twice the marked nodes |

: Some amortized bounds and the potentials that prove them. Here $n$ is the number of items, $c$ the capacity of a table and $k$ the number of bits of the counter. The first four are the examples of this chapter; the last two are in Volume 3.

## Doing an amortized analysis

- Start from the expensive operation and ask what made it possible. Each item copied in a doubling was appended since the last doubling; each item popped by multipop was pushed once.
- Try the aggregate method first. Use the potential method when the operations are of several kinds and you want a separate bound for each.
- Check the potential on every operation, including the cheap ones, and check that it is never below its starting value.
- State the start state. A counter that starts at $2^k - 1$ or a stack that starts with $s$ items needs an extra term, the starting potential, in the bound.
- If single operations must be fast, an amortized bound is not enough. Spread the expensive work over the cheap operations, as global rebuilding does.

## What to remember

- An **array** reaches the item at index $i$ in $\Theta(1)$ time by computing its address, but an insert or delete at index $i$ moves $\Theta(n - i)$ items. A **linked list** inserts or deletes next to a node it holds in $\Theta(1)$ time, but reaches position $i$ only in $\Theta(i)$ steps. No list structure can have both: in the cell-probe model, get, insert and delete by position need $\Omega(\log n / \log \log n)$ amortized time per operation for some sequences.
- A **stack** (last in, first out), a **queue** (first in, first out) and a **deque** (both ends) each take $O(1)$ time per operation, on a linked list or on an array.
- A **dynamic array** that doubles when full and halves when a quarter full takes $O(1)$ amortized time per append and pop, and its capacity stays below $4\max(n, 1)$. Halving at one half instead is a mistake: operations that alternate at the boundary cost $\Theta(n)$ each.
- A **circular buffer** turns a fixed array into a queue or deque with $O(1)$ worst-case time and no allocation, by taking indices modulo the capacity.
- A **doubly linked list with a sentinel** has no special cases for the ends or the empty list, and deletes a node it holds in $O(1)$ time. A singly linked list needs the predecessor for that, which costs $\Theta(n)$ to find.
- **Floyd's** and **Brent's** methods find the tail length $\mu$ and the cycle length $\lambda$ of an iterated function with $O(\mu + \lambda)$ evaluations and $O(1)$ memory.
- **A queue built from two stacks** moves each item at most once, so it takes $O(1)$ amortized time per operation; with a running minimum on each stack it answers the minimum of the queue. A **monotonic stack** or **monotonic deque** pops each item at most once, so a scan of $n$ items costs $\Theta(n)$.
- A **sequential search** table needs $n$ compares for a miss, which is optimal when keys can only be tested for equality. A **binary search** table searches in at most $\lfloor \lg n \rfloor + 1$ compares but inserts in $\Theta(n)$.
- **Move-to-front** costs at most $2(C_A + X_A) - m$ on every sequence of $m$ requests, where $C_A + X_A$ is the cost of any other algorithm $A$, so it is 2-competitive; no deterministic rule beats $2 - 2/(n + 1)$.

## The main sequence structures side by side

| Structure | Item $i$ | Front | Back | Middle, at a held place | Space |
|---|---|---|---|---|---|
| [Array](/array/) | $\Theta(1)$ | $\Theta(n)$ | $\Theta(1)$ while there is room | $\Theta(n - i + 1)$ | $N$ cells |
| [Dynamic array](/dynamic-array/) | $\Theta(1)$ | $\Theta(n)$ | $O(1)$ amortized | $\Theta(n - i + 1)$ | under $4\max(n, 1)$ cells |
| [Circular buffer](/circular-buffer/) | $\Theta(1)$ | $O(1)$ | $O(1)$ | $\Theta(\min(i, n - i) + 1)$ | $N$ cells, 2 words |
| [Gap buffer](/gap-buffer/), gap at $g$ | $\Theta(1)$ | $\Theta(g + 1)$ | $\Theta(n - g + 1)$ | $O(1)$ amortized at the gap | at most $\max(cap_0, 2n_{\max})$ cells |
| [Singly linked list](/singly-linked-list/), with tail | $\Theta(i)$ | $\Theta(1)$ | push $\Theta(1)$, pop $\Theta(n)$ | insert after $\Theta(1)$, delete $\Theta(n)$ | $n$ nodes of 2 fields |
| [Doubly linked list](/doubly-linked-list/), with sentinel | $\Theta(\min(i, n - i) + 1)$ | $\Theta(1)$ | $\Theta(1)$ | $\Theta(1)$ | $n + 1$ nodes of 3 fields |
| [Unrolled linked list](/unrolled-linked-list/), node size $b$ | $O(1 + n/b)$ | $O(b)$ | $O(n/b + b)$ | $O(n/b + b)$ by position | about $2n/b$ links |

: Worst-case times unless marked amortized. "Front" and "Back" are an insert or delete at that end. For the gap buffer, an edit away from the gap first moves the gap there, at a cost of the distance moved.

## Choosing a structure

- Use a dynamic array as the default sequence. Its items are contiguous and fast to scan.
- For a queue or a deque with a known bound on its size, or where allocation is not allowed, use a circular buffer.
- Use a doubly linked list when the program holds handles to items and must delete them or insert next to them in $O(1)$ time, as in an LRU cache.
- For text edited at a cursor, use a gap buffer; for a long sequence edited at many places, use a balanced tree such as a [rope](/rope/) from Chapter 3.8.
- For a small symbol table, or keys with only an equality test, a sequential search list is fine. For a static table with ordered keys, use sorted arrays and binary search. Otherwise use a [hash table](/hash-table/) or a search tree from the next chapters.

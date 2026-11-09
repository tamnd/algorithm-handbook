## What to remember

- An **ordered set** is a dictionary that also answers min, max, predecessor, successor, floor, ceiling, rank and select. In the [comparison model](/comparison-model/) a search needs $\lceil \lg(n + 1) \rceil$ comparisons in the worst case, and a structure whose inserts are cheap must pay in its queries, because an ordered set can sort.
- A **binary search tree** does every ordered-set operation along one path, in $\Theta(h)$ time. The height lies between $\lfloor \lg n \rfloor$ and $n - 1$; keys inserted in sorted order give the worst case, a path, after $n(n-1)/2$ comparisons.
- **Deletion** of a node with two children replaces it by its successor, the minimum of its right subtree, which has no left child. The asymmetric choice tilts trees under long mixed sequences of updates.
- A **random BST** has $\mathbb{E}[\mathrm{depth}(i)] = H_i + H_{n-i+1} - 2$ for the key of rank $i$, average depth $2(1 + 1/n)H_n - 4 \approx 1.39 \lg n$, and expected height about $4.311 \ln n \approx 2.99 \lg n$. The [skip list](/skip-list/) and the treap get these costs for every input by drawing their own random bits.
- An **augmented** tree stores in each node a field computed from the node and its children, such as the subtree size. Such a field is fixed after a rotation in $O(1)$ time.
- For known access probabilities, the **optimal static tree** comes from an interval DP in $\Theta(n^3)$ time, or $\Theta(n^2)$ with Knuth's monotone roots. Its expected cost is at least $H / \lg 3$ comparisons, where $H$ is the entropy of the distribution.
- A **splay tree** moves each accessed node to the root by zig, zig-zig and zig-zag steps. One access can cost $\Theta(n)$, but $m$ accesses cost $O((m + n) \log n)$, within a constant factor of the best static tree, and an access costs $O(\log(t + 1))$ amortized when $t$ distinct keys were used since the last access to it.
- Whether splay trees are $O(1)$-competitive with every binary search tree algorithm is the **dynamic optimality conjecture**, open since 1985. The best known ratio is $O(\log \log n)$, by the [tango tree](/tango-tree/).
- The $\lg n$ barrier is a property of comparisons from the root. A [finger search](/finger-search-tree/) costs $O(\log d)$ for a key $d$ places away, and on $w$-bit integers a [fusion tree](/fusion-tree/) answers predecessor queries in $O(\log n / \log w)$ time.

## The structures side by side

| Structure | Search | Insert or delete | Kind of bound | Extra per node |
|---|---|---|---|---|
| [Binary search tree](/binary-search-tree/) | $\Theta(h)$, up to $\Theta(n)$ | $\Theta(h)$ | worst case | none |
| [Random BST](/random-binary-search-tree/) | $\Theta(\log n)$ | $\Theta(\log n)$ | average over insertion orders | none |
| [Skip list](/skip-list/) | $\Theta(\log n)$ | $\Theta(\log n)$ | expected, for every input | $1/(1-p)$ pointers on average |
| [Optimal static BST](/optimal-bst-dynamic-programming/) | least expected cost | no updates | worst case, $\Theta(n^2)$ to build | none |
| [Splay tree](/splay-tree/) | $O(\log n)$ | $O(\log n)$ | amortized; $\Theta(n)$ worst | none |
| [Tango tree](/tango-tree/) | $O(\log n \log \log n)$ | none | worst case; $O(\log \log n)$-competitive | depth and path data |
| [Finger search tree](/finger-search-tree/) | $O(\log d)$ | $O(1)$ amortized at a finger | worst case search | level links |
| [Fusion tree](/fusion-tree/) | $O(\log n / \log w)$ | amortized in the dynamic form | worst case, word RAM | packed sketches |

: Costs of the search structures of the chapter for $n$ keys. Here $h$ is the height, $d$ the distance in keys from the finger, $w$ the word size, and $p$ the level probability of the skip list. The balanced trees of Chapter 3.4 have $\Theta(\log n)$ worst-case cost for all operations.

## Choosing a structure

- For lookups by exact key only, use a hash table. Use a search tree when order matters: ranges, successors, ranks, sorted output.
- In production code, use the balanced tree of your library (Chapter 3.4). Write a plain binary search tree only when the keys arrive in random order.
- A skip list is short to write, and its costs do not depend on the input order. It spends more memory on pointers than a tree.
- When a few keys get most of the accesses, a splay tree adapts with no tuning. Avoid it when each single operation has a deadline.
- When the probabilities are known in advance and the set does not change, build the optimal static tree once.
- When the keys are machine integers and the set is large, look at integer structures such as the van Emde Boas tree and the fusion tree; see the [predecessor problem](/predecessor-problem/).

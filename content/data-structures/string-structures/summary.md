## What to remember

- A [trie](/trie/) stores a set of strings so that a search reads the key once, one symbol per step. The cost does not depend on the number of keys, and the keys with a given prefix fill one subtree, which a hash table cannot offer.
- The plain trie with an array of $R$ links in each node is fast but can use $R$ links for each symbol of the keys. Every other trie of the chapter is the same tree with a smaller layout.
- The [radix tree](/radix-tree/) merges chains of one-child nodes into labelled edges and has at most $2n$ nodes for $n$ keys, whatever their length. The [adaptive radix tree](/adaptive-radix-tree/) also lets each node choose its size from its number of children.
- The [ternary search tree](/ternary-search-tree/) keeps the children of a node in a binary search tree. It has 3 links per node, one node for each node of the trie except the root, and pays extra comparisons for the left and right steps.
- Static tries can be packed: the [double-array trie](/double-array-trie/) keeps two array reads per symbol in about two integers per node, and the [LOUDS trie](/louds-trie/) stores the shape in $2n + 1$ bits.
- On real hardware, misses count more than steps. The [burst trie](/burst-trie/) and the [HAT-trie](/hat-trie/) keep a small trie on top of dense containers, and the [String B-tree](/string-b-tree/) brings the idea to disk.
- A [rope](/rope/) and a [piece table](/piece-table/) edit a long text without moving it. The cost of an edit depends on the depth of the tree or the number of pieces, not on the length of the text.
- A pattern occurs in a text exactly where it is a prefix of a suffix, so [substring queries](/substring-queries/) are prefix matching on the suffixes. Building the suffix structures in linear time and listing results by [document](/muthukrishnan-document-listing/) are the topics of the last groups.

| Structure | Search for a key of length $m$ | Space |
|---|---|---|
| Trie, array of $R$ links | $\Theta(m)$ | $\Theta(R)$ words per node, at most $N + 1$ nodes |
| Radix tree | $O(m)$ | at most $2n$ nodes, plus the keys |
| Ternary search tree | $O(mR)$, or $O(m \log R)$ with balanced sibling trees | 3 links per node, at most $N$ nodes |
| Hybrid TST | $O(1)$ plus a TST search on $m - 2$ symbols | $R^2$ cells plus the TST nodes |
| Adaptive radix tree | $O(m)$ | $O(1)$ words per key for the inner nodes, plus the leaves |
| Double-array trie | $O(m)$, two array reads per symbol | $2M$ integers, $M \ge$ number of nodes |
| LOUDS trie | $O(m \log \sigma)$ | $2n + 1 + n \lceil \log_2 \sigma \rceil + n$ bits plus $o(n)$, for $n$ nodes |
| Burst trie | $O(m)$ slot steps and $O(\log L)$ string comparisons | the keys, plus $R$ links per access node |
| String B-tree, on disk | $O(p/B + \log_B K)$ I/Os for a pattern of length $p$ | $O(K/B)$ pages plus the strings |

: Worst-case costs for $n$ keys of total length $N$ over an alphabet of $R$ (or $\sigma$) symbols. $L$ is the container limit of the burst trie, $B$ the page size and $K$ the number of strings of the String B-tree.

## Choosing a structure

- For a set of strings in memory that changes, with prefix queries, start with a radix tree or a ternary search tree. A ternary search tree is the simplest to write and wastes no links on a large alphabet; a radix tree has fewer nodes when keys are long and share little.
- For a large in-memory index of byte strings, such as the index of a database, use an adaptive radix tree. For string keys that are mostly searched and seldom listed in order, a HAT-trie or a burst trie has fewer cache misses than a trie of pointers.
- For a static dictionary that must be small and fast, as in a morphological analyser, build a double-array trie. When space matters more than speed, use a LOUDS trie.
- For an editor, a piece table is the simplest structure and keeps old versions cheap; store its pieces in a balanced tree when the file has many edits. Use a rope when texts are joined and split often, or when many versions must share memory.
- For a text that must answer substring queries, use the suffix structures of Volume 8. Use a sparse suffix tree when only some positions matter, and a compressed index when the text is too large for a suffix array.

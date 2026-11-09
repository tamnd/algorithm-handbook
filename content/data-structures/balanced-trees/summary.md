## What to remember

- A **rotation** moves a child into its parent's place, keeps the order of the keys and costs $O(1)$. At most $2n - 2$ rotations turn any tree on $n$ keys into any other. Every balanced tree repairs the path of an update with rotations or a rebuild.
- An **AVL tree** keeps the subtree heights of each node within one. The smallest tree of height $h$ has $F_{h+2} - 1$ nodes, so the height is below $1.4405 \lg(n + 2)$. An insertion needs at most one single or double rotation; a deletion may need $O(\log n)$.
- A **2-3 tree** or **2-3-4 tree** keeps all leaves at one depth and grows only at the root, by splitting full nodes. Its height is at most $\lg(n + 1)$.
- A **red-black tree** is a 2-3-4 tree written with binary nodes and one color bit. A subtree of [black-height](/black-height/) $b$ holds at least $2^b - 1$ keys, so the height is at most $2 \lg(n + 1)$. An insertion does at most two rotations and a deletion at most three.
- An **order-statistic tree** stores subtree sizes and answers SELECT and RANK in $O(\log n)$ time. A size is fixed in $O(1)$ time after a rotation, so any balanced tree can carry it.
- A **weight-balanced tree** bounds the ratio of sibling sizes, with height below $2.41 \lg(n + 1)$ for $\Delta = 3$. A **scapegoat tree** stores nothing in its nodes and rebuilds lopsided subtrees, at $O(\log n)$ amortized cost per update.
- A **treap** has the shape of a random binary search tree for every sequence of updates: expected depth below $2 \ln n \approx 1.39 \lg n$, fewer than two rotations per update on average. [Split](/treap-split/) and [merge](/treap-merge/) give all other operations.
- The **WAVL tree** does at most two rotations per update and is an AVL tree when there are no deletions. With **join** as the only balance-aware step, union of sets of sizes $m \le n$ takes $O(m \log(n/m + 1))$ work.

## The trees side by side

| Tree | Height for $n$ keys | Restructuring per update | Kind of bound | Data per node |
|---|---|---|---|---|
| [AVL tree](/avl-tree/) | $< 1.4405 \lg(n + 2)$ | insertion $\le 1$ single or double rotation, deletion $O(\log n)$ | worst case | height or balance factor |
| [2-3-4 tree](/two-three-four-tree/) | $\log_4(n+1)$ to $\lg(n + 1)$ | $O(\log n)$ splits or merges | worst case | 1 to 3 keys |
| [Red-black tree](/red-black-tree/) | $\le 2 \lg(n + 1)$ | insertion $\le 2$, deletion $\le 3$ rotations | worst case | 1 color bit |
| [Left-leaning red-black tree](/left-leaning-red-black-tree/) | $\le 2 \lg(n + 1)$ | $O(\log n)$ rotations | worst case | 1 color bit |
| [AA tree](/aa-tree/) | $\le 2 \lg(n + 1)$ | $O(\log n)$ skews and splits | worst case | a level |
| [WAVL tree](/wavl-tree/) | $\le 2 \lg n$ | $\le 2$ rotations | worst case | a rank |
| [Weight-balanced tree](/weight-balanced-tree/) | $< 2.41 \lg(n + 1)$ | $O(\log n)$ rotations | worst case | subtree size |
| [Scapegoat tree](/scapegoat-tree/) | $\le \log_{1/\alpha} n + 1$ | subtree rebuilds | amortized; $\Theta(n)$ worst | none |
| [Treap](/treap/) | expected depth $< 2 \ln n$ | $< 2$ rotations on average | expected; $\Theta(n)$ worst | a priority |
| [Zip tree](/zip-tree/) | expected depth about $1.5 \lg n$ | no rotations | expected; $\Theta(n)$ worst | a small rank |

: Balanced search trees with $n$ keys. Search, insertion and deletion take time proportional to the height, so $\Theta(\log n)$ in the sense of the fourth column. The entries count height in nodes or in edges, which moves the bounds by one.

## Choosing a balanced tree

- Use the sorted map of your library. In C++ and Java it is a red-black tree.
- For the shortest correct code of your own, write a treap with split and merge, or a left-leaning red-black tree.
- If searches far outnumber updates, the AVL tree has the smallest height bound here.
- For rank and select, store subtree sizes in any of these trees.
- If the nodes cannot hold extra fields, or other structures point into them, a scapegoat tree needs no balance data and no rotations.
- To cut, paste or reverse parts of a sequence by position, use an implicit treap.
- For bulk set operations or parallel code, use join-based algorithms.
- For data on disk, use a B-tree from Chapter 3.13.

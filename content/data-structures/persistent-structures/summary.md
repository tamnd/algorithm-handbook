## What to remember

- There are three degrees of persistence. Under **partial** persistence the versions form a list and only the newest can be updated; under **full** persistence they form a [version tree](/version-tree/); under **confluent** persistence an operation may combine two versions, and the versions form a directed acyclic graph.
- **Path copying** changes a node at depth $d$ of a tree by copying the $d + 1$ nodes from the root to it and sharing the rest. In a balanced tree that is $O(\log n)$ time and space per update, so $m$ updates use $O(n + m \log n)$ space, and searches on every version run at full speed. It needs nodes with one incoming pointer: with parent pointers, one change copies the whole tree.
- **Node copying** gives each node a few spare slots and copies a node only when they are full. By the [DSST theorem](/dsst-persistence-theorem/), a linked structure of bounded in-degree becomes partially or fully persistent with $O(1)$ worst-case time per access step and $O(1)$ amortized time and space per update step.
- **Arrays are harder.** A cell is reached by index from every version, so the theorem does not apply. Path copying gives $O(\log n)$ per access, Dietz's structure $O(\log \log m)$ for $m$ versions (amortized and expected), and [Baker's trick](/bakers-trick/) $O(1)$ on the version in use and $O(d)$ to switch to a version at distance $d$.
- A **purely functional** structure never writes a field twice, so it is fully persistent by construction. The [persistent stack](/persistent-stack/) is the simplest: push and pop take $\Theta(1)$ time, and $p$ pushes make $p$ nodes however many versions they create.
- **Amortized bounds can fail under persistence,** because one expensive version can be reused many times. Lazy evaluation with memoization repairs this: the [banker's queue](/banker-queue/) takes $O(1)$ amortized time per operation on any sequence of versions, and the [real-time queue](/real-time-queue/) adds a schedule that makes every operation $O(1)$ in the worst case.
- **Numerical representations** shape a structure after a number system. The [binary random-access list](/binary-random-access-list/) does everything in $O(\log n)$; the [skew binary](/skew-binary-random-access-list/) one does cons, head and tail in $\Theta(1)$ worst-case time and lookup in $O(\min(i, \log n))$.
- A **retroactive** structure has one timeline, and a change in the past changes the present. Undoing and redoing the $r$ later updates always works, and in general no method does much better, so efficient retroactive structures are built one type at a time.

## The general methods side by side

| Method | Read in a version | Update | Space per update | Degree | Condition |
|---|---|---|---|---|---|
| Copy the whole structure | $O(1)$ overhead | $\Theta(n)$ | $\Theta(n)$ | full | none |
| [Path copying](/path-copying/) | $O(1)$ overhead | $O(d + 1)$, $O(\log n)$ balanced | $O(d + 1)$ nodes | full | a tree, no parent pointers |
| [Fat node](/fat-node/) | $O(\log m)$ per step | $O(1)$ partial, $O(\log m)$ full | $O(1)$ per field change | partial, full | none |
| [Node copying](/node-copying/) | $O(1)$ per step | $O(1)$ amortized per step | $O(1)$ amortized | partial; node splitting for full | in-degree at most a constant |
| [Baker's trick](/bakers-trick/) | $O(1)$ in use, $O(d)$ to switch | the same | $O(1)$ | full | arrays |

: Here $n$ is the size of a version, $m$ the number of versions, and $d$ the depth of the changed node, or for Baker's trick the distance in the version tree from the version in use. A "step" is one field access or one field change of the ephemeral structure.

## Choosing a method

- For sets and maps in functional code, use a [persistent red-black tree](/persistent-red-black-tree/) or a [persistent treap](/persistent-treap/); both copy $O(\log n)$ nodes per update.
- For a sequence with fast indexing, use the 32-way [persistent vector](/persistent-vector/); for fast catenation and splitting, use a [finger tree](/finger-tree/).
- For many offline queries over prefixes of an array, such as the $k$-th smallest in a range, build one version of a [persistent segment tree](/persistent-segment-tree/) per prefix.
- For a backtracking search that returns only to ancestors of the current state, use a [semi-persistent array](/semi-persistent-array/) or Baker's trick: the state in use stays as fast as a plain array.
- For many versions of a large pointer structure where space matters, use node copying, which needs $O(1)$ amortized space per update instead of $O(\log n)$.
- For a queue, use the banker's queue if amortized time is enough and the real-time queue if every operation must be fast.

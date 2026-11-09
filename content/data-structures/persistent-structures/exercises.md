1. ◦ Start from version $v_0$ of some structure. Make $v_1 = \text{upd}(v_0)$, $v_2 = \text{upd}(v_1)$, $v_3 = \text{upd}(v_1)$, $v_4 = \text{upd}(v_3)$ and $v_5 = \text{upd}(v_0)$. Draw the [version tree](/version-tree/). Which updates could a [partially persistent](/partial-persistence/) structure not perform? If a seventh step makes $v_6 = \text{combine}(v_2, v_4)$, what kind of persistence is needed, and what does the graph of versions become?

2. ◦ On an empty [persistent stack](/persistent-stack/) $v_0$, make $v_1 = \text{push}(v_0, 1)$, $v_2 = \text{push}(v_1, 2)$, $v_3 = \text{push}(v_2, 3)$, $v_4 = \text{push}(v_2, 4)$, then pop $v_3$ to get $v_5$, and make $v_6 = \text{push}(v_5, 5)$. How many list nodes exist in all? Which node is the top of $v_5$? How many cells would the seven versions need if each were kept as its own array?

3. ◦ Insert the keys $1, 2, \ldots, 7$, in this order, into an empty unbalanced [persistent binary search tree](/persistent-binary-search-tree/) that uses [path copying](/path-copying/). How many nodes does each insert make, and how many in all? Compare with keeping a full copy of every version. Then do the same for the order $4, 2, 6, 1, 3, 5, 7$.

4. ◦ A partially persistent array has four cells, all 0 in version 0, and each cell is a fat node as in the [fat node](/fat-node/) method. Version 1 sets $a[2] = 7$, version 2 sets $a[0] = 1$, version 3 sets $a[2] = 8$, version 4 sets $a[3] = 5$ and version 5 sets $a[2] = 9$. Give $a[2]$ in each of the versions 0 to 5, and the whole array in version 3. How many (version, value) pairs are stored?

5. ◦ Write 11 as a [binary random-access list](/binary-random-access-list/) and as a [skew binary random-access list](/skew-binary-random-access-list/): give the sizes of the trees. Then cons a 12th and a 13th item onto each, and count the links each cons makes. Continue the skew list to 14, 15 and 16 items.

6. ◦ A [banker's queue](/banker-queue/) keeps $|R| \le |F|$ and rotates when a snoc breaks this. Starting from the empty queue, do only snocs. After which snocs does a rotation start? Give the pattern.

7. ◦ Continue the example on the page [real-time queue](/real-time-queue/) from $q_7$, whose sizes $(|f|, |r|, |s|)$ are $(5, 0, 5)$. Push six more items and pop nothing. Give the three sizes after each push, and say which push starts a rotation.

8. ◦ A [retroactive](/retroactive-data-structure/) queue has the timeline: enqueue $a$ at time 1, enqueue $b$ at time 3, dequeue at time 5, dequeue at time 7. What do the dequeues return? Insert "enqueue $c$" at time 0 and answer again, and give the present queue. Then take a priority queue with: insert 5 at time 1, insert 3 at time 2, delete-min at time 3, insert 4 at time 4, delete-min at time 5. Give the present set, then insert "insert 1" at time 2.5 and give the items removed and the new present set.

9. ◦ A [fully persistent array](/fully-persistent-array/) of $n = 1000$ cells is stored as a complete binary tree with the cells at the leaves, and each set uses path copying. How many nodes does one set make at most? After 500 sets on various versions, how many nodes exist at most? How many cells would 501 full copies use?

10. • Let $b = \langle 2, 0, 3, 1, 3, 2 \rangle$, with values in $[0, 4)$. Build a [persistent segment tree](/persistent-segment-tree/) of counts over the values, with version $i$ holding the first $i$ items of $b$. Find the third smallest item of $b[1..5)$ (positions 1 to 4, from 0) using only versions 1 and 5, and show the count compared at each node. How many nodes does the pool hold after all six versions, counting the empty tree?

11. • Use a [persistent trie](/persistent-trie/) on 4-bit keys, with version $i$ holding the first $i$ items of $a = \langle 9, 4, 14, 7, 2 \rangle$ and a count in each node. For $y = 10$, find the item $x$ of $a[1..4)$ that makes $x \oplus y$ largest, where $\oplus$ is bitwise exclusive or. How many trie nodes exist after all five inserts, if the empty version is a single root?

12. • Take the tree with root 8, children 4 and 12, and leaves 2, 6 under 4 and 10, 14 under 12. With a [zipper](/zipper/), run: from_tree, right, left, set_value(11), up, right, set_value(15), top. How many tree nodes does the zipper make, and how many of them are in the final tree? How many would two separate path-copying updates make?

13. • Write 100 as a sum of skew binary weights $2^k - 1$ in the canonical form of the skew binary random-access list, and give the trees. Item 50 (from 0) is looked up: which tree holds it, at which index in that tree, and which steps (left, right) lead to it?

14. • Change the banker's queue so that its rotation is an ordinary function call, with no memoization of the suspended reverse. Give a sequence of operations on persistent versions that costs $\Theta(n)$ per operation, and point to the step of the [debit analysis](/debit-analysis/) that fails.

15. • Points $(1, 3), (2, 1), (4, 4), (5, 2), (6, 0)$ are given. Using [historical queries](/historical-queries/) on a persistent segment tree over $y$, with one version per point in order of $x$, count the points $(x, y)$ with $x \le a$ and $y \le b$ for $(a, b) = (4, 3)$, $(6, 2)$ and $(3, 4)$. State the cost of building and of one query.

16. • A linked list $A \to B \to C \to D$ is made partially persistent by [node copying](/node-copying/) with one extra field per node, and each node has in-degree 1. Version $i$, for $i = 1, \ldots, 16$, sets the value of $D$ to $i$. Which versions copy which nodes? How many copies are made in all, and how does this compare with the amortized bound?

17. • Start from a one-item list $\ell_0$ and make $\ell_{k+1} = \text{cat}(\ell_k, \ell_k)$ for $k < 30$. How many items does $\ell_{30}$ have? If cat makes $O(1)$ new nodes, how many nodes exist? Explain why [confluent persistence](/confluent-persistence/) can make versions exponentially larger than the number of operations.

18. • In a [finger tree](/finger-tree/), the elements at level $k$ are 2-3 trees of height $k$. How many items can one such element hold, at least and at most? Show that a finger tree of $n$ items has depth $O(\log n)$, with an explicit bound.

19. • A fully retroactive counter supports "add $c$ at time $t$", deletion of such an operation, and "value at time $t$". Show how to get $O(\log T)$ per operation when times are integers in $[1, T]$. Run: add 5 at time 2, add $-3$ at time 6, add 4 at time 9; ask the value at time 7; insert "add 10 at time 4" and ask again; delete the add at time 2 and give the present value.

20. • A [persistent vector](/persistent-vector/) has $M = 32$ and $n = 1000$. Give tailoff$(n)$, the shift, and the number of leaves in the trie. Which leaf and slot hold item 500, and how many nodes does set$(v, 500, x)$ copy? How many more pushes, at least, until the trie gains a level?

21. ★ Prove that in the skew binary random-access list the weights are strictly increasing except that the first two may be equal, and that cons and tail keep this invariant with $O(1)$ work in the worst case. Deduce that a list of $n$ items has $O(\log n)$ trees and that lookup takes $O(\log n)$ time.

22. ★ Design a structure that answers, online, the number of distinct values in $a[l..r)$ in $O(\log n)$ time, with $O(n \log n)$ space, using a persistent segment tree over positions. Run it on $a = \langle 1, 2, 1, 3, 2, 1 \rangle$ for $[1, 5)$ and $[0, 3)$.

23. ★ A rooted tree has a value at each node. Answer "the $k$-th smallest value on the path from $u$ to $v$" in $O(\log n)$ time after an $O(n \log n)$ preprocessing, using persistent segment trees and the [lowest common ancestor](/lowest-common-ancestor/).

24. ★ Give a persistent stack in which push is $O(1)$ and the item at depth $k$ can be found in $O(\log n)$ time, by adding to each node a single *jump* pointer to an earlier node. Give the rule that sets the jump pointer, show that jump lengths follow the skew binary weights, and bound the search.

25. ★ In a retroactive priority queue, prove that inserting the operation "insert $x$" at a past time changes the present set by exactly one item, and that the same holds for removing a past "insert". Which item enters the present set in the second half of Exercise 8?

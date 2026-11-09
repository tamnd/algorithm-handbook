1. ◦ Write a tree as (left, key, right). Do a right [rotation](/tree-rotation/) at the root of ((10, 20, 30), 40, 50). Draw the result, say which subtree changes parent, and list the links that change.

2. ◦ Insert 50, 40, 30, 10, 20, 45, 42, in this order, into an empty [AVL tree](/avl-tree/). After each insertion, say whether the tree rotates, where, and whether the rotation is single or double. Draw the final tree.

3. ◦ Count the height of an AVL tree in nodes, so that a single node has height 1. Give the fewest nodes of an AVL tree of height $h$ for $h = 1, \dots, 7$. What is the largest possible height of an AVL tree with 20 nodes?

4. ◦ Which of these trees are [red-black trees](/red-black-tree/)? Give the black-height of the root of each valid tree, and name the broken rule in each invalid one. (a) A black root 20 with children 10 (red) and 30 (black); 10 has black children 5 and 15; 30 has no left child and a red right child 40. (b) A black root 20 with black children 10 and 30; 10 has a red left child 5 and no right child; 30 has black children 25 and 40.

5. ◦ Insert 50, 60, 70, 40, 30, 35, 32, in this order, into an empty red-black tree with the bottom-up insertion of the [red-black tree](/red-black-tree/) entry. For each insertion, name the cases of the fix-up that run and the rotations they do. Draw the final tree with its colors.

6. ◦ Insert 31, 41, 59, 26, 53, 58, 97, 93, in this order, into an empty [2-3 tree](/two-three-tree/). Draw the tree after each split. How many splits happen in all, and how many times does the height grow?

7. ◦ A [2-3-4 tree](/two-three-four-tree/) has the root [30 60] and the three leaves [10 20], [40] and [70 80 90]. Write it as a red-black tree, as in [the correspondence with 2-3-4 trees](/red-black-correspondence-with-2-3-4-trees/), making the red child of every 3-node a left child. What is the black-height of the root?

8. ◦ A [treap](/treap/) holds the keys 1 to 6 with the priorities 12, 45, 7, 30, 58 and 21, in key order; a higher priority sits nearer the root. Draw it. Insert key 7 with priority 50 and say which rotations happen. Then [split](/treap-split/) the result at the key 4 and draw the two treaps.

9. ◦ An [order-statistic tree](/order-statistic-tree/) has the root 41. Its left child 20 has children 11 and 29, and 29 has children 26 and 38. Its right child 65 has children 50 and 72, and 72 has only a right child 99. Write the size of every subtree. Trace SELECT(4), where SELECT(0) is the smallest key, and compute RANK(60), the number of keys less than 60.

10. • In a [weight-balanced tree](/weight-balanced-tree/) with $\Delta = 3$, the weight of a subtree is its number of keys plus one. How many keys can the left subtree of a node with 10 keys hold at most? For $n = 10^6$ keys, compare the height bound $\log_{4/3} \frac{n+1}{2}$ with $2.41 \lg(n + 1)$ and with $\lg(n + 1)$.

11. • Count the height of a red-black tree as the number of internal nodes on the longest path from the root to a nil leaf. Find the fewest internal nodes of a red-black tree of height $h$ for $h = 1, \dots, 10$, and give a formula for even and for odd $h$. Check the tightness claim of the [red-black height theorem](/red-black-height-theorem/).

12. • The root of a red-black tree has [black-height](/black-height/) $b$. Show that the tree has at least $2^b - 1$ and at most $4^b - 1$ internal nodes, and draw trees that reach both bounds for $b = 2$.

13. • Count the [inversions](/inversion/) of an array of $n$ distinct numbers in $O(n \log n)$ time with an order-statistic tree, reading the array once from left to right. Run your method on 4, 1, 3, 5, 2.

14. • Insert 9, 8, 7, 6, 5, 4, 3, 2, 1, in this order, into an empty [scapegoat tree](/scapegoat-tree/) with $\alpha = 2/3$. A rebuild happens when the new node is deeper than $\log_{3/2} q$, counting depth in edges. For each rebuild, give the key just inserted, the scapegoat, and the new root of the rebuilt subtree. Draw the final tree and give its height.

15. • In a [zip tree](/zip-tree/), each rank is $k$ with probability $1/2^{k+1}$, independently. What is the probability that two given nodes have the same rank? Why do zip trees need a rule for ties, while treaps with real priorities do not?

16. • The right spine of a binary search tree is the path from the root along right children. Show that the fewest rotations that turn a tree on $n$ keys into the path of right children is exactly $n$ minus the number of nodes on its right spine. How many does the path of left children need?

17. • An [implicit treap](/implicit-treap/) stores a list of $n$ items. Move the block of items at positions $i$ to $j$ so that it starts at position $p$ of the rest of the list. Use only split by position and [merge](/treap-merge/), and give the expected time.

18. • Show that a 2-3 tree whose leaves are all on level $h$, with the root on level 1, holds at least $2^h - 1$ and at most $3^h - 1$ keys. Deduce the height bounds of the entry.

19. • A treap with distinct random priorities holds the keys $1, \dots, n$. Show that key $j$ is an ancestor of key $i$ with probability $1/(|i - j| + 1)$, and use this to compute the expected depth of key $i$.

20. • Every AVL tree can be colored as a red-black tree. Show that the converse fails: find the smallest binary search tree that has a valid red-black coloring but is not height-balanced, and give the coloring.

21. • Keys are integers in a treap. Give an operation that adds $v > 0$ to every key at least $k$ in $O(\log n)$ expected time, with a lazy tag in each node. Why does the same method fail for $v < 0$?

22. ★ Count AVL heights in nodes, with nil at height 0. Color a node red when its height is odd and its parent's height is even, and black otherwise. Prove that this gives a valid red-black tree for every AVL tree, and find the black-height of a node in terms of its height.

23. ★ Start from an empty red-black tree and do $n$ insertions with the bottom-up fix-up. One insertion can recolor $\Theta(\log n)$ nodes. Show that the total number of recolorings over the $n$ insertions is $O(n)$.

24. ★ Insert $1, 2, \dots, n$ in increasing order into an empty AVL tree. Show that the final height, in nodes, is $\lfloor \lg n \rfloor + 1$, that every left subtree is perfect, and that the tree is perfect when $n = 2^k - 1$.

25. ★ The Fibonacci tree $T_h$ is the empty tree for $h = 0$, a single node for $h = 1$, and for $h \ge 2$ a root with $T_{h-1}$ on the left and $T_{h-2}$ on the right, with keys $1, 2, \dots$ in order. Delete the largest key from $T_5$ and draw each rotation. Then show that deleting the largest key from $T_h$ causes $\lfloor (h - 1)/2 \rfloor$ rotations, so AVL deletion can need $\Theta(\log n)$ rotations.

26. ★ Let $A(h)$ be the number of shapes of AVL trees of height $h$, in nodes, with $A(0) = A(1) = 1$. Show that $A(h) = A(h-1)^2 + 2A(h-1)A(h-2)$ for $h \ge 2$, compute $A(h)$ up to $h = 5$, and show that $\lg A(h) = \Theta(2^h)$.

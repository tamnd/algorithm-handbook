1. ◦ Insert 30, 15, 45, 8, 22, 40, 60, 19, 27, 50, in this order, into an empty [binary search tree](/binary-search-tree/). Draw the tree. What is its height, counted in edges, and which keys are deepest? Which nodes does a [search](/bst-search/) for 25 visit, and where does it stop?

2. ◦ In the tree of exercise 1, give the floor and the ceiling of 25, 42, 5 and 61, as [floor and ceiling in a BST](/bst-floor-and-ceiling/) defines them. Say which answers do not exist.

3. ◦ In the tree of exercise 1, delete 15 and then 30 with [BST deletion](/bst-deletion/). Draw the tree after each step. Do you get the same tree if you delete 30 first?

4. ◦ Insert the keys 1, 2, 3, 4 into an empty binary search tree in each of the 24 possible orders. How many distinct shapes appear? How many orders give a tree of height 3 (in edges), and what is the expected height over all 24 orders?

5. ◦ A [random binary search tree](/random-binary-search-tree/) holds the keys 1 to 7. Give the expected depth of key 1 and of key 4 as exact fractions.

6. ◦ Three keys $k_1 < k_2 < k_3$ are searched with probabilities $0.6$, $0.3$ and $0.1$, and every search succeeds. Count the cost of a search as the number of nodes it visits, as in [expected search cost](/expected-search-cost-bst/). Give the expected cost of each of the five binary search trees on these keys. Which tree is best, and is it balanced?

7. ◦ A [skip list](/skip-list/) holds eight keys, with their levels in parentheses: 4 (2), 7 (1), 10 (3), 13 (1), 16 (2), 20 (1), 23 (3), 27 (1). Write out the list of each level. Search for 21: name the nodes the search moves to, level by level, and say what the search returns. What are the floor and the ceiling of 21?

8. ◦ Build a binary search tree by inserting 6, 4, 8, 2, 5, 1, 3 in this order. [Splay](/splaying/) the node 3 and draw the tree, naming each step (zig, zig-zig or zig-zag). Then splay 8 in the new tree and draw the result.

9. ◦ Turn the tree of exercise 1 into a [threaded binary tree](/threaded-binary-tree/). List each thread and the node it points to. How many threads are there, and which of them are NIL?

10. ◦ A node of a [fusion tree](/fusion-tree/) holds the 5-bit keys 3, 6, 20 and 22. Find the set $D$ of distinguishing positions (bit 0 is the lowest) and the sketch of each key. Check that the sketches are in the same order as the keys. Then compute the sketch of the query 2 and explain why the rank of the sketch alone gives the wrong predecessor.

11. • Show that the preorder sequence of a binary search tree determines the tree. Rebuild the tree whose preorder is 30, 15, 8, 22, 19, 27, 45, 40, 60, 50, and give a method that rebuilds a tree of $n$ keys from its preorder in $O(n)$ time.

12. • Show that the number of insertion orders of $n$ distinct keys that build a given binary search tree $T$ is $n! / \prod_{x} s(x)$, where $s(x)$ is the number of nodes in the subtree of $x$. How many orders build the perfect tree on the keys 1 to 7? How many build the tree of exercise 1?

13. • Two keys of a binary search tree have been swapped by mistake, so the tree is no longer a search tree. Give a method that finds the two keys and swaps them back in $O(n)$ time and $O(h)$ extra space.

14. • Write a procedure that reports all keys of a binary search tree that lie in $[a, b]$, in sorted order. Show that it runs in $O(h + k)$ time, where $k$ is the number of keys reported.

15. • Show that the expected number of leaves of a random binary search tree on $n \ge 2$ keys is $(n + 1)/3$. Use the rule that key $j$ is an ancestor of key $i$ exactly when $j$ comes first in the insertion order among the keys between them.

16. • In a skip list with $p = 1/2$ and $n$ keys, let $L$ be the highest level of a node. Show that $\Pr[L > k] \le n 2^{-k}$, that $\mathbb{E}[L] \le \lceil \lg n \rceil + 2$, and that $L \le 2 \lg n$ with probability at least $1 - 1/n$.

17. • The skip-list analysis shows that a search makes about $(1/p) \log_{1/p} n$ steps. Write this as $c(p) \lg n$. Compute $c(1/2)$ and $c(1/4)$, and find the $p$ that minimizes $c(p)$. Which of $p = 1/2$ and $p = 1/4$ would you choose, given that a node has $1/(1 - p)$ pointers on average?

18. • A greedy method builds a search tree by putting the most probable key at the root and recursing on each side. Show that it is not optimal, using three keys with probabilities $0.34$, $0.33$ and $0.33$ and the cost of exercise 6. Give the cost of the greedy tree and of the optimal one.

19. • Run the [optimal BST dynamic program](/optimal-bst-dynamic-programming/) on four keys with probabilities $0.1$, $0.2$, $0.4$ and $0.3$ and no failed searches, counting nodes visited. Give the optimal tree, its expected cost, and the root it chooses for each interval of keys.

20. • A splay tree holds $n$ keys. A program accesses $k$ of them in a fixed cyclic order, $x_1, \ldots, x_k, x_1, \ldots, x_k, \ldots$, for $m$ accesses in all. Use the [working set theorem](/working-set-theorem/) to bound the total cost. How does the bound compare with that of the [balance theorem](/splay-tree/), $O((m + n) \log n)$?

21. • An [ordered set](/ordered-set/) gives you only contains, rank and select, with rank counting the keys smaller than $k$ and select counting from 0. Write floor and ceiling with at most one call to each. Take care with the cases where the answer does not exist.

22. • A sorted array of $n$ keys and a finger, an index $f$, are given. Show that a search for a key at index $f + d$ can be done in $O(\log d)$ comparisons by [exponential search](/exponential-search/) from the finger. Why does this not give a [finger search tree](/finger-search-tree/), that is, why is a sorted array not enough?

23. • Delete a key chosen uniformly at random from a random binary search tree on 3 keys, with the method of [BST deletion](/bst-deletion/). Show that the result has its larger key at the root with probability $5/9$, so the result is not a random binary search tree on 2 keys.

24. • Show that a binary search tree on $n$ keys has total depth at least $\sum_{i=1}^{n} \lfloor \lg i \rfloor$, and that this bound is reached. What is the least average number of nodes visited by a successful search in a tree of 10 keys, all keys equally likely?

25. ★ Change the deletion of exercise 23 in one case: when the node has a right child, always replace it by its successor, even if it has no left child; delete it by its left child only when it has no right child. Show that deleting a uniformly random key from a random binary search tree on $n$ keys with this method gives a random binary search tree on $n - 1$ keys.

26. ★ Insertion into a random binary search tree on $n$ keys can keep it random whatever the key: with probability $1/(n + 1)$, split the tree at the new key $x$ and make $x$ the root, with the two parts as its subtrees; otherwise insert $x$ by the same rule into the subtree of the root where it belongs. Show that the result is a random binary search tree on $n + 1$ keys. You may use that splitting a random BST at any key gives two independent random BSTs.

27. ★ The keys are $w$-bit integers. Store, for each length $\ell$ from 0 to $w$, a [hash table](/hash-table/) of the length-$\ell$ prefixes of the keys, each with the smallest and the largest key that starts with it, and keep the keys in a sorted linked list. Show how to answer a predecessor query in $O(\log w)$ expected time. How much space does the structure use?

28. ★ Reduce the space of the structure of exercise 27 to $O(n)$ while keeping $O(\log w)$ expected time per predecessor query. Use groups of about $w$ consecutive keys.

29. ★ Insert $n$ keys in increasing order into an initially empty 2-3 tree with level links, starting each insertion from a finger at the last key inserted. Show that the total time is $O(n)$, although a single insertion can split $\Theta(\log n)$ nodes.

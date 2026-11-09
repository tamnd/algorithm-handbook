2. Five list nodes, one for each push. Popping $v_3$ returns 3 and the node of 2, which is the top of $v_2$, so $v_5$ is $v_2$ and makes no node. $v_6$ is $[5, 2, 1]$. As separate arrays the versions have $0 + 1 + 2 + 3 + 3 + 2 + 3 = 14$ cells.

3. In increasing order each new key goes to the right end, so insert $i$ copies the whole path of $i - 1$ nodes and adds one: $1 + 2 + \cdots + 7 = 28$ nodes, exactly as many as seven full copies. In the order $4, 2, 6, 1, 3, 5, 7$ the paths have $1, 2, 2, 3, 3, 3, 3$ nodes, 17 in all, while full copies still need 28.

4. $a[2]$ is $0, 7, 7, 8, 8, 9$ in versions 0 to 5. Version 3 is $\langle 1, 0, 8, 0 \rangle$. There are $4 + 5 = 9$ pairs: one initial pair per cell and one per write.

5. Binary: $11 = 1 + 2 + 8$. The 12th cons links $1 + 1$ and then $2 + 2$, two links, giving trees of sizes 4 and 8; the 13th adds a tree of size 1 with no link. Skew: $11 = 1 + 3 + 7$. The 12th cons adds a singleton, giving $1, 1, 3, 7$ with no link; the 13th links the two trees of size 1 under a new root, giving $3, 3, 7$ with one link. Then 14 is $7, 7$, 15 is $15$ and 16 is $1, 15$.

7. $(5, 1, 4)$, $(5, 2, 3)$, $(5, 3, 2)$, $(5, 4, 1)$, $(5, 5, 0)$. The sixth push makes $|r| = 6 = |f| + 1$ with an empty schedule, so it starts a rotation, and the sizes become $(11, 0, 11)$.

8. Queue: the dequeues return $a$ and $b$. With "enqueue $c$" at time 0 they return $c$ and $a$, and the present queue is $[b]$. Priority queue: the delete-mins remove 3 and 4, and the present set is $\{5\}$. With "insert 1" at time 2.5 they remove 1 and 3, and the present set is $\{4, 5\}$: one item more.

10. At the root, the left half holds the values 0 and 1: version 5 counts 2 of them and version 1 counts 0, so $c = 2 < 3$; go right with $k = 1$. At the node of $[2, 4)$, the left child is the value 2, counted once in both versions, so $c = 0 < 1$; go right. The answer is 3. The empty tree has 7 nodes and each insert copies a path of 3, so the pool holds $7 + 6 \cdot 3 = 25$ nodes.

13. $100 = 3 + 3 + 31 + 63$. The first three trees hold items 0 to 36, so item 50 is index 13 of the tree of 63. In a tree of size $2^k - 1$, index 0 is the root, the left subtree holds the next $2^{k-1} - 1$ indices and the right subtree the rest. The steps are left, left, right, left, right.

16. The copies follow the carries of a binary counter. $D$ is copied in every even version, $C$ in versions 4, 8, 12 and 16, $B$ in 8 and 16, and $A$ in 16, which then becomes the entry of version 16. That is $8 + 4 + 2 + 1 = 15$ copies for $u = 16$ changes, inside the bound $(k + 1 - p)\,C \le u$ with $k = p = 1$.

20. tailoff$(1000) = 992$, so the trie has 31 full leaves and shift 5, and the tail holds 8 items. Item 500 is in leaf $\lfloor 500/32 \rfloor = 15$, slot $500 \bmod 32 = 20$; the set copies the root and that leaf. The trie can hold 32 leaves at shift 5, so it gains a level when the tail is full and 32 leaves are already in it, at $n = 1056$: the 57th push from now.

22. Let version $r$ be the tree over positions in which position $i < r$ holds 1 when $i$ is the last occurrence of $a[i]$ in $a[0..r)$. Going from version $r$ to $r + 1$ sets position $r$ to 1 and clears the previous occurrence of $a[r]$, two path copies. The answer for $[l, r)$ is the sum over $[l, r)$ in version $r$. On the example the answers are 3 and 2.

23. Let the version of a node be the version of its parent with the value of the node added, so it counts the values on the path from the root. With $w$ the lowest common ancestor of $u$ and $v$ and $p$ its parent, the count of a value range on the path is $c_u + c_v - c_w - c_p$. Descend the four trees together as in the range $k$-th smallest query.

24. When pushing $u$ on $p$, let $j$ be the jump of $p$. If $p$ and $j$ both have jumps and the jump from $p$ is as long as the jump from $j$, set the jump of $u$ to the jump of $j$; otherwise set it to $p$. The jump lengths along a chain are $1, 1, 3, 1, 1, 3, 7, \ldots$, the skew binary weights. To find depth $d$, take the jump while it does not go above depth $d$ and the parent otherwise.

25. Compare the old and the new timeline after the inserted operation. Show by induction over time that the new set equals the old set plus one extra item. An insert keeps the same extra item. A delete-min either removes the same item in both, or, if the extra item is smaller than the old minimum, removes the extra item, and the old minimum becomes the new extra. In Exercise 8 the item that enters is 4.

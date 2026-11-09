1. The left child 20 becomes the root: (10, 20, (30, 40, 50)). The subtree of 30 moves from 20 to 40. Three links change: the root pointer now points to 20, the right child of 20 is 40, and the left child of 40 is 30.

2. Inserting 30 makes 50 left-heavy by two, with the new key on the outside: a single right rotation at 50. Inserting 20 puts it right of 10 below 30: a double rotation at 30, left at 10 and then right at 30. Inserting 42 makes 50 unbalanced again: a single right rotation at 50. The other insertions do not rotate. The final tree is ((10, 20, 30), 40, (42, 45, 50)), which is perfect.

3. The counts follow $N(h) = N(h-1) + N(h-2) + 1$: 1, 2, 4, 7, 12, 20, 33. A tree of height 7 needs 33 nodes, so an AVL tree with 20 nodes has height at most 6, and the bound is reached.

4. Tree (a) is valid, and the root has black-height 2. Tree (b) is not: the path from 20 through 10 to a nil leaf has 2 black nodes below the root, and the path through 30 and 25 has 3.

5. Inserting 70: case 3, a left rotation at 50. Inserting 40: case 1, a recoloring only. Inserting 30: case 3, a right rotation at 50. Inserting 35: case 1. Inserting 32: case 2, a right rotation at 35, then case 3, a left rotation at 30. The final tree is (((30r, 32b, 35r), 40r, 50b), 60b, 70b), where r and b are the colors, with four rotations in all.

6. The root splits when 59 arrives: 41 over [31] and [59]. Inserting 58 splits [53 58 59]: the root becomes [41 58] over [26 31], [53] and [59]. Inserting 93 splits [59 93 97], and then the root [41 58 93] splits: 58 over 41 and 93, with leaves [26 31], [53], [59] and [97]. There are four splits, and the height grows twice.

7. The root is 60, black, with a red left child 30. Node 30 has black children 20 and 40, and 20 has a red left child 10. The right child of 60 is 80, black, with red children 70 and 90. The black-height of the root is 2, the height of the 2-3-4 tree.

8. Key 5 has the highest priority, so it is the root: ((1, 2, (3, 4, nil)), 5, 6). Key 7 goes to the right of 6, and one left rotation at 6 lifts it: ((1, 2, (3, 4, nil)), 5, (6, 7, nil)). The split gives (1, 2, 3), rooted at 2, and (4, 5, (6, 7, nil)), rooted at 5.

9. The sizes are 10 at 41, 5 at 20, 3 at 29, 4 at 65, 2 at 72, and 1 at each leaf. SELECT(4): at 41 the left size is 5, so go left; at 20 the left size is 1, so go right with $i = 4 - 2 = 2$; at 29 the left size is 1, so go right with $i = 0$; at 38 the left size is 0, and the answer is 38. RANK(60) = 7: the keys 11, 20, 26, 29, 38, 41 and 50.

11. A shortest tree of height $2j$ is a path of alternating black and red nodes, with every other subtree as small as the black counts allow. The counts are 1, 2, 4, 6, 10, 14, 22, 30, 46, 62: $2^{j+1} - 2$ for $h = 2j$ and $3 \cdot 2^j - 2$ for $h = 2j + 1$.

14. Three rebuilds. After 5: the scapegoat is 8, and the subtree on 5 to 8 is rebuilt with root 7. After 3: the scapegoat is 6, rebuilt with root 5. After 1: the scapegoat is 4, rebuilt with root 3. The final tree is (((((1, 2, nil), 3, 4), 5, 6), 7, 8), 9, nil), of height 5.

19. Key $j$ is an ancestor of key $i$ exactly when $j$ has the highest priority among the $|i - j| + 1$ keys between them, both included. Summing over $j \ne i$ gives $H_i + H_{n-i+1} - 2$.

22. Prove by induction on height that the black-height of a node of height $h$ is $\lceil h/2 \rceil$. A child of height $h - 1$ is red exactly when $h$ is even, and a child of height $h - 2$ is always black; check that both cases give the same count. A red node has odd height. Its children are black: a child of even height because only odd heights are red, and a child of odd height because its parent's height is odd.

23. Count the red nodes. An insertion adds one. Case 1 paints two nodes black and one red, so it removes one. Cases 2 and 3 do not change the count, and painting the root black at the end can only lower it. The count never goes below zero.

24. Show by induction that after each insertion the tree is a right spine whose left subtrees are all perfect. A rotation can happen only at a spine node whose right child has a perfect left subtree of the same height as its own left subtree, and the single left rotation there makes a larger perfect tree.

25. In $T_5$, deleting 12 leaves 11 with a left subtree of height 2 and no right child: a right rotation at 11. Then the root 8 has subtrees of heights 4 and 2: a right rotation at 8. In general, deleting the maximum from $T_{h-2}$ lowers its height by one, and then the root of $T_h$ needs one single rotation, so the count $r(h)$ satisfies $r(h) = r(h-2) + 1$ with $r(1) = r(2) = 0$.

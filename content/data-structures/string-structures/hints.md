1. The nodes are the root and the 14 distinct nonempty prefixes of the keys, so 15 nodes, $15 \cdot 26 = 390$ links and 14 of them not null. Deleting $\texttt{toolbox}$ removes the three nodes below $\texttt{tool}$ and leaves 12. Deleting $\texttt{top}$ only clears the value of its node, which still leads to $\texttt{topaz}$, so 15 nodes stay.

2. The nodes are the root, $\texttt{t}$, $\texttt{to}$, $\texttt{too}$, $\texttt{top}$, $\texttt{tea}$, $\texttt{tool}$, $\texttt{tooth}$, $\texttt{toolbox}$ and $\texttt{topaz}$: 10 nodes, against the bound 12. The edges below $\texttt{t}$ are $\texttt{ea}$ and $\texttt{o}$, and the longest labels are $\texttt{box}$ and $\texttt{az}$. After deleting $\texttt{top}$, its node has one child and no key, so it merges with $\texttt{topaz}$ into one edge $\texttt{paz}$ from $\texttt{to}$, and 9 nodes remain.

3. The tree has 14 nodes. get($\texttt{topaz}$) takes 6 comparisons, with one right step at $\texttt{o}$ against $\texttt{p}$. get($\texttt{tea}$) takes 4, with one left step. The miss get($\texttt{toot}$) takes 4 and ends at a node with no value; get($\texttt{ten}$) takes 4 and falls off the right link of the node $\texttt{a}$.

5. The leaves are $\texttt{data\_}$, $\texttt{struc}$, $\texttt{tures}$, $\texttt{\_and\_}$, $\texttt{algor}$, $\texttt{ithms}$, and the tree is $(((\texttt{data\_}\ \texttt{struc})\ \texttt{tures})\ ((\texttt{\_and\_}\ \texttt{algor})\ \texttt{ithms}))$ of height 3, with 15 characters on the left. CHAR-AT$(17)$ goes right with $i = 2$, then left twice, and returns character 2 of $\texttt{\_and\_}$, which is $\texttt{n}$.

6. The final pieces are $(add, 0, 4)$, $(orig, 4, 7)$, $(add, 8, 1)$, for the text $\texttt{fat cat sat.}$ and the add buffer $\texttt{fat big .}$. The second insert makes no piece: it starts where the piece $(add, 0, 4)$ ends, and that piece ends at the end of the add buffer, so the piece grows to $(add, 0, 8)$.

7. $\mathit{base} = [1, -1, 1, 4, 7, 9, 10, -4, 9, -2, -3, 12, -5]$ and $\mathit{check} = [\text{root}, 2, 0, 0, 0, 3, 3, 4, 4, 5, 6, 8, 11]$, 13 cells and none free. $\texttt{cab}$ goes through the cells 4, 8, 11 and ends at the leaf cell 12, which holds $-5$, the value 4. For $\texttt{ca}$ the end code leads to cell $9$, whose check is 5 and not 8, so $\texttt{ca}$ is not a key.

8. $B = \texttt{101101101011010100000}$, 21 bits for 10 nodes. The group of node 1 is $B[5 \ldots 6]$, after the second 0, and there are three 1s before position 5, so its children are nodes 3 and 4; the label $\texttt{o}$ gives node 4, $\texttt{co}$. The tenth 1 is at position 15, with six 0s before it, so the parent of node 9 is node 5, $\texttt{do}$.

14. Count the edges two ways. When all keys are at leaves and every inner node has at least two children, there are fewer inner nodes than leaves. For the tight case, make the root have one child, for example with the keys $\texttt{a}\texttt{b}^i\texttt{c}$ for $0 \le i \le n - 2$ and $\texttt{a}\texttt{b}^{n-1}$.

16. A tree of height $h$ under the AVL rule has at least $F_{h+2}$ leaves. There are 15625 leaves, and $F_{21} = 10946 \le 15625 < F_{22} = 17711$, so the height is at most 19. A perfectly balanced tree has height $\lceil \lg 15625 \rceil = 14$.

20. At depth $d$ the walk is at every node whose path agrees with the fixed symbols among the first $d$ positions. With the two wildcards at the end the count is $1 + 1 + 1 + 26 + 676 = 705$; at the start it is $1 + 26 + 676 + 676 + 676 = 2055$.

22. An occurrence at position $i$ contains the next multiple of $k$, at $i + j$ with $0 \le j < k$. Search the tree for $P[j \ldots m - 1]$ for each $j$, and check the first $j$ symbols of each candidate in the text.

23. A document occurs in rows $[lo, hi]$ exactly when one of its rows $r$ there has $C[r] < lo$, and then exactly one does. So the answer is the number of rows $r$ in $[lo, hi]$ with $C[r] < lo$, which is the [distinct count query](/range-distinct-count-query/) of Chapter 3.7. A persistent segment tree or a wavelet tree answers it in $O(\log n)$ time.

24. Store a reverse bit in each node, meaning that the subtree must be read mirrored. Before any operation goes into a node, swap its children, flip the bits of both, and clear its own bit; a leaf with the bit set is read from its end. For REVERSE, split twice, flip the bit of the middle rope, and concatenate again.

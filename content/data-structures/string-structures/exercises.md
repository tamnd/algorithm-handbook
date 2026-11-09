1. ◦ Put the keys $\texttt{tooth}$, $\texttt{tea}$, $\texttt{toolbox}$, $\texttt{top}$, $\texttt{tool}$ and $\texttt{topaz}$ into a [trie](/trie/). How many nodes does it have, counting the root? With an array of 26 links in each node, how many links are there, and how many of them are not null? How many nodes are left after deleting $\texttt{toolbox}$? How many after deleting $\texttt{top}$ instead?

2. ◦ Draw the [radix tree](/radix-tree/) of the six keys of exercise 1, with the label of each edge. How many nodes does it have, and how does this compare with the bound $2n$? Delete $\texttt{top}$: which nodes merge, and what is the label of the new edge?

3. ◦ Insert the six keys of exercise 1 into a [ternary search tree](/ternary-search-tree/) in the order $\texttt{tooth}$, $\texttt{tea}$, $\texttt{toolbox}$, $\texttt{top}$, $\texttt{tool}$, $\texttt{topaz}$. How many nodes does it have? Counting one comparison for each node visited, how many comparisons do get($\texttt{topaz}$) and get($\texttt{tea}$) take, and how many do the misses get($\texttt{toot}$) and get($\texttt{ten}$) take?

4. ◦ Put the same keys, in the same order, into a [hybrid TST](/hybrid-tst/) over the 26 lowercase letters. How many table cells are used, and how many TST nodes are there in all? How many comparisons do get($\texttt{topaz}$) and get($\texttt{tea}$) take now?

5. ◦ A [rope](/rope/) is built from $\texttt{data\_structures\_and\_algorithms}$ (30 characters) with leaves of at most $L = 5$ characters, by cutting the text into leaves and building a perfectly balanced tree whose left subtree gets the larger half of the leaves. Write the tree, its height and the length stored at the root's left child. Follow CHAR-AT$(17)$ from the root and give the character it returns.

6. ◦ A [piece table](/piece-table/) is loaded with $\texttt{the cat sat}$. Apply, in order: insert $\texttt{fat }$ at position 4; insert $\texttt{big }$ at position 8; delete 4 characters at position 0; insert $\texttt{.}$ at position 15; delete 4 characters at position 4. After each step give the text, the add buffer and the list of pieces $(b, s, \ell)$. Which step makes no new piece, and why?

7. ◦ Build the [double-array trie](/double-array-trie/) of the keys $\texttt{a}$, $\texttt{ba}$, $\texttt{bb}$, $\texttt{c}$, $\texttt{cab}$ with the values 0 to 4. Use the codes $\texttt{a} = 1$, $\texttt{b} = 2$, $\texttt{c} = 3$ and 0 for the end of a key, place the nodes in breadth-first order with children in order of code, take for each node the smallest base $b \ge 1$ that fits all its children, and store $-(i + 1)$ in the leaf cell of the key with value $i$. Give the arrays $\mathit{base}$ and $\mathit{check}$. Follow the lookups of $\texttt{cab}$ and of $\texttt{ca}$.

8. ◦ Write the LOUDS bit string $B$ of the [LOUDS trie](/louds-trie/) of the keys $\texttt{car}$, $\texttt{cat}$, $\texttt{cow}$, $\texttt{do}$, $\texttt{dog}$, with the nodes numbered in breadth-first order from 0 and children in alphabetical order, and with the prefix $\texttt{10}$ for the root. How many bits does it have? Use rank and select on $B$ to find the child of node 1 ($\texttt{c}$) by the label $\texttt{o}$, and the parent of node 9.

9. • Build the [position heap](/position-heap/) of $T = \texttt{abbabba}$: insert the suffixes from position 6 down to 0, each adding the shortest of its prefixes that is not yet a node. List the nodes with their positions. Then run SEARCH for $\texttt{abb}$ and for $\texttt{bab}$, saying which positions are checked against the text and which are reported without a check.

10. • Put the six keys of exercise 1, in the same order, into a [burst trie](/burst-trie/) with the limit $L = 2$, where a container bursts when it holds more than $L$ strings. Give the access nodes and the containers after each burst and at the end. How many bursts happen? Compare the number of access nodes with the 15 nodes of the plain trie.

11. • Insert $\texttt{team}$, $\texttt{tear}$, $\texttt{tell}$, $\texttt{ten}$, $\texttt{tent}$ and $\texttt{test}$, each with a terminating 0 byte, into an [adaptive radix tree](/adaptive-radix-tree/) with path compression and lazy expansion. How many inner nodes does it have, and what are their layouts, prefixes and children? Then insert $\texttt{text}$, delete $\texttt{tell}$ and delete $\texttt{test}$, and give the layout of the root after each step, with the shrink threshold of 3 children for a Node16.

12. • In [Muthukrishnan's document listing](/muthukrishnan-document-listing/), the rows $0, \ldots, 9$ of a suffix array have the documents $D = [0, 1, 0, 2, 1, 0, 1, 2, 2, 0]$. Compute the array $C$, where $C[r]$ is the last row before $r$ with the same document, or $-1$. A pattern has the rows $[2, 8]$. Run the listing with range minimum queries on $C$: in what order are the documents reported, and how many queries are made? Compare with the bound $2d + 1$.

13. • The [LZ-index](/lz-index/) keeps a trie of the phrases of the LZ78 parsing, in which each phrase is the longest earlier phrase that matches, extended by one symbol. Parse $\texttt{abaababbabbba}$ and give the phrases and the number of nodes of the phrase trie. How many phrases does $\texttt{a}^{21}$ have, and about how many does $\texttt{a}^n$ have?

14. • Show that if no key is a prefix of another and the keys do not all begin with the same symbol, a radix tree of $n \ge 2$ keys has at most $2n - 1$ nodes. Then, for every $n \ge 2$, give $n$ keys, none a prefix of another, whose radix tree has exactly $2n$ nodes.

15. • Show that a ternary search tree with no dead nodes has exactly one node for each node of the trie of the same keys, except the root. Then insert the 26 one-letter keys $\texttt{a}, \ldots, \texttt{z}$ in alphabetical order: how many comparisons does get($\texttt{z}$) take? What is the smallest possible worst case over all insertion orders?

16. • A rope holds $10^6$ characters in full leaves of $L = 64$ characters. What is the largest height it can have under the AVL rule of the rope, and what height would a perfectly balanced tree over the same leaves have?

17. • On the rope of exercise 5, run SPLIT$(12)$ with the CONCAT and AVL BALANCE of the rope entry. Give the two trees and their heights. Then compute CONCAT of the second tree with the first, which moves the first 12 characters to the end, and give its tree and height.

18. • Insert the key $\texttt{bc}$ with the value 5 into the double array of exercise 7. Its cell is taken, so use this rule: move all children of the node being extended, together with the new child, to the smallest base where they all fit (old cells still count as taken), copy their bases, fix the $\mathit{check}$ of every cell that pointed to a moved cell, and free the old cells. Give the new arrays, and check the lookups of all six keys.

19. • Add undo to the piece table. Show that each insert or delete replaces a run of consecutive pieces by at most three pieces, and say what must be stored for each edit so that undo restores the old list in time proportional to the length of that run, after a FIND. Why do the buffers never need to change on undo?

20. ★ A trie holds all $R^m$ strings of length $m$ over $R$ symbols, and the pattern of [wildcard matching](/wildcard-matching-in-trie/) has $k$ wildcards. Show that the walk visits $\sum_{d=0}^{m} R^{w_d}$ nodes, where $w_d$ is the number of wildcards among the first $d$ positions. Where should the wildcards be to make the walk shortest and longest? Give both counts for $R = 26$, $m = 4$ and $k = 2$.

21. ★ In the LOUDS bit string with the prefix $\texttt{10}$, prove that the $j$-th 1 of $B$, counting from 1, stands for node $j - 1$, and that the children of node $x$ are written between the $(x + 1)$-th and the $(x + 2)$-th 0. Derive from this the formulas for the first child and the parent with rank and select.

22. ★ A [sparse suffix tree](/sparse-suffix-tree/) holds only the suffixes that start at the multiples of $k$. Show how to find all occurrences of a pattern of length $m \ge k$ in $O(km + kc)$ time, where $c$ is the number of candidates found in the tree, and why $m \ge k$ is needed.

23. ★ Using the array $C$ of document listing, show how to count the distinct documents that contain a pattern, without listing them, in $O(\log n)$ time after the range of the pattern is found. Bound the space of your structure.

24. ★ Extend the rope with REVERSE$(i, j)$, which reverses the characters at positions $i$ to $j - 1$, in $O(\log n + L)$ time, while CHAR-AT, SPLIT and CONCAT keep their bounds. What must each node store, and when is that information pushed down?

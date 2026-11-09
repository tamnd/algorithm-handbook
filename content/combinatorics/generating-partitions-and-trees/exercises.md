1. ◦ Find the [conjugate partition](/conjugate-partition/) of $\lambda = (6, 4, 4, 2, 1)$, the side of its [Durfee square](/durfee-square/), and its Frobenius coordinates $(\lambda_1 - 1, \ldots, \lambda_d - d \mid \lambda'_1 - 1, \ldots, \lambda'_d - d)$.

2. ◦ Glaisher's map in [Euler's partition theorem](/euler-partition-theorem/) writes the multiplicity $c$ of each odd part $j$ in binary, $c = \sum 2^e$, and replaces the $c$ copies of $j$ by the distinct parts $2^e j$. Its inverse splits each even part $2^e j$, with $j$ odd, into $2^e$ parts $j$. Apply the map to the partition $(5, 5, 5, 3, 1, 1, 1, 1, 1, 1, 1)$ of 25 into odd parts, and the inverse map to the partition $(12, 9, 6, 2)$ of 29 into distinct parts.

3. ◦ Run [Algorithm P](/integer-partition-generation/) for $n = 6$ and write down the eleven partitions in the order it visits them. Which partition follows $(3, 3)$? How many of the ten steps take the short branch, where the last part larger than 1 is a 2?

4. ◦ Use the hook length formula from [standard Young tableaux](/standard-young-tableaux/) to count the standard tableaux of shape $(4, 2, 1)$ and of shape $(3, 3, 3)$.

5. ◦ Write the [restricted growth string](/restricted-growth-string/) of the set partition $\{1, 3\}, \{2, 4\}, \{5\}, \{6\}$ of $[6]$. Apply the lexicographic successor of [set partition generation](/set-partition-generation/) to it, and give the set partition that the new string stands for.

6. ◦ Apply the [successor rule for balanced brackets](/next-balanced-bracket-sequence/) to the word `(()())(())`. At which position does the scan from the right stop, and what is the next word?

7. ◦ In [Zaks' algorithm](/zaks-tree-generation/) a $t$-ary tree with $n$ internal nodes is coded by its z-sequence, the increasing positions of the internal nodes in preorder, with $z_i \le t(i - 1) + 1$. For $t = 2$, find the successor of the z-sequence $1\,2\,5\,7$. For $t = 3$ and $n = 4$, how many z-sequences are there, and which are the first and the last?

8. ◦ Run [Prüfer decoding](/pruefer-decoding/) on the code $(2, 6, 2, 5)$ with $n = 6$. List the edges in the order they are produced, and name the vertex of largest degree.

9. ◦ The [level sequence](/level-sequence/) $0\,1\,2\,1\,2\,3\,2$ lists the depths of a rooted tree in preorder. Find the canonical level sequence of the same tree, the largest over all orders of the children.

10. • Count the partitions of 12 with parts at most 3 by the recurrence $p(n, k) = p(n, k - 1) + p(n - k, k)$, where $p(n, k)$ counts the partitions of $n$ with parts at most $k$. Explain with the [Ferrers diagram](/ferrers-diagram/) why the partitions of 12 into at most 3 parts have the same count.

11. • List the self-conjugate partitions of 16. Match each one with a partition of 16 into distinct odd parts by reading off the hooks along the diagonal.

12. • How many partitions of 13 have a Durfee square of side 3? Find also the counts for sides 1 and 2, and check that the three counts add up to $p(13)$, using the [partition function](/integer-partition-function/).

13. • Number the partitions of 12 from 0 in the order of Algorithm P. Find the rank of $(5, 3, 2, 1, 1)$, and the partition of rank 40. Use the counts of partitions of $m$ with parts at most $k$, in the manner of [ranking and unranking](/ranking-unranking/).

14. • A naive generator lists all [integer compositions](/integer-compositions/) of $n$ and keeps those that are non-increasing. How many compositions does it look at for each partition it keeps, for $n = 20$ and for $n = 50$? Is the method output polynomial in the sense of [output-sensitive generation](/output-sensitive-generation/)?

15. • Find the rank, counting from 0, of the restricted growth string $0\,1\,0\,2\,0\,0$ among the 203 strings of length 6 in lexicographic order. You need the number of ways to complete a prefix of length $i$ with maximum $m$.

16. • How many [set partitions](/set-partitions/) of $[6]$ have no block of size 1? Of $[7]$? Use inclusion and exclusion over the set of singletons, with the Bell numbers.

17. • A maximal chain in the [partition lattice](/partition-lattice/) $\Pi_n$ goes from the partition into singletons to the one-block partition by merging two blocks at a time. Show that $\Pi_n$ has $n!\,(n-1)!/2^{n-1}$ maximal chains, and find the number for $n = 4$ and $n = 5$.

18. • A set partition is crossing if there are $a < b < c < d$ with $a, c$ in one block and $b, d$ in another. Find the only crossing partition of $[4]$, and count the crossing partitions of $[5]$ and $[6]$. Use the fact that the non-crossing partitions of $[n]$ number $C_n$, the Catalan number of [Dyck words](/dyck-word/).

19. • Split the $6^4 = 1296$ [labeled trees](/labeled-tree-generation/) on $[6]$ by their number of leaves. Use the fact that a vertex is a leaf exactly when it does not appear in the Prüfer code.

20. • For even $n$, Otter's formula gives the number of free trees with $n$ nodes as $t_n = r_n - \frac12\bigl(\sum_{i=1}^{n-1} r_i r_{n-i} - r_{n/2}\bigr)$, where $r_i$ counts rooted trees with $i$ nodes. Compute $t_8$ from the counts of [rooted tree generation](/rooted-tree-generation/), $r_1, \ldots, r_8 = 1, 1, 2, 4, 9, 20, 48, 115$, and compare it with [free tree generation](/free-tree-generation/).

21. • The 11 graphs on 4 vertices, listed by [graph generation](/graph-generation/), stand for the $2^6 = 64$ labeled graphs. For each class, find the number of labeled graphs in it, and check the sum.

22. ★ Prove Franklin's theorem: the number of partitions of $n$ into an even number of distinct parts minus the number into an odd number of distinct parts is $(-1)^j$ when $n = j(3j \pm 1)/2$ and 0 otherwise. Check it for $n = 7$, $8$ and $12$. Explain how it yields the recurrence for $p(n)$.

23. ★ Show that the number of [ordered trees](/ordered-tree-generation/) with $n$ nodes and $k$ leaves is $\frac1n \binom{n}{k}\binom{n-2}{k-1}$, using the [cycle lemma](/cycle-lemma/). List the counts for $n = 7$.

24. ★ Show that vertex 1 has degree $k$ in exactly $\binom{n-2}{k-1}(n-1)^{n-1-k}$ labeled trees on $[n]$. Give the counts for $n = 7$, the average degree of vertex 1, and the limit, as $n \to \infty$, of the fraction of trees in which vertex 1 is a leaf.

25. ★ A free tree with an even number $n = 2m$ of nodes may have two [centroids](/centroid/), joined by an edge that splits the tree into two halves of $m$ nodes. Show that the number of such trees is $r_m(r_m + 1)/2$, where $r_m$ counts rooted trees with $m$ nodes. How many of the 23 free trees with 8 nodes, and of the 6 with 6 nodes, have two centroids? A generator that roots each free tree at its centroid must treat these trees apart; say what rule makes the choice of root canonical.

26. ★ Count the graphs on 5 vertices up to isomorphism with the [Burnside lemma](/burnside-lemma/). For each cycle type of $S_5$, find the number of cycles it induces on the 10 vertex pairs, and sum $2^{\text{cycles}}$ over the group.

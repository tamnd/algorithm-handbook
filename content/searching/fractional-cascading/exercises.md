1. ◦ Let $C_1 = (3, 11, 19, 30)$, $C_2 = (1, 8, 15, 22, 27)$ and $C_3 = (4, 9, 14, 25, 33, 40)$. Solve [multiple list search](/multiple-list-search/) for $x = 16$ and for $x = 26$: give the successor of $x$ in each list.

2. ◦ Build the augmented lists $M_3$, $M_2$ and $M_1$ for the catalogs of Exercise 1 with the rule of the [bridge](/fractional-cascading-bridge/) entry: $M_3$ is $C_3$ followed by $+\infty$, and $M_i$ is the merge of $C_i$ with the elements at odd positions of $M_{i+1}$ and its final $+\infty$. Mark the bridges, and compare the total size with the bound $2n + k + 1$.

3. ◦ Using your lists from Exercise 2, run the query $x = 26$. Give the position found by the binary search in $M_1$, the down pointer at each step, and say at which steps the test of the position just before the down pointer moves the search back.

4. ◦ There are $k = 20$ sorted lists of $50{,}000$ items each. How many comparisons do 20 separate binary searches make in the worst case? How many does fractional cascading on a path make at most, counting $\lceil \lg(|M_1| + 1) \rceil$ for the first search with $|M_1| \le 2n + k + 1$, and one comparison for each later list?

5. ◦ A segment tree over 1024 elementary intervals stores a sorted list at each node, each of about 1000 items. As a [catalog graph](/catalog-graph/), what is its degree? How many catalogs does a stabbing query visit? How many comparisons do separate binary searches in those catalogs make, and what order of cost does fractional cascading give instead?

6. ◦ The [Chazelle–Liu lower bound](/fractional-cascading-lower-bound/) says that a structure answering queries on its path of $\lceil \omega \rceil$ planar catalogs with $O(\omega)$ visits needs $\Omega(n^2/\omega^2)$ nodes. Evaluate $n^2/\omega^2$ for $n = 10^6$ and $\omega = 20$, and for $\omega = 1000$. For which of the two does the bound say something?

7. • Change the path construction so that every third element of $M_{i+1}$ is copied into $M_i$, at positions $2, 5, 8, \ldots$, together with the final $+\infty$. Bound the total size of the lists, and say how many positions before the down pointer the query must now test. Generalize to a fraction $1/c$.

8. • A query asks for the successors of $x$ in $C_i, C_{i+1}, \ldots, C_j$ only, for some $1 < i \le j \le k$. Show how the path structure answers it in $O(\log n + j - i)$ time.

9. • In a merge sort tree, the sorted list at a node is the merge of the lists of its two children. Store with each element of a node's list the position of its successor in each child's list. Show that a root-to-leaf walk then needs only one binary search, at the root. Why does this tree need no sampling, unlike the path of Exercise 2?

10. • Three catalogs sit on a cycle $u \to v \to w \to u$, and each augmented list receives every second element of the augmented list before it on the cycle. Show that the total size is at most $2n + O(1)$. Why can the lists not be built one at a time from the last to the first, as on a path, and how can they be built instead?

11. • In the static path structure, every element of $M_1$ between two consecutive bridges from $M_2$ has the same down pointer. Give catalogs $C_1$ and $C_2$ for which one new bridge in $M_1$ changes the down pointers of $\Theta(n)$ elements. What does [dynamic fractional cascading](/dynamic-fractional-cascading/) use instead of stored down pointers?

12. • The path in the Chazelle–Liu theorem has $L = \lceil \omega \rceil$ vertices. Separate [planar point location](/planar-point-location/) at each vertex uses $O(n)$ space. How many nodes does it visit per query, and why does this not contradict the theorem?

13. • A long horizontal segment $s_m$ has $m$ short disjoint segments just above it, and a second long segment $s_b$ lies below it. In the vertical adjacency map, how many extra vertices does the top side of the face below $s_m$ have? How many edges can a walk up a vertical query through this face inspect while it reports one segment? How does the combing step of the [hive graph](/hive-graph/) fix this?

14. • The queries are all known in advance: $q$ keys, already sorted, each to be located in all $k$ lists. Show that merging gives all the answers in $O(n + qk)$ time with no preprocessing. When is fractional cascading still the better choice?

15. ★ A rooted tree has a sorted catalog at each vertex, and each query walks from the root down to a leaf, choosing the child at each step. Design a fractional cascading structure in which each vertex receives every second element of the augmented list of each child, with a separate down pointer for each child. Prove that it uses $O(n + |V|)$ space and answers a query that visits $k$ vertices in $O(\log n + k)$ time.

16. ★ In the construction of the hive graph, combing at a segment extends every other vertical edge that ends on top of it down to the next segment. Show that the total number of vertical edges added by the downward sweep is $O(n)$.

17. ★ A monotone planar subdivision with $n$ edges is split by $m$ monotone separating chains, ordered from left to right, and a balanced binary tree over the chains locates a point by testing it against $O(\log m)$ chains, each test a search in the $y$-coordinates of the chain's vertices. Store each edge only at the highest tree node whose chain contains it. Use fractional cascading along the root-to-leaf path to locate a point in $O(\log n)$ time with $O(n)$ space.

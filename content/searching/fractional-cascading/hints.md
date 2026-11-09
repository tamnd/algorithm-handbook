2. $M_3 = (4, 9, 14, 25, 33, 40, \infty)$. $M_2 = (1, 8, \mathbf{9}, 15, 22, \mathbf{25}, 27, \mathbf{40}, \infty)$. $M_1 = (3, \mathbf{8}, 11, \mathbf{15}, 19, \mathbf{25}, 30, \mathbf{40}, \infty)$. The bold elements and the final $\infty$ of $M_1$ and $M_2$ are bridges. The total size is $9 + 9 + 7 = 25$, within $2 \cdot 15 + 3 + 1 = 34$.

3. The binary search finds position 6 of $M_1$, the element 30, so the answer in $C_1$ is 30. The down pointer is 7, the bridge 40 of $M_2$, and $M_2[6] = 27 \ge 26$, so the search moves back to position 6: the answer in $C_2$ is 27. The down pointer is then 5, the bridge 40 of $M_3$, and $M_3[4] = 33 \ge 26$, so the search moves back again, to 33.

4. Separate searches: $20 \lceil \lg 50{,}001 \rceil = 320$. Fractional cascading: $\lceil \lg 2{,}000{,}022 \rceil = 21$ for the first search and 19 more, so at most 40.

7. $|P_{i+1}| \le (|M_{i+1}| + 2)/3$, so $S \le n + 1 + S/3 + O(k)$ and $S \le \frac{3}{2} n + O(k)$. Promoted positions are now up to 3 apart, so the query tests up to two positions back. With a fraction $1/c$ the space is about $\frac{c}{c - 1} n$ and the query tests up to $c - 1$ positions per list.

9. The list of a node contains every element of its children's lists, so the successor of $x$ in a child's list is found from the successor in the parent's list by the stored position, with no gap to search. The space is already $\Theta(n \log n)$, because each element appears once on each level, and copying adds nothing.

10. With $S$ the total size, each list receives at most half of the list before it plus one, so $S \le n + S/2 + 3$. On a cycle, each list depends on the one before it, which depends in the end on itself. Start with $A_v = C_v$ and pass copies around the cycle repeatedly; each round passes at most about half as many new copies as the round before, so the process stops after $O(\log n)$ rounds and linear total work.

11. Take $C_1 = (1, 2, \ldots, n)$ and $C_2 = (0, n + 1)$. Every element of $C_1$ points to the bridge $n + 1$. A new key near $n/2$ in $C_2$ that becomes a bridge changes the pointers of about $n/2$ elements. The dynamic structure answers "next bridge of this edge" with a union-split-find structure in $O(\log \log n)$ time.

12. It visits $O(L \log n) = O(\omega \log n)$ nodes, which is more than $a(L + \omega) = O(\omega)$ for every constant $a$ once $n$ is large. So it is not a structure of the kind the theorem bounds.

13. Each short segment has two endpoints, so the face has $2m$ extra vertices on its top side, and a walk can step along up to $2m + 1$ edges to report the one segment $s_m$. Combing extends every other one of these edges down to $s_b$, which leaves at most one extra vertex on the top side of each new face.

15. Each vertex receives at most half of each child's augmented list plus one, so $S \le n + S/2 + |V|$ and $S \le 2n + 2|V|$. Keep for each element and each child the position of the first promoted element of that child at or after it. Moving down to a child is then the path step: follow the pointer and test one position back.

16. Count the vertical edges that end on top of a segment, original or added. Each one lies in at most one group at combing time, and combing a group of $j$ edges adds at most $j/2$ new edges. So if $E_0 = O(n)$ is the number of original edges and $E$ the number of added ones, $E \le (E_0 + E)/2$, and $E \le E_0$.

17. The chains tested by a query form a root-to-leaf path of the tree. Give each tree node the sorted list of the $y$-coordinates of the edges stored there; each edge is stored once, so the lists have total size $O(n)$. A test at a node whose chain has its edge stored higher up is already decided by an earlier test. Cascade the lists from the leaves towards the root as in Exercise 15, so that after one binary search at the root each test costs $O(1)$.

1. The children have areas 35, 42 and 12, so the coverage is 89. Only $R_1 \cap R_2 = [5, 7] \times [2, 5]$, of area 6, and $R_1 \cap R_3 = [1, 4] \times [4, 5]$, of area 3, are not empty, so the overlap is 9. No point lies in all three, so the union has area $89 - 9 = 80$ and the dead space is $96 - 80 = 16$. A uniform point enters $89/96 \approx 0.93$ children on average.

2. The cell is $(\lfloor 13/5 \rfloor, \lfloor 27/5 \rfloor) = (2, 5)$. The columns run from $\lfloor 6/5 \rfloor = 1$ to $\lfloor 20/5 \rfloor = 4$ and the rows from 4 to 6, so the query scans $4 \cdot 3 = 12$ cells. The bound is $(2 \cdot 2 + 1)^2 = 25$.

3. With $x = 101_2$ and $y = 011_2$, the code is $y_2 x_2\, y_1 x_1\, y_0 x_0 = 01\,10\,11_2 = 27$. The code $45 = 10\,11\,01_2$ gives $y = 110_2 = 6$ and $x = 011_2 = 3$, the cell $(3, 6)$.

4. The fifteen bits, starting with longitude, are 11010 00000 01001, which give `u09`. The cell is $[47.8125, 49.21875]$ in latitude and $[1.40625, 2.8125]$ in longitude. Eight bits of longitude and seven of latitude make a square of $360/256 = 180/128 = 1.40625$ degrees.

5. The root is $(5, 9)$; its left child $(4, 4)$ has the children $(1, 1)$ and $(2, 7)$, and its right child $(8, 5)$ has the children $(6, 2)$ and $(9, 8)$. The height is 3. The query visits $(5, 9)$, $(4, 4)$, $(1, 1)$ and $(2, 7)$, skips the right subtree because $3 < 5$, and reports only $(1, 1)$.

6. The root splits, and so do three of its quadrants: the southwest one, at center $(2, 2)$, the southeast one, at $(6, 2)$, and the northeast one, at $(6, 6)$. That makes 4 internal nodes and $1 + 4 \cdot 4 = 17$ nodes. Of the 13 leaves, 7 are empty, and every leaf of a split quadrant is at depth 2.

7. The tree has 21 nodes, of which 5 are internal and 16 are leaves; 6 of the leaves are black: one block of side 2 and five single pixels. Indeed $(4 \cdot 16 - 1)/3 = 21$.

8. Leaves at depth $h$ hold at most $100^{h+1}$ entries, so $h \ge 3$. The root has at least 2 children and every other node at least 40 entries, so $2 \cdot 40^h \le 10^8$, which gives $h \le 4$. The node has $\frac12 \sum_{k=3}^{6} \binom{9}{k} = \frac12 (84 + 126 + 126 + 84) = 210$ feasible splits.

9. S2 has $6 \cdot 4^{12} = 100\,663\,296$ cells at level 12, about $5.07$ km² each. H3 has $2 + 120 \cdot 7^7 = 98\,825\,162$ cells at resolution 7, about $5.16$ km² each.

11. The digits are 3, 3 and 1, so the index is $3 \cdot 16 + 3 \cdot 4 + 1 = 61$. At each level, find the quadrant, add its digit times the size of a quadrant, and turn the coordinates into those of the copy of the curve in that quadrant, as in the entry.

22. At depth $t$ the query visits $2^{t - c(t)}$ nodes, where $c(t)$ counts the depths below $t$ that split on the axis of the line. For the vertical line $c(t) = \lceil t/2 \rceil$, and for the horizontal line $c(t) = \lfloor t/2 \rfloor$.

23. The cells of the internal nodes at one depth are disjoint, and each holds at least two points.

25. Reducing modulo $2^k$ keeps the low $k$ bits, and the exclusive or works bit by bit. Since $73856093$ and $19349663$ are odd, multiplication by either is a bijection modulo $2^k$.

26. In the first quadrant, the curve is a copy of the curve of order $D - 1$ with $x$ and $y$ exchanged, so the left cell is the top left cell of that copy. If $b_D$ is the index of the top left cell $(0, 2^D - 1)$ of the curve of order $D$, then $b_D = 4^{D-1} + b_{D-1}$. For the right cell, use the mirror symmetry of the curve.

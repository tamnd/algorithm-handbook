1. The exact heights are $0, 0.25, 0.5, 0.75, 1$, and column 2 is a tie. The DDA rounds half up and gives $(0, 0), (1, 0), (2, 1), (3, 1), (4, 1)$; Bresenham's algorithm gives the tie to the start, $(2, 0)$. Drawn from $(4, 1)$, the tie goes to the new start, so column 2 gets $(2, 1)$. The increment $0.25$ and its multiples are exact in binary, so no addition rounds.

3. Each square covers 16 centers and the overlap $[2, 4]^2$ covers 4, and no center lies on an edge. Even-odd: $16 + 16 - 2 \cdot 4 = 24$. Nonzero: 28 when both run the same way (the overlap has $w = 2$), and 24 when they run opposite ways (the overlap has $w = 0$).

5. The samples with $y < 0.2 + 0.7x$ are 1, 2, 3 and 3 in the four columns, so 9 of 16 and the estimate is $0.5625$. The exact area is $0.2 + 0.35 = 0.55$, an error of $0.0125$, well under $7/16$.

7. The levels are $512 \times 256$ down to $2 \times 1$ and $1 \times 1$: 10 levels, $174763$ texels. That is $\tfrac13$ of a texel more than $\tfrac43 WH = 174762\tfrac23$, and it agrees with $(4WH + 2r - 3)/3$ for $r = 2$.

9. Interpolate $u/w$ to $(0 + \tfrac13)/2 = \tfrac16$ and $1/w$ to $(1 + \tfrac13)/2 = \tfrac23$; the quotient is $u = \tfrac14$. Screen-space interpolation gives $\tfrac12$.

10. The edge from $(2.5, 0.5)$ to $(6.5, 4.5)$ is a right edge and the horizontal edge is a bottom edge, so only the edge from $(0.5, 4.5)$ to $(2.5, 0.5)$, a left edge, is included. Of its centers, the two vertices also lie on excluded edges, so only $(1.5, 2.5)$ is drawn. The covered pixels are $(2, 1)$, $(1, 2)$, $(2, 2)$, $(3, 2)$, $(1, 3)$, $(2, 3)$, $(3, 3)$, $(4, 3)$: eight in all.

14. With ties toward the start, the first-octant pixel of column $x$ is $y(x) = \lceil d_y x / d_x - \tfrac12 \rceil$. Since $d_y/g$ is an integer, adding $d_x/g$ to $x$ adds exactly $d_y/g$ inside the ceiling. The pixels are $(0, 0), (1, 0), (2, 0), (3, 1), (4, 1), (5, 1), (6, 1), (7, 2), (8, 2)$.

17. The bound $2q + 2 \le 64$ gives $q \le 31$, so $k \le 23$: pixels $-4194304$ to $4194303$. With 32 bits, $q \le 15$, and with $s = 4$ this is $k \le 11$: pixels $-1024$ to $1023$.

20. The triangle lies in $0.1 \le x \le 0.3$, which holds no $i + \tfrac12$. Edge walking still sets up a span for each of the $h$ rows whose center line meets the triangle, so it spends $\Theta(h)$ time with $c = 0$. Pineda's box runs from column $0$ to column $-1$, which is empty. So $O(h + c)$ is not $O(1 + c)$, and the two bounds are not comparable in general.

22. $A$ over $B$ minus $B$ over $A$ is $\alpha_B A - \alpha_A B$. They are equal exactly when $\alpha_B A = \alpha_A B$ in every channel: when both alphas are positive this says the straight colors are equal, whatever the alphas; otherwise one of the two is fully transparent, $(0, 0, 0, 0)$.

23. Divide the storage formula by $WH = r m^2$, where $m$ is the shorter side: the excess over $\tfrac43$ is $(2r - 3)/(3 r m^2)$. It exceeds $\tfrac16$ only for $m = 1$ and $r > 2$. So the sizes are $2^a \times 1$ and $1 \times 2^a$ with $a \ge 2$; a $4 \times 1$ texture holds $7/4$ of its base.

24. Row $k$ gets the columns $x$ with $|sx + c - k| < \tfrac12$, up to the tie rule at one end. These $x$ form an interval of length $1/s$, and an interval of that length that is not cut by an end of the segment holds $\lfloor 1/s \rfloor$ or $\lceil 1/s \rceil$ integers.

25. Turn the plane by $180°$, $p \mapsto -p$. It maps pixel centers to pixel centers and triangles to triangles with the same orientation, and it negates $A$ and $B$ of every edge. So the bottom-right rule on the scene is the top-left rule on the turned scene.

26. Each edge seen from $p$ turns through an angle strictly between $-\pi$ and $\pi$, and the angles sum to $2\pi w(p)$, so $2\pi |w| < n\pi$. With $n \le 512$ this gives $|w| \le 255$, which is not $0$ modulo $256$ unless $w = 0$. The regular star polygon $\{513/256\}$ winds 256 times around its center, which the counter reads as 0.

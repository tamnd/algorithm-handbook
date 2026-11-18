2. (a) $M = 2 \cdot 64 - 1 = 127$. (b) For a real signal with fixed support the trivial ambiguities are $x$, $-x$, the reversal and its negative: 4 signals, fewer when $x$ equals its own reversal or the negative of it. (c) $2^{62}$.

5. The zero $-1$ lies on the unit circle and $1/\overline{(-1)} = -1$, so flipping it changes nothing. Flipping $-2$ gives $[2, 9, 10, 3]$ and flipping $-3$ gives $[3, 10, 9, 2]$, its reversal. The 8 signals are $\pm[1, 6, 11, 6]$, $\pm[6, 11, 6, 1]$, $\pm[2, 9, 10, 3]$ and $\pm[3, 10, 9, 2]$, in 2 classes.

6. $z(2z^{-1} + 5 + 2z) = 2z^2 + 5z + 2 = (2z + 1)(z + 2)$, with roots $-1/2$ and $-2$, a single pair. The signals are $\pm[1, 2]$ and $\pm[2, 1]$.

8. Flip both zeros $-2$ and $-3$ to $-1/2$ and $-1/3$: $6(1 + \tfrac{1}{2} z^{-1})(1 + \tfrac{1}{3} z^{-1}) = 6 + 5z^{-1} + z^{-2}$, so $[6, 5, 1]$, up to sign. Its autocorrelation is $[6, 35, 62, 35, 6]$.

10. $G'_k$ is the nearest point to $G_k$ with the measured magnitude, so $\lVert G_{k+1} - G'_{k+1}\rVert \le \lVert G_{k+1} - G'_k\rVert$. The unitary DFT keeps distances, so this equals $\lVert g_{k+1} - g'_k\rVert$. And $g_{k+1}$ is the nearest point to $g'_k$ that meets the constraint, while $g_k$ meets it too, so $\lVert g_{k+1} - g'_k\rVert \le \lVert g_k - g'_k\rVert = \lVert G_k - G'_k\rVert$. A non-increasing error need not go to zero: the iteration can stop at a point that is not a solution.

11. Any $y$ with the same magnitude has the same autocorrelation, so its zeros take one element of each pair $\{a_j, 1/a_j\}$; with real zeros every choice gives a real signal. There are $2^{n-1}$ choices, each fixing $y$ up to sign, and the choices give different zero sets because the $2n - 2$ numbers $a_j, 1/a_j$ are distinct. For $[1, 5, 6]$ that is 8 signals, for $[1, 10, 31, 30]$ 16.

1. ◦ Run one level of [Strassen's algorithm](/strassen-algorithm/) on $A = \begin{pmatrix} 2 & 0 \\ 1 & 3 \end{pmatrix}$ and $B = \begin{pmatrix} 1 & 4 \\ 2 & 1 \end{pmatrix}$. Give the seven products $M_1, \ldots, M_7$ and check the result against the triple loop.

2. ◦ How many scalar multiplications and additions does [naive matrix multiplication](/naive-matrix-multiplication/) make for a $3 \times 4$ matrix times a $4 \times 2$ matrix?

3. ◦ How many matrix products does [matrix exponentiation](/matrix-exponentiation/) by repeated squaring make for $A^{100}$? For $A^{63}$? Find a way to compute $A^{63}$ with fewer products.

4. ◦ A directed graph on vertices $0, 1, 2, 3$ has the edges $0 \to 1$, $1 \to 2$, $2 \to 3$ and $3 \to 1$. Compute the [Boolean](/boolean-matrix-multiplication/) square of its adjacency matrix. Which pairs does it connect?

5. ◦ A graph has the edges $0 \to 1$ of weight 5, $0 \to 2$ of weight 1 and $2 \to 1$ of weight 2. Compute the [min-plus](/min-plus-matrix-multiplication/) square of its weight matrix, with $0$ on the diagonal and $\infty$ for missing edges. How many squarings give all shortest path lengths for a graph with $n$ vertices?

6. ◦ Compute the [Kronecker product](/kronecker-product/) $\begin{pmatrix} 1 & 2 \\ 3 & 4 \end{pmatrix} \otimes \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}$.

7. ◦ Let $A$ be $n \times n$ with nonzeros only in its first column, and $B$ with nonzeros only in its first row. How many elementary products $f$ does [Gustavson's algorithm](/sparse-matrix-multiplication/) make for $AB$, and how many nonzeros does $AB$ have? Answer the same for $BA$.

8. ◦ A bilinear algorithm multiplies $3 \times 3$ matrices with $r$ multiplications. For which $r$ does it give a better [exponent](/matrix-multiplication-exponent/) than Strassen's algorithm?

9. • Winograd's variant of Strassen's algorithm uses 7 products and 15 additions of half-size blocks. Solve $T(n) = 7T(n/2) + 15(n/2)^2$, $T(1) = 1$, exactly for $n$ a power of 2.

10. • Show that squaring a matrix is as hard as multiplying two: compute $\begin{pmatrix} 0 & A \\ B & 0 \end{pmatrix}^2$.

11. • Show that entry $(i, j)$ of $A^k$, for the adjacency matrix $A$ of a graph, counts the walks of length $k$ from $i$ to $j$. How many closed walks of length 4 start at a given vertex of the complete graph $K_3$?

12. • Write $a_m = a_{m-1} + 2a_{m-2}$, $a_0 = 0$, $a_1 = 1$, as a $2 \times 2$ matrix power and compute $a_{10}$ by [matrix power](/matrix-power/). Then find a closed form for $a_m$ from the eigenvalues of the matrix.

13. • Show that the [transitive closure](/transitive-closure/) of a graph on $n$ vertices is $(I \vee A)^{n-1}$ over the Boolean semiring, and that $\lceil \lg(n-1) \rceil$ squarings compute it. What is the total time with a fast Boolean product?

14. • Show that the number of triangles in an undirected graph is $\operatorname{tr}(A^3)/6$. Conclude that triangles can be counted in $O(n^\omega)$ time.

15. • Check the identity $(x_1 + y_2)(x_2 + y_1) = x_1 y_1 + x_2 y_2 + x_1 x_2 + y_1 y_2$ behind the [Winograd inner product algorithm](/winograd-inner-product-algorithm/). Where does it use that multiplication is commutative, and why does that stop it from being applied to blocks?

16. • To check a claimed product $C = AB$, pick a random vector $r \in \{0, 1\}^n$ and compare $A(Br)$ with $Cr$. Show that this takes $O(n^2)$ time, and that if $C \ne AB$ the test fails with probability at least $1/2$.

17. • Flatten the tensor of $\langle n, m, p \rangle$ along each of its three factors, and show that its [tensor rank](/tensor-rank/) is at least $\max(nm, mp, np)$. Conclude that the inner product of two vectors of length $n$ needs $n$ multiplications in any bilinear algorithm.

18. • [AlphaTensor](/alphatensor/) found a scheme for $4 \times 4$ matrices over $\mathrm{GF}(2)$ with 47 products, and one for $\langle 4, 5, 5 \rangle$ with 76. What exponents do they give? Compare them with Strassen's.

19. • A *circulant* matrix has entry $c_{(i - j) \bmod n}$ in position $(i, j)$. Show that a circulant matrix-vector product is a cyclic convolution, so it takes $O(n \log n)$ time by the [convolution theorem](/convolution-theorem/). Extend this to Toeplitz matrices, with entry $t_{i - j}$.

20. • Let $W$ be the weight matrix of a graph with no negative cycles, with $0$ on the diagonal. Prove that the min-plus power $W^k$ holds the shortest path lengths using at most $k$ edges, and hence that [repeated squaring](/apsp-repeated-squaring/) computes all shortest paths.

21. ★ A *witness* for entry $(i, j)$ of a Boolean product is an index $k$ with $A_{ik} = B_{kj} = 1$. Show that if every entry has at most one witness, one integer product finds them all. Then show how random sampling of the columns of $A$ handles entries with many witnesses.

22. ★ The rank of the tensor $\langle n, m, p \rangle$ does not change under cyclic shifts of $(n, m, p)$, and $\langle n, m, p \rangle \otimes \langle n', m', p' \rangle = \langle nn', mm', pp' \rangle$. Use these to prove that a scheme of rank $r$ for $\langle n, m, p \rangle$ gives $\omega \le 3 \log r / \log(nmp)$.

23. ★ In [Cannon's algorithm](/cannons-algorithm/) on a $q \times q$ grid, processor $(i, j)$ starts with blocks $A_{i, (i + j) \bmod q}$ and $B_{(i + j) \bmod q, j}$ after the skew, and each step shifts $A$ left and $B$ up by one. Prove that at step $s$ it holds $A_{i, k}$ and $B_{k, j}$ with $k = (i + j + s) \bmod q$, and so it computes $C_{ij}$ after $q$ steps.

24. ★ A linear recurrence of order $d$ has a $d \times d$ companion matrix, so its $k$-th term costs $O(d^3 \log k)$ by matrix powers. Show that it is enough to compute $x^k \bmod \chi(x)$, where $\chi$ is the characteristic polynomial, and that this takes $O(d^2 \log k)$ operations.

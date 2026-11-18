1. ◦ List every triple of distinct elements of $S = \{-12, -5, -2, 1, 3, 4, 7, 9\}$ that sums to zero, as the [3SUM](/3sum/) problem asks.

2. ◦ Let $A = \{1010, 0110, 1101\}$ and $B = \{0101, 1011, 0011\}$ be sets of vectors in $\{0, 1\}^4$. Find every pair $(a, b) \in A \times B$ with $a \cdot b = 0$, as in [orthogonal vectors](/orthogonal-vectors/).

3. ◦ The formula $(x_1 \lor x_3) \land (\lnot x_2 \lor x_4) \land (\lnot x_1 \lor \lnot x_4)$ is split into the halves $\{x_1, x_2\}$ and $\{x_3, x_4\}$, as in the proof that [SETH implies the OV lower bound](/seth-implies-ov-lower-bound/). Coordinate $j$ of the vector of a half assignment is 0 when that half satisfies clause $j$ and 1 otherwise. Write the eight vectors, count the orthogonal pairs, and check the count against the number of satisfying assignments.

4. ◦ Compute the [min-plus convolution](/min-plus-convolution/) $c_k = \min_{i+j=k}(a_i + b_j)$ of $a = (0, 3, 1, 4)$ and $b = (2, 0, 5, 1)$.

5. ◦ The complete graph on vertices $1, 2, 3, 4$ has edge weights $w_{12} = 3$, $w_{13} = -4$, $w_{14} = 2$, $w_{23} = -1$, $w_{24} = -3$ and $w_{34} = 5$. Give the weight of each of its four triangles and say which are negative, as in [negative triangle](/negative-triangle/).

6. ◦ Say which statements are true. (a) SETH implies the orthogonal vectors hypothesis. (b) The orthogonal vectors hypothesis is known to imply SETH. (c) An $O(N^{1.99})$ algorithm for edit distance would prove $\mathsf{P} = \mathsf{NP}$. (d) SETH says that 3-SAT needs time $2^{(1-o(1))n}$.

7. ◦ Schöning's algorithm shows that $k$-SAT can be solved in time $O^*(2^{s n})$ with $s = \log_2(2 - 2/k)$. Compute $s$ for $k = 3$, $4$ and $10$ to three decimal places, and say what SETH claims about the best such $s$ as $k$ grows.

8. ◦ Find all pairs $(i, j)$ with $a_i + a_j = a_{i+j}$ in the array $a = (5, -2, 7, 1, 3, -1, 8, 4)$, indexed from 0, as [Convolution 3SUM](/convolution-3sum/) asks.

9. • Show that the points $(a, a^3)$, $(b, b^3)$ and $(c, c^3)$ for distinct $a, b, c$ are collinear if and only if $a + b + c = 0$. Factor the determinant that tests collinearity.

10. • Give an algorithm for 4-SUM with time $O(n^2 \log n)$, and explain how [$k$-SUM](/k-sum/) for even $k$ is solved in time $O(n^{k/2} \log n)$ in the same way.

11. • A reduction maps an instance of orthogonal vectors with $n$ vectors of dimension $d$ to two strings of length $N = n d^2$. Suppose edit distance had an algorithm with time $O(N^{1.9})$. What time would follow for orthogonal vectors with $d = c \log_2 n$ for a constant $c$, and does it contradict the orthogonal vectors hypothesis?

12. • Show that negative triangle detection on $n$ vertices takes one min-plus product of $n \times n$ matrices and $O(n^2)$ extra time.

13. • Orthogonal vectors can be solved in time $O(2^d d + n d)$ with a table over all subsets of the $d$ coordinates. For which constants $c$ is this truly subquadratic when $d = c \log_2 n$? Explain why this does not contradict the [orthogonal vectors hypothesis](/orthogonal-vectors-hypothesis/).

14. • A reduction solves [OMv](/online-matrix-vector-multiplication/) for an $n \times n$ matrix with a dynamic algorithm: after preprocessing in time $O(n^2)$, each of the $n$ vectors costs $n$ updates and $n$ queries. Show that update and query times of $O(n^{1-\varepsilon})$ would refute the [OMv conjecture](/omv-conjecture/).

15. • Give a dynamic program that solves set cover on a universe of $n$ elements with $m$ sets in time $O(2^n m)$ word operations. What does the [set cover conjecture](/set-cover-conjecture/) say about the base 2?

16. • The reduction from orthogonal vectors to graph diameter builds a graph with $O(n d)$ edges whose diameter is 2 or 3. Show that an algorithm that tells the two cases apart in time $O(m^{2-\varepsilon})$ on graphs with $m$ edges would refute the orthogonal vectors hypothesis.

17. • For graphs, 6-clique can be found in time $O(n^{2\omega})$ by grouping the vertices into triples and finding a triangle in a graph on $\binom{n}{3}$ or fewer nodes. Give the exponent for $\omega < 2.371552$, and explain why the same grouping does not work for [hypercliques](/hyperclique/) in 3-uniform hypergraphs.

18. • Let $A$ reduce to $B$ by a fine-grained reduction from time $n^2$ to time $n^2$, and let $B$ reduce to $C$ in the same way. Suppose the first reduction makes $n^{0.5}$ calls on instances of size $n^{0.7}$, and the second makes one call on an instance of size $N \log N$. Ignoring the time of the reductions themselves, find the time for $A$ that follows from an $O(N^{1.8})$ algorithm for $C$.

19. ★ Give a linear-time reduction from Convolution 3SUM to 3SUM with three lists. Choose the encoding so that the positions cannot interfere with the values.

20. ★ Show that 3SUM on $n$ integers from $\{-U, \ldots, U\}$ can be solved in time $O(n + U \log U)$. Take care that a triple uses three distinct elements.

21. ★ The $k$-orthogonal vectors problem asks for $k$ vectors, one from each of $k$ lists of $n$ vectors, whose coordinatewise product is zero. Prove that under SETH it has no algorithm with time $O(n^{k-\varepsilon} \mathrm{poly}(d))$ for any $\varepsilon > 0$.

22. ★ Show that a triangle in a graph with $m$ edges can be found in time $O(m^{3/2})$ without matrix multiplication, by treating vertices of degree at most $\sqrt{m}$ and of larger degree differently. Then use fast matrix multiplication on the vertices of large degree to get time $O(m^{2\omega/(\omega+1)})$, and say what this is for $\omega = 2$, as in the [triangle detection hypothesis](/triangle-detection-hypothesis/).

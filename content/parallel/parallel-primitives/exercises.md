1. ◦ Which of these operations are an [associative operator](/associative-operator/), and which of those have an identity? (a) $a - b$ on the integers. (b) $\max(a, b)$ on the integers. (c) $a \oplus b = a + b + ab$ on the integers. (d) $(a + b)/2$ on the rationals. (e) $a \oplus b = b$ on a set with at least two elements. (f) $\gcd(a, b)$ on the nonnegative integers.

2. ◦ Run the [Hillis-Steele scan](/hillis-steele-scan/) on $[2, 5, 1, 4, 3, 6]$. Write the array after each round, count the combines, and check the count against $nK - 2^K + 1$ with $K = \lceil \lg n \rceil$.

3. ◦ Run the [Blelloch scan](/blelloch-scan/) on $[2, 5, 1, 4, 3, 6, 0, 7]$. Write the array after each step of the up-sweep, after the root is cleared, and after each step of the down-sweep. How many combines and how many rounds are there, and is the result the inclusive or the exclusive scan?

4. ◦ (a) Gather from $A = [a, b, c, d, e]$ with the index array $I = [4, 4, 0, 2]$. Which PRAM variant does the step need? (b) Scatter the values $[1, 2, 3, 4]$, held by processors 0 to 3, to the indices $I = [2, 0, 2, 2]$ of an array $[0, 0, 0, 0]$, under the priority rule (the smallest processor number wins), under the combining rule with $+$, and under the common rule. See [scatter and gather](/scatter-and-gather/).

5. ◦ Use [parallel pack](/parallel-pack/) to keep the items greater than 5 of $A = [4, 9, 2, 7, 7, 1, 8, 3, 6]$. Give the flag array $F$, its exclusive scan $X$, the output length and the output. Then give the split of $A$ with the kept items last. With $K = \lceil \lg n \rceil$ and $m = 2^K$, what are the work $2n + 2(m - 1)$ and the span $2 + 2K$ of the pack?

6. ◦ Take $A = [5, 2, 0, 3, 1, 4, 2]$ with the segment flags $F = [1, 0, 0, 1, 1, 0, 0]$. Compute the inclusive and the exclusive [segmented prefix sums](/segmented-prefix-sums/) and the total of each segment. A student computes the exclusive sums by shifting the inclusive ones right by one place. Which entries come out wrong, and what are their wrong values?

7. ◦ The list $4 \to 2 \to 0 \to 3 \to 1$ is stored as $next = [3, \mathit{nil}, 0, 1, 2]$. Run [pointer jumping](/pointer-jumping/) for [list ranking](/list-ranking/), with rank 1 at every node that has a successor and 0 at the tail. Give $rank$ and $next$ after each round, and count the updates.

8. ◦ Merge $A = [2, 4, 6, 8, 10]$ and $B = [1, 3, 5, 7, 9, 11, 13]$ in $p = 3$ pieces of four output items each, as in [merging sorted sequences](/merging-sorted-sequences/). Find the co-ranks $(i, j)$ of the cuts $k = 4$ and $k = 8$, with $i + j = k$, and list the inputs of each piece.

9. ◦ For the [parallel transpose](/parallel-matrix-transpose/) of an $8 \times 8$ matrix, give the number of swaps, the work and the span. What lower bound on the span does the rule "a computation of span $S$ has at most $2^S - 1$ unit steps" give here? Compute $W_s(2)$ and $W_s(4)$ for P-SWAP-T, and the number of cache misses for lines of $B = 4$ entries, under the cache assumptions of the entry.

10. • A [parallel for loop](/parallel-for/) has $n = 1000$ iterations, and iteration $i$ costs $i$. Four workers split the loop into four blocks of 250 consecutive iterations. Find the work of each block and an upper bound on the speedup. Then let worker $j$ take the iterations with $(i - 1) \bmod 4 = j$, and answer the same questions.

11. • (a) Compute the [histogram](/histogram-computation/) of $x = [1, 3, 0, 1, 1, 2, 3, 1, 0, 1, 2, 3]$ with $k = 4$ bins, and the work and span of the [parallel histogram](/parallel-histogram/) with $p = 3$ blocks. (b) For $n = 10^6$ and $k = 256$, which $p$ give the least span, and what is the work at the smallest of them?

12. • The Hillis-Steele scan does $nK - 2^K + 1$ combines and the Blelloch scan does $2(m - 1)$, with $K = \lceil \lg n \rceil$ and $m = 2^K$. Find every $n$ for which the Hillis-Steele scan does fewer combines, and the $n$ for which the two are equal. Show that for $K \ge 6$ the Blelloch scan always does fewer.

13. • The recurrence $x_i = a_i x_{i-1} + b_i$ is a scan of the pairs $(a_i, b_i)$, read as the maps $x \mapsto a_i x + b_i$, under $(m_1, c_1) \oplus (m_2, c_2) = (m_1 m_2, m_2 c_1 + c_2)$. Show that $\oplus$ is associative and not commutative. With $x_0 = 1$ and the pairs $(2, 1), (3, -1), (1, 4), (-1, 2)$, compute the prefixes and $x_1, \ldots, x_4$ from them. See [all-prefix-sums](/all-prefix-sums/).

14. • Add $a = 01101101$ and $b = 00110111$ (109 and 55) as a [carry-lookahead adder](/carry-lookahead-adder/) does. Give the pairs $(g_i, p_i)$ with $g_i = a_i \land b_i$ and $p_i = a_i \oplus b_i$ from bit 0 up, the carries $c_1, \ldots, c_8$ that the scan of the pairs gives, and the sum. Which bit generates the carry $c_7$?

15. • The deficiency of a prefix circuit is $s + d - (2n - 2)$. For $n = 16$, find the size, depth and deficiency of the serial circuit, the Sklansky circuit, the Kogge-Stone circuit and the Brent-Kung circuit of the [parallel prefix](/parallel-prefix/) entry. How many gates must any circuit of depth 4 have?

16. • Sort $[5, 2, 7, 4, 1, 6, 3, 0]$ by three splits on bits 0, 1 and 2, as a parallel [radix sort](/radix-sort/) does. Give the array after each pass. Write the destination of each item of a split in terms of two exclusive scans, $X_0$ of the zero flags and $X_1$ of the one flags, and $k_0$, the number of zeros. Why must the split be stable?

17. • Find the largest sum of a nonempty subarray of $[3, -5, 4, -1, 2, -6, 5, 1]$ with two scans: the prefix sums $P$ with $P_0 = 0$, the prefix minima of $P$, and one map. Give all three arrays and the work and span. See the [maximum subarray problem](/maximum-subarray-problem/).

18. • Replace the merge of P-MERGE-SORT by a co-rank merge that cuts the output of $N$ items into $\lceil N / \lg N \rceil$ pieces and merges each piece serially. Find the work and span of one merge and of the whole sort, and compare with the $\Theta(\log^3 n)$ span of the sort that uses [parallel merge](/parallel-merge/).

19. • (a) In [parallel Strassen](/parallel-strassen/), suppose the 18 matrix additions of each level run as serial loops. What are the span and the parallelism? (b) With the entry's closed forms $W = (37 \cdot 7^L - 32n^2 - 2)/3$ and $S = 2L^2 + 11L + 1$, find the least power of 2 for which the parallelism exceeds 1000. (c) Bound $T_{64}$ and the speedup for $n = 64$ on 64 processors.

20. • Evaluate $((2 \times (3 + 4)) - 5) \times (1 + 6)$ with the shunt of [tree expression evaluation](/tree-expression-evaluation/). Number the leaves 0 to 5 from left to right, and in each round rake the odd leaves that are left children and then those that are right children. Give the new edge function at each rake, the number of rounds and rakes, and the value.

21. ★ Change the rule of [list contraction](/list-contraction/): each node draws a random priority, all distinct, and a node is removed when its priority is less than those of its neighbours in the list. Show that the removed set is independent. For one list of $m \ge 2$ nodes, find $\mathbb{E}[|R|]$ and bound the expected number of rounds. Compare with random mate.

22. ★ Write a recursive fork-join scan. UP($v$) computes and stores the sum of each subtree of a balanced tree over the input. DOWN($v$, $acc$) receives the sum of everything to the left of $v$'s subtree, and spawns DOWN on both children with the right accumulators. Prove it correct, and find its work and span. Why is the span smaller than that of the Blelloch scan written as $2K$ parallel loops?

23. ★ The Brent-Kung inclusive circuit for $n = 2^K$, $K \ge 2$, is the up-sweep of the Blelloch scan followed by a down phase: for the strides $s = n/4, n/8, \ldots, 1$, each $i = (2j + 1)s - 1$ with $j \ge 1$ and $i < n$ gets $y[i] \leftarrow y[i - s] \oplus y[i]$. Show that the size is $2n - 2 - K$ and the depth is $2K - 2$, so that the deficiency is $K - 2$.

24. ★ Find a monoid on tuples $(t, p, s, b)$ (total, best prefix, best suffix, best subarray) such that the [parallel reduction](/parallel-reduce/) of the leaves $(x, x, x, x)$ gives the largest sum of a nonempty subarray. Give the combine and the identity, and run the tree on $[3, -5, 4, -1, 2, -6, 2, 4]$, level by level.

25. ★ A scheme multiplies $k \times k$ block matrices with $r > k^2$ block products and a constant number of block additions. Find the work and span of its fork-join form, with the additions as parallel loops. For $k = 3$, which $r$ give less work than parallel Strassen?

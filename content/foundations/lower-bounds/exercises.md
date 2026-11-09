1. ◦ What is the least worst-case number of comparisons with which a comparison algorithm can search a sorted array of $n$ keys, for $n = 1000$, $n = 10^6$, $n = 1023$ and $n = 1024$? Which result of this chapter gives the answer?

2. ◦ For $n = 100$ distinct keys, give the exact worst-case number of comparisons needed to find the maximum, the maximum and the minimum together, and the second largest. How many comparisons do two separate scans use for the second and third tasks?

3. ◦ A key $x$ is looked up in a sorted array of 100 distinct keys. The answer is either the position of $x$ or the gap between two neighbouring keys (or before the first or after the last) where $x$ would go. How many answers are there, and what lower bound does the [information-theoretic bound](/information-theoretic-bound/) give for comparisons with two outcomes?

4. ◦ Give the [trivial lower bound](/trivial-lower-bound/) from reading the input and writing the output for each problem: (a) the sum of $n$ numbers; (b) the product of two $n \times n$ matrices; (c) membership in a sorted array of $n$ keys; (d) connectivity of a graph with $n$ vertices and $m$ edges given by adjacency lists. For which of them is the trivial bound far from the true cost?

5. ◦ For each problem, say whether the known [upper](/upper-bound/) and [lower bounds](/lower-bound/) match, and if so whether exactly or up to a constant factor: (a) sorting by comparisons; (b) the maximum by comparisons; (c) multiplying two $n \times n$ matrices, with an upper bound of $O(n^{2.38})$ arithmetic operations; (d) the DFT of order $n$ by linear algorithms with constants of modulus at most 1.

6. ◦ How many bits are needed at least to store an arbitrary permutation of $\{1, \ldots, 10\}$, and how many does the plain encoding with 4 bits for each entry use?

7. ◦ Among $n$ coins one is heavier than the others, which all weigh the same. A balance compares two groups of coins and reports which side is heavier or that they balance. How many weighings does the counting argument require for $n = 100$, and for $n = 81$?

8. ◦ What lower bound on additions does [Morgenstern's theorem](/fft-lower-bound/) give for the DFT of order $1024$, and how many additions does the radix-2 FFT use?

9. ◦ In the [external memory model](/external-memory-model/), $N = 2^{29}$ items are sorted with fast memory of $M = 2^{20}$ items and blocks of $B = 2^{10}$ items. Evaluate $\frac NB \log_{M/B} \frac NB$. How many passes over the data does [external merge sort](/external-merge-sort/) make?

10. ◦ A pattern of length 5 is searched for in a text of length 100. How many text characters must the best algorithm read in the worst case, and how many must an algorithm that reports all occurrences read on every text?

11. • In Exercise 3, let the algorithm use comparisons with three outcomes, $<$, $=$ and $>$. Show that the information-theoretic bound becomes 5, that every such comparison tree has depth at least 7, and that [binary search](/binary-search/) reaches 7.

12. • An $n \times n$ matrix has rows and columns in increasing order. Show that every comparison algorithm that decides whether a given $x$ occurs in it makes at least $n$ comparisons in the worst case.

13. • An algorithm for [element distinctness](/element-distinctness/) may only ask whether two keys are equal. Show that it needs $\binom n2$ questions in the worst case.

14. • Use [reductions](/reduction-lower-bound/) from element distinctness to show that, in the algebraic computation tree model, each of these needs $\Omega(n \log n)$ operations: (a) finding a most frequent value of $n$ reals; (b) finding the closest pair of $n$ points on a line.

15. • Show that every comparison algorithm that builds a binary search tree from $n$ unsorted keys makes $\Omega(n \log n)$ comparisons. A [binary heap](/binary-heap/) can be built from $n$ keys with $O(n)$ comparisons; why does the argument not apply to it?

16. • An array of $n$ bits holds exactly one 1. Show that a deterministic algorithm needs $n - 1$ probes in the worst case to find it. Use [Yao's principle](/yao-minimax-principle/) to show that every randomized algorithm needs at least $(n+1)/2 - 1/n$ probes in expectation on some input, and give an algorithm that meets this bound on every input.

17. • An array is $k$-sorted if each key is at most $k$ places from its position in sorted order. Show that sorting $k$-sorted arrays by comparisons needs $\Omega(n \log k)$ comparisons in the worst case.

18. • Show that merging $k$ sorted lists of $m$ keys each, $n = km$ keys in all, needs at least $n \lg k - O(k \log n)$ comparisons.

19. • A program computes $x^n$ from $x$ using only multiplications. Show that it needs at least $\lceil \lg n \rceil$ multiplications. For $n = 15$, compare this bound with the binary method of repeated squaring and with the best program.

20. • A [decision tree](/decision-tree-model/) computes a function of $n$ bits by querying bits. Show that the parity and the OR of $n$ bits both need depth $n$. Give a function of 3 bits that depends on all three but has a tree of depth 2.

21. • Yao's [static dictionary bound](/static-dictionary-lower-bound/) says that a table holding $n$ keys from a large universe needs $\lceil \lg(n+1) \rceil$ probes per membership query. Perfect hashing answers membership with $O(1)$ probes. Which assumption of Yao's theorem does perfect hashing break?

22. • Apply Morgenstern's bound $\log_2 |\det A|$ to (a) $A = 2I$, the map $x \mapsto 2x$ on $n$ inputs, and (b) the lower triangular matrix of ones, which computes the prefix sums. Is either bound attained?

23. ★ Show that deciding whether a graph on $v$ vertices, given by its adjacency matrix, is connected needs all $\binom v2$ queries in the worst case.

24. ★ Use [Ben-Or's theorem](/ben-or-theorem/) to show that deciding whether two sets of $n$ reals, $\{x_1, \ldots, x_n\}$ and $\{y_1, \ldots, y_n\}$, are disjoint needs $\Omega(n \log n)$ operations of an algebraic computation tree.

25. ★ Show that the information-theoretic lower bound for building a binary heap from $n$ distinct keys by comparisons is $\sum_v \lg s_v$, where $s_v$ is the size of the subtree at node $v$, and that it is less than $2n$ for $n = 2^k - 1$.

26. ★ Use the [incompressibility method](/incompressibility-method/) to prove that there are infinitely many primes.

27. ★ Use a [counting argument](/counting-argument/) to show that at most half of the $2^{2^n}$ Boolean functions of $n$ bits have a decision tree of depth at most $n - \lg(\lg n + 1) - 1$.

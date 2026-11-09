1. ◦ Use the greedy scan of [subsequence checking](/subsequence-checking/) to decide which of AGRIM, GOTH, HIT, LIAR and RITH are subsequences of ALGORITHM. For each one that is, give the positions the scan matches. Which of them are also substrings?

2. ◦ Fill the [LCS table](/lcs-dynamic-programming/) for $X = \text{ABAZDC}$ and $Y = \text{BACBAD}$. What is the length of a longest common subsequence, and what does the traceback return? Is the longest common subsequence unique here?

3. ◦ Run the pile method for the [longest increasing subsequence](/longest-increasing-subsequence/) on $\langle 2, 9, 5, 3, 7, 11, 8, 10, 4 \rangle$. Show the array of smallest tails after each item. What is the length, and which increasing subsequences reach it? Why is the final tail array not itself an increasing subsequence of the input?

4. ◦ Find the [maximum-sum non-adjacent subsequence](/max-sum-non-adjacent-subsequence/) of $\langle 6, 7, 1, 30, 8, 2, 4 \rangle$. Write out the values $W_0, \dots, W_7$ and trace back to the chosen positions.

5. ◦ Count the [distinct subsequences](/distinct-subsequences/) of abab and of abcab, counting the empty one. Use the recurrence $D_i = 2D_{i-1} - D_{p(i)-1}$ and show each $D_i$.

6. ◦ How many times does sue [occur as a subsequence](/count-subsequence-occurrences/) of subsequence? Then find the [shortest window](/minimum-window-subsequence/) of abracadabra that contains cab as a subsequence.

7. ◦ For $X = \text{sunday}$ and $Y = \text{saturday}$, find the length $L$ of a longest common subsequence, the length of the [shortest edit script](/shortest-edit-script/) by insertions and deletions, and the length of the [shortest common supersequence](/shortest-common-supersequence/). Compare the edit script with the [edit distance](/edit-distance/), which also allows substitutions.

8. ◦ By the [Erdős–Szekeres theorem](/erdos-szekeres-theorem/), how long a monotone subsequence must a sequence of 17 distinct numbers contain? Give a sequence of 16 distinct numbers with no increasing and no decreasing subsequence of that length.

9. ◦ Find the [longest palindromic subsequence](/longest-palindromic-subsequence/) of abracadabra. How many letters must be inserted to make abracadabra a palindrome?

10. • A friend computes the LCS of three strings by taking an LCS of the first two and then an LCS of that with the third. Show by a small example that this can fail. Then give a recurrence for the LCS of three strings of length $n$ that runs in $O(n^3)$ time.

11. • Let $X = a_1 b_1 a_2 b_2 \cdots a_k b_k$ and $Y = b_1 a_1 b_2 a_2 \cdots b_k a_k$, with all $2k$ letters distinct. Show that the LCS has length $k$ and that there are $2^k$ different longest common subsequences. What does this say about any algorithm that lists them all?

12. • $X$ and $Y$ are two permutations of $\{1, \dots, n\}$. Show how to find their LCS in $O(n \log n)$ time by reducing it to a longest increasing subsequence.

13. • Envelope $(w, h)$ fits inside $(w', h')$ when $w < w'$ and $h < h'$. Show how to find the longest chain of nested envelopes in $O(n \log n)$ time by sorting and an LIS. Why must envelopes of equal width be sorted by decreasing height? Find the answer for $(5, 4), (6, 4), (6, 7), (2, 3)$.

14. • Extend the quadratic LIS recurrence so that it also counts the longest increasing subsequences. How many are there in $\langle 1, 3, 5, 4, 7 \rangle$?

15. • What is the fewest number of decreasing subsequences into which $\langle 4, 2, 6, 1, 5, 3 \rangle$ can be split? Give such a split, and explain how the answer follows from the dual of [Dilworth's theorem](/dilworth-theorem/).

16. • Change the non-adjacent problem so that a chosen set may contain two neighbours but never three items in a row. Give the recurrence and find the best sum for $\langle 3, 2, 5, 10, 7 \rangle$.

17. • The items now sit on a cycle, so the first and the last are neighbours too. Show how to solve the non-adjacent problem with two runs of the path recurrence. Find the answer for $\langle 5, 1, 1, 5 \rangle$. Show that the number of allowed sets on a cycle of $n \ge 3$ items is the Lucas number $L_n = F_{n-1} + F_{n+1}$.

18. • What is the shortest string over $\{a, b\}$ that is not a subsequence of abba? List all such strings of that length.

19. • Let $L_n$ be the length of the longest increasing subsequence of a random permutation of $n$ items. Use the Erdős–Szekeres theorem, in the form $L_\uparrow \cdot L_\downarrow \ge n$, to show that $E[L_n] \ge \sqrt{n}$.

20. • Compare the work of [Myers' algorithm](/myers-diff/) and [Hunt–Szymanski](/hunt-szymanski/) on two pairs of inputs: $X = a^n$, $Y = b^n$; and $X = Y = a^n$. For each pair give $D$, the number $r$ of matching pairs, and the running time of both algorithms.

21. • Prove that in the LCS table $c[i,j] - c[i-1,j] \in \{0, 1\}$ for all $i, j \ge 1$, and the same for $c[i,j] - c[i,j-1]$. Which later methods in the chapter depend on this fact?

22. ★ Show that $E[L_n] \le (1 + o(1))\, e \sqrt{n}$ for a random permutation. Count the expected number of increasing subsequences of length $k$ and choose $k$ with care.

23. ★ Prove that a string of length $n$ over $\{a, b\}$ has at most $F_{n+3} - 1$ distinct subsequences, counting the empty one, and that the alternating string $abab\cdots$ reaches this bound.

24. ★ Split a string $T$ over an alphabet of size $\sigma$ greedily into blocks: cut each time the current block has seen all $\sigma$ letters. Say there are $k$ complete blocks. Prove that the shortest string that is not a subsequence of $T$ has length exactly $k + 1$, and show how to build one in $O(|T|)$ time.

25. ★ A *longest common increasing subsequence* of two integer sequences is a longest sequence that is a subsequence of both and is strictly increasing. Give an $O(nm)$ algorithm for it, and find one for $\langle 3, 1, 4, 1, 5, 9, 2, 6 \rangle$ and $\langle 1, 4, 2, 5, 6, 9, 3 \rangle$.

26. ★ Prove that the number of permutations of $\{1, \dots, n\}$ with no increasing subsequence of length 3 is the Catalan number $C_n = \frac{1}{n+1}\binom{2n}{n}$. Check your answer for $n = 3$ and $n = 4$.

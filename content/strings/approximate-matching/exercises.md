1. ◦ Fill the [Wagner-Fischer](/wagner-fischer-algorithm/) table for $\texttt{cocoa}$ and $\texttt{cacao}$. What is their [edit distance](/edit-distance/), and which edit operations does an optimal alignment use?

2. ◦ Find the Levenshtein distance and the [Damerau-Levenshtein distance](/damerau-levenshtein-distance/) of $\texttt{recieve}$ and $\texttt{receive}$, and of $\texttt{word}$ and $\texttt{drow}$.

3. ◦ Compute the [Soundex](/soundex/) codes of Turing, Hopper, Lovelace, Knuth and Schmidt.

4. ◦ Compute the Hamming distance of the pattern $\texttt{aba}$ to every window of the text $\texttt{abbaabab}$, as in [Hamming string matching](/hamming-string-matching/). Which positions solve the [k-mismatch problem](/k-mismatch-problem/) with $k = 1$?

5. ◦ Run [Sellers' algorithm](/sellers-algorithm/) for the pattern $\texttt{abc}$ on the text $\texttt{axbcabbc}$ with $k = 1$. At which text positions, counting from 0, does an approximate occurrence end?

6. ◦ The pattern $\texttt{algorithmics}$ is searched with $k = 2$ by [pigeonhole filtering](/pigeonhole-filtering/). Give the pieces. The text holds $\texttt{alxorithmucs}$; which piece finds it?

7. ◦ The [bitap algorithm](/bitap-algorithm/) for $k$ mismatches uses a field of $\lceil \lg(k+1) \rceil + 1$ bits per pattern position. How many 64-bit words does it need for a pattern of length 20 with $k = 3$, and with $k = 4$?

8. ◦ Which of the strings $\texttt{ward}$, $\texttt{wrd}$, $\texttt{drow}$, $\texttt{words}$, $\texttt{sword}$ and $\texttt{wodr}$ does the [Levenshtein automaton](/levenshtein-automaton/) of $\texttt{word}$ with $k = 1$ accept?

9. • Prove that the edit distance is a metric: it is zero only for equal strings, symmetric, and satisfies the triangle inequality. Show also that $|m - n| \le d(x, y) \le \max(m, n)$ for strings of lengths $m$ and $n$, and that both bounds are reached.

10. • In a [weighted edit distance](/weighted-edit-distance/), insertions and deletions cost 1 and substitutions cost 2. Show that the distance is $m + n - 2\,\mathrm{LCS}(x, y)$, where LCS is the length of a [longest common subsequence](/longest-common-subsequence/). Compute it for $\texttt{garden}$ and $\texttt{danger}$.

11. • The optimal string alignment distance allows a transposition of adjacent characters but no further edit on a transposed pair. Show with the strings $\texttt{ba}$, $\texttt{ab}$ and $\texttt{acb}$ that it does not satisfy the triangle inequality. What is the true Damerau-Levenshtein distance of $\texttt{ba}$ and $\texttt{acb}$?

12. • Over the binary alphabet, show that all Hamming distances between a pattern and the windows of a text follow from one convolution and two prefix sums.

13. • Show that the bound of the [q-gram lemma](/q-gram-lemma/) is tight: give, for $q = 2$ and $k = 1$, a pattern of length 5 and a string at distance 1 from it that share exactly $m - q + 1 - kq$ q-grams.

14. • A word $w$ of length $n$ has no two equal adjacent letters, and the alphabet has $\sigma$ letters. Show that exactly $(2n + 1)\sigma - n$ strings are at edit distance exactly 1 from $w$. How many are there for $\texttt{word}$ over 26 letters? Why is the count different for $\texttt{aab}$ over $\{\texttt{a}, \texttt{b}\}$?

15. • Build the Levenshtein automaton of $\texttt{ab}$ with $k = 1$ over the alphabet $\{\texttt{a}, \texttt{b}, \texttt{c}\}$, with the rows of the Wagner-Fischer table capped at $k + 1 = 2$ as states. How many states can be reached, and which are accepting?

16. • Prove that the cells of the edit distance table satisfy $D[i-1][j-1] \le D[i][j] \le D[i-1][j-1] + 1$. Explain why this lets the [Landau-Vishkin algorithm](/landau-vishkin-algorithm/) describe each diagonal by the furthest row it reaches with $e$ errors.

17. • In [Ukkonen's cut-off](/ukkonen-cutoff-algorithm/), let $\ell_j$ be the last row of column $j$ with a value at most $k$. Prove that $\ell_{j+1} \le \ell_j + 1$, so the next column needs to be computed only down to row $\ell_j + 1$.

18. ★ Show how to compute the edit distance $d$ of two strings of lengths $m$ and $n$ in $O((m + n)d)$ time without knowing $d$ in advance, by computing furthest reaching points on the diagonals for $e = 0, 1, 2, \ldots$. How does the bound change with constant-time longest common extension queries?

19. ★ Show that all Hamming distances between a pattern of length $m$ and the windows of a text of length $n$, over any alphabet, can be computed in $O(n \sqrt{m \log m})$ time. Treat the symbols that occur often in the pattern with convolutions and the others by direct counting, and choose the threshold.

20. ★ Prove that two vertically adjacent cells of a column of the Sellers table differ by at most 1. Conclude that the columns, with values capped at $k + 1$, take at most $3^m$ different values, so approximate matching can be done by a deterministic automaton whose size does not depend on the text.

21. ★ Two strings are permutations of the same $n$ distinct symbols. Show that their distance with insertions and deletions only can be computed in $O(n \log n)$ time.

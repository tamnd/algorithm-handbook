1. ◦ Write the [suffix array](/suffix-array/) and the [LCP array](/lcp-array/) of $\texttt{papaya}$, counting positions from 0 and with no sentinel.

2. ◦ From the arrays of exercise 1, find the number of distinct nonempty substrings of $\texttt{papaya}$ and its [longest repeated substring](/longest-repeated-substring/).

3. ◦ How many nodes, counting the root, does the [suffix trie](/suffix-trie/) of $\texttt{cocoa}$ have? How many does the [suffix tree](/suffix-tree/) of $\texttt{cocoa\$}$ have, and how many of them are leaves?

4. ◦ The [implicit suffix tree](/implicit-suffix-tree/) of $\texttt{papaya}$ has no sentinel. How many leaves does it have, and which suffixes do not end at a leaf?

5. ◦ Write the [circular suffix array](/circular-suffix-array/) and the suffix array of $\texttt{abaa}$. Where do they differ, and why? Read the Burrows-Wheeler transform from the circular suffix array.

6. ◦ [Kasai's algorithm](/kasai-algorithm/) visits the suffixes of $\texttt{papaya}$ in text order, $i = 0, 1, \ldots, 5$. Give the value $h$ it finds for each suffix, the length of its common prefix with the suffix just before it in sorted order. Check that $h$ never drops by more than 1 from one suffix to the next.

7. ◦ Use the LCP array of exercise 1 and the [LCP-RMQ reduction](/lcp-rmq-reduction/) to find the [longest common extension](/longest-common-extension-query/) of positions 0 and 2, and of positions 1 and 5, of $\texttt{papaya}$.

8. ◦ Show that the suffix tree of $\texttt{a}^n\texttt{\$}$ has exactly $2n + 1$ nodes, so the bound of the [suffix tree size theorem](/suffix-tree-size-theorem/) is reached.

9. ◦ Compute the [matching statistics](/matching-statistics/) of the pattern $\texttt{coat}$ against the text $\texttt{cocoa}$.

10. • The Burrows-Wheeler transform of $\texttt{papaya\$}$, with $\texttt{\$}$ smallest, is $\texttt{aypp\$aa}$. Use the backward search of the [FM-index](/fm-index/) to count the occurrences of $\texttt{pa}$ and of $\texttt{aya}$. Give the range of rows after each step.

11. • Show how to count the distinct substrings of length exactly $L$ of a string from its suffix array and LCP array in $O(n)$ time. Apply your rule to $\texttt{papaya}$ with $L = 2$.

12. • Give an $O(n)$ method that finds the longest substring occurring at least $k$ times in a string of length $n$, given its suffix array and LCP array. What is the answer for $\texttt{papaya}$ with $k = 3$, and for $\texttt{murmur}$ with $k = 2$?

13. • Find the [longest common substring](/longest-common-substring/) of $\texttt{tomato}$ and $\texttt{potato}$ with the suffix array of $\texttt{tomato\#potato}$. Explain why it suffices to look at pairs of suffixes that are adjacent in sorted order and come from different strings.

14. • A shortest absent word of a string $T$ over an alphabet $\Sigma$ is a shortest string over $\Sigma$ that does not occur in $T$. Show how to find one in $O(n\sigma)$ time with the [suffix automaton](/suffix-automaton/) of $T$. Find all shortest absent words of $\texttt{aabbab}$ over $\{\texttt{a}, \texttt{b}\}$.

15. • When the suffix automaton is extended by one symbol, the new state $\mathit{last}$ is created. Show that the number of new distinct substrings is $\mathrm{len}(\mathit{last}) - \mathrm{len}(\mathrm{link}(\mathit{last}))$. List these increments for $\texttt{cocoa}$, one symbol at a time, and check their sum against the [count of distinct substrings](/count-distinct-substrings/).

16. • Find all [maximal repeats](/maximal-repeats/) of $\texttt{papaya}$ and of $\texttt{cocoa}$.

17. • For each position $i$ of $\texttt{cocoa}$, find the length of the [shortest unique substring](/shortest-unique-substring/) that starts at $i$.

18. • Count the internal nodes of the suffix tree of $\texttt{papaya\$}$ from the LCP array of $\texttt{papaya\$}$ alone, and give the path label of each. Describe the rule in terms of the [LCP interval tree](/lcp-interval-tree/).

19. • The function $\Psi$ of a [compressed suffix array](/compressed-suffix-array/) is $\Psi[i] = SA^{-1}[SA[i] + 1]$, with position $n$ taken as 0. Compute $\Psi$ for $\texttt{papaya\$}$. Check that it is increasing on each block of rows whose suffixes start with the same symbol, and recover the text from $\Psi$, the first column and $SA^{-1}[0]$.

20. ★ Show that any algorithm that builds the suffix array of a string over a general ordered alphabet, using only comparisons of symbols, needs $\Omega(n \log n)$ comparisons in the worst case. Does the bound also hold for a suffix tree whose children are kept in sorted order?

21. ★ Give an $O(n \log n)$ algorithm that finds the longest substring with two occurrences that do not overlap. Find the answer for $\texttt{murmur}$ and for $\texttt{aaaaa}$.

22. ★ There are $m$ strings of total length $N$. Give an $O(N)$ algorithm, using the suffix array and LCP array of their concatenation with separators, that finds the longest substring common to at least $k$ of the strings.

23. ★ Every permutation of $0, \ldots, n - 1$ is the suffix array of some string over an alphabet of $n$ letters. Show that the smallest alphabet that suffices for the permutation $SA$ has $1 + d$ letters, where $d$ is the number of ranks $i < n - 1$ with $R(SA[i] + 1) > R(SA[i + 1] + 1)$, $R$ is the inverse of $SA$, and $R(n) = -1$. What is the smallest alphabet for $[5, 1, 3, 0, 2, 4]$, and for $[2, 0, 3, 1]$?

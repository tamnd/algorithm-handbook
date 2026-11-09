1. ◦ Build the trie of the patterns $\{\texttt{ab}, \texttt{abc}, \texttt{bca}, \texttt{c}, \texttt{caa}\}$. How many nodes does it have, counting the root? Give the [failure link](/failure-link/) of every node.

2. ◦ In the trie of exercise 1, which nodes have a [dictionary suffix link](/dictionary-suffix-link/) that is not nil, and where do those links point?

3. ◦ Run [Aho-Corasick](/aho-corasick/) with the patterns of exercise 1 on the text $\texttt{abcaab}$. List every occurrence as a pair (pattern, starting position), counting from 0.

4. ◦ The patterns are $\texttt{a}, \texttt{aa}, \ldots, a^k$ and the text is $a^n$ with $n \ge k$. How many occurrences are there in all? What does this say about any bound for [multiple string matching](/multiple-string-matching/) that depends on $n$ and $m$ only?

5. ◦ Compute the shift table of [Set Horspool](/set-horspool/) for the patterns $\{\texttt{tick}, \texttt{stack}, \texttt{rock}\}$.

6. ◦ Compute the [block shift table](/block-shift-table/) of [Wu-Manber](/wu-manber/) with $B = 2$ for the patterns $\{\texttt{share}, \texttt{hares}, \texttt{shore}\}$. What is the shift for a block that occurs in no pattern?

7. ◦ Build the trie of the single pattern $\texttt{aabaa}$ and give the failure link of each node. Check your answer against the [prefix function](/prefix-function/) of $\texttt{aabaa}$.

8. ◦ A $2 \times 2$ pattern has the rows $\texttt{ab}$ and $\texttt{ba}$. The text is the $3 \times 4$ matrix with rows $\texttt{abab}$, $\texttt{baba}$, $\texttt{abab}$. Follow the [Bird-Baker](/bird-baker/) method: name the pattern rows, write the matrix of names that the row automaton produces, and list the top-left corners of all occurrences.

9. • Give a set of patterns and a text on which an Aho-Corasick search that reports by walking the whole failure chain at each text position takes $\Theta(nk)$ steps, while there are no occurrences at all. How do dictionary suffix links avoid this?

10. • Show how to decide which patterns of a set occur in a text at least once, in $O(n + m)$ time, even when the number of occurrences $z$ is much larger than $n + m$.

11. • Show how to count the occurrences of every pattern of a set in a text in $O(n + m)$ time in all, without listing them. (Use the tree formed by the failure links.)

12. • Prove that at most $\sqrt{2m}$ distinct patterns of a set of total length $m$ can end at one text position. Conclude that $z \le n\sqrt{2m}$ for a set of distinct patterns.

13. • Failure links are computed in breadth-first order. Show, with the patterns $\{\texttt{abcd}, \texttt{bcx}, \texttt{cd}\}$, what goes wrong if they are computed in depth-first order, visiting the branch of $\texttt{a}$ before the branch of $\texttt{b}$.

14. • Use the Aho-Corasick automaton of $\{\texttt{11}, \texttt{101}\}$ to count the binary strings of length 6 that contain neither pattern. Give the count and the size of the dynamic program in general.

15. • In [Karp-Rabin for many patterns](/karp-rabin-multiple-patterns/), $k$ distinct patterns of length $\ell$ are hashed with a prime modulus $p$ and a random base. Bound the expected number of windows of a text of length $n$ that are compared character by character with a pattern they do not equal.

16. • Set Horspool, Commentz-Walter and Wu-Manber all use a window as long as the shortest pattern. Why must they? What happens to Set Horspool when one of the patterns has length 1?

17. • Give a [dynamic dictionary](/dynamic-dictionary-matching/) that supports insertion of a pattern of length $p$ in $O(p \log m)$ amortized time and a search in $O(n \log m + z)$ time, by keeping several Aho-Corasick automata whose sizes are powers of two.

18. ★ Prove that, once the automaton is built, the Aho-Corasick search with dictionary suffix links runs in $O(n + z)$ time, when a trie step costs $O(1)$.

19. ★ Prove that the failure links of the trie of a set of patterns of total length $m$ are computed in $O(m)$ time in all, by bounding the work along the path of each pattern separately.

20. ★ Extend Karp-Rabin fingerprints to two dimensions: find all occurrences of an $R' \times C'$ pattern in an $R \times C$ text in $O(RC + R'C')$ expected time.

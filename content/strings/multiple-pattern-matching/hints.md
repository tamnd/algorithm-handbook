1. Ten nodes: the root, $\texttt{a}$, $\texttt{ab}$, $\texttt{abc}$, $\texttt{b}$, $\texttt{bc}$, $\texttt{bca}$, $\texttt{c}$, $\texttt{ca}$, $\texttt{caa}$. The failure links are: $\texttt{a}$, $\texttt{b}$ and $\texttt{c}$ to the root; $\texttt{ab} \to \texttt{b}$; $\texttt{abc} \to \texttt{bc}$; $\texttt{bc} \to \texttt{c}$; $\texttt{bca} \to \texttt{ca}$; $\texttt{ca} \to \texttt{a}$; $\texttt{caa} \to \texttt{a}$.

2. Only $\texttt{abc}$ and $\texttt{bc}$, both to $\texttt{c}$.

3. $(\texttt{ab}, 0)$, $(\texttt{abc}, 0)$, $(\texttt{bca}, 1)$, $(\texttt{c}, 2)$, $(\texttt{caa}, 2)$ and $(\texttt{ab}, 4)$: six occurrences.

4. $\sum_{j=1}^{k} (n - j + 1) = kn - k(k-1)/2$, which is $\Theta(nk)$ when $k \le n/2$. Here $m = k(k+1)/2$, so the output alone can exceed any bound of the form $O(n + m)$.

5. $\ell = 4$. The table gives 1 for $\texttt{c}$, 2 for $\texttt{a}$, $\texttt{i}$ and $\texttt{o}$, 3 for $\texttt{t}$ and $\texttt{r}$, and 4 for every other character.

6. $\ell = 5$. The shifts are 0 for $\texttt{re}$ and $\texttt{es}$, 1 for $\texttt{ar}$ and $\texttt{or}$, 2 for $\texttt{ha}$ and $\texttt{ho}$, 3 for $\texttt{sh}$, and $\ell - B + 1 = 4$ for any other block.

7. $\texttt{a} \to$ root, $\texttt{aa} \to \texttt{a}$, $\texttt{aab} \to$ root, $\texttt{aaba} \to \texttt{a}$, $\texttt{aabaa} \to \texttt{aa}$. The prefix function is $0, 1, 0, 1, 2$, the depths of these targets.

8. Name $\texttt{ab}$ as 1 and $\texttt{ba}$ as 2. In columns 1 to 3 the rows of names are $1, 2, 1$; $2, 1, 2$; $1, 2, 1$. The column string $1\,2$ occurs at rows 0 and 1, giving occurrences with top-left corners $(0, 0)$, $(1, 1)$ and $(0, 2)$.

9. The single pattern $a^k\texttt{b}$ and the text $a^n$. After $k$ characters the search sits at $a^k$, whose failure chain $a^{k-1}, \ldots, \texttt{a}$ holds no pattern. A dictionary link is nil there, so the report at each position costs $O(1)$.

10. Mark each node the search reaches, without reporting. Then process the nodes in reverse breadth-first order and mark the failure target of every marked node. A pattern occurs exactly when its node is marked.

11. Count how often the search reaches each node, then add the count of each node to its failure target, in reverse breadth-first order. The final count at a pattern's node is its number of occurrences.

12. The patterns that end at one position are suffixes of one another, so they have distinct lengths. If $j$ of them end there, their total length is at least $1 + 2 + \cdots + j$, so $j(j+1)/2 \le m$.

13. Depth-first order computes $\mathrm{fail}(\texttt{abcd})$ before $\mathrm{fail}(\texttt{bc})$. From $\mathrm{fail}(\texttt{abc}) = \texttt{bc}$, which has no child $\texttt{d}$, it needs $\mathrm{fail}(\texttt{bc}) = \texttt{c}$, which is not known yet; it finds the root instead and misses $\texttt{cd}$.

14. 13 strings. The states are the trie nodes that are not patterns and have no pattern on their dictionary chain; the program has (length) $\times$ (number of nodes) $\times\, \sigma$ steps.

15. For a fixed window and a fixed pattern that differs from it, the hashes collide with probability at most $(\ell - 1)/p$. By the union bound over $k$ patterns and $n - \ell + 1$ windows, the expectation is at most $(n - \ell + 1)k(\ell - 1)/p$.

16. A shift is safe only if no pattern can end inside the skipped part; the shortest pattern can end as soon as $\ell$ characters after the window start. With a pattern of length 1, $\ell = 1$, every shift is 1 and the algorithm reads every character, often more than once.

17. Keep at most one automaton for each power of two, holding patterns of that total size. To insert, merge it with the automata of sizes $1, 2, 4, \ldots$ as in binary addition and rebuild. Each character is rebuilt $O(\log m)$ times. A search runs all $O(\log m)$ automata.

18. Let $d$ be the depth of the current node. Each text character raises $d$ by at most 1, and each failure step lowers it by at least 1, so there are at most $n$ failure steps. Each dictionary link visited reports an occurrence.

19. Along the path of one pattern $P$, the depths of the failure targets behave like the prefix function of $P$: the depth of $\mathrm{fail}$ rises by at most 1 from a node to its child and each step of the inner loop lowers it. So the work charged to the nodes on the path of $P$ is $O(|P|)$. Every node lies on the path of some pattern, so the total is $O(m)$.

20. Hash each column segment of height $R'$ with a rolling hash, then roll a second hash over each row of column hashes. The text fingerprints for all $(R - R' + 1)(C - C' + 1)$ positions take $O(RC)$ time; check each hit, and pick the base at random to bound the expected number of false hits.

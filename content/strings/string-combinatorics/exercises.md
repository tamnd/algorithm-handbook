1. ◦ Find all nonempty [borders](/border/) and all [periods](/string-period/) of $\texttt{abcababc}$. Which period is the smallest?

2. ◦ Run [Duval's algorithm](/duval-algorithm/) on $\texttt{bcabcaab}$ and write down its [Lyndon factorization](/lyndon-factorization/). Check that the factors do not increase.

3. ◦ Find the [least rotation](/minimal-rotation/) of $\texttt{cabbab}$ and the index where it starts. Then decide whether $\texttt{babcab}$ is a [rotation](/word-conjugacy/) of $\texttt{cabbab}$ by searching for it in $\texttt{cabbabcabbab}$.

4. ◦ Which of $\texttt{aab}$, $\texttt{aba}$, $\texttt{abb}$, $\texttt{aabab}$, $\texttt{abab}$, $\texttt{aabb}$ and $\texttt{abaab}$ are [Lyndon words](/lyndon-word/)? For each one that is not, name a proper rotation that is not larger than it.

5. ◦ List the [minimal absent words](/minimal-absent-word/) of $\texttt{abba}$ over the alphabet $\{a, b\}$. Why is $\texttt{aab}$ absent from $\texttt{abba}$ but not a minimal absent word?

6. ◦ Write the [Parikh vectors](/parikh-vector/) of $\texttt{dormitory}$ and $\texttt{dirtyroom}$ over the letters $d, i, m, o, r, t, y$. Are the two words [Abelian equivalent](/abelian-equivalence/)? Are they conjugate?

7. ◦ List the distinct [squares](/square/) of $\texttt{abaababb}$, with the start of each occurrence.

8. ◦ Write the [Christoffel word](/christoffel-word/) for $(p, q) = (5, 4)$, the lower one, with five letters $a$ and four letters $b$. Check that it has the form $a\,P\,b$ with $P$ a palindrome, and that it is a Lyndon word.

9. ◦ Use [Witt's formula](/witt-formula/) to count the Lyndon words of length 6 over four letters, and the formula for [necklaces](/necklace/) to count the necklaces of length 4 over four letters.

10. • Give a binary word of length 10 that has the periods 5 and 7 but not the period 1. Use the [Fine and Wilf theorem](/fine-and-wilf-theorem/) to explain why no binary word of length 11 can do the same.

11. • Compute the [Lyndon array](/lyndon-array/) of $\texttt{abbaabab}$, and read the Lyndon factorization of the word off the array.

12. • The word $\texttt{aabab}$ has smallest period 5. Compute its local period at each of the cuts 1 to 4, and find its [critical](/critical-factorization/) cuts.

13. • Run [greedy merging](/greedy-superstring-merge/) on the set $\{\texttt{bbaa}, \texttt{abaab}, \texttt{bbb}, \texttt{baaba}\}$, and compare its result with a [shortest common superstring](/shortest-common-superstring/) of the set.

14. • List all [runs](/maximal-repetition/) of $\texttt{abbabbabab}$ with their periods and exponents. Check the number of runs and the sum of the exponents against the bounds of the [runs theorem](/runs-theorem/).

15. • Show that more than a fraction $(k - 2)/(k - 1)$ of the $k^n$ words of length $n$ over $k$ letters are unbordered. What does this give for $k = 3$ and for $k = 2$?

16. • In the [de Bruijn graph](/de-bruijn-graph/) whose vertices are the $k^m$ words of length $m$ over $k \ge 2$ letters, with an edge from $x$ to $y$ when $x$ without its first letter equals $y$ without its last letter, show that any vertex reaches any vertex by a path of exactly $m$ edges, and that the diameter of the graph is $m$.

17. • A [de Bruijn sequence](/de-bruijn-sequence/) of order $n$ over $k$ letters is read cyclically. Show that each word of length $j \le n$ occurs in it exactly $k^{n-j}$ times. How many letters $b$ does a binary de Bruijn sequence of order $n$ over $\{a, b\}$ contain?

18. • A binary word of length 6 has, over $\{a, b\}$, exactly the minimal absent words $\texttt{aa}$, $\texttt{aba}$, $\texttt{abba}$, $\texttt{babb}$ and $\texttt{bbbb}$. Find the word, and explain why there is only one.

19. • Show that the number of binary words of length $2n$ that are [Abelian squares](/abelian-square/) is $\binom{2n}{n}$. List the six of length 4.

20. • Show that $a^m b^m$, for $m \ge 1$, has exactly $m^2 + 2$ distinct factors that are Lyndon words, while its Lyndon array has only $2m$ entries.

21. ★ Show that two nonempty words satisfy $uv = vu$ if and only if $u^{|v|} = v^{|u|}$.

22. ★ The [Thue-Morse word](/thue-morse-word/) $t = \texttt{abbabaabbaababba}\cdots$ is the fixed point of $a \mapsto ab$, $b \mapsto ba$. Show that every square $uu$ in $t$ with $|u|$ odd has $|u| = 1$ or $|u| = 3$, and find squares of both lengths in $t$.

23. ★ Show that a shortest common superstring of a set of distinct strings of length 2 can be found in polynomial time, and give its length by a formula. Find one for $\{\texttt{ab}, \texttt{bc}, \texttt{ca}, \texttt{bd}, \texttt{db}, \texttt{ad}\}$.

24. ★ Show that the number of binary Lyndon words of length $n$ with exactly $j$ letters $b$ is $\frac{1}{n} \sum_{d \mid \gcd(n, j)} \mu(d) \binom{n/d}{j/d}$, and that the number of binary necklaces of length $n$ with $j$ letters $b$ is the same sum with Euler's $\varphi(d)$ in place of $\mu(d)$. Evaluate the first for $n = 8$, $j = 4$ and the second for $n = 6$, $j = 3$.

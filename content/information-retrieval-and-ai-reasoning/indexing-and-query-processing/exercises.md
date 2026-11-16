1. ◦ Four documents are d1 "red fish blue fish", d2 "one fish two fish", d3 "red hat" and d4 "blue hat red sky". Write the [posting lists](/posting-list/) of red, blue, hat and fish, with the term frequency in each posting. Answer the Boolean query (red OR blue) AND NOT hat. How many cells of the [term-document incidence matrix](/term-document-incidence-matrix/) are 0?

2. ◦ Run [merge-based intersection](/merge-based-list-intersection/) on $A = (2, 5, 9, 14, 20)$ and $B = (3, 5, 8, 14, 15, 21)$, counting each three-way comparison as one step. What is the result, how many steps does it take, and what is the worst-case bound for these lengths?

3. ◦ A term occurs in documents 5, 6, 13, 140 and 1000 of a collection of 1000 documents. Write the gaps of its list. How many bits do the gaps take with [variable-byte encoding](/variable-byte-encoding/), with [Elias gamma coding](/elias-gamma-coding/), and how many do the ids take with a fixed width of 10 bits each?

4. ◦ Assume that [Zipf's law](/zipfs-law/) holds exactly with $\alpha = 1$ over a vocabulary of 1000 terms. What share of the tokens do the 10 most frequent terms cover? Then take the [Heaps' law](/heaps-law/) fit $M = 44\,T^{0.49}$. By what factor does the vocabulary grow when the collection grows 100 times, and how many terms does the fit predict for $10^9$ tokens?

5. ◦ Give the stems that the [Porter stemmer](/porter-stemmer/) produces for queries, merging, compression, documents and relevance.

6. ◦ A [positional index](/positional-index/) holds to ⟨1: 0, 4, 9⟩ ⟨2: 2⟩ ⟨5: 1, 7⟩ and be ⟨1: 1, 6⟩ ⟨2: 5⟩ ⟨5: 8⟩ ⟨6: 3⟩, as document: positions. Where does the phrase "to be" occur? Which pairs of positions satisfy the proximity query to /2 be, with the two words at most 2 positions apart in either order?

7. ◦ The vocabulary is bred, read, red, reduced, rested and retired. For the [wildcard query](/wildcard-query/) `re*ed`, which 3-grams does the [k-gram index](/k-gram-index/) look up (with \$ marking the ends of a term), which candidates does it return, and which survive the final check? Which key does the [permuterm index](/permuterm-index/) search for, and which terms does it find?

8. ◦ [Logarithmic merging](/logarithmic-merging/) runs with a buffer of $n = 1000$ postings, and the buffer has been flushed 11 times. Which disk indexes exist, and how many postings does each hold? How many postings have the merges written in total, counting each merge of two indexes as in the entry?

9. • The query $a$ AND $b$ AND $c$ has the lists $a = (4, 9)$, $b = (1, 2, 4, 6, 9, 11)$ and $c = (2, 3, 4, 5, 7, 8, 9, 10, 12, 13)$. Intersect them pairwise by merges, first shortest list first ($a$, then $b$, then $c$) and then longest first ($c$, then $b$, then $a$). Count the three-way comparisons of each order.

10. • The bound of [small versus small](/small-versus-small-intersection/) for lists of lengths $m \le n$ is $2m \log_2(1 + n/m) + 3m$ tests, and the merge makes at most $m + n - 1$. Write $n = rm$. For $m \ge 10$, what is the smallest integer $r$ for which the galloping bound is below the merge bound? Explain why this compares bounds, not the counts on a given input.

11. • Encode with [Simple-9](/simple-9/), as the greedy encoder of the entry does, the gaps of the list 3, 4, 5, 6, 8, 9, 10, 11, 12, 13, 14, 15, 16, 40, 41, 42, 43, 44, 45, 46, 300, 301. Give the selector and the number of values of each word, and compare the total size with variable-byte and Elias gamma codes of the same gaps.

12. • [Front-code](/front-coding/) the sorted terms index, indexed, indexer, indexes, indexing and indices with blocks of $k = 1, 2, 3$ and 6 terms. Count bytes as in the entry: one byte for each length, the rest of each term in full, and leave out the number of strings at the start.

13. • The four documents of the first exercise are split by [index partitioning](/index-partitioning/) into node 1 with d1 and d2 and node 2 with d3 and d4. Score the query "red fish" with the weight $\mathrm{tf} \cdot \lg(N/\mathrm{df})$, once with global statistics and once with the statistics of each node. Which documents get the local score 0, and why?

14. • A [signature file](/signature-file/) uses signatures of $F = 64$ bits for documents of $D = 20$ distinct terms, each term setting $m$ distinct bits. With the exact false-drop formula of the entry, which $m$ gives the lowest false-drop rate for a one-term query, and what is the rate? Answer the same for $F = 128$.

15. • A query has three terms with integer weights: $a$ has weight 1 in d1 to d8; $b$ has weight 2 in d2, 1 in d4 and 2 in d7; $c$ has weight 4 in d3 and 2 in d6. Run [WAND](/wand/) for $k = 1$ with the list maxima as upper bounds. Which documents does it fully score, and what does it return?

16. • Run [MaxScore](/maxscore/) on the index of the previous exercise with $k = 1$. Which lists are essential after the heap holds d3? Which documents are fully scored, which are started and stopped early, and which are never looked at?

17. • [Geometric partitioning](/geometric-partitioning/) writes $(t \bmod r^{v+1})\,b$ postings at flush $t$, where $r^v$ is the largest power of $r$ that divides $t$. Show that for $r = 2$ this is $2^{v} b$, and prove that $m = 2^j$ flushes write $(j/2 + 1) m b$ postings in total. Check the formula for $j = 3$ and $j = 10$, and relate the value for $j = 3$ and $b = 4$ to the counts in the entry on logarithmic merging.

18. • A collection has 8000 distinct terms after $10^5$ tokens and 100,000 after $10^7$ tokens. Fit Heaps' law $M = kT^b$ through these two points, and predict the vocabulary at $10^9$ tokens.

19. • An [impact-ordered index](/impact-ordered-index/) has three query terms. Term $x$ has impact 5 in d3 and impact 2 in d1, d4 and d6. Term $y$ has impact 4 in d1 and d3 and impact 1 in d2 and d5. Term $z$ has impact 3 in d4, 2 in d2, and 1 in d1 and d6. Evaluate score at a time with the safe stop of the entry and $k = 1$, taking segments of equal impact in the order $x, y, z$. After how many segments and postings does it stop, and why does it not stop one segment earlier?

20. ★ The greedy Simple-9 encoder is not always optimal. Write a dynamic program for the least number of words, where each word except the last holds exactly $c_s$ values of its layout. Run both on 7, 20, 100, 1, 9, 3, 5, 15, 0, 7, 100, 1, 5, 1 and give the layouts of each.

21. ★ Use the cost model of [partitioned Elias-Fano](/partitioned-elias-fano/) on the 20 ids 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 60, 130, 200, 210, 212, 213, 215, 216, 218, 219. Find the cuts of least total size for $F = 8$ and for $F = 16$ bits for each chunk, with the kind and payload of each chunk, and compare with a single chunk.

22. ★ Six documents are 1 "red fish", 2 "blue car", 3 "red fish blue", 4 "car road", 5 "fish sea" and 6 "road car blue". The log-gap cost of an order is the sum of $\lfloor \lg g \rfloor + 1$ over all gaps $g$ of all lists, the first gap of a list being its first id. Find the cost of the input order, the least cost over all $720$ orders, and how many orders reach it. Is the cost of an order always equal to the cost of its reverse? This is the objective of [document identifier reassignment](/document-identifier-reassignment/).

23. ★ In the random text model of Heaps' law, the tokens are independent draws with $p_i = i^{-3}/\zeta(3)$. Derive Heaps' law with $b = 1/3$, give the constant $k$, and compare the prediction at $T = 10^6$ tokens with the exact expectation $\sum_i \left(1 - (1 - p_i)^T\right)$.

24. ★ Implement small versus small, the [Baeza-Yates method](/baeza-yates-intersection/) and [adaptive intersection](/adaptive-set-intersection/) with the test counts of their entries, and check your counts on the worked examples of the entries. Then intersect $A = (9, 10, 45, 57)$ with $B = (3, 6, 9, \ldots, 60)$, the 20 multiples of 3. Give the result and the number of tests of each method, against the steps of the merge.

1. ◦ A heap has the objects A to G. The roots point to A and D, and the pointers are A → B, B → C, D → B, E → F, F → E and F → G. Which objects are [reachable](/heap-reachability/) and which are [garbage](/garbage/)? With exact [reference counts](/reference-counting/) and no cycle collector, give the count of each garbage object and say which of them are ever freed.

2. ◦ A heap holds $L = 20$ live words, and $H = 100$ words in all. With unit costs $c = m = s = 1$, compute the cost per allocated word of copying and of mark-and-sweep from the formulas of the [space-time tradeoff](/gc-space-time-tradeoff/). Find the smallest $H$ for which copying costs at most $1/4$ per word, and the mark-and-sweep cost at that $H$.

3. ◦ From-space holds A with fields (B, C), B with the field (D), C with the field (A), D with no fields, and E with the field (D). Each object takes one header word and one word per field. The first root points to C and the second to A, and to-space starts at address 0. Run [Cheney's collector](/cheney-copying-collector/): give the address of each copy, and the values of $\mathit{scan}$ and $\mathit{free}$ after the roots and after each object is scanned. Which object is never copied?

4. ◦ A [mark-and-sweep](/mark-and-sweep/) heap has $n = 1000$ cells, $L = 600$ of them live, with $c_m = 5$ and $c_s = 1$. Compute the collection cost per allocated cell, and again for $n = 2000$ with the same $L$. In the first heap every block has the live fraction $f = 0.6$; with [lazy sweeping](/lazy-sweeping/), how many cell visits does each allocation make on average, and how many do the 400 allocations make together?

5. ◦ A heap of 13 words holds A at 0 (3 words, garbage), B at 3 (2 words, live), C at 5 (4 words, garbage), D at 9 (1 word, live) and E at 10 (3 words, live). A field of B points to E. Give the forwarding address of each live object under [Lisp 2 compaction](/lisp2-compaction/), the new value of the field of B, the first free word after compaction, and the number of words moved. Why does [two-finger compaction](/two-finger-compaction/) not apply to this heap?

6. ◦ In the model of the [generational hypothesis](/generational-hypothesis/), 80 percent of the objects have lifetime exactly 2 and 20 percent lifetime exactly 100. Compute $\sigma(10)$, $\sigma(100)$ and $\sigma(1000)$, and the hazard $h(a)$ at every age. Does the strong form hold?

7. ◦ An old generation has $2^{27}$ words of 8 bytes, with [cards](/card-marking/) of $2^6$ words and one byte per card. How many bytes does the card table take, and what fraction of the old generation is that? Which card holds the slot at word 100000? If a minor collection finds only 3 dirty cards, how many card bytes does it read?

8. ◦ [Baker's collector](/baker-real-time-collector/) runs with at most $L = 1000$ reachable cells. For $k = 4$, what semispace size does the pacing theorem ask for, and what is the whole heap? Find the smallest $k$ for which the theorem allows a whole heap of at most 2200 cells.

9. ◦ An object F has a [finalizer](/finalization/) and refers to G, which nothing else refers to. F becomes unreachable before collection 1, and its finalizer runs between collections 1 and 2. At which collection are F and G freed if the finalizer does not store F anywhere? If the finalizer stores F into a global $g$, and much later the program sets $g$ to nil, how many times does the finalizer run in Java, and when are F and G freed?

10. • With unit costs $c = m = s = 1$, find the ratio $k = H/L$ above which copying costs less per allocated word than mark-and-sweep, and the common cost at that ratio. Do the same for $c = m = 1$ and $s = 1/4$, a cheap sweep. Which method is cheaper at $k = 2.5$ with unit costs?

11. • The roots point to A and B. For each state, say whether the strong and the weak [tricolor](/tricolor-marking/) invariants hold. (a) A is black and points to B, B is gray and points to C, C is white. (b) A is black and points to C, B is gray and points to C, C is white. (c) A is black and points to C, B is gray and points to D, D is white and points to C, C is white. (d) As (c), but D is black. Then prove that when no object is gray, the weak invariant implies the strong one.

12. • A is black and A.f is nil. B is gray and B.g points to C, which is white, and nothing else points to C. The mutator runs A.f ← B.g and then B.g ← nil; its registers hold no pointer to C afterwards, and the roots are not rescanned. Then the collector scans B and finishes. With no barrier, with Dijkstra's and with Steele's [incremental update](/incremental-update-barrier/) barriers and with Yuasa's [deletion barrier](/snapshot-at-the-beginning/), say which invariant holds just after the first store and whether C is freed.

13. • At the start of a cycle the root $r$ points to X, X.f points to Y, and Y has no fields. The collector scans the roots, so X is gray. The mutator then allocates N into the root $r_2$, sets X.f ← nil, and sets $r_2$ ← nil. The collector finishes marking and sweeps. Which of X, Y and N survive with Yuasa's barrier and black allocation, and which with Dijkstra's barrier, white allocation and a rescan of the roots at the end? Which survivors are floating garbage?

14. • The pointers are A → B, B → A, B → C, C → D, D → C and E → C, and the roots point to A and E. The program clears the root to A. Run [trial deletion](/trial-deletion/) with A as the only candidate, with children visited in the order listed. Give the counts after MARK-GRAY, the colors and counts after SCAN, and the objects that COLLECT-WHITE frees. Is the final count of C right?

15. • In [weighted reference counting](/weighted-reference-counting/) with $W = 8$, the program creates $x$ with the reference $a$, runs COPY($a$) seven times, and then deletes all eight references. How many indirection cells are made, and how many messages are sent in all? How many would plain distributed reference counting send? Before the deletes, how many cells does a use of $a$ pass through?

16. • Use the lifetimes of Exercise 6 in the [pause model](/generational-collector-pause-tradeoff/) with $c_0 = c_r = 0$ and $c = 1$. For $(N, T) = (10, 1)$, $(10, 2)$ and $(20, 1)$, give the pause, the work per allocation, the promotion rate and the number of objects of lifetime 2 promoted per allocation.

17. • In the same pause model, prove that for a fixed nursery size $N$ the number of objects promoted per collection, $P(TN) - P((T-1)N)$, is nonincreasing in $T$, and that the pause satisfies $P(TN) \le T\,P(N)$.

18. • A card scan costs $|M|/2^k + d \cdot 2^k$: one read per card byte and one per word on a dirty card. Let $|M| = 2^{27}$ words and let $d = 2^9$ dirty cards, whatever the card size. Find the card size that minimizes the cost, the cost there, and the ratio to the cost with cards of $2^6$ words.

19. • A collector handles [ephemerons](/ephemeron/) naively: it marks from the roots, then makes passes over the list of ephemerons, marking from the value of each ephemeron whose key is marked and whose value is not, until a pass marks nothing. Ephemeron $E_i$ has key $K_i$ and value $V_i$ for $i = 1, \ldots, n$; $V_i$ points to $K_{i+1}$ for $i < n$, and a root points to $K_1$. Which objects survive? How many passes does the collector make when the list is $E_1, \ldots, E_n$, and when it is $E_n, \ldots, E_1$? How many ephemeron visits is that?

20. • An [Immix](/immix-collector/) block has 256 lines of 128 bytes. After a collection, lines 0, 1, 5 and 9 are marked, each by a small object that starts there. List the holes the allocator uses and the bytes they offer. Where does the next object of 64 bytes go if the current hole is the first one, and what happens to an object of 300 bytes?

21. ★ Prove that for any costs $c, m, s > 0$ there is exactly one ratio $k^* > 2$ at which copying and mark-and-sweep cost the same per allocated word, that copying is cheaper exactly when $k > k^*$, and give $k^*$ as the root of a quadratic. Check it against Exercise 10.

22. ★ [Garbage-First](/garbage-first-collector/) picks old regions with garbage $g_i$ and cost $c_i$ under a budget $B$ by ratio $g_i/c_i$, and stops at the first region that does not fit. Assume $c_i \le B$ for every region. Prove that the better of this set and the best single region reclaims at least half of the most that any set within $B$ reclaims. Apply the combined rule to the entry's instance with $B = 10$ and the regions $(10, 1)$ and $(90, 10)$.

23. ★ Let $F(X) = R \cup \mathrm{succ}(X)$ on a finite heap, where $R$ is the set of objects the roots point to. (a) Let $R = \{A\}$, A have no fields, and the pointers be B → C, C → B, C → D and E → B. List every fixed point of $F$, name the least and the greatest, and say which objects plain reference counting keeps. (b) A heap has $j$ disjoint garbage cycles, no other garbage, and no pointer into a cycle from outside it. Show that $F$ has exactly $2^j$ fixed points.

24. ★ Take one marking cycle in which the mutator touches only objects it can reach, and run an incremental update collector (Dijkstra's barrier, white allocation, roots rescanned at the end) and a snapshot collector (Yuasa's barrier, black allocation) on the same schedule, sweeping at the same point. Prove that every object the incremental update collector keeps is kept by the snapshot collector. Give a schedule where the inclusion is strict.

25. ★ In weighted reference counting with $W = 2^k$, a program starts with one reference and only copies. Show that if it always copies the same reference, the first indirection cell appears at copy $k + 1$. Show that whatever it copies, some copy among the first $W$ makes a cell, and that always copying a reference of largest weight makes the first cell at copy $W$ exactly.

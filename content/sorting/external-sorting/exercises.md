1. ◦ List the maximal [sorted runs](/sorted-run/) of $\langle 6, 2, 9, 9, 4, 1, 7, 8, 3 \rangle$. How many maximal runs does a random permutation of nine distinct keys have on average?

2. ◦ Run [replacement selection](/replacement-selection/) with a heap of $P = 3$ items on $\langle 4, 9, 2, 7, 1, 8, 5, 3, 6, 10 \rangle$. Give the runs. How many runs does sorting each memoryload of 3 items give?

3. ◦ Merge the four runs $\langle 2, 9 \rangle$, $\langle 5, 6 \rangle$, $\langle 1, 8 \rangle$ and $\langle 3, 7 \rangle$ with a tree of losers, as in the [k-way merge](/k-way-merge/). Which loser sits at each of the three inner nodes after the tree is built, and after the next item of the first winner's run is played in? How many comparisons does each replay make?

4. ◦ A file holds $N = 2 \cdot 10^6$ items, memory holds $M = 5000$ items and a block holds $B = 100$ items. How many runs does [external merge sort](/external-merge-sort/) make, what is its fan-in, how many merge passes does it need, and how many block transfers does it make in all? How many transfers would it make if it merged only two runs at a time?

5. ◦ Memory holds $M = 10^6$ items and a block holds $B = 1000$ items. About how large a file can external merge sort sort with one merge pass? With [double buffering](/double-buffering/) for every run? With single buffers and runs made by replacement selection, on random input?

6. ◦ A file has $S = 200$ initial runs. How many merge passes does the [balanced merge sort](/balanced-merge-sort/) need on 4, 6 and 8 tapes? How many merge levels does the [oscillating sort](/oscillating-sort/) need on 5 and on 6 tapes?

7. ◦ Run the [polyphase merge sort](/polyphase-merge-sort/) on 3 tapes with $S = 8$ initial runs of equal length. Give the number of runs on each tape after each phase. How many items do the merges move in all, as a multiple of $N$? Compare with the merge passes of a balanced merge on 4 tapes.

8. ◦ For 5 tapes, compute the totals of the perfect distributions of the polyphase merge and of the [cascade merge](/cascade-merge-sort/) up to the first total of at least 30. With $S = 30$ runs, how many phases does the polyphase merge need and how many dummy runs? How many passes does the cascade merge need?

9. ◦ One level of [external samplesort](/external-samplesort/) uses the splitters 4 and 9 on $\langle 7, 2, 9, 4, 4, 11, 1, 6, 4, 13, 8, 3 \rangle$. List the five buckets, with their items in the order the distribution pass writes them. Which buckets need a recursive call?

10. • Prove that every run of replacement selection except the last has at least $P$ items, so that it never makes more runs than sorting each memoryload. Then show that on an input in decreasing order every run except the last has exactly $P$ items.

11. • An input of distinct keys is *$P$-close* if each key is fewer than $P$ places from its position in sorted order. Prove that replacement selection with a heap of $P$ items turns a $P$-close input into a single run.

12. • Show that halving the number of runs saves at most one merge pass of an external merge sort with fan-in $k \ge 2$. With $k = 10$, give a number of runs $r$ for which going from $r$ to $r/2$ runs saves a pass, and one for which it saves none.

13. • Merge $k$ runs of $n/k$ items each by merging the first with the second, then the result with the third, and so on. Show that this moves exactly $n(k+1)/2 - n/k$ items. How many does a balanced tree of two-way merges move when $k$ is a power of 2?

14. • An external merge sort has $r = 30$ runs of equal length and fan-in $k = 10$. Instead of two full passes, its first pass merges only enough runs to leave exactly 10 for the final merge. How many runs must the first pass merge, and what fraction of the data does it read and write? Show that no plan with one partial pass and one full merge does better.

15. • A file of $N$ records has only $K$ distinct keys, and memory holds $K$ counters and $K + 1$ blocks. Sort it with about $3n$ block transfers, where $n = N/B$, by adapting [counting sort](/counting-sort/) to external memory.

16. • A key sort reads the $n$ blocks of records once to pull out the (key, record number) pairs, sorts the pairs, and then gathers the records, as in [external permuting](/external-permuting/). Count the gather as $N + n$ transfers, its cost when no two records of an output block come from the same input block, and ignore the cost of sorting the pairs. Show that the key sort beats an external merge sort with $p$ merge passes exactly when $B < 2p$. For which $B$ does it win when one merge pass is enough?

17. • Show that external merge sort makes about $N \lg N$ comparisons in all when its merges use a tree of losers, whatever the values of $M$ and $B$: count run formation and the merge passes separately.

18. • Show that for 3 tapes the perfect distribution of level $\ell$ of the polyphase merge is $(F_{\ell+1}, F_\ell)$, where $F_\ell$ are the [Fibonacci numbers](/fibonacci-numbers/). With $S = 100$ runs, how many phases are needed, and how many dummy runs?

19. • Show that [funnelsort](/funnelsort/) makes about $N \lg N$ comparisons, the same leading term as binary merge sort, using that a $k$-funnel passes each item through $\lg k$ binary mergers.

20. ★ Let $R$ be the number of maximal runs of a random permutation of $n \ge 2$ distinct keys. Prove that $\operatorname{Var}(R) = (n+1)/12$.

21. ★ For 4 tapes, show that the first entries of the polyphase perfect distributions, and also their totals $1, 3, 5, 9, 17, 31, \ldots$, satisfy $x_\ell = x_{\ell-1} + x_{\ell-2} + x_{\ell-3}$ from some level on. Conclude that the number of phases for $S$ runs is about $\log S / \log \lambda$, where $\lambda \approx 1.839$ is the real root of $x^3 = x^2 + x + 1$.

22. ★ A $k$-funnel has a top funnel with about $\sqrt k$ leaves, about $\sqrt k$ bottom funnels with about $\sqrt k$ leaves each, and a buffer of $\lceil k^{3/2} \rceil$ items at the root of each bottom funnel. Prove that it uses $O(k^2)$ space.

23. ★ Show that the item of rank $i$ in a file of $N$ items can be found with $O(N/B)$ block transfers, so that selection is cheaper than sorting in external memory too. Adapt the [median of medians](/median-of-medians/), and count the transfers of each step.

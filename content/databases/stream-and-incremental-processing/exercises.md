1. ◦ A [materialized view](/materialized-view/) keeps `AVG(amount)` per store. Store $s_1$ has three sales with total 300, and store $s_2$ has one sale of 200; both are in the same region. Compute the true average for the region and the average of the two store averages. What should the view store so that it can answer the region query?

2. ◦ Let $R(a, b) = \{(1,1), (2,1), (2,2), (3,3)\}$, $S(b, c) = \{(1,u), (2,v)\}$ and $V = \pi_a(R \bowtie S)$ with a count of derivations for each tuple. Give $V$. Then one update inserts $R(3,1)$, deletes $S(1,u)$ and inserts $S(3,w)$. Compute $\Delta V$ with the three terms of the join rule of [incremental view maintenance](/incremental-view-maintenance/), and check the new $V$ against a recomputation.

3. ◦ A view $V = \sigma_{\mathit{amount} > 100}(\mathit{Sales})$ stores whole rows. For each update say whether it can change $V$, and whether $V$ can be maintained from the update and $V$ alone, without reading $\mathit{Sales}$, that is, whether it is [self-maintainable](/self-maintainable-view/): (a) insert a sale of 50; (b) insert a sale of 200; (c) delete a sale of 200. Then answer the same for $V = \pi_{\mathit{store}}(\mathit{Sales})$ as a set without counts, under the deletion of one sale.

4. ◦ The program $\mathit{path}(x, y) \leftarrow \mathit{edge}(x, y)$; $\mathit{path}(x, y) \leftarrow \mathit{edge}(x, z), \mathit{path}(z, y)$ runs on the edges $1 \to 2$, $2 \to 3$, $3 \to 4$ and $2 \to 4$. Run the [DRed algorithm](/dred-algorithm/) for the deletion of $2 \to 3$: give the overdeleted facts, the rederived facts, the facts added by the insert phase and the new model.

5. ◦ A stream has the elements $a$ at time 0, $b$ and $c$ at time 1, $d$ at time 3 and $e$ at time 6. In the [CQL stream model](/cql-stream-model/), give the relation $S\,[\mathrm{Range}\ 2]$ at each instant from 0 to 9, and the streams Istream and Dstream of it. Then give the relation `SELECT COUNT(*)` over the window at each instant, and the elements of its Istream.

6. ◦ Events arrive with the event times 3, 1, 5, 4, 9, 2, 8, 7, in this order. The [watermark](/event-time-watermark/) is the largest event time seen so far minus $D = 3$, and an element is late if its event time is below the watermark when it arrives. Which elements are late? A tumbling window $[0, 5)$ fires when the watermark reaches 5: after which arrival does it fire, and which elements does it hold?

7. ◦ A [symmetric hash join](/symmetric-hash-join/) on the key receives, in order, a tuple of $R$ with key 1, a tuple of $S$ with key 1, one of $S$ with key 2, one of $R$ with key 1, one of $R$ with key 2 and one of $S$ with key 1. How many results does each arrival emit? Check the total against the join of the two complete inputs.

8. ◦ The pattern $\mathrm{SEQ}(a, b, c)\ \mathrm{WITHIN}\ 10$ of [complex event processing](/complex-event-processing/) runs on the events $a@1$, $b@2$, $a@3$, $b@4$, $c@5$, $c@12$, where the window bounds the span from the first to the last event of a match. List the matches under strict contiguity, under skip till next match and under skip till any match.

9. ◦ In [DBSP](/dbsp/), $I$ is the running sum of a stream, $D$ its difference with the delayed stream, and $z^{-1}$ the delay, which starts with 0. For the stream of integers $s = 3, -1, 4, 0, 2$, compute $z^{-1}(s)$, $I(s)$, $D(s)$, $D(I(s))$ and $I(D(s))$.

10. • Let $V = R \bowtie S \bowtie T$, and let one update change all three relations. Write $\Delta V$ in terms of the old relations and the deltas, and show that it has 7 terms. How many terms does the rule have for a join of $k$ relations when $j$ of them change?

11. • A view keeps `MAX(amount)` per store. Show that no state of bounded size per store is enough to maintain it under deletions. Then design a structure per store that supports an insertion and a deletion in $O(\log m)$ time for $m$ sales, and compare its space with that of the base table.

12. • In [deferred maintenance](/deferred-view-maintenance/), the refresh runs after the update and sees only the new states $R' = R + \Delta R$ and $S' = S + \Delta S$. On the data of exercise 2, compute $\Delta R \bowtie S' + R' \bowtie \Delta S$ and show that it is wrong. Then derive the correct formula in terms of $R'$, $S'$, $\Delta R$ and $\Delta S$.

13. • Run DRed with the program of exercise 4 on the chain $1 \to 2 \to \cdots \to 10$, deleting the edge $5 \to 6$. Count the facts that are overdeleted, rederived and added, and the size of the new model. Then add the edges $i \to i + 2$ for $1 \le i \le 8$ and delete $5 \to 6$ again. How many facts does the new model lose, and how many did DRed overdelete?

14. • Say which views are [self-maintainable](/self-maintainable-view/) for which changes, with a reason or a pair of databases that refutes it: (a) $\gamma_{G;\,\mathrm{COUNT}(*)}(R)$ under insertions and deletions; (b) $\gamma_{G;\,\mathrm{SUM}(X)}(R)$ under insertions only; (c) $\gamma_{G;\,\mathrm{MIN}(X)}(R)$ under deletions; (d) the set projection $\pi_A(R)$ under deletions, when $A$ is a key of $R$; (e) the set join $R \bowtie S$ under deletions from $S$.

15. • The query $Q$ counts the tuples of $R(A, B) \bowtie S(B, C)$. [Higher-order IVM](/higher-order-ivm/) keeps $Q$ and the maps $M_R[b]$ and $M_S[b]$, the numbers of tuples of $R$ and of $S$ with $B = b$. Write the update rules for an insertion or a deletion in each relation, and run them on: insert $R(1, x)$, insert $S(x, 5)$, insert $S(x, 6)$, insert $R(2, x)$, delete $S(x, 5)$, insert $S(y, 7)$. What does first-order maintenance, which keeps only $Q$, have to read for each update?

16. • For the arrivals of exercise 6, find the smallest $D$ for which no element is late, and say after which arrival the window $[0, 5)$ fires with that $D$. Explain the trade-off between lateness and delay that the two values of $D$ show.

17. • A [FlatFAT](/flatfat/) has $n = 8$ leaves, numbered 1 to 8. Count the calls of the combine operation for an update that rewrites (a) leaf 5 alone; (b) leaves 1 to 4; (c) leaves 2, 4, 6 and 8; (d) leaves 1 and 8. Compare each count with the bound $m(1 + \lceil \log_2(n/m) \rceil)$ for $m$ rewritten leaves.

18. • A query has three unit-time operators, and the size of a tuple is 1 at the start, then $1/2$, $2/5$ and 0 after each operator. Find the lower envelope of its progress chart and the priorities that [Chain scheduling](/chain-scheduling/) gives to the three operators. Is the chart convex? A second query has one operator that takes a tuple from size 1 to 0. Which of the two waiting tuples, one at the start of each query, does Chain run first?

19. • An operator keeps the sum of its two inputs $A$ and $B$, under [asynchronous barrier snapshotting](/asynchronous-barrier-snapshotting/). $A$ sends 1, a barrier, then 2; $B$ sends 10, then a barrier. The operator receives 1, the barrier of $A$, 2, 10 and the barrier of $B$, in this order. Give the snapshot and the sum after recovery from it, when the sources replay what follows their barriers, (a) with alignment, (b) when the operator copies its state at the first barrier without blocking, (c) when it copies at the last barrier without blocking.

20. • Show that under skip till any match, without a window, the pattern $\mathrm{SEQ}(E_1, \dots, E_k)$ can have $(n/k)^k$ matches on a stream of $n$ events, so that any algorithm needs $\Omega(n + T)$ time for $T$ matches and no bound in $n$ alone. Then show that under strict contiguity there are at most $n - k + 1$ matches.

21. ★ Bag difference keeps $\max(0, m_R(t) - m_S(t))$ copies of each tuple $t$. Show that the stored view $V = R - S$ alone is not enough to maintain it under deletions from $S$. Give a delta rule that is correct when the view also keeps $m_R(t)$ and $m_S(t)$ for each $t$ in $R$ or $S$, and prove it.

22. ★ On the cycle $1 \to 2 \to \cdots \to n \to 1$, delete the edge $n \to 1$ and run DRed with the program of exercise 4. Prove that it overdeletes all $n^2$ path facts, rederives $n - 1$ of them, and adds $(n - 1)(n - 2)/2$ in the insert phase. Check the counts for $n = 3$ against the example of the DRed entry.

23. ★ Prove that the symmetric hash join emits each pair of matching tuples exactly once, at the arrival of the later of the two. Then show that any join that emits each result at that moment must keep all the tuples it has seen with distinct keys: give an adversary that, after any $n$ arrivals, chooses a next tuple whose results the join cannot emit without the tuple it dropped.

24. ★ Let $\times$ be bilinear and $Q(a, b) = a \times b$ on streams. From $Q^\Delta = D \circ Q \circ I$, prove the DBSP rule $(a \times b)^\Delta = a \times b + z^{-1}(I(a)) \times b + a \times z^{-1}(I(b))$. Show that for the join of Z-sets it is the three-term delta rule of exercise 2, and say which state the incremental circuit keeps.

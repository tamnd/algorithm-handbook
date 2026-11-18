1. ◦ A [materialized view](/materialized-view/) keeps `AVG(amount)` per store. Store $s_1$ has three sales with total 300, and store $s_2$ has one sale of 200; both are in the same region. Compute the true average for the region and the average of the two store averages. What should the view store so that it can answer the region query?

2. ◦ Let $R(a, b) = \{(1,1), (2,1), (2,2), (3,3)\}$, $S(b, c) = \{(1,u), (2,v)\}$ and $V = \pi_a(R \bowtie S)$ with a count of derivations for each tuple. Give $V$. Then one update inserts $R(3,1)$, deletes $S(1,u)$ and inserts $S(3,w)$. Compute $\Delta V$ with the three terms of the join rule of [incremental view maintenance](/incremental-view-maintenance/), and check the new $V$ against a recomputation.

3. ◦ A view $V = \sigma_{\mathit{amount} > 100}(\mathit{Sales})$ stores whole rows. For each update say whether it can change $V$, and whether $V$ can be maintained from the update and $V$ alone, without reading $\mathit{Sales}$: (a) insert a sale of 50; (b) insert a sale of 200; (c) delete a sale of 200. Then answer the same for $V = \pi_{\mathit{store}}(\mathit{Sales})$ as a set without counts, under the deletion of one sale.

4. ◦ The program $\mathit{path}(x, y) \leftarrow \mathit{edge}(x, y)$; $\mathit{path}(x, y) \leftarrow \mathit{edge}(x, z), \mathit{path}(z, y)$ runs on the edges $1 \to 2$, $2 \to 3$, $3 \to 4$ and $2 \to 4$. Run the [DRed algorithm](/dred-algorithm/) for the deletion of $2 \to 3$: give the overdeleted facts, the rederived facts, the facts added by the insert phase and the new model.

5. • Let $V = R \bowtie S \bowtie T$, and let one update change all three relations. Write $\Delta V$ in terms of the old relations and the deltas, and show that it has 7 terms. How many terms does the rule have for a join of $k$ relations when $j$ of them change?

6. • A view keeps `MAX(amount)` per store. Show that no state of bounded size per store is enough to maintain it under deletions. Then design a structure per store that supports an insertion and a deletion in $O(\log m)$ time for $m$ sales, and compare its space with that of the base table.

7. • In deferred maintenance, the refresh runs after the update and sees only the new states $R' = R + \Delta R$ and $S' = S + \Delta S$. On the data of exercise 2, compute $\Delta R \bowtie S' + R' \bowtie \Delta S$ and show that it is wrong. Then derive the correct formula in terms of $R'$, $S'$, $\Delta R$ and $\Delta S$.

8. • Run DRed with the program of exercise 4 on the chain $1 \to 2 \to \cdots \to 10$, deleting the edge $5 \to 6$. Count the facts that are overdeleted, rederived and added, and the size of the new model. Then add the edges $i \to i + 2$ for $1 \le i \le 8$ and delete $5 \to 6$ again. How many facts does the new model lose, and how many did DRed overdelete?

9. ★ Bag difference keeps $\max(0, m_R(t) - m_S(t))$ copies of each tuple $t$. Show that the stored view $V = R - S$ alone is not enough to maintain it under deletions from $S$. Give a delta rule that is correct when the view also keeps $m_R(t)$ and $m_S(t)$ for each $t$ in $R$ or $S$, and prove it.

10. ★ On the cycle $1 \to 2 \to \cdots \to n \to 1$, delete the edge $n \to 1$ and run DRed with the program of exercise 4. Prove that it overdeletes all $n^2$ path facts, rederives $n - 1$ of them, and adds $(n - 1)(n - 2)/2$ in the insert phase. Check the counts for $n = 3$ against the example of the DRed entry.

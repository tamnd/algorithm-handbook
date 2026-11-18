## What to remember

- **Borda points.** With $n$ items, a list gives $n - i + 1$ points to its item at rank $i$, and each item missing from a partial list $L$ gets $(n - |L| + 1)/2$, so every list hands out $n(n+1)/2$ points. The Borda order sorts by total points in $O(nk + n \log n)$ time for $k$ lists.
- **Pairwise form.** On full lists, the Borda score of $x$ is $k$ plus the number of pairs (list, item) in which $x$ beats the item: $s(x) = k + \sum_{y \ne x} w_{xy}$, where $w_{xy}$ counts the lists that put $x$ above $y$. Borda adds margins, so a large win over one rival can outweigh small losses to the others.
- **What Borda gets right and wrong.** It is monotone and never ranks a Condorcet loser first on full lists. It is not Condorcet consistent, not independent of other items, and open to strategic lists.
- **Kemeny cost.** $C(\pi) = \sum_i K(\pi, \tau_i)$, the total Kendall tau distance, equals $\sum_{a \text{ before } b \text{ in } \pi} w_{ba}$. Each pair costs at least $\min(w_{ab}, w_{ba})$, with equality exactly when $\pi$ follows the strict majority on that pair; if the strict majorities form a total order, that order is the unique Kemeny ranking.
- **Kemeny is hard.** It is NP-hard already for $k = 4$ input rankings and for every even $k \ge 4$, and for every odd $k \ge 7$. With many voters, deciding whether an item is a Kemeny winner is $\Theta_2^p$-complete.
- **Kemeny is approximable.** The best input ranking and the footrule-optimal ranking are within a factor 2; KwikSort has expected ratio 2, and $11/7$ together with the best input; an LP-based pivot gives $4/3$; and there is a PTAS. Borda is within a factor 5 on full lists. The exact dynamic program over subsets takes $O(2^n n^2)$ time.

## The two rules side by side

| | Borda count | Kemeny ranking |
|---|---|---|
| Time | $O(nk + n \log n)$ | NP-hard; $O(2^n n^2 + n^2 k)$ exactly |
| Partial lists | shared points for missing items | a pair counts only in lists that order it |
| Condorcet winner ranked first | not always | always |
| Condorcet loser ranked first | never on full lists | never |
| Ratio to the Kemeny cost | at most 5 on full lists | 1 |

: The two entries of the chapter on a profile of $k$ rankings of $n$ items.

## Choosing a rule

For merging search results or other long partial lists, Borda is the usual choice: it is linear, it handles missing items, and its weights can be learned. When agreement with pairwise majorities matters, compute the Kemeny ranking exactly when the items are few, with the subset dynamic program (whose $2^n n^2$ steps limit it to about 20 items) or an integer program, or start from Borda or KwikSort and clean up with local Kemenization, which never raises the cost.

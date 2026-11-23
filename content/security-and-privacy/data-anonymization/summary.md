## What to remember

- A quasi-identifier is not an identifier alone but singles people out when joined with other data: about 87 percent of the 1990 United States population was likely unique on ZIP code, sex and date of birth (Sweeney's estimate; Golle later found about 61 percent). Removing names or replacing them by pseudonyms keeps the records linkable.
- A table is k-anonymous when every record shares its quasi-identifier values with at least $k - 1$ others; the check takes $O(nd)$ expected time. It stops the linkage of a person to fewer than $k$ records. It does not stop attribute disclosure: a group whose records share one sensitive value tells that value (homogeneity), and background knowledge can rule out the others.
- Full-domain generalization vectors form a lattice of $\prod_a (h_a + 1)$ vectors. A vector above a k-anonymous one is k-anonymous, which is what lets Samarati's algorithm binary search the heights and Incognito prune its search.
- Fewest suppressed cells is NP-hard for each fixed $k \ge 3$ (Meyerson and Williams), already for $k = 3$ with a ternary alphabet (Aggarwal et al.), while 2-anonymity is in P. The forest algorithm suppresses at most $3k - 3$ times the optimum; Park and Shim improve the ratio to $O(\log k)$.
- Entropy l-diversity asks $H(E) \ge \log l$ in each group $E$; recursive $(c, l)$-diversity asks $r_1 < c(r_l + r_{l+1} + \cdots + r_m)$ for the sorted counts $r_1 \ge r_2 \ge \cdots$. Skewed and semantically similar values defeat both.
- t-closeness bounds the earth mover's distance between each group's sensitive distribution and the table's by $t$. For $m$ ordered values the distance is $\frac{1}{m-1} \sum_i \lvert r_1 + \cdots + r_i \rvert$, with $r_j$ the difference of the shares of value $j$. It does not imply l-diversity.
- Optimal microaggregation uses groups of $k$ to $2k - 1$ records. It is a shortest path problem in one dimension and NP-hard in several.
- The post-randomization method publishes its matrix $P$. Since $\mathbb{E}[T^*] = P^{\mathsf T} T$, solving $P^{\mathsf T} \hat T = T^*$ gives an unbiased estimate of the true counts, and $P$ is $\varepsilon$-[locally private](/local-differential-privacy/) with $\varepsilon = \max_l \ln(\max_k p_{kl} / \min_k p_{kl})$.
- A table with margins leaks a small cell by subtraction. A hidden cell is checked by two linear programs, its least and greatest feasible values, and every line with a hidden cell needs a second hidden cell.

## The algorithms side by side

| Algorithm | Output | Time in the entry | What it guarantees |
|---|---|---|---|
| [Datafly](/datafly/) | one full-domain vector, at most $k$ rows removed | $O(hnd)$ | k-anonymity; not minimal |
| [Samarati's algorithm](/samarati-algorithm/) | a vector of least height | $O(ndg \log h)$ | least height within the suppression limit |
| [Incognito](/incognito/) | all k-anonymous vectors, and the minimal ones | $O(2^d g n d)$ | every minimal vector |
| [Mondrian](/mondrian-anonymization/) | a partition of the records into boxes | $O(d n^2 \log n)$ worst | discernibility within $2d + m/k$ of the least |
| [Forest approximation](/k-anonymity-approximation/) | clusters with suppressed cells | $O(n^2 d + n^2 \log n)$ | at most $3k - 3$ times the fewest cells |
| [MDAV](/mdav/) | groups of $k$, the last of $k$ to $2k - 1$ | $O(n^2(d + \log k)/k + nd)$ | none on the loss; group means kept |
| [Anatomy](/anatomy-bucketization/) | l-diverse groups in two tables | $O(n \log m)$ | error within $1 + 1/n$ of the least |
| [k-degree anonymization](/k-degree-anonymization/) | a k-anonymous degree sequence, then edges | $O(n \log n + nk + nr)$ | least cost sequence; the edge step may say UNKNOWN |

: Times and guarantees as the entries state them. The symbols are defined in each entry.

## Choosing a method

Start from the threat. Find the quasi-identifiers first; pseudonyms and removed names do not stop linkage. For a few categorical quasi-identifiers, a full-domain search gives a release that is easy to explain: Samarati's algorithm for a vector of least height, Incognito for all minimal ones, Datafly for speed. For numeric attributes, Mondrian usually keeps more detail, with ranges that differ from row to row. If the sensitive attribute matters, ask for l-diversity or t-closeness on top, or publish it apart with anatomy, and check the groups for skew. Numeric microdata for statistical use suit MDAV or swapping; categorical variables suit PRAM, whose matrix lets users correct their estimates. For tables of counts or sums, audit every suppression pattern with the linear programs, or adjust the cells instead. For graphs, traces and long sparse records, the entries show attacks that need only a few known facts. When the guarantee must hold against any background knowledge, none of these methods gives it; [differential privacy](/differential-privacy-definition/), in Chapter 45.8, is built for that case.

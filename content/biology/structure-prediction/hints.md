1. (a) `((.(...).)).` is a secondary structure: the pairs nest and the hairpin of $(4, 8)$ has three unpaired bases. (b) `(((..)...)).` is not: the hairpin closed by $(3, 6)$ has only two. (c) `(..[..)...].` is not: $1 < 4 < 7 < 11$, so the two pairs cross and form a pseudoknot.

3. The edges are $ab$, $ad$, $bc$, $bd$ and $cd$, and $e$ crosses nothing. The triangle $abd$ needs three kinds, and three are enough: `(.[.(....){).(...]..}..)`, with $a$, $c$ and $e$ written as $(\,)$, $b$ as $[\,]$ and $d$ as $\{\,\}$. The largest nested subset is $\{a, c, e\}$, with three pairs, since among $a, b, c, d$ only $a$ and $c$ do not cross.

4. The RMSD is $\sqrt{(90 \cdot 0.64 + 10 \cdot 100)/100} \approx 3.25$ Å. With $d_0 \approx 3.652$ for $L = 100$, the TM-score at this superposition is $(90/1.048 + 10/8.50)/100 \approx 0.871$. At this superposition 90% of the residues are within each of 1, 2, 4 and 8 Å, so its GDT-TS is 90. Both true scores maximize over superpositions, so the true TM-score is at least 0.871 and the true GDT-TS at least 90; the least-RMSD fit could be a different superposition.

6. Over rotations the maximum of $\operatorname{tr}(RH)$ is $5 + 3 - 1 = 7$, so the residual is $30 - 14 = 16$ and the RMSD is $\sqrt{16/4} = 2$. With reflections allowed it is $5 + 3 + 1 = 9$, the residual is 12 and the RMSD is $\sqrt 3 \approx 1.73$.

8. Four residues are wrong (positions 2, 8, 10 and 14), so $Q_3 = 12/16 = 75\%$. Helix: 5 of 6; strand: 3 of 5; coil: 4 of 5. The most common true state is H, with 6 residues, so predicting H everywhere gives $6/16 = 37.5\%$.

10. By the parity lemma, an H-H contact joins residues whose indices differ by an odd number. In HPHPHPHPH every H has an even index, so no contact is possible. For HPPHHPPHHPPH the H residues are at 0, 4, 8 (even) and 3, 7, 11 (odd), so the bound is 8 contacts; the search finds at most 5, so the optimum energy is $-5$.

11. Four pairs, reached by 7 structures, for example `((((...)))....)` and `((.(...))(...))`.

13. The multiloop closed by $(1, 12)$ has $k = 3$ branches with the closing pair and costs $3 + 3 = 6$, and each hairpin of three bases costs 6, so the energy is 18. The minimum free energy is 0, and three structures reach it: `((...)).....`, `.....((...))` and the open chain. Each of the first two is a stack of $-6$ on a hairpin of 6.

14. The structures are the open chain (0), `((...))` (0), `.(...).` (6), `(....).` and `.(....)` (7 each) and `(.....)` (8). So $Z = 2 + 2^{-6} + 2 \cdot 2^{-7} + 2^{-8} = 521/256$. Then $p(1, 7) = 257/521 \approx 0.493$ and $p(2, 6) = 260/521 \approx 0.499$. No pair is above $1/2$, so the centroid is the open chain, while the minimum energy is shared by the open chain and `((...))`.

20. Let $V(i, j)$ be the most stacked pairs in $[i, j]$ when $(i, j)$ is a pair, and $N(i, j)$ the most with no condition. Then $V(i, j) = \max\big(N(i + 1, j - 1),\ 1 + V(i + 1, j - 1)\big)$, the second case only when $(i + 1, j - 1)$ can pair, and $N(i, j) = \max\big(N(i, j - 1),\ \max_k N(i, k - 1) + V(k, j)\big)$ as in the Nussinov algorithm. A pair's stacking bonus depends only on the pair directly inside it, so the split stays independent.

21. Two pairs that share a base, or that cross, never occur in the same nested structure, so their probabilities sum to at most 1. Hence two pairs above $1/2$ neither share a base nor cross, and the set is nested. The expected number of correct pairs minus wrong pairs of a structure $P$ is $\sum_{(i,j) \in P} \big(p_{ij} - (1 - p_{ij})\big) = \sum_{(i,j) \in P} (2p_{ij} - 1)$, and the centroid takes exactly the pairs with a positive term.

22. Map an opening position to an up step, a closing position to a down step and an unpaired one to a level step. Nesting is what makes the map invertible: each down step closes the latest open up step, as in matching parentheses.

24. Root the tree. For a residue $v$ and rotamer $r$, let $f_v(r)$ be the least energy of the subtree of $v$ with $v$ in $r$: $f_v(r) = E_v(r) + \sum_{c} \min_s \big(E_{vc}(r, s) + f_c(s)\big)$ over the children $c$. Each edge costs $p^2$ work, and there are $n - 1$ edges.

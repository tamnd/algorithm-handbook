1. The true average is $500 / 4 = 125$; the average of the store averages is $(100 + 200)/2 = 150$. The view should store the sum and the count per store, from which any average over a group of stores follows.

2. The join has $(1,1,u)$, $(2,1,u)$ and $(2,2,v)$, so $V = \{1{:}1, 2{:}2\}$. The term $\Delta R \bowtie S$ gives $3{:}{+1}$; the term $R \bowtie \Delta S$ gives $1{:}{-1}$, $2{:}{-1}$ and $3{:}{+1}$; the term $\Delta R \bowtie \Delta S$ gives $3{:}{-1}$. So $\Delta V = \{1{:}{-1}, 2{:}{-1}, 3{:}{+1}\}$ and the new view is $\{2{:}1, 3{:}1\}$, as a recomputation gives. A script checked both.

4. Phase 1 overdeletes $p_{23}$, $p_{24}$, $p_{13}$ and $p_{14}$, since each has a derivation through the edge $2 \to 3$. Phase 2 rederives $p_{24}$ from the edge $2 \to 4$. The insert phase adds $p_{14}$ from $\mathit{edge}(1,2)$ and $p_{24}$. The new model is $p_{12}$, $p_{14}$, $p_{24}$ and $p_{34}$. A script that runs the three phases checked this.

5. The window at $\tau$ holds the elements with times from $\tau - 2$ to $\tau$: $\{a\}$ at 0, $\{a, b, c\}$ at 1 and 2, $\{b, c, d\}$ at 3, $\{d\}$ at 4 and 5, $\{e\}$ from 6 to 8, and nothing at 9. Istream has $a@0$, $b@1$, $c@1$, $d@3$, $e@6$; Dstream has $a@3$, $b@4$, $c@4$, $d@6$, $e@9$. The counts are 1, 3, 3, 3, 1, 1, 1, 1, 1, 0, so Istream of the count emits 1 at 0, 3 at 1, 1 at 4 and 0 at 9. A script checked the windows and both streams.

6. The watermark after each arrival is 0, 0, 2, 2, 6, 6, 6, 6. Only 2 is late: it arrives when the watermark is 6. The window fires after the fifth arrival, 9, and holds 3, 1 and 4. A script checked this.

7. The arrivals emit 0, 1, 0, 1, 1 and 2 results. The complete inputs have two tuples with key 1 on each side and one with key 2 on each side, so the join has $2 \cdot 2 + 1 \cdot 1 = 5$ tuples.

8. Strict contiguity gives only $(a@3, b@4, c@5)$. Skip till next match gives $(a@1, b@2, c@5)$ and $(a@3, b@4, c@5)$. Skip till any match adds $(a@1, b@4, c@5)$ and $(a@3, b@4, c@12)$, four in all; the combinations of $a@1$ with $c@12$ span 11 and fall outside the window. A script that enumerates the combinations checked the counts.

9. $z^{-1}(s) = 0, 3, -1, 4, 0$; $I(s) = 3, 2, 6, 6, 8$; $D(s) = 3, -4, 5, -4, 2$. Both $D(I(s))$ and $I(D(s))$ equal $s$, as Theorem 2.20 of the DBSP entry says.

10. Write each relation as old plus delta and expand the product. Every term that uses at least one delta remains, which gives $2^3 - 1 = 7$. With $j$ changed relations there are $2^j - 1$ terms.

12. The two terms give $\{1{:}{-1}, 2{:}{-1}, 3{:}0\}$, so $a = 3$ would wrongly be missing from the view. Since $R = R' - \Delta R$ and $S = S' - \Delta S$, bilinearity gives $\Delta V = \Delta R \bowtie S' + R' \bowtie \Delta S - \Delta R \bowtie \Delta S$. A script checked both versions on the data.

13. On the chain DRed overdeletes the 25 facts $p_{xy}$ with $x \le 5 < y$, rederives none and adds none, and the new model has 20 facts. With the extra edges, DRed still overdeletes 25 facts, rederives 9 and adds 15, so the new model has 44 facts and loses only $p_{56}$. A script that runs DRed on both graphs checked these counts.

15. An insertion of $R(a, b)$ adds $M_S[b]$ to $Q$ and 1 to $M_R[b]$, and a deletion subtracts both; the rules for $S$ are symmetric. The values of $Q$ are 0, 1, 2, 4, 2, 2, and the final inputs $\{(1, x), (2, x)\}$ and $\{(x, 6), (y, 7)\}$ do give 2. First-order maintenance must count the tuples of the other relation with $B = b$ at each update, which needs an index on $B$ and reads every match. A script checked the values.

16. The element 2 arrives 7 behind the maximum 9, and no element is further behind, so $D = 7$. Then the window fires only when an event time of at least 12 arrives, which does not happen among these eight. A small $D$ gives early results and drops late data; a large one keeps everything but delays every result.

17. (a) 3 calls, one per level; (b) 4, since the four leaves share their ancestors; (c) 7, since every level-one node changes; (d) 5. The bounds are 4, 8, 8 and 6. A script counted the calls.

19. (a) The operator holds back 2 until the barrier of $B$, so the snapshot is 11, and the replay of 2 gives 13, the right sum. (b) The snapshot is 1; the record 10 was sent before the barrier of $B$, so it is in neither the copy nor the replay, and the sum becomes 3. (c) The snapshot is 13, and 2 is replayed again, so the sum becomes 15.

20. Put $n/k$ events of type $E_1$ first, then $n/k$ of type $E_2$, and so on: every choice of one event from each block is a match. Under strict contiguity a match is fixed by the position of its last event.

22. Every path fact has a derivation that uses the edge $n \to 1$, by going round the cycle. After the deletion only the edges remain, so phase 2 finds the $n - 1$ edge facts. The insert phase builds the paths of the chain $1 \to \cdots \to n$ of length at least 2. A script checked $n = 3, 5, 6$.

23. Use the invariant that each table holds exactly the tuples of its input seen so far, so the join grows by $\{t\} \bowtie S_{j-1}$ when $t$ arrives in $R$. For the bound, if the join has dropped a tuple with key $\kappa$, the adversary sends a tuple of the other input with key $\kappa$.

24. Write $I(a)[t] = I(a)[t-1] + a[t]$ and the same for $b$, and expand $I(a)[t] \times I(b)[t] - I(a)[t-1] \times I(b)[t-1]$ by bilinearity. The old relations of the delta rule are $z^{-1}(I(a))$ and $z^{-1}(I(b))$, and the circuit keeps the two integrated inputs.

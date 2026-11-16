1. red ⟨d1: 1⟩ ⟨d3: 1⟩ ⟨d4: 1⟩, blue ⟨d1: 1⟩ ⟨d4: 1⟩, hat ⟨d3: 1⟩ ⟨d4: 1⟩, fish ⟨d1: 2⟩ ⟨d2: 2⟩. red OR blue gives $\{d1, d3, d4\}$, and removing the documents of hat leaves $\{d1\}$. The collection has 7 terms (blue, fish, hat, one, red, sky, two) and 12 postings, so $28 - 12 = 16$ cells are 0.

2. The result is $(5, 14)$, after 8 steps: the merge stops when 20 is compared with 21 and $A$ runs out. The worst-case bound is $m + n - 1 = 10$.

3. The gaps are 5, 1, 7, 127 and 860. Variable-byte needs one byte for each gap below 128 and two for 860, so 6 bytes or 48 bits. Elias gamma needs $5 + 1 + 5 + 13 + 19 = 43$ bits. The fixed width needs $5 \cdot 10 = 50$ bits.

5. queri, merg, compress, document, relev. For documents, step 4 picks the longest matching suffix, ment, and its stem docu has measure 1, so nothing is removed and the shorter suffix ent is not tried.

7. The grams are \$re and ed\$. Their lists are read, red, reduced, rested, retired and bred, red, reduced, rested, retired, so the candidates are red, reduced, rested and retired. The check drops red, because `re*ed` needs at least four letters. The permuterm index rotates `re*ed$` to `ed$re*` and searches the prefix ed\$re, which finds reduced, rested and retired with no false match.

8. Eleven is 1011 in binary, so $I_0$, $I_1$ and $I_3$ exist, with 1000, 2000 and 8000 postings. The merges happen at flushes 2, 4, 6, 8 and 10 and write 2000, 6000, 2000, 14,000 and 2000 postings: 26,000 in total.

10. Divide both bounds by $m$ and compare $2\log_2(1 + r) + 3$ with $r + 1 - 1/m$. At $r = 8$ the left side is 9.34 and the right side is below 9; at $r = 9$ they are 9.64 and at least 9.9. So $r = 9$. Both are worst cases, and on a given input either method can do far fewer steps.

13. Globally, red has idf $\lg(4/3) \approx 0.415$ and fish has idf 1, so d1 gets 2.415, d2 gets 2, and d3 and d4 get 0.415. On node 1 fish is in every document and on node 2 red is, so each of them has local idf 0 there: d1 gets 1, and d2, d3 and d4 get 0. Local scores from different nodes cannot be compared.

17. For $r = 2$, $t \bmod 2^{v+1} = 2^v$, since bit $v$ of $t$ is 1. Among $t = 1, \ldots, 2^j$, the number with $v(t) = i$ is $2^{j-i-1}$ for $i < j$, and one $t$ has $v(t) = j$, so the sum is $j\,2^{j-1} + 2^j = (j/2 + 1)m$. This gives $20b$ for $j = 3$ and $6144b$ for $j = 10$. With $b = 4$ the 8 flushes write 80 postings; the 4 odd flushes only write the buffer, and the remaining 64 are the count of the entry on logarithmic merging with one multiway merge for each carry (96 with pairwise merges).

19. The segments come in the order $x5, y4, z3, x2, z2, y1, z1$. Before $z2$ the leaders are d3 with 9 and d1 with 6, and $r = 0 + 1 + 2 = 3$, so $9 > 6 + 3$ fails by equality. After $z2$, $r = 1 + 1 = 2$ and $9 > 8$, so the method stops after 5 segments and 8 of the 12 postings, and returns d3.

20. Let $f(i)$ be the least number of words for the values from $i$ on; try each layout $s$ whose next $c_s$ values, or all the rest at the end, fit in $w_s$ bits, and take $1 + f(i + c_s)$. The greedy encoder uses 4 words: 4 values of 7 bits, 5 of 5 bits, 4 of 7 bits, and a last word for the final 1. The optimum uses 3 words: 3 of 9 bits (7, 20, 100), 7 of 4 bits (1, 9, 3, 5, 15, 0, 7) and 4 of 7 bits (100, 1, 5, 1).

21. The first chunk has base 0, so it is never a run when the list starts at 5. For $F = 8$ the best cuts are 0, 1, 10, 14, 20: the id 5 alone in Elias-Fano (5 bits), a run from 6 to 14, the ids 60 to 210 in Elias-Fano ($U = 196$, $b = 4$, 31 bits) and a bitmap of 9 bits for 212 to 219. The total is $32 + 45 = 77$ bits, against 116 for one chunk. For $F = 16$ the cuts are 0, 10, 14, 20, with a bitmap of 15 bits for 5 to 14, and the total is 103 bits, against 124.

22. Enumerate the 720 orders with a short program. The input order costs 27, the least cost is 20, and exactly two orders reach it: the old documents 3, 1, 5, 2, 6, 4 and 5, 1, 3, 2, 6, 4 in this new order. The first gap of a list depends on the position itself, not on a difference, so the cost is not symmetric: the reverse of the first optimal order costs 22.

23. Follow the derivation of the entry with $\alpha = 3$: $k = \Gamma(2/3)\,\zeta(3)^{-1/3} \approx 1.3541 \cdot 0.9405 \approx 1.2735$. At $T = 10^6$ this predicts $1.2735 \cdot 100 \approx 127.4$ terms, while the exact sum is about 126.85, so the approximation is about 0.4 percent high.

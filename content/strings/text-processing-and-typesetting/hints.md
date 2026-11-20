1. U+20AC is `E2 82 AC` in UTF-8 (3 bytes) and `20AC` in UTF-16 (2 bytes). U+1D11E is `F0 9D 84 9E` (4 bytes) and the surrogate pair `D834 DD1E` (4 bytes): $\mathtt{1D11E} - \mathtt{10000} = \mathtt{D11E}$, whose top 10 bits are 34 and low 10 bits are 11E in hexadecimal.

2. A, U+FFFD, A, U+FFFD, é, U+FFFD, B: three replacement characters. `E2 82` is a truncated three-byte sequence, `F0 9F 98` a truncated four-byte sequence, and `FF` never occurs in UTF-8.

3. The index of U+1112 U+1173 U+11AF is $(18 \cdot 21 + 18) \cdot 28 + 8 = 11{,}096$, so the syllable is $\mathtt{AC00} + 11{,}096 = \mathtt{D758}$ (흘). U+AE00 has index $512 = (0 \cdot 21 + 18) \cdot 28 + 8$, so it is U+1100 U+1173 U+11AF (글).

4. NFD of the first string is U+0061 U+0323 U+0301, since the mark of class 220 moves before the mark of class 230. NFC is U+1EA1 U+0301: a and U+0323 compose to ạ, and no precomposed character is ạ with an acute. The second string has NFD U+0064 U+0323 U+0307 and NFC U+1E0D U+0307.

6. For 50: $r = 2/3$, real badness 29.6, TeX 30, loose. For 44: $r = -2/3$, the same badness, tight. For 42: $r = -4/3 < -1$, overfull, no finite badness. For 55: $r = 3/2$, real 337.5, TeX $\lfloor (445^3 + 2^{17}) / 2^{18} \rfloor = 336$, very loose.

8. The values at the gaps before l, g, o, r, i, t, h, m are 0, 1, 2, 1, 2, 2, 0, 2. The odd gaps are before g and before r, so the result is al-go-rithm. At the gap before t, the 1 of 1t loses to the 2 of i2t.

9. Forward: cote < coté < côte < côté. The second-level weights follow the string, with an accent weight after its letter, so côte has an accent weight in third place where coté has the smaller 0020 of t. Backwards, the second level is compared from the end, so the last accent counts first: cote < côte < coté < côté.

11. 6 code points, 10 UTF-16 units, 19 UTF-8 bytes and 3 clusters: the acute is Extend (GB9), the two regional indicators pair up (GB12 and GB13), and the skin tone modifier is Extend. NFC composes e and the acute into U+00E9, giving 5 code points, 9 units and 18 bytes; the clusters stay 3.

12. The first strong character is R, so the paragraph level is 1. W7 makes 12 into L because the last strong character before it is d. The space between the letters ב and c lies between R and L, so N2 gives it the embedding direction R. The other space lies between L and L. So the levels are 1, 1, 1, 2, 2, 2, 2, 2, and the display from left to right is "cd 12 בא".

14. The chunks are a (stable), [X | b | Z] (both changed, differently: a conflict), c (stable), d → Y (changed in B only), e (stable) and the added f (changed in A only). So the result is a, conflict(X, b, Z), c, Y, e, f. With B = a, b, c, Y, e there is no conflict, and the result is a, X, c, Y, e, f.

16. Try every vector of column widths drawn from the configurations. Width 10: the best is 4, with columns 5 and 4. Width 11: 3, with columns 5 and 6. Width 16: 2, with columns 9 and 7. The smallest width is $3 + 4 = 7$, the widest of the narrowest configurations in each column.

17. Filling gives pages of lines 1–3, 4–6 and 7. Lines 4 and 7 are widows, so the cost is 100. The optimum, found by dynamic programming over the 8 break positions, puts lines 1–2, 3–4 and 5–7 on the pages, at cost $1 + 1 + 0 = 2$. It is the only breaking of cost 2.

21. The first byte gives the length and the top bits of the value. Compare two code points by their encodings. If the lengths differ, the shorter one has the smaller value, and its lead byte is smaller, because the lead byte ranges 00–7F, C2–DF, E0–EF and F0–F4 increase with the length. If the lengths are equal, the bytes hold the bits of the value from high to low, so byte order is numeric order. Since UTF-8 is a prefix code, two strings with the same first code points have the same first bytes, so the first differing byte lies in the first pair of differing code points, which start at the same offset. A proper prefix stays a proper prefix.

22. Code points below D800 keep their units. E000–FFFF go to D800–F7FF, still in order and below all the others. A supplementary code point starts with a high surrogate, which goes to F800–FBFF, so it sorts after every BMP character. Among supplementary code points, (high, low) is $(v \gg 10, v \mathbin{\&} \mathtt{3FF})$, which orders as $v$ does. U+FF61 becomes F761 and U+10000 becomes F800 FC00.

23. The equal first and last lines can be matched, since some LCS matches them. After that, every common line is unique in both files, so a common subsequence is a set of pairs whose positions increase in both files. The longest increasing subsequence step finds the largest such set, so it is already an LCS, and the recursion on the gaps can only add pairs consistent with it.

24. Add the hypothesis to the quadrangle inequality $w(i, j) + w(i', j') \le w(i, j') + w(i', j)$ and cancel $w(i, j) + w(i', j)$. So once a later candidate beats an earlier one at some target, it beats it at every later target. Each candidate is then best for an interval of targets, and the intervals appear in the order of the candidates.

25. Each swap of insertion sort removes one inversion, a pair whose classes are in the wrong order, and stable insertion never swaps equal classes. So the number of swaps is the number of pairs with the larger class first, at most $k(k-1)/2$, with equality exactly when all pairs are inverted, that is, when the classes strictly decrease. That needs $k$ distinct classes, so $k = 55$ and $55 \cdot 54 / 2 = 1485$ swaps.

1. ◦ Write the euro sign U+20AC and the musical symbol G clef U+1D11E in [UTF-8](/utf-8/) and in big-endian [UTF-16](/utf-16/). How many bytes does each take in each encoding?

2. ◦ A decoder replaces each maximal subpart of an ill-formed UTF-8 sequence with one U+FFFD. What does it output for the bytes `41 E2 82 41 F0 9F 98 C3 A9 FF 42`? How many replacement characters are there?

3. ◦ Use the arithmetic of [Hangul syllable composition](/hangul-syllable-composition/) to compose the jamo U+1112, U+1173, U+11AF into one syllable, and to decompose the syllable U+AE00. Give the syllable index in both cases.

4. ◦ Give NFD and NFC of the two strings U+0061 U+0301 U+0323 and U+1E0B U+0323. The combining class of U+0323 is 220, and that of U+0301 and U+0307 is 230. Explain why U+0301 is not composed in the first string.

5. ◦ Under default caseless matching with full [case folding](/unicode-case-folding/), which of these pairs match: "Straße" and "STRASSE"; U+01C5 ǅ and U+01C4 Ǆ; the Kelvin sign U+212A and "k"; U+0130 İ and "i"?

6. ◦ A line has natural width 46, total stretch 6 and total shrink 3. For the line lengths 50, 44, 42 and 55, give the adjustment ratio, the real [badness](/typesetting-badness/), the integer badness of TeX and the fitness class.

7. ◦ Break the words "aaa bb cc ddddd" into lines of length 6, with each letter 1 wide and rigid spaces of width 1. Give the [greedy](/greedy-line-breaking/) breaking and a breaking that minimizes the sum of the cubes of the empty space at the ends of the lines, with the last line free. What does each cost?

8. ◦ Hyphenate "algorithm" by [Liang's method](/liang-hyphenation/) with the patterns l1g, g2o, go1r, r2i, 1t, i2t and h2m, and the limits of TeX: at least 2 letters before a hyphen and 3 after it. Give the value at each gap.

9. ◦ The words cote, coté, côte and côté are equal at the first level of the [collation algorithm](/unicode-collation-algorithm/) and differ only at the second. Sort them with the default forward second level, and then with the backwards second level that CLDR uses for some French tailorings.

10. • Encode "café" in [Punycode](/punycode/) by hand. Show that the first delta is $(\mathtt{E9} - 128) \cdot 4 + 3$, and write it with the initial bias 72.

11. • The string U+0065 U+0301 U+1F1EB U+1F1F7 U+1F44D U+1F3FD is e with an acute accent, the flag of France and a thumbs up with a skin tone modifier. Give its length in code points, in UTF-16 units, in UTF-8 bytes and in [extended grapheme clusters](/extended-grapheme-cluster/). Which numbers change under NFC?

12. • Run the [bidirectional algorithm](/unicode-bidirectional-algorithm/) on the paragraph "אב cd 12", stored in this order: two Hebrew letters, a space, "cd", a space and "12". Give the paragraph level, the resolved level of each of the 8 characters, and the order in which they are shown from left to right.

13. • Let A be the lines a, b, c, a, b, c, U and B the lines U, a, b, c. Which lines does [patience diff](/patience-diff/) match, and how many deletions and insertions does its script have? Compare with a shortest edit script.

14. • Merge with [diff3](/diff3/) the ancestor O = a, b, c, d, e and the versions A = a, X, c, d, e, f and B = a, Z, c, Y, e. Give the result and any conflict, with the three versions of the conflicting chunk. What is the result if B is a, b, c, Y, e instead?

15. • Take the source S = abcdefg and the target T = efgabcxcd. Give the cover that [Tichy's method](/tichy-block-moves/) builds and its number of moves. How many operations does an edit script made only of deletions and insertions of single symbols need?

16. • A table has two rows and two columns with the configurations (width, height): cell (1, 1) has (9, 1), (5, 2), (3, 3); cell (1, 2) has (7, 1), (4, 2); cell (2, 1) has (4, 1), (2, 2); cell (2, 2) has (6, 1), (3, 2), (2, 3). In the [table layout problem](/table-layout-problem/), what is the least table height for the widths 10, 11 and 16? What is the smallest width that admits any layout?

17. • Seven lines of height 1 form two paragraphs, of lines 1 to 4 and 5 to 7, and a page holds 3 lines. Each page but the last costs $(3 - u)^2$ for $u$ lines on it. A page that starts with the last line of a paragraph (a widow) or ends with its first line (an orphan) costs 50 more. Find the cost of filling each page, and an optimal [page breaking](/page-breaking-problem/).

18. • Solve the [least weight subsequence](/least-weight-subsequence/) problem with $n = 8$ and $w(i, j) = |j - i - 3|$. Give $F(0), \ldots, F(8)$ and every optimal subsequence. Is this weight concave in the sense of Hirschberg and Larmore?

19. • In the ragged-right encoding of the [box, glue and penalty model](/box-glue-penalty-model/), each space is a glue of width 0 and stretch $S$, a penalty 0, and a glue of width $w$ and stretch $-S$. A line holds words of widths 3, 4 and 2 and ends at the penalty after the last word, with $w = 1$, $S = 6$ and line length 14. Find its natural width, its total stretch, its adjustment ratio, its badness and the width of its two inner spaces.

20. • Prove that two weights of line breaking satisfy the quadrangle inequality $w(i, j) + w(i', j') \le w(i, j') + w(i', j)$ for $i \le i' < j \le j'$: the weight that is 1 when the line fits and $+\infty$ when it does not, for positive word widths; and $w(i, j) = f(T_j - T_i)$ for a convex $f$ and nondecreasing $T$.

21. ★ Prove that the byte-by-byte lexicographic order of UTF-8 strings is the lexicographic order of their sequences of scalar values.

22. ★ Comparing UTF-16 strings unit by unit puts U+FF61 after U+10000. Show that mapping each unit $x$ to $x - \mathtt{800}$ when $x \ge \mathtt{E000}$, to $x + \mathtt{2000}$ when $\mathtt{D800} \le x < \mathtt{E000}$, and to $x$ otherwise makes unit order agree with code point order, for well-formed strings.

23. ★ Prove that patience diff returns a longest common subsequence when no line occurs more than once in either file.

24. ★ Let $w$ satisfy the quadrangle inequality, let $i < i' < j \le j'$, and suppose $F(i') + w(i', j) \le F(i) + w(i, j)$. Prove that $F(i') + w(i', j') \le F(i) + w(i, j')$. Explain why this lets the [Hirschberg-Larmore algorithm](/hirschberg-larmore-algorithm/) keep its candidates as intervals of targets in a deque.

25. ★ Canonical ordering in the [normalization algorithm](/unicode-normalization-algorithm/) sorts each run of non-starters stably by combining class, by insertion. Show that a run of $k$ non-starters needs at most $k(k-1)/2$ swaps, and that the bound is reached exactly when the classes strictly decrease. In Unicode 16.0.0, which has 55 distinct nonzero combining classes, what is the longest run that reaches the bound, and how many swaps does it need?

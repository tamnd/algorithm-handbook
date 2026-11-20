## What to remember

- The codespace has $17 \cdot 2^{16} = 1{,}114{,}112$ code points; without the 2,048 surrogates, 1,112,064 **scalar values** remain for the encodings to write. [UTF-8](/utf-8/) is a prefix code of one to four bytes whose byte order is code point order. [UTF-16](/utf-16/) uses one unit or a surrogate pair, and its unit order is not code point order.
- Two strings are **canonically equivalent** exactly when $\mathrm{NFD}(s) = \mathrm{NFD}(t)$, and also exactly when $\mathrm{NFC}(s) = \mathrm{NFC}(t)$. Each normal form is idempotent, but the normal forms are not closed under concatenation. The [normalization algorithm](/unicode-normalization-algorithm/) takes $\Theta(n^2)$ time in the worst case, because it sorts runs of marks by insertion, and $\Theta(n)$ time on Stream-Safe text.
- The Unicode algorithms are **specifications**: an implementation is correct when it agrees with the standard and its conformance tests. Their data change between versions, so a confusable skeleton, for example, is not stable.
- A **character** in the reader's sense is an [extended grapheme cluster](/extended-grapheme-cluster/), not a code point. A family emoji is 5 code points, 8 UTF-16 units and 18 UTF-8 bytes, but it is 1 cluster.
- The [badness](/typesetting-badness/) of a line is about $100|r|^3$ for the adjustment ratio $r$, capped at 10000, and it is infinite when $r < -1$. [Greedy breaking](/greedy-line-breaking/) uses the fewest lines when spaces cannot stretch, but can leave a very loose line. Choosing all breaks at once is a [least weight subsequence](/least-weight-subsequence/) problem: $O(n^2)$ in general, $O(n \log n)$ or $O(n)$ under the quadrangle inequality, which the capped badness of TeX fails in general.
- [Liang's patterns](/liang-hyphenation/) allow a hyphen where the largest digit at a gap is odd. His TeX82 set found about 89 percent of the hyphens of his word list with almost no errors, a measurement.
- **Pages.** Text alone is a least weight subsequence problem, $O(nk)$. With figures that keep their order, [optimal pagination](/optimal-pagination/) takes $O(n^2 m^2)$; with figures that may change order, the problem is [strongly NP-complete](/pagination-np-completeness/). The [best-fit page builder](/best-fit-page-breaking/) of TeX is a heuristic.
- **Diff.** [Myers' algorithm](/myers-diff/) finds a shortest edit script in $O((n + m) D)$ time. [Heckel](/heckel-diff/), [patience](/patience-diff/) and [histogram](/histogram-diff/) diff anchor on rare lines and do not minimize the script in general. [Tichy's](/tichy-block-moves/) greedy cover gives the fewest moves.
- **Merge.** [diff3](/diff3/) has conflicts by design: if both sides change the same region in different ways, it reports a conflict. Its result depends on the two-way diffs it uses.

## The main methods side by side

| Method | Time | What the result is |
|---|---|---|
| [UTF-8](/utf-8/) decoding | $\Theta(n)$ | exact; one U+FFFD per maximal subpart is recommended |
| [Normalization](/unicode-normalization-algorithm/) | $\Theta(n^2)$ worst, $\Theta(n)$ Stream-Safe | the form defined by the standard |
| [Greedy line breaking](/greedy-line-breaking/) | $O(m + KB)$ | fewest lines with rigid or shrink-only spaces |
| [Knuth-Plass](/knuth-plass-line-breaking/) | $O(mA)$ | least total demerits |
| [Hirschberg-Larmore](/hirschberg-larmore-algorithm/) | $O(n \log n)$ | optimal for concave weights |
| [Wilber](/wilber-algorithm/) | $O(n)$ | optimal for concave weights |
| [Liang hyphenation](/liang-hyphenation/) | $O(k l^2)$ | the hyphens the patterns allow |
| [Best-fit page breaking](/best-fit-page-breaking/) | $O(mk)$ | best break for each page alone |
| [Optimal pagination](/optimal-pagination/) | $O(n^2 m^2)$ | optimal when figures keep their order |
| [Myers' diff](/myers-diff/) | $O((n + m)D)$ | a shortest edit script |
| [Patience diff](/patience-diff/) | $O(n^2 \log n)$ expected | an LCS when no line repeats, else not minimal |
| [Histogram diff](/histogram-diff/) | $O(c n^3)$ expected | not minimal |
| [Tichy's block moves](/tichy-block-moves/) | $O(mn)$ | fewest copies and adds |
| [diff3](/diff3/) | $O(n^2)$ with dynamic programming diffs | a merge with conflicts |
| [Chawathe](/chawathe-tree-diff/) | $O(n + nd)$ | a minimum conforming script for its matching |

: The main methods of the chapter. Variables as in the entries ($D$ is the edit distance, $c = 64$ in JGit). Segmentation, line breaking and bidi are $\Theta(n)$ in code points.

## Choosing a method

- **Unicode.** Use a library that follows the Unicode version you need and passes its conformance tests. Normalize before comparing, fold case for caseless matching, and collate with a locale tailoring when people read the order.
- **Lines.** Use greedy breaking in an editor, where lines must not move as text is added, and total fit for justified print. The fast least weight subsequence methods need a line cost that is a convex function of the line width.
- **Pages.** Best fit ships each page at once; optimal pagination needs the whole document but keeps figures nearer their references.
- **Diff and merge.** Use Myers' algorithm when the shortest script matters. Patience or histogram diff often reads better, but it is a heuristic. Expect conflicts from any three-way merge, and resolve them by hand.

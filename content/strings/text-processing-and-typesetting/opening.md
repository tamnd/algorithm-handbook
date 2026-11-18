The earlier chapters of this volume treat a string as a sequence of abstract symbols. Real text is messier. A single letter on screen can be several code points, the same word can be stored in two byte sequences that must compare equal, and a paragraph must be cut into lines and pages that look even. A text editor, a browser, a typesetting system and a version-control tool all solve these problems every time they show or store text, and the algorithms behind them are a mix of careful tables, dynamic programming and string matching.

Two problems stand out. Breaking a paragraph into lines so that the spacing is even everywhere is a shortest path problem over the possible breaks, and its fast solutions use the structure of the cost function. Comparing two versions of a file and merging changes from two sides are string problems on lines, solved by longest common subsequences and by heuristics that match unique lines first.

## What the chapter will cover

The entries of this chapter are being written. They will cover:

1. **Unicode text.** Code points and the UTF-8 and UTF-16 encodings with fast validation, Punycode, the normalization forms and canonical equivalence, case folding, grapheme clusters and text segmentation, collation, the bidirectional algorithm and confusable detection.
2. **Line breaking and hyphenation.** Greedy line breaking, badness and the box, glue and penalty model, the least weight subsequence problem with the faster algorithms of Wilber and of Hirschberg and Larmore, the Unicode line breaking rules, and Liang's hyphenation with its pattern generation and packed trie.
3. **Pages and layout.** Page breaking by best fit and by dynamic programming, the NP-completeness of pagination with figures, widows and orphans, table layout, the layout of mathematics in TeX, kerning and text shaping.
4. **Diff and merge.** Heckel's algorithm, patience diff and histogram diff, Tichy's block moves, diff3 and three-way merge, merge of structured files, and change detection in trees by Chawathe's method.

## What to read meanwhile

[Knuth-Plass line breaking](/knuth-plass-line-breaking/) is written in Volume 2, as a shortest path over the break points. [Optimal text wrapping](/optimal-text-wrapping/), the [Monge property](/monge-property/) and the [SMAWK algorithm](/smawk-algorithm/), all in Volume 2, explain why line breaking with a convex cost can run faster than the obvious quadratic loop. The [trie](/trie/) of Volume 3 is the structure behind hyphenation patterns.

For diff, read the [longest common subsequence](/longest-common-subsequence/), [Hunt-Szymanski](/hunt-szymanski/) and [Myers' diff algorithm](/myers-diff/) in Volume 6, and [edit distance](/edit-distance/) in Chapter 8.4. [Tree edit distance](/tree-edit-distance/) in Volume 7 is the exact, slower way to compare two trees.

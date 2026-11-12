The Handbook of Algorithms, edition 0.23.0: the written areas of [algorithm.tamnd.com](https://algorithm.tamnd.com)
as books, one volume per area, in PDF (7 × 10 in, with bookmarks and links), EPUB 3 and LaTeX source. Built from
[`tamnd/algorithm` v0.23.0](https://github.com/tamnd/algorithm/releases/tag/v0.23.0)
(`8f6ee18ef6b3028e694c1021a0503c00f1cb54d7`); the edition number follows the release of the site.

| | Volume | Entries | Pages |
|---|---|---:|---:|
| 0 | Guide and Index | the whole set | 1,150 |
| 1 | Foundations | 204 | 1,000 |
| 2 | Techniques | 208 | 1,123 |
| 3 | Data structures | 427 | 3,138 |
| 4 | Sorting | 156 | 910 |
| 5 | Searching | 115 | 646 |
| 6 | Sequences | 120 | 594 |
| 7 | Graphs | 685 | 3,691 |
| 8 | Strings | 216 | 1,256 |
| 9 | Automata and parsing | 270 | 1,604 |
| 10 | Number theory | 238 | 1,438 |
| 11 | Algebra | 328 | 2,122 |
| 12 | Numerical | 465 | 3,022 |
| 13 | Geometry | 280 | 1,794 |
| 14 | Combinatorics | 174 | 877 |
| 15 | Optimization | 301 | 1,762 |
| 16 | Logic and constraints | 325 | 2,106 |
| 17 | Randomized | 141 | 840 |
| 18 | Approximation | 213 | 1,311 |
| 19 | Online and streaming | 195 | 1,133 |
| 20 | Parallel | 128 | 897 |
| 21 | Distributed | 281 | 2,060 |
| 22 | Concurrency | 155 | 2,240 |
| 23 | Cryptography | 390 | 3,136 |
| 24 | Compression and coding | 220 | 1,741 |
| | **All** | **6,235** | **41,591** |

- **New in this edition: Volume 24, Compression and coding**, in five chapters: entropy coding (entropy and the
  source coding theorem, prefix codes and the Kraft inequality, Huffman, Elias, Golomb and Rice codes, arithmetic
  and range coding, asymmetric numeral systems, context modeling), dictionary compression (LZ77, LZ78, LZW,
  match finding and optimal parsing, DEFLATE, LZ4, LZMA, Brotli and Zstandard, grammar-based compression),
  transforms for compression (run-length and delta coding, the Burrows-Wheeler and move-to-front transforms,
  quantization, the discrete cosine transform, JPEG and JPEG 2000), error correcting codes (linear codes, the
  channels and their capacity, the Hamming, Singleton, Gilbert-Varshamov and other bounds, Reed-Solomon and BCH
  codes with their decoders, convolutional, turbo, LDPC, fountain and polar codes) and checksums (parity, the
  Internet checksum, Fletcher and Adler-32, CRCs from the polynomial to table-driven and folded forms, check
  digits). Each method names its source model or its channel. The volume has the same apparatus as the others:
  a volume introduction, chapter openings, summaries, exercises with hints, notes, concept maps and indexes.
- **Volume 0, Guide and Index**, covers the whole set of 6,235 entries and has a new learning path,
  *Compression and coding*.
- **Volumes 1 to 23** have the same entries under the same numbers as in 0.22.0; their cross-references to entries
  of Volume 24 (Huffman coding, the Burrows-Wheeler transform, Reed-Solomon codes and others) now give entry
  numbers.
- Volumes 25 to 31 are forthcoming; Volume 0 lists their chapters.

**Files.** For each volume `NN-area`: `handbook-of-algorithms-0.23.0-NN-area.pdf`, `.epub`, and `-tex.tar.gz`
(`main.tex`, `body.tex`, `handbook.sty` and the figures; compile `main.tex` with XeLaTeX or tectonic).
`…-all-pdf.zip` and `…-all-epub.zip` hold every volume; `SHA256SUMS` lists the checksums.

Entry and statement numbers (such as 4.1.12 and Lemma 4.1.12.2) belong to this edition. The entries are the text of
the site; the learner pages were drafted by AI agents and checked as described in `content/PROVENANCE.md`. Text
CC BY-SA 4.0, code MIT. Report errors in an entry at https://github.com/tamnd/algorithm/issues and errors in the
books at https://github.com/tamnd/algorithm-handbook/issues.

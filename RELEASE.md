The Handbook of Algorithms, edition 0.42.0: the written areas of [algorithm.tamnd.com](https://algorithm.tamnd.com)
as books, one volume per area, in PDF (7 × 10 in, with bookmarks and links), EPUB 3 and LaTeX source. Built from
[`tamnd/algorithm` v0.42.0](https://github.com/tamnd/algorithm/releases/tag/v0.42.0)
(`56d85ec9f045746050a9f644811529bdb768d909`); the edition number follows the release of the site.

| | Volume | Entries | Pages |
|---|---|---:|---:|
| 0 | Guide and Index | the whole set | 2,214 |
| 1 | Foundations | 204 | 1,000 |
| 2 | Techniques | 208 | 1,123 |
| 3 | Data structures | 427 | 3,140 |
| 4 | Sorting | 156 | 910 |
| 5 | Searching | 115 | 646 |
| 6 | Sequences | 120 | 596 |
| 7 | Graphs | 685 | 3,693 |
| 8 | Strings | 259 | 1,632 |
| 9 | Automata and parsing | 270 | 1,604 |
| 10 | Number theory | 238 | 1,438 |
| 11 | Algebra | 328 | 2,122 |
| 12 | Numerical | 463 | 3,004 |
| 13 | Geometry | 280 | 1,796 |
| 14 | Combinatorics | 174 | 877 |
| 15 | Optimization | 301 | 1,766 |
| 16 | Logic and constraints | 325 | 2,106 |
| 17 | Randomized | 141 | 840 |
| 18 | Approximation | 213 | 1,309 |
| 19 | Online and streaming | 195 | 1,135 |
| 20 | Parallel | 128 | 897 |
| 21 | Distributed | 281 | 2,060 |
| 22 | Concurrency | 155 | 2,240 |
| 23 | Cryptography | 389 | 3,128 |
| 24 | Compression and coding | 220 | 1,741 |
| 25 | Machine learning | 419 | 2,982 |
| 26 | Systems | 346 | 2,550 |
| 27 | Biology | 468 | 3,346 |
| 28 | Graphics and signals | 594 | 4,817 |
| 29 | Games and search | 205 | 1,592 |
| 30 | Quantum | 152 | 1,582 |
| 31 | CAD | 374 | 3,027 |
| 32 | Electronic design automation | 358 | 2,690 |
| 33 | Statistics and inference | 276 | 2,168 |
| 34 | Compilers and program analysis | 272 | 2,793 |
| 35 | Information retrieval and AI reasoning | 276 | 1,716 |
| 36 | Control | 279 | 2,334 |
| 37 | Robotics | 264 | 2,135 |
| 38 | Computer vision | 277 | 2,593 |
| 39 | Complexity | 284 | 1,225 |
| 40 | Databases | 296 | 2,420 |
| 41 | Natural language and speech | 22 | 215 |
| 42 | Algorithmic game theory | 6 | 102 |
| 43 | Scientific computing | 3 | 91 |
| 45 | Security and privacy | 2 | 75 |
| 46 | Imaging and inverse problems | 1 | 61 |
| | **All** | **11,449** | **83,531** |

- **Volume 28, Graphics and signals**, now has all twelve of its chapters written, 594 entries in all. Three
  new chapters: *Real-time rendering* (60 entries: shading models, stylized shading and tone mapping, environment
  lighting, procedural and compressed textures, surface detail, level of detail, shadows, deferred shading,
  screen-space effects and transparency), *Character animation* (36 entries: skeletons, linear blend and dual quaternion
  skinning and their corrections, automatic rigging and skinning weights, blendshapes and facial rigs, blending
  and warping captured motion, motion graphs and motion matching, inverse kinematics, spacetime constraints and
  retargeting, physics-based control and crowds) and
  *Deformable body simulation* (31 entries: mass-spring systems, continuum elasticity and finite elements, cloth,
  shells and rods, position based dynamics, implicit steps as optimization, collisions and contact).
- **Volume 40, Databases**, now has all nine of its chapters written, 296 entries in all (126 in 0.40.0). Two new
  chapters: *Distributed and replicated databases* (20 entries: fragmentation and allocation, distributed query
  processing and semijoins, replication, distributed transactions, coordination avoidance) and *Data integration
  and cleaning* (30 entries: schema matching and mappings, answering queries using views, data exchange, entity
  resolution, constraints and repairs, dependency discovery, truth discovery). Six chapters grew, and their pages
  are rewritten: *Storage and indexing* (31 entries), *Query processing* (40), *Query optimization* (35),
  *Transactions and concurrency control* (41), *Logging and recovery* (21) and *Stream and incremental
  processing* (25).
- **Volume 8, Strings**, has a new chapter, *Text processing and typesetting* (43 entries: Unicode code points and
  encodings, normalization and case folding, segmentation and collation, text shaping, line breaking with
  boxes, glue and penalties, hyphenation, page and table layout, diff and merge), and has 259 entries.
- **New in this edition: Volume 41, Natural language and speech**, with its introduction, its first chapter,
  *Tokenization and text normalization* (22 entries: language identification, tokenization, sentence boundaries
  and truecasing, word segmentation, morphology, byte pair encoding, WordPiece and unigram subword vocabularies),
  and the openings of the other eight chapters.
- **Volume 0, Guide and Index**, covers the whole set of 11,449 entries.
- The other volumes have the same entries under the same numbers as in 0.40.0. The entries have the corrections
  that the site made up to its release v0.42.0, among them those found while writing edition 0.40.0.
- Backslashes in the text of an entry outside mathematics, such as the string "\uD800" or the category (S\NP)/NP,
  are now printed as written; before, the builder passed them to TeX. Hangul and emoji in the text now have fonts.
- Volume 44 (Communications) is not built: the site has only short pages for it so far. Volume 0 lists its
  chapters.

**Files.** For each volume `NN-area`: `handbook-of-algorithms-0.42.0-NN-area.pdf`, `.epub`, and `-tex.tar.gz`
(`main.tex`, `body.tex`, `handbook.sty` and the figures; compile `main.tex` with XeLaTeX or tectonic).
`…-all-pdf.zip` and `…-all-epub.zip` hold every volume; `SHA256SUMS` lists the checksums.

Entry and statement numbers (such as 4.1.12 and Lemma 4.1.12.2) belong to this edition. The entries are the text of
the site; the learner pages were drafted by agents and checked as described in `content/PROVENANCE.md`. Text
CC BY-SA 4.0, code MIT. Report errors in an entry at https://github.com/tamnd/algorithm/issues and errors in the
books at https://github.com/tamnd/algorithm-handbook/issues.

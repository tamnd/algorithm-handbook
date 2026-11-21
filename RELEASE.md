The Handbook of Algorithms, edition 0.48.0: the written areas of [algorithm.tamnd.com](https://algorithm.tamnd.com)
as books, one volume per area, in PDF (7 × 10 in, with bookmarks and links), EPUB 3 and LaTeX source. Built from
[`tamnd/algorithm` v0.48.0](https://github.com/tamnd/algorithm/releases/tag/v0.48.0)
(`86848c7b1b17aeb7dc0bec542553c9817a7dd39b`); the edition number follows the release of the site.

| | Volume | Entries | Pages |
|---|---|---:|---:|
| 0 | Guide and Index | the whole set | 2,511 |
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
| 12 | Numerical | 463 | 3,008 |
| 13 | Geometry | 280 | 1,796 |
| 14 | Combinatorics | 174 | 877 |
| 15 | Optimization | 301 | 1,766 |
| 16 | Logic and constraints | 325 | 2,106 |
| 17 | Randomized | 141 | 842 |
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
| 41 | Natural language and speech | 299 | 2,157 |
| 42 | Algorithmic game theory | 292 | 1,845 |
| 43 | Scientific computing | 292 | 2,441 |
| 44 | Communications | 259 | 2,006 |
| 45 | Security and privacy | 2 | 75 |
| 46 | Imaging and inverse problems | 251 | 2,327 |
| | **All** | **12,810** | **94,141** |

- **Three volumes are new or complete.** By its release v0.48.0 the site has written all chapters of three more
  areas, and each volume now has its introduction, a first course, and for every chapter an opening, groups, a
  summary, exercises with hints and notes.
  - **Volume 42, Algorithmic game theory**, has all nine chapters, 292 entries (6 in 0.45.0), and 230 exercises:
    *Games and solution concepts* (29 entries), *Computing equilibria* (32), *Price of anarchy and selfish
    routing* (27), *Mechanism design* (30), *Auctions* (33), *Social choice and voting* (41), *Fair division* (32),
    *Matching markets and market equilibria* (36) and *Cooperative games and cost sharing* (32).
  - **Volume 44, Communications**, is built for the first time, with nine chapters, 259 entries and 226
    exercises: *Modulation and detection* (39), *Synchronization* (22), *Fading channels* (29), *Channel
    estimation and equalization* (28), *OFDM and multicarrier* (25), *MIMO communications* (37), *Multiple access
    and spread spectrum* (31), *Link adaptation and resource allocation* (26) and *Radar waveforms and detection*
    (22).
  - **Volume 46, Imaging and inverse problems**, has all eight chapters, 251 entries (1 in 0.45.0), and 195
    exercises: *Regularization of inverse problems* (35), *Variational and learned reconstruction* (30),
    *Tomographic reconstruction* (42), *MRI reconstruction* (29), *Ultrasound and radar imaging* (31), *Seismic
    imaging* (25), *Phase retrieval and coherent imaging* (26) and *Deconvolution and astronomical imaging* (33).
- **Volume 0, Guide and Index**, covers the whole set and has three new learning paths: *Algorithmic game
  theory*, *Communications and radar*, and *Imaging and inverse problems*.
- **Volume 43, Scientific computing**, has the corrections of
  [tamnd/algorithm#880](https://github.com/tamnd/algorithm/pull/880), found while writing edition 0.45.0, which
  are in the site's release v0.48.0.
- Only the volumes whose text changed were built again: 0, 1, 2, 7, 12, 15, 17, 19, 23 to 29, 33, 35, 38, 39,
  41, 42, 43, 44 and 46. Most of them refer to entries of Volumes 42, 44 and 46, whose numbers are new (the
  minimax theorem is now 42.1.10). The other volumes have the same text as in 0.45.0, and their files are those
  of 0.45.0 under the new names, so their covers, title pages and copyright pages say the edition in which they
  were last built: 0.45.0 for Volumes 10, 31 and 32, and 0.43.0 for the others.
- **Corrections**: thirteen errors found in thirteen entries of Volumes 42, 44 and 46 while writing (the price of
  stability of linear congestion games, a Talmud rule example, the hardness of bribery, a table of
  inter-carrier interference, the monotone errors of CG-SENSE, among others) were corrected on the site after
  v0.48.0 ([tamnd/algorithm#883](https://github.com/tamnd/algorithm/pull/883)); this edition prints the entries
  of v0.48.0.
- Volume 45, Security and privacy, still has two of nine chapters written, with openings for the others.

**Files.** For each volume `NN-area`: `handbook-of-algorithms-0.48.0-NN-area.pdf`, `.epub`, and `-tex.tar.gz`
(`main.tex`, `body.tex`, `handbook.sty` and the figures; compile `main.tex` with XeLaTeX or tectonic).
`…-all-pdf.zip` and `…-all-epub.zip` hold every volume; `SHA256SUMS` lists the checksums.

Entry and statement numbers (such as 4.1.12 and Lemma 4.1.12.2) belong to this edition. The entries are the text of
the site; the learner pages were drafted by agents and checked as described in `content/PROVENANCE.md`. Text
CC BY-SA 4.0, code MIT. Report errors in an entry at https://github.com/tamnd/algorithm/issues and errors in the
books at https://github.com/tamnd/algorithm-handbook/issues.

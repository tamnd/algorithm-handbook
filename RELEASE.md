The Handbook of Algorithms, edition 0.22.0: the written areas of [algorithm.tamnd.com](https://algorithm.tamnd.com)
as books, one volume per area, in PDF (7 × 10 in, with bookmarks and links), EPUB 3 and LaTeX source. Built from
[`tamnd/algorithm` v0.22.0](https://github.com/tamnd/algorithm/releases/tag/v0.22.0)
(`d16615c67f8a2e5446a9e852920ec1fffb2055dc`); the edition number follows the release of the site.

| | Volume | Entries | Pages |
|---|---|---:|---:|
| 0 | Guide and Index | the whole set | 1,102 |
| 1 | Foundations | 204 | 1,000 |
| 2 | Techniques | 208 | 1,121 |
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
| 17 | Randomized | 141 | 839 |
| 18 | Approximation | 213 | 1,311 |
| 19 | Online and streaming | 195 | 1,133 |
| 20 | Parallel | 128 | 897 |
| 21 | Distributed | 281 | 2,060 |
| 22 | Concurrency | 155 | 2,240 |
| 23 | Cryptography | 390 | 3,136 |
| | **All** | **6,015** | **39,799** |

- **New in this edition: Volume 23, Cryptography**, the largest volume of the set, in seven chapters: symmetric
  ciphers (from the classical ciphers and perfect secrecy to DES, AES, the modes of operation, stream ciphers,
  authenticated encryption and cryptanalysis), hash functions (Merkle–Damgård and the sponge, SHA-2 and SHA-3,
  HMAC, password hashing, the generic attacks), public-key encryption (RSA, ElGamal, the notions IND-CPA and
  IND-CCA, hybrid encryption and KEMs, pairings and homomorphic encryption), signatures, key exchange, the
  post-quantum schemes (lattices, codes, hashes, isogenies, multivariate systems, the NIST standards) and
  protocols (commitments, zero knowledge, secret sharing, oblivious transfer, multiparty computation, TLS and
  Signal). Each security claim names its adversary, its assumption and its model.
- **And Volume 22, Concurrency** (first built for 0.21.0, which was not released), in four chapters: mutual
  exclusion (Peterson, the filter and bakery locks, the lower bounds, spin, ticket, queue and cohort locks,
  semaphores, monitors, deadlock), lock-free structures (linearizability and the progress conditions, consensus
  numbers and the universal construction, Treiber's stack, the Michael-Scott queue, Harris's list, work-stealing
  deques, skip lists and counting networks), memory reclamation (hazard pointers, epochs, RCU, eras and
  intervals, reference counts) and transactional memory (opacity, TL2, NOrec, TinySTM, contention managers,
  hardware transactions and lock elision). Both new volumes have the same apparatus as the others: a volume
  introduction, chapter openings, summaries, exercises with hints, notes, concept maps and indexes.
- **More numbered statements, in every volume.** The definition of the problem or structure of an entry
  (*Definition 5.1.4.1* states the problem of finding the maximum), the statement of a theorem entry, its worked
  examples and the theorems and lemmas that the site sets as headings are now numbered like the other statements
  and listed in the appendix *Theorems and definitions*.
- **A box for the plain-words summary.** The section *In plain words* of an entry, the idea in everyday terms
  before the definition, is set in a light box with its label on the frame, in the PDF and the EPUB.
- **Each entry starts a page**, in the PDF and the EPUB; the first entry of a group stays under the group's
  heading.
- **Even line spacing.** In 0.20.1 and earlier, a line with a cross-reference number (such as 3.5.7) or a
  pseudocode line number could stand two lines' height below the line above it, because XeTeX gave the small
  number the size of a chapter number. Each TeX pass now runs in a fresh process, and the spacing is even in
  every volume.
- **Fixes.** A theorem whose label stands alone above a numbered list keeps the list, which 0.20.1 ran into one
  paragraph. Links that the site makes from sorting, searching and other areas to `total-order` (an entry on the
  order of events in distributed systems) no longer point to Volume 21, and links from the tree algorithms to
  `tree-hashing` (a hash mode in Volume 23) no longer point there. Mathematics after a procedure name with a
  space before its closing dollar (`UseHint$(h, r) = $ HighBits$(r + z)$`), which the site's KaTeX reads and pandoc
  does not, is set as mathematics again instead of printing its dollars.
- **Volume 0, Guide and Index**, covers the whole set of 6,015 entries, has two new learning paths, *Concurrent
  algorithms* and *Cryptography*, and explains the numbered definitions and the boxes in Chapter 0.1.
- **Volumes 1 to 21** have the same entries under the same numbers as in 0.20.1; their cross-references to entries
  of Volumes 22 and 23 now give entry numbers.
- Volumes 24 to 31 are forthcoming; Volume 0 lists their chapters.

**Files.** For each volume `NN-area`: `handbook-of-algorithms-0.22.0-NN-area.pdf`, `.epub`, and `-tex.tar.gz`
(`main.tex`, `body.tex`, `handbook.sty` and the figures; compile `main.tex` with XeLaTeX or tectonic).
`…-all-pdf.zip` and `…-all-epub.zip` hold every volume; `SHA256SUMS` lists the checksums.

Entry and statement numbers (such as 4.1.12 and Lemma 4.1.12.2) belong to this edition. The entries are the text of
the site; the learner pages were drafted by AI agents and checked as described in `content/PROVENANCE.md`. Text
CC BY-SA 4.0, code MIT. Report errors in an entry at https://github.com/tamnd/algorithm/issues and errors in the
books at https://github.com/tamnd/algorithm-handbook/issues.

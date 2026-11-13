The Handbook of Algorithms, edition 0.25.0: the written areas of [algorithm.tamnd.com](https://algorithm.tamnd.com)
as books, one volume per area, in PDF (7 × 10 in, with bookmarks and links), EPUB 3 and LaTeX source. Built from
[`tamnd/algorithm` v0.25.0](https://github.com/tamnd/algorithm/releases/tag/v0.25.0)
(`595050f399a3231f2360b82fc3a677e72b9323c1`); the edition number follows the release of the site.

| | Volume | Entries | Pages |
|---|---|---:|---:|
| 0 | Guide and Index | the whole set | 1,334 |
| 1 | Foundations | 204 | 1,000 |
| 2 | Techniques | 208 | 1,123 |
| 3 | Data structures | 427 | 3,140 |
| 4 | Sorting | 156 | 910 |
| 5 | Searching | 115 | 646 |
| 6 | Sequences | 120 | 594 |
| 7 | Graphs | 685 | 3,691 |
| 8 | Strings | 216 | 1,256 |
| 9 | Automata and parsing | 270 | 1,604 |
| 10 | Number theory | 238 | 1,438 |
| 11 | Algebra | 328 | 2,122 |
| 12 | Numerical | 465 | 3,024 |
| 13 | Geometry | 280 | 1,794 |
| 14 | Combinatorics | 174 | 877 |
| 15 | Optimization | 301 | 1,764 |
| 16 | Logic and constraints | 325 | 2,106 |
| 17 | Randomized | 141 | 840 |
| 18 | Approximation | 213 | 1,309 |
| 19 | Online and streaming | 195 | 1,135 |
| 20 | Parallel | 128 | 897 |
| 21 | Distributed | 281 | 2,060 |
| 22 | Concurrency | 155 | 2,240 |
| 23 | Cryptography | 390 | 3,136 |
| 24 | Compression and coding | 220 | 1,741 |
| 25 | Machine learning | 419 | 2,978 |
| 26 | Systems | 442 | 3,209 |
| | **All** | **7,096** | **47,968** |

- **Volume 26, Systems, is now complete**, in eight chapters and 442 entries. To *Caching policies* (26.1) this
  edition adds scheduling (the classical CPU scheduling rules and their optimality, fair-share and proportional
  schedulers, flow shops and Johnson's rule, and real-time scheduling: rate-monotonic and earliest-deadline-first,
  the Liu-Layland bound, response-time analysis and the priority protocols), memory allocation (sequential fits,
  segregated lists, the buddy system, slab and arena allocators, fragmentation and Robson's bounds), garbage
  collection (marking, sweeping, copying and compaction, reference counting, generational, incremental and
  concurrent collectors, barriers and the tricolor invariant), database algorithms (joins and the AGM bound, query
  optimization, normal forms and dependencies, concurrency control and isolation levels, logging and recovery),
  networking algorithms (routing protocols, reliable transfer, TCP congestion control, fair queueing and active
  queue management, packet classification and switch scheduling), load balancing and hashing (balls into bins,
  the power of two choices, consistent, rendezvous, jump and Maglev hashing, and the policies of load balancers)
  and rate limiting (token and leaky buckets, GCRA, window counters, traffic shaping and policing). Each page
  says what is proved, under which model, and what is only measured. The volume introduction is rewritten for the
  whole volume, and the opening of each new chapter replaces the short one of 0.24.0.
- **Volume 0, Guide and Index**, covers the whole set of 7,096 entries and has a new learning path,
  *Systems*.
- **Volumes 1 to 25** have the same entries under the same numbers as in 0.24.0; their cross-references to the
  new entries of Volume 26 (the scheduling rules, the buddy system, two-phase locking, consistent hashing, the
  token bucket and others) now give entry numbers. The tables of Exercises 18.3.16 and 22.1.14, which printed as
  plain text, are now set as tables.
- Volumes 27 to 31 are forthcoming; Volume 0 lists their chapters.

**Files.** For each volume `NN-area`: `handbook-of-algorithms-0.25.0-NN-area.pdf`, `.epub`, and `-tex.tar.gz`
(`main.tex`, `body.tex`, `handbook.sty` and the figures; compile `main.tex` with XeLaTeX or tectonic).
`…-all-pdf.zip` and `…-all-epub.zip` hold every volume; `SHA256SUMS` lists the checksums.

Entry and statement numbers (such as 4.1.12 and Lemma 4.1.12.2) belong to this edition. The entries are the text of
the site; the learner pages were drafted by AI agents and checked as described in `content/PROVENANCE.md`. Text
CC BY-SA 4.0, code MIT. Report errors in an entry at https://github.com/tamnd/algorithm/issues and errors in the
books at https://github.com/tamnd/algorithm-handbook/issues.

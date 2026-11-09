A string is a finite sequence of symbols from an alphabet: the letters of a text, the bytes of a file, the bases of a genome, the notes of a melody, the tokens of a program. Every editor has a search command, every compiler reads its input as a string, and every search engine, spam filter, version-control system and DNA sequencer spends much of its time on string problems. The questions are easy to state. Where does this word occur? Which of these thousand words occur? How close are two strings? What is the longest piece that two strings share? Their answers fill a field of their own, with its own data structures and its own mathematics.

This volume collects that field. It starts with finding one pattern in a text and goes on to many patterns, to indexes built once on a text and queried many times, and to matches that allow errors. Two shorter chapters treat palindromes and hashing. The last chapter is the mathematics of words that the others use: periods, rotations, Lyndon words, repetitions and the words that avoid them.

## Why strings get a volume of its own

A string is only an array, and many string algorithms are array algorithms in disguise. What sets strings apart is that a string overlaps with itself. When a pattern fails to match at one place, what it has already matched says where it can match next, and that self-knowledge is the source of most of the ideas in this volume:

- **Preprocessing the pattern.** The [prefix function](/prefix-function/) records how a pattern overlaps itself, and [Knuth-Morris-Pratt](/knuth-morris-pratt/) uses it to read the text once, never moving back.
- **Skipping.** [Boyer-Moore](/boyer-moore/) compares from the end of the pattern and, on large alphabets, looks at only a fraction of the text.
- **Automata.** [Aho-Corasick](/aho-corasick/) turns a set of patterns into one automaton, and the [suffix automaton](/suffix-automaton/) is the smallest automaton for all substrings of a text.
- **Indexing.** The [suffix tree](/suffix-tree/) and the [suffix array](/suffix-array/) answer any substring query in time that depends on the query, not on the text, after one linear-time construction.
- **Dynamic programming.** [Edit distance](/edit-distance/) is the textbook example of a quadratic table, and bit-parallel and filtering methods are what make it fast in practice.
- **Randomization.** A [rolling hash](/polynomial-rolling-hash/) compares two strings in constant time with a small chance of error, and [Rabin-Karp](/rabin-karp/) turns that into a matcher.
- **Combinatorics.** The [Fine and Wilf theorem](/fine-and-wilf-theorem/) and the [Lyndon factorization](/lyndon-factorization/) are facts about words that turn directly into linear-time, constant-space algorithms.

## The chapters

**Chapter 8.1, Exact matching**, finds every occurrence of one pattern in a text. It defines [string matching](/string-matching/) and then builds the two classic families: the left-to-right matchers led by Knuth-Morris-Pratt, with linear worst-case time, and the right-to-left matchers led by Boyer-Moore, which are fast on natural text. It ends with matchers in constant space and with other notions of a match.

**Chapter 8.2, Multiple pattern matching**, searches for a whole set of patterns in one pass. [Aho-Corasick](/aho-corasick/) is the linear-time answer; the Boyer-Moore family extends to sets as [Commentz-Walter](/commentz-walter/) and [Wu-Manber](/wu-manber/), which search tools such as `agrep` and GNU `fgrep` were built on.

**Chapter 8.3, Suffix structures**, spends time once on a fixed text so that later queries are fast. It covers the suffix array and the [LCP array](/lcp-array/), the suffix tree and its linear-time constructions, the suffix automaton, and compressed indexes such as the [FM-index](/fm-index/), which search a text in space close to the size of the compressed text.

**Chapter 8.4, Approximate matching**, allows errors. It defines edit distance and its relatives, computes them with the [Wagner-Fischer](/wagner-fischer-algorithm/) table and its faster forms, searches a text for close matches, and filters candidates so that the expensive check runs rarely.

**Chapter 8.5, Palindromes**, finds the substrings that read the same in both directions. [Manacher's algorithm](/manacher/) finds all of them in linear time, and the [palindromic tree](/palindromic-tree/) stores the distinct ones.

**Chapter 8.6, String hashing**, maps strings to numbers. It analyzes the polynomial hash and its collision bound, uses it for equality tests and for Rabin-Karp, shows how [anti-hash tests](/anti-hash-tests/) defeat a fixed base and modulus, and compares the hash functions used in practice.

**Chapter 8.7, String combinatorics**, studies words for their own sake. [Borders](/border/) and [periods](/string-period/), [primitive words](/primitive-word/) and rotations, [Lyndon words](/lyndon-word/) and [de Bruijn sequences](/de-bruijn-sequence/), [runs](/maximal-repetition/) and [square-free words](/square-free-word/) are the tools behind many algorithms in the earlier chapters.

## How to read this volume

If this is your first course, read these entries in this order: [alphabet](/alphabet/), [border](/border/) and [string period](/string-period/) from Chapter 8.7; [string matching](/string-matching/), [naive string matching](/naive-string-matching/), [the prefix function](/prefix-function/), [Knuth-Morris-Pratt](/knuth-morris-pratt/), [the Z-algorithm](/z-algorithm/) and [Horspool](/boyer-moore-horspool/) from Chapter 8.1; the [polynomial rolling hash](/polynomial-rolling-hash/) and [Rabin-Karp](/rabin-karp/) from Chapter 8.6; [Aho-Corasick](/aho-corasick/) from Chapter 8.2; the [suffix array](/suffix-array/), the [LCP array](/lcp-array/) and the [suffix tree](/suffix-tree/) from Chapter 8.3; [edit distance](/edit-distance/) and [Wagner-Fischer](/wagner-fischer-algorithm/) from Chapter 8.4; and [Manacher's algorithm](/manacher/) from Chapter 8.5. Do the exercises marked ◦ and • at the end of these chapters. That is a complete first unit on strings.

The chapters are not in strict order of dependence. The basic words of Chapter 8.7, such as border and period, are used from the first page of Chapter 8.1, and Rabin-Karp, in Chapter 8.6, is the third classic answer to the problem of Chapter 8.1. Read those entries when the first chapter points to them.

If you already know the basic matchers, start with the opening page of each chapter. It names the groups in the chapter and the order to read them. The entries marked *Advanced* and *Research* are the place to go deeper.

Each entry stands on its own. Its facts box lists what it needs, with the number of the entry where each prerequisite is explained. Entries in other volumes are cited by number too, as [asymptotic notation](/asymptotic-notation/) in Volume 1 and the [trie](/trie/) in Volume 3 are; the number is printed with the link.

## What you need first

You should be able to read a short program and follow a proof by induction. From Volume 1 you need [asymptotic notation](/asymptotic-notation/), [loop invariants](/loop-invariant/) and [amortized analysis](/amortized-cost/), which gives the linear bounds of the left-to-right matchers. From Volume 3 you need the [trie](/trie/), [hash tables](/hash-table/) and the [range minimum query](/range-minimum-query/). Suffix arrays are built with [counting sort](/counting-sort/) and [radix sort](/radix-sort/) from Volume 4 and searched with [binary search](/binary-search/) from Volume 5, and edit distance is computed by [tabulation](/tabulation/), the bottom-up form of dynamic programming from Volume 2. The matching automata need [deterministic finite automata](/deterministic-finite-automaton/) from Volume 9, and the analysis of hashing needs a little modular arithmetic from Volume 10. Nothing else is assumed.

## The exercises

Each chapter ends with exercises in three bands. Exercises marked ◦ check that you read the entries closely; you should be able to do them in a few minutes. Exercises marked • ask you to use an idea in a new place; each takes some thought, and some need a short program. Exercises marked ★ are harder; some are results from research papers. Hints for many exercises are in the appendix *Hints to the exercises* at the end of the volume.

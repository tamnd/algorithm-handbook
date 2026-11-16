Take eight short documents about algorithms and the query "sorted array search". The term sorted is in documents d1, d2, d4 and d8, the term array in d1, d2 and d8, and the term search in d1 and d7. These three lists are all a search engine needs. The Boolean query *sorted AND array AND search* is the intersection of the lists, here d1 alone. A ranked query instead adds up a weight for each term in each document: with [BM25](/bm25/) weights the two best documents are d1 with score 3.0283 and d2 with 1.8893. Five documents match at least one term, but [WAND](/wand/) finds this top 2 after fully scoring only three of them, and it is still exact. A [tiered index](/tiered-index/) with its quick stop rule is faster again and returns d7 in place of d2, which is wrong.

A web engine does the same with lists that can hold millions of entries. The lists are the [inverted index](/inverted-index/), and this chapter is about how to build them, store them in few bits, keep them up to date and answer queries over them. The recurring question is what is exact and what is not. The merge of two lists is linear in their total length; galloping and the method of Baeza-Yates have proved bounds that adapt to the input. MaxScore, WAND and block-max WAND return the exact top $k$ when their score bounds are true bounds, and their speedups are measured. Tiered stops on a budget and static pruning give up exactness for speed. Zipf's and Heaps' laws, which size everything, are fits to data and not theorems.

## What the chapter covers

1. **Documents, terms and lists.** The [incidence matrix](/term-document-incidence-matrix/), the [posting list](/posting-list/), and the empirical laws of [Zipf](/zipfs-law/) and [Heaps](/heaps-law/) for term frequencies and vocabulary growth.
2. **From text to terms.** [Stop-word removal](/stop-word-removal/), [stemming](/stemming/) and the [Porter stemmer](/porter-stemmer/).
3. **Boolean queries and list intersection.** The [merge](/merge-based-list-intersection/), [skip pointers](/skip-pointers/), [small versus small](/small-versus-small-intersection/) with galloping, the [Baeza-Yates method](/baeza-yates-intersection/), [adaptive intersection](/adaptive-set-intersection/) and the older [signature file](/signature-file/).
4. **Phrases and positions.** [Phrase queries](/phrase-query/), the [positional index](/positional-index/) and [positional intersection](/positional-intersection/).
5. **Wildcards and the dictionary.** [Wildcard queries](/wildcard-query/) answered by the [permuterm index](/permuterm-index/) or the [k-gram index](/k-gram-index/), and [front coding](/front-coding/) of the sorted dictionary.
6. **Compressing posting lists.** [Gap encoding](/postings-gap-encoding/), [Simple-9](/simple-9/), [partitioned Elias-Fano](/partitioned-elias-fano/), and [document reordering](/document-identifier-reassignment/) by [recursive graph bisection](/recursive-graph-bisection-reordering/).
7. **Building and updating the index.** [Blocked sort-based indexing](/blocked-sort-based-indexing/), [single-pass in-memory indexing](/single-pass-in-memory-indexing/), [index partitioning](/index-partitioning/), and [dynamic maintenance](/dynamic-index-maintenance/) by [logarithmic merging](/logarithmic-merging/) or [geometric partitioning](/geometric-partitioning/).
8. **Ranked retrieval and safe pruning.** [Ranked retrieval](/ranked-retrieval/), [term-at-a-time](/term-at-a-time-evaluation/) and [document-at-a-time](/document-at-a-time-evaluation/) evaluation, [MaxScore](/maxscore/), WAND and [block-max WAND](/block-max-wand/).
9. **Approximate methods.** The tiered index, the [impact-ordered index](/impact-ordered-index/) and [static index pruning](/static-index-pruning/).

## A first reading

Read these first, in this order:

1. [Posting list](/posting-list/)
2. [Zipf's law](/zipfs-law/)
3. [Stemming](/stemming/)
4. [Posting list intersection](/posting-list-intersection/)
5. [Merge-based list intersection](/merge-based-list-intersection/)
6. [Small versus small intersection](/small-versus-small-intersection/)
7. [Positional index](/positional-index/)
8. [Postings gap encoding](/postings-gap-encoding/)
9. [Single-pass in-memory indexing](/single-pass-in-memory-indexing/)
10. [Logarithmic merging](/logarithmic-merging/)
11. [Ranked retrieval](/ranked-retrieval/)
12. [Document-at-a-time evaluation](/document-at-a-time-evaluation/)
13. [WAND](/wand/)
14. [Tiered index](/tiered-index/)

That path goes from the lists to the queries over them, then to their storage, construction and ranked evaluation. Skip at first the Porter stemmer in detail, the Baeza-Yates and adaptive methods, signature files, the dictionary group, partitioned Elias-Fano, document reordering and geometric partitioning. Come back to block-max WAND after WAND, since it adds one idea, bounds for each block of a list.

## Before you start

The [inverted index](/inverted-index/) itself, built with MapReduce, is in Volume 20; this chapter assumes the idea and goes into its parts. The intersection methods build on [sorted array intersection](/sorted-array-intersection/) from Volume 2 and on [binary search](/binary-search/) and [exponential search](/exponential-search/) from Volume 5. Index construction uses [external merge sort](/external-merge-sort/), the [k-way merge](/k-way-merge/) and [top-k selection](/top-k-selection/) from Volume 4. The compression group uses [variable-byte encoding](/variable-byte-encoding/), [Elias gamma coding](/elias-gamma-coding/) and [delta encoding](/delta-encoding/) from Volume 24, and [Elias-Fano encoding](/elias-fano-encoding/), [bit vectors](/bit-vector/), [hash tables](/hash-table/) and [tries](/trie/) from Volume 3. Logarithmic merging is the [binary counter](/binary-counter-increment/) of Volume 1, and splitting an index across machines is [sharding](/sharding/) from Volume 26. The scores that ranked retrieval computes, [tf-idf](/tf-idf/) and BM25, are defined in the ranking models chapter of this volume. You should be comfortable with sorted lists, logarithms, and counting comparisons.

Real data comes from many sources that were built apart. Two databases describe the same customers with different schemas, spell the same name in three ways, and disagree on an address. Data integration gives such sources one view: it matches their schemas, maps one into the other, and answers queries over a global schema from sources that each hold only part of it. Data cleaning finds the records that refer to the same entity, detects values that break the rules the data should obey, and repairs them or answers queries in spite of them.

The subject matters because most of the effort of using data goes here, before any analysis starts. It also has a solid theory: query answering with views, data exchange and consistent query answering rest on conjunctive queries, containment and the chase, so that the results can be stated and proved exactly.

## What the chapter will cover

The entries of this chapter are being written. They will cover:

1. **Schema matching and mapping.** Schema matching and similarity flooding, schema mappings and their composition, and the global-as-view and local-as-view styles of integration.
2. **Answering queries using views.** Certain answers, the bucket, inverse rules and MiniCon algorithms, and the NP-completeness of rewriting queries using views.
3. **Data exchange.** The data exchange problem, universal solutions, the computation of the core, and weak acyclicity as a condition for the chase to terminate.
4. **Entity resolution.** The Fellegi-Sunter model, blocking and the sorted neighborhood method, R-Swoosh and collective entity resolution.
5. **Constraints, repairs and cleaning.** Discovery of functional dependencies with TANE, conditional functional dependencies and denial constraints, database repairs and consistent query answering, HoloClean, and truth discovery with TruthFinder.

## What to read meanwhile

The theory rests on Chapter 40.1: [conjunctive queries](/conjunctive-query/), the [query containment problem](/query-containment-problem/) and the [Chandra-Merlin theorem](/chandra-merlin-theorem/), the [chase](/chase-algorithm/) and [functional dependencies](/functional-dependency/). The [materialized view](/materialized-view/) of Chapter 40.9 explains views as stored queries, and [provenance semirings](/provenance-semirings/) track where an answer came from.

For entity resolution, string similarity is the [edit distance](/edit-distance/) and the [Jaro-Winkler distance](/jaro-winkler-distance/) of Volume 8, and set similarity is the [Jaccard similarity](/jaccard-similarity/), estimated with [MinHash](/minhash/) and found at scale with [locality-sensitive hashing](/locality-sensitive-hashing/) in Volume 5. The Fellegi-Sunter weights are often fitted with [expectation-maximization](/expectation-maximization/) from Volume 25, and [TF-IDF](/tf-idf/) of Volume 35 weights the words of a record.

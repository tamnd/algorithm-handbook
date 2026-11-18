Removing names from a data set does not make it anonymous. A few ordinary attributes, such as postcode, birth date and sex, are enough to single out most people, and joining them with a public register puts the names back. Sweeney did exactly this with released hospital records, and later work did the same for film ratings and for social networks, where the shape of a person's links is itself an identifier. Anonymization is the problem of changing a data set so that this linkage fails while the data stay useful for analysis.

The classical answer is k-anonymity: generalize or suppress values until every record shares its quasi-identifiers with at least k − 1 others. Finding the cheapest such change is NP-hard, which is why the chapter has approximation algorithms and heuristics. k-anonymity also has known weaknesses, and l-diversity and t-closeness were proposed to fix them. Statistical agencies use a separate family of methods, statistical disclosure control, for tables and microdata. None of these methods gives a guarantee that holds against every background knowledge; that guarantee is the subject of the next chapter, on differential privacy.

## What the chapter will cover

The entries of this chapter are being written. They will cover:

1. **Re-identification.** Quasi-identifiers and linkage attacks, de-anonymization of sparse data sets and of social networks, active attacks on social graphs, and what pseudonymization does and does not hide.
2. **k-anonymity.** Generalization and suppression, Samarati's algorithm, Datafly, Incognito, Mondrian multidimensional partitioning, the NP-hardness of optimal k-anonymity and an O(k) approximation.
3. **Beyond k-anonymity.** l-diversity, t-closeness, m-invariance for republished data, anatomy, km-anonymity for transaction data, k-degree anonymization of graphs and spatial cloaking for locations.
4. **Statistical disclosure control.** Microaggregation and the MDAV heuristic, data swapping, post-randomization, cell suppression and controlled tabular adjustment.
5. **Private record linkage.** Matching records across organizations with Bloom filter encodings instead of the raw identifiers.

## What to read meanwhile

Mondrian partitioning is a [k-d tree](/kd-tree/) of Volume 3 built on the data, and microaggregation is a form of clustering close to [k-means](/k-means/) in Volume 25. An early approximation algorithm for optimal suppression, by Meyerson and Williams, is a greedy cover in the style of [set cover](/set-cover/) in Volume 18. t-closeness measures distance between distributions; the [Kullback-Leibler divergence](/kullback-leibler-divergence/) of Volume 33 is the nearest written relative. Record linkage compares names with the [edit distance](/edit-distance/) and the [Jaro-Winkler distance](/jaro-winkler-distance/) of Volume 8 and encodes them in a [Bloom filter](/bloom-filter/) from Volume 3. Graph de-anonymization starts from [graph isomorphism](/graph-isomorphism-problem/) in Volume 7. When the parties will not share data at all, [secure multiparty computation](/secure-multiparty-computation/) in Volume 23 is the alternative.

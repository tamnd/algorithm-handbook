## What to remember

- **Everything rests on the distance.** A metric index may only compute distances, and the [triangle inequality](/triangle-inequality/) turns stored distances into lower bounds: $d(q, x) \ge |d(q, p) - d(p, x)|$. A similarity that breaks it, such as $1 - \cos$, makes exact pruning unsafe.
- **The scan is the baseline.** [Brute-force search](/brute-force-nearest-neighbor-search/) computes $n$ distances, needs no index and is exact for any distance. Every other method is judged by how many distances it saves and what it gives up.
- **Exact indexes depend on the intrinsic dimension.** Trees such as the [vantage-point tree](/vantage-point-tree/) and the [cover tree](/cover-tree/) prune well when the data has few real degrees of freedom. When the intrinsic dimension is high, they visit almost every point.
- **Approximation breaks the curse of dimensionality.** Asking for a point within a factor $c$ of the nearest lets [locality-sensitive hashing](/locality-sensitive-hashing/) answer with about $n^\rho$ distance computations, where $\rho < 1$ depends on $c$ and the hash family, for example $\rho \le 1/c$ for Hamming distance.
- **Keys and tables shape the collision curve.** A key of $k$ functions makes far pairs rare; $L$ tables make near pairs likely to meet once. The same AND and OR structure drives the banding of [MinHash](/minhash/) signatures.
- **Sketches estimate similarity in a few bytes.** MinHash agrees with probability equal to the Jaccard similarity, and a random hyperplane bit agrees with probability $1 - \theta/\pi$. The error falls like $1/\sqrt{k}$ in the number of hash functions.
- **Joins can be exact and fast.** [Prefix filtering](/prefix-filtering/) only compares sets whose short prefixes share an element, and never misses a pair above the threshold.
- **Graphs win in practice.** [HNSW](/hnsw/) and [DiskANN](/diskann/) walk a proximity graph toward the query. They have no useful worst-case bound but on real data they reach high recall with a small fraction of the distances of a scan.

## The methods side by side

| Method | Answer | Distances per query | Space |
|---|---|---|---|
| Brute-force scan | exact | $n$ | none beyond the data |
| Metric trees: [BK-tree](/bk-tree/), vantage-point tree, [ball tree](/ball-tree/), [M-tree](/m-tree/) | exact | $O(n)$ worst, often far fewer at low intrinsic dimension | $O(n)$ |
| Cover tree | exact | $O(c^{12} \log n)$ | $O(n)$ |
| Locality-sensitive hashing | $(c, r)$-near neighbor, with constant failure probability | $O(n^\rho)$, plus $O(n^\rho \log n)$ hash evaluations | $O(n^{1 + \rho})$ |
| [HNSW](/hnsw/) | approximate, measured by recall | no useful bound; small in practice | $O(n M_0)$ links |
| [Inverted file](/inverted-file-index/) with [product quantization](/product-quantization/) | approximate | $m$ centroids plus about $n_{\text{probe}} n/m$ table lookups | $m \log_2 k^*$ bits per vector |

: Nearest neighbor methods. Here $n$ is the number of points, $c$ in the cover tree row is the expansion constant, $\rho = \ln(1/p_1)/\ln(1/p_2)$, $M_0$ is the number of links on the bottom layer of HNSW, and the inverted file has $m$ cells, of which $n_{\text{probe}}$ are scanned, with codes of $m$ blocks of $k^*$ centroids. Each distance in $\mathbb{R}^d$ costs $O(d)$.

## When to use it

- For a few thousand points, or a batch of queries, scan. A scan written with vector instructions is often as fast as an index at that size, and it is always exact.
- For exact answers in a general metric of low intrinsic dimension, use a vantage-point tree or a ball tree; for words under the edit distance, a BK-tree. Measure the number of distances on real queries before trusting the index.
- For vectors of high dimension in memory, use HNSW and tune the beam width until the recall, measured against a scan on a sample of queries, is high enough.
- When the vectors do not fit in memory, compress them with product quantization behind an inverted file, or keep a graph on disk with DiskANN.
- For near-duplicate documents, take [shingles](/shingling/), then MinHash with banding, or 64-bit [SimHash](/simhash/) fingerprints compared by Hamming distance.
- For all pairs of sets above a Jaccard threshold, use prefix filtering with the positional filter of [PPJoin](/ppjoin/); for sparse vectors under cosine similarity, use [All-Pairs](/allpairs/).
- For the largest inner product, do not use a distance index on the raw vectors; first apply the reduction of [maximum inner product search](/maximum-inner-product-search/) or [asymmetric LSH](/asymmetric-lsh/).

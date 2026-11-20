## What to remember

- A schema mapping is a set of dependencies between two schemas. GAV defines each global relation by a query over the sources and makes query answering an unfolding. LAV defines each source as a view over the global schema, so adding a source is easy and answering a query is a rewriting problem.
- Deciding whether a conjunctive query has an equivalent rewriting over conjunctive views is NP-complete, and some rewriting, if one exists, uses no more view atoms than the query has subgoals. When the sources may be incomplete, the goal is the maximally contained rewriting, which the bucket algorithm, MiniCon and inverse rules all compute.
- The certain answers are the tuples that are answers in every possible target. For unions of conjunctive queries they come from one universal solution: evaluate the query on the chased instance and drop the tuples with nulls. With inequalities it fails, and for some queries the problem is coNP-complete.
- With general target dependencies the chase may not stop, and whether a solution exists is undecidable. Weak acyclicity is a syntactic test that keeps the chase polynomial in the data. The core is the unique smallest universal solution, and it can be computed in polynomial time in the data for the same classes.
- Entity resolution is a pair problem of quadratic size. The Fellegi-Sunter model scores a pair by a likelihood ratio, and its rule leaves the fewest pairs for review among rules with the same error levels, when $m$ and $u$ are known. Blocking and the sorted neighborhood method cut the number of pairs and trade recall for time. R-Swoosh gives the exact answer only when match and merge satisfy the ICAR properties.
- A repair is a minimal change that satisfies the constraints, and there can be exponentially many. Consistent query answering returns what is true in every repair; for primary keys and self-join-free conjunctive queries, each query is first-order rewritable, in polynomial time, or coNP-complete.
- An instance can have exponentially many minimal functional dependencies in the number of attributes, so every discovery method is exponential in the worst case. TANE tests a candidate with stripped partitions and prunes by levels.
- HoloClean, TruthFinder, similarity flooding and collective entity resolution are heuristics. Their entries prove what they compute, not that the result is right; their quality figures are measurements.

## The methods side by side

| Method | Returns | Guarantee | Cost |
|---|---|---|---|
| [Bucket algorithm](/bucket-algorithm/) | union of conjunctive rewritings | maximally contained | exponential in the query size |
| [MiniCon](/minicon-algorithm/) | union of conjunctive rewritings | maximally contained | exponential in the query size, fewer tests |
| [Inverse rules](/inverse-rules-algorithm/) | Datalog program | certain answers under the open world | $O(N^{r(b+1)})$ in the data |
| [Chase and core](/data-exchange-core-computation/) | smallest universal solution | exact, unique up to renaming | $O(m^{w+2})$ for s-t tgds |
| [TANE](/tane-algorithm/) | all minimal FDs | exact | $O((n + m^{2.5})\, 2^m)$ |
| [Sorted neighborhood](/sorted-neighborhood-method/) | candidate pairs | no recall guarantee | $O(p(n \log n + wn))$ |
| [R-Swoosh](/r-swoosh/) | resolved records | exact under ICAR | at most $(n-1)^2$ match calls |
| [Similarity flooding](/similarity-flooding/) | ranked match pairs | heuristic | $O(s(v + e) + v \log v)$ |
| [TruthFinder](/truthfinder/) | a value per object, trust per source | heuristic | $O(knd)$ for $k$ rounds |
| [HoloClean](/holoclean/) | a likely value per noisy cell | heuristic | quadratic in the rows for detection |

: The main algorithms of the chapter with the bounds their entries prove. Here $N$ is the number of source facts, $m$ the size of the instance or the number of attributes as in each entry, and $n$ the number of records or rows. "Heuristic" means no guarantee on quality.

## Choosing a method

To combine sources that change often and may be incomplete, describe them in LAV and answer queries with MiniCon, or with inverse rules when the query is recursive. To build a target database, test the target dependencies for weak acyclicity, chase, and compute the core if people will query the result.

For duplicates, block or sort on two or three keys, measure pair completeness on a labeled sample, then score the candidate pairs with Fellegi-Sunter weights. Use R-Swoosh when a merge can create new matches, and collective resolution when records link to one another.

For errors, write the rules as constraints and find the violations first; that step is exact. Repair by a minimal change when the rules are trusted, use consistent query answering when no single repair should be chosen, and use HoloClean when the data has useful statistics. Treat the result of a heuristic as a proposal to check.

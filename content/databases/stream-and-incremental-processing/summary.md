## What to remember

- A **materialized view** stores the result of a query, and **view maintenance** keeps it equal to its query. Store sums and counts, never averages.
- **Delta rules** come from the algebra. Selection, projection and union are linear; join is bilinear: $\Delta(R \bowtie S) = \Delta R \bowtie S + R \bowtie \Delta S + \Delta R \bowtie \Delta S$ with the old $R$ and $S$. The **counting algorithm** keeps the number of derivations of each tuple. A **self-maintainable** view can be maintained from itself and the change alone, depending on the change, the semantics and the constraints. **Deferred maintenance** computes its delta against old states rebuilt from a log.
- **Higher-order IVM** also stores the deltas of the query as maps of every order, so that an update is a few lookups and additions. **DBSP** states all of this as an algebra of streams: $Q^\Delta = D \circ Q \circ I$, and linear operators are their own incremental form.
- In a recursive view counts never fall to 0. **DRed** overdeletes, rederives and inserts; it is correct for Datalog without negation, but can overdelete far more than the change. **Differential dataflow** keeps differences over partially ordered times, updates and iterations, on the progress tracking of **timely dataflow**.
- A **continuous query** runs forever; a non-monotone one must retract results. **CQL** turns streams into relations with windows, and relations back into streams with Istream, Dstream and Rstream.
- A **watermark** says that no earlier event time will come; it is correct when this is true and heuristic otherwise, and an element below it is late. **Punctuation** marks any pattern of values that will not appear again. The **Dataflow Model** separates what, where, when and how.
- **Sliding-window aggregation** shares work between overlapping windows: **panes** of length $\gcd(R, S)$, **slices** cut at window starts or edges, and **FlatFAT**, a tree of partial aggregates that needs only associativity.
- The **symmetric hash join** emits each result when its second tuple arrives, but keeps both inputs; **XJoin** spills to disk and still emits each pair once.
- **Complex event processing** finds sequences of events within a time window. The selection strategy sets the number of matches: at most $n$ under strict contiguity, up to $(n/k)^k$ under skip till any match. **SASE** matches with stacks of active instances.
- **Chain scheduling** runs the operator with the steepest lower envelope of its progress chart, minimizing queue memory for convex charts, and **asynchronous barrier snapshotting** snapshots a running job consistently, exactly once for internal state with aligned barriers.

## The methods side by side

| Method | Problem | Key idea | Cost or guarantee |
|---|---|---|---|
| [Delta rules](/delta-rules/) and counting | nonrecursive views | linear and bilinear rules, counts of derivations | the delta query |
| [DRed](/dred-algorithm/) | recursive Datalog, no negation | overdelete and rederive | grows with the overdeleted facts |
| [Higher-order IVM](/higher-order-ivm/) | sums of products over joins | store the deltas of the deltas | $2^{k-1}$ map updates for $k$ atoms |
| [DBSP](/dbsp/) | any relational query, recursion | $Q^\Delta = D \circ Q \circ I$ | per step, state in the integrators |
| [Differential dataflow](/differential-dataflow/) | iterative computation | differences over partially ordered times | work in proportion to the differences |
| [CQL](/cql-stream-model/) | queries over streams | windows to relations and back | semantics, not an algorithm |
| [Watermarks](/event-time-watermark/) | out-of-order input | a lower bound on future event times | correct or heuristic |
| [Panes](/panes-window-aggregation/), [slicing](/stream-slicing/) | overlapping windows | aggregate disjoint pieces once | one combine per tuple |
| [FlatFAT](/flatfat/) | any associative aggregate | tree of partials | $O(\log n)$ per update |
| [Symmetric hash join](/symmetric-hash-join/) | joining two streams | insert, then probe the other side | $O(1 + m)$ expected per tuple, all tuples kept |
| [SASE](/sase-event-matching/) | event sequences | stacks of active instances | each match once, at its last event |
| [Chain](/chain-scheduling/) | queue memory | steepest envelope first | optimal for convex charts |
| [Barrier snapshots](/asynchronous-barrier-snapshotting/) | fault tolerance | aligned barriers, no channel state | exactly once for internal state |

: The main methods of the chapter.

## How to choose

Store a view when many queries read it and the base tables change slowly compared with the reads; maintain it incrementally when changes are small, and recompute after a bulk load. For recursive views use DRed when deletions are rare, and differential dataflow or DBSP when updates are frequent. Over streams, choose event time or processing time first, and with event time a watermark and a policy for late data. Use panes or slices when windows overlap and the aggregate is decomposable, and FlatFAT when it is only associative.
